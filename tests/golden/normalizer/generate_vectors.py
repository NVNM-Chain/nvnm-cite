"""Generate vectors.json for the normalizer golden suite (task 1.6).

Expectations are hand-derived from docs/canonical-citation-spec.md via the
static tables below; this script never imports nvnm_cite, so the suite stays
an independent statement of intended behavior. Where a spec-derived
expectation disagreed with measured eyecite behavior, the resolution was
adjudicated by hand and recorded in DECISIONS.md, then encoded here.

Run: python tests/golden/normalizer/generate_vectors.py
"""

from __future__ import annotations

import json
from pathlib import Path

OK = "ok"
AMB = "ambiguous_jurisdiction"
VEN = "vendor"
UNR = "unresolved"

VECTORS: list[dict] = []


def vec(category: str, text: str, expect: list[dict]) -> None:
    VECTORS.append(
        {
            "id": f"{category}-{sum(v['category'] == category for v in VECTORS) + 1:03d}",
            "category": category,
            "text": text,
            "expect": expect,
        }
    )


def full(as_written: str, canonical: str | None, registry: str | None,
         disposition: str = OK, kind: str = "full") -> dict:
    return {
        "as_written": as_written,
        "canonical": canonical,
        "registry": registry,
        "disposition": disposition,
        "kind": kind,
    }


# --- 1. SCOTUS editions: every reporter family x spelling variants ---------
SCOTUS_BASES = [(410, 113), (347, 483), (558, 310), (565, 400), (576, 644)]
SCOTUS_SPELLINGS = [
    ("U.S.", "U.S."),
    ("U. S.", "U.S."),
    ("S. Ct.", "S. Ct."),
    ("S.Ct.", "S. Ct."),
    ("L. Ed. 2d", "L. Ed. 2d"),
    ("L.Ed.2d", "L. Ed. 2d"),
    ("L. Ed.", "L. Ed."),
    ("L.Ed.", "L. Ed."),
]
for vol, page in SCOTUS_BASES:
    for written, edition in SCOTUS_SPELLINGS:
        aw = f"{vol} {written} {page}"
        vec(
            "scotus_editions",
            f"See Alpha v. Beta, {aw} (1990).",
            [full(aw, f"{vol} {edition} {page}", "us-scotus")],
        )

# --- 2. Circuit parentheticals: federal appellate reporters x circuits -----
CIRCUITS = [
    ("1st Cir.", "us-ca1"), ("2d Cir.", "us-ca2"), ("3d Cir.", "us-ca3"),
    ("4th Cir.", "us-ca4"), ("5th Cir.", "us-ca5"), ("6th Cir.", "us-ca6"),
    ("7th Cir.", "us-ca7"), ("8th Cir.", "us-ca8"), ("9th Cir.", "us-ca9"),
    ("10th Cir.", "us-ca10"), ("11th Cir.", "us-ca11"), ("D.C. Cir.", "us-cadc"),
    ("Fed. Cir.", "us-cafc"),
]
FED_REPORTERS = [("F.2d", 800), ("F.3d", 925), ("F.4th", 50), ("F. App'x", 789)]
for rep, vol in FED_REPORTERS:
    for paren, registry in CIRCUITS:
        aw = f"{vol} {rep} 1339"
        vec(
            "circuit_parentheticals",
            f"Gamma v. Delta, {aw}, 1345 ({paren} 2019).",
            [full(aw, aw, registry)],
        )

# spacing variants with a parenthetical
for written, edition in [("F. 3d", "F.3d"), ("F. 4th", "F.4th"), ("F. 2d", "F.2d")]:
    aw = f"925 {written} 1339"
    vec(
        "circuit_parentheticals",
        f"Gamma v. Delta, {aw} (11th Cir. 2019).",
        [full(aw, f"925 {edition} 1339", "us-ca11")],
    )

# no-pin variant across every circuit
for paren, registry in CIRCUITS:
    vec(
        "circuit_parentheticals",
        f"Kappa v. Lambda, 412 F.3d 88 ({paren} 2005).",
        [full("412 F.3d 88", "412 F.3d 88", registry)],
    )

# --- 3. Federal reporters, no parenthetical: ambiguous, canonical kept -----
for rep, vol, page in [
    ("F.", 300, 57), ("F.2d", 800, 100), ("F.3d", 538, 1000), ("F.4th", 50, 700),
    ("F. App'x", 789, 12), ("F. Supp.", 100, 9), ("F. Supp. 2d", 200, 19),
    ("F. Supp. 3d", 300, 29),
]:
    aw = f"{vol} {rep} {page}"
    vec(
        "federal_no_parenthetical",
        f"Epsilon v. Zeta, {aw}.",
        [full(aw, aw, None, AMB)],
    )
# with a pin but still no court: first-page key survives, still ambiguous
for rep, vol, page, pin in [
    ("F.3d", 538, 1000, 1004), ("F.2d", 800, 100, 105),
    ("F.4th", 50, 700, 702), ("F. Supp. 2d", 200, 19, 25),
]:
    aw = f"{vol} {rep} {page}"
    vec(
        "federal_no_parenthetical",
        f"Epsilon v. Zeta, {aw}, {pin} (2010).",
        [full(aw, aw, None, AMB)],
    )

# --- 4. District parentheticals -------------------------------------------
DISTRICTS = [
    ("S.D.N.Y.", "us-nysd"), ("E.D.N.Y.", "us-nyed"),
    ("N.D. Ga.", "us-gand"), ("S.D. Fla.", "us-flsd"),
    ("N.D. Cal.", "us-cand"), ("D. Mass.", "us-mad"),
    ("S.D. Tex.", "us-txsd"), ("D.N.J.", "us-njd"),
]
for rep, vol in [("F. Supp.", 100), ("F. Supp. 2d", 200), ("F. Supp. 3d", 300)]:
    for paren, registry in DISTRICTS:
        aw = f"{vol} {rep} 99"
        vec(
            "district_parentheticals",
            f"Eta v. Theta, {aw} ({paren} 2015).",
            [full(aw, aw, registry)],
        )

# --- 5. Line-break mangled --------------------------------------------------
MANGLED = [
    ("410\nU.S. 113", "410 U.S. 113", "410 U.S. 113", "us-scotus"),
    ("410 U.S.\n113", "410 U.S. 113", "410 U.S. 113", "us-scotus"),
    ("410\nU. S.\n113", "410 U. S. 113", "410 U.S. 113", "us-scotus"),
    ("132\nS. Ct. 945", "132 S. Ct. 945", "132 S. Ct. 945", "us-scotus"),
    ("181 L. Ed.\n2d 911", "181 L. Ed. 2d 911", "181 L. Ed. 2d 911", "us-scotus"),
]
for written, aw_clean, canonical, registry in MANGLED:
    vec(
        "line_break_mangled",
        f"See Iota v. Kappa, {written} (1990), on point.",
        [full(aw_clean, canonical, registry)],
    )
for written, aw_clean, canonical in [
    ("925 F.\n3d 1339", "925 F. 3d 1339", "925 F.3d 1339"),
    ("925\nF.3d\n1339", "925 F.3d 1339", "925 F.3d 1339"),
]:
    vec(
        "line_break_mangled",
        f"Lambda v. Mu, {written} (11th Cir. 2019).",
        [full(aw_clean, canonical, "us-ca11")],
    )
