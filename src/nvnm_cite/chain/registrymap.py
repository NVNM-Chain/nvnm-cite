"""Pinned registry-name -> registryId manifests (the name->id trust anchor).

Under anchoring v1.2.0 registry names are NON-UNIQUE and every chain call
keys on the numeric registryId. Anyone can create a registry named
"us-scotus"; what makes ours authoritative is the PUBLISHED id + creator
pair. These manifests pin that mapping per network profile, generated
read-only by scripts/build_registry_manifest.py from a creator-filtered
enumeration of registries() cross-checked against the court-name list, and
checked in beside the vendored ABI. Runtime resolution goes through the
pinned map, never through a live name search; diff_against_chain() exists
to DETECT drift, not to follow it silently. A manifest that lists registries is refused when its network key or chain
id disagrees with its profile. An empty manifest does not pin a chain id.

Stdlib only, like the rest of chain/. The profile check imports config
lazily so config can finish loading its JSON before this module runs.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Any

from nvnm_cite.chain import precompile as pc

MANIFEST_SCHEMA = "nvnm-cite-registry-manifest/v1"


@dataclass(frozen=True)
class RegistryManifest:
    schema: str
    network: str
    chain_id: int | None
    creator: str
    generated_at: str
    generated_at_block: int
    ids: dict[str, int]  # name -> registryId

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


def _parse(raw: str) -> RegistryManifest:
    doc = json.loads(raw)
    if doc.get("schema") != MANIFEST_SCHEMA:
        raise ValueError(f"unexpected manifest schema {doc.get('schema')!r}")
    raw_chain = doc["chain_id"]
    return RegistryManifest(
        schema=doc["schema"],
        network=doc["network"],
        chain_id=None if raw_chain is None else int(raw_chain),
        creator=doc["creator"],
        generated_at=doc["generated_at"],
        generated_at_block=doc["generated_at_block"],
        ids={name: entry["id"] for name, entry in doc["registries"].items()},
    )


def _read_packaged(network_key: str) -> tuple[str, str]:
    filename = f"registry_manifest_{network_key}.json"
    raw = resources.files("nvnm_cite.chain").joinpath(filename).read_text()
    return filename, raw


def _agree(network: Any, manifest: RegistryManifest, filename: str) -> RegistryManifest:
    if manifest.network != network.key:
        raise ValueError(f"manifest {filename} claims network {manifest.network!r}")
    if not manifest.ids:
        # An empty map does not pin a chain id, so the identity env can be
        # filled later without replacing this file.
        return manifest
    from nvnm_cite import config

    if network.chain_id is None:
        raise ValueError(
            f"{network.profile_env('CHAIN_ID')} is not set; the manifest lists registries"
        )
    if manifest.chain_id is None:
        raise ValueError(f"manifest {filename} lists registries but has no chain_id")
    if manifest.creator != network.creator:
        raise ValueError(
            f"manifest {filename} creator {manifest.creator!r} is not profile creator {network.creator!r}"
        )
    config.match_manifest(
        network, chain_id=manifest.chain_id, manifest_network=manifest.network
    )
    return manifest


@lru_cache(maxsize=4)
def _load_pinned(network_key: str) -> RegistryManifest:
    filename, raw = _read_packaged(network_key)
    from nvnm_cite import config

    return _agree(config.resolve_profile(network_key), _parse(raw), filename)


def load_manifest(network_key: str) -> RegistryManifest:
    """Load the pinned manifest for a network profile.

    A packaged manifest that lists registries is cached and ignores
    ``NVNM_MANIFEST_PATH``. A packaged manifest with no registries reads
    that path when it is set, so a generated file can fill the hole
    without a new image.
    """
    from nvnm_cite import config

    filename, raw = _read_packaged(network_key)
    if _parse(raw).ids:
        return _load_pinned(network_key)
    network = config.resolve_profile(network_key)
    override = os.environ.get("NVNM_MANIFEST_PATH", "").strip()
    if not override:
        return _agree(network, _parse(raw), filename)
    path = Path(override)
    if not path.is_file():
        raise ValueError(f"NVNM_MANIFEST_PATH does not name a file: {override}")
    return _agree(network, _parse(path.read_text()), path.name)
