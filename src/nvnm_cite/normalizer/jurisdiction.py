"""Map a resolved case citation to an NVNM registry name.

Registry names are courts-db court IDs prefixed "us-" (us-scotus, us-ca11).
The mapping never guesses: a citation whose court cannot be determined from
the reporter edition or the court parenthetical returns (None, reason) and
the caller reports AMBIGUOUS_JURISDICTION.

Mapping rules, in order (an explicit court signal always outranks a
reporter-derived default):
1. Reporter edition in SCOTUS_EDITIONS -> us-scotus. Needed because eyecite
   sets court='scotus' for bare U.S. and S. Ct. cites but NOT for bare
   L. Ed. / L. Ed. 2d cites (measured against eyecite 2.7.6).
2. eyecite's metadata.court (already a courts-db ID, parsed from the court
   parenthetical) -> us-<id>, after validating the ID against courts-db.
   CORROBORATION-GATED (1.3.0, measured on the state corpus run): eyecite's
   forward parenthetical scan overreaches across neighboring citations in
   string cites and tables of authorities, so a claim is accepted only when
   an ADJACENT parenthetical corroborates it. A contradicting adjacent
   parenthetical wins outright (it is the citation's own signal); a claim
   with NO adjacent parenthetical at all is the measured overreach
   signature and is refused.
3. Closed-set federal-circuit parenthetical fallback ("(3d Cir. 1999)" and
   ordinal variants eyecite misses).
4. General court-parenthetical fallback: exact longest-prefix match of the
   parenthetical's content against courts-db citation_strings — measured
   globally unique (1,959/1,959 map to exactly one court) — plus closed
   sets for New York Appellate Division forms ("App. Div.", "1st Dep't" …
   "4th Dep't", state-gated on the reporter) and Florida DCA forms
   ("Fla. 1st DCA" … — courts-db has no citation_string for them and the
   corpus keys DCA cases under the parent fladistctapp). 1.3.0: the
   parenthetical BEFORE the citation is read too — California citation
   style is "Name (Court Year) cite" — with the trailing year stripped; a
   year-only preceding parenthetical carries no court signal. A prefix
   match is refused when the remainder begins with an ordinal token
   ("Fla." must never swallow "Fla. 1st DCA"), and curly apostrophes /
   quotes normalize to straight before matching ("Tex. Comm'n App.").
   1.4.0 (7.8.2, the remaining-45-states rollout): ¶-pinpoint
   parentheticals are pin material — skipped by the scan, and not
   corroboration surface for a rule-2 claim; bare "(Ct. App.)"/"(App.)"
   are state-gated like App. Div. (S.C./W. Va./Wis./Idaho/Nev.;
   Ariz./Haw.), and a recognized bare form the reporter cannot resolve is
   refused WITH PREJUDICE — it defeats a rule-2 claim riding the same
   text; a curated closed set covers court forms courts-db lacks
   (Ky. App., Minn. App., Mo. App. + districts, Mo. banc, N.C. App. Ct.,
   Pa. Cmwlth., Alaska App., Kan. App., Md. App. Ct., Nev. Ct. App.,
   W. Va. Ct. App., Tennessee period-drop variants); Louisiana's numbered
   circuits map to us-lactapp; Ohio's numbered districts map to
   us-ohioctapp for Ohio editions only (N.E. spans Ohio AND Illinois);
   Alabama's historical "(Civ.)"/"(Crim.)" map to the division courts for
   Ala. editions only.
5. Reporter-edition inference from the corpus-derived table
   (reporter_registries.json, built by scripts/build_reporter_map.py):
   editions that one registry dominates >= 99.5% across the 11.9M-record
   mainnet corpus, guarded (single reporters-db reporter, non-vendor,
   curated adjudications in DECISIONS 2026-08-01). This is what makes bare
   "212 A.D.2d 331", "248 N.Y. 339" or "T.C. Memo. 1976-300" resolvable.
5b. Same-state family candidates (1.3.0): editions whose ENTIRE >=1%
   corpus population sits in ONE state but across sibling registries
   (measured: "Cal. App. 5th" splits 71/29 calctapp5d/calctapp from
   CourtListener attribution drift; N.Y.2d splits ny/nyappdiv; NY Slip Op,
   Misc. 3d, Ill. Dec.) route to the family's dominant registry, and the
   verifier sweeps the remaining candidates with keyed reads before
   reporting a miss (lookup_candidates). Existence-only semantics are
   unchanged: every hit is a live keyed read, and the answering registry
   is disclosed per row.
6. Anything else is ambiguous. This includes F.2d/F.3d/F.4th/F. App'x and
   regional reporters (S.W.2d, N.E.2d, …) with no recognizable
   parenthetical, genuinely multi-STATE reporters (S.W.3d, So. 3d, M.J.),
   and shared nominatives ("Cranch" is both scotus_early and a D.C.
   reporter).

Vendor identifiers (Westlaw "2019 WL 1439098", LEXIS) are not jurisdiction
questions at all: they are never registry keys (the corpus scope excludes
them by design), so vendor_kind() lets the caller report them as outside
coverage without a chain read.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from importlib import resources

import courts_db
from eyecite.models import CaseCitation
from reporters_db import REPORTERS

REGISTRY_PREFIX = "us-"

# The three SCOTUS reporter families (reporters-db edition strings). All carry
# cite_type='federal' in reporters-db, so the edition set, not cite_type, is
# the discriminator.
SCOTUS_EDITIONS = frozenset({"U.S.", "S. Ct.", "L. Ed.", "L. Ed. 2d"})

# Federal reporters that span every circuit: without a court parenthetical
# these are the canonical AMBIGUOUS_JURISDICTION case (called out in the spec).
AMBIGUOUS_FEDERAL_REPORTERS = frozenset(
    {"F.", "F.2d", "F.3d", "F.4th", "F. App'x", "F. Supp.", "F. Supp. 2d", "F. Supp. 3d"}
)

_VALID_COURT_IDS: frozenset[str] = frozenset(c["id"] for c in courts_db.courts)

# Closed-set fallback for standard federal appellate parentheticals.
# eyecite 2.7.6 resolves "(3rd Cir.)" but not the Bluebook-standard
# "(3d Cir.)" (measured; "2d Cir." works, the gap is 3d only). The spec's
# rule 2 makes these 13 forms recognizable per se, so when eyecite reports
# no court we match them exactly: ordinal + "Cir." right after the cite,
# with only pin-cite characters allowed in between so a neighboring
# citation's parenthetical can never be misattributed. An exact whitelist
# is not a guess.
_CIRCUIT_BY_ORDINAL: dict[str, str] = {
    "1st": "ca1", "2d": "ca2", "2nd": "ca2", "3d": "ca3", "3rd": "ca3",
    "4th": "ca4", "5th": "ca5", "6th": "ca6", "7th": "ca7", "8th": "ca8",
    "9th": "ca9", "10th": "ca10", "11th": "ca11", "D.C.": "cadc", "Fed.": "cafc",
}
_CIRCUIT_PARENTHETICAL = re.compile(
    r"^(?:\s*,?\s*(?:at\s+)?[\d\s,\-–&n\.\*]*)"  # optional pin cites only (incl. *4 star pages)
    r"\((?P<ordinal>1st|2d|2nd|3d|3rd|4th|5th|6th|7th|8th|9th|10th|11th|D\.C\.|Fed\.)"
    r"\s+Cir\.?(?:[\s,][^)]*)?\)"
)


def _circuit_from_following_text(following_text: str) -> str | None:
    match = _CIRCUIT_PARENTHETICAL.match(following_text)
    if not match:
        return None
    return _CIRCUIT_BY_ORDINAL[match.group("ordinal")]


# General parenthetical fallback (rule 4): the first parenthetical right
# after the cite (same pin-cite-only guard as the circuit fallback, so a
# neighboring citation's parenthetical is never misattributed). ¶ joined
# the pin-cite class in 7.8.2c: Ohio pinpoints paragraphs before the
# district parenthetical ("2023-Ohio-116, ¶ 29 (12th Dist.)").
_ANY_PARENTHETICAL = re.compile(
    r"^(?:\s*,?\s*(?:at\s+)?[\d\s,\-–&n\.\*¶]*)\((?P<content>[^)]{1,80})\)"
)

# A parenthetical that is itself a paragraph pinpoint — Mississippi's
# standard citation interleaves one before the court parenthetical
# ("102 So. 3d 1209, 1214 (¶13) (Miss. Ct. App. 2012)", spacing varies).
# The court scan skips these (7.8.2c); they are pins, not court signals,
# so they are also NOT corroboration surface for an eyecite claim.
_PARAGRAPH_PARENTHETICAL = re.compile(r"^¶")

# The parenthetical BEFORE the citation (California style: "Name (Court
# Year) cite"). It must close immediately before the cite (only whitespace
# or a comma in between) and its content must END with a year — that year
# is stripped before the court match, and a year-only parenthetical
# ("(2018)") carries no court signal at all.
_PRECEDING_PARENTHETICAL = re.compile(r"\((?P<content>[^()]{1,80})\)[\s,]*$")
_TRAILING_YEAR = re.compile(r"(?:1[6-9]|20)\d{2}$")

# Court text in real documents uses typographic apostrophes and quotes;
# courts-db citation_strings use straight ones ("Tex. Comm'n App.").
_QUOTE_TRANSLATION = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})

# A prefix match whose remainder begins with an ordinal token is matching a
# SHORTER court's string inside a longer court form: "Fla." must never
# swallow "Fla. 1st DCA" (measured: 60 misroutes on the 2026-08-09 state
# corpus run). A year remainder ("2020") does not trip this.
_ORDINAL_REMAINDER = re.compile(r"\d{1,2}(?:st|nd|rd|d|th)\b")

# Florida DCA forms as actually written ("Fla. 1st DCA 1989"): courts-db
# has NO citation_string for the DCA courts (the district entries are
# blank), and the corpus keys DCA cases under the parent court
# fladistctapp — measured 100,839 So. 3d records there vs single digits in
# the per-district registries.
_FLA_DCA = re.compile(r"Fla\.\s*\d{1,2}(?:st|nd|rd|d|th)\s+DCA\b")

# "App. Div." / department parentheticals are STATE-GATED on the reporter:
# both New York and New Jersey have an Appellate Division, so the bare form
# identifies a court only in combination with the citation's own reporter
# family. Within a state the synonym is definitional, not a guess (courts-db
# models N.Y.'s four departments as the single court nyappdiv).
_NY_EDITION_PREFIXES = ("A.D.", "N.Y.", "Misc.", "How. Pr.", "Hun", "Barb.")
_NJ_EDITION_PREFIXES = ("N.J.",)
_APPDIV_FORMS: tuple[str, ...] = (
    "App. Div.",
    "1st Dep't", "2d Dep't", "2nd Dep't", "3d Dep't", "3rd Dep't", "4th Dep't",
    "1st Dept.", "2d Dept.", "2nd Dept.", "3d Dept.", "3rd Dept.", "4th Dept.",
)

# A recognized bare form whose state cannot be resolved from the citation's
# own reporter. Distinct from None (unrecognized content): a REFUSED form
# also DEFEATS an eyecite court claim riding the same parenthetical —
# measured (7.8.2, calibration on the 45-state report strings): eyecite
# resolves bare "(Ct. App. 2020)" to ctappindterr, the Indian Territory
# Court of Appeals (dead 1907), on live S.C./W. Va./Idaho/Nev. strings,
# and the state gate is inert because that territorial court carries no
# state. Truthy on purpose so it propagates through or-chains; never a
# courts-db id.
_REFUSE = "__refuse__"

# Bare intermediate-court parentheticals, state-gated on the reporter (the
# App. Div. pattern, 7.8.2a). "(Ct. App. 2020)" after an S.C. cite is the
# South Carolina Court of Appeals; after a W. Va. cite it is the 2022
# Intermediate Court of Appeals (courts-db wvactapp — no registry on
# chain, so the verifier reports NOT_COVERED per the 2026-08-11 decision);
# after a multi-state regional reporter it names an intermediate court of
# SOME unknowable state and is REFUSED. The gate fires only on truly BARE
# content (remainder empty or a year), so genuine longer courts-db strings
# ("Ct. App. Nev.", "Ct. App. Ind. Terr.") still reach the index.
_CT_APP_EDITION_GATE: tuple[tuple[tuple[str, ...], str], ...] = (
    (("S.C.",), "scctapp"),
    (("W. Va.", "W.Va."), "wvactapp"),
    (("Wis.",), "wisctapp"),  # pre-2000 "(Ct. App. 1993)" after Wis. 2d
    (("Idaho",), "idahoctapp"),
    (("Nev.",), "nevapp"),
)
# "(App. 1995)" — Arizona and Hawaii identify their intermediate courts by
# a bare "(App. <year>)" after the official reporter (the reporter itself
# spans both appellate levels in each state).
_APP_EDITION_GATE: tuple[tuple[tuple[str, ...], str], ...] = (
    (("Ariz.",), "arizctapp"),
    (("Haw.",), "hawapp"),
)
_BARE_REMAINDER = re.compile(r"^(?:(?:1[6-9]|20)\d{2})?$")  # empty or a year

# Alabama's historical compressed division parentheticals: "(Civ. 1974)" /
# "(Crim. 1974)" after an Ala. / Ala. App. cite (measured in the 45-state
# report's verbatim strings). Gated on Ala. editions only — So. 2d/3d spans
# four states, so the bare token is not state-provable there.
_ALA_DIVISION_GATE: tuple[tuple[str, str], ...] = (
    ("Civ.", "alacivapp"),
    ("Crim.", "alacrimapp"),
)

# Court-parenthetical forms courts-db has NO citation_string for, each
# measured swallowing into the state's shortest string (7.8.2b, the
# Fla-DCA precedent — calibration: "(Ky. App. 2019)" routed us-ky,
# "(Minn. App. 2019)" us-minn, "(Mo. App. W.D. 2017)" us-mo,
# "(Pa. Cmwlth. 2018)" us-pa, "(Alaska App. 2002)" us-alaska,
# "(N.C. App. Ct. 2024)" us-nc). Prefix-matched before the courts-db index
# (every entry is longer than the string it was measured swallowing into);
# a single "Mo. App." entry covers the E.D./W.D./S.D. district suffixes,
# the bracketed "[W.D.]" editorial form, and the district-less generic the
# Missouri Supreme Court itself uses. "Mo. banc" is the Missouri Supreme
# Court's own signal (previously right only by prefix accident).
_CURATED_COURT_FORMS: tuple[tuple[str, str], ...] = (
    ("W. Va. Ct. App.", "wvactapp"),
    ("W.Va. Ct. App.", "wvactapp"),
    ("N.C. App. Ct.", "ncctapp"),
    ("Md. App. Ct.", "mdctspecapp"),
    ("Nev. Ct. App.", "nevapp"),  # courts-db has only the inverted "Ct. App. Nev."
    ("Tenn. Crim App.", "tenncrimapp"),  # measured period-drop variants in
    ("Tenn Crim. App.", "tenncrimapp"),  # court-authored text (the report)
    ("Pa. Cmwlth.", "pacommwct"),
    # 7.8.4 live-sweep finds (2026-08-11): courts-db writes "Pa. Super.
    # Ct." / "Colo. Ct. App.", but the state's actual parenthetical is
    # "(Pa. Super. 2011)" / "(Colo. App. 2003)" — neither prefix-matches
    # the courts-db string, so both swallowed into "Pa."/"Colo." (caught
    # by the census classification of the 45-state verification run:
    # in-corpus keys NOT_FOUND under the swallowed registry).
    ("Pa. Super.", "pasuperct"),
    ("Colo. App.", "coloctapp"),
    ("Alaska App.", "alaskactapp"),
    ("Minn. App.", "minnctapp"),
    ("Kan. App.", "kanctapp"),
    ("Ky. App.", "kyctapp"),
    ("Mo. App.", "moctapp"),
    ("Mo. banc", "mo"),
)

# Louisiana's five numbered Courts of Appeal: the circuit is part of the
# citation ("La. App. 2 Cir." per the Supreme Court's rule; "La. App. 1st
# Cir." in actual First Circuit opinions). All five are one courts-db court
# (lactapp) and one registry. The trailing full date ("1/26/11") rides in
# the remainder. Anchored so federal "(1st Cir.)" can never reach it.
_LA_CIRCUIT = re.compile(r"^La\.\s?App\.\s?[1-5](?:st|nd|rd|d|th)?\s?Cir\.")

# Ohio's twelve numbered appellate districts, as trailing parentheticals
# ("(12th Dist.)", "(6th Dist.1991)" — no space before the year in real
# text). One courts-db court (ohioctapp); gated on Ohio editions because
# N.E.-family reporters span Ohio AND Illinois (which also has numbered
# districts), so the bare district is not state-provable there.
_OHIO_DISTRICT = re.compile(r"^(?:1st|2n?d|3r?d|[4-9]th|1[0-2]th)\s?Dist\.")

_BOUNDARY_CHARS = " ,—–[(0123456789"


@lru_cache(maxsize=1)
def _citation_string_index() -> tuple[dict[str, str], list[str]]:
    """courts-db citation_string -> court id, longest-first key list.

    Measured against courts-db 0.10.x: every non-empty citation_string maps
    to exactly one court, so an exact prefix match cannot be ambiguous. If a
    future courts-db release ever introduces a duplicate, both courts are
    dropped here (refuse rather than guess).
    """
    seen: dict[str, list[str]] = {}
    for court in courts_db.courts:
        s = (court.get("citation_string") or "").strip().translate(_QUOTE_TRANSLATION)
        if s:
            seen.setdefault(s, []).append(court["id"])
    index = {s: ids[0] for s, ids in seen.items() if len(ids) == 1}
    return index, sorted(index, key=len, reverse=True)


def _prefix_match(content: str, key: str) -> bool:
    return content == key or (
        content.startswith(key) and content[len(key) : len(key) + 1] in _BOUNDARY_CHARS
    )


def _court_from_content(content: str, edition: str | None = None) -> str | None:
    """Resolve parenthetical CONTENT (already extracted) to a courts-db id.

    Shared by the following-parenthetical (rule 4) and preceding-
    parenthetical (California style) channels. Refuses rather than guesses:
    unknown forms, state-gate conflicts, and ordinal-remainder swallows all
    return None. A RECOGNIZED bare form whose state the citation's own
    reporter cannot prove returns _REFUSE instead — the caller must treat
    it as "this parenthetical is the citation's signal and it resolves
    nothing", defeating any eyecite claim that rode the same text."""
    content = content.strip().translate(_QUOTE_TRANSLATION)
    ed = edition or ""
    if any(_prefix_match(content, form) for form in _APPDIV_FORMS):
        if ed.startswith(_NY_EDITION_PREFIXES):
            return "nyappdiv"
        if ed.startswith(_NJ_EDITION_PREFIXES):
            return "njsuperctappdiv"
        return _REFUSE  # "App. Div." without a state-identifying reporter
    # Bare "(Ct. App.)" / "(App.)" — state-gated (7.8.2a). Only truly bare
    # content (remainder empty or a year) qualifies; longer genuine
    # courts-db strings ("Ct. App. Nev.") fall through to the index.
    for lead, gate in (("Ct. App.", _CT_APP_EDITION_GATE), ("App.", _APP_EDITION_GATE)):
        if _prefix_match(content, lead) and _BARE_REMAINDER.match(
            content[len(lead) :].strip(" ,")
        ):
            for prefixes, court_id in gate:
                if ed.startswith(prefixes):
                    return court_id
            return _REFUSE
    if ed.startswith("Ala."):
        for lead, court_id in _ALA_DIVISION_GATE:
            if _prefix_match(content, lead) and _BARE_REMAINDER.match(
                content[len(lead) :].strip(" ,")
            ):
                return court_id
    if _FLA_DCA.match(content):
        court_id = "fladistctapp"
        if edition and _state_conflict(edition, court_id):
            return None
        return court_id
    if _LA_CIRCUIT.match(content):
        court_id = "lactapp"
        if edition and _state_conflict(edition, court_id):
            return None
        return court_id
    if ed.startswith("Ohio") and _OHIO_DISTRICT.match(content):
        return "ohioctapp"
    # Curated forms courts-db lacks (7.8.2b): checked before the index so
    # the state's shortest string can no longer swallow them. Same state
    # gate as index matches.
    for key, court_id in _CURATED_COURT_FORMS:
        if _prefix_match(content, key):
            if edition and _state_conflict(edition, court_id):
                return None
            return court_id
    index, keys_longest_first = _citation_string_index()
    for key in keys_longest_first:
        if _prefix_match(content, key):
            remainder = content[len(key) :].lstrip(" ,")
            if _ORDINAL_REMAINDER.match(remainder):
                # "Fla. 1st DCA …" reached the "Fla." key: the content
                # continues with MORE court text, so this match is a
                # shorter court swallowing a longer form. Refuse it (a
                # longer key would already have matched above).
                continue
            court_id = index[key]
            # State gate: a prefix match whose court sits outside the
            # reporter's own state set is a misattribution, not a signal.
            if edition and _state_conflict(edition, court_id):
                return None
            return court_id
    return None