# breaks in the case name and inside the parenthetical
vec(
    "line_break_mangled",
    "Varghese v.\nChina S. Airlines Co., 925 F.3d 1339 (11th\nCir. 2019).",
    [full("925 F.3d 1339", "925 F.3d 1339", "us-ca11")],
)
vec(
    "line_break_mangled",
    "Roe v.\nWade, 410 U.S. 113, 116\n(1973), held otherwise.",
    [full("410 U.S. 113", "410 U.S. 113", "us-scotus")],
)
vec(
    "line_break_mangled",
    "See Eta v. Theta, 200 F. Supp.\n2d 19 (S.D.N.Y. 2002).",
    [full("200 F. Supp. 2d 19", "200 F. Supp. 2d 19", "us-nysd")],
)

# --- 6. Short-form chains ----------------------------------------------------
vec(
    "short_form_chains",
    "Roe v. Wade, 410 U.S. 113, 116 (1973), controls. Roe, 410 U.S. at 120. Id. at 121.",
    [
        full("410 U.S. 113", "410 U.S. 113", "us-scotus"),
        full("410 U.S. at 120", "410 U.S. 113", "us-scotus", OK, "short"),
        full("Id.", "410 U.S. 113", "us-scotus", OK, "id"),
    ],
)
vec(
    "short_form_chains",
    "Varghese v. China S. Airlines Co., 925 F.3d 1339 (11th Cir. 2019). Varghese, 925 F.3d at 1345.",
    [
        full("925 F.3d 1339", "925 F.3d 1339", "us-ca11"),
        full("925 F.3d at 1345", "925 F.3d 1339", "us-ca11", OK, "short"),
    ],
)
vec(
    "short_form_chains",
    "Roe v. Wade, 410 U.S. 113 (1973). Roe, supra, at 120.",
    [
        full("410 U.S. 113", "410 U.S. 113", "us-scotus"),
        full("supra,", "410 U.S. 113", "us-scotus", OK, "supra"),
    ],
)
vec(
    "short_form_chains",
    "Smith v. Doe, 538 F.3d 1000 (9th Cir. 2008). Id. at 1005. Id.",
    [
        full("538 F.3d 1000", "538 F.3d 1000", "us-ca9"),
        full("Id.", "538 F.3d 1000", "us-ca9", OK, "id"),
        full("Id.", "538 F.3d 1000", "us-ca9", OK, "id"),
    ],
)
# interleaved: the short cite re-anchors by volume/reporter
vec(
    "short_form_chains",
    "Brown v. Board, 347 U.S. 483 (1954). Roe v. Wade, 410 U.S. 113 (1973). Brown, 347 U.S. at 490.",
    [
        full("347 U.S. 483", "347 U.S. 483", "us-scotus"),
        full("410 U.S. 113", "410 U.S. 113", "us-scotus"),
        full("347 U.S. at 490", "347 U.S. 483", "us-scotus", OK, "short"),
    ],
)

# interleaved chains with id. retargeting and a supra with pin
vec(
    "short_form_chains",
    "Roe v. Wade, 410 U.S. 113 (1973). Id. at 116. Brown v. Board, 347 U.S. 483 (1954). Id. at 490.",
    [
        full("410 U.S. 113", "410 U.S. 113", "us-scotus"),
        full("Id.", "410 U.S. 113", "us-scotus", OK, "id"),
        full("347 U.S. 483", "347 U.S. 483", "us-scotus"),
        full("Id.", "347 U.S. 483", "us-scotus", OK, "id"),
    ],
)
vec(
    "short_form_chains",
    "Varghese v. China S. Airlines Co., 925 F.3d 1339 (11th Cir. 2019), guides. Varghese, supra, at 1345.",
    [
        full("925 F.3d 1339", "925 F.3d 1339", "us-ca11"),
        full("supra,", "925 F.3d 1339", "us-ca11", OK, "supra"),
    ],
)
vec(
    "short_form_chains",
    "Smith v. Doe, 538 F.3d 1000 (9th Cir. 2008). Smith, 538 F.3d at 1003. Id.",
    [
        full("538 F.3d 1000", "538 F.3d 1000", "us-ca9"),
        full("538 F.3d at 1003", "538 F.3d 1000", "us-ca9", OK, "short"),
        full("Id.", "538 F.3d 1000", "us-ca9", OK, "id"),
    ],
)

# --- 7. Orphan short forms ----------------------------------------------------
vec("orphans", "Id. at 5, as previously noted.",
    [full("Id.", None, None, UNR, "id")])
vec("orphans", "See 410 U.S. at 120 for the discussion.",
    [full("410 U.S. at 120", None, None, UNR, "short")])
vec("orphans", "Nu, supra, at 10, settles it.",
    [full("supra,", None, None, UNR, "supra")])
vec("orphans", "925 F.3d at 1345 is the page cited.",
    [full("925 F.3d at 1345", None, None, UNR, "short")])
vec(
    "orphans",
    "The brief opens with Id. at 3, then cites Roe v. Wade, 410 U.S. 113 (1973).",
    [
        full("Id.", None, None, UNR, "id"),
        full("410 U.S. 113", "410 U.S. 113", "us-scotus"),
    ],
)

# --- 8. Parallel citations -----------------------------------------------------
vec(
    "parallel_citations",
    "Citizens United v. FEC, 558 U.S. 310, 130 S. Ct. 876, 175 L. Ed. 2d 753 (2010).",
    [
        full("558 U.S. 310", "558 U.S. 310", "us-scotus"),
        full("130 S. Ct. 876", "130 S. Ct. 876", "us-scotus"),
        full("175 L. Ed. 2d 753", "175 L. Ed. 2d 753", "us-scotus"),
    ],
)
vec(
    "parallel_citations",
    "Milkovich v. Lorain Journal Co., 494 U.S. 472, 110 S.Ct. 1249, 108 L.Ed.2d 400 (1990).",
    [
        full("494 U.S. 472", "494 U.S. 472", "us-scotus"),
        full("110 S.Ct. 1249", "110 S. Ct. 1249", "us-scotus"),
        full("108 L.Ed.2d 400", "108 L. Ed. 2d 400", "us-scotus"),
    ],
)
vec(
    "parallel_citations",
    "New York Times Co. v. Sullivan, 376 U.S. 254, 84 S. Ct. 710 (1964).",
    [
        full("376 U.S. 254", "376 U.S. 254", "us-scotus"),
        full("84 S. Ct. 710", "84 S. Ct. 710", "us-scotus"),
    ],
)
vec(
    "parallel_citations",
    "Gertz v. Robert Welch, Inc., 418 U.S. 323, 339-40, 94 S. Ct. 2997, 41 L. Ed. 2d 789 (1974).",
    [
        full("418 U.S. 323", "418 U.S. 323", "us-scotus"),
        full("94 S. Ct. 2997", "94 S. Ct. 2997", "us-scotus"),
        full("41 L. Ed. 2d 789", "41 L. Ed. 2d 789", "us-scotus"),
    ],
)

