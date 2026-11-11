"""Network profiles and per-profile signing keys."""

from dataclasses import replace

import pytest

from nvnm_cite import config


def test_profiles_pin_chain_constants():
    assert set(config.NETWORKS) == {"testnet", "devnet"}
    assert config.network_choices() == ["devnet", "testnet"]
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


def test_get_network_precedence(monkeypatch):
    monkeypatch.delenv("NVNM_NETWORK", raising=False)
    assert config.get_network() is config.TESTNET
    monkeypatch.setenv("NVNM_NETWORK", "devnet")
    assert config.get_network() is config.DEVNET
    assert config.get_network("testnet") is config.TESTNET  # explicit arg wins
    with pytest.raises(ValueError):
        config.get_network("no-such")
    with pytest.raises(ValueError):
        config.get_network("mainnet")


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