def _first_court_parenthetical(following_text: str) -> str | None:
    """Content of the first following parenthetical that is not a paragraph
    pinpoint, or None. Skips at most two ¶-parentheticals (Mississippi
    writes one; two is margin, unbounded scanning is not)."""
    window = following_text
    for _ in range(3):
        match = _ANY_PARENTHETICAL.match(window)
        if not match:
            return None
        content = match.group("content").strip()
        if _PARAGRAPH_PARENTHETICAL.match(content):
            window = window[match.end() :]
            continue
        return content
    return None


def _court_from_parenthetical(following_text: str, edition: str | None = None) -> str | None:
    content = _first_court_parenthetical(following_text)
    if content is None:
        return None
    return _court_from_content(content, edition)


def _court_from_preceding(preceding_text: str, edition: str | None = None) -> str | None:
    """Court from the parenthetical immediately BEFORE the citation.

    California style places the court parenthetical ahead of the cite —
    "E. & J. Gallo Winery v. Andina Licores S.A. (9th Cir. 2006) 446 F.3d
    984" — so the preceding parenthetical is the citation's own signal
    there. The content must end with a year (stripped before matching);
    a year-only parenthetical ("(2018)") names no court."""
    match = _PRECEDING_PARENTHETICAL.search(preceding_text or "")
    if not match:
        return None
    content = _TRAILING_YEAR.sub("", match.group("content").strip()).strip(" ,")
    if not content:
        return None
    return _court_from_content(content, edition)