# --- 9. Early SCOTUS ------------------------------------------------------------
for written, canonical in [
    ("5 U.S. (1 Cranch) 137", "5 U.S. 137"),
    ("17 U.S. (4 Wheat.) 316", "17 U.S. 316"),
    ("60 U.S. (19 How.) 393", "60 U.S. 393"),
    ("2 U.S. (2 Dall.) 419", "2 U.S. 419"),
    ("33 U.S. (8 Pet.) 591", "33 U.S. 591"),
]:
    vec(
        "early_scotus",
        f"Omicron v. Pi, {written} (1850).",
        [full(written, canonical, "us-scotus")],
    )

# --- 10. State reporters ----------------------------------------------------------
STATE_WITH_PAREN = [
    ("123 So. 2d 456", "Fla. 1960", "us-fla"),
    ("456 P.2d 789", "Cal. 1969", "us-cal"),
    ("250 N.E.2d 200", "N.Y. 1969", "us-ny"),
    ("300 S.W.2d 100", "Tex. 1957", "us-tex"),
    ("150 A.2d 50", "Pa. 1959", "us-pa"),
    ("88 So. 3d 90", "Fla. 2012", "us-fla"),
    ("710 N.W.2d 44", "Minn. 2006", "us-minn"),
    ("950 P.3d 11", "Cal. 2024", "us-cal"),
]
for aw, paren, registry in STATE_WITH_PAREN:
    vec(
        "state_reporters",
        f"Rho v. Sigma, {aw} ({paren}).",
        [full(aw, aw, registry)],
    )
for aw in ["123 So. 2d 456", "456 P.2d 789", "250 N.E.2d 200"]:
    vec(
        "state_reporters",
        f"Tau v. Upsilon, {aw}.",
        [full(aw, aw, None, AMB)],
    )

# --- 11. Statutes and journals excluded -------------------------------------------
for text in [
    "The claim arises under 42 U.S.C. § 1983 and 28 U.S.C. § 1331.",
    "See 29 C.F.R. § 1604.11.",
    "See Charles A. Wright, Law of Federal Courts, 103 Harv. L. Rev. 405 (1989).",
    "The claim arises under 42 U.S.C. § 1983. Id.",
    "Pub. L. No. 110-325, 122 Stat. 3553 (2008).",
]:
    vec("non_case_excluded", text, [])
vec(
    "non_case_excluded",
    "Under 42 U.S.C. § 1983 and Monroe v. Pape, 365 U.S. 167 (1961).",
    [full("365 U.S. 167", "365 U.S. 167", "us-scotus")],
)

# --- 12. Pin cites and the first-page rule ------------------------------------------
PIN_FORMS = ["113, 116", "113, 116-17", "113, 113", "113, 159 n.4", "113, 116, 118", "113, 152-53 & n.7"]
for pin in PIN_FORMS:
    vec(
        "first_page_rule",
        f"Roe v. Wade, 410 U.S. {pin} (1973).",
        [full("410 U.S. 113", "410 U.S. 113", "us-scotus")],
    )
vec(
    "first_page_rule",
    "(quoting Roe v. Wade, 410 U.S. 113, 116 (1973)).",
    [full("410 U.S. 113", "410 U.S. 113", "us-scotus")],
)

# --- 13. Unicode and odd whitespace ---------------------------------------------------
vec(
    "unicode_whitespace",
    "See Phi v. Chi, 410 U.S. 113 (1973).",
    [full("410 U.S. 113", "410 U.S. 113", "us-scotus")],
)
vec(
    "unicode_whitespace",
    "Psi v. Omega, 789 F. App’x 12 (11th Cir. 2019).",
    [full("789 F. App’x 12", "789 F. App'x 12", "us-ca11")],
)
vec(
    "unicode_whitespace",
    "Alpha v. Beta, 410 U.S. 113 (1973), with non-breaking spaces.",
    [full("410 U.S. 113", "410 U.S. 113", "us-scotus")],
)
vec(
    "unicode_whitespace",
    "Gamma v. Delta, 410 U.S. 113, 116–17 (1973), en-dash pin range.",
    [full("410 U.S. 113", "410 U.S. 113", "us-scotus")],
)
vec(
    "unicode_whitespace",
    "“Quoted matter.” Roe v. Wade, 410 U.S. 113 (1973).",
    [full("410 U.S. 113", "410 U.S. 113", "us-scotus")],
)

# --- 14. Pending publication / underscores --------------------------------------------
for text in [
    "Recent v. Pending, 596 U.S. ___ (2022), changes nothing here.",
    "Newest v. Slip, 600 U.S. ____, ____ (2023).",
]:
    vec("pending_publication", text, [])

# --- 15. Noise robustness ---------------------------------------------------------------
vec(
    "noise_robustness",
    "compare Roe v. Wade, 410 U.S. 113 (1973), with Doe v. Bolton, 410 U.S. 179 (1973).",
    [
        full("410 U.S. 113", "410 U.S. 113", "us-scotus"),
        full("410 U.S. 179", "410 U.S. 179", "us-scotus"),
    ],
)
vec(
    "noise_robustness",
    "footnote 12: Varghese v. China S. Airlines Co., 925 F.3d 1339, 1345 (11th Cir. 2019); accord Smith v. Doe, 538 F.3d 1000, 1002 (9th Cir. 2008).",
    [
        full("925 F.3d 1339", "925 F.3d 1339", "us-ca11"),
        full("538 F.3d 1000", "538 F.3d 1000", "us-ca9"),
    ],
)
vec("noise_robustness", "No citations live in this sentence about page 113 and volume 410.", [])
vec("noise_robustness", "", [])
vec("noise_robustness", "   \n\n   ", [])
vec(
    "noise_robustness",
    "See, e.g., Roe v. Wade, 410 U.S. 113 (1973); Brown v. Board, 347 U.S. 483 (1954); Smith v. Doe, 538 F.3d 1000 (9th Cir. 2008).",
    [
        full("410 U.S. 113", "410 U.S. 113", "us-scotus"),
        full("347 U.S. 483", "347 U.S. 483", "us-scotus"),
        full("538 F.3d 1000", "538 F.3d 1000", "us-ca9"),
    ],
)
vec(
    "noise_robustness",
    "Affirmed. Sigma v. Tau, 412 F.3d 88, 90 (2d Cir. 2005) (per curiam) (collecting cases).",
    [full("412 F.3d 88", "412 F.3d 88", "us-ca2")],
)

# --- 12. Normalizer 1.1.0 (2026-08-01): expanded jurisdiction mapping ------
# N.Y. Appellate Division: A.D. editions infer us-nyappdiv from the reporter
# table (bare), and the department / "App. Div." parenthetical forms are a
# definitional closed set (courts-db models the four departments as one
# court). Adjudications in DECISIONS 2026-08-01.
vec(
    "ny_appdiv",
    "Podraza v. Carriero, 212 A.D.2d 331 (4th Dep't 1995).",
    [full("212 A.D.2d 331", "212 A.D.2d 331", "us-nyappdiv")],
)
vec(
    "ny_appdiv",
    "Kingsland Land Co. v. Newman, 1 A.D. 1 (App. Div. 1896).",
    [full("1 A.D. 1", "1 A.D. 1", "us-nyappdiv")],
)
vec(
    "ny_appdiv",
    "Bare edition, no parenthetical: Matter of Smith, 100 A.D.3d 500.",
    [full("100 A.D.3d 500", "100 A.D.3d 500", "us-nyappdiv")],
)
vec(
    "ny_appdiv",
    "People v. Jones, 45 N.Y.S.3d 200 (App. Div. 2017).",
    [full("45 N.Y.S.3d 200", "45 N.Y.S.3d 200", "us-nyappdiv")],
)
vec(
    "ny_appdiv",
    # N.Y.S. spans New York courts. 1.3.0: bare routes via the same-state
    # family (rule 5b) — 91% of its corpus population is us-nyappdiv and
    # every >=1% candidate is a New York court; the verifier sweeps the
    # family before reporting a miss.
    "People v. Jones, 45 N.Y.S.3d 200.",
    [full("45 N.Y.S.3d 200", "45 N.Y.S.3d 200", "us-nyappdiv")],
)
vec(
    "ny_appdiv",
    "Bare official reporter infers the Court of Appeals: Palsgraf v. Long Island R.R. Co., 248 N.Y. 339.",
    [full("248 N.Y. 339", "248 N.Y. 339", "us-ny")],
)

