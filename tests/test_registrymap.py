"""Pinned registry manifests: load, resolve, and drift detection."""

import pytest

from nvnm_cite.chain import abi
from nvnm_cite.chain import precompile as pc
from nvnm_cite.chain.registrymap import (
    CitationScan,
    RegistryManifest,
    _parse,
    load_manifest,
    scan_first_citations,
)
from nvnm_cite.chain.rpc import RpcError

ADMIN = "nvnm14a3em3mr9mvta9ccgk80wn0dxgzt5lkt2r8trx"


@pytest.mark.parametrize(
    "network, chain_id",
    [("testnet", 787223), ("devnet", 787222)],
)
def test_manifest_pins_its_own_chain(network, chain_id):
    m = load_manifest(network)
    assert m.network == network
    assert m.chain_id == chain_id
    assert m.creator == ADMIN
    assert len(m.ids) == 2114
    assert m.registry_id("us-scotus") == 82
    assert m.registry_id("not-a-court") is None
    assert m.empty == frozenset()


def test_load_manifest_unknown_network():
    with pytest.raises(FileNotFoundError):
        load_manifest("no-such-network")


class _FakeRpc:
    """Serves a canned registries() enumeration through eth_call."""

    def __init__(self, rows):
        self._rows = rows

    def eth_call(self, to, data, block="latest"):
        # decode the offset out of the query to serve the right page
        args_entries = pc._FUNCTIONS["registries"]["inputs"]
        from nvnm_cite.chain import abi

        _, page = abi.decode_values(args_entries, data[4:])
        offset, limit = page[1], page[2]
        rows = self._rows[offset : offset + limit]
        as_lists = [
            [r.id, r.name, r.description, r.creator, r.created_at, r.metadata]
            for r in rows
        ]
        return abi.encode_values(
            pc._FUNCTIONS["registries"]["outputs"], [as_lists, [b"", 0]]
        )


def _manifest(ids):
    return RegistryManifest(
        schema="nvnm-cite-registry-manifest/v1",
        network="testnet",
        chain_id=787111,
        creator=ADMIN,
        generated_at="2026-07-31T00:00:00Z",
        generated_at_block=1,
        ids=ids,
    )


def _reg(rid, name, creator=ADMIN):
    return pc.Registry(rid, name, "d", creator, "2026-07-30", "")


def test_diff_against_chain_clean():
    m = _manifest({"us-scotus": 737, "us-ca11": 738})
    rpc = _FakeRpc([_reg(737, "us-scotus"), _reg(738, "us-ca11"), _reg(739, "other", "nvnm1someoneelse")])
    assert m.diff_against_chain(rpc) == {"added": {}, "missing": {}, "renamed": {}}


def test_diff_against_chain_detects_drift():
    m = _manifest({"us-scotus": 737, "us-ca11": 738})
    rpc = _FakeRpc(
        [
            _reg(737, "us-renamed"),  # renamed in place
            # 738 gone entirely
            _reg(740, "us-ca11"),  # a NEW registry by our creator with a manifest name
        ]
    )
    diff = m.diff_against_chain(rpc)
    assert diff["renamed"] == {737: {"pinned": "us-scotus", "chain": "us-renamed"}}
    assert diff["missing"] == {738: "us-ca11"}
    assert diff["added"] == {740: "us-ca11"}


def _cite(registry_id=82, **overrides) -> pc.Record:
    fields = dict(
        uri="https://www.courtlistener.com/opinion/108713/roe-v-wade/",
        checksum="410 U.S. 113",
        checksum_algo="cite-canonical-v1",
        metadata='{"cluster":108713,"name":"Roe v. Wade","year":1973}',
        timestamp="2026-07-30T15:04:00Z",
        status="Active",
        record_id=138702,
        index=1,
        is_latest=True,
        registry_id=registry_id,
    )
    fields.update(overrides)
    return pc.Record(**fields)