def _adjacent_parenthetical_exists(following_text: str, preceding_text: str) -> bool:
    """True when the citation has ANY adjacent parenthetical that could
    carry a court — the corroboration surface for an eyecite court claim.
    A year-only preceding parenthetical does not count, and neither does a
    ¶-pinpoint parenthetical (7.8.2c): a paragraph pin is pin material, so
    a claim whose only adjacency is "(¶13)" has the same no-parenthetical
    overreach signature the 1.3.0 rule refuses."""
    if _first_court_parenthetical(following_text or "") is not None:
        return True
    match = _PRECEDING_PARENTHETICAL.search(preceding_text or "")
    if not match:
        return False
    content = _TRAILING_YEAR.sub("", match.group("content").strip()).strip(" ,")
    return bool(content)


# --- state-consistency gate (1.2.0) ---
# reporters-db ties most state reporters to a small state set via
# mlz_jurisdiction ("us:ny;supreme.court" -> ny). A claimed court — from
# eyecite's metadata.court or a rule-4 prefix match — located in a state
# OUTSIDE the reporter's own set is refused (measured trigger: eyecite
# claims the D.C. court 'supctdc' from "(Sup. Ct. 2004)" after a N.Y.
# "Misc. 3d" cite). The gate is deliberately inert when either side is
# unknown: federal/national reporters have no state set, and courts-db
# locations outside the table below (federal courts' "United States",
# foreign and territorial-era locations) never conflict.