# Tax Court: T.C. (curated), T.C. No. and T.C. Memo. (corpus-dominant).
# eyecite reads "T.C. Memo. 1976-300" as volume 1976 / page 300, matching
# the corpus key format exactly.
vec(
    "tax_court",
    "Fehrs v. Commissioner, 65 T.C. 346 (1975).",
    [full("65 T.C. 346", "65 T.C. 346", "us-tax")],
)
vec(
    "tax_court",
    "Smith v. Commissioner, T.C. Memo. 1976-300.",
    [full("T.C. Memo. 1976-300", "1976 T.C. Memo. 300", "us-tax")],
)
vec(
    "tax_court",
    "Jones v. Commissioner, 100 T.C. No. 11 (1993).",
    [full("100 T.C. No. 11", "100 T.C. No. 11", "us-tax")],
)

# Vendor identifiers OUTSIDE the registry key space (WL and the generic /
# federal LEXIS families hold zero corpus records): the verifier reports
# them as outside coverage with no chain read (disposition VENDOR).
vec(
    "vendor_cites",
    "LAM Wholesale, LLC v. United Airlines, Inc., 2019 WL 1439098 (E.D.N.Y. 2019).",
    [full("2019 WL 1439098", "2019 WL 1439098", None, VEN)],
)
vec(
    "vendor_cites",
    "Doe v. Roe, 2019 U.S. App. LEXIS 12345 (1st Cir. 2019).",
    [full("2019 U.S. App. LEXIS 12345", "2019 U.S. App. LEXIS 12345", None, VEN)],
)
vec(
    "vendor_cites",
    # Court-specific LEXIS editions ARE corpus keys (3.28M parallel records
    # on chain): dominance-clean ones map from the table like any reporter.
    "State v. Doe, 1894 La. LEXIS 577.",
    [full("1894 La. LEXIS 577", "1894 La. LEXIS 577", "us-la")],
)
vec(
    "vendor_cites",
    # A corpus-present LEXIS edition the dominance guard keeps OUT of the
    # table (a real us-nysupct second population): bare stays VENDOR...
    # 1.3.0: this LEXIS edition's genuine nyappdiv/nysupct split is a same-
    # state family, so the bare form routes to the dominant registry and the
    # verifier sweeps both — 3.28M court-specific LEXIS keys are real
    # parallel keys on chain (supersedes the 1.1.0 vendor-bare posture for
    # same-state-family LEXIS editions).
    "Doe v. Roe, 1912 N.Y. App. Div. LEXIS 7085.",
    [full("1912 N.Y. App. Div. LEXIS 7085", "1912 N.Y. App. Div. LEXIS 7085", "us-nyappdiv")],
)
vec(
    "vendor_cites",
    # ...but an explicit court parenthetical still maps it (a lookup there
    # can genuinely hit — the keys are on chain).
    "Doe v. Roe, 1912 N.Y. App. Div. LEXIS 7085 (N.Y. App. Div. 1912).",
    [full("1912 N.Y. App. Div. LEXIS 7085", "1912 N.Y. App. Div. LEXIS 7085", "us-nyappdiv")],
)

# Reporter-edition inference across court classes (corpus-dominant table).
vec(
    "reporter_inference",
    "Bare state officials: People v. A, 61 Cal. 2d 529; Baker v. B, 37 Ill. 2d 111; C v. D, 219 Ga. 555.",
    [
        full("61 Cal. 2d 529", "61 Cal. 2d 529", "us-cal"),
        full("37 Ill. 2d 111", "37 Ill. 2d 111", "us-ill"),
        full("219 Ga. 555", "219 Ga. 555", "us-ga"),
    ],
)
vec(
    "reporter_inference",
    "Neutral formats: In re T, 2013 IL App (1st) 111279-U; State v. U, 2019 OK 5.",
    [
        full("2013 IL App (1st) 111279-U", "2013 IL App (1st) 111279-U", "us-illappct"),
        full("2019 OK 5", "2019 OK 5", "us-okla"),
    ],
)
vec(
    "reporter_inference",
    "Intermediate courts: E v. F, 300 Ill. App. 3d 673; G v. H, 45 Cal. App. 4th 100.",
    [
        full("300 Ill. App. 3d 673", "300 Ill. App. 3d 673", "us-illappct"),
        full("45 Cal. App. 4th 100", "45 Cal. App. 4th 100", "us-calctapp"),
    ],
)

# The general court-parenthetical fallback (courts-db citation strings are
# globally unique) and its precedence over the reporter default.
vec(
    "parenthetical_index",
    "State v. Brown, 100 Ohio St. 3d 500 (Ohio Ct. App. 2003).",
    [full("100 Ohio St. 3d 500", "100 Ohio St. 3d 500", "us-ohioctapp")],
)
vec(
    "parenthetical_index",
    "Doe v. Agency, 50 F. Supp. 3d 10 (D. Mass. 2014).",
    [full("50 F. Supp. 3d 10", "50 F. Supp. 3d 10", "us-mad")],
)

# What must STAY ambiguous under 1.1.0: multi-court reporters with no court
# signal (never guess).
vec(
    "still_ambiguous",
    "Baz v. Qux, 500 S.W.3d 100.",
    [full("500 S.W.3d 100", "500 S.W.3d 100", None, AMB)],
)
vec(
    "still_ambiguous",
    "United States v. Smith, 54 M.J. 783.",
    [full("54 M.J. 783", "54 M.J. 783", None, AMB)],
)
vec(
    "still_ambiguous",
    "Foo v. Bar, 100 F.3d 200.",
    [full("100 F.3d 200", "100 F.3d 200", None, AMB)],
)

