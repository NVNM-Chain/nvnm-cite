"""Build the reporter-edition -> registry inference table for the normalizer.

Generates src/nvnm_cite/normalizer/reporter_registries.json from the mainnet
bulk-load export (data/mainnet-full-export/, byte-validated against the
chain): for every reporter edition observed in the corpus, if ONE registry
dominates it overwhelmingly, a citation in that edition can be routed there
WITHOUT a court parenthetical. This powers jurisdiction.py's rule 5
(reporter-edition inference) — the mapper still lets an explicit court
parenthetical override the table, so the table is a default, not a guess.

Guards (an edition is included only if ALL hold):
- total corpus records >= MIN_RECORDS (noise floor);
- the top registry holds >= DOMINANCE of them (stray records in other
  registries are CourtListener attribution noise, e.g. 3 A.D.2d rows filed
  under New Jersey courts against 177,540 in us-nyappdiv);
- exactly ONE reporters-db reporter carries the edition (excludes shared
  nominatives like "Cranch", which is both scotus_early and a D.C. reporter);
- not a vendor identifier (WL / LEXIS): those are never registry keys;
- the registry exists in the pinned mainnet manifest.

Curated adjudications (DECISIONS 2026-08-01) applied on top:
- EXCLUDED editions that are jurisdictionally multi-court in reality even
  though the corpus happens to hold them in one registry;
- ADDED definitionally single-court editions the corpus lacks entirely.

Run:  uv run python scripts/build_reporter_map.py
Review the diff, then commit. Regenerate whenever the corpus scope changes.
"""

from __future__ import annotations

import gzip
import json
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from reporters_db import REPORTERS

from nvnm_cite.chain.registrymap import load_manifest

REPO = Path(__file__).resolve().parent.parent
EXPORT = REPO / "data" / "mainnet-full-export"
OUT = REPO / "src" / "nvnm_cite" / "normalizer" / "reporter_registries.json"

MIN_RECORDS = 100
DOMINANCE = 0.995

# Same-state family candidates (rule 5b, 1.3.0): an edition that fails the
# dominance guard still gets an entry when EVERY registry holding >= 1% of
# its records sits in ONE state — the corpus itself proves every plausible
# home of the edition, so the verifier can sweep the family with keyed
# reads instead of refusing (measured: "Cal. App. 5th" splits 71/29 between
# us-calctapp5d and us-calctapp from CourtListener attribution drift).
FAMILY_MIN_SHARE = 0.01
FAMILY_CAP = 5

# The corpus splits some intermediate courts between a parent registry and
# per-district ones (granularity inconsistency, DECISIONS 2026-08-01
# findings; measured misroutes on the 2026-08-09 state corpus run). A
# lookup routed to the parent sweeps the districts too. Members are
# validated against the manifest at build time.
REGISTRY_FAMILIES = {
    "us-texapp": [f"us-txctapp{n}" for n in range(1, 15)],
    "us-calctapp": [f"us-calctapp{n}d" for n in range(1, 7)],
    "us-fladistctapp": [f"us-fladistctapp{n}" for n in range(1, 7)],
}

# Jurisdictionally multi-court in reality; corpus dominance is an artifact
# of what happens to be loaded. Mapping them would be a genuine guess.
EXCLUDE = {
    "M.J.",  # Military Justice Reporter: CAAF + four service courts
    "Fla. L. Weekly Supp.",  # weekly covering many Florida trial courts
}

# Definitionally single-court editions the corpus lacks (CourtListener stores
# other forms), mapped so the citation at least routes to the right registry.
CURATED_ADD = {
    "T.C.": "us-tax",  # bound Tax Court reports; corpus holds T.C. No./Memo.
}


def is_vendor(edition: str) -> bool:
    # Only the identifiers with no presence in the registry key space:
    # Westlaw numbers and the generic/federal LEXIS families are absent from
    # the corpus entirely. Court-specific LEXIS editions ("La. LEXIS",
    # "N.Y. App. Div. LEXIS", ...) are 3.28M parallel keys ON CHAIN
    # (27% of the corpus), so they map and verify like any other reporter —
    # the dominance guards apply to them unchanged.
    return edition in ("WL", "LEXIS")


def rdb_entries(edition: str) -> list[tuple[str, str | None]]:
    return [
        (canon, entry.get("cite_type"))
        for canon, entries in REPORTERS.items()
        for entry in entries
        if edition in entry.get("editions", {})
    ]