_LOCATION_STATE: dict[str, str] = {
    "Alabama": "al", "Alaska": "ak", "Arizona": "az", "Arkansas": "ar",
    "California": "ca", "Colorado": "co", "Connecticut": "ct",
    "Delaware": "de", "Florida": "fl", "Georgia": "ga", "Hawaii": "hi",
    "Idaho": "id", "Illinois": "il", "Indiana": "in", "Iowa": "ia",
    "Kansas": "ks", "Kentucky": "ky", "Louisiana": "la", "Maine": "me",
    "Maryland": "md", "Massachusetts": "ma", "Michigan": "mi",
    "Minnesota": "mn", "Mississippi": "ms", "Missouri": "mo",
    "Montana": "mt", "Nebraska": "ne", "Nevada": "nv",
    "New Hampshire": "nh", "New Jersey": "nj", "New Mexico": "nm",
    "New York": "ny", "North Carolina": "nc", "North Dakota": "nd",
    "Ohio": "oh", "Oklahoma": "ok", "Oregon": "or", "Pennsylvania": "pa",
    "Rhode Island": "ri", "South Carolina": "sc", "South Dakota": "sd",
    "Tennessee": "tn", "Texas": "tx", "Utah": "ut", "Vermont": "vt",
    "Virginia": "va", "Washington": "wa", "West Virginia": "wv",
    "Wisconsin": "wi", "Wyoming": "wy",
    # D.C. appears under several spellings (one a courts-db typo).
    "D.C.": "dc", "DC": "dc", "Washington D.C.": "dc", "Washignton D.C.": "dc",
    "Puerto Rico": "pr", "Guam": "gu", "Virgin Islands": "vi",
    "American Samoa": "as", "Northern Mariana Islands": "mp",
}