# --- 13. Normalizer 1.2.0 (2026-08-02): real-filings corpus-run fixes ------
# (a) Orphan short-form fallback: a short cite eyecite strands attaches to
# the same-volume/edition full cite whose first page bounds the pin page;
# two same-volume candidates split by the page window (Gratz 244 / Grutter
# 306: "at 331" -> Grutter, "at 270" -> Gratz).
OOS = "out_of_scope"
vec(
    "short_fallback",
    "Grutter v. Bollinger, 539 U.S. 306 (2003), and Gratz v. Bollinger, "
    "539 U.S. 244 (2003), control. Deference applies, 539 U.S. at 331; "
    "quotas do not, 539 U.S. at 270.",
    [
        full("539 U.S. 306", "539 U.S. 306", "us-scotus"),
        full("539 U.S. 244", "539 U.S. 244", "us-scotus"),
        full("539 U.S. at 331", "539 U.S. 306", "us-scotus", OK, "short"),
        full("539 U.S. at 270", "539 U.S. 244", "us-scotus", OK, "short"),
    ],
)
vec(
    "short_fallback",
    "Otto v. City of Boca Raton, 981 F.3d 854 (11th Cir. 2020), controls. "
    "The panel said so, 981 F.3d at 860.",
    [
        full("981 F.3d 854", "981 F.3d 854", "us-ca11"),
        full("981 F.3d at 860", "981 F.3d 854", "us-ca11", OK, "short"),
    ],
)
# A pin page BELOW every candidate's first page cannot belong to any of
# them: the short stays an orphan rather than guessing. (Two same-volume
# candidates, so eyecite itself strands the short and the fallback tier —
# where the page window lives — is what decides; with a single antecedent
# eyecite resolves natively without any page check, measured 2.7.6.)
vec(
    "short_fallback",
    "Grutter v. Bollinger, 539 U.S. 306 (2003), and Gratz v. Bollinger, "
    "539 U.S. 244 (2003), control. See 539 U.S. at 200.",
    [
        full("539 U.S. 306", "539 U.S. 306", "us-scotus"),
        full("539 U.S. 244", "539 U.S. 244", "us-scotus"),
        full("539 U.S. at 200", None, None, UNR, "short"),
    ],
)
# (b) Law-section tokens (§ fragments) are OUT_OF_SCOPE, never unparseable
# case citations (measured shapes from the real-filings run).
vec(
    "law_sections",
    "The Act, 42 U.S.C. §2000d, applies. See also §2101(e).",
    [
        full("§2000d,", None, None, OOS, "unknown"),
        full("§2101(e).", None, None, OOS, "unknown"),
    ],
)
# (c) State-consistency gate: eyecite claims the D.C. court 'supctdc' from
# "(Sup. Ct. 2004)" after a N.Y. Misc. 3d cite (measured on the Mata reply
# brief). The claim is still refused; under 1.3.0 the cite then routes via
# the Misc. 3d same-state family (all >=1% candidates are New York courts)
# instead of refusing outright — the verifier sweeps the family.
vec(
    "state_gate",
    "Astudillo v. Port Auth., 7 Misc. 3d 1004(A), *4 (Sup. Ct. 2004) (same).",
    [full("7 Misc. 3d 1004(A)", "7 Misc. 3d 1004(A)", "us-nysupct")],
)
# Gate is inert when the claimed court's state agrees with the reporter's.
vec(
    "state_gate",
    "Matter of Smith, 100 Misc. 2d 500 (N.Y. Sup. Ct. 1979).",
    [full("100 Misc. 2d 500", "100 Misc. 2d 500", "us-nysupct")],
)

# --- 14. Normalizer 1.3.0 (2026-08-09): state-filings corpus-run fixes -----
# (a) Preceding-parenthetical channel: California citation style puts the
# court parenthetical BEFORE the cite ("Name (Court Year) cite"). Measured
# on the CA Supreme Court briefs: without it, eyecite's forward scan claims
# a NEIGHBORING authority's court.
vec(
    "preceding_parenthetical",
    "E. & J. Gallo Winery v. Andina Licores S.A. (9th Cir. 2006) 446 F.3d 984.",
    [full("446 F.3d 984", "446 F.3d 984", "us-ca9")],
)
vec(
    "preceding_parenthetical",
    "Perkins v. CCH Computax, Inc. (N.C. 1992) 423 S.E.2d 780, 784.",
    [full("423 S.E.2d 780", "423 S.E.2d 780", "us-nc")],
)
vec(
    "preceding_parenthetical",
    "Salzberg v. Sciabacucchi (Del. 2020) 227 A.3d 102, 113.",
    [full("227 A.3d 102", "227 A.3d 102", "us-del")],
)
vec(
    "preceding_parenthetical",
    # A year-only preceding parenthetical carries no court signal: a bare
    # federal reporter stays honestly ambiguous.
    "Foo v. Bar (2018) 100 F.3d 200.",
    [full("100 F.3d 200", "100 F.3d 200", None, AMB)],
)
# (b) Table-of-authorities overreach refused: the TOA lists entries with
# dotted leaders, and eyecite attaches the NEXT entry's leading
# parenthetical to the PREVIOUS entry's cite. With no adjacent
# parenthetical of its own, the claim is refused and the citation's own
# signals decide (here: the Cal. App. 5th same-state family). Measured:
# Drulias, claimed 'ca9' from the following Gallo entry.
vec(
    "toa_overreach",
    "Drulias v. 1st Century Bancshares, Inc., (2018) 30 Cal.App.5th 696 "
    "....................... 15, 19, 27 E. & J. Gallo Winery v. Andina "
    "Licores S.A., (9th Cir. 2006) 446 F.3d 984 .......... 12",
    [
        full("30 Cal.App.5th 696", "30 Cal. App. 5th 696", "us-calctapp5d"),
        full("446 F.3d 984", "446 F.3d 984", "us-ca9"),
    ],
)
vec(
    "toa_overreach",
    # The adjacent PRECEDING parenthetical contradicts eyecite's claim
    # (claimed 'cal' from the next entry): the local parenthetical wins.
    "Greenwich Financial Services Distressed Mortg. Fund 3 LLC v. "
    "Countrywide Financial Corp., (2d Cir. 2010) 603 F.3d 23 ........... "
    "18 6 Handoush v. Lease Finance Group, (Cal. 2020) 258 Cal.Rptr.3d 363 "
    "....... 6",
    [
        full("603 F.3d 23", "603 F.3d 23", "us-ca2"),
        full("258 Cal.Rptr.3d 363", "258 Cal. Rptr. 3d 363", "us-cal"),
    ],
)
# (c) Florida DCA forms: courts-db has no citation_string for the DCA
# courts, and "Fla." must never swallow "Fla. 2d DCA" (the ordinal-
# remainder guard). The corpus keys DCA cases under the parent
# fladistctapp. Measured: 60 misroutes to us-fla on the state corpus run.
vec(
    "fla_dca",
    "Masonoff v. State, 546 So. 2d 72, 74 (Fla. 2d DCA 1989).",
    [full("546 So. 2d 72", "546 So. 2d 72", "us-fladistctapp")],
)
vec(
    "fla_dca",
    "Baxter v. State, 389 So. 3d 803 (Fla. 5th DCA 2024) (en banc).",
    [full("389 So. 3d 803", "389 So. 3d 803", "us-fladistctapp")],
)
vec(
    "fla_dca",
    # The supreme court's own form still routes to us-fla.
    "State v. Poole, 297 So. 3d 487 (Fla. 2020).",
    [full("297 So. 3d 487", "297 So. 3d 487", "us-fla")],
)
# (d) Typographic quotes normalize before the courts-db match ("Tex.
# Comm'n App." is straight-quoted in courts-db, curly in real documents).
vec(
    "curly_quotes",
    "Fid. Union Cas. Co. v. Hammock, 248 S.W. 667 "
    "(Tex. Comm’n App. 1923, judgm’t adopted).",
    [full("248 S.W. 667", "248 S.W. 667", "us-texcommnapp")],
)
# (e) Same-state family inference (rule 5b): editions whose whole >=1%
# corpus population sits in one state's registries route to the dominant
# one; the verifier sweeps the siblings. Measured splits: Cal. App. 5th
# 71/29 calctapp5d/calctapp, N.Y.2d 65/35 ny/nyappdiv, Cal. 4th 99.4% cal.
vec(
    "family_inference",
    "Doe v. Roe (2018) 30 Cal.App.5th 696.",
    [full("30 Cal.App.5th 696", "30 Cal. App. 5th 696", "us-calctapp5d")],
)
vec(
    "family_inference",
    "People v. Vivar (1999) 21 Cal.4th 903.",
    [full("21 Cal.4th 903", "21 Cal. 4th 903", "us-cal")],
)
vec(
    "family_inference",
    "Matter of Jamal S., 28 NY3d 92 (2016).",
    [full("28 NY3d 92", "28 N.Y.3d 92", "us-ny")],
)
vec(
    "family_inference",
    "People v. Bing, 76 NY2d 331 (1990).",
    [full("76 NY2d 331", "76 N.Y.2d 331", "us-ny")],
)
vec(
    "family_inference",
    # Multi-STATE regionals have no family and stay ambiguous bare
    # (S.W.3d spans TX/KY/MO/AR/TN in the corpus itself).
    "Baz v. Qux, 700 S.W.3d 100.",
    [full("700 S.W.3d 100", "700 S.W.3d 100", None, AMB)],
)

