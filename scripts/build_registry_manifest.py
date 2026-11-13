"""Build the pinned registry-name -> registryId manifest for a network.

READ-ONLY: enumerates registries() (offset-paged), filters to the profile's
creator + the court-name list, hard-verifies the match, and writes
src/nvnm_cite/chain/registry_manifest_<network>.json. Run after any
registry-set change on chain, review the diff, commit.

    uv run python scripts/build_registry_manifest.py --network testnet

Resolves the profile without requiring the manifest file, so the first
manifest for a new profile can be written by this script. Review the
printed count before committing. Any duplicate name within the creator
set, or any court name missing, aborts without writing. A matched
registry with no citation record is marked
``"empty": true`` and the manifest is still written. A first page that
is not a citation record aborts without writing.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from nvnm_cite import config
from nvnm_cite.chain import precompile as pc
from nvnm_cite.chain.registrymap import MANIFEST_SCHEMA, scan_first_citations
from nvnm_cite.chain.rpc import EvmRpc

REPO = Path(__file__).resolve().parent.parent
EXPORT_REGISTRIES = REPO / "data" / "mainnet-full-export" / "registries.json"


def court_names() -> set[str]:
    """Names to pin: the local export when present, else the testnet manifest."""
    if EXPORT_REGISTRIES.exists():
        return {entry["name"] for entry in json.loads(EXPORT_REGISTRIES.read_text())}
    from nvnm_cite.chain.registrymap import load_manifest

    return set(load_manifest("testnet").ids)


def enumerate_registries(rpc: EvmRpc) -> list[pc.Registry]:
    out: list[pc.Registry] = []
    offset = 0
    while True:
        raw = rpc.eth_call(
            pc.PRECOMPILE_ADDRESS, pc.build_registries_query(offset=offset, limit=200)
        )
        rows, _ = pc.decode_registries_result(raw)
        if not rows:
            break
        out.extend(rows)
        offset += len(rows)
        if len(rows) < 200:
            break
    return out


def registry_entries(ids: dict[str, int], empty: tuple[str, ...]) -> dict[str, dict]:
    """Sorted manifest entries. An empty court is marked and warned."""
    registries: dict[str, dict] = {}
    for name, rid in sorted(ids.items()):
        entry: dict = {"id": rid}
        if name in empty:
            print(
                f"warning: {name} (#{rid}): no citation record; marked empty",
                file=sys.stderr,
            )
            entry["empty"] = True
        registries[name] = entry
    return registries


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--network", choices=config.network_choices(), required=True)
    ap.add_argument("--rpc", help="override the network's default RPC URL")
    args = ap.parse_args()

    network = config.resolve_profile(args.network)
    rpc = EvmRpc(
        args.rpc or network.rpc_url(),
        timeout=30,
        max_attempts=8,
        backoff_base=1.0,
        backoff_cap=30.0,
        on_retry=lambda method, attempt, exc: print(
            f"  transient {type(exc).__name__} on {method} (attempt {attempt}); retrying",
            flush=True,
        ),
    )

    chain_id = rpc.chain_id()
    if chain_id != network.chain_id:
        print(f"FATAL: RPC chain id {chain_id} != {network.chain_id}", file=sys.stderr)
        return 1
    block = rpc.block_number()

    names = court_names()
    print(f"{network.key}: court-name list has {len(names)} registries")

    all_regs = enumerate_registries(rpc)
    print(f"{network.key}: enumerated {len(all_regs)} registries at block {block}")

    registry_by_name: dict[str, int] = {}
    dupes: dict[str, list[int]] = {}

    for registry in all_regs:
        if registry.creator != network.creator or registry.name not in names:
            continue

        prior = registry_by_name.get(registry.name)
        if prior is None:
            registry_by_name[registry.name] = registry.id
            continue
        dupes.setdefault(registry.name, [prior]).append(registry.id)

    errors: list[str] = []
    if dupes:
        errors.append(f"duplicate names within the creator set: {dupes}")

    missing = sorted(names.difference(registry_by_name))
    if missing:
        errors.append(f"{len(missing)} court names missing on chain: {missing[:5]}...")

    scan = scan_first_citations(rpc, registry_by_name)
    errors.extend(scan.errors)

    if errors:
        for e in errors:
            print(f"FATAL: {e}", file=sys.stderr)
        return 1

    manifest = {
        "schema": MANIFEST_SCHEMA,
        "network": network.key,
        "chain_id": network.chain_id,
        "creator": network.creator,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_at_block": block,
        "registries": registry_entries(registry_by_name, scan.empty),
    }
    out_path = REPO / "src" / "nvnm_cite" / "chain" / f"registry_manifest_{network.key}.json"
    out_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {out_path.relative_to(REPO)}: {len(registry_by_name)} registries, block {block}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