@lru_cache(maxsize=1)
def _edition_state_table() -> dict[str, frozenset[str]]:
    """Edition string -> the state codes reporters-db ties it to.

    An edition is absent from the table (no constraint) when any reporter
    entry carrying it is national/federal-scoped ("us;...") or has no
    mlz_jurisdiction data at all.
    """
    table: dict[str, set[str] | None] = {}
    for entries in REPORTERS.values():
        for entry in entries:
            states: set[str] = set()
            unconstrained = False
            mlz = entry.get("mlz_jurisdiction") or []
            if not mlz:
                unconstrained = True
            for j in mlz:
                head = j.split(";", 1)[0]
                parts = head.split(":")
                if parts[0] != "us":
                    continue
                if len(parts) >= 2 and parts[1]:
                    states.add(parts[1])
                else:
                    unconstrained = True  # "us;..." national scope
            for ed in entry.get("editions") or {}:
                if unconstrained or not states:
                    table[ed] = None
                elif table.get(ed, set()) is not None:
                    table[ed] = (table.get(ed) or set()) | states
    return {ed: frozenset(s) for ed, s in table.items() if s}


@lru_cache(maxsize=1)
def _court_state_table() -> dict[str, str]:
    return {
        c["id"]: _LOCATION_STATE[loc]
        for c in courts_db.courts
        if (loc := (c.get("location") or "").strip()) in _LOCATION_STATE
    }