# --- 15. Normalizer 1.4.0 / task 7.8.1 (2026-08-11): reporter_registries v3
# Remaining-45-states rollout, Session 1 (data only; DECISIONS 2026-08-11).
# The v3 carrier rule admits editions carried by SEVERAL reporters-db
# reporters when every >=1% registry of their corpus records sits in ONE
# state — the states that reused a bound-reporter string as their
# neutral-citation identifier. Every bare form below refused to route
# before v3; every routing below was verified with a live mainnet keyed
# read on 2026-08-11.
# (a) Ohio's webcite is the state's universal modern citation form (110k
# corpus records, 10.7k from 2024+ alone; written hyphenated, keyed in
# space form). Family us-ohioctapp/.86, us-ohio/.11, us-ohioctcl: the
# mapper routes to the dominant candidate and the VERIFIER sweeps the
# family (the Supreme Court's own 2019-Ohio-2450 answers from us-ohio on
# the second read; the Court of Claims' 2002-Ohio-3234 from us-ohioctcl
# on the third).
vec(
    "v3_same_state_carriers",
    "In re Adoption of B.I., 2019-Ohio-2450.",
    [full("2019-Ohio-2450", "2019 Ohio 2450", "us-ohioctapp")],
)
vec(
    "v3_same_state_carriers",
    "Cincinnati v. Beretta U.S.A. Corp., 2002-Ohio-2480, ¶ 8.",
    [full("2002-Ohio-2480", "2002 Ohio 2480", "us-ohioctapp")],
)
vec(
    "v3_same_state_carriers",
    # The Ohio triple-parallel run: official reporter (edition table),
    # webcite (v3 family), bare regional (honestly ambiguous, rule 6).
    "In re Adoption of B.I., 157 Ohio St.3d 29, 2019-Ohio-2450, 131 N.E.3d 28.",
    [
        full("157 Ohio St.3d 29", "157 Ohio St. 3d 29", "us-ohio"),
        full("2019-Ohio-2450", "2019 Ohio 2450", "us-ohioctapp"),
        full("131 N.E.3d 28", "131 N.E.3d 28", None, AMB),
    ],
)
# (b) Arkansas discontinued its bound reporters in 2009 and reused "Ark."
# / "Ark. App." as the official electronic citation (volume = year). Both
# eras share the edition strings, so one admission covers both.
vec(
    "v3_same_state_carriers",
    "Lane v. State, 2019 Ark. 5, at 4, 564 S.W.3d 524, 529.",
    [
        full("2019 Ark. 5", "2019 Ark. 5", "us-ark"),
        full("564 S.W.3d 524", "564 S.W.3d 524", None, AMB),
    ],
)
vec(
    "v3_same_state_carriers",
    "Slocum v. State, 325 Ark. 38, 924 S.W.2d 237 (1996).",
    [
        full("325 Ark. 38", "325 Ark. 38", "us-ark"),
        full("924 S.W.2d 237", "924 S.W.2d 237", None, AMB),
    ],
)
vec(
    "v3_same_state_carriers",
    "Kellco Custom Homes, Inc. v. Williams, 2024 Ark. App. 205.",
    [full("2024 Ark. App. 205", "2024 Ark. App. 205", "us-arkctapp")],
)
vec(
    "v3_same_state_carriers",
    "Walker v. State, 91 Ark. App. 300, 210 S.W.3d 157 (2005).",
    [
        full("91 Ark. App. 300", "91 Ark. App. 300", "us-arkctapp"),
        full("210 S.W.3d 157", "210 S.W.3d 157", None, AMB),
    ],
)
# (c) New Hampshire: bound N.H. Reports + the court-assigned "2025 N.H. 23"
# neutral share the edition string (family us-nh/us-nhsuperct).
vec(
    "v3_same_state_carriers",
    "Ortolano v. City of Nashua, 2025 N.H. 23.",
    [full("2025 N.H. 23", "2025 N.H. 23", "us-nh")],
)
vec(
    "v3_same_state_carriers",
    "Cecere v. Aetna Insurance, 145 N.H. 660 (2001).",
    [full("145 N.H. 660", "145 N.H. 660", "us-nh")],
)
# (d) Pennsylvania Superior Court: the bound Pa. Super. reports + the
# "2025 PA Super 112" header identifier share the edition (family
# us-pasuperct/.92, us-pa).
vec(
    "v3_same_state_carriers",
    "Commonwealth v. Slaughter, 2025 PA Super 112.",
    [full("2025 PA Super 112", "2025 Pa. Super. 112", "us-pasuperct")],
)
vec(
    "v3_same_state_carriers",
    "Commonwealth v. Archer, 440 Pa. Super. 380 (1995).",
    [full("440 Pa. Super. 380", "440 Pa. Super. 380", "us-pasuperct")],
)
# (e) Washington first-series and Connecticut Superior Court Reports (bound
# + format-neutral carriers, both one state); Hun's Reports (two carriers,
# both New York).
vec(
    "v3_same_state_carriers",
    "Scott v. Patterson, 1 Wash. 487 (1889).",
    [full("1 Wash. 487", "1 Wash. 487", "us-wash")],
)
vec(
    "v3_same_state_carriers",
    "People's Bank v. Balance Rock Condominium, 1998 Conn. Super. Ct. 1781.",
    [full("1998 Conn. Super. Ct. 1781", "1998 Conn. Super. Ct. 1781", "us-connsuperct")],
)
vec(
    "v3_same_state_carriers",
    "Bennett v. Pittman, 48 Hun 612 (1888).",
    [full("48 Hun 612", "48 Hun 612", "us-nysupct")],
)
# (f) Adjudicated EXCLUDES stay refused: cross-state nominative name shares
# ("Met." is Kentucky's Metcalf AND Massachusetts' Metcalf) and the
# scotus_early nominatives that would ride courts-db's SCOTUS-location-is-DC
# quirk ("Cranch", "Wall."). Corpus residence in one state is not proof the
# STRING is single-state in the wild.
vec(
    "v3_same_state_carriers",
    "Snow v. Alley, 10 Met. 263.",
    [full("10 Met. 263", "10 Met. 263", None, AMB)],
)
vec(
    "v3_same_state_carriers",
    # Bare Cranch nevertheless ROUTES — via rule 2, eyecite's own
    # scotus_early court metadata, unchanged since 1.0. The v3 EXCLUDE only
    # keeps Cranch out of the inference TABLES, where the corpus one-state
    # test would have booked SCOTUS under state=dc (the courts-db
    # SCOTUS-location quirk).
    "The Schooner Exchange v. McFaddon, 7 Cranch 116 (1812).",
    [full("7 Cranch 116", "7 Cranch 116", "us-scotus")],
)

