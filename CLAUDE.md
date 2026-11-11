# nvnm-cite

Citation existence verification and filing receipts on NVNM Chain. Plaintext per-court registries of canonical US case citations + a verifier that checks briefs against them and anchors a receipt at filing time.

What this is NOT: it never asserts a case supports a proposition, and it never asserts good-law status. Provenance, not truth.

## Invariants (never violate)

1. Citations are stored and checked in PLAINTEXT. Citation identifiers are never hashed. The only hash in the system is the SHA-256 of the checked document inside a receipt.
2. Existence-only verification. No holdings, no propositions, no good-law flags. If citator data ever enters, it enters as a named citator's attested claim, never as an NVNM assertion.
3. Anchoring (a chain WRITE) is explicit and happens only at filing time. Drafting-time checks READ the chain live via the NVNM-operated RPC: `eth_call` reads are point-to-point (no mempool, no block, no on-chain trace), so the citation set is visible only to NVNM as operator — equivalent to the in-memory parse, never published. The win is non-repudiation (we cannot lie about the chain's answer; any skeptic replays the exact `records()` call against any node), not secrecy. The local index is a rebuildable audit/cache (`rebuild-index`), never the lookup authority. SUPERSEDES the original local-index-only / no-RPC rule (DECISIONS 2026-06-13, item 0).
4. The registry write model must allow third parties to own registries. Writes are deny-by-default (creator = admin; no public-write mode), so there is NO single global shared registry — it would make NVNM a permanent write-gatekeeper. Inveniam populates the COURT registries but never assumes it is the only attestor. RECEIPTS live in per-firm-per-case registries owned by the filing party's own wallet; discovery is the registry LINK on the filing (a stable pointer established before the document is hashed — never the receipt/tx, which is circular), and a verifier hashes the document locally and does a keyed `records(registry_id, hash)` lookup (DECISIONS 2026-06-13, item 3). AMENDED 2026-07-31 (anchoring v1.2.0): registry names are NOT unique on chain, so the link carries the numeric registry #id (format in `receipts/anchor.py::registry_line`); published registry IDS — the pinned, creator-verified manifests in `src/nvnm_cite/chain/registry_manifest_*.json` — are the name→id trust anchor for the court registries. AMENDED 2026-08-06 (first-filing bootstrap, Albert): the receipts registry is created by the FIRST document's own anchor, so a first filing NEVER carries the id line — its discovery is the derived firm+case name (creator+name enumeration); the id line goes on subsequent filings only. AMENDED same day (chain-wide verify, Albert): a verifier needs NO pointer at all — the default verify is hash-first: sweep every non-court registry with the keyed read and surface every hit with its registry #id, CREATOR WALLET, and chain time (`receipts/discover.py::find_anchors`; any wallet can anchor any hash into its own registry, so who recorded it is part of the answer, rendered per hit). The filing line / firm+case name remain optional scoping, not prerequisites.
5. The normalizer is part of the trust boundary. Its spec is open and versioned, and every receipt records the normalizer version used.
6. The product name is NVNM Chain. Never "Inveniam Chain".
7. Receipts are minimal and NON-ENUMERATING: a receipt records the document SHA-256, provenance (chain_id, checked_at_block, normalizer_version, the court registries read, the attesting wallet address, timestamp) and a non-identifying status tally — never the list of cited cases. The SHA-256 binds the exact document, so verdicts are fully reproducible without publishing the brief's authorities on chain. Case-frequency analytics come ONLY from aggregate RPC query telemetry (by citation, decoupled from document hash and client identity), never from receipt contents (DECISIONS 2026-06-13, items 2/2b).

## Chain constants

Network identity is a profile in `src/nvnm_cite/networks/`. Shipped profiles are testnet and devnet. `get_network()` resolves an explicit argument, then `NVNM_NETWORK`, then testnet. One process uses that profile for reads and writes. Adding a network is a new profile JSON plus `src/nvnm_cite/chain/registry_manifest_<key>.json`, built by `scripts/build_registry_manifest.py` (it resolves the profile before the manifest file exists). The profile and the manifest must agree on network key and `chain_id`, or load fails. Signing reads only the env var named by the profile's `key_env`. Never print keys.

| Item | testnet (default) | devnet (`--network devnet` or `NVNM_NETWORK=devnet`) |
|---|---|---|
| EVM chain ID | 787223 | 787222 |
| Network name (`network_name`) | nvnm-next-testnet-1 | nvnm-next-devnet-1 |
| EVM RPC | https://rpc.nvnm.testnet.nvnmchain.io | https://rpc.nvnm.canary.mantrachain.dev |
| RPC override env | `NVNM_TESTNET_RPC` | `NVNM_DEVNET_RPC` |
| Signing key env | `NVNM_TESTNET_KEY` | `NVNM_DEVNET_KEY` |
| Explorer | https://explorer.nvnm.testnet.nvnmchain.io | https://explorer.nvnm.canary.mantrachain.dev |
| Gas token | nUSD | nUSD |
| Fee token | `0x20C0000000000000000000000000000000000000` (6 decimals) | same |

Profile values are copied from the previous in-code constants (docs.nvnmchain.io "Network Details", checked against `eth_chainId` 2026-11-10). A profile's RPC override env replaces `rpc_default`.

Protocol, shared by every profile. A network that moves any of these is a client change, not a new profile file:

- **Anchoring v1.2.0:** registry names are not unique. Every read and write keys on the numeric registryId. Selectors: `records(uint64,string,uint64,uint64,Page)`=`c7be5e37`, `registries(uint64,Page)`=`17bd3e65`, `addRecord`=`64d25295`, `addRegistry`=`318b38b1`, `grantRole`=`b8fdd1a7`, `revokeRole`=`acd58bc7`, `updateRecordStatus`=`97b40c25`. Module doc: github.com/NVNM-Chain/nvnmchain v1.2.0 `x/anchoring/readme.md`.
- Anchor precompile: `0x0000000000000000000000000000000000000A00`. Vendored ABI (functions and the five events): `src/nvnm_cite/chain/anchoring.json`.
- Both shipped manifests pin 2,114 court registries, ids 69 (`us-ca1`) through 2182 (`us-wyo`), creator `nvnm14a3em3mr9mvta9ccgk80wn0dxgzt5lkt2r8trx`. `us-scotus`=82, `us-ca11`=71, `us-ca2`=72. Roe `records(82,"410 U.S. 113")` → recordId 138702. Do not assume a future network's ids are the same, dense, or small. The pinned manifest is the map. `nvnm-cite manifest-verify` diffs it against a live enumeration. State-migrated records emitted no events, so offset-paged `records()` is the rebuild path.
- `records(registry_id, checksum, recordId, index, pagination)` is the keyed existence read. An explicit `index` returns that version. A keyed read returns the latest version only, and the latest `index` is the version count.
- The precompile emits AddRegistry, AddRecord, UpdateRecordStatus, GrantRole, RevokeRole. Only `caller` is indexed. AddRegistry data is (registryId, name), recovered by `precompile.decode_add_registry_log`. AddRecord data is (registryId, recordId, index, checksum), recovered by `precompile.decode_add_record_log`. eth_getLogs is capped at 10,000 blocks. Reads (`eth_call`) produce no logs.
- A keyed miss reverts with `record does not exist` (also `records()` on a missing registry) or `registry does not exist` (`registries()`). `precompile.is_keyed_miss` matches those strings. An empty page is not a miss. The ABI decoder replaces non-UTF-8 registry bytes instead of raising. Field caps: checksum <= 64 B, uri <= 2048 B, metadata <= 2048 B. uri, checksumAlgo, and metadata must be non-empty, and `{}` counts as empty. Writes are deny-by-default (creator = admin; grantRole adds editors, revokeRole removes them). `status` is a free-form string. updateRecordStatus writes status only, in place, and is reversible. Duplicates create versions. Pagination is offset-based, 200 rows per page. nextKey and countTotal are unreliable. The public RPC serves archive state.
- Writers send at `eth_gasPrice`. The loader's spendable balance is the profile's fee token (`balanceOf`). The gas-limit curve in `loader/bulk_load.py` is measured for the shipped profiles; remeasure it before a bulk load on a network with a different gas schedule.
- The NVNM Chain MCP server's `anchor_get_registries` / `anchor_get_registry` tools speak the pre-v1.2.0 read ABI. Until that is fixed, read with `precompile.build_*` / `decode_*` or the LCD.

## Record schema (LOCKED v1 at task 1.5, 2026-06-11; full text in docs/record-schema.md)

- Per-case record: `checksum` = canonical citation string in plaintext per cite-canonical/v1 (e.g. `410 U.S. 113`; first-page keys, spec in docs/canonical-citation-spec.md), `checksumAlgo` = `cite-canonical-v1`, `uri` = CourtListener cluster URL (bulk-data slug form, API-URL fallback), `metadata` = compact JSON {"cluster","name","year"} (collision form {"cases":[...]}; deterministic truncation rules in the schema doc), `status` = `Active`.
- Receipt record (registry = a PER-FIRM-PER-CASE receipts registry owned by the filing party, NOT a global registry — amended 2026-06-13, DECISIONS items 2/2b/3; re-locks at Phase 4 task 4.1): `checksum` = document SHA-256 hex (exactly fills the 64 B cap), `checksumAlgo` = `sha256`, `uri` = `urn:nvnm-cite:receipt:v1` (fixed), `metadata` = the MINIMAL receipt JSON (hash + provenance + a non-identifying status tally; NO case enumeration → always well under the 2048 B cap, so no chunking). JSON rules everywhere: UTF-8, ensure_ascii=false, sorted keys, no whitespace.
- Registry names: courts-db IDs prefixed `us-` (`us-scotus`, `us-ca11`) for case records; receipts go in per-firm-per-case registries (deterministic naming, owned by the filing party's wallet — see the schema doc). Court-registry creation strings (descriptions + metadata incl. FLP attribution) are fixed in the schema doc. v1.2.0 amendment (2026-07-31, appendix in the schema doc; no schema bump): names are non-unique on chain, the numeric #id is canonical, the filing's discovery line carries it, and a many-court receipt's registries table truncates deterministically into the additive optional `registries_omitted` field.
- Schema changes from here require a version bump, never an edit.

## Conventions

- Python 3.11+, uv for env and deps, pytest, type hints everywhere.
- `src/nvnm_cite/chain/` uses ONLY the standard library. The signer is written from scratch (keccak-256 with original Keccak padding, RLP, secp256k1 + RFC-6979, EIP-155 type-0). The golden suites in `tests/golden/` are the contract; run pytest after every change to `chain/`, `normalizer/`, or `receipts/`.
- Build on eyecite / reporters-db / courts-db (Phase 1 onward). Never write a citation parser from scratch.
- No new dependency without a dated DECISIONS.md entry (name, version pin, license).
- Never print private keys, `.env` values, or seed phrases.
- Case data attribution (CourtListener / Free Law Project) stays in README, registry metadata, and demos.
- Before sending any chain transaction, present the plan and get an explicit OK (use plan mode when available).
- Session cadence (user preference, 2026-06-10): one phase per session. Do not suggest opening a fresh session between tasks of the same phase; wrap up at phase boundaries.

## Where state lives

- `IMPLEMENTATION_PLAN.md`: position. 3-line Status header + checkboxed phases. The next session continues from here.
- `DECISIONS.md`: memory. Append-only, dated. Read it before proposing changes to anything it covers.
- Git: main-only with `phase-N-done` tags, no feature branches. History is the session log.
- The session kickoff prompt lives in README.md.

## Session end ritual (do this without being asked)

When the user says "wrap up", or when the session's goal is reached:
1. Run pytest; do not commit on red without an explicit user OK.
2. Update IMPLEMENTATION_PLAN.md: tick completed checkboxes, refresh the 3-line Status header.
3. Append settled choices to DECISIONS.md (dated).
4. `git add -A && git commit -m "session: <phase> - <one-line summary>"`
5. If a phase just completed: `git tag phase-N-done && git push && git push --tags`. Otherwise just `git push`.
6. Print: phase status, what the next session starts with, and a reminder that the kickoff prompt in README.md is generic.