def _state_conflict(edition: str | None, court_id: str) -> bool:
    """True when the reporter's state set and the court's state both exist
    and disagree — the only case the gate acts on."""
    states = _edition_state_table().get(edition or "")
    court_state = _court_state_table().get(court_id)
    return bool(states) and court_state is not None and court_state not in states


# Federal appellate courts have no state location, so the state gate above
# is inert for them — but a STATE-scoped reporter can never be a federal
# appellate citation ("30 Cal.App.5th 696" claimed as ca9, measured on the
# 2026-08-09 state corpus run: eyecite overreach in a table of authorities).
_FEDERAL_APPELLATE_IDS = frozenset({"scotus", "cadc", "cafc"} | {f"ca{n}" for n in range(1, 12)})


def _federal_appellate_conflict(edition: str | None, court_id: str) -> bool:
    return court_id in _FEDERAL_APPELLATE_IDS and bool(
        _edition_state_table().get(edition or "")
    )


# Reporter-edition inference table (rule 5): corpus-derived, guarded,
# curated; see scripts/build_reporter_map.py and DECISIONS 2026-08-01.
@lru_cache(maxsize=1)
def _reporter_registries_doc() -> dict:
    raw = resources.files("nvnm_cite.normalizer").joinpath("reporter_registries.json").read_text()
    return json.loads(raw)