def scan_corpus() -> dict[str, Counter]:
    ed_regs: dict[str, Counter] = defaultdict(Counter)
    t0 = time.monotonic()
    n = 0
    for f in sorted(EXPORT.glob("tranche-*/*.jsonl.gz")):
        with gzip.open(f, "rt") as fh:
            for line in fh:
                # Export lines have sorted keys: "checksum" first, "registry"
                # in the tail. Manual slicing; json.loads as the fallback.
                try:
                    cs = line[13 : line.index('","checksumAlgo"')]
                    rpos = line.rindex('"registry":"') + 12
                    reg = line[rpos : line.index('"', rpos)]
                except ValueError:
                    rec = json.loads(line)
                    cs, reg = rec["checksum"], rec["registry"]
                parts = cs.split(" ")
                if len(parts) < 3:
                    continue
                ed_regs[" ".join(parts[1:-1])][reg] += 1
                n += 1
    print(f"scanned {n:,} records in {time.monotonic() - t0:.0f}s")
    return ed_regs


def main() -> int:
    manifest = load_manifest("mainnet")
    manifest_names = set(manifest.all_registries())
    ed_regs = scan_corpus()

    table: dict[str, dict] = {}
    for ed, regs in sorted(ed_regs.items()):
        if is_vendor(ed) or ed in EXCLUDE:
            continue
        total = sum(regs.values())
        top_reg, top_n = max(regs.items(), key=lambda kv: kv[1])
        if total < MIN_RECORDS or top_n / total < DOMINANCE:
            continue
        if top_reg not in manifest_names:
            continue
        entries = rdb_entries(ed)
        if len(entries) != 1 or entries[0][1] in ("specialty_west", "specialty_lexis"):
            continue
        table[ed] = {
            "registry": top_reg,
            "records": top_n,
            "share": round(top_n / total, 5),
            "cite_type": entries[0][1],
        }
    for ed, reg in CURATED_ADD.items():
        if reg not in manifest_names:
            print(f"FATAL: curated {ed!r} -> {reg} not in manifest", file=sys.stderr)
            return 1
        table[ed] = {"registry": reg, "records": 0, "share": None, "cite_type": "curated"}

    # Same-state families (rule 5b) for editions the dominance guard keeps
    # out of the table. Same entry guards (non-vendor, not excluded, one
    # reporters-db reporter, noise floor); the extra condition is that every
    # >= FAMILY_MIN_SHARE registry maps to ONE state via courts-db.
    from nvnm_cite.normalizer.jurisdiction import _court_state_table

    court_state = _court_state_table()
    families: dict[str, dict] = {}
    for ed, regs in sorted(ed_regs.items()):
        if ed in table or is_vendor(ed) or ed in EXCLUDE:
            continue
        total = sum(regs.values())
        if total < MIN_RECORDS:
            continue
        entries = rdb_entries(ed)
        if len(entries) != 1 or entries[0][1] in ("specialty_west", "specialty_lexis"):
            continue
        candidates = [
            (reg, n)
            for reg, n in regs.most_common()
            if n / total >= FAMILY_MIN_SHARE and reg in manifest_names
        ][:FAMILY_CAP]
        if not candidates:
            continue
        states = {court_state.get(reg.removeprefix("us-")) for reg, _ in candidates}
        if len(states) != 1 or None in states:
            continue  # multi-state (regional reporters) or non-state courts: refuse
        families[ed] = {
            "state": states.pop(),
            "candidates": [
                {"registry": reg, "records": n, "share": round(n / total, 5)}
                for reg, n in candidates
            ],
        }

    registry_families: dict[str, list[str]] = {}
    for parent, children in REGISTRY_FAMILIES.items():
        if parent not in manifest_names:
            print(f"FATAL: registry family parent {parent} not in manifest", file=sys.stderr)
            return 1
        present = [c for c in children if c in manifest_names]
        missing = sorted(set(children) - set(present))
        if missing:
            print(f"note: {parent} family members not in manifest, dropped: {missing}")
        registry_families[parent] = present

    # LEXIS editions with ANY corpus presence: these are real (parallel) keys
    # on chain, so the normalizer treats them as reporters, not vendor
    # identifiers — even when dominance keeps them out of the inference table
    # (an explicit court parenthetical can still map them).
    lexis_present = sorted(
        ed for ed in ed_regs if ed.endswith(" LEXIS") and sum(ed_regs[ed].values()) > 0
    )

    doc = {
        "schema": "nvnm-cite-reporter-registries/v1",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "data/mainnet-full-export (mainnet corpus, manifest block "
        f"{manifest.generated_at_block})",
        "guards": {
            "min_records": MIN_RECORDS,
            "dominance": DOMINANCE,
            "single_reporters_db_entry": True,
            "vendor_excluded": True,
            "family_min_share": FAMILY_MIN_SHARE,
            "family_cap": FAMILY_CAP,
            "family_same_state": True,
        },
        "curated_excluded": sorted(EXCLUDE),
        "curated_added": sorted(CURATED_ADD),
        "lexis_editions_present": lexis_present,
        "editions": dict(sorted(table.items())),
        "families": dict(sorted(families.items())),
        "registry_families": dict(sorted(registry_families.items())),
    }
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(
        f"wrote {OUT.relative_to(REPO)}: {len(table)} editions, "
        f"{len(families)} families, {len(registry_families)} registry families"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
