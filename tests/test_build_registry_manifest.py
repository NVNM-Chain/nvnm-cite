"""The manifest builder refuses a bad first record and retries transport errors."""

from __future__ import annotations

import http.client
import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path

from nvnm_cite import config
from nvnm_cite.chain import abi
from nvnm_cite.chain import precompile as pc
from nvnm_cite.chain import rpc as rpc_module

_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_registry_manifest.py"
_spec = importlib.util.spec_from_file_location("build_registry_manifest", _SCRIPT)
assert _spec is not None and _spec.loader is not None
builder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(builder)

_CITE = pc.Record(
    uri="https://www.courtlistener.com/opinion/108713/roe-v-wade/",
    checksum="410 U.S. 113",
    checksum_algo="cite-canonical-v1",
    metadata='{"cluster":108713,"name":"Roe v. Wade","year":1973}',
    timestamp="2026-07-30T15:04:00Z",
    status="Active",
    record_id=138702,
    index=1,
    is_latest=True,
    registry_id=82,
)


def _rpc(result: str) -> dict:
    return {"jsonrpc": "2.0", "id": 1, "result": result}


def _page(fn: str, rows: list) -> str:
    blob = abi.encode_values(pc._FUNCTIONS[fn]["outputs"], [rows, [b"", 0]])
    return "0x" + blob.hex()


def _record_row(record: pc.Record) -> list:
    return [
        record.uri,
        record.checksum,
        record.checksum_algo,
        record.metadata,
        record.timestamp,
        record.status,
        record.record_id,
        record.index,
        record.is_latest,
        record.registry_id,
    ]


_CHAIN = _rpc(hex(config.TESTNET.chain_id))
_BLOCK = _rpc("0x10")
_REGISTRIES = _rpc(
    _page(
        "registries",
        [[82, "us-scotus", "", config.TESTNET.creator, "2026-07-30", ""]],
    )
)
_GOOD_RECORDS = _rpc(_page("records", [_record_row(_CITE)]))
_EMPTY_RECORDS = _rpc(_page("records", []))
# chain id, block, then the one registries page. The next reply is the first-page read.
_SETUP = [_CHAIN, _BLOCK, _REGISTRIES]


class _Response:
    def __init__(self, body: dict) -> None:
        self._raw = json.dumps(body).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self) -> bytes:
        return self._raw


def _run(monkeypatch, tmp_path, steps):
    monkeypatch.setattr(builder, "REPO", tmp_path)
    monkeypatch.setattr(builder, "court_names", lambda: {"us-scotus"})
    monkeypatch.setattr(
        sys,
        "argv",
        ["build_registry_manifest.py", "--network", "testnet", "--rpc", "http://node.test"],
    )
    (tmp_path / "src" / "nvnm_cite" / "chain").mkdir(parents=True)
    calls = {"n": 0}

    def fake_urlopen(_request, timeout=None):
        step = steps[calls["n"]]
        calls["n"] += 1
        if isinstance(step, Exception):
            raise step
        return _Response(step)

    monkeypatch.setattr(rpc_module.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(rpc_module.time, "sleep", lambda _s: None)
    rc = builder.main()
    path = tmp_path / "src" / "nvnm_cite" / "chain" / "registry_manifest_testnet.json"
    return rc, path


def test_retries_transport_error_then_writes(monkeypatch, tmp_path, capsys):
    steps = [http.client.IncompleteRead(b"partial"), *_SETUP, _GOOD_RECORDS]
    rc, path = _run(monkeypatch, tmp_path, steps)
    out = capsys.readouterr().out
    assert rc == 0
    assert "transient IncompleteRead on eth_chainId (attempt 1); retrying" in out
    written = json.loads(path.read_text())
    assert written["registries"] == {"us-scotus": {"id": 82}}


def test_empty_first_record_marks_and_writes(monkeypatch, tmp_path, capsys):
    rc, path = _run(monkeypatch, tmp_path, [*_SETUP, _EMPTY_RECORDS])
    err = capsys.readouterr().err
    assert rc == 0
    assert "warning: us-scotus (#82): no citation record; marked empty" in err
    written = json.loads(path.read_text())
    assert written["registries"] == {"us-scotus": {"id": 82, "empty": True}}


def test_bad_citation_shape_refuses_to_write(monkeypatch, tmp_path, capsys):
    bad = replace(_CITE, checksum_algo="sha256")
    rc, path = _run(monkeypatch, tmp_path, [*_SETUP, _rpc(_page("records", [_record_row(bad)]))])
    err = capsys.readouterr().err
    assert rc == 1
    assert "checksumAlgo" in err
    assert not path.exists()