@lru_cache(maxsize=1)
def _reporter_registry_table() -> dict[str, str]:
    return {ed: e["registry"] for ed, e in _reporter_registries_doc()["editions"].items()}


@lru_cache(maxsize=1)
def _lexis_editions_present() -> frozenset[str]:
    return frozenset(_reporter_registries_doc().get("lexis_editions_present", []))


# --- same-state family candidates (rule 5b, 1.3.0) ---


@lru_cache(maxsize=1)
def _families_table() -> dict[str, dict]:
    return dict(_reporter_registries_doc().get("families", {}))


@lru_cache(maxsize=1)
def _registry_families_table() -> dict[str, list[str]]:
    return dict(_reporter_registries_doc().get("registry_families", {}))


def family_candidates(edition: str | None) -> list[str]:
    """Ordered same-state registries an edition's corpus population spans
    (share-descending), or [] when the edition has no family entry."""
    entry = _families_table().get(edition or "")
    if not entry:
        return []
    return [c["registry"] for c in entry["candidates"]]


def lookup_candidates(edition: str | None, registry: str | None) -> list[str]:
    """Every registry a keyed existence lookup should try, in order.

    The routed registry first, then the edition's same-state family
    candidates, then the routed registry's district siblings (the corpus
    splits some intermediate courts across a parent registry and
    per-district ones — measured: us-texapp vs us-txctapp1..14). The
    verifier resolves each with a live keyed read and reports the registry
    that answered; a miss is a miss across ALL of them."""
    out: list[str] = []
    if registry:
        out.append(registry)
    for name in family_candidates(edition):
        if name not in out:
            out.append(name)
    if registry:
        for name in _registry_families_table().get(registry, []):
            if name not in out:
                out.append(name)
    return out


def vendor_kind(edition: str | None) -> str | None:
    """"Westlaw"/"LEXIS" when the edition is a vendor database identifier."""
    if not edition:
        return None
    if edition == "WL":
        return "Westlaw"
    if edition == "LEXIS" or edition.endswith(" LEXIS"):
        return "LEXIS"
    return None


def vendor_in_key_space(edition: str | None) -> bool:
    """True when this vendor edition holds records in the corpus (measured
    2026-08-01: 92+ court-specific LEXIS editions, 3.28M parallel keys).
    These behave as reporters — the inference table or a court parenthetical
    can map them and a keyed lookup can genuinely hit. WL and the generic /
    federal LEXIS families hold ZERO records, so a lookup can never hit and
    the verifier reports them as outside coverage without a chain read."""
    return bool(edition) and edition in _lexis_editions_present()