class _RecordsRpc:
    """Serves records() pages, or one RpcError, through eth_call."""

    def __init__(self, pages, error=None):
        self.pages = pages
        self.error = error
        self.limits: list[int] = []

    def eth_call(self, to, data, block="latest"):
        decoded = abi.decode_values(pc._FUNCTIONS["records"]["inputs"], data[4:])
        self.limits.append(decoded[4][2])
        if self.error is not None:
            raise self.error
        rows = self.pages.get(decoded[0], [])
        as_lists = [
            [
                r.uri,
                r.checksum,
                r.checksum_algo,
                r.metadata,
                r.timestamp,
                r.status,
                r.record_id,
                r.index,
                r.is_latest,
                r.registry_id,
            ]
            for r in rows
        ]
        return abi.encode_values(
            pc._FUNCTIONS["records"]["outputs"], [as_lists, [b"", 0]]
        )


def test_empty_registry_is_marked_not_failed():
    rpc = _RecordsRpc({82: []})
    scan = scan_first_citations(rpc, {"us-scotus": 82})
    assert scan.empty == ("us-scotus",)
    assert scan.errors == ()
    assert rpc.limits == [1]


def test_record_does_not_exist_counts_as_empty():
    rpc = _RecordsRpc(
        {},
        error=RpcError("eth_call", -32000, "execution reverted: record does not exist"),
    )
    scan = scan_first_citations(rpc, {"us-scotus": 82})
    assert scan.empty == ("us-scotus",)
    assert scan.errors == ()


@pytest.mark.parametrize(
    "override, fragment",
    [
        ({"checksum_algo": "sha256"}, "checksumAlgo 'sha256'"),
        ({"metadata": "not-json"}, "metadata is not a citation object"),
        ({"metadata": '{"name":"Roe v. Wade"}'}, "metadata is not a citation object"),
        ({"uri": "urn:nvnm-cite:receipt:v1"}, "uri 'urn:nvnm-cite:receipt:v1'"),
        ({"status": "Superseded"}, "status 'Superseded'"),
        ({"registry_id": 99}, "registry id 99"),
    ],
)
def test_non_citation_record_fails(override, fragment):
    rpc = _RecordsRpc({82: [_cite(**override)]})
    scan = scan_first_citations(rpc, {"us-scotus": 82})
    assert scan.errors == (f"us-scotus (#82): {fragment}",)
    assert scan.empty == ()


def _clean() -> CitationScan:
    return CitationScan(errors=(), empty=())


def test_cluster_record_passes():
    rpc = _RecordsRpc({82: [_cite()]})
    assert scan_first_citations(rpc, {"us-scotus": 82}) == _clean()


def test_cases_record_passes():
    meta = '{"cases":[{"cluster":111,"name":"A v. B","year":1990}]}'
    rpc = _RecordsRpc({82: [_cite(metadata=meta)]})
    assert scan_first_citations(rpc, {"us-scotus": 82}) == _clean()


def test_full_page_of_citation_records_passes():
    rpc = _RecordsRpc({82: [_cite(), _cite(checksum="347 U.S. 483")]})
    assert scan_first_citations(rpc, {"us-scotus": 82}) == _clean()


def test_bad_row_in_a_full_page_fails():
    rpc = _RecordsRpc({82: [_cite(), _cite(checksum_algo="sha256")]})
    scan = scan_first_citations(rpc, {"us-scotus": 82})
    assert scan.errors == ("us-scotus (#82): checksumAlgo 'sha256'",)
    assert scan.empty == ()


def test_node_error_is_not_an_empty_registry():
    rpc = _RecordsRpc({}, error=RpcError("eth_call", -32000, "header not found"))
    scan = scan_first_citations(rpc, {"us-scotus": 82})
    assert scan.empty == ()
    assert scan.errors == ("us-scotus (#82): eth_call: [-32000] header not found",)


def test_empty_flag_keeps_the_id():
    manifest = _parse(
        '{"schema":"nvnm-cite-registry-manifest/v1","network":"testnet",'
        '"chain_id":787223,"creator":"nvnm1x","generated_at":"2026-11-12T00:00:00Z",'
        '"generated_at_block":1,"registries":{'
        '"us-scotus":{"id":82},'
        '"us-ca11":{"id":71,"empty":true}'
        "}}"
    )
    assert manifest.registry_id("us-ca11") == 71
    assert manifest.all_registries() == {"us-scotus": 82, "us-ca11": 71}
    assert manifest.empty == frozenset({"us-ca11"})
