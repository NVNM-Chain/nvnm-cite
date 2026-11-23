"""Network profiles and per-profile signing keys."""

import json
from dataclasses import replace

import pytest

from nvnm_cite import config
from nvnm_cite.chain.registrymap import load_manifest
from nvnm_cite.verifier.check import NOT_COVERED, check_text
from nvnm_cite.webapp.service import StatusService

_MAINNET_ENV = (
    "NVNM_NETWORK",
    "NVNM_MAINNET_CHAIN_ID",
    "NVNM_MAINNET_RPC",
    "NVNM_MAINNET_EXPLORER",
    "NVNM_MAINNET_NETWORK_NAME",
    "NVNM_MAINNET_CREATOR",
    "NVNM_MAINNET_FEE_TOKEN",
    "NVNM_MAINNET_KEY",
    "NVNM_MANIFEST_PATH",
)


def _clear_mainnet(monkeypatch):
    for name in _MAINNET_ENV:
        monkeypatch.delenv(name, raising=False)


def test_profiles_pin_chain_constants():
    assert set(config.NETWORKS) == {"testnet", "devnet", "mainnet"}
    assert config.network_choices() == ["devnet", "mainnet", "testnet"]
    assert config.TESTNET.chain_id == 787223
    assert config.TESTNET.network_name == "nvnm-next-testnet-1"
    assert config.TESTNET.gas_token == "nUSD"
    assert config.TESTNET.key_env == "NVNM_TESTNET_KEY"
    assert config.TESTNET.rpc_env == "NVNM_TESTNET_RPC"
    assert config.TESTNET.fee_token_decimals == 6
    assert config.TESTNET.manifest_check is not None
    assert config.TESTNET.manifest_check.count == 2114
    assert config.TESTNET.manifest_check.spot_name == "us-scotus"
    assert config.DEVNET.chain_id == 787222
    assert config.DEVNET.network_name == "nvnm-next-devnet-1"
    assert config.DEVNET.gas_token == "nUSD"
    assert config.DEVNET.rpc_env == "NVNM_DEVNET_RPC"
    assert config.DEVNET.key_env == "NVNM_DEVNET_KEY"
    assert config.DEVNET.fee_token == config.TESTNET.fee_token
    assert config.NETWORKS["mainnet"].chain_id is None
    assert config.NETWORKS["mainnet"].key_env == "NVNM_MAINNET_KEY"
    assert config.NETWORKS["mainnet"].profile_env("CHAIN_ID") == "NVNM_MAINNET_CHAIN_ID"
    assert config.NETWORKS["mainnet"].fee_token == config.TESTNET.fee_token


def test_get_network_precedence(monkeypatch):
    _clear_mainnet(monkeypatch)
    assert config.get_network() is config.NETWORKS["mainnet"]
    monkeypatch.setenv("NVNM_NETWORK", "devnet")
    assert config.get_network() is config.DEVNET
    assert config.get_network("testnet") is config.TESTNET  # explicit arg wins
    with pytest.raises(ValueError):
        config.get_network("no-such")


def test_filled_json_fields_ignore_env(monkeypatch):
    _clear_mainnet(monkeypatch)
    monkeypatch.setenv("NVNM_TESTNET_RPC", "http://localhost:9999")
    network = config.get_network("testnet")
    assert network is config.TESTNET
    assert network.chain_id == 787223
    assert network.rpc_default == "https://rpc.nvnm.testnet.nvnmchain.io"
    assert network.rpc_url() == "http://localhost:9999"
    monkeypatch.setenv("NVNM_MAINNET_CREATOR", "nvnm1other")
    monkeypatch.setenv("NVNM_MAINNET_FEE_TOKEN", "0x11")
    mainnet = config.get_network("mainnet")
    assert mainnet.creator == config.TESTNET.creator
    assert mainnet.fee_token == config.TESTNET.fee_token


def test_rpc_env_override(monkeypatch):
    monkeypatch.setenv("NVNM_TESTNET_RPC", "http://localhost:9999")
    assert config.TESTNET.rpc_url() == "http://localhost:9999"
    monkeypatch.delenv("NVNM_TESTNET_RPC", raising=False)
    assert config.TESTNET.rpc_url() == "https://rpc.nvnm.testnet.nvnmchain.io"
    monkeypatch.setenv("NVNM_DEVNET_RPC", "http://localhost:9998")
    assert config.DEVNET.rpc_url() == "http://localhost:9998"
    monkeypatch.delenv("NVNM_DEVNET_RPC", raising=False)
    assert config.DEVNET.rpc_url() == "https://rpc.nvnm.canary.mantrachain.dev"