def registry_for_court(court_id: str) -> str:
    """Registry name for a courts-db court ID. Raises if the ID is unknown."""
    if court_id not in _VALID_COURT_IDS:
        raise ValueError(f"unknown courts-db id: {court_id!r}")
    return REGISTRY_PREFIX + court_id


def map_citation(
    citation: CaseCitation, following_text: str = "", preceding_text: str = ""
) -> tuple[str | None, str | None]:
    """(registry, None) when the citation maps cleanly, else (None, reason).

    following_text is the cleaned text immediately after the citation span
    (circuit fallback + rule-4 parenthetical); preceding_text is the cleaned
    text immediately before it (California style puts the court parenthetical
    ahead of the cite). A (None, reason) result means AMBIGUOUS_JURISDICTION
    to the caller.
    """
    edition = citation.corrected_reporter()
    if edition in SCOTUS_EDITIONS:
        return REGISTRY_PREFIX + "scotus", None

    table_default = _reporter_registry_table().get(edition or "")

    # The citation's OWN adjacent parentheticals — the strongest local
    # signal after the reporter itself. Following (Bluebook) outranks
    # preceding (California style) when both are readable. _REFUSE is
    # truthy, so a recognized-but-unresolvable form propagates here too.
    following_court = _circuit_from_following_text(following_text) or _court_from_parenthetical(
        following_text, edition
    )
    preceding_court = _court_from_preceding(preceding_text, edition)
    adjacent = following_court or preceding_court
    refused = adjacent == _REFUSE
    if refused:
        adjacent = None

    court = (citation.metadata.court or "").strip()
    if court and (_state_conflict(edition, court) or _federal_appellate_conflict(edition, court)):
        # eyecite's claimed court is impossible for the citation's own
        # reporter (measured: 'supctdc' for a N.Y. Misc. 3d cite; 'ca9' for
        # a Cal.App.5th cite via table-of-authorities overreach). The
        # reporter is part of the citation itself — drop the claim and let
        # the citation's own signals decide.
        court = ""
    if court and court not in _VALID_COURT_IDS:
        # eyecite court IDs come from courts-db, so this branch should be
        # unreachable; if the libraries ever skew, refuse rather than guess.
        return None, f"court id {court!r} not found in courts-db"
    if court:
        if court in (following_court, preceding_court):
            return REGISTRY_PREFIX + court, None
        if adjacent is not None:
            # The citation's own adjacent parenthetical names a DIFFERENT
            # court: eyecite's forward scan overreached onto a neighboring
            # citation (measured: "(2d Cir. 2010) 603 F.3d 23" claimed as
            # 'cal' from the NEXT authority's parenthetical). The local
            # parenthetical wins.
            return REGISTRY_PREFIX + adjacent, None
        if refused:
            # The adjacent parenthetical is a RECOGNIZED bare form the
            # citation's own reporter cannot resolve to a state ("(Ct.
            # App. 2020)" after S.E.2d). eyecite's claim rode that same
            # text and can only be a guess dressed as data — measured:
            # ctappindterr, a court dead since 1907, on live 2020s
            # strings. Drop the claim; rules 5/5b/6 decide.
            court = ""
        windows_provided = bool(following_text or preceding_text)
        if court and (
            not windows_provided
            or _adjacent_parenthetical_exists(following_text, preceding_text)
        ):
            # Either the caller gave no document context (a bare
            # map_citation call — nothing to corroborate against), or an
            # adjacent parenthetical exists that our index cannot read and
            # eyecite likely read that same parenthetical with richer
            # patterns. Keep the 2026-08-02 rule: the reporter's own
            # default outranks an uncorroborated contradicting claim.
            claimed = REGISTRY_PREFIX + court
            if table_default is None or claimed == table_default:
                return claimed, None
            return table_default, None
        # Document context was provided and holds NO adjacent parenthetical:
        # the claim's source parenthetical belongs to some OTHER citation —
        # the measured table-of-authorities overreach signature. Refuse the
        # claim; rules 5/5b/6 decide.
        court = ""

    if adjacent is not None:
        return REGISTRY_PREFIX + adjacent, None

    if table_default is not None:
        return table_default, None

    family = family_candidates(edition)
    if family:
        # Rule 5b: the edition's whole corpus population sits in one
        # state's family of registries. Route to the dominant one; the
        # verifier sweeps the rest (lookup_candidates) before reporting a
        # miss, and the answering registry is disclosed.
        return family[0], None

    if edition in AMBIGUOUS_FEDERAL_REPORTERS:
        return None, f"{edition} citation with no recognizable court parenthetical"
    return None, "no recognizable court parenthetical"
