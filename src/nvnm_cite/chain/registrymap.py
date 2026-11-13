"""Pinned registry-name -> registryId manifests (the name->id trust anchor).

Under anchoring v1.2.0 registry names are NON-UNIQUE and every chain call
keys on the numeric registryId. Anyone can create a registry named
"us-scotus"; what makes ours authoritative is the PUBLISHED id + creator
pair. These manifests pin that mapping per network profile, generated
read-only by scripts/build_registry_manifest.py from a creator-filtered
enumeration of registries() cross-checked against the court-name list, and
checked in beside the vendored ABI. Runtime resolution goes through the
pinned map, never through a live name search; diff_against_chain() exists
to DETECT drift, not to follow it silently. A manifest whose network key
or chain id disagrees with its profile is refused.

Stdlib only, like the rest of chain/. The profile check imports config
lazily so config can finish loading its JSON before this module runs.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from importlib import resources
from typing import Any

from nvnm_cite.chain import precompile as pc
from nvnm_cite.chain.rpc import RpcError

MANIFEST_SCHEMA = "nvnm-cite-registry-manifest/v1"
_COURTLISTENER_URI = "https://www.courtlistener.com/"


@dataclass(frozen=True)
class RegistryManifest:
    schema: str
    network: str
    chain_id: int
    creator: str
    generated_at: str
    generated_at_block: int
    ids: dict[str, int]  # name -> registryId
    empty: frozenset[str] = frozenset()  # pinned courts with no citation record

    @property
    def names(self) -> dict[int, str]:
        return {rid: name for name, rid in self.ids.items()}

    def registry_id(self, name: str) -> int | None:
        return self.ids.get(name)

    def registry_name(self, registry_id: int) -> str | None:
        return self.names.get(registry_id)

    def all_registries(self) -> dict[str, int]:
        return dict(self.ids)

    def diff_against_chain(self, rpc: Any) -> dict[str, Any]:
        """Re-enumerate registries() (creator-filtered) and diff against the
        pinned map. Returns {added, missing, renamed}; all empty means the
        chain still matches the manifest. Read-only."""
        on_chain: dict[int, str] = {}
        offset = 0
        while True:
            raw = rpc.eth_call(
                pc.PRECOMPILE_ADDRESS,
                pc.build_registries_query(offset=offset, limit=200),
            )
            rows, _ = pc.decode_registries_result(raw)
            if not rows:
                break
            for reg in rows:
                if reg.creator == self.creator:
                    on_chain[reg.id] = reg.name
            offset += len(rows)
            if len(rows) < 200:
                break
        pinned = self.names
        added = {
            rid: name
            for rid, name in on_chain.items()
            if rid not in pinned and name in self.ids
        }
        missing = {rid: name for rid, name in pinned.items() if rid not in on_chain}
        renamed = {
            rid: {"pinned": pinned[rid], "chain": on_chain[rid]}
            for rid in pinned
            if rid in on_chain and on_chain[rid] != pinned[rid]
        }
        return {"added": added, "missing": missing, "renamed": renamed}


def _citation_problem(record: pc.Record, registry_id: int) -> str | None:
    """Why this row is not a section-3 citation record, or None when it is."""
    if record.checksum_algo != "cite-canonical-v1":
        return f"checksumAlgo {record.checksum_algo!r}"
    if record.status != "Active":
        return f"status {record.status!r}"
    if not record.uri.startswith(_COURTLISTENER_URI):
        return f"uri {record.uri!r}"
    try:
        meta = json.loads(record.metadata)
    except json.JSONDecodeError:
        meta = None
    if not isinstance(meta, dict) or ("cluster" not in meta and "cases" not in meta):
        return "metadata is not a citation object"
    if record.registry_id != registry_id:
        return f"registry id {record.registry_id}"
    return None


@dataclass(frozen=True)
class CitationScan:
    """First-page read of court registries.

    ``empty`` names had no record (empty page or a keyed miss). ``errors``
    are a wrong citation shape, or an RPC error that is not a keyed miss.
    One string per failing registry, and the string names it.
    """

    errors: tuple[str, ...]
    empty: tuple[str, ...]


def scan_first_citations(rpc: Any, registries: dict[str, int]) -> CitationScan:
    """Read records(registry_id, limit=1) for each court.

    An empty page and a keyed miss are the same empty outcome. Every row
    in the returned page is checked. A node error is not treated as empty.
    """
    errors: list[str] = []
    empty: list[str] = []
    for name, rid in registries.items():
        try:
            raw = rpc.eth_call(
                pc.PRECOMPILE_ADDRESS,
                pc.build_records_query(registry_id=rid, limit=1),
            )
        except RpcError as err:
            if pc.is_keyed_miss(err):
                rows: list[pc.Record] = []
            else:
                errors.append(f"{name} (#{rid}): {err}")
                continue
        else:
            rows, _ = pc.decode_records_result(raw)
        if not rows:
            empty.append(name)
            continue
        for row in rows:
            problem = _citation_problem(row, rid)
            if problem is not None:
                errors.append(f"{name} (#{rid}): {problem}")
                break
    return CitationScan(errors=tuple(errors), empty=tuple(empty))


def _parse(raw: str) -> RegistryManifest:
    doc = json.loads(raw)
    if doc.get("schema") != MANIFEST_SCHEMA:
        raise ValueError(f"unexpected manifest schema {doc.get('schema')!r}")
    registries = doc["registries"]
    return RegistryManifest(
        schema=doc["schema"],
        network=doc["network"],
        chain_id=doc["chain_id"],
        creator=doc["creator"],
        generated_at=doc["generated_at"],
        generated_at_block=doc["generated_at_block"],
        ids={name: entry["id"] for name, entry in registries.items()},
        empty=frozenset(name for name, entry in registries.items() if entry.get("empty") is True),
    )


@lru_cache(maxsize=4)
def load_manifest(network_key: str) -> RegistryManifest:
    """Load the pinned manifest for a shipped network profile."""
    filename = f"registry_manifest_{network_key}.json"
    raw = resources.files("nvnm_cite.chain").joinpath(filename).read_text()
    manifest = _parse(raw)
    if manifest.network != network_key:
        raise ValueError(
            f"manifest {filename} claims network {manifest.network!r}"
        )
    from nvnm_cite import config

    try:
        profile = config.NETWORKS[network_key]
    except KeyError:
        raise ValueError(f"no profile for manifest network {network_key!r}") from None
    config.match_manifest(
        profile, chain_id=manifest.chain_id, manifest_network=manifest.network
    )
    return manifest