def test_signing_context_testnet(monkeypatch):
    monkeypatch.setenv("NVNM_TESTNET_KEY", "0x" + "11" * 32)
    key, chain_id = config.signing_context(config.TESTNET)
    assert key == int("11" * 32, 16)
    assert chain_id == 787223


def test_signing_context_devnet(monkeypatch):
    monkeypatch.delenv("NVNM_TESTNET_KEY", raising=False)
    monkeypatch.setenv("NVNM_DEVNET_KEY", "0x" + "33" * 32)
    key, chain_id = config.signing_context(config.DEVNET)
    assert key == int("33" * 32, 16)
    assert chain_id == 787222


def test_devnet_signing_does_not_reuse_testnet_key(monkeypatch):
    monkeypatch.setenv("NVNM_TESTNET_KEY", "0x" + "11" * 32)
    monkeypatch.delenv("NVNM_DEVNET_KEY", raising=False)
    with pytest.raises(RuntimeError, match="NVNM_DEVNET_KEY is not set"):
        config.signing_context(config.DEVNET)


def test_testnet_signing_does_not_reuse_devnet_key(monkeypatch):
    monkeypatch.setenv("NVNM_DEVNET_KEY", "0x" + "33" * 32)
    monkeypatch.delenv("NVNM_TESTNET_KEY", raising=False)
    with pytest.raises(RuntimeError, match="NVNM_TESTNET_KEY is not set"):
        config.signing_context(config.TESTNET)


def test_mainnet_boots_unconfigured(monkeypatch):
    _clear_mainnet(monkeypatch)
    network = config.get_network("mainnet")
    assert network is config.NETWORKS["mainnet"]
    assert network.chain_id is None
    assert network.rpc_url() == ""
    manifest = load_manifest("mainnet")
    assert manifest.ids == {}
    assert manifest.chain_id is None


def test_mainnet_env_overlay(monkeypatch):
    _clear_mainnet(monkeypatch)
    monkeypatch.setenv("NVNM_MAINNET_CHAIN_ID", "424242")
    monkeypatch.setenv("NVNM_MAINNET_RPC", "http://127.0.0.1:9")
    monkeypatch.setenv("NVNM_MAINNET_EXPLORER", "http://explorer.example")
    monkeypatch.setenv("NVNM_MAINNET_NETWORK_NAME", "nvnm-mainnet-1")
    network = config.get_network("mainnet")
    assert network.chain_id == 424242
    assert network.rpc_url() == "http://127.0.0.1:9"
    assert network.rpc_default == "http://127.0.0.1:9"
    assert network.explorer == "http://explorer.example"
    assert network.network_name == "nvnm-mainnet-1"
    assert network.creator == config.TESTNET.creator
    assert load_manifest("mainnet").ids == {}


def test_mainnet_chain_id_must_be_a_positive_integer(monkeypatch):
    _clear_mainnet(monkeypatch)
    monkeypatch.setenv("NVNM_MAINNET_CHAIN_ID", "nope")
    with pytest.raises(ValueError, match="positive integer"):
        config.get_network("mainnet")
    monkeypatch.setenv("NVNM_MAINNET_CHAIN_ID", "0")
    with pytest.raises(ValueError, match="positive integer"):
        config.get_network("mainnet")


def test_mainnet_manifest_path_must_match_chain_id(monkeypatch, tmp_path):
    _clear_mainnet(monkeypatch)
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps({
        "schema": "nvnm-cite-registry-manifest/v1",
        "network": "mainnet",
        "chain_id": 424242,
        "creator": config.TESTNET.creator,
        "generated_at": "2026-11-23T00:00:00Z",
        "generated_at_block": 1,
        "registries": {"us-scotus": {"id": 9}},
    }))
    monkeypatch.setenv("NVNM_MANIFEST_PATH", str(path))
    monkeypatch.setenv("NVNM_MAINNET_CHAIN_ID", "424242")
    assert load_manifest("mainnet").registry_id("us-scotus") == 9
    monkeypatch.setenv("NVNM_MAINNET_CHAIN_ID", "1")
    with pytest.raises(ValueError, match="does not match"):
        load_manifest("mainnet")
    monkeypatch.delenv("NVNM_MAINNET_CHAIN_ID")
    with pytest.raises(ValueError, match="NVNM_MAINNET_CHAIN_ID"):
        load_manifest("mainnet")


