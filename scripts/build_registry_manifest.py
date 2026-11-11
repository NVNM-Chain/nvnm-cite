"""Build the pinned registry-name -> registryId manifest for a network.

READ-ONLY: enumerates registries() (offset-paged), filters to the profile's
creator + the court-name list, hard-verifies the result when the profile
carries manifest_check, and writes
src/nvnm_cite/chain/registry_manifest_<network>.json. Run after any
registry-set change on chain, review the diff, commit.

    uv run python scripts/build_registry_manifest.py --network testnet

Resolves the profile without requiring the manifest file, so the first
manifest for a new profile can be written by this script. A profile with
no manifest_check still writes; review the printed count before committing.
Verification is deliberately loud when manifest_check is set: any duplicate
name within the creator set, any court name missing, an id outside the
pinned range, or a failed record spot-check aborts without writing.
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
from nvnm_cite.chain.registrymap import MANIFEST_SCHEMA
from nvnm_cite.chain.rpc import EvmRpc, RpcError

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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--network", choices=config.network_choices(), required=True)
    ap.add_argument("--rpc", help="override the network's default RPC URL")
    args = ap.parse_args()

    network = config.resolve_profile(args.network)
    rpc = EvmRpc(args.rpc or network.rpc_url(), timeout=30)

    chain_id = rpc.chain_id()
    if chain_id != network.chain_id:
        print(f"FATAL: RPC chain id {chain_id} != {network.chain_id}", file=sys.stderr)
        return 1
    block = rpc.block_number()

    names = court_names()
    print(f"{network.key}: court-name list has {len(names)} registries")

    all_regs = enumerate_registries(rpc)
    print(f"{network.key}: enumerated {len(all_regs)} registries at block {block}")

    matched = [
        r for r in all_regs if r.creator == network.creator and r.name in names
    ]

    errors: list[str] = []
    names_seen: dict[str, list[int]] = {}
    for r in matched:
        names_seen.setdefault(r.name, []).append(r.id)
    dupes = {n: ids for n, ids in names_seen.items() if len(ids) > 1}
    if dupes:
        errors.append(f"duplicate names within the creator set: {dupes}")

    by_name = {r.name: r.id for r in matched}
    check = network.manifest_check
    if check is None:
        print(f"{network.key}: no manifest_check; matched {len(matched)} (review the diff)")
    else:
        if len(matched) != check.count:
            errors.append(f"expected {check.count} registries, matched {len(matched)}")
        ids = sorted(r.id for r in matched)

        if ids and (ids[0] < check.id_min or ids[-1] > check.id_max):
            errors.append(
                f"ids outside expected range {check.id_min}-{check.id_max}: {ids[0]}..{ids[-1]}"
            )

        if len(ids) == check.count and ids != list(range(ids[0], ids[0] + len(ids))):
            errors.append("ids are not contiguous")

        missing = names - set(names_seen)
        if missing:
            errors.append(f"{len(missing)} court names missing on chain: {sorted(missing)[:5]}...")
        rid = by_name.get(check.spot_name)
        if rid is None:
            errors.append(f"spot check: {check.spot_name} not in matched set")
        else:
            try:
                raw = rpc.eth_call(
                    pc.PRECOMPILE_ADDRESS,
                    pc.build_records_query(registry_id=rid, checksum=check.spot_checksum),
                )
                recs, _ = pc.decode_records_result(raw)
            except RpcError as err:
                errors.append(f"spot check {check.spot_name}/{check.spot_checksum}: {err}")
            else:
                if not recs:
                    errors.append(
                        f"spot check {check.spot_name}/{check.spot_checksum}: empty result"
                    )
                elif (
                    check.spot_record_id is not None
                    and recs[0].record_id != check.spot_record_id
                ):
                    errors.append(
                        f"spot check {check.spot_name}/{check.spot_checksum}: "
                        f"recordId {recs[0].record_id} != {check.spot_record_id}"
                    )

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
        "registries": {
            name: {"id": rid} for name, rid in sorted(by_name.items())
        },
    }
    out_path = REPO / "src" / "nvnm_cite" / "chain" / f"registry_manifest_{network.key}.json"
    out_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {out_path.relative_to(REPO)}: {len(by_name)} registries, block {block}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
