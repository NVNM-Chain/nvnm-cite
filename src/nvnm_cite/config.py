"""Project configuration from .env and the process environment.

Values are loaded, never logged. Code in this package must not print
private keys or token values; callers get parsed values only.

Network identity is a JSON profile in ``nvnm_cite.networks``. ``get_network()``
resolves an explicit argument, then ``NVNM_NETWORK``, then mainnet. A field
the JSON leaves empty is filled from ``NVNM_<PROFILE>_<FIELD>``; a
field the JSON sets is kept. ``rpc_url()`` still prefers ``rpc_env`` for the
server's call when ``rpc_default`` is already set. A manifest that lists
registries must name the same network and chain id. An empty manifest does
not. Signing reads the env var named by ``key_env`` and never another
profile's key.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, replace
from importlib import resources
from pathlib import Path

from nvnm_cite.chain.signer import parse_private_key

DEFAULT_NETWORK = "mainnet"

_PROFILE_FIELDS = (
    "key",
    "chain_id",
    "network_name",
    "rpc_default",
    "rpc_env",
    "explorer",
    "gas_token",
    "label",
    "key_env",
    "creator",
    "fee_token",
    "fee_token_decimals",
)


@dataclass(frozen=True)
class Network:
    key: str
    chain_id: int | None
    network_name: str
    rpc_default: str
    rpc_env: str  # env var that overrides rpc_default
    explorer: str
    gas_token: str
    label: str
    key_env: str  # env var holding this profile's signing key
    creator: str
    fee_token: str
    fee_token_decimals: int

    def rpc_url(self) -> str:
        return os.environ.get(self.rpc_env, self.rpc_default)

    def profile_env(self, field: str) -> str:
        """``NVNM_MAINNET_CHAIN_ID`` for key ``mainnet`` and field ``CHAIN_ID``."""
        return f"NVNM_{self.key.upper()}_{field}"


def _load_profiles() -> dict[str, Network]:
    root = resources.files("nvnm_cite.networks")
    found: dict[str, Network] = {}
    for path in sorted(root.iterdir(), key=lambda item: item.name):
        if not path.name.endswith(".json"):
            continue
        doc = json.loads(path.read_text())
        missing = [field for field in _PROFILE_FIELDS if field not in doc]
        if missing:
            raise ValueError(f"{path.name} missing {missing}")
        key = doc["key"]
        if key != path.name[: -len(".json")]:
            raise ValueError(f"{path.name} declares key {key!r}")
        if key in found:
            raise ValueError(f"duplicate network profile {key!r}")
        raw_chain = doc["chain_id"]
        chain_id = None if raw_chain is None else int(raw_chain)
        found[key] = Network(
            key=key,
            chain_id=chain_id,
            network_name=doc["network_name"],
            rpc_default=doc["rpc_default"],
            rpc_env=doc["rpc_env"],
            explorer=doc["explorer"],
            gas_token=doc["gas_token"],
            label=doc["label"],
            key_env=doc["key_env"],
            creator=doc["creator"],
            fee_token=doc["fee_token"],
            fee_token_decimals=int(doc["fee_token_decimals"]),
        )
    if not found:
        raise ValueError("no network profiles in nvnm_cite.networks")
    if DEFAULT_NETWORK not in found:
        raise ValueError(f"default network {DEFAULT_NETWORK!r} has no profile")
    return found


NETWORKS: dict[str, Network] = _load_profiles()
TESTNET = NETWORKS["testnet"]
DEVNET = NETWORKS["devnet"]

# Derived from the testnet profile. Callers that only need the chain id.
TESTNET_CHAIN_ID = TESTNET.chain_id
TESTNET_EXPLORER = TESTNET.explorer


def network_choices() -> list[str]:
    """Profile keys, for argparse ``choices``."""
    return sorted(NETWORKS)


def match_manifest(network: Network, chain_id: int, manifest_network: str) -> None:
    """Refuse a profile whose pinned manifest names another network or chain."""
    if manifest_network != network.key or chain_id != network.chain_id:
        raise ValueError(
            f"profile {network.key!r} (chain {network.chain_id}) does not match "
            f"manifest {manifest_network!r} (chain {chain_id})"
        )


def _fill_empty(network: Network) -> Network:
    """Fill JSON fields that were left empty. A value in the file stays."""
    updates: dict[str, object] = {}
    if network.chain_id is None:
        chain_env = network.profile_env("CHAIN_ID")
        chain_raw = os.environ.get(chain_env, "").strip()
        if chain_raw:
            try:
                chain_id = int(chain_raw, 10)
            except ValueError as exc:
                raise ValueError(f"{chain_env} must be a positive integer") from exc
            if chain_id <= 0:
                raise ValueError(f"{chain_env} must be a positive integer")
            updates["chain_id"] = chain_id
    if not network.rpc_default:
        # rpc_default is what the wallet is told. Copy it only when the file
        # had no public URL. A set rpc_default stays; rpc_url() still prefers rpc_env.
        rpc = os.environ.get(network.rpc_env, "").strip()
        if rpc:
            updates["rpc_default"] = rpc
    for field, attr in (("NETWORK_NAME", "network_name"), ("EXPLORER", "explorer")):
        if getattr(network, attr):
            continue
        value = os.environ.get(network.profile_env(field), "").strip()
        if value:
            updates[attr] = value
    if not updates:
        return network
    return replace(network, **updates)


def resolve_profile(name: str | None = None) -> Network:
    """Resolve a profile without reading its manifest.

    The manifest builder uses this so it can write the first manifest for a
    new profile. Every other entry point uses ``get_network()``. Empty
    profile fields are filled from env. Set fields are unchanged.
    """
    chosen = name or os.environ.get("NVNM_NETWORK") or DEFAULT_NETWORK
    try:
        network = NETWORKS[chosen]
    except KeyError:
        raise ValueError(
            f"unknown network {chosen!r}; expected one of {sorted(NETWORKS)}"
        ) from None
    return _fill_empty(network)


def get_network(name: str | None = None) -> Network:
    """Resolve a profile and load its manifest.

    Precedence: explicit arg, then ``NVNM_NETWORK``, then mainnet. A manifest
    that lists registries must agree on network key and chain id. An empty
    manifest loads either way.
    """
    network = resolve_profile(name)
    # Lazy import: registrymap checks the profile, so this module must finish
    # loading before that import runs.
    from nvnm_cite.chain.registrymap import load_manifest

    load_manifest(network.key)
    return network


def load_dotenv(path: Path | None = None) -> None:
    """Overlay .env values into os.environ (existing variables win)."""
    env_path = path or Path.cwd() / ".env"
    if not env_path.is_file():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _env_private_key(env_name: str) -> int:
    raw = os.environ.get(env_name, "")
    if not raw:
        raise RuntimeError(
            f"{env_name} is not set; copy .env.example to .env and fill it in"
        )
    return parse_private_key(raw)


def signing_context(network: Network) -> tuple[int, int]:
    """The single gate for transaction signing: returns (private_key, chain_id).

    The key is the env var named by ``network.key_env``. A key set for
    another profile is never read. A profile with no chain id refuses, so a
    receipt is never signed for an unknown chain.
    """
    if network.chain_id is None:
        raise RuntimeError(f"{network.profile_env('CHAIN_ID')} is not set; refusing to sign")
    return _env_private_key(network.key_env), network.chain_id