def test_mainnet_manifest_path_must_match_creator(monkeypatch, tmp_path):
    _clear_mainnet(monkeypatch)
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps({
        "schema": "nvnm-cite-registry-manifest/v1",
        "network": "mainnet",
        "chain_id": 424242,
        "creator": "nvnm1someoneelse",
        "generated_at": "2026-11-23T00:00:00Z",
        "generated_at_block": 1,
        "registries": {"us-scotus": {"id": 9}},
    }))
    monkeypatch.setenv("NVNM_MANIFEST_PATH", str(path))
    monkeypatch.setenv("NVNM_MAINNET_CHAIN_ID", "424242")
    with pytest.raises(ValueError, match="creator"):
        load_manifest("mainnet")


def test_manifest_path_does_not_override_published_profiles(monkeypatch, tmp_path):
    path = tmp_path / "manifest.json"
    path.write_text('{"schema": "nvnm-cite-registry-manifest/v1", "network": "testnet",'
                    ' "chain_id": 1, "creator": "x", "generated_at": "t",'
                    ' "generated_at_block": 1, "registries": {}}')
    monkeypatch.setenv("NVNM_MANIFEST_PATH", str(path))
    assert load_manifest("testnet").registry_id("us-scotus") == 82


def test_mainnet_signing_uses_its_own_key(monkeypatch):
    _clear_mainnet(monkeypatch)
    monkeypatch.setenv("NVNM_TESTNET_KEY", "0x" + "11" * 32)
    with pytest.raises(RuntimeError, match="NVNM_MAINNET_CHAIN_ID is not set"):
        config.signing_context(config.NETWORKS["mainnet"])
    monkeypatch.setenv("NVNM_MAINNET_CHAIN_ID", "424242")
    with pytest.raises(RuntimeError, match="NVNM_MAINNET_KEY is not set"):
        config.signing_context(config.get_network("mainnet"))
    monkeypatch.setenv("NVNM_MAINNET_KEY", "0x" + "44" * 32)
    key, chain_id = config.signing_context(config.get_network("mainnet"))
    assert key == int("44" * 32, 16)
    assert chain_id == 424242


def test_empty_manifest_does_not_read_the_chain():
    class _Boom:
        def resolve(self, *args, **kwargs):
            raise AssertionError("chain read")

    report = check_text(
        "Roe v. Wade, 410 U.S. 113 (1973).",
        _Boom(),
        registry_ids={},
    )
    assert report["citations"]
    assert {row["status"] for row in report["citations"]} == {NOT_COVERED}


def test_status_unconfigured_mainnet_does_not_probe(monkeypatch, tmp_path):
    _clear_mainnet(monkeypatch)

    class _Gateway:
        def chain_id(self):
            raise AssertionError("probed")

    class _Index:
        def coverage(self):
            return []

    network = config.get_network("mainnet")
    status = StatusService(
        _Gateway(), _Index(), tmp_path, network, load_manifest("mainnet"), rpc_url=""
    ).status()
    assert status["network"]["chain_id"] is None
    assert status["network"]["chain_id_hex"] is None
    assert status["chain"] == {"rpc_ok": False, "error": "NVNM_MAINNET_RPC is not set"}
    assert status["coverage"]["count"] == 0


def test_manifest_chain_id_must_match_profile():
    bad = replace(config.TESTNET, chain_id=1)
    with pytest.raises(ValueError, match="does not match"):
        config.match_manifest(
            bad, chain_id=config.TESTNET.chain_id, manifest_network="testnet"
        )
    other = replace(config.TESTNET, key="devnet")
    with pytest.raises(ValueError, match="does not match"):
        config.match_manifest(
            other, chain_id=config.TESTNET.chain_id, manifest_network="testnet"
        )