# --- 16. Normalizer 1.4.0 / task 7.8.2 (2026-08-11): rule-4 forms for the
# remaining 45 states. Every vector below is a measured calibration case
# (DECISIONS 2026-08-11) or a verbatim string from the 45-state report.
# (a) Bare "(Ct. App.)" / "(App.)", state-gated on the reporter. Before
# 7.8.2 eyecite resolved the bare form to ctappindterr — the Indian
# Territory Court of Appeals, dead since 1907 — on live SC/WV/ID/NV
# strings, and the claim survived because the territorial court carries no
# state for the state gate. A recognized form the citation's own reporter
# cannot resolve now DEFEATS the claim (refuse-with-prejudice) instead of
# counting as an unreadable parenthetical.
vec(
    "ct_app_state_gate",
    "State v. Daniels, 439 S.C. 500 (Ct. App. 2023).",
    [full("439 S.C. 500", "439 S.C. 500", "us-scctapp")],
)
vec(
    "ct_app_state_gate",
    # W. Va. + bare Ct. App. = the 2022 Intermediate Court of Appeals
    # (courts-db wvactapp). No registry exists on chain, so the verifier
    # reports NOT_COVERED — the approved 2026-08-11 disclosure posture.
    "Foster cited 247 W. Va. 590 (Ct. App. 2023).",
    [full("247 W. Va. 590", "247 W. Va. 590", "us-wvactapp")],
)
vec(
    "ct_app_state_gate",
    "Monahan v. Hogan, 138 Nev. 58 (Ct. App. 2022).",
    [full("138 Nev. 58", "138 Nev. 58", "us-nevapp")],
)
vec(
    "ct_app_state_gate",
    # The parallel-run form: the parenthetical is adjacent to the REGIONAL
    # cite, whose multi-state edition cannot prove the state — honestly
    # refused (no ctappindterr, no guess). The official half routes via
    # its edition/family and the family sweep carries the authority.
    "State v. Franks, 432 S.C. 58, 79, 849 S.E.2d 580, 591 (Ct. App. 2020).",
    [
        full("432 S.C. 58", "432 S.C. 58", "us-sc"),
        full("849 S.E.2d 580", "849 S.E.2d 580", None, AMB),
    ],
)
vec(
    "ct_app_state_gate",
    "Town of Menasha v. Bastian, 178 Wis. 2d 191, 503 N.W.2d 382 (Ct. App. 1993).",
    [
        full("178 Wis. 2d 191", "178 Wis. 2d 191", "us-wis"),
        full("503 N.W.2d 382", "503 N.W.2d 382", None, AMB),
    ],
)
vec(
    "ct_app_state_gate",
    "Doe v. Roe, 500 S.E.2d 100 (Ct. App. 1998).",
    [full("500 S.E.2d 100", "500 S.E.2d 100", None, AMB)],
)
vec(
    "ct_app_state_gate",
    "State v. Sanchez, 181 Ariz. 492, 495 (App. 1995).",
    [full("181 Ariz. 492", "181 Ariz. 492", "us-arizctapp")],
)
vec(
    "ct_app_state_gate",
    "Turbin v. Superior Court, 165 Ariz. 195, 196 (App. 1990).",
    [full("165 Ariz. 195", "165 Ariz. 195", "us-arizctapp")],
)
# (b) Curated court forms courts-db lacks, each measured swallowing into
# the state's shortest citation_string before 7.8.2.
vec(
    "curated_court_forms",
    "Mayfield v. Commonwealth, 590 S.W.3d 300, 303-05 (Ky. App. 2019).",
    [full("590 S.W.3d 300", "590 S.W.3d 300", "us-kyctapp")],
)
vec(
    "curated_court_forms",
    "Fletcher Props., Inc. v. City of Minneapolis, 931 N.W.2d 410, 429-30 (Minn. App. 2019).",
    [full("931 N.W.2d 410", "931 N.W.2d 410", "us-minnctapp")],
)
vec(
    "curated_court_forms",
    "Corozzo v. Wal-Mart Stores, Inc., 531 S.W.3d 566, 575 (Mo. App. W.D. 2017).",
    [full("531 S.W.3d 566", "531 S.W.3d 566", "us-moctapp")],
)
vec(
    "curated_court_forms",
    # The bracketed editorial district and the district-less generic the
    # Missouri Supreme Court itself writes — one "Mo. App." entry covers
    # E.D./W.D./S.D., "[W.D.]", and the bare form.
    "Groh v. Groh, 910 S.W.2d 747 (Mo. App. [W.D.] 1995).",
    [full("910 S.W.2d 747", "910 S.W.2d 747", "us-moctapp")],
)
vec(
    "curated_court_forms",
    "Mo. Mun. League v. Carnahan, 303 S.W.3d 573, 586 (Mo. App. 2010).",
    [full("303 S.W.3d 573", "303 S.W.3d 573", "us-moctapp")],
)
vec(
    "curated_court_forms",
    # "Mo. banc" previously resolved right only because "Mo." swallowed it.
    "J.C.W. v. Wyciskalla, 275 S.W.3d 249 (Mo. banc 2009).",
    [full("275 S.W.3d 249", "275 S.W.3d 249", "us-mo")],
)
vec(
    "curated_court_forms",
    # The report's measured N.C. Ct. App. word-order inversion.
    "State v. Hollis, 905 S.E.2d 265, 267 (N.C. App. Ct. 2024).",
    [full("905 S.E.2d 265", "905 S.E.2d 265", "us-ncctapp")],
)
vec(
    "curated_court_forms",
    "Rogele, Inc. v. WCAB, 198 A.3d 1195, 1204 (Pa. Cmwlth. 2018).",
    [full("198 A.3d 1195", "198 A.3d 1195", "us-pacommwct")],
)
vec(
    "curated_court_forms",
    # 7.8.4 live-sweep find: courts-db says "Pa. Super. Ct.", briefs say
    # "(Pa. Super. YEAR)" — previously swallowed into "Pa.". Caught by the
    # census classification of the verification run (an in-corpus
    # pasuperct key NOT_FOUND under us-pa).
    "Commonwealth v. Kittrell, 19 A.3d 532, 538 (Pa. Super. 2011).",
    [full("19 A.3d 532", "19 A.3d 532", "us-pasuperct")],
)
vec(
    "curated_court_forms",
    # Same class: courts-db "Colo. Ct. App." vs the real "(Colo. App.
    # YEAR)" parenthetical on pre-2012 regional-only Colorado cites.
    "Henderson v. Master Klean Janitorial, Inc., 70 P.3d 612, 615 (Colo. App. 2003).",
    [full("70 P.3d 612", "70 P.3d 612", "us-coloctapp")],
)
vec(
    "curated_court_forms",
    "McCoy v. State, 80 P.3d 757, 764 (Alaska App. 2002).",
    [full("80 P.3d 757", "80 P.3d 757", "us-alaskactapp")],
)
vec(
    "curated_court_forms",
    # Court-authored period-drop variant preserved verbatim in the report.
    "State v. Lee, 71 S.W.3d 299, 303 (Tenn. Crim App. 2001).",
    [full("71 S.W.3d 299", "71 S.W.3d 299", "us-tenncrimapp")],
)
vec(
    "curated_court_forms",
    # Alabama's historical compressed division parenthetical, gated on
    # Ala. editions ("(Civ. 1974)" after an Ala. App. cite).
    "Phillips v. Phillips, 52 Ala. App. 234 (Civ. 1974).",
    [full("52 Ala. App. 234", "52 Ala. App. 234", "us-alacivapp")],
)
# (c) Paragraph parentheticals are pin material, not court signals: the
# scan skips them (Mississippi's standard form), and a claim whose only
# adjacency is "(¶13)" has the no-parenthetical overreach signature.
vec(
    "paragraph_parenthetical",
    "Esco v. State, 102 So. 3d 1209, 1214 (¶13) (Miss. Ct. App. 2012).",
    [full("102 So. 3d 1209", "102 So. 3d 1209", "us-missctapp")],
)
vec(
    "paragraph_parenthetical",
    "Huff-Cook, Inc. v. Dale, 913 So. 2d 988, 990 (¶ 10) (Miss. 2005).",
    [full("913 So. 2d 988", "913 So. 2d 988", "us-miss")],
)
# (d) Louisiana public-domain citations: the numbered circuit is part of
# the citation, cardinal per the Supreme Court's rule and ordinal in real
# First Circuit opinions, with a full M/D/YY date. The docket half is not
# reporter-shaped (never parsed); the So. 2d/3d parallel carries the key,
# routed by the circuit parenthetical on its PRECEDING side. Writ history
# appends a separate Supreme Court decision.
vec(
    "la_public_domain",
    "State v. Palmer, 45,627 (La. App. 2 Cir. 1/26/11), 57 So. 3d 1099, writ denied, 11-0412 (La. 9/2/11), 68 So. 3d 526.",
    [
        full("57 So. 3d 1099", "57 So. 3d 1099", "us-lactapp"),
        full("68 So. 3d 526", "68 So. 3d 526", "us-la"),
    ],
)
vec(
    "la_public_domain",
    "Succession of Blythe, 466 So. 2d 500, 501 (La. App. 5 Cir.), writ denied, 469 So. 2d 985 (La. 1985).",
    [
        full("466 So. 2d 500", "466 So. 2d 500", "us-lactapp"),
        full("469 So. 2d 985", "469 So. 2d 985", "us-la"),
    ],
)
vec(
    "la_public_domain",
    "Lafayette Steel Erector, Inc. v. G. Kendrick LLC, 2022-0892 (La. App. 1st Cir. 8/29/23), 375 So. 3d 464, 474.",
    [full("375 So. 3d 464", "375 So. 3d 464", "us-lactapp")],
)
vec(
    "la_public_domain",
    # The federal-circuit whitelist is untouched: "(1st Cir.)" without the
    # "La. App." lead is still the First Circuit.
    "United States v. Gamma, 100 F.3d 200 (1st Cir. 1996).",
    [full("100 F.3d 200", "100 F.3d 200", "us-ca1")],
)
# (e) Ohio's numbered districts, trailing ("(12th Dist.)", "(6th
# Dist.1991)" with no space before the year) — gated on Ohio editions
# because N.E.-family reporters span Ohio AND Illinois, which also
# numbers its districts. The webcite routes via the v3 family either way;
# a lone N.E. cite with a district parenthetical stays honestly ambiguous.
vec(
    "ohio_districts",
    "Hild v. Samaritan Health Partners, 2023-Ohio-2408, ¶ 87 (2d Dist.).",
    [full("2023-Ohio-2408", "2023 Ohio 2408", "us-ohioctapp")],
)
vec(
    "ohio_districts",
    "State v. Rosa, 2013-Ohio-5867, 6 N.E.3d 57 (7th Dist.).",
    [
        full("2013-Ohio-5867", "2013 Ohio 5867", "us-ohioctapp"),
        full("6 N.E.3d 57", "6 N.E.3d 57", None, AMB),
    ],
)
vec(
    "ohio_districts",
    "In re Smith, 77 Ohio App.3d 1, 16, 601 N.E.2d 45 (6th Dist.1991).",
    [
        full("77 Ohio App.3d 1", "77 Ohio App. 3d 1", "us-ohioctapp"),
        full("601 N.E.2d 45", "601 N.E.2d 45", None, AMB),
    ],
)
# (f) North Carolina's withdrawn 2021–2022 universal citations: eyecite is
# blind to them and the corpus holds zero keys under them — accounted as
# out-of-scope (the law-sections precedent), never silently dropped.
vec(
    "nc_universal",
    "State v. Johnson, 2021-NCSC-165, ¶ 12, was decided that term.",
    [full("2021-NCSC-165", None, None, "out_of_scope", kind="unknown")],
)
vec(
    "nc_universal",
    "Vaitovas v. City of Greenville, 2022-NCCOA-169.",
    [full("2022-NCCOA-169", None, None, "out_of_scope", kind="unknown")],
)
# (g) Hawaiʻi ʻokina, ADJUDICATED NOT FIXED (2026-08-11): archive text
# renders the ʻokina as "Hawai#i" / "Hawai i" / a backtick, and eyecite
# drops the state cite (the straight-apostrophe form "Hawai'i" parses
# fine). Recovering it would mean a new text-cleaning rule, and §7 of the
# spec makes cleaning rules checksumAlgo territory — not warranted for an
# additive parse-recovery of archive artifacts. Pinned: the P.3d parallel
# survives and carries the authority; the mangled state cite drops.
vec(
    "okina_artifacts",
    "Womble Bond Dickinson (US) LLP v. Kim, 153 Hawai i 307, 319, 537 P.3d 1154, 1166 (2023).",
    [full("537 P.3d 1154", "537 P.3d 1154", None, AMB)],
)


def main() -> None:
    out = Path(__file__).parent / "vectors.json"
    payload = {
        "_meta": {
            "spec": "cite-canonical-v1",
            "generator": "generate_vectors.py",
            "note": "Expectations hand-derived from docs/canonical-citation-spec.md; adjudications recorded in DECISIONS.md. Compared fields: as_written, canonical, registry, disposition, kind.",
            "vector_count": len(VECTORS),
            "expectation_rows": sum(len(v["expect"]) for v in VECTORS),
        },
        "vectors": VECTORS,
    }
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    cats: dict[str, int] = {}
    for v in VECTORS:
        cats[v["category"]] = cats.get(v["category"], 0) + 1
    for cat, n in cats.items():
        print(f"{cat}: {n}")
    print(f"TOTAL vectors: {len(VECTORS)}, expectation rows: {payload['_meta']['expectation_rows']}")


if __name__ == "__main__":
    main()
