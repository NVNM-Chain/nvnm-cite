# State Citation-Practice Evidence for `nvnm-cite`

## Consolidated seven-batch report

**Prepared:** August 11, 2026  
**Repository baseline:** [`NVNM-Chain/nvnm-cite`, `main` branch](https://github.com/NVNM-Chain/nvnm-cite)  
**Scope:** Citation-format evidence for the 45 U.S. states not included in the original CA/NY/TX/FL/IL recall proof.  
**Purpose:** Real-world citation-practice evidence for normalizer verification; this report does not propose code changes or assess database coverage.

This file consolidates the seven regional-reporter-family reports produced in this research sequence. Source links, copied citation strings, punctuation, spacing, apostrophes, blanks, status parentheticals, and stated verification limits have been preserved. Delaware is included in Batch 1 because it was the otherwise omitted A./A.3d jurisdiction needed to reach all 45 remaining states. Massachusetts appears only in Batch 1 and is not duplicated in Batch 2.

Batch 1 was originally delivered as a cross-state report organized under the seven requested evidence categories. Batches 2–7 were delivered state by state, with those same seven categories repeated for each state.

## Contents

1. [Batch 1 — A./A.3d family](#batch-1--aa3d-family) — Pennsylvania, New Jersey, Maryland, Massachusetts, Connecticut, Maine, New Hampshire, Rhode Island, Vermont, Delaware
2. [Batch 2 — N.E.3d family](#batch-2--ne3d-family) — Ohio, Indiana
3. [Batch 3 — S.E.2d family](#batch-3--se2d-family) — Georgia, North Carolina, Virginia, South Carolina, West Virginia
4. [Batch 4 — So. 3d family](#batch-4--so-3d-family) — Alabama, Mississippi, Louisiana
5. [Batch 5 — S.W.3d family](#batch-5--sw3d-family) — Missouri, Tennessee, Kentucky, Arkansas
6. [Batch 6 — N.W.2d/N.W.3d family](#batch-6--nw2dnw3d-family) — Michigan, Wisconsin, Minnesota, Iowa, Nebraska, North Dakota, South Dakota
7. [Batch 7 — P.3d family](#batch-7--p3d-family) — Arizona, Washington, Colorado, Oregon, Oklahoma, Kansas, New Mexico, Utah, Nevada, Idaho, Montana, Wyoming, Alaska, Hawaiʻi

## Coverage index

| Batch | Reporter family | States |
|---|---|---|
| 1 | A./A.3d | PA, NJ, MD, MA, CT, ME, NH, RI, VT, DE |
| 2 | N.E.3d | OH, IN |
| 3 | S.E.2d | GA, NC, VA, SC, WV |
| 4 | So. 3d | AL, MS, LA |
| 5 | S.W.3d | MO, TN, KY, AR |
| 6 | N.W.2d/N.W.3d | MI, WI, MN, IA, NE, ND, SD |
| 7 | P.3d | AZ, WA, CO, OR, OK, KS, NM, UT, NV, ID, MT, WY, AK, HI |

---

## Batch 1 — A./A.3d family

This batch covers **Pennsylvania, New Jersey, Maryland, Massachusetts, Connecticut, Maine, New Hampshire, Rhode Island, Vermont, and Delaware**. I have included Delaware because the regional-family list in the request otherwise contains only 44 unique states after excluding CA, NY, TX, FL, and IL; Delaware is the omitted A./A.3d jurisdiction.

I treated the `main`-branch normalizer as the baseline rather than re-deriving it: the §4 jurisdiction hierarchy, the existing reporter/court inference tables and same-state families, and the golden-vector representation are already part of the implementation.   I also treated the August 9 recall-proof findings as the five specific failure probes for this batch: prefix swallow, district-specific intermediate courts, same-state multi-court reporter editions, apostrophe/ordinal normalization, and same-state attribution splits.

A qualification matters at the outset. I would rather under-deliver a state's requested 10–25 strings than manufacture one. For several smaller jurisdictions, the born-digital primary/public-archive material I could validate in this pass did **not** yield ten safely copyable state-case strings. Those shortfalls are identified explicitly under **Not verified**.

### Sources

**Pennsylvania.** Four recent, text-layered appellate opinions supplied the working corpus: [Commonwealth v. Laird, Supreme Court of Pennsylvania (2025)](https://law.justia.com/cases/pennsylvania/supreme-court/2025/809-cap.html); [Wentworth v. Steinmetz, Superior Court (2025)](https://law.justia.com/cases/pennsylvania/superior-court/2025/293-wda-2025.html); [Commonwealth v. Slaughter, Superior Court (2025)](https://law.justia.com/cases/pennsylvania/superior-court/2025/1374-mda-2024.html); and [Stewart v. City of Philadelphia (WCAB), Commonwealth Court (2025)](https://law.justia.com/cases/pennsylvania/commonwealth-court/2025/490-c-d-2024.html). Together they cover the Supreme Court and both intermediate appellate courts and contain dense in-state citation runs.

**New Jersey.** Five useful born-digital opinions are [State v. Bragg, Supreme Court (2025)](https://law.justia.com/cases/new-jersey/supreme-court/2025/a-13-24.html); [Haylie Senape v. South Amboy High Middle School, Appellate Division (2025)](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-1329-24.html); [James Ofeldt v. New Jersey Department of Corrections, Appellate Division (2025)](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-0220-22.html); [State v. R.S., Appellate Division (2025)](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-2964-23.html); and [Unifund CCR LLC v. Garabedian, Appellate Division (2025)](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-4148-23.html). The latter four are especially valuable because their front matter and citations expose actual Appellate Division practice, including Rule 1:36-3 unpublished-opinion treatment.

**Maryland.** I used [Walton v. Premier Soccer Club, Supreme Court of Maryland (2025)](https://law.justia.com/cases/maryland/court-of-appeals/2025/11-24.html), [Akers v. State, Supreme Court of Maryland (2025)](https://law.justia.com/cases/maryland/court-of-appeals/2025/7-24.html), and [Davis v. State, Supreme Court of Maryland (2025)](https://law.justia.com/cases/maryland/court-of-appeals/2025/21m-24.html). These are unusually good test documents because they cite both the newly renamed Appellate Court of Maryland and older cases under the long-running `Md.`/`Md. App.` reporter structure, including official/Atlantic parallels and Westlaw cites to unreported intermediate decisions.

**Massachusetts.** The source set is [Luppold v. Hanlon, Supreme Judicial Court (2025)](https://law.justia.com/cases/massachusetts/supreme-court/2025/sjc-13577.html), [Commonwealth v. Rodriguez, Supreme Judicial Court (2025)](https://law.justia.com/cases/massachusetts/supreme-court/2025/sjc-13727.html), and [Deckelbaum v. Zoning Board of Appeals of Provincetown, Appeals Court (2024)](https://law.justia.com/cases/massachusetts/court-of-appeals/2024/23-p-443.html). The first and third are particularly citation-dense.

**Connecticut.** I could validate only two individual legal documents to the requested standard in this pass: [State v. Traynham, Connecticut Supreme Court (2025)](https://law.justia.com/cases/connecticut/supreme-court/2025/sc20883.html) and [Troy Laundry Building, LLC v. Beautiful Life Adult Daycare, LLC, Connecticut Appellate Court (2025)](https://law.justia.com/cases/connecticut/court-of-appeals/2025/ac47173.html). Both are born-digital reproductions of Connecticut Law Journal material and are exceptionally useful for the state's parallel-reporting mechanics. This is **below the requested three-document floor**, so Connecticut remains source-incomplete for proof purposes.

**Maine.** Three dense Law Court opinions are [Bagrii v. Campbell (2025 ME 38)](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-38.html), [State v. Robshaw (2025 ME 50)](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-50.html), and [State v. Woodard (2025 ME 32)](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-32.html). They give a very clean corpus of neutral citations, paragraph pins, Atlantic parallels, and pre-neutral `Me.` forms.

**New Hampshire.** The legal-document set is [Rand v. State, Supreme Court of New Hampshire (2025)](https://law.justia.com/cases/new-hampshire/supreme-court/2025/2024-0138.html), [Ortolano v. City of Nashua (2025)](https://law.justia.com/cases/new-hampshire/supreme-court/2025/2024-0181.html), and [Ball v. Roman Catholic Bishop of Manchester (2025)](https://law.justia.com/cases/new-hampshire/supreme-court/2025/2024-0606.html). Ortolano is especially useful because the slip opinion itself prints the court-assigned citation `2025 N.H. 23` and states that the opinion remains subject to formal revision before publication in the New Hampshire Reports.

**Rhode Island.** I used [Lambert v. Salisbury (2025)](https://law.justia.com/cases/rhode-island/supreme-court/2025/22-79.html), [State v. McLean (2025)](https://law.justia.com/cases/rhode-island/supreme-court/2025/24-48.html), and [Roman v. City of Providence (2025)](https://law.justia.com/cases/rhode-island/supreme-court/2025/24-75.html). They are good modern A.3d specimens and include both full and short cites.

**Vermont.** The core sources are [State v. Aaliyah Johnson, 2025 VT 11](https://law.justia.com/cases/vermont/supreme-court/2025/25-ap-048.html), [Belter v. City of Burlington, 2025 VT 35](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-275.html), and [Veljovic v. TD Bank, N.A., 2025 VT 38](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-352.html). Additional current specimens are [State v. Meta Platforms, Inc., 2025 VT 51](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-295.html) and [State v. Orost, 2025 VT 15](https://law.justia.com/cases/vermont/supreme-court/2025/23-ap-345.html).

**Delaware.** Delaware was not named in the batch list but belongs here. I used [Anderson v. Christiana Care Health Services, Inc., Supreme Court (2025)](https://law.justia.com/cases/delaware/supreme-court/2025/92-2025.html), [Sawyer v. State (2025)](https://law.justia.com/cases/delaware/supreme-court/2025/186-2024.html), [Kellam v. State (2025)](https://law.justia.com/cases/delaware/supreme-court/2025/224-2024.html), and [Daniels v. State (2025)](https://law.justia.com/cases/delaware/supreme-court/2025/532-2024.html). The samples are valuable because Delaware Supreme Court opinions routinely cite both A.3d and court-specific Westlaw dispositions.

### Court structure as cited

**Pennsylvania.** The appellate hierarchy has a **Supreme Court of Pennsylvania** and two statewide intermediate courts, the **Superior Court of Pennsylvania** and the **Commonwealth Court of Pennsylvania**. Actual citation parentheticals in the corpus are `Pa.`, `Pa. Super.`/`Pa.Super.`, and `Pa. Cmwlth.`. The Superior Court sample proves that both spaced and unspaced forms occur in real court output: Wentworth uses `(Pa.Super. 2024)` while Slaughter uses `(Pa. Super. 2023)`. Commonwealth Court opinions use `(Pa. Cmwlth. YEAR)`. EAP/MAP/WAP and EDA/MDA/WDA are docket-geography identifiers, not court-parenthetical district identifiers analogous to Florida DCA numbers or Texas court-of-appeals districts.

**New Jersey.** The highest court is the **Supreme Court of New Jersey**; the statewide intermediate appellate tribunal is the **Superior Court of New Jersey, Appellate Division**. In actual published-case citations, Supreme Court authority is identified by the official reporter `N.J.`, ordinarily with a year-only parenthetical, while intermediate authority uses `N.J. Super.` plus `(App. Div. YEAR)`. There are no numbered appellate districts/divisions in the citation parenthetical. Current unpublished Appellate Division opinions expressly style themselves `SUPERIOR COURT OF NEW JERSEY APPELLATE DIVISION` and warn that their use is limited by Rule 1:36-3.

**Maryland.** Effective **December 14, 2022**, the former Court of Appeals became the **Supreme Court of Maryland**, and the former Court of Special Appeals became the **Appellate Court of Maryland**. The official reporter abbreviations did not undergo an analogous wholesale rename: Supreme Court decisions continue in `Md.`, and intermediate decisions in `Md. App.`. For unreported/vendor-cited current intermediate opinions, the sampled Supreme Court uses the explicit parenthetical `Md. App. Ct.`; Davis also shows a Supreme Court docket disposition parenthetical simply as `Md.`. This produces a real modern naming/reporting asymmetry worth testing.

**Massachusetts.** The appellate courts are the **Supreme Judicial Court** and **Appeals Court**. The corresponding official citation forms are `Mass.` and `Mass. App. Ct.`. The Reporter of Decisions is responsible for publishing both courts' decisions, and the state's own law-library guidance uses those two forms as the standard appellate examples. There are no district or division identifiers in ordinary Appeals Court parentheticals.

**Connecticut.** The appellate structure is the **Connecticut Supreme Court** and the **Connecticut Appellate Court**. Their official reporter forms are `Conn.` and `Conn. App.`. Actual opinions overwhelmingly let the reporter identify the court rather than adding a `Conn.` or `Conn. App.` court parenthetical to every state case. There are no district/division-specific intermediate citation forms.

**Maine.** Maine has one state appellate tribunal, the **Supreme Judicial Court**. When it hears appeals it is “sitting as the Law Court”; there is no intermediate appellate court. The Judiciary itself describes the SJC as the State's highest court/court of last resort and says that when deciding appeals it is “Sitting as the Law Court.” Modern opinions are therefore state-coded by `ME` rather than needing a second-level court identifier.

**New Hampshire.** The relevant appellate tribunal is the **Supreme Court of New Hampshire**. The sourced cases come directly from Superior Court to that court and show no intermediate appellate layer. The current slip form uses `N.H.` inside the court-assigned case citation—for example, `2025 N.H. 23`—while traditional bound authority uses `N.H.` as the New Hampshire Reports abbreviation.

**Rhode Island.** The sourced state appeals proceed from Superior Court directly to the **Rhode Island Supreme Court**; there is no intermediate appellate form to encode in these materials. Modern reported citations use the state identifier `(R.I. YEAR)` after A.2d/A.3d.

**Vermont.** The **Vermont Supreme Court** is the appellate court reflected throughout the source set. Published decisions use the public-domain `YYYY VT N` identifier; later print citations use `Vt.` for Vermont Reports. The Judiciary distinguishes published full-court precedent from many three-justice entry orders, which generally are not included in Vermont Reports.

**Delaware.** The sourced opinions are from the **Supreme Court of the State of Delaware** and show direct review of judgments from Superior Court and Family Court. There is no intermediate appellate-court form in the sources. Delaware does, however, present a closely related parser hazard because lower courts have court-specific identifiers such as `Del. Super.` and `Del. Ch.` while Supreme Court cites use `Del.`. The Supreme Court's own current opinions visibly use `Del. Super.` for lower-court vendor dispositions.

### Reporters in actual use

**Pennsylvania.** The modern reported corpus is dominated by **Atlantic Reporter, Third Series (`A.3d`)**, with `(Pa. YEAR)`, `(Pa. Super. YEAR)`, or `(Pa. Cmwlth. YEAR)` supplying jurisdiction. The sourced 2025 opinions do not rely on a current `Pa.` volume/page reporter as their principal modern citation. Unreported/nonprecedential decisions are routinely carried by **Westlaw**, often with docket and filing-date information: Commonwealth Court's Stewart, for example, cites another unreported Commonwealth Court case through `2025 WL 595736`. Superior Court opinions also display court-issued header identifiers such as `2025 PA Super 253` and `2025 PA Super 112`; I did **not** find a primary Pennsylvania rule in this pass establishing the adoption date or legal status of those identifiers as a mandatory neutral/public-domain citation, so I do not treat that point as proven. The official Pennsylvania Reports cessation date likewise remains unverified from a primary source here.

**New Jersey.** Actual New Jersey house style is still strongly centered on the **official reporters**: `N.J.` for Supreme Court and `N.J. Super.` for Superior Court published decisions. The intermediate reporter needs a division parenthetical because `N.J. Super.` is not itself synonymous with Appellate Division; the sampled opinions consistently give `(App. Div. YEAR)` for appellate cases. In contrast to nearby Pennsylvania and Rhode Island, the sampled New Jersey court opinions do **not** use A.3d as their normal state-case cite even though Atlantic is a commercial parallel source. No public-domain/neutral state citation format appeared in the sample.

**Maryland.** Maryland maintains official **Maryland Reports (`Md.`)** for the Supreme Court and **Maryland Appellate Reports (`Md. App.`)** for the intermediate court. The courts' official opinions page gives an unusually precise publication transition: reported opinions posted on or before **June 30, 2018** have their final official text in the bound Maryland Reports/Maryland Appellate Reports; under Maryland's Uniform Electronic Legal Materials Act, opinions and orders posted on or after **July 1, 2018** are official/authentic electronically. New reported decisions initially may carry a provisional blank-volume form and later acquire bound volume/page numbers. The State Law Library also identifies West's Atlantic Reporter as the regional reporter. Actual sourced opinions contain classic official/Atlantic parallel runs such as `454 Md. 296, 325, 164 A.3d 265, 282 (2017)`. For current unreported intermediate cases, Westlaw is materially present—for example `2024 WL 338958 ... (Md. App. Ct. Jan. 30, 2024)`.

**Massachusetts.** The official reporters remain **Massachusetts Reports (`Mass.`)** for the SJC and **Massachusetts Appeals Court Reports (`Mass. App. Ct.`)**. The state's current opinion portal describes `Mass. Reports` as running from 1804 to date and Appeals Court Reports from 1972 to date. Massachusetts' own legal-citation guidance describes the **Northeastern Reporter** as the unofficial regional reporter and explicitly illustrates official/N.E. parallel citations. In the actual SJC and Appeals Court opinions sampled here, however, in-state cases are overwhelmingly cited to `Mass.` or `Mass. App. Ct.` alone; I did not find enough primary-document evidence to call `N.E.3d` prevalent in Massachusetts appellate house style. No court-issued neutral citation format was verified.

**Connecticut.** Connecticut retains **Connecticut Reports (`Conn.`)** and **Connecticut Appellate Reports (`Conn. App.`)** as the complete official editions and expressly calls them the “required citation source” for Connecticut courts and agencies. Both are now compiled electronically: Connecticut Reports beginning with volume 320 and Connecticut Appellate Reports beginning with volume 168. Unlike New Jersey and Massachusetts, actual Connecticut opinions frequently carry the **Atlantic parallel in the same citation**, e.g. `172 Conn. App. 108, 117, 158 A.3d 826`. No public-domain neutral citation appeared in the verified material.

**Maine.** Maine is especially clean. The Judicial Branch states that the **Atlantic Reporter, Second and Third Series, has been Maine's official reporter since 1966**. Online opinions have been published since January 1997, and the court instructs that those decisions be cited in the form `Dutil v. Burns, 1997 ME 1, ¶ 2, 687 A.2d 639.` Thus the post-1997 production format is a court-assigned **`YYYY ME N` neutral/public-domain citation + paragraph pin + Atlantic parallel**. Pre-neutral cases remain visible as regional citations with `(Me. YEAR)`.

**New Hampshire.** Current slips use a court-issued identifier in the exact form **`YYYY N.H. N`**—Ortolano is expressly labeled `Citation: Ortolano v. City of Nashua, 2025 N.H. 23`—and the same slip warns that it is subject to formal revision before publication in the **New Hampshire Reports**. This establishes actual current use of the identifier and the continuing role of `N.H.` bound reporting. I did not verify from a primary rule the date on which `YYYY N.H. N` was adopted, nor did the extracted in-state citation sample establish how frequently New Hampshire practitioners pair those forms with A.3d.

**Rhode Island.** Modern sourced Supreme Court opinions cite Rhode Island precedent principally through **A.3d** (and older A.2d), followed by `(R.I. YEAR)`. Examples include `316 A.3d 1197, 1219-20 (R.I. 2024)` and `115 A.3d 961, 964 (R.I. 2015) (mem.)`. No neutral/public-domain state citation appeared in the sample. I did not obtain a primary-source statement establishing the exact cessation date of Rhode Island Reports, so that date is deliberately left unproved below rather than supplied from secondary material.

**Vermont.** Vermont has one of the most explicit state rules in this batch. Rule 28.2, reproduced by Cornell's Legal Information Institute and linked through the state's court-rules ecosystem, provides that **all Supreme Court opinions issued on or after January 1, 2003** receive a sequential annual number and numbered paragraphs. Post-2003 Vermont opinions are cited `YYYY VT N`, followed by official and unofficial print reporters, and pinpoint citations are by paragraph. Actual opinions conform: `2022 VT 20, ¶ 7, 216 Vt. 609, 279 A.3d 118 (mem.)`. Thus modern Vermont gives three usable signals in one full cite: neutral `VT`, official `Vt.`, and regional `A.3d`.

**Delaware.** The current Supreme Court corpus relies heavily on **A.3d** for reported cases and **Westlaw** for orders/unreported dispositions. A single table disposition may have both: `108 A.3d 1225, 2015 WL 631581, at *2 n.12 (Del. Feb. 11, 2015) (TABLE)`. Lower-court authorities are likewise vendor-cited with explicit court attribution, e.g. `2024 WL 4867172 (Del. Super. Nov. 22, 2024)`. I did not verify a current Delaware public-domain neutral citation or, from a primary source, the precise cessation date of the old Delaware Reports.

### Verbatim examples

The strings below are **not normalized or reconstructed**. They preserve what the linked document exposes, including spacing variants such as `Pa.Super.`, capitalization such as `N.J. super.`, en dashes, `supra`, paragraph marks, and vendor parentheticals. Where a jurisdiction fell below ten safely verified strings, I stop rather than fabricate the balance.

**Pennsylvania — twelve verified strings**

| Exact string | Case cited | Source |
|---|---|---|
| `323 A.3d 792, 799 (Pa.Super. 2024)` | *Morrissey v. St. Joseph’s Preparatory School* | [Wentworth](https://law.justia.com/cases/pennsylvania/superior-court/2025/293-wda-2025.html) |
| `260 A.3d 967, 970–71 (Pa.Super. 2021)` | *Palmiter v. Commonwealth Health Systems, Inc.* | [Wentworth](https://law.justia.com/cases/pennsylvania/superior-court/2025/293-wda-2025.html) |
| `60 A.3d 133, 139 (Pa.Super. 2012) (en banc)` | *Milliken v. Jacono* | [Wentworth](https://law.justia.com/cases/pennsylvania/superior-court/2025/293-wda-2025.html) |
| `2025 PA Super 253` | *Wentworth v. Steinmetz* — opinion-header identifier | [Wentworth](https://law.justia.com/cases/pennsylvania/superior-court/2025/293-wda-2025.html) |
| `303 A.3d 124, 134 (Pa. Super. 2023)` | *Commonwealth v. Bartic* | [Slaughter](https://law.justia.com/cases/pennsylvania/superior-court/2025/1374-mda-2024.html) |
| `19 A.3d 532, 538 (Pa. Super. 2011)` | *Commonwealth v. Kittrell* | [Slaughter](https://law.justia.com/cases/pennsylvania/superior-court/2025/1374-mda-2024.html) |
| `163 A.3d 466, 469 (Pa. Super. 2017)` | *Commonwealth v. Monjaras-Amaya* | [Slaughter](https://law.justia.com/cases/pennsylvania/superior-court/2025/1374-mda-2024.html) |
| `327 A.3d 301, 304 (Pa. Super. 2024)` | *Commonwealth v. Stewart* | [Slaughter](https://law.justia.com/cases/pennsylvania/superior-court/2025/1374-mda-2024.html) |
| `2 A.3d 548, 558 (Pa. 2010)` | *Bufford v. Workers’ Compensation Appeal Board* | [Stewart](https://law.justia.com/cases/pennsylvania/commonwealth-court/2025/490-c-d-2024.html) |
| `198 A.3d 1195, 1204 (Pa. Cmwlth. 2018)` | *Rogele, Inc. v. Workers’ Compensation Appeal Board* | [Stewart](https://law.justia.com/cases/pennsylvania/commonwealth-court/2025/490-c-d-2024.html) |
| `251 A.3d 467, 475 (Pa. Cmwlth. 2021)` | *W. Penn Allegheny Health Systems, Inc. v. Workers’ Compensation Appeal Board* | [Stewart](https://law.justia.com/cases/pennsylvania/commonwealth-court/2025/490-c-d-2024.html) |
| `2025 PA Super 112` | *Commonwealth v. Slaughter* — opinion-header identifier | [Slaughter](https://law.justia.com/cases/pennsylvania/superior-court/2025/1374-mda-2024.html) |

The reporter strings and spacing differences are visible in the cited court texts.

**New Jersey — twelve verified strings**

| Exact string | Case cited | Source |
|---|---|---|
| `308 N.J. Super. 1, 12 (App. Div. 1998)` | *State v. Bilek* | [Bragg](https://law.justia.com/cases/new-jersey/supreme-court/2025/a-13-24.html) |
| `213 N.J. at 149-50` | *D.D.* | [Senape](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-1329-24.html) |
| `384 N.J. super. 182, 189-90 (App. Div. 2006)` | *Maher v. County of Mercer* | [Senape](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-1329-24.html) |
| `461 N.J. Super. at 237-38` | *Blanchard* | [Ofeldt](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-0220-22.html) |
| `414 N.J. Super. 186, 192 (App. Div. 2010)` | *Figueroa v. N.J. Department of Corrections* | [Ofeldt](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-0220-22.html) |
| `67 N.J. 496, 525-46 (1975)` | *Avant v. Clifford* | [Ofeldt](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-0220-22.html) |
| `330 N.J. Super. 197, 203 (App. Div. 2000)` | *Williams v. Department of Corrections* | [Ofeldt](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-0220-22.html) |
| `450 N.J. Super. 499, 502 (App. Div. 2017)` | *T.M.S. v. W.C.P.* | [R.S.](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-2964-23.html) |
| `442 N.J. Super. 205, 215 (App. Div. 2015)` | *N.T.B. v. D.D.B.* | [R.S.](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-2964-23.html) |
| `478 N.J. Super. 171, 180 (App. Div. 2024)` | *Francavilla v. Absolute Resolutions VI, LLC* | [Garabedian](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-4148-23.html) |
| `464 N.J. Super. 103 (App. Div. 2020)` | *LVNV Funding, LLC v. Deangelo* | [Garabedian](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-4148-23.html) |
| `220 N.J. 544, 559 (2015)` | *Badiali v. New Jersey Manufacturers Insurance* | [Garabedian](https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2025/a-4148-23.html) |

The lowercase `N.J. super.` example is preserved because that is what the linked text exposes; it should be treated as a real input oddity, not silently “corrected” here.

**Maryland — ten verified strings**

| Exact string | Case cited | Source |
|---|---|---|
| `357 Md. 344, 358-59 (2000)` | *Brown v. Dermer* | [Walton](https://law.justia.com/cases/maryland/court-of-appeals/2025/11-24.html) |
| `261 Md. App. 53 (2024)` | *Walton v. Premier Soccer Club, Inc.* — Appellate Court decision | [Walton](https://law.justia.com/cases/maryland/court-of-appeals/2025/11-24.html) |
| `487 Md. 212 (2024)` | *Walton v. Premier Soccer Club, Inc.* — Supreme Court certiorari disposition | [Walton](https://law.justia.com/cases/maryland/court-of-appeals/2025/11-24.html) |
| `459 Md. 356, 382-83 (2018)` | *Young Electric Contractors, Inc. v. Dustin Construction, Inc.* | [Walton](https://law.justia.com/cases/maryland/court-of-appeals/2025/11-24.html) |
| `No. 0925, 2024 WL 338958, at *16 (Md. App. Ct. Jan. 30, 2024)` | *Akers v. State* — unreported Appellate Court decision | [Akers](https://law.justia.com/cases/maryland/court-of-appeals/2025/7-24.html) |
| `454 Md. 296, 325, 164 A.3d 265, 282 (2017)` | *Fuentes v. State* | [Akers](https://law.justia.com/cases/maryland/court-of-appeals/2025/7-24.html) |
| `171 Md. App. 668, 912 A.2d 16 (2006)` | *State v. Adams* | [Davis](https://law.justia.com/cases/maryland/court-of-appeals/2025/21m-24.html) |
| `230 Md. App. 537, 148 A.3d 377 (2016)` | *Rich v. State* | [Davis](https://law.justia.com/cases/maryland/court-of-appeals/2025/21m-24.html) |
| `406 Md. 240, 958 A.2d 295 (2008)` | *State v. Adams* — Supreme Court disposition | [Davis](https://law.justia.com/cases/maryland/court-of-appeals/2025/21m-24.html) |
| `454 Md. 448, 164 A.3d 355 (2017)` | *Rich v. State* — Supreme Court disposition | [Davis](https://law.justia.com/cases/maryland/court-of-appeals/2025/21m-24.html) |

These examples directly prove current `Md. App. Ct.` vendor-parenthetical practice, ordinary `Md.`/`Md. App.` reporter attribution, and official/Atlantic parallel runs.

**Massachusetts — eight safely verified strings**

| Exact string | Case cited | Source |
|---|---|---|
| `100 Mass. App. Ct. 443, 446 (2021)` | *David v. Kelly* | [Luppold](https://law.justia.com/cases/massachusetts/supreme-court/2025/sjc-13577.html) |
| `487 Mass. at 6` | *Doull* | [Luppold](https://law.justia.com/cases/massachusetts/supreme-court/2025/sjc-13577.html) |
| `488 Mass. 399, 417 (2021)` | *Laramie v. Philip Morris USA Inc.* | [Luppold](https://law.justia.com/cases/massachusetts/supreme-court/2025/sjc-13577.html) |
| `467 Mass. 525, 547 (2014)` | *Selmark Associates v. Ehrlich* | [Luppold](https://law.justia.com/cases/massachusetts/supreme-court/2025/sjc-13577.html) |
| `18 Mass. App. Ct. 249, 254 (1984)` | *Butts v. Zoning Board of Appeals of Falmouth* | [Deckelbaum](https://law.justia.com/cases/massachusetts/court-of-appeals/2024/23-p-443.html) |
| `72 Mass. App. Ct. 419, 426 (2008)` | *Renovator’s Supply, Inc. v. Sovereign Bank* | [Deckelbaum](https://law.justia.com/cases/massachusetts/court-of-appeals/2024/23-p-443.html) |
| `27 Mass. App. Ct. 301, 307 (1989)` | *Harrington v. Fall River Housing Authority* | [Deckelbaum](https://law.justia.com/cases/massachusetts/court-of-appeals/2024/23-p-443.html) |
| `463 Mass. 394, 400 (2012)` | *Marabello v. Boston Bark Corp.* | [Deckelbaum](https://law.justia.com/cases/massachusetts/court-of-appeals/2024/23-p-443.html) |

I am not padding this to ten with reconstructed N.E.3d parallels that do not appear in the linked opinions.

**Connecticut — eight safely verified strings/forms**

| Exact string | Case cited | Source |
|---|---|---|
| `172 Conn. App. 108, 117, 158 A.3d 826` | *State v. Bonds* | [Traynham](https://law.justia.com/cases/connecticut/supreme-court/2025/sc20883.html) |
| `326 Conn. 907, 163 A.3d 1206 (2017)` | Supreme Court certiorari disposition following *Bonds* | [Traynham](https://law.justia.com/cases/connecticut/supreme-court/2025/sc20883.html) |
| `277 Conn. 42, 67, 890 A.2d 474` | *State v. Pierre* | [Traynham](https://law.justia.com/cases/connecticut/supreme-court/2025/sc20883.html) |
| `194 Conn. App. 245, 275, 221 A.3d 45 (2019)` | *State v. Patel* | [Traynham](https://law.justia.com/cases/connecticut/supreme-court/2025/sc20883.html) |
| `342 Conn. 445, 270 A.3d 627` | Supreme Court disposition affirming *Patel* | [Traynham](https://law.justia.com/cases/connecticut/supreme-court/2025/sc20883.html) |
| `184 Conn. App. 786, 805–806, 196 A.3d 366 (2018)` | *Rocco v. Shaikh* | [Troy Laundry](https://law.justia.com/cases/connecticut/court-of-appeals/2025/ac47173.html) |
| `Iacurci v. Wells, supra, 108 Conn. App. 283` | *Iacurci v. Wells* — `supra` short form | [Troy Laundry](https://law.justia.com/cases/connecticut/court-of-appeals/2025/ac47173.html) |
| `158 A.3d 826, cert. denied, 326 Conn. 907, 163 A.3d 1206 (2017)` | *Bonds* plus certiorari-history run | [Traynham](https://law.justia.com/cases/connecticut/supreme-court/2025/sc20883.html) |

The first five expose exactly the parallel-reporter behavior most relevant to the normalizer. The eight-count shortfall is deliberate.

**Maine — twelve verified strings**

| Exact string | Case cited | Source |
|---|---|---|
| `2021 ME 62, ¶¶ 29-31, 264 A.3d 1224` | *Martin v. MacMahan* | [Bagrii](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-38.html) |
| `507 A.2d 596, 598-600 (Me. 1986)` | *Jacobs v. Jacobs* | [Bagrii](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-38.html) |
| `2008 ME 147, ¶ 38-41, 957 A.2d 108` | *Nadeau v. Nadeau* | [Bagrii](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-38.html) |
| `2015 ME 136, ¶ 30-31, 125 A.3d 1149` | *Pearson v. Wendell* | [Bagrii](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-38.html) |
| `2020 ME 53, ¶ 18, 230 A.3d 17` | *State v. Paquin* | [Robshaw](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-50.html) |
| `2020 ME 97, ¶¶ 8-11, 237 A.3d 185` | *State v. Armstrong* | [Robshaw](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-50.html) |
| `2021 ME 39, ¶ 10, 254 A.3d 1171` | *State v. Bentley* | [Robshaw](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-50.html) |
| `2024 ME 80, ¶ 34, 327 A.3d 1103` | *State v. Ketcham* | [Woodard](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-32.html) |
| `622 A.2d 1151, 1154 (Me. 1993)` | *State v. Hewey* | [Woodard](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-32.html) |
| `2013 ME 16, ¶ 5, 60 A.3d 783` | *State v. Hamel* | [Woodard](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-32.html) |
| `2010 ME 30, ¶ 28, 991 A.2d 806` | *State v. Reese* | [Woodard](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-32.html) |
| `2024 ME 25, ¶ 36, 314 A.3d 224` | *Cardilli v. State* | [Woodard](https://law.justia.com/cases/maine/supreme-court/2025/2025-me-32.html) |

This is the clearest neutral-plus-regional test corpus in the batch.

**New Hampshire — two safely verified citation strings**

| Exact string | Case cited | Source |
|---|---|---|
| `2025 N.H. 23` | *Ortolano v. City of Nashua* | [Ortolano](https://law.justia.com/cases/new-hampshire/supreme-court/2025/2024-0181.html) |
| `Claremont III, 144 N.H. at 212` | *Claremont III* | [Rand](https://law.justia.com/cases/new-hampshire/supreme-court/2025/2024-0138.html) |

I could not safely expand incomplete archive-extract fragments such as `159 N.H.` into full cites; doing so would violate the no-reconstruction requirement.

**Rhode Island — seven safely verified strings**

| Exact string | Case cited | Source |
|---|---|---|
| `316 A.3d 1197, 1219-20 (R.I. 2024)` | *Neves v. State* | [Lambert](https://law.justia.com/cases/rhode-island/supreme-court/2025/22-79.html) |
| `316 A.3d at 1220` | *Neves v. State* — short form | [Lambert](https://law.justia.com/cases/rhode-island/supreme-court/2025/22-79.html) |
| `703 A.2d 754, 756 (R.I. 1997)` | *Yang v. State* | [Lambert](https://law.justia.com/cases/rhode-island/supreme-court/2025/22-79.html) |
| `115 A.3d 961, 964 (R.I. 2015) (mem.)` | *State v. Farooq* | [McLean](https://law.justia.com/cases/rhode-island/supreme-court/2025/24-48.html) |
| `5 A.3d at 867` | *Ruffner* — short form | [McLean](https://law.justia.com/cases/rhode-island/supreme-court/2025/24-48.html) |
| `295 A.3d at 67` | *Davis* — short form | [McLean](https://law.justia.com/cases/rhode-island/supreme-court/2025/24-48.html) |
| `102 A.3d 650, 653 (R.I. 2014)` | *Wells v. Smith* | [Roman](https://law.justia.com/cases/rhode-island/supreme-court/2025/24-75.html) |

These establish both full `(R.I. YEAR)` attribution and the state's very terse regional-reporter short forms.

**Vermont — ten verified strings/identifiers**

| Exact string | Case cited | Source |
|---|---|---|
| `2025 VT 11` | *State v. Aaliyah Johnson* | [Johnson](https://law.justia.com/cases/vermont/supreme-court/2025/25-ap-048.html) |
| `2025 VT 35` | *Belter v. City of Burlington* | [Belter](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-275.html) |
| `2025 VT 38` | *Veljovic v. TD Bank, N.A.* | [Veljovic](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-352.html) |
| `2025 VT 51` | *State v. Meta Platforms, Inc.* | [Meta](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-295.html) |
| `2025 VT 15` | *State v. Orost* | [Orost](https://law.justia.com/cases/vermont/supreme-court/2025/23-ap-345.html) |
| `2025 VT 62` | *State v. Shores* | [Shores](https://law.justia.com/cases/vermont/supreme-court/2025/25-ap-337.html) |
| `2022 VT 20, ¶ 7, 216 Vt. 609, 279 A.3d 118 (mem.)` | *State v. LaBrecque* | [Johnson](https://law.justia.com/cases/vermont/supreme-court/2025/25-ap-048.html) |
| `2021 VT 68, ¶ 14` | *State v. Tarbell* | [Johnson](https://law.justia.com/cases/vermont/supreme-court/2025/25-ap-048.html) |
| `2015 VT 2, ¶ 30, 198 Vt. 453, 117 A.3d 798` | *Walsh v. Cluba* | [Veljovic](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-352.html) |
| `2003 VT 62, ¶ 11, 175 Vt.` | *Courchesne v. Town of Weathersfield* — as the linked extraction exposes it | [Belter](https://law.justia.com/cases/vermont/supreme-court/2025/24-ap-275.html) |

The last row is intentionally left at the source-extracted endpoint rather than completed from outside knowledge.

**Delaware — three safely verified state citation strings**

| Exact string | Case cited | Source |
|---|---|---|
| `2005 WL 3031636, at *2 (Del. Nov. 10, 2005)` | *Thomas v. State* | [Sawyer](https://law.justia.com/cases/delaware/supreme-court/2025/186-2024.html) |
| `108 A.3d 1225, 2015 WL 631581, at *2 n.12 (Del. Feb. 11, 2015) (TABLE)` | *Ingram v. State* | [Sawyer](https://law.justia.com/cases/delaware/supreme-court/2025/186-2024.html) |
| `2024 WL 4867172 (Del. Super. Nov. 22, 2024)` | *State v. Daniels* | [Daniels](https://law.justia.com/cases/delaware/supreme-court/2025/532-2024.html) |

The second is particularly valuable because the document itself carries an A.3d + Westlaw parallel for one Delaware Supreme Court table disposition.

### Style mechanics

**Pennsylvania.** The first structural oddity is **spacing instability in the court parenthetical**: current Superior Court output supplies both `Pa.Super.` and `Pa. Super.`. A normalizer therefore should not mistake the space for a jurisdictional distinction. Second, Commonwealth Court unpublished opinions can appear as a compound citation containing blanks for an eventual reporter, docket information, `slip op.`, and Westlaw; Stewart itself cites a 2025 unreported case that way. Third, nonprecedential intermediate opinions are legally citable under Pa.R.A.P. 126 within specified date limits: the Pennsylvania courts' official announcement states that the 2019 amendment permits persuasive citation of Superior Court nonprecedential memoranda filed after May 1, 2019, and Commonwealth Court unreported opinions filed after January 15, 2008. [Official Rule 126 announcement](https://www.pacourts.us/news-and-statistics/news/news-detail/992/pa-supreme-court-adopts-rule-allowing-citation-of-unpublished-superior-court-opinions).

**New Jersey.** `N.J. Super.` **does not, by itself, mean Appellate Division**; actual citations append `(App. Div. YEAR)`, which is exactly why a bare `App. Div.` parenthetical needs state context. Current unpublished opinions place a conspicuous Rule 1:36-3 warning at the beginning: they are nonprecedential and their use is limited. One sampled opinion even contains `N.J. super.` with lowercase `super.`, an input variation worth retaining as a real-world abnormality rather than silently normalizing in the evidence set. The judiciary's house-style reference is the **New Jersey Manual on Style for Judicial Opinions**; the New Jersey State Library preserves the Supreme Court-issued manual here: [New Jersey Manual on Style](https://dspace.njstatelib.org/items/04152d4b-cb2d-4b56-88ac-c5a3e87877e2).

**Maryland.** Two mechanics are load-bearing. First, the **2022 court rename did not replace the historic reporter abbreviations**: a current Appellate Court case may be `261 Md. App. 53`, while an unreported current decision is described in a vendor parenthetical as `Md. App. Ct.`. Second, Maryland opinions still show substantial **parallel-reporter runs** (`Md.`/`Md. App.` plus A.2d/A.3d), so the same case occurrence can expose both official and regional keys. The official opinions page also explains the slip-to-final transition: post-July 2018 electronic opinions are official, initially can have provisional blank Maryland-report pages, and later acquire bound volume/page references. [Official Maryland opinions/publication page](https://www.mdcourts.gov/opinions/opinions).

**Massachusetts.** The strongest house-style tendency in the sampled opinions is **official-reporter-first citation with no redundant court parenthetical**: `Mass.` identifies SJC and `Mass. App. Ct.` identifies the Appeals Court. Short cites collapse further to forms such as `487 Mass. at 6` and `38 Mass. App. Ct. at 499-500`. Luppold also demonstrates traditional `supra` usage in surrounding citations. The state's current official reference is the **SJC Style Manual, Interim Edition (March 2026)**, linked by the Massachusetts Trial Court Law Libraries at [Massachusetts legal writing and citations](https://www.mass.gov/info-details/massachusetts-legal-writing-and-citations). The law-library page explicitly recognizes Northeastern parallel citations, but the sourced appellate opinions themselves are materially more conservative and favor official reporters.

**Connecticut.** Connecticut has the batch's most conspicuous **house-style parallel citation runs** after Vermont and Maine: a state citation commonly contains `Conn.`/`Conn. App.`, a pinpoint, and A.2d/A.3d in a single string. Procedural-history chains can immediately append another official + Atlantic cite, as the `Bonds` certiorari history demonstrates. The sources also show `supra` rather than mechanically repeating a full cite: `Iacurci v. Wells, supra, 108 Conn. App. 283`. The Judicial Branch identifies the **Manual of Style for the Connecticut Courts** and its official reporters on its publications pages. [Connecticut Judicial Branch publications](https://www.jud.ct.gov/pub.htm); [official-publications description](https://vvv.jud.ct.gov/colp/publicat.htm).

**Maine.** The structurally distinctive form is `YYYY ME N, ¶ pin, A.2d/A.3d page`: public-domain decision number and paragraph pin come first, followed by the official Atlantic parallel. This has been the online citation practice since January 1997. Legacy cases immediately expose a different grammar—ordinary reporter/page plus `(Me. YEAR)`, as in `507 A.2d 596, 598-600 (Me. 1986)`. The Judicial Branch itself supplies the canonical example and points to **Uniform Maine Citations** from the Maine Law Review. [Maine published-opinions/citation page](https://www.courts.maine.gov/courts/sjc/opinions.html).

**New Hampshire.** A current slip opinion places the court-issued citation in its front matter before formal New Hampshire Reports publication—`Citation: Ortolano v. City of Nashua, 2025 N.H. 23`—and separately warns that the text remains subject to formal revision before publication in the New Hampshire Reports. The periods in `N.H.` are part of the live form; this is **not** Maine/Vermont-style bare `NH` or `VT`. The same opinion uses numbered paragraphs. I did not verify an authoritative current Rule 20 text/adoption history from the court website, so the style-rule point remains open.

**Rhode Island.** The current house form is compact: regional reporter + pin + `(R.I. YEAR)`. Short forms rapidly collapse to `316 A.3d at 1220`, `5 A.3d at 867`, and `295 A.3d at 67`. The sourced opinion also proves a status parenthetical after the jurisdiction/year, `(mem.)`, in `115 A.3d 961, 964 (R.I. 2015) (mem.)`. I did not locate a current Rhode Island judicial citation manual/rule that I could validate as primary authority in this pass; the opinions themselves are therefore the controlling practice evidence here.

**Vermont.** Rule 28.2 makes paragraph numbering structurally mandatory for post-January 1, 2003 opinions and says pinpoint citations are made by paragraph number. The resulting three-layer full form—`YYYY VT N, ¶ x, volume Vt. page, volume A.3d page`—is unusually information-rich. Current opinions before final print pagination can of course appear simply as `2025 VT 35` or `2025 VT 38`; later citations can carry the full neutral + official + regional run. The rule also permits citation of unpublished judicial dispositions, subject to its conditions. The Vermont Judiciary's official rules page points users to the state's current court rules, while Cornell reproduces Rule 28.2's operative citation language. [Vermont Judiciary rules](https://www.vtcourts.gov/attorneys/rules); [Rule 28.2 reproduction](https://www.law.cornell.edu/citation/sample_vermont).

**Delaware.** Vendor citations are not peripheral noise: they are part of ordinary Supreme Court citation practice for unpublished/table decisions and lower-court orders. A single Supreme Court precedent can appear as an **A.3d + WL parallel**, while a Superior Court order is identified by `(Del. Super. date)`. This makes court attribution in the parenthetical materially important even in a state with no intermediate appellate court. `TABLE` is another useful status token that appears after the Delaware parenthetical.

### Risk flags

| State | (a) Supreme/intermediate prefix collision | (b) District/division-specific intermediate | (c) Reporter edition spans multiple state courts | (d) Apostrophes / ordinals in court abbrev. | (e) Supreme vs intermediate attribution inconsistency |
|---|---|---|---|---|---|
| **PA** | **Yes, structurally.** `Pa.` is the prefix of `Pa. Super.` and `Pa. Cmwlth.`. | **No.** EDA/MDA/WDA and EAP/MAP/WAP are docket identifiers, not cite-parenthetical court districts. | **Yes.** A.3d is used for Supreme, Superior, and Commonwealth Court authority. | **No** in sampled court identifiers. | **Not observed.** |
| **NJ** | **No Fla-like parenthetical collision in house style.** Supreme cases are `N.J.`; intermediate official cites use `N.J. Super.` + `App. Div.`. | **No numbered districts.** The relevant identifier is statewide `App. Div.`. | **Yes, importantly.** `N.J. Super.` is not self-proving as Appellate Division; the `(App. Div.)` qualifier carries court-level information. | **No** apostrophe/ordinal form observed. | **Not observed.** |
| **MD** | **Yes.** `Md.` is a literal prefix of `Md. App.` and current vendor `Md. App. Ct.`. | **No.** | **Yes.** A.2d/A.3d spans Supreme and intermediate authority; official `Md.` and `Md. App.` remain distinct. | **No.** | **Not observed.** |
| **MA** | **Yes at the reporter/court-label level:** `Mass.` / `Mass. App. Ct.`. | **No.** | **Yes for the regional N.E. family**; official reporters themselves are court-specific. | **No.** | **Not observed.** |
| **CT** | **Yes at the reporter/court-label level:** `Conn.` / `Conn. App.`. | **No.** | **Yes.** A.3d parallels both Supreme and Appellate Court decisions. | **No.** | **Not observed.** |
| **ME** | **N/A.** No intermediate appellate court. | **N/A.** | **No appellate split:** one Law Court. | **No.** | **N/A.** |
| **NH** | **N/A.** No intermediate appellate court evidenced. | **N/A.** | **No appellate split evidenced.** | **No.** | **N/A.** |
| **RI** | **N/A.** No intermediate appellate court. | **N/A.** | **No appellate split:** modern A.3d state appellate cases in this corpus are Supreme Court cases. | **No.** | **N/A.** |
| **VT** | **N/A.** No intermediate appellate court. | **N/A.** | **No appellate split** in the Supreme Court citation system. | **No.** | **N/A.** |
| **DE** | **No intermediate-court collision**, but a related lower-court hazard exists: `Del.` vs `Del. Super.`/`Del. Ch.`. | **N/A.** | **Potentially yes across Delaware court levels**, and vendor parentheticals definitely distinguish Supreme from Superior Court; I did not fully prove the A.3d lower-court distribution from this source set. | **No.** | **N/A as framed** because Delaware has no intermediate appellate tier. |

The high-confidence risk calls are directly visible in the source strings: Pennsylvania's three parentheticals, New Jersey's `N.J. Super.` + `App. Div.`, Maryland's `Md.`/`Md. App.`/`Md. App. Ct.`, Massachusetts' `Mass.`/`Mass. App. Ct.`, Connecticut's `Conn.`/`Conn. App.`, and Delaware's `Del.`/`Del. Super.`.

The most important batch-level result is that the Florida failure is **not Florida-specific as a string-shape hazard**: PA, MD, MA, and CT all have highest-court abbreviations that are lexical prefixes of an intermediate-court reporter/court label. Whether that becomes an actual Rule-4 swallow depends on the exact parenthetical forms fed to the mapper, but the collision shape exists. New Jersey is different: its salient discriminator is `App. Div.` attached to `N.J. Super.`, not a numbered DCA-style continuation. This is an inference from the sourced citation forms, not a proposed implementation change.

### Not verified

**Pennsylvania.** I did not verify from a primary Pennsylvania source the exact cessation date, if any formally specified, for Pennsylvania's old official bound reporter as opposed to modern A.3d practice. I also did not prove that identifiers such as `2025 PA Super 253` are formally designated public-domain/neutral citations, or establish their adoption date. They are unquestionably present in current opinion headers; their precise doctrinal status remains unproved. No same-case Supreme/Superior/Commonwealth attribution inconsistency was observed in the sampled opinions.

**New Jersey.** I did not find primary-document evidence that A.3d is routinely used by New Jersey appellate courts for their own in-state authorities; the corpus instead strongly favors `N.J.` and `N.J. Super.`. I therefore do not claim A.3d prevalence merely because the commercial regional reporter contains New Jersey cases. No neutral citation system was verified. No same case was observed being alternately attributed to Supreme Court and Appellate Division. The New Jersey Manual on Style was identified from an official state-library record, but I did not rely on unexamined PDF passages to override actual opinion practice.

**Maryland.** I did not find a current practice in which the same case is commonly assigned inconsistently between the Supreme Court and Appellate Court. The material instead shows clean `Md.` vs `Md. App.` differentiation. I also did not characterize generic Westlaw citation frequency quantitatively; the source set proves that WL is a normal vehicle for unreported Appellate Court authority, not how large a percentage of Maryland citations it represents.

**Massachusetts.** Only **eight** exact test-vector-grade strings are reported above, below the requested ten. I did not reconstruct two more from the large body of official-reporter citations. More importantly for the regional-family mandate, I did **not** establish from the sampled appellate opinions that Massachusetts practitioners or courts routinely cite their own modern cases to `N.E.3d`; the state law library recognizes Northeastern parallel citations, but the actual court documents sampled here strongly prefer `Mass.` and `Mass. App. Ct.`. No neutral/public-domain format or adoption date was verified.

**Connecticut.** This is **not yet a complete proof state**. I validated only **two legal documents**, below the requested three-document floor, and only **eight safely copied state-citation strings/forms**, below the requested ten. The documents are nevertheless high-value because they conclusively prove `Conn.`/`Conn. App.` + A.3d parallel practice and `supra` mechanics. I did not verify a neutral citation format because none appeared, and I did not infer one.

**Maine.** The material is comparatively complete. What I did not independently establish is the exact final volume/date of the old Maine Reports series; the primary Judicial Branch statement establishes the operational fact needed for citation normalization—**Atlantic Reporter has been Maine's official reporter since 1966**—but does not, in the material reviewed here, give a last Maine Reports volume. No intermediate-court, district, or same-case attribution risk exists in the sourced appellate structure.

**New Hampshire.** This state remains **example-incomplete**. Although three born-digital opinions were identified, only **two exact in-state case citation strings** could be safely extracted without filling broken line fragments from outside knowledge. I did not verify from a current primary court rule when the `YYYY N.H. N` identifier was adopted or whether the court formally labels it “public-domain” or “neutral.” I also did not establish current A.3d prevalence from the sampled state opinions. What is verified is the live `2025 N.H. 23` form and continued forthcoming publication in New Hampshire Reports.

**Rhode Island.** Only **seven** exact strings are reported, below the requested ten; I did not backfill with reconstructed citations. I did not verify from a primary Rhode Island source the exact cessation date of Rhode Island Reports. The current documents do prove that modern Supreme Court practice uses A.3d/A.2d with `(R.I. YEAR)`, including `(mem.)` and terse reporter short forms. No neutral citation system was verified, and no current judicial citation manual/rule was located in a form I could responsibly rely on.

**Vermont.** The main mechanics are well proved. The remaining caveat is publication status: Vermont's Judiciary distinguishes published opinions from many three-justice entry orders, and not every current `YYYY VT N` item should be assumed to have the same precedential status merely from the identifier. The source itself may say `ENTRY ORDER`, `(mem.)`, or otherwise disclose status. I did not collapse those distinctions. One copied `Courchesne` string ends at `175 Vt.` because that is where the validated extraction ended; it was deliberately not completed from another database.

**Delaware.** This state is **example-incomplete**: four suitable born-digital Supreme Court documents were identified, but only **three** state-case citation strings were safely extracted at test-vector quality. Those three are nevertheless high-value because they prove Supreme Court `Del.` vendor attribution, lower-court `Del. Super.` attribution, and a single-case A.3d/Westlaw parallel. I did not verify from a primary source the exact cessation date of Delaware Reports, a public-domain citation system, or the full extent to which A.3d contains decisions from Delaware courts below the Supreme Court. I also found no intermediate appellate court to which failure class (e) could apply.


---

## Batch 2 — N.E.3d family

**States covered:** Ohio and Indiana.  
**Massachusetts is not repeated** because it was covered in the prior A./A.3d batch.

The sources below are searchable, born-digital court opinions or public-archive reproductions of born-digital opinions. No example depends on OCR or a scanned reporter page.

---

### Ohio

#### 1. Sources

1. **Bruns v. Green**, Supreme Court of Ohio — useful for district-numbered citations, old unpublished forms, and Supreme Court parallel citations. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2019-1028.html))
2. **Hild v. Samaritan Health Partners**, Supreme Court of Ohio — includes the trailing-parenthetical form for a Second District decision. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-1076.html))
3. **Ohio State Bar Assn. v. Ross**, Supreme Court of Ohio — citation-dense disciplinary opinion. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2018/2018-0782.html))
4. **In re Adoption of A.K.**, Supreme Court of Ohio — includes Eighth District, Supreme Court, and N.E.3d citations. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2022/2020-1163.html))
5. **State v. Faggs**, Supreme Court of Ohio — includes modern Ohio Supreme Court triple-parallel citations. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2018-1501.html))
6. **Torres Friedenberg v. Friedenberg**, Supreme Court of Ohio — includes Sixth District and Eleventh District forms. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2019-0416.html))
7. **State ex rel. Mobarak v. Brown**, Supreme Court of Ohio — especially useful for Tenth District full and short forms. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-0369.html))
8. **Berkheimer v. REKM, L.L.C.**, Supreme Court of Ohio — includes a modern Twelfth District trailing-parenthetical citation. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-0293.html))
9. **Jackson v. Smith**, Supreme Court of Ohio — citation-dense opinion with intermediate-court authorities. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2024-0033.html))
10. **In re National Prescription Opiate Litigation**, Supreme Court of Ohio — recent opinion illustrating current Supreme Court house style. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-1155.html))

Authoritative citation and publication materials:

- **Supreme Court of Ohio Writing Manual**, third edition, effective June 17, 2024. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/opinions-cases/opinions/writing-manual))
- **Supreme Court of Ohio Opinion Search Help**, explaining webcites, official-report citations, and the twelve appellate districts. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/ROD/docs/Help.aspx))
- **Ohio Rules for the Reporting of Opinions**, including the July 1, 2012 official-publication change for courts of appeals and the Court of Claims. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/docs/LegalResources/rules/reporting/Report.pdf))
- **Reporter of Decisions directory**, linking opinions from the First through Twelfth District Courts of Appeals. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/opinions/office-of-the-reporter/))

#### 2. Court structure as cited

Ohio has one **Supreme Court of Ohio** and twelve numbered **district courts of appeals**. The state court’s search guidance expressly identifies twelve appellate districts, and the Reporter of Decisions maintains separate opinion links for the First through Twelfth Districts. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/ROD/docs/Help.aspx))

**Supreme Court.** Modern in-state citations ordinarily identify Supreme Court decisions through the official `Ohio St.3d` reporter, the Ohio webcite, and sometimes an `N.E.3d` parallel. A separate `(Ohio)` court parenthetical is normally unnecessary in Ohio’s own opinions:

- `157 Ohio St.3d 29, 2019-Ohio-2450, 131 N.E.3d 28`
- `154 Ohio St.3d 1476, 2019-Ohio-169, 114 N.E.3d 1204`

The examples are therefore structurally unlike Bluebook citations written for an out-of-state or federal audience, where `(Ohio)` may be supplied.

**Courts of appeals.** Two recurrent forms appear in actual opinions:

1. A district-first form containing the numbered district, county, docket number, webcite, and paragraph:

   `10th Dist. Franklin No. 14AP-517, 2015-Ohio-3007, ¶ 9`

2. A webcite or reporter citation followed by the numbered district in a trailing parenthetical:

   `2023-Ohio-116, ¶ 29 (12th Dist.)`

Ohio uses **numbered districts**, not named divisions. The county and docket number are common in district-first citations, but can disappear when the district is placed in a trailing parenthetical. The selected sources contain actual citations covering all twelve districts.

#### 3. Reporters in actual use

**Official Supreme Court reporter.** `Ohio St.3d` remains an active official reporter for Supreme Court decisions. Ohio’s reporting rules provide for Supreme Court opinions to appear on the court website and in the bound Ohio Official Reports; the opinion-search guidance illustrates a Supreme Court printed citation as `140 Ohio St.3d 1`. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/docs/LegalResources/rules/reporting/Report.pdf))

**Historical appellate official reporter.** `Ohio App.3d` remains heavily cited for older appellate decisions. For newer appellate decisions, Ohio’s website is itself the designated official report: effective **July 1, 2012**, the Supreme Court website became the Ohio Official Reports for opinions of the courts of appeals and the Court of Claims. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/docs/LegalResources/rules/reporting/Report.pdf))

I did not verify an authoritative “last volume” or single cessation date for `Ohio App.3d`. The legally important transition confirmed by the reporting rule is the July 1, 2012 designation of the website as the official report for appellate opinions.

**Regional reporters.** Both `N.E.2d` and `N.E.3d` occur in actual Ohio citations. They can accompany:

- Supreme Court decisions: `157 Ohio St.3d 29, 2019-Ohio-2450, 131 N.E.3d 28`
- Appellate decisions: `2013-Ohio-5867, 6 N.E.3d 57 (7th Dist.)`
- Older official appellate reports: `185 Ohio App.3d 163, 2009-Ohio-6117, 923 N.E.2d 651 (5th Dist.)`

Thus, the regional reporter edition does **not** by itself distinguish the Ohio Supreme Court from an Ohio court of appeals.

**Neutral/public-domain format.** Ohio assigns a webcite in the exact form:

`YYYY-Ohio-N`

The Supreme Court’s search guidance gives `2002-Ohio-1234` as the model and states that each posted decision is assigned a webcite. The reporting rules also provide that court-of-appeals opinions issued after May 1, 2002 may be cited regardless of publication designation. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/ROD/docs/Help.aspx))

Although commonly called a “webcite,” it functions as Ohio’s public-domain identifier. Paragraph pinpoints use `¶` rather than reporter-page pinpoints.

**Westlaw and LEXIS.** Vendor citations appear, but in this sample they are principally fallbacks for older or otherwise unreported decisions, rather than the ordinary citation for currently published Ohio opinions. Examples include:

- `2002 WL 185182`
- `1999 Ohio App. LEXIS 4124`

No defensible prevalence percentage was established from this selected source set.

#### 4. Verbatim examples

The strings below are copied as they appear in the linked opinions.

1. **In re A.C. — First District**

   `1st Dist. Hamilton No. C-180088, 2019-Ohio-2891, ¶ 18`

   Source: *Bruns v. Green*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2019-1028.html))

2. **Hild v. Samaritan Health Partners — Second District**

   `2023-Ohio-2408, ¶ 87 (2d Dist.)`

   Source: *Hild v. Samaritan Health Partners*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-1076.html))

3. **Drees Co. v. Hamilton Twp. — Third District**

   `3d Dist. Mercer No. 10-13-04, 2013-Ohio-5197, ¶ 12-14`

   Source: *Bruns v. Green*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2019-1028.html))

4. **State v. Clay — Fourth District**

   `2013-Ohio-4649, ¶ 6, 78, 89 (4th Dist.)`

   Source: cited Ohio Supreme Court opinion. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2024-0033.html))

5. **Bank of New York v. Miller — Fifth District; official, webcite, and regional run**

   `185 Ohio App.3d 163, 2009-Ohio-6117, 923 N.E.2d 651 (5th Dist.)`

   Source: cited Ohio opinion. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2018/2018-0782.html))

6. **In re Smith — Sixth District**

   `77 Ohio App.3d 1, 16, 601 N.E.2d 45 (6th Dist.1991)`

   Source: cited in *Torres Friedenberg v. Friedenberg*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2022/2020-1163.html))

7. **State v. Rosa — Seventh District**

   `2013-Ohio-5867, 6 N.E.3d 57 (7th Dist.)`

   Source: cited Ohio Supreme Court opinion. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2018-1501.html))

8. **In re A.K. — Eighth District**

   `8th Dist. Cuyahoga No. 105426, 2017-Ohio-9165`

   Source: *In re Adoption of A.K.* ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2022/2020-1163.html))

9. **Boling v. Valecko — Ninth District; Westlaw fallback**

   `9th Dist. Summit No. 20464, 2002 WL 185182 (Feb. 6, 2002), *6`

   Source: cited Ohio opinion. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2019-0416.html))

10. **State v. Mobarak — Tenth District**

    `10th Dist. Franklin No. 14AP-517, 2015-Ohio-3007, ¶ 9`

    Source: *State ex rel. Mobarak v. Brown*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-0369.html))

11. **Schill v. Schill — Eleventh District**

    `11th Dist. Geauga No. 2002-G-2465, 2004-Ohio-5114, at ¶ 47`

    Source: cited in *Torres Friedenberg v. Friedenberg*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2019-0416.html))

12. **Berkheimer v. REKM, L.L.C. — Twelfth District**

    `2023-Ohio-116, ¶ 29 (12th Dist.)`

    Source: *Berkheimer v. REKM, L.L.C.* ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-0293.html))

13. **In re Adoption of B.I. — Supreme Court triple-parallel form**

    `157 Ohio St.3d 29, 2019-Ohio-2450, 131 N.E.3d 28`

    Source: *In re Adoption of A.K.* ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2022/2020-1163.html))

14. **Supreme Court jurisdictional entry in State v. Faggs**

    `154 Ohio St.3d 1476, 2019-Ohio-169, 114 N.E.3d 1204`

    Source: *State v. Faggs*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2018-1501.html))

15. **Cincinnati v. Beretta U.S.A. Corp. — webcite with paragraph pinpoint**

    `2002-Ohio-2480, ¶ 8`

    Source: cited Ohio opinion. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-1155.html))

16. **State ex rel. R.T.G., Inc. v. State — webcite form**

    `2002-Ohio-6716, ¶ 59`

    Source: cited Ohio opinion. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-1155.html))

17. **Dobran v. Franciscan Med. Ctr. — LEXIS form**

    `1999 Ohio App. LEXIS 4124 (Sept. 1, 1999)`

    Source: *Bruns v. Green*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2020/2019-1028.html))

18. **State v. Mobarak — named short form**

    `Mobarak II at ¶ 1`

    Source: *State ex rel. Mobarak v. Brown*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-0369.html))

19. **State v. Mobarak — webcite, regional reporter, district, and paragraph**

    `2017-Ohio-7999, 98 N.E.3d 1023, ¶ 37 (10th Dist.)`

    Source: *State ex rel. Mobarak v. Brown*. ([law.justia.com](https://law.justia.com/cases/ohio/supreme-court-of-ohio/2024/2023-0369.html))

#### 5. Style mechanics

**Manual and governing rules.** The third edition of the Supreme Court of Ohio Writing Manual became effective June 17, 2024. Its opinion-writing rules govern Supreme Court opinions, while the manual is recommended more broadly for Ohio courts and practitioners; the Supreme Court practice rules direct parties to the manual for citation form. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/opinions-cases/opinions/writing-manual))

**Parallel citations remain normal.** Ohio’s house style frequently gives a run consisting of:

`official reporter, webcite, regional reporter`

For example:

`157 Ohio St.3d 29, 2019-Ohio-2450, 131 N.E.3d 28`

Appellate citations may similarly combine `Ohio App.3d`, a webcite, and `N.E.2d`. This is not merely a style-guide prescription; it appears repeatedly in the sourced opinions.

**Paragraph pinpoints.** Modern citations use `¶` and can include multiple paragraph numbers:

`2013-Ohio-4649, ¶ 6, 78, 89 (4th Dist.)`

The reporting rules require numbered paragraphs in reported opinions. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/docs/LegalResources/rules/reporting/Report.pdf))

**Court signal placement varies.** The appellate district may appear:

- Before the reporter or webcite: `8th Dist. Cuyahoga No. ...`
- At the end: `(12th Dist.)`
- Inside a conventional court-and-year parenthetical for older reporter citations: `(6th Dist.1991)`

A parser should therefore not assume that Ohio’s district signal is always adjacent to the right side of the reporter citation.

**Docket information is structural, not random prose.** The district-first form frequently carries:

`<ordinal> Dist. <county> No. <docket>, <webcite>`

The county component can be important because the docket itself is not globally self-identifying.

**Short forms.** Ohio opinions use case-name labels such as `Mobarak II`, followed directly by `at ¶ 1`. That short form contains neither the first page nor the webcite and must inherit from its antecedent.

**Observed deviations or legacy residue.** The sourced opinions contain older typography such as `(6th Dist.1991)` without a space before the year and `at ¶ 47` where newer house style may omit `at`. I did not verify that these are current approved forms rather than faithful reproduction of older citations or publication-system formatting.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix collision:** **Not demonstrated in the ordinary in-state house style.** Ohio Supreme Court decisions usually have no separate `(Ohio)` parenthetical, while intermediate decisions use numbered forms such as `1st Dist.` or `(1st Dist.)`. A broader parser may nevertheless encounter the external Bluebook pair `(Ohio)` and `(Ohio Ct. App.)`; that external-use collision was not proven from the selected Ohio court documents.

**(b) District/division-specific intermediate citations:** **Yes—strongly.** Ohio has twelve appellate districts, and actual citations preserve the ordinal district from `1st Dist.` through `12th Dist.`. District identification may precede the cite or appear in a trailing parenthetical. ([supremecourt.ohio.gov](https://www.supremecourt.ohio.gov/ROD/docs/Help.aspx))

**(c) Reporter edition spans multiple courts within the state:** **Yes.**

- `N.E.3d` contains both Supreme Court and appellate cases.
- `N.E.2d` likewise spans both levels.
- `Ohio App.3d` spans all twelve courts of appeals rather than identifying one district.

Consequently, `N.E.3d` plus an Ohio state inference cannot determine Supreme versus intermediate court without another signal.

**(d) Apostrophes or ordinals in court abbreviations:** **Ordinals are pervasive.** Actual court signals include `1st`, `2d`, `3d`, `4th`, and so on through `12th`. The distinction between Bluebook-style `2d`/`3d` and ordinary `2nd`/`3rd` spelling is parser-relevant. No apostrophe occurs in the core Supreme Court or district-court signals found here.

**(e) Inconsistent Supreme-versus-intermediate attribution of the same case:** **Not verified as a common Ohio practice.** The sources clearly distinguish the levels through official reporter or district signals. No primary-source sample established recurrent attribution drift for the same Ohio decision.

#### 7. Not verified

- The exact final volume or publication date of `Ohio App.3d`.
- A quantitative rate for Westlaw or LEXIS use in Ohio filings.
- Whether current practitioner briefs regularly use `(Ohio)` and `(Ohio Ct. App.)` rather than Ohio’s internal district forms.
- Whether Supreme-versus-appellate attribution inconsistency is common for any particular Ohio case.
- Whether the compressed form `(6th Dist.1991)` reflects an intentional historical style rule, a legacy typesetting convention, or archive formatting.
- Use of first-series `N.E.` in current born-digital Ohio filings was not independently sampled.

---

### Indiana

#### 1. Sources

1. **Hancz-Barron v. State**, Indiana Supreme Court — dense with modern Supreme Court and Court of Appeals regional citations. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2024/22s-lw-00310.html))
2. **WEOC, Inc. v. Adair**, Indiana Supreme Court — useful for Supreme Court and Court of Appeals parentheticals. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2024/23s-ct-00184.html))
3. **Rock Creek Capital, LLC v. Tibbett**, Indiana Supreme Court — contains modern regional-reporter citations and older Court of Appeals authorities. ([law.justia.com](https://law.justia.com/cases/indiana/court-of-appeals/2024/23a-cc-00531.html))
4. **Gilday & Associates, P.C. v. Marion County Assessor**, Indiana Tax Court — shows `Ind. Tax Ct.` and Westlaw fallback practice. ([law.justia.com](https://law.justia.com/cases/indiana/tax-court/2024/22t-ta-00008.html))
5. **Taylor v. State**, Indiana Court of Appeals — memorandum-decision citation under the current post-2023 rule. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2025/25s-cr-00349.html))
6. **Miller v. State**, Indiana Supreme Court — particularly useful for the former official-plus-regional parallel form and transfer history. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2022/22s-cr-00059.html))
7. **ResCare Health Services, Inc. v. Indiana Family & Social Services Administration**, Indiana Supreme Court — distinguishes the Court of Appeals decision from the Supreme Court transfer disposition. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2022/21s-mi-00372.html))
8. **Geiling v. State**, Indiana Supreme Court — contains a long Court of Appeals citation with parenthetical explanation, rehearing, and transfer history. ([law.justia.com](https://law.justia.com/cases/indiana/court-of-appeals/2024/23a-cr-02221.html))

Authoritative citation and publication materials:

- **Indiana Appellate Rule 22**, current version effective January 1, 2024. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/current.htm))
- **Former Indiana Appellate Rule 22**, effective September 1, 2020 and superseded January 1, 2024. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/09-01-2020.htm))
- **Indiana State Library, Indiana Cases**, documenting the historical official reporters and regional-reporter transition. ([in.gov](https://www.in.gov/library/collections-and-services/indiana/indiana-state-documents/locating-indiana-government-documents/))
- **Indiana Judicial Branch appellate decisions portal**, linking Supreme Court, Court of Appeals, and Tax Court decisions. ([in.gov](https://www.in.gov/courts/public-records/appellate-decisions))
- **Indiana Court of Appeals overview**, identifying it as the state’s second-highest court. ([in.gov](https://www.in.gov/courts/appeals/))

#### 2. Court structure as cited

Indiana’s relevant appellate structure consists of:

- **Indiana Supreme Court** — cited as `(Ind.)`
- **Indiana Court of Appeals** — cited as `(Ind. Ct. App.)`
- **Indiana Tax Court** — cited as `(Ind. Tax Ct.)`

The judicial branch’s appellate portal separately identifies the Supreme Court, Court of Appeals, and Tax Court, and describes the Court of Appeals as Indiana’s second-highest court. ([in.gov](https://www.in.gov/courts/public-records/appellate-decisions))

Actual parentheticals include:

- `54 N.E.3d 986, 992 (Ind. 2016)`
- `986 N.E.2d 852, 857 (Ind. Ct. App. 2013)`
- `176 N.E.3d 1000, 1003 (Ind. Tax Ct. 2021)`

Unlike Ohio, Indiana appellate citations do **not** encode an appellate district or division in the citation parenthetical. The Court of Appeals is presented as one statewide court for citation purposes.

Memorandum decisions use the same court abbreviation inside a docket-and-date form:

`Taylor v. State, No. 24A-CR-2107, at *8 (Ind. Ct. App. Mar. 14, 2025) (mem.)`

#### 3. Reporters in actual use

**Historical official reporters.**

The Indiana State Library identifies:

- **Indiana Reports** for Supreme Court decisions, 1847–1981.
- **Reports of the Appellate Court/Court of Appeals** for intermediate decisions, 1891–1979.
- **West’s Indiana Cases**, drawing from the North Eastern Reporter, from September 1980 through 2017. ([in.gov](https://www.in.gov/library/collections-and-services/indiana/indiana-state-documents/locating-indiana-government-documents/))

Older opinions therefore appear in forms such as:

`273 Ind. 34, 38, 401 N.E.2d 697, 699 (1980)`

Here `273 Ind. 34` is the official Indiana Reports citation and `401 N.E.2d 697` is the regional parallel.

**Post-cessation practice.** The current Rule 22 directs published-case citations to the **regional reporter**, using the official reporter only if the case has no regional citation. It no longer requires the historical official-and-regional parallel run. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/current.htm))

This differs from the prior rule, which instructed writers to cite both the regional and official reporters when both were available. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/09-01-2020.htm))

**Regional reporters.** `N.E.2d` and `N.E.3d` are the dominant reporters in the selected modern opinions. The same regional edition is used for:

- Indiana Supreme Court
- Indiana Court of Appeals
- Indiana Tax Court

The court parenthetical is therefore essential. A bare `N.E.3d` citation cannot identify which Indiana appellate court decided the case, much less distinguish Indiana from the other states using the reporter.

**Neutral/public-domain citation.** Indiana does not appear to assign a `YYYY-IN-N`-style neutral identifier to published opinions. Instead, current Rule 22 uses the regional reporter for published decisions.

For memorandum decisions issued on or after **January 1, 2023**, Rule 22 prescribes a docket-and-date format:

`<case name>, No. <appellate case number>, at *<page> (<court> <date>) (mem.)`

That is a formal public-document citation method, but not a case-level neutral identifier comparable to Ohio’s webcite.

**Westlaw and LEXIS.** Westlaw citations occur as fallbacks, particularly in Tax Court and non-reporter contexts. The sample includes:

`Case No. 23T-TA-00023, 2024 WL 1597532, *2-3 (Ind. Tax Ct. Apr. 12, 2024)`

Vendor citations were not the dominant form for published Supreme Court or Court of Appeals decisions in the selected opinions. No quantitative prevalence rate was established.

#### 4. Verbatim examples

1. **Clippinger v. State — Indiana Supreme Court**

   `54 N.E.3d 986, 992 (Ind. 2016)`

   Source: *Hancz-Barron v. State*. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2024/22s-lw-00310.html))

2. **Johnson v. State — Indiana Court of Appeals**

   `986 N.E.2d 852, 857 (Ind. Ct. App. 2013)`

   Source: *Hancz-Barron v. State*. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2024/22s-lw-00310.html))

3. **Ferdinand Sesquicentennial Committee, Inc. v. State — Court of Appeals**

   `637 N.E.2d 178, 180 (Ind. Ct. App. 1994)`

   Source: *WEOC, Inc. v. Adair*. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2024/23s-ct-00184.html))

4. **Vanderhoek v. Willy — footnote pinpoint**

   `728 N.E.2d 213, 216 n.1 (Ind. Ct. App. 2000)`

   Source: *WEOC, Inc. v. Adair*. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2024/23s-ct-00184.html))

5. **Anderson v. Gaudin — Indiana Supreme Court**

   `42 N.E.3d 82, 85 (Ind. 2015)`

   Source: *Rock Creek Capital, LLC v. Tibbett*. ([law.justia.com](https://law.justia.com/cases/indiana/court-of-appeals/2024/23a-cc-00531.html))

6. **Hatcher v. State — Indiana Court of Appeals**

   `762 N.E.2d 189, 192 (Ind. Ct. App. 2002)`

   Source: *Rock Creek Capital, LLC v. Tibbett*. ([law.justia.com](https://law.justia.com/cases/indiana/court-of-appeals/2024/23a-cc-00531.html))

7. **Gilday & Associates, P.C. v. Marion County Assessor — Indiana Tax Court**

   `176 N.E.3d 1000, 1003 (Ind. Tax Ct. 2021)`

   Source: later *Gilday & Associates* opinion. ([law.justia.com](https://law.justia.com/cases/indiana/tax-court/2024/22t-ta-00008.html))

8. **Ciceu v. Marion County Assessor — Tax Court Westlaw form**

   `Case No. 23T-TA-00023, 2024 WL 1597532, *2-3 (Ind. Tax Ct. Apr. 12, 2024)`

   Source: *Gilday & Associates, P.C. v. Marion County Assessor*. ([law.justia.com](https://law.justia.com/cases/indiana/tax-court/2024/22t-ta-00008.html))

9. **Taylor v. State — memorandum-decision form**

   `Taylor v. State, No. 24A-CR-2107, at *8 (Ind. Ct. App. Mar. 14, 2025) (mem.)`

   Source: later Court of Appeals opinion citing the memorandum decision. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2025/25s-cr-00349.html))

10. **Benton v. State — historical official and regional parallel**

    `273 Ind. 34, 38, 401 N.E.2d 697, 699 (1980)`

    Source: *Miller v. State*. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2022/22s-cr-00059.html))

11. **Miller v. State — lower Court of Appeals decision**

    `177 N.E.3d 893, 899–900 (Ind. Ct. App. 2021), vacated`

    Source: *Miller v. State*. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2022/22s-cr-00059.html))

12. **Miller v. State — Supreme Court transfer grant**

    `182 N.E.3d 836 (Ind. 2022)`

    Source: *Miller v. State*. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2022/22s-cr-00059.html))

13. **ResCare Health Services, Inc. v. Indiana Family & Social Services Administration — lower decision**

    `169 N.E.3d 864, 870 (Ind. Ct. App. 2021)`

    Source: Supreme Court opinion in the same litigation. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2022/21s-mi-00372.html))

14. **ResCare — Supreme Court transfer grant**

    `172 N.E.3d 275 (Ind. 2021)`

    Source: Supreme Court opinion in the same litigation. ([law.justia.com](https://law.justia.com/cases/indiana/supreme-court/2022/21s-mi-00372.html))

15. **Simmons v. State — explanatory parenthetical and subsequent history**

    `746 N.E.2d 81, 86 (Ind. Ct. App. 2001) (providing that a finger is an object), reh’g denied, trans. denied`

    Source: *Geiling v. State*. ([law.justia.com](https://law.justia.com/cases/indiana/court-of-appeals/2024/23a-cr-02221.html))

#### 5. Style mechanics

**Current rule.** Indiana Appellate Rule 22, effective January 1, 2024, provides the controlling citation formats. For a published opinion, it calls for the case title, regional-reporter citation—or official reporter if no regional citation exists—and the court and year. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/current.htm))

**Material 2024 change: no required official parallel.** The former rule required a citation to both the regional and official reporters where both existed. The current rule no longer does. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/current.htm))

That temporal distinction is visible in real opinions:

- Historical parallel: `273 Ind. 34, 38, 401 N.E.2d 697, 699 (1980)`
- Modern single reporter: `54 N.E.3d 986, 992 (Ind. 2016)`

A normalizer should accept the historical parallel without treating the current single-reporter form as incomplete.

**Memorandum decisions.** For memorandum decisions issued on or after January 1, 2023, the rule uses the appellate case number, court, full date, star pinpoint, and `(mem.)`. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/current.htm))

The actual sourced form is:

`Taylor v. State, No. 24A-CR-2107, at *8 (Ind. Ct. App. Mar. 14, 2025) (mem.)`

This has no reporter volume or first page. It is structurally closer to an unpublished docket citation than to a conventional neutral citation.

**Transfer history is prominent and legally significant.** Indiana opinions frequently append:

- `trans. denied`
- `vacated`
- A separate Supreme Court citation showing transfer

The current rule expressly addresses subsequent history and transfer dispositions. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/current.htm))

The paired Miller citations demonstrate why court attribution should not be inferred from the case name alone:

- Court of Appeals: `177 N.E.3d 893 ... (Ind. Ct. App. 2021), vacated`
- Supreme Court: `182 N.E.3d 836 (Ind. 2022)`

These are separate decisions in the same litigation, not parallel citations to one opinion.

**Pinpoints.** Indiana uses ordinary reporter pages, page ranges with an en dash, and footnote pinpoints such as `216 n.1`. Memorandum decisions use star pagination, for example `at *8`.

**Apostrophes beyond the court token.** The court names themselves are straightforward, but subsequent-history tokens include the typographic apostrophe in `reh’g denied`. This can matter when citation-span parsing extends through history clauses.

**Vendor fallback.** The Tax Court source demonstrates a vendor citation prefixed by `Case No.` and followed by a full court-and-date parenthetical. That form should not be collapsed into the ordinary published-opinion template.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix collision:** **Yes.** The Supreme Court signal `(Ind.)` is a literal prefix of both:

- `(Ind. Ct. App.)`
- `(Ind. Tax Ct.)`

A shortest-prefix matcher would swallow the longer intermediate or specialized-court form. Exact or longest-prefix matching is required.

**(b) District/division-specific intermediate citations:** **No in the cited form.** Actual Court of Appeals citations use the statewide `(Ind. Ct. App.)` abbreviation. No numbered district or division appears in the citation parenthetical.

**(c) Reporter edition spans multiple courts within the state:** **Yes.** `N.E.2d` and `N.E.3d` occur in decisions from the Supreme Court, Court of Appeals, and Tax Court. The Indiana State Library also describes the North Eastern reporter collection as containing both Supreme Court and Court of Appeals cases. ([in.gov](https://www.in.gov/library/collections-and-services/indiana/indiana-state-documents/locating-indiana-government-documents/))

**(d) Apostrophes or ordinals in court abbreviations:** **No in the core court abbreviations.** The court tokens are `Ind.`, `Ind. Ct. App.`, and `Ind. Tax Ct.` No ordinal or apostrophe occurs in them. However, the adjacent subsequent-history token `reh’g` contains a typographic apostrophe and is present in actual citation strings.

**(e) Same case cited under Supreme-versus-intermediate attribution inconsistently:** **No common inconsistency was verified.** Indiana instead presents a closely related but important pattern: the same litigation can generate a Court of Appeals opinion and a later Supreme Court opinion after transfer. The sources distinguish those decisions through separate reporter citations and history signals such as `vacated`; Rule 22 requires transfer disposition to be reported. ([rules.incourts.gov](https://rules.incourts.gov/Content/appellate/rule22/current.htm))

A case-name-only resolver could mistake this for inconsistent attribution, but the citations are normally to distinct decisions.

#### 7. Not verified

- A quantitative rate for Westlaw or LEXIS use in Indiana appellate practice.
- Any Indiana public-domain identifier for published opinions comparable to `YYYY-Ohio-N`; none appeared in the current rule or selected opinions.
- A separate current official reporter for Indiana Tax Court decisions.
- Modern born-digital examples using the first-series `N.E.` rather than `N.E.2d` or `N.E.3d`.
- Common erroneous attribution of one identical Indiana opinion to both the Supreme Court and Court of Appeals.
- Whether every public archive preserves memorandum-decision star pagination identically across HTML, PDF, Westlaw, and LEXIS.
- The exact final bound volume numbers of Indiana Reports and Indiana Appellate Reports; the confirmed cessation periods are 1981 and 1979, respectively.


---

## Batch 3 — S.E.2d family

**States covered:** Georgia, North Carolina, Virginia, South Carolina, and West Virginia.

The opinion sources below are contemporary HTML opinions or digitally generated PDFs from court sites and public legal archives. I did not use OCR output or reporter scans. Exact citation strings are reproduced in code formatting without normalizing their punctuation, spacing, apostrophes, reporter abbreviations, or apparent source-level errors.

---

### Georgia

#### 1. Sources

1. **Oskouei v. Matthews**, Supreme Court of Georgia, 2025 — especially dense with Georgia Supreme Court and Court of Appeals authorities, parallel citations, and short forms. [Opinion](https://law.justia.com/cases/georgia/supreme-court/2025/s24g0335.html)
2. **Corkren v. Maynard**, Georgia Court of Appeals, 2025 — numerous `Ga. App.` and `SE2d` citations. [Opinion](https://law.justia.com/cases/georgia/court-of-appeals/2025/a24a1812.html)
3. **State v. Dean**, Georgia Court of Appeals, 2025 — useful for Supreme-versus-intermediate citations, numbered subdivisions, and a house-style deviation. [Opinion](https://law.justia.com/cases/georgia/court-of-appeals/2025/a25a0160.html)
4. **Gwinnett County v. State**, Georgia Court of Appeals, 2025. [Opinion](https://law.justia.com/cases/georgia/court-of-appeals/2025/a25a1243.html)
5. **Harris v. State**, Supreme Court of Georgia, 2025. [Opinion](https://law.justia.com/cases/georgia/supreme-court/2025/s24a0910.html)
6. **Walmart Stores East, LP v. Leverette**, Supreme Court of Georgia, 2025. [Opinion](https://law.justia.com/cases/georgia/supreme-court/2025/s24g1104.html)
7. **Supreme Court of Georgia 2025 opinions directory**, linking the court’s signed opinions and describing their publication status. [Court directory](https://www.gasupreme.us/2025-opinions/)
8. **Georgia Court of Appeals overview**, the court’s official description of the statewide intermediate appellate court. [Georgia.gov](https://georgia.gov/organization/georgia-court-appeals)
9. **Georgia official-reporting provisions**, governing publication in the Georgia Reports and Georgia Appeals Reports. [Statute](https://law.justia.com/codes/georgia/title-50/chapter-18/article-2/section-50-18-26/)
10. **Supreme Court of Georgia Rule 22**, citation-of-authorities rule. [Rule](https://www.courtrules.net/georgia/ga-supreme-court/rule-22)

#### 2. Court structure as cited

Georgia has a **Supreme Court of Georgia** and one statewide **Georgia Court of Appeals**. The intermediate court is not divided into citation-relevant districts or divisions.

In the ordinary in-state published form, the reporter identifies the court:

- Supreme Court: `Ga.`
- Court of Appeals: `Ga. App.`

Accordingly, Georgia opinions generally end these citations with a year-only parenthetical:

- `312 Ga. 647, 650 (864 SE2d 422) (2021)`
- `369 Ga. App. 568 (894 SE2d 141) (2023)`

A separate `(Ga.)` or `(Ga. Ct. App.)` parenthetical is unnecessary in this house style. The official reporter token, not the parenthetical, carries the court-level distinction.

#### 3. Reporters in actual use

**Official reporters.** The current official reporters are:

- `Ga.` — Georgia Reports, Supreme Court decisions.
- `Ga. App.` — Georgia Appeals Reports, Court of Appeals decisions.

The Supreme Court’s current slip opinions state that the electronic opinion remains subject to revision until publication in the advance sheets and that the bound Georgia Reports contain the final official text. No cessation of either official reporter was found.

**Regional reporter.** Georgia decisions are routinely cited in `S.E.2d`. In the dominant Georgia house style observed here, it is written without periods as `SE2d` and enclosed in its own parenthetical after the official citation:

`369 Ga. App. 568 (894 SE2d 141) (2023)`

The regional citation normally includes its first page, while an official-reporter pinpoint can precede it:

`312 Ga. 647, 650 (864 SE2d 422) (2021)`

The samples also prove that not every source conforms: one Court of Appeals opinion uses `S.E.2d` with periods and a comma-separated parallel run.

**Neutral/public-domain format.** No Georgia state-level neutral identifier comparable to `YYYY-Ohio-N` or `YYYY-NCSC-N` appeared in the rules or opinions reviewed. Current unreported decisions are identified by court, docket or opinion number, and date rather than by a universal neutral citation.

**Westlaw and LEXIS.** Vendor citations occur for unreported authorities, but the selected published opinions overwhelmingly use the official-plus-regional form for reported Georgia cases. This source set does not establish a defensible prevalence percentage.

#### 4. Verbatim examples

1. **Matthews v. Oskouei — Court of Appeals**

   `Matthews v. Oskouei, 369 Ga. App. 568 (894 SE2d 141) (2023)`

   Source: *Oskouei v. Matthews*. [Opinion](https://law.justia.com/cases/georgia/supreme-court/2025/s24g0335.html)

2. **American Civil Liberties Union, Inc. v. Zeh — Supreme Court**

   `American Civil Liberties Union, Inc. v. Zeh, 312 Ga. 647, 650 (864 SE2d 422) (2021)`

   Source: *Oskouei v. Matthews*.

3. **Wilkes & McHugh, P.A. v. LTC Consulting, L.P. — Supreme Court**

   `Wilkes & McHugh, P.A. v. LTC Consulting, L.P., 306 Ga. 252, 261 (830 SE2d 119) (2019)`

   Source: *Oskouei v. Matthews*.

4. **Saye v. Deloitte & Touche, LLP — Court of Appeals**

   `Saye v. Deloitte & Touche, LLP, 295 Ga. App. 128, 131 (670 SE2d 818) (2008)`

   Source: *Oskouei v. Matthews*.

5. **Murray v. Community Health Systems Professional Corporation — Court of Appeals**

   `Murray v. Community Health Systems Professional Corporation, 345 Ga. App. 279, 286 (811 SE2d 531) (2018)`

   Source: *Oskouei v. Matthews*.

6. **Seals v. State — Supreme Court**

   `Seals v. State, 311 Ga. 739, 740 (860 SE2d 419) (2021)`

   Source: *Oskouei v. Matthews*.

7. **Gonzales v. State — Supreme Court**

   `Gonzales v. State, 315 Ga. 661 (884 SE2d 339) (2023)`

   Source: *Oskouei v. Matthews*.

8. **Olevik v. State — Supreme Court**

   `Olevik v. State, 302 Ga. 228, 235 (806 SE2d 505) (2017)`

   Source: *Oskouei v. Matthews*.

9. **Planet Insurance Co. v. Ferrell — Court of Appeals**

   `Planet Ins. Co. v. Ferrell, 228 Ga. App. 264, 266 (491 SE2d 471) (1997)`

   Source: *Corkren v. Maynard*. [Opinion](https://law.justia.com/cases/georgia/court-of-appeals/2025/a24a1812.html)

10. **Irvin v. Lowe’s of Gainesville, Inc. — Court of Appeals, numbered division**

    `Irvin v. Lowe’s of Gainesville, Inc., 165 Ga. App. 828, 829 (1) (302 SE2d 734) (1983)`

    Source: *Corkren v. Maynard*.

11. **Harrison v. McAfee — Court of Appeals, numbered division**

    `Harrison v. McAfee, 338 Ga. App. 393, 395 (2) (788 SE2d 872) (2016)`

    Source: *Corkren v. Maynard*.

12. **Tisdale v. City of Cumming — Court of Appeals, page range**

    `Tisdale v. City of Cumming, 326 Ga. App. 19, 22-23 (755 SE2d 833) (2014)`

    Source: *Corkren v. Maynard*.

13. **State v. Copeland — Supreme Court, nested subdivision**

    `State v. Copeland, 310 Ga. 345, 351 (2) (b) (850 SE2d 736) (2020)`

    Source: *State v. Dean*. [Opinion](https://law.justia.com/cases/georgia/court-of-appeals/2025/a25a0160.html)

14. **Snellings v. State — Court of Appeals**

    `Snellings v. State, 371 Ga. App. 795, 798 (903 SE2d 177) (2024)`

    Source: *State v. Dean*.

15. **Jackson v. State — Court of Appeals, non-house-style parallel**

    `Jackson v. State, 335 Ga. App. 630, 632, 782 S.E.2d 691, 693 (2016)`

    Source: *State v. Dean*. The source itself uses periods in `S.E.2d` and separates the reporter by commas rather than a regional-reporter parenthetical.

16. **Matthews — named short form**

    `Matthews, 369 Ga. App. at 575`

    Source: *Oskouei v. Matthews*.

17. **Zeh — named short form**

    `Zeh, 312 Ga. at 650`

    Source: *Oskouei v. Matthews*.

18. **Id. short form**

    `Id. at 573-575.`

    Source: *Oskouei v. Matthews*.

#### 5. Style mechanics

**Parallel reporter in parentheses.** The most distinctive Georgia mechanic is the placement of the regional reporter in a standalone parenthetical:

`306 Ga. 252, 261 (830 SE2d 119) (2019)`

The official reporter and its pinpoint come first; the regional reporter follows in parentheses; the year follows in a second parenthetical. This differs from the comma-separated parallel format common in North Carolina, South Carolina, and West Virginia.

**Georgia’s house abbreviation is `SE2d`.** Most selected opinions omit the periods used in Bluebook-style `S.E.2d`. The `Jackson` citation proves that filed or published material is not perfectly uniform, so both punctuation forms are real-world inputs.

**Numbered opinion divisions are embedded after the pinpoint.** Examples include:

- `829 (1)`
- `395 (2)`
- `351 (2) (b)`

These are not court divisions. They identify numbered portions of the cited opinion and can appear between the official pinpoint and regional parallel.

**Short forms retain the official reporter.** `Matthews, 369 Ga. App. at 575` and `Zeh, 312 Ga. at 650` identify the antecedent by case name, official volume, reporter, and pin page. `Id.` can omit all reporter information.

**Rule and observed deviation.** Rule 22 directs parties toward Georgia’s official-reporter citation form, while the sampled opinions demonstrate both the standard `SE2d` parenthetical and at least one comma-separated `S.E.2d` deviation.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix collision:** **Not in the dominant published house form.** `Ga.` and `Ga. App.` are reporter tokens rather than court parentheticals, and exact reporter matching distinguishes them. A generic prefix algorithm could still treat `Ga.` as a prefix of `Ga. App.`, so longest-token recognition is required at the reporter level. The selected opinions did not prove recurrent use of the external parenthetical pair `(Ga.)` and `(Ga. Ct. App.)`.

**(b) District/division-specific intermediate citations:** **No.** The Georgia Court of Appeals is cited statewide as `Ga. App.`. Parentheticals such as `(1)` and `(2) (b)` are opinion subdivisions, not appellate districts.

**(c) Reporter edition spans multiple courts in the state:** **Yes for `S.E.2d`; no for the two current official reporters.** `S.E.2d` contains both Supreme Court and Court of Appeals decisions. `Ga.` identifies the Supreme Court; `Ga. App.` identifies the intermediate court.

**(d) Apostrophes or ordinals in court abbreviations:** **No in the core court/reporter abbreviations.** Typographic apostrophes are common in party names, including `Lowe’s`, but not in `Ga.` or `Ga. App.`. Numbered opinion subdivisions must not be mistaken for court ordinals.

**(e) Same case commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** No primary-source example established that the same Georgia opinion is commonly attributed to both levels.

#### 7. Not verified

- A current Georgia-issued neutral/public-domain citation system.
- A quantitative Westlaw or LEXIS usage rate.
- Common use in Georgia filings of explicit `(Ga.)` or `(Ga. Ct. App.)` parentheticals when an official reporter citation is present.
- Recurrent Supreme-versus-Court-of-Appeals attribution drift for the same Georgia opinion.
- Whether the `Jackson` comma-separated `S.E.2d` form originated with the authoring court, an incorporated quotation, or archive processing. The source unmistakably contains it, but its production history was not confirmed.

---

### North Carolina

#### 1. Sources

1. **State v. Hunt**, Supreme Court of North Carolina, 2025 — includes a recent regional-only Court of Appeals citation and an official-only Supreme Court citation. [Opinion](https://law.justia.com/cases/north-carolina/supreme-court/2025/280a24.html)
2. **Griffin v. North Carolina State Board of Elections**, North Carolina Court of Appeals, 2025 — exceptionally citation-dense and useful for official-plus-regional parallels, blanks pending official pagination, typographic apostrophes, and subsequent history. [Opinion](https://law.justia.com/cases/north-carolina/court-of-appeals/2025/25-181.html)
3. **Blackrock Equestrian, LLC v. Town of Southern Pines**, Court of Appeals, 2025 — official and regional citations, including a source-level extra parenthesis. [Opinion](https://law.justia.com/cases/north-carolina/court-of-appeals/2025/25-359.html)
4. **Leech v. State**, Court of Appeals, 2025 — recent Court of Appeals citations and a vendor fallback for a not-yet-bound decision. [Opinion](https://law.justia.com/cases/north-carolina/court-of-appeals/2025/24-1113.html)
5. **State v. Windseth**, Court of Appeals, 2025 — demonstrates competing `N.C. App. Ct.`/official-reporter forms. [Opinion](https://law.justia.com/cases/north-carolina/court-of-appeals/2025/24-718.html)
6. **Vaitovas v. City of Greenville**, Court of Appeals, 2022 — contemporaneous universal-citation-era opinion. [Opinion](https://law.justia.com/cases/north-carolina/court-of-appeals/2022/20-889.html)
7. **State v. Johnson**, Supreme Court, 2021 — contemporaneous Supreme Court universal citation. [Opinion](https://law.justia.com/cases/north-carolina/supreme-court/2021/420a20.html)
8. **North Carolina Rules of Appellate Procedure**, current official rules page. [Rules](https://www.nccourts.gov/courts/supreme-court/court-rules/north-carolina-rules-of-appellate-procedure)
9. **Order adopting universal citations**, effective January 1, 2021. [Press release](https://www.nccourts.gov/news/tag/press-release/supreme-court-of-north-carolina-adopts-universal-citation-format)
10. **Order withdrawing the universal-citation system**, issued January 13, 2023. [Press release](https://www.nccourts.gov/news/tag/press-release/supreme-court-of-north-carolina-withdraws-order-implementing-universal-citation-system)

#### 2. Court structure as cited

North Carolina has a **Supreme Court of North Carolina** and a statewide **North Carolina Court of Appeals**.

In bound official citations:

- Supreme Court: `N.C.`
- Court of Appeals: `N.C. App.`

Examples:

- `386 N.C. 1, 4, 900 S.E.2d 838, 843 (2024)`
- `118 N.C. App. 698, 700, 456 S.E.2d 878, 879 (1995)`

The official reporter identifies the court, so the final parenthetical can contain the year alone.

When a recent decision has only a regional citation, the court can instead be expressed in the parenthetical. The sources contain at least two word orders:

- `(N.C. Ct. App. 2024)`
- `(N.C. App. Ct. 2024)`

That variation is directly relevant to exact court-parenthetical matching.

No district or division identifier appears in the Court of Appeals citation.

#### 3. Reporters in actual use

**Official reporters.**

- `N.C.` — Supreme Court.
- `N.C. App.` — Court of Appeals.

Both remain active. Recent slip opinions may initially cite a case using only `S.E.2d`, an incomplete official citation containing blanks, or an official citation without the regional parallel. The 2023 withdrawal order explained that improvements in publication now made official citations available quickly enough that the temporary universal-citation system was no longer needed.

**Regional reporter.** `S.E.2d` is common and often appears as a full parallel:

`386 N.C. 1, 4, 900 S.E.2d 838, 843 (2024)`

Both first pages and both pin pages may be supplied. `S.E.2d` spans the Supreme Court and Court of Appeals and therefore cannot identify the court by itself.

**Universal/public-domain format.** North Carolina adopted universal citations effective **January 1, 2021**, using:

- `YYYY-NCSC-N` for Supreme Court opinions.
- `YYYY-NCCOA-N` for Court of Appeals opinions.
- Paragraph pinpoints using `¶`.

The Supreme Court withdrew the system on **January 13, 2023**. The 2021–2022 identifiers remain real citation strings in opinions issued during that period, even though new opinions no longer receive them.

**Vendor citations.** Westlaw citations occur for unpublished opinions and recent decisions awaiting complete official publication. They are a practical fallback, but no prevalence percentage was measured.

#### 4. Verbatim examples

1. **State v. Hunt — lower Court of Appeals decision cited regionally**

   `908 S.E.2d 92 (N.C. Ct. App. 2024)`

   Source: *State v. Hunt*. [Opinion](https://law.justia.com/cases/north-carolina/supreme-court/2025/280a24.html)

2. **State v. Reber — Supreme Court, official-only**

   `State v. Reber, 386 N.C. 153 (2024)`

   Source: *State v. Hunt*.

3. **Bouvier v. Porter — Supreme Court full parallel**

   `Bouvier v. Porter, 386 N.C. 1, 4, 900 S.E.2d 838, 843 (2024)`

   Source: *Griffin v. North Carolina State Board of Elections*. [Opinion](https://law.justia.com/cases/north-carolina/court-of-appeals/2025/25-181.html)

4. **Appeal of Harper — Court of Appeals full parallel**

   `Appeal of Harper, 118 N.C. App. 698, 700, 456 S.E.2d 878, 879 (1995)`

   Source: *Griffin*.

5. **In re Brown — Court of Appeals, source’s Unicode range character preserved**

   `In re Brown, 56 N.C. App. 629, 630, 289 S.E.2d 626, 626−27 (1982)`

   Source: *Griffin*. The regional range uses the source’s `−` character, not a hyphen or en dash.

6. **In re Redmond — Supreme Court full parallel**

   `In re Redmond, 369 N.C. 490, 493, 797 S.E.2d 275, 277 (2017)`

   Source: *Griffin*.

7. **Griffin — pending official pagination**

   `Griffin v. N.C. State Bd. of Elections, __ N.C. __, __, 910 S.E.2d 348 (2025)`

   Source: *Griffin*.

8. **Thompson v. Union County — Court of Appeals full parallel**

   `Thompson v. Union Cnty., 283 N.C. App. 547, 553, 874 S.E.2d 623, 628 (2022)`

   Source: *Griffin*.

9. **Sutton v. North Carolina Department of Labor — typographic apostrophe**

   `Sutton v. N.C. Dep’t of Lab., 132 N.C. App. 387, 389, 511 S.E.2d 340, 342 (1999)`

   Source: *Griffin*.

10. **Pender County v. Bartlett — parallel citation plus federal subsequent history**

    `Pender County v. Bartlett, 361 N.C. 491, 510, 649 S.E.2d 364, 376 (2007), aff’d sub nom. Bartlett v. Strickland, 556 U.S. 1, 129 S. Ct. 1231, 173 L. Ed. 2d 173 (2009)`

    Source: linked North Carolina Court of Appeals opinion.

11. **Veazey v. City of Durham — source-level extra closing parenthesis**

    `Veazey v. City of Durham, 231 N.C. 357, 361–62, 57 S.E.2d 377, 381 (1950))`

    Source: *Blackrock Equestrian, LLC v. Town of Southern Pines*. The source contains the second closing parenthesis.

12. **Barrow v. D.A.N. Joint Venture Properties of North Carolina, LLC — Court of Appeals**

    `Barrow v. D.A.N. Joint Venture Props. of N.C., LLC, 232 N.C. App. 528, 534, 755 S.E.2d 641, 646 (2014)`

    Source: *Blackrock Equestrian*.

13. **Askew v. City of Kinston — Supreme Court**

    `Askew v. City of Kinston, 386 N.C. 286, 299, 902 S.E.2d 722, 732 (2024)`

    Source: *Blackrock Equestrian*.

14. **State v. Nanes — Court of Appeals**

    `State v. Nanes, 297 N.C. App. 863, 870, 912 S.E.2d 202, 209 (2025)`

    Source: *Leech v. State*.

15. **State v. Hollis — regional-only intermediate citation, alternate court-name order**

    `State v. Hollis, 905 S.E.2d 265, 267 (N.C. App. Ct. 2024)`

    Source: *State v. Windseth*.

16. **State v. Johnson — Supreme Court universal citation**

    `2021-NCSC-165`

    Source: opinion header in *State v. Johnson*.

17. **Vaitovas v. City of Greenville — Court of Appeals universal citation**

    `2022-NCCOA-169`

    Source: opinion header in *Vaitovas*.

18. **Unpublished Court of Appeals universal citation**

    `2022-NCCOA-938`

    Source: linked unpublished North Carolina Court of Appeals opinion.

#### 5. Style mechanics

**Full double-pin parallel runs.** North Carolina commonly gives:

`official volume + official first page + official pin, regional volume + regional first page + regional pin`

For example:

`386 N.C. 1, 4, 900 S.E.2d 838, 843 (2024)`

This is structurally different from Georgia’s parenthesized regional reporter.

**Publication-stage variability.** Current sources contain all of the following:

- Official-only: `386 N.C. 153 (2024)`
- Regional-only with explicit court: `908 S.E.2d 92 (N.C. Ct. App. 2024)`
- Incomplete official plus regional: `__ N.C. __, __, 910 S.E.2d 348 (2025)`
- Full official-plus-regional parallel.

That variation reflects publication timing and makes the parenthetical materially important when the official reporter is absent.

**Temporary universal-citation era.** The 2021–2022 identifiers are not reconstructed conventions; they were assigned under an official order. The system was formally withdrawn in January 2023, so the normalizer must recognize legacy `NCSC` and `NCCOA` strings without assuming that current opinions continue the sequence.

**Unpublished decisions.** North Carolina’s rule warning states that an unpublished opinion does not constitute controlling legal authority and that citation is disfavored, except as permitted by the rule. Unpublished decisions can nevertheless carry a universal-era identifier, a docket number, or a vendor citation.

**Real-source deviations.** The source set contains:

- Both `N.C. Ct. App.` and `N.C. App. Ct.`
- A typographic `Dep’t`
- A Unicode minus sign in `626−27`
- An apparent extra closing parenthesis in the *Veazey* string.

Those are real extraction inputs and should not be replaced with an imagined uniform form.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix collision:** **Yes when explicit court parentheticals are used.** `(N.C.)` is a prefix-like state signal within `(N.C. Ct. App.)` and `(N.C. App. Ct.)`. Official-reporter citations usually avoid the issue because `N.C.` and `N.C. App.` independently identify the court, but regional-only citations require exact recognition of the longer parenthetical.

**(b) District/division-specific intermediate citations:** **No.** The Court of Appeals citation does not encode a district or division.

**(c) Reporter edition spans multiple courts in the state:** **Yes.** `S.E.2d` contains both Supreme Court and Court of Appeals decisions. The official reporters separate them.

**(d) Apostrophes or ordinals in court abbreviations:** **No in the core court abbreviations.** Typographic apostrophes frequently occur elsewhere in the citation string—`Dep’t`, `aff’d`, party names—and therefore still matter to span handling.

**(e) Same case commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** Publication-stage changes can transform a regional-only citation into an official parallel, but the source set did not establish recurrent court-level attribution inconsistency for one identical opinion.

#### 7. Not verified

- A post-January 2023 North Carolina neutral-citation replacement; none was identified.
- A quantitative percentage of vendor citations in appellate briefs or opinions.
- Whether `N.C. App. Ct.` is an affirmatively approved house abbreviation or a recurring author-level inversion of `N.C. Ct. App.`.
- Common Supreme-versus-Court-of-Appeals attribution drift for one opinion.
- Whether the extra parenthesis in the *Veazey* citation originated in the court’s filed PDF or the public archive’s HTML conversion.

---

### Virginia

#### 1. Sources

1. **Drasovean v. Walts**, Court of Appeals of Virginia sitting en banc, 2025 — useful for Court of Appeals slip citations, Supreme Court official citations, blanks pending publication, and short forms. [Opinion](https://law.justia.com/cases/virginia/court-of-appeals-published/2025/0259-23-4.html)
2. **Highlander v. Department of Wildlife Resources**, Court of Appeals, 2025 — numerous `Va.` and `Va. App.` authorities. [Opinion](https://law.justia.com/cases/virginia/court-of-appeals-published/2025/2110-23-2.html)
3. **City of Virginia Beach v. Mathias**, Court of Appeals, 2025 — recent intermediate-court citations and an en banc parenthetical. [Opinion](https://law.justia.com/cases/virginia/court-of-appeals-published/2025/2073-23-1.html)
4. **AV Automotive, LLC v. Bavely**, Court of Appeals, 2025. [Opinion](https://law.justia.com/cases/virginia/court-of-appeals-published/2025/2168-23-4.html)
5. **Smith v. Commonwealth**, Court of Appeals, 2025. [Opinion](https://law.justia.com/cases/virginia/court-of-appeals-published/2025/0949-24-2.html)
6. **Beebout v. Commonwealth**, unpublished Court of Appeals opinion, 2025. [Opinion](https://law.justia.com/cases/virginia/court-of-appeals-unpublished/2025/1466-23-2.html)
7. **Commonwealth v. Jackson**, Supreme Court of Virginia, 2025 — especially useful for a partially paginated official/regional parallel and a `Va. App. LEXIS` citation. [Opinion](https://law.justia.com/cases/virginia/supreme-court/2025/240843.html)
8. **Virginia appellate-opinions portal**, official Supreme Court and Court of Appeals publication archive. [Court portal](https://www.courts.state.va.us/opinions/home)
9. **Rules of the Supreme Court of Virginia**, official rules page. [Rules](https://vacourts.gov/courts/scv/rules)

#### 2. Court structure as cited

Virginia’s relevant appellate courts are:

- **Supreme Court of Virginia**
- **Court of Appeals of Virginia**

The official reporter forms are:

- Supreme Court: `Va.`
- Court of Appeals: `Va. App.`

Examples:

- `268 Va. 624, 633 (2004)`
- `76 Va. App. 596, 612 (2023)`

Because the official reporter identifies the court, ordinary bound citations end with a year-only parenthetical.

Unpublished or not-yet-reported Court of Appeals decisions use the explicit parenthetical:

`(Va. Ct. App. Nov. 6, 2024)`

The Court of Appeals docket suffixes—such as `-1`, `-2`, or `-4`—appear in docket numbers but are not cited as appellate districts or divisions.

#### 3. Reporters in actual use

**Official reporters.**

- `Va.` — Supreme Court of Virginia.
- `Va. App.` — Court of Appeals of Virginia.

Both remain active. The official court portal continues to publish opinions from both courts, and recent opinions cite current cases in those reporters.

**Regional reporter.** `S.E.2d` remains an actual Virginia reporter, but current Virginia opinions in the sample usually cite their own state decisions by official reporter alone. A particularly informative transitional example is:

`304 Va. 200, ___, 914 S.E.2d 176, 181-83 (2025)`

The official first page had been assigned, the official pinpoint remained blank, and the regional reporter supplied a complete pin range.

**Unreported decisions.** A current Court of Appeals slip opinion may be cited by:

`No. <docket>, slip op. at <pages> (Va. Ct. App. <full date>)`

**Vendor citations.** The sources include `Va. App. LEXIS` for an intermediate decision that did not yet have a conventional published citation. Westlaw and LEXIS are therefore genuine fallback forms, though no prevalence percentage was established.

**Neutral/public-domain format.** No Virginia universal identifier comparable to `YYYY-NCSC-N` was found. Docket-plus-date slip citation is not a case-level neutral sequence.

#### 4. Verbatim examples

1. **Drasovean v. Walts — Court of Appeals slip citation**

   `Drasovean v. Walts, No. 0259-23-4, slip op. at 27-28 (Va. Ct. App. Nov. 6, 2024)`

   Source: en banc *Drasovean v. Walts*.

2. **Drasovean dissent — Id. with judge parenthetical**

   `Id. at 29-30 (Callins, J., dissenting)`

   Source: *Drasovean*.

3. **Kellam v. School Board of the City of Norfolk — Supreme Court**

   `Kellam v. School Board of the City of Norfolk, 202 Va. 252 (1960)`

   Source: *Drasovean*.

4. **City of Chesapeake v. Cunningham — Supreme Court**

   `City of Chesapeake v. Cunningham, 268 Va. 624, 633 (2004)`

   Source: *Drasovean*.

5. **Fines v. Rappahannock Area Community Services Board — Supreme Court**

   `Fines v. Rappahannock Area Cmty. Servs. Bd., 301 Va. 305, 313 (2022)`

   Source: *Drasovean*.

6. **Hinchey v. Ogden — Supreme Court**

   `Hinchey v. Ogden, 226 Va. 234, 238 (1983)`

   Source: *Drasovean*.

7. **Suffolk City School Board v. Wahlstrom — Supreme Court**

   `Suffolk City Sch. Bd. v. Wahlstrom, 302 Va. 188, 221 (2023)`

   Source: *Drasovean*.

8. **Newport News School Board v. Z.M. — pending official pages**

   `Newport News School Board v. Z.M., ___ Va. ___, ___ (May 8, 2025)`

   Source: *Drasovean*.

9. **Page v. Portsmouth Redevelopment & Housing Authority — pending official pages**

   `Page v. Portsmouth Redev. & Hous. Auth., ___ Va. ___, ___ (July 3, 2024)`

   Source: *Drasovean*.

10. **Large v. Clinchfield Coal Co. — Supreme Court**

    `Large v. Clinchfield Coal Co., 239 Va. 144, 148 (1990)`

    Source: *Highlander v. Department of Wildlife Resources*.

11. **Theologis v. Weiler — Court of Appeals**

    `Theologis v. Weiler, 76 Va. App. 596, 612 (2023)`

    Source: *City of Virginia Beach v. Mathias*.

12. **Pereira v. Commonwealth — Court of Appeals**

    `Pereira v. Commonwealth, 83 Va. App. 431, 445 (2025)`

    Source: *Mathias*.

13. **Whitt v. Commonwealth — Court of Appeals en banc**

    `Whitt v. Commonwealth, 61 Va. App. 637, 659 (2013) (en banc)`

    Source: *Mathias*.

14. **Commonwealth v. Canales — official and regional transitional parallel**

    `Commonwealth v. Canales, 304 Va. 200, ___, 914 S.E.2d 176, 181-83 (2025)`

    Source: *Commonwealth v. Jackson*.

15. **Jackson — Court of Appeals LEXIS citation**

    `Jackson, 2024 Va. App. LEXIS 499, at *8-9`

    Source: *Commonwealth v. Jackson*.

16. **Smith v. Commonwealth — Court of Appeals**

    `Smith v. Commonwealth, 27 Va. App. 357 (1998)`

    Source: *Commonwealth v. Jackson*.

17. **Lawlor — official-reporter short form**

    `Lawlor, 285 Va. at 263-67`

    Source: *Commonwealth v. Jackson*.

#### 5. Style mechanics

**Official-reporter-first practice.** Unlike Georgia, North Carolina, South Carolina, and West Virginia, current Virginia appellate opinions in this sample usually cite Virginia cases with only `Va.` or `Va. App.` and the year. Routine `S.E.2d` parallels are uncommon in the sampled current opinions.

**Publication-stage hybrids.** The *Canales* string proves that one citation can have:

- An assigned official first page.
- A blank official pin.
- A complete regional reporter and pin.

The blank is not safely reconstructable and should remain unresolved as written for that component.

**Slip citations.** The intermediate court’s unreported form can include:

- `No.`
- Full docket number.
- `slip op. at`
- Explicit court.
- Full decision date.

The `-4` in `0259-23-4` belongs to the docket identifier and is not a parenthetical district.

**Vendor short form.** `Jackson, 2024 Va. App. LEXIS 499, at *8-9` lacks a conventional reporter first page but contains a court-specific LEXIS edition. It is structurally distinguishable from generic LEXIS.

**No dedicated citation manual verified.** The Rules of the Supreme Court of Virginia govern appellate filings, but I did not locate a separate current court-issued citation manual analogous to Ohio’s writing manual. The strongest format evidence here is therefore the courts’ own opinions.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix collision:** **Potentially yes in explicit parentheticals.** `Va.` is the state/Supreme signal and is a prefix of `Va. Ct. App.`. Ordinary official citations largely avoid the collision because `Va.` and `Va. App.` are distinct reporter tokens. Slip and vendor forms require recognition of the longer court name.

**(b) District/division-specific intermediate citations:** **No.** Court of Appeals docket suffixes such as `-4` are not citation-level district identifiers.

**(c) Reporter edition spans multiple courts in the state:** **Yes for `S.E.2d`.** The official reporters `Va.` and `Va. App.` distinguish the two courts.

**(d) Apostrophes or ordinals in court abbreviations:** **No in the core court abbreviations.** Docket suffixes contain digits, but the court token itself does not use ordinals.

**(e) Same case commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** The source set contains Supreme Court review of Court of Appeals decisions but no proof that one identical opinion is commonly assigned to both courts.

#### 7. Not verified

- A current Virginia neutral/public-domain citation system.
- A separate binding Virginia court citation manual beyond the appellate rules.
- Quantitative Westlaw/LEXIS prevalence.
- Common court-attribution inconsistency for the same Virginia opinion.
- Whether all docket suffixes correspond to particular administrative regions or panels; whatever their administrative meaning, the sources did not use them as court parentheticals.
- A formal cessation date for routine `S.E.2d` parallel citations, because no cessation was established; current practice simply favors the official reporter in the sampled opinions.

---

### South Carolina

#### 1. Sources

1. **State v. Daniels**, Supreme Court of South Carolina, 2025 — cites the lower Court of Appeals opinion in full official-plus-regional form. [Opinion](https://law.justia.com/cases/south-carolina/supreme-court/2025/28268.html)
2. **Marlowe v. South Carolina Department of Transportation**, Supreme Court, 2025 — dense with Supreme Court and Court of Appeals parallels and a dual-reporter `id.` short form. [Opinion](https://law.justia.com/cases/south-carolina/supreme-court/2025/28271.html)
3. **Planned Parenthood South Atlantic v. State**, Supreme Court, 2025. [Opinion](https://law.justia.com/cases/south-carolina/supreme-court/2025/28280.html)
4. **State v. Pray**, Supreme Court memorandum disposition, 2025 — cites an unpublished Court of Appeals opinion by opinion number and filing date. [Opinion](https://law.justia.com/cases/south-carolina/supreme-court/2025/2025-mo-031.html)
5. **State v. Barclay**, unpublished Court of Appeals opinion, 2025. [Opinion](https://law.justia.com/cases/south-carolina/court-of-appeals/2025/2025-up-259.html)
6. **Kirk v. State**, unpublished Court of Appeals opinion, 2025. [Opinion](https://law.justia.com/cases/south-carolina/court-of-appeals/2025/2025-up-279.html)
7. **South Carolina Appellate Court Rule 268**, official citation, publication, and precedential-status rule. [Rule](https://www.sccourts.org/resources/judicial-community/court-rules/appellate/rule-268/)
8. **Supreme Court opinions directory**, official court source. [Directory](https://www.sccourts.org/opinions-orders/opinions/published-opinions/supreme-court/)

#### 2. Court structure as cited

South Carolina has:

- **Supreme Court of South Carolina**
- **South Carolina Court of Appeals**

Both courts’ published decisions use the official reporter `S.C.`. Court level is instead distinguished by the final parenthetical:

- Supreme Court: year alone, such as `(2024)`.
- Court of Appeals: `(Ct. App. 2023)`.

Examples:

- `444 S.C. 224, 233, 906 S.E.2d 588, 593 (2024)`
- `439 S.C. 500, 888 S.E.2d 9 (Ct. App. 2023)`

For unreported decisions, the full court can appear in the filing parenthetical:

- `S.C. Sup. Ct.`
- `S.C. Ct. App.`

There are no appellate district or division identifiers.

#### 3. Reporters in actual use

**Official reporter.** `S.C.` is the official state reporter for both the Supreme Court and Court of Appeals. Because it spans both levels, the intermediate-court parenthetical is essential.

**Regional reporter.** `S.E.2d` is routinely supplied as a parallel. Rule 268’s prescribed examples and the current opinions use:

`official reporter and pin, regional reporter and pin, court/year parenthetical`

For example:

`434 S.C. 39, 45, 862 S.E.2d 259, 262 (2021)`

No cessation of the official reporter or the parallel practice was identified.

**Unreported and memorandum formats.**

- Published-but-not-yet-reported opinions can be identified by `Op. No.` plus court and filing date.
- Unpublished Court of Appeals opinions use identifiers such as `2023-UP-067`.
- Memorandum dispositions may use `MO` identifiers.

Rule 268 states that memorandum and unpublished opinions have no precedential value and limits their citation, subject to the rule’s terms.

**Neutral/public-domain format.** `2023-UP-067` and `2025-MO-031` are opinion-type identifiers, not a universal neutral citation system for all decisions.

**Vendor citations.** Westlaw appears for some unreported authorities, but official and regional reporters dominate the reported South Carolina cases sampled here. No quantitative prevalence rate was established.

#### 4. Verbatim examples

1. **State v. Daniels — Court of Appeals**

   `State v. Daniels, 439 S.C. 500, 888 S.E.2d 9 (Ct. App. 2023)`

   Source: Supreme Court’s *State v. Daniels*.

2. **Marlowe v. South Carolina Department of Transportation — Court of Appeals**

   `Marlowe v. S.C. Dep't of Transp., 441 S.C. 319, 893 S.E.2d 21 (Ct. App. 2023)`

   Source: Supreme Court’s *Marlowe*.

3. **Marlowe — dual-reporter id. short form**

   `id. at 324-28, 893 S.E.2d at 24-26`

   Source: *Marlowe*.

4. **Williams v. Jeffcoat — Supreme Court full parallel**

   `Williams v. Jeffcoat, 444 S.C. 224, 233, 906 S.E.2d 588, 593 (2024)`

   Source: *Marlowe*.

5. **Ray v. City of Rock Hill — Supreme Court**

   `Ray v. City of Rock Hill, 434 S.C. 39, 45, 862 S.E.2d 259, 262 (2021)`

   Source: *Marlowe*.

6. **Hawkins v. City of Greenville — Court of Appeals**

   `Hawkins v. City of Greenville, 358 S.C. 280, 290, 594 S.E.2d 557, 562 (Ct. App. 2004)`

   Source: *Marlowe*.

7. **WRB Limited Partnership v. County of Lexington — Supreme Court, apostrophe in party abbreviation**

   `WRB Ltd. P'ship v. Cnty. of Lexington, 369 S.C. 30, 32, 630 S.E.2d 479, 481 (2006)`

   Source: *Marlowe*.

8. **State v. Pray — unpublished Court of Appeals opinion**

   `State v. Pray, Op. No. 2023-UP-067 (S.C. Ct. App. filed Feb. 22, 2023)`

   Source: Supreme Court memorandum in *State v. Pray*.

9. **State v. Taylor — Supreme Court**

   `State v. Taylor, 436 S.C. 28, 870 S.E.2d 168 (2022)`

   Source: *State v. Pray*.

10. **State v. Lowery — Supreme Court**

    `State v. Lowery, 443 S.C. 473, 905 S.E.2d 361 (2024)`

    Source: *State v. Pray*.

11. **White v. State — Supreme Court**

    `White v. State, 263 S.C. 110, 208 S.E.2d 35 (1974)`

    Source: *Kirk v. State*.

12. **State v. Franks — Court of Appeals**

    `State v. Franks, 432 S.C. 58, 79, 849 S.E.2d 580, 591 (Ct. App. 2020)`

    Source: *State v. Barclay*.

13. **State v. Simmons — Supreme Court**

    `State v. Simmons, 423 S.C. 552, 561, 816 S.E.2d 566, 571 (2018)`

    Source: *State v. Barclay*.

14. **State v. Cheeseboro — Supreme Court**

    `State v. Cheeseboro, 346 S.C. 526, 552 S.E.2d 300 (2001)`

    Source: *State v. Barclay*.

15. **Andrews v. Piedmont Air Lines — Rule 268’s exact Court of Appeals model**

    `Andrews v. Piedmont Air Lines, 297 S.C. 367, 377 S.E.2d 127 (Ct. App. 1989).`

    Source: official Rule 268. The final period is part of the rule’s example.

16. **Satcher v. Berry — Rule 268’s exact unreported Court of Appeals model**

    `Satcher v. Berry, Op. No. 1383 (S.C. Ct. App. filed July 31, 1989)`

    Source: official Rule 268.

17. **Burns v. Burns — Rule 268’s exact memorandum model**

    `Burns v. Burns, Op. No. 89-MO-110 (S.C. Ct. App. filed July 31, 1989)`

    Source: official Rule 268.

#### 5. Style mechanics

**Both reporters can carry pinpoints.** South Carolina parallels often repeat the pin page in each reporter:

`434 S.C. 39, 45, 862 S.E.2d 259, 262 (2021)`

This is the same general double-pin structure seen in North Carolina and West Virginia, rather than Georgia’s parenthesized regional reporter.

**One official reporter spans both appellate levels.** `S.C.` alone does not distinguish Supreme Court from Court of Appeals. The omission or presence of `(Ct. App.)` is therefore load-bearing.

**Short forms can preserve two reporter pinpoints.**

`id. at 324-28, 893 S.E.2d at 24-26`

The short form has no first page but retains both pin ranges. It must inherit its first-page keys from the antecedent citation.

**Opinion-number forms.** Unreported citations can contain both `Op. No.` and a code such as `UP` or `MO`, followed by the full court and filing date. The source uses `filed`, not merely a year.

**Rule versus practice.** Rule 268’s model forms closely match the sampled current opinions. The clearest observed variation is not a rejection of the rule but the use of modern `YYYY-UP-###` identifiers within the same court-and-filing-date framework.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix collision:** **Yes in unreported forms.** `S.C.` is the common state prefix in both `S.C. Sup. Ct.` and `S.C. Ct. App.`. Published Supreme Court citations often avoid an explicit court name, but unpublished and opinion-number forms require longest exact matching.

**(b) District/division-specific intermediate citations:** **No.** The Court of Appeals is cited statewide as `Ct. App.` or `S.C. Ct. App.`.

**(c) Reporter edition spans multiple courts in the state:** **Yes for both important reporters.** `S.C.` and `S.E.2d` each contain decisions from both appellate levels. The Court of Appeals parenthetical is the distinguishing signal.

**(d) Apostrophes or ordinals in court abbreviations:** **No in the core court abbreviations.** Apostrophes occur in party and entity abbreviations—`Dep't`, `P'ship`—and therefore remain relevant to exact-string handling.

**(e) Same case commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** No source established recurring inconsistent attribution of one opinion.

#### 7. Not verified

- A universal neutral/public-domain citation assigned to all South Carolina opinions.
- Quantitative Westlaw or LEXIS prevalence.
- Common inconsistent attribution of a single opinion between the two appellate levels.
- Whether every `UP` or `MO` identifier is globally unique without the accompanying court and year.
- A separate official reporter devoted only to Court of Appeals decisions; the source set instead confirms shared use of `S.C.`.

---

### West Virginia

#### 1. Sources

1. **Dunlap v. Switzer**, Intermediate Court of Appeals, 2025 memorandum decision — exceptionally dense with Supreme Court parallel citations, syllabus-point forms, Westlaw memorandum citations, and intermediate-court parentheticals. [Opinion](https://law.justia.com/cases/west-virginia/intermediate-court-of-appeals/2025/25-ica-105.html)
2. **State v. Browning**, Supreme Court of Appeals, 2025 memorandum decision — full official/regional pinpoints, footnote pins, and short forms. [Opinion](https://law.justia.com/cases/west-virginia/supreme-court/2025/22-705.html)
3. **State v. McKinley**, Supreme Court of Appeals signed opinion, 2014. [Opinion](https://law.justia.com/cases/west-virginia/supreme-court/2014/13-0745.html)
4. **Foster v. PrimeCare Medical of West Virginia, Inc.**, Supreme Court of Appeals signed opinion, 2025 — proves a published Intermediate Court of Appeals citation using `W. Va.`, `S.E.2d`, and `(Ct. App. 2023)`, as well as a memorandum ICA citation. [Opinion](https://law.justia.com/cases/west-virginia/supreme-court/2025/23-726-0.html)
5. **City of Huntington v. AmerisourceBergen Drug Corp.**, Supreme Court of Appeals signed opinion, 2025. [Opinion](https://law.justia.com/cases/west-virginia/supreme-court/2025/24-166.html)
6. **Rules of Appellate Procedure**, including Rule 22’s full-parallel requirement and Rule 21’s memorandum-decision form. [Rules](https://www.courtswv.gov/legal-community/court-rules/rules-appellate-procedure)
7. **Official Intermediate Court of Appeals opinion information**, distinguishing signed/per curiam opinions from memorandum decisions. [Court page](https://www.courtswv.gov/appellate-courts/intermediate-court-of-appeals/opinions/opinion-information)
8. **Official Supreme Court opinion information**, describing publication and memorandum-decision treatment. [Court page](https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/opinions/opinion-information)

#### 2. Court structure as cited

West Virginia’s appellate courts are:

- **Supreme Court of Appeals of West Virginia**
- **Intermediate Court of Appeals of West Virginia**

Published Supreme Court decisions ordinarily use:

`W. Va.` plus `S.E.2d`, followed by the year alone.

Published Intermediate Court of Appeals decisions use the same official `W. Va.` reporter and regional `S.E.2d`, but add:

`(Ct. App. <year>)`

For example:

`247 W. Va. 590, 594, 595, 885 S.E.2d 171, 175, 176 (Ct. App. 2023)`

Memorandum ICA decisions instead commonly appear as:

`No. 23-ICA-353, 2024 WL 1592600, at *5 (W. Va. Ct. App. Feb. 27, 2024) (memorandum decision)`

No appellate districts or divisions are encoded in these forms. `ICA` in the docket identifies the intermediate court, not a geographic district.

#### 3. Reporters in actual use

**Official reporter.** `W. Va.` is the state’s official reporter and now spans both the Supreme Court of Appeals and published Intermediate Court of Appeals decisions. The official court information states that signed and per curiam opinions are published in West Virginia Reports, while memorandum decisions are not.

**Regional reporter.** `S.E.2d` is used as a required parallel under Rule 22. The rule calls for parallel citation to both the West Virginia Reports and the South Eastern Reporter when available.

**Post-publication and memorandum practice.**

- Published opinions: `W. Va.` plus `S.E.2d`.
- Memorandum decisions: docket number, often Westlaw, full court/date parenthetical, and `(memorandum decision)`.
- A memorandum decision may be cited even though it is not published in the bound reporter, subject to the governing rules.

**Neutral/public-domain format.** West Virginia does not use a statewide year-court-sequence neutral identifier for all opinions. ICA docket numbers such as `23-ICA-353` and memorandum citations are not universal neutral case citations.

**Vendor prevalence.** Westlaw is conspicuous in citations to memorandum decisions, particularly ICA decisions. Reported Supreme Court and published ICA cases continue to use official-plus-regional parallels. No numerical prevalence rate was measured.

#### 4. Verbatim examples

1. **Hurley v. Allied Chemical Corp. — Supreme Court**

   `Hurley v. Allied Chemical Corp., 164 W. Va. 268, 262 S.E.2d 757 (1980)`

   Source: *Dunlap v. Switzer*.

2. **State ex rel. McGraw v. Scott Runyan Pontiac-Buick, Inc. — syllabus-point form**

   `Syl. Pt. 2, State ex rel. McGraw v. Scott Runyan Pontiac-Buick, Inc., 194 W. Va. 770, 461 S.E.2d 516 (1995)`

   Source: *Dunlap*.

3. **Chapman v. Kane Transfer Co., Inc. — double-reporter pinpoints**

   `Chapman v. Kane Transfer Co., Inc., 160 W. Va. 530, 538, 236 S.E.2d 207, 212 (1977)`

   Source: *Dunlap*.

4. **Corporation of Harpers Ferry v. Taylor — matching footnote pins**

   `Corp. of Harpers Ferry v. Taylor, 227 W. Va. 501, 506 n.5, 711 S.E.2d 571, 576 n.5 (2011)`

   Source: *Dunlap*.

5. **Bee v. West Virginia Supreme Court of Appeals — Supreme Court memorandum/WL form**

   `Bee v. W.Va. Sup. Ct. of App., No. 121111, 2013 WL 5967045, at *4 (W. Va. Nov. 8, 2013) (memorandum decision)`

   Source: *Dunlap*. Note that the case-name abbreviation uses `W.Va.` without a space, while the court parenthetical uses `W. Va.`.

6. **Bego v. Bego — Supreme Court**

   `Bego v. Bego, 177 W. Va. 74, 76, 350 S.E.2d 701, 703 (1986)`

   Source: *Dunlap*.

7. **State ex rel. Cooper v. Caperton — syllabus point**

   `Syl. Pt. 2, State ex rel. Cooper v. Caperton, 196 W. Va. 208, 470 S.E.2d 162 (1996)`

   Source: *Dunlap*.

8. **State v. Jessie — matching official/regional pinpoints**

   `State v. Jessie, 225 W. Va. 21, 27, 689 S.E.2d 21, 27 (2009)`

   Source: *Dunlap*.

9. **Vogt v. Macy’s, Inc. — ICA memorandum/WL form**

   `Vogt v. Macy’s, Inc., 22-ICA-162, 2023 WL 4027501, at *4 (W. Va. Ct. App. June 15, 2023) (memorandum decision)`

   Source: *Dunlap*.

10. **Megan W. v. Robert R. — ICA memorandum/WL form with `No.`**

    `Megan W. v. Robert R., No. 23-ICA-353, 2024 WL 1592600, at *5 (W. Va. Ct. App. Feb. 27, 2024) (memorandum decision)`

    Source: *Dunlap*.

11. **State v. Dennis — Supreme Court**

    `State v. Dennis, 216 W. Va. 331, 352, 607 S.E.2d 437, 458 (2004)`

    Source: *State v. Browning*.

12. **State v. Knuckles — per curiam parenthetical**

    `State v. Knuckles, 196 W. Va. 416, 424, 473 S.E.2d 131, 139 (1996) (per curiam)`

    Source: *State v. Browning*.

13. **State v. LaRock — matching reporter footnote pins**

    `State v. LaRock, 196 W. Va. 294, 312 n.29, 470 S.E.2d 613, 631 n.29 (1996)`

    Source: *State v. Browning*.

14. **LaRock — Id. short form retaining only the regional reporter**

    `Id., 470 S.E.2d at 631 n.29`

    Source: *State v. Browning*.

15. **Metro Tristate, Inc. v. Public Service Commission — typographic apostrophe in entity abbreviation**

    `Metro Tristate, Inc. v. Pub. Serv. Comm’n, 245 W. Va. 495, 503 n.12, 859 S.E.2d 438, 446 n.12 (2021)`

    Source: *State v. Browning*.

16. **PrimeCare Medical of West Virginia, Inc. v. Foster — published ICA decision**

    `PrimeCare Med. of WV, Inc. v. Foster [PrimeCare I], 247 W. Va. 590, 594, 595, 885 S.E.2d 171, 175, 176 (Ct. App. 2023)`

    Source: Supreme Court’s *Foster v. PrimeCare Medical of West Virginia, Inc.*

17. **PrimeCare II — ICA memorandum/WL form**

    `PrimeCare Med. of WV, Inc. v. Foster [Primecare II], No. 23-ICA-266, 2023 WL 7203395, at *3 (W. Va. Ct. App. Nov. 1, 2023) (memorandum decision)`

    Source: *Foster*. The bracketed label’s capitalization is preserved exactly as it appears in that occurrence.

18. **Duff v. Kanawha County Commission — current Supreme Court parallel**

    `Duff v. Kanawha Cnty. Comm’n, 250 W. Va. 510, 905 S.E.2d 528 (2024)`

    Source: *Foster*.

#### 5. Style mechanics

**Full parallel citation is prescribed.** Rule 22 requires parallel citations to West Virginia Reports and the South Eastern Reporter when available. Current opinions follow that form.

**The official reporter no longer uniquely identifies the court.** Since published ICA decisions also appear in `W. Va.`, the final `(Ct. App. 2023)` signal is essential. This differs from Virginia, Georgia, and North Carolina, whose separate official intermediate reporters encode court level.

**Multiple official and regional pinpoints.** West Virginia often supplies:

`official first page, official pin, regional first page, regional pin`

It can repeat footnote pins in both reporters:

`506 n.5, 711 S.E.2d 571, 576 n.5`

The published ICA example is even more complex, carrying two official pin pages and two regional pin pages.

**Syllabus-point prefixes.** West Virginia uses structurally significant prefixes such as:

- `Syl. Pt. 2,`
- `Syllabus Point 1,`

The syllabus-point number precedes the case citation and is neither a volume nor a court identifier.

**Memorandum decisions.** Actual memorandum citations vary as to whether `No.` precedes the docket:

- `22-ICA-162, 2023 WL ...`
- `No. 23-ICA-353, 2024 WL ...`

Both end with the explicit court/date and `(memorandum decision)`. Rule 21 supplies the governing memorandum framework.

**Mixed spacing in the state abbreviation.** The source contains `W.Va.` in an abbreviated party name and `W. Va.` in reporter and court-parenthetical positions. That distinction should not be silently assumed away at extraction time.

**Short forms may select one parallel.** `Id., 470 S.E.2d at 631 n.29` refers back to a full dual-reporter citation but retains only the regional reporter in the short form.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix collision:** **Yes.** Explicit forms such as `(W. Va.)`, `W.Va. Supreme Court`, and `(W. Va. Ct. App.)` share the state prefix. Published Supreme citations often use only a year, but memorandum/vendor forms require recognition of the longer intermediate-court signal.

**(b) District/division-specific intermediate citations:** **No.** `ICA` identifies the statewide Intermediate Court of Appeals, not a geographic district.

**(c) Reporter edition spans multiple courts in the state:** **Yes for both `W. Va.` and `S.E.2d`.** Published decisions from the Supreme Court and ICA can appear in both. The `(Ct. App.)` parenthetical is therefore load-bearing for published ICA cases.

**(d) Apostrophes or ordinals in court abbreviations:** **No in the core court abbreviations.** Typographic apostrophes occur in party and entity strings—`Macy’s`, `Comm’n`—and can sit inside the citation span. Docket numbers contain digits but not court ordinals.

**(e) Same case commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** The *PrimeCare* litigation produces multiple ICA decisions and a later Supreme Court decision, but those are distinct opinions with separate citations, not inconsistent attribution of one opinion.

#### 7. Not verified

- A West Virginia universal/public-domain citation system.
- Quantitative Westlaw or LEXIS prevalence.
- Common inconsistent Supreme-versus-ICA attribution of one identical opinion.
- Whether every published ICA opinion receives both bound `W. Va.` and `S.E.2d` citations at the same time.
- A primary-source example of a published ICA citation without `(Ct. App.)`; none appeared, and omission would be structurally ambiguous.
- Whether `No.` omission before ICA docket numbers is an approved alternative or merely variable authoring practice. Both forms appear in the cited born-digital opinion.


---

## Batch 4 — So. 3d family

**States covered:** Alabama, Mississippi, and Louisiana.

The examples below come from searchable, born-digital appellate opinions and current court rules. Reporter scans and OCR-derived texts were excluded.

---

### Alabama

#### 1. Sources

1. **Billy Ray Morris v. Lazzari**, Alabama Court of Civil Appeals, 2025 — particularly useful for Supreme Court and Civil Appeals citations, historical parallel reporters, pending-publication forms, and named short forms. [Opinion](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html)
2. **W.D.G. v. K.S.G.**, Alabama Court of Civil Appeals, 2025 — useful for pending-publication citations, historical `Ala. App.` parallels, and an actual Supreme-versus-intermediate attribution inconsistency. [Opinion](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0072.html)
3. **State v. M.D.D.**, Alabama Court of Criminal Appeals, 2025 — dense with Criminal Appeals citations, table dispositions, footnote pinpoints, and blank-reporter forms. [Opinion](https://law.justia.com/cases/alabama/court-of-appeals-criminal/2025/cr-2023-0303.html)
4. **Stanley v. Ivey**, Alabama Court of Civil Appeals, 2025 — contains authorities from all three appellate courts, including pending-publication Criminal Appeals citations. [Opinion](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0276.html)
5. **Alabama Supreme Court decisions archive**, the state judiciary’s current slip-opinion source. [Archive](https://judicial.alabama.gov/Decision/SupremeCourtDecisions)
6. **Alabama Court of Civil Appeals decisions archive.** [Archive](https://judicial.alabama.gov/decision/civildecisions)
7. **Alabama Court of Criminal Appeals decisions archive.** [Archive](https://judicial.alabama.gov/decision/criminaldecisions)
8. **Alabama Rule of Appellate Procedure 28**, governing briefs and citation form. [Rule 28 PDF](https://judicial.alabama.gov/docs/library/rules/ap28.pdf)
9. **Alabama Rule of Appellate Procedure 53**, governing publication and no-opinion dispositions of the Supreme Court. [Rule 53 PDF](https://judicial.alabama.gov/docs/library/rules/ap53.pdf)
10. **Alabama Rule of Appellate Procedure 54**, governing Court of Civil Appeals and Court of Criminal Appeals memorandum or no-opinion dispositions. [Rule 54 PDF](https://judicial.alabama.gov/docs/library/rules/ap54.pdf)

#### 2. Court structure as cited

Alabama has three appellate courts relevant to ordinary state case citations:

- **Supreme Court of Alabama:** `(Ala.)`
- **Alabama Court of Civil Appeals:** `(Ala. Civ. App.)`
- **Alabama Court of Criminal Appeals:** `(Ala. Crim. App.)`

Current reported citations ordinarily place the court and year after the Southern Reporter citation:

- `34 So. 3d 1238, 1241 (Ala. 2009)`
- `333 So. 3d 149, 151 (Ala. Civ. App. 2021)`
- `322 So. 3d 979, 1025 (Ala. Crim. App. 2019)`

Neither intermediate court uses district or division identifiers in its citation parenthetical. The distinction between the two intermediate courts is functional—civil versus criminal—rather than geographic.

Pending-publication citations use the same court abbreviations after a docket-and-date component, for example:

`[Ms. CR-20220651, June 23, 2023] ___ So. 3d ___, ___ (Ala. Crim. App. 2023)`

The `Ms.` docket is not a neutral-citation sequence and should not be treated as a reporter edition.

#### 3. Reporters in actual use

**Current official publication.** Alabama’s judiciary states that slip opinions remain subject to correction and that, once published in West’s Southern Reporter, they are reprinted in the **Alabama Reporter**, described by the court as the official report of Alabama appellate decisions. Current opinions therefore use `So. 2d` and `So. 3d` as the operative reported citation.

**Historical official reporters.**

- `Ala.` — historical Alabama Supreme Court reporter.
- `Ala. App.` — historical appellate reporter.

Born-digital current opinions still cite historical decisions with official-and-regional parallels, including:

`267 So. 2d 405, 410, 289 Ala. 328, 334 (1972)`

and:

`52 Ala. App. 234, 236, 291 So. 2d 322, 324 (Civ. 1974)`

A secondary legal-research guide places cessation of the separate Alabama Reports and Alabama Appellate Reports in **1976**, but I did not locate a primary Alabama court rule fixing the exact final-volume or cessation date. The 1976 date should therefore be treated as externally documented rather than primary-source-proven for this project.

**Regional reporters.** `So. 2d` and `So. 3d` span all three Alabama appellate courts. The reporter alone cannot distinguish Supreme Court, Civil Appeals, or Criminal Appeals.

**Pending-publication form.** Before assignment of Southern Reporter pages, Alabama opinions cite:

`[Ms. <docket>, <full date>] ___ So. 3d ___ (<court> <year>)`

An interior pinpoint can appear as a second blank:

`___ So. 3d ___, ___`

This form has no resolvable reporter first page and must not be filled from inference.

**Neutral/public-domain format.** I found no Alabama universal identifier comparable to `2021-NCSC-165` or an Ohio webcite. The docket-and-date `Ms.` form is a pending-publication citation, not a permanent neutral identifier.

**Westlaw and LEXIS.** Vendor citations appear for unpublished or otherwise unreported decisions, but the sampled current published opinions predominantly use Southern Reporter citations or the blank `___ So. 3d ___` pending-publication form. No quantitative prevalence rate was established.

#### 4. Verbatim examples

1. **Nationwide Mutual Fire Insurance Co. v. Austin — Supreme Court**

   `Nationwide Mut. Fire Ins. Co. v. Austin, 34 So. 3d 1238, 1241 (Ala. 2009)`

   Source: [Billy Ray Morris v. Lazzari](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html).

2. **1st Franklin Financial Corp. v. Pettway — Court of Civil Appeals**

   `1st Franklin Fin. Corp. v. Pettway, 333 So. 3d 149, 151 (Ala. Civ. App. 2021)`

   Source: [Billy Ray Morris v. Lazzari](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html).

3. **Alabama Department of Labor v. Wiggins — Court of Civil Appeals; apostrophe preserved**

   `Alabama Dep't of Labor v. Wiggins, 168 So. 3d 84, 87 (Ala. Civ. App. 2014)`

   Source: [Billy Ray Morris v. Lazzari](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html).

4. **Hilb, Rogal & Hamilton Co. v. Beiersdoerfer — Supreme Court**

   `Hilb, Rogal & Hamilton Co. v. Beiersdoerfer, 989 So. 2d 1045, 1055 (Ala. 2007)`

   Source: [Billy Ray Morris v. Lazzari](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html).

5. **Johnson v. Fishbein — historical regional and official parallel**

   `Johnson v. Fishbein, 267 So. 2d 405, 410, 289 Ala. 328, 334 (1972)`

   Source: [Billy Ray Morris v. Lazzari](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html).

6. **Satterfield v. Winston Industries, Inc. — full citation**

   `Satterfield v. Winston Industries, Inc., 553 So. 2d 61, 63 (Ala. 1989)`

   Source: [Billy Ray Morris v. Lazzari](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html).

7. **Satterfield — named short form**

   `Satterfield, 553 So. 2d at 63`

   Source: [Billy Ray Morris v. Lazzari](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0116.html).

8. **W.D.G. v. K.S.G. — pending-publication form attributed to Alabama Supreme Court**

   `W.D.G. v. K.S.G., [Ms. CL-2024-0223, Nov. 15, 2024] ___ So. 3d ___ (Ala. 2024)`

   Source: [W.D.G. v. K.S.G.](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0072.html).

9. **The same W.D.G. decision — later attributed to the Court of Civil Appeals**

   `W.D.G. v. K.S.G., [Ms. CL2024-0223, Nov. 15, 2024] ___ So. 3d ___ (Ala. Civ. App. 2024)`

   Source: [W.D.G. v. K.S.G.](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0072.html). The missing hyphen after `CL` is preserved exactly from this occurrence.

10. **Stover v. Stover — Court of Civil Appeals**

    `Stover v. Stover, 176 So. 3d 854, 863 (Ala. Civ. App. 2015)`

    Source: [W.D.G. v. K.S.G.](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0072.html).

11. **Phillips v. Phillips — historical `Ala. App.` and regional parallel**

    `Phillips v. Phillips, 52 Ala. App. 234, 236, 291 So. 2d 322, 324 (Civ. 1974)`

    Source: [W.D.G. v. K.S.G.](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0072.html).

12. **M.D.D. v. State — table disposition**

    `M.D.D. v. State, 152 So. 3d 456 (Ala. Crim. App. 2012) (table)`

    Source: [State v. M.D.D.](https://law.justia.com/cases/alabama/court-of-appeals-criminal/2025/cr-2023-0303.html).

13. **State v. M.D.D. — Court of Criminal Appeals**

    `State v. M.D.D., 324 So. 3d 425 (Ala. Crim. App. 2020)`

    Source: [State v. M.D.D.](https://law.justia.com/cases/alabama/court-of-appeals-criminal/2025/cr-2023-0303.html).

14. **State v. M.D.D. — named short form**

    `State v. M.D.D., 324 So. 3d at 427`

    Source: [State v. M.D.D.](https://law.justia.com/cases/alabama/court-of-appeals-criminal/2025/cr-2023-0303.html).

15. **Jones v. State — Court of Criminal Appeals**

    `Jones v. State, 322 So. 3d 979, 1025 (Ala. Crim. App. 2019)`

    Source: [State v. M.D.D.](https://law.justia.com/cases/alabama/court-of-appeals-criminal/2025/cr-2023-0303.html).

16. **T.C.S. v. State — footnote pinpoint**

    `T.C.S. v. State, 386 So. 3d 857, 860 n.2 (Ala. Crim. App. 2023)`

    Source: [State v. M.D.D.](https://law.justia.com/cases/alabama/court-of-appeals-criminal/2025/cr-2023-0303.html).

17. **C.L.A. v. State — pending publication with blank first page and blank pin**

    `C.L.A. v. State, [Ms. CR-20220651, June 23, 2023] ___ So. 3d ___, ___ (Ala. Crim. App. 2023)`

    Source: [State v. M.D.D.](https://law.justia.com/cases/alabama/court-of-appeals-criminal/2025/cr-2023-0303.html).

18. **Alabama Department of Corrections v. Booth — later pending-publication form**

    `Alabama Dep't of Corr. v. Booth, [Ms. CR-2023-0426, Nov. 7, 2025] ___ So. 3d ___, ___ (Ala. Crim. App. 2025)`

    Source: [Stanley v. Ivey](https://law.justia.com/cases/alabama/court-of-appeals-civil/2025/cl-2025-0276.html).

#### 5. Style mechanics

**Rule 28 permits multiple accepted style authorities.** Alabama appellate briefs may use the latest Bluebook, the ALWD guide, or the style and form used in Alabama Supreme Court opinions. Rule 28 also requires a pinpoint page where the proposition appears rather than merely the case’s first page. This produces some legitimate variation rather than one perfectly closed punctuation grammar.

**Current reported form is regional-reporter-centered.** The dominant form is:

`<case>, <volume> So. 3d <first page>, <pin> (<court> <year>)`

The court parenthetical is necessary because the reporter is shared by all three appellate courts.

**Pending-publication strings are structurally significant.** The `Ms.` component precedes a blank reporter:

`[Ms. <docket>, <date>] ___ So. 3d ___`

This can contain a second blank for the pin page. Such a citation has no first-page canonical key until publication; the blanks must not be “repaired” from surrounding text.

**Historical parallels vary in ordering.** The sources contain both:

- Regional reporter followed by official reporter: `267 So. 2d 405, 410, 289 Ala. 328, 334`
- Official appellate reporter followed by regional reporter: `52 Ala. App. 234, 236, 291 So. 2d 322, 324`

**Historical intermediate parentheticals can be compressed.** `(Civ. 1974)` appears instead of the modern `(Ala. Civ. App. 1974)`. This is an older court signal, not merely an explanatory parenthetical.

**Short forms.** Alabama opinions use ordinary named short forms such as:

`Satterfield, 553 So. 2d at 63`

and can retain only the regional volume and reporter.

**No-opinion and memorandum treatment.** Rules 53 and 54 distinguish published opinions from no-opinion or memorandum dispositions. The latter may be omitted from the official reports and may carry restrictions on precedential use, which explains table and nonstandard citation forms.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `(Ala.)` shares the complete state prefix with both `(Ala. Civ. App.)` and `(Ala. Crim. App.)`. A matcher that accepts the first readable state abbreviation rather than the longest exact court string can misroute both intermediate courts to the Supreme Court.

**(b) Intermediate-court citations are district/division-specific:** **No.** Alabama uses two statewide subject-matter intermediate courts. No geographic district or division token appeared.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `So. 2d` and `So. 3d` span the Supreme Court, Court of Civil Appeals, and Court of Criminal Appeals. Historical `Ala. App.` also did not by itself encode the modern civil-versus-criminal distinction in every era.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in the core court abbreviations.** `Ala.`, `Ala. Civ. App.`, and `Ala. Crim. App.` contain neither. Apostrophes do occur inside the citation span in entity names such as `Dep't`.

**(e) The same case is cited under Supreme-versus-intermediate attribution inconsistently:** **Yes, concretely demonstrated.** The same *W.D.G. v. K.S.G.* docket is cited once with `(Ala. 2024)` and later with `(Ala. Civ. App. 2024)` in one born-digital Court of Civil Appeals opinion. The docket typography also varies by one hyphen. This proves the failure class exists in real Alabama text, though it does not establish its statewide frequency.

#### 7. Not verified

- The exact final volume and primary-source cessation date for the separate `Ala.` and `Ala. App.` reporters. A secondary source gives 1976, but the reviewed Alabama rules and court archives did not state the date directly.
- A permanent Alabama neutral or public-domain case identifier.
- Quantitative Westlaw or LEXIS prevalence.
- Whether the erroneous `(Ala. 2024)` attribution for *W.D.G.* originated in the filed opinion, a later editorial layer, or the archive’s text conversion.
- Whether historical `(Civ. <year>)` and any corresponding criminal shorthand remain accepted in current briefs.
- Whether every `Ms.` citation is updated consistently after Southern Reporter pagination becomes available.

---

### Mississippi

#### 1. Sources

1. **Gavin v. Evers**, Supreme Court of Mississippi, 2025 — dense with current Supreme Court citations and paragraph pinpoints; also supplies an actual `-SCT` opinion identifier. [Opinion](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-ec-00061-sct.html)
2. **Sardin v. State**, Supreme Court of Mississippi, 2025 — current criminal Supreme Court citation practice. [Opinion](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-ka-00319-sct.html)
3. **Mississippi Methodist Hospital & Rehabilitation Center, Inc. v. Mississippi Division of Medicaid**, Supreme Court, 2025 — especially valuable for paired Court of Appeals and Supreme Court decisions in the same litigation. [Opinion](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-sa-01113-sct.html)
4. **James Luster v. State**, Mississippi Court of Appeals, 2025 — paragraph pinpoints, named short forms, and `Id.` practice. [Opinion](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ca-00014-coa.html)
5. **Roberts v. State**, Mississippi Court of Appeals, 2025 — intermediate and Supreme Court authorities, nested quotations, and paragraph pinpoints. [Opinion](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ka-00358-coa.html)
6. **McLaurin v. State**, Mississippi Court of Appeals, 2025 — dense modern citation practice from both appellate courts. [Opinion](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ka-00138-coa.html)
7. **Mississippi Code § 9-3-43**, authorizing official status for privately published volumes. [Statute](https://law.justia.com/codes/mississippi/title-9/chapter-3/general-provisions/section-9-3-43/)
8. **Mississippi Rule of Appellate Procedure 28**, including the Southern Reporter requirement, pre-1967 parallel requirement, and paragraph-number/public-domain provisions. [Rule history and text](https://law.justia.com/cases/mississippi/supreme-court/1997/conv4375.html)
9. **Mississippi Commission on Judicial Performance’s official-reports description**, confirming West’s Southern Reporter and Mississippi Edition as official reports by designation of the Supreme Court. [Official page](https://www.judicialperformance.ms.gov/reported-commission-cases)

#### 2. Court structure as cited

Mississippi has:

- **Supreme Court of Mississippi:** `(Miss.)`
- **Mississippi Court of Appeals:** `(Miss. Ct. App.)`

The Court of Appeals is cited as a single statewide court; citations do not contain district or division identifiers.

The court distinction is normally carried by the parenthetical because both courts publish in the same Southern Reporter series:

- `307 So. 3d 427, 432 (¶ 15) (Miss. 2020)`
- `102 So. 3d 1209, 1214 (¶13) (Miss. Ct. App. 2012)`

Mississippi also uses docket-based public-domain identifiers whose suffix identifies the court:

- `-SCT` — Supreme Court.
- `-COA` — Court of Appeals.

Actual current headers include:

- `2024-EC-00061-SCT`
- `2024-CA-00014-COA`

The middle classification token varies with the proceeding, including forms such as `EC`, `KA`, `CA`, `SA`, and `IA`.

#### 3. Reporters in actual use

**Official status of Southern Reporter.** Mississippi law authorizes the Supreme Court to declare privately published volumes to be the official reports, and current state materials identify West’s Southern Reporter and its Mississippi Edition as the designated official reports.

**Historical Mississippi Reports.** Rule 28 requires:

- All Mississippi cases to be cited to the Southern Reporter.
- Cases decided before **1967** also to be cited to the Mississippi Reports.

Thus the operative transition is July 1, 1966/1967-era official adoption: post-transition filings cite Southern Reporter; pre-1967 cases retain an official `Miss.` parallel under the rule.

**Current regional editions.** Current cases use `So. 3d`; older cases use `So. 2d`. Both editions span the Supreme Court and Court of Appeals, so the court parenthetical or public-domain suffix is necessary.

**Public-domain citation.** Effective **July 1, 1997**, published Mississippi opinions began receiving paragraph numbers, and Rule 28 permits citation by the clerk-assigned case number together with paragraph and court/year. The rule’s model uses a form such as:

`95-KA-01234-SCT (¶1) (Miss. 1997)`

Current opinion headers continue the expanded year-classification-number-court pattern, for example `2024-KA-00319-SCT`.

**Paragraph pinpoints.** A common full citation is:

`<volume> So. 3d <first page>, <pin> (¶<paragraph>) (<court> <year>)`

Spacing around the paragraph number is inconsistent in real opinions: both `(¶ 10)` and `(¶13)` occur.

**Westlaw and LEXIS.** Vendor identifiers occur for decisions not yet available in the official reporter and for unpublished material, but the selected reported opinions overwhelmingly use `So. 3d`. No quantitative rate was verified.

#### 4. Verbatim examples

1. **Huff-Cook, Inc. v. Dale — Supreme Court; spaced paragraph number**

   `Huff-Cook, Inc. v. Dale, 913 So. 2d 988, 990 (¶ 10) (Miss. 2005)`

   Source: [Gavin v. Evers](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-ec-00061-sct.html).

2. **Ground Control, LLC v. Capsco Industries, Inc. — Supreme Court**

   `Ground Control, LLC v. Capsco Indus., Inc., 120 So. 3d 365, 372 (¶ 16) (Miss. 2013)`

   Source: [Gavin v. Evers](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-ec-00061-sct.html).

3. **City of Jackson v. Jones — Supreme Court**

   `City of Jackson v. Jones, 393 So. 3d 1002, 1004 (¶ 7) (Miss. 2024)`

   Source: [Gavin v. Evers](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-ec-00061-sct.html).

4. **Self v. Mitchell — Supreme Court**

   `Self v. Mitchell, 327 So. 3d 93, 96 (¶ 11) (Miss. 2021)`

   Source: [Gavin v. Evers](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-ec-00061-sct.html).

5. **Gavin v. Evers — actual public-domain header identifier**

   `2024-EC-00061-SCT`

   Source: opinion header in [Gavin v. Evers](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-ec-00061-sct.html).

6. **City of Cleveland v. Mid-South Associates, LLC — Court of Appeals decision followed by Supreme Court decision**

   `City of Cleveland v. Mid-South Associates, LLC, 94 So. 3d 1137, 1139-40 (Miss. Ct. App. 2011), vacated on other grounds by City of Cleveland v. Mid-South Associates, LLC, 94 So. 3d 1049, 1051 (Miss. 2012)`

   Source: [Mississippi Methodist Hospital & Rehabilitation Center, Inc. v. Mississippi Division of Medicaid](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-sa-01113-sct.html).

7. **Latham v. Latham — Supreme Court**

   `Latham v. Latham, 261 So. 3d 1110, 1115 (Miss. 2019)`

   Source: [Mississippi Methodist Hospital](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-sa-01113-sct.html).

8. **Hatfield v. Deer Haven Homeowners Association, Inc. — typographic apostrophe**

   `Hatfield v. Deer Haven Homeowners Ass’n, Inc., 234 So. 3d 1269, 1277 (Miss. 2017)`

   Source: [Mississippi Methodist Hospital](https://law.justia.com/cases/mississippi/supreme-court/2025/2024-sa-01113-sct.html).

9. **James Luster v. State — actual Court of Appeals public-domain header**

   `2024-CA-00014-COA`

   Source: opinion header in [James Luster v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ca-00014-coa.html).

10. **Luster v. State — Court of Appeals**

    `Luster v. State, 143 So. 3d 636 (Miss. Ct. App. 2014).`

    Source: [James Luster v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ca-00014-coa.html). The source’s final period is preserved.

11. **Esco v. State — Court of Appeals; unspaced paragraph number**

    `Esco v. State, 102 So. 3d 1209, 1214 (¶13) (Miss. Ct. App. 2012)`

    Source: [James Luster v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ca-00014-coa.html).

12. **Esco — named short form**

    `Esco, 102 So. 3d at 1214 (¶13)`

    Source: [James Luster v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ca-00014-coa.html).

13. **Corrothers v. State — Supreme Court**

    `Corrothers v. State, 404 So. 3d 112, 118 (¶22) (Miss. 2024)`

    Source: [James Luster v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ca-00014-coa.html).

14. **Id. short form with paragraph**

    `Id. at 118 (¶19)`

    Source: [James Luster v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ca-00014-coa.html).

15. **Horn v. State — Court of Appeals**

    `Horn v. State, 273 So. 3d 759, 766 (¶24) (Miss. Ct. App. 2018)`

    Source: [Roberts v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ka-00358-coa.html).

16. **Bell — short form with nested quotation and differing antecedent reporter**

    `Bell, 287 So. 3d at 954 (¶18) (quoting Lee, 944 So. 2d at 40 (¶16)).`

    Source: [Roberts v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ka-00358-coa.html).

17. **Dewberry v. State — Court of Appeals**

    `Dewberry v. State, 407 So. 3d 269, 278 (¶37) (Miss. Ct. App. 2025)`

    Source: [McLaurin v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ka-00138-coa.html).

18. **Little — named short form**

    `Little, 233 So. 3d at 292 (¶20)`

    Source: [McLaurin v. State](https://law.justia.com/cases/mississippi/court-of-appeals/2025/2024-ka-00138-coa.html).

#### 5. Style mechanics

**Reporter citation plus paragraph pinpoint.** Mississippi’s characteristic modern form places the reporter page pinpoint before a parenthetical paragraph number:

`404 So. 3d 112, 118 (¶22) (Miss. 2024)`

The paragraph is an additional structural pinpoint, not the case’s first page.

**Spacing is not uniform.** Real opinions contain:

- `(¶ 10)`
- `(¶13)`

The whitespace difference is therefore genuine input variation, not safely rejectable noise.

**Public-domain identifier.** Since July 1, 1997, opinions receive paragraph numbering and may be cited through a clerk-assigned identifier. Current headers use a more explicit form than the rule’s older example:

`2024-CA-00014-COA`

The suffix supplies a direct court signal even when a reporter citation is absent.

**Historical parallels.** Rule 28 requires a Mississippi Reports parallel for pre-1967 decisions. The current born-digital source set did not contain a clean, full pre-1967 `Miss.`/Southern Reporter run suitable for copying as a new vector; the rule nevertheless confirms the required structure.

**Short forms retain paragraph numbers.** Both named short forms and `Id.` can append the antecedent opinion’s paragraph:

- `Esco, 102 So. 3d at 1214 (¶13)`
- `Id. at 118 (¶19)`

**Subsequent history can contain two Mississippi court levels and two different first pages.** The *City of Cleveland* string cites a Court of Appeals opinion and a later Supreme Court opinion under the same case name. These are separate decisions, not parallel citations to one opinion.

**Rule-based citation hierarchy.** Mississippi differs from Alabama because Rule 28 specifically requires Southern Reporter citation for Mississippi cases and prescribes the historical `Miss.` parallel, rather than broadly allowing any of several independent style manuals.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `(Miss.)` shares the state prefix with `(Miss. Ct. App.)`. Longest exact matching is required for regional-only citations.

**(b) Intermediate-court citations are district/division-specific:** **No.** The Court of Appeals is cited statewide. The `-COA` suffix identifies the court, not a district.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `So. 2d` and `So. 3d` contain both Supreme Court and Court of Appeals decisions. The reporter cannot supply court level independently.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in the court tokens.** `Miss.` and `Miss. Ct. App.` contain neither. Typographic apostrophes appear in party and agency names such as `Ass’n` and `Dep’t`.

**(e) The same case is commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not shown as an attribution error.** The *City of Cleveland* example demonstrates the same caption at both levels, but the string accurately distinguishes a Court of Appeals decision from a later Supreme Court decision after vacatur. This is a same-caption/multiple-opinion hazard, not proof of inconsistent court attribution.

#### 7. Not verified

- A born-digital current-opinion example of the full pre-1967 `Miss.` plus Southern Reporter parallel required by Rule 28.
- Quantitative Westlaw or LEXIS prevalence.
- A single statewide rule fixing whether a space must appear after `¶`; actual opinions use both forms.
- Common erroneous Supreme-versus-Court-of-Appeals attribution of one identical opinion.
- Whether every docket classification token—`EC`, `KA`, `CA`, `SA`, `IA`, and others—has a stable machine-readable subject meaning across all historical years.
- Whether public-domain docket citations without any reporter parallel are common in filed briefs, as opposed to being permitted by Rule 28 and displayed in opinion headers.

---

### Louisiana

#### 1. Sources

1. **State v. Michael Deon Riley**, Louisiana Second Circuit Court of Appeal, 2025 — dense with Second Circuit public-domain citations, writ history, pending-reporter blanks, Westlaw citations, and `supra`. [Opinion](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html)
2. **State v. Torail Thomas**, Louisiana Second Circuit Court of Appeal, 2025 — includes Louisiana Supreme Court public-domain and regional citations. [Opinion](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-373-ka.html)
3. **State v. Ruffins**, Louisiana Second Circuit Court of Appeal, 2025 — useful for a recent Supreme Court decision still carrying blank Southern Reporter pages and a Westlaw parallel. [Opinion](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/55-952-ka.html)
4. **Cunningham v. Borden Dairy**, Louisiana First Circuit Court of Appeal, 2024 — proves actual `La. App. 1st Cir.` ordinal usage. [Opinion](https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2024/2024ca0105.html)
5. **Bias v. Foster**, Louisiana First Circuit Court of Appeal, 2024 — shows the alternate `La. App. 1 Cir.` form. [Opinion](https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2024/2024ca0776.html)
6. **Henry Pete v. Boland Marine**, Louisiana Fourth Circuit Court of Appeal, 2023 — dense with Supreme Court, Third Circuit, and Fourth Circuit citations and `p.` pinpoints. [Opinion](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2023/2021-ca-0626.html)
7. **State v. Theophile**, Louisiana Fourth Circuit Court of Appeal, 2024 — provides public-domain short forms and another Fourth Circuit example. [Opinion](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2024/2024-k-0019.html)
8. **Rosetta Nelson v. Teachers’ Retirement System of Louisiana**, Louisiana First Circuit Court of Appeal, 2011 — contains clean Fifth Circuit citations and writ history. [Opinion](https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2011/2010ca1190-1.html)
9. **Louisiana Supreme Court Rule VIII, Part G, § 8**, “Citation of Louisiana Appellate Decisions.” [Official rule page](https://www.lasc.org/Supreme_Court_Rules?p=PartGSection8) and [court rules index](https://www.lasc.org/rules/supreme/RuleVIII.asp)
10. **Rule VIII, Part G, § 8 text and examples**, including adoption dates and treatment of Louisiana Reports. [Rule reproduction](https://www.law.cornell.edu/citation/sample_louisiana)

#### 2. Court structure as cited

Louisiana has:

- **Louisiana Supreme Court:** `(La.)`
- **Louisiana First Circuit Court of Appeal:** `(La. App. 1 Cir.)`, with actual opinions also using `(La. App. 1st Cir.)`
- **Louisiana Second Circuit Court of Appeal:** `(La. App. 2 Cir.)`
- **Louisiana Third Circuit Court of Appeal:** `(La. App. 3 Cir.)`
- **Louisiana Fourth Circuit Court of Appeal:** `(La. App. 4 Cir.)`
- **Louisiana Fifth Circuit Court of Appeal:** `(La. App. 5 Cir.)`

The numbered circuit is a substantive court identifier. A Louisiana Court of Appeal citation without the circuit is incomplete for court-mapping purposes.

The Supreme Court’s rule uses cardinal numerals—`1 Cir.`, `2 Cir.`—but born-digital First Circuit opinions also contain the ordinal `1st Cir.`. Both forms are therefore real-world citation strings.

Louisiana public-domain citations normally place the docket number before the court and full decision date:

`45,627 (La. App. 2 Cir. 1/26/11)`

The letters attached to the court’s docket, such as `-KA` or `-CA`, are commonly omitted from the citation itself under the Supreme Court rule. Thus an opinion headed `56,131-KA` can cite other criminal cases simply as `55,491`.

#### 3. Reporters in actual use

**Louisiana Reports.** The Louisiana Supreme Court’s citation rule states that the official **Louisiana Reports** were discontinued in **1972**. Pre-1972 Supreme Court decisions can therefore retain a `La.` official parallel along with the Southern Reporter.

**Historical Courts of Appeal reporters.** The rule identifies historical official Court of Appeal reporters for pre-1928 decisions; from 1928 through 1993 the ordinary form is the Southern Reporter citation with court and year.

**Regional reporter.** Modern Louisiana appellate decisions use `So. 2d` and `So. 3d`. The reporter spans the Supreme Court and all five Courts of Appeal, so the parenthetical court signal is indispensable.

**Public-domain citation adoption.** For decisions issued after **December 31, 1993**, Rule VIII, Part G, § 8 prescribes a Louisiana public-domain citation consisting of:

- Case name.
- Docket number without letter designation.
- Court abbreviation.
- Full decision date.
- `p.` pinpoint where needed.
- Southern Reporter parallel when available.

The format became mandatory in briefs and other court filings after **July 1, 1994**.

A complete modern citation can therefore contain two independently meaningful location systems:

`2008-0309, p. 4 (La. 4/4/08), 979 So.2d 456, 458`

**Pending publication and vendor citations.** Current opinions use blanks where Southern Reporter pagination has not yet been assigned:

`____ So. 3d ____`

or:

`___ So. 3d ___`

A Westlaw citation may follow the blanks. These components must remain vendor or unresolved-reporter forms; no first page can be reconstructed.

**Spacing variation.** Both `So.3d` and `So. 3d` occur in actual opinions.

#### 4. Verbatim examples

1. **State v. Jyles — Louisiana Supreme Court**

   `State v. Jyles, 96-2669 (La. 12/12/97), 704 So. 2d 241`

   Source: [State v. Torail Thomas](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-373-ka.html).

2. **State v. Bishop — Louisiana Supreme Court**

   `State v. Bishop, 01-2548 (La. 1/14/03), 835 So. 2d 434`

   Source: [State v. Michael Deon Riley](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html).

3. **State v. Ruffins — pending Supreme Court reporter pages plus Westlaw**

   `State v. Ruffins, 24-01512 (La. 6/25/25), ___ So. 3d ___, 2025 WL 17878821`

   Source: [State v. Ruffins](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/55-952-ka.html).

4. **State v. Ramsey — Second Circuit plus Supreme Court writ history**

   `State v. Ramsey, 55,491 (La. App. 2 Cir. 2/28/24), 381 So. 3d 308, writ denied, 2400379 (La. 10/1/24), 393 So. 3d 865.`

   Source: [State v. Michael Deon Riley](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html). The writ docket `2400379` is preserved as printed in the source.

5. **State v. Palmer — Second Circuit and writ history**

   `State v. Palmer, 45,627 (La. App. 2 Cir. 1/26/11), 57 So. 3d 1099, writ denied, 11-0412 (La. 9/2/11), 68 So. 3d 526.`

   Source: [State v. Michael Deon Riley](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html).

6. **State v. Warren — Second Circuit with blank reporter and Westlaw fallback**

   `State v. Warren, 56,041 (La. App. 2 Cir. 12/18/24), ____ So. 3d ____, 2024 WL 5149817`

   Source: [State v. Michael Deon Riley](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html). The four-underscore groups are preserved exactly.

7. **State v. Langston — Second Circuit and writ history**

   `State v. Langston, 43,923 (La. App. 2 Cir. 2/25/09), 3 So. 3d 707, writ denied, 09-0696 (La. 12/11/09), 23 So. 3d 912.`

   Source: [State v. Michael Deon Riley](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html).

8. **Ramsey — supra short form**

   `Ramsey, supra;`

   Source: [State v. Michael Deon Riley](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html).

9. **Bias v. Haley — First Circuit cardinal form**

   `Bias v. Haley, 2023- 0281 ( La. App. 1 Cir. 11/ 3/ 23), 383 So. 3d 175, 181.`

   Source: [Bias v. Foster](https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2024/2024ca0776.html). Spaces after hyphens, parentheses, and slashes are retained from the linked source’s extracted text.

10. **Lafayette Steel Erector, Inc. v. G. Kendrick LLC — First Circuit ordinal form**

    `Lafayette Steel Erector, Inc. v. G. Kendrick LLC, 2022- 0892 ( La. App. 1st Cir. 8/ 29/ 23), 375 So. 3d 464, 474, writ denied, 2023- 01316 ( La. 12/ 19/ 23), 375 So. 3d 414.`

    Source: [Cunningham v. Borden Dairy](https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2024/2024ca0105.html). Source-extraction spacing is preserved exactly.

11. **Venissat v. St. Paul Fire & Marine Insurance Co. — Third Circuit**

    `Venissat v. St. Paul Fire & Marine Ins. Co., 2006-987, p. 17 (La. App. 3 Cir. 8/15/07), 968 So. 2d 1063, 1074`

    Source: [Henry Pete v. Boland Marine](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2023/2021-ca-0626.html).

12. **Copell v. Arceneaux Ford, Inc. — Third Circuit**

    `Copell v. Arceneaux Ford, Inc., 2020-299, p. 12 (La. App. 3 Cir. 6/9/21), 322 So.3d 886`

    Source: [Henry Pete v. Boland Marine](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2023/2021-ca-0626.html). Note the unspaced `So.3d`.

13. **Louisiana Stadium and Exposition District — Fourth Circuit**

    `La. Stadium and Exposition Dist., 2021-0503, p. 31 (La. App. 4 Cir. 3/23/22), 336 So.3d 920, 932`

    Source: [Henry Pete v. Boland Marine](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2023/2021-ca-0626.html).

14. **Theophile — Fourth Circuit public-domain short form**

    `Theophile, 2023-0396, p. 8, 371 So.3d at 492.`

    Source: [State v. Theophile](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2024/2024-k-0019.html).

15. **State v. Candebat — Fourth Circuit**

    `State v. Candebat, 20130780, pp. 6-7 (La. App. 4 Cir. 1/30/14), 133 So.3d 304-306`

    Source: [State v. Theophile](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2024/2024-k-0019.html). The undivided docket digits and reporter range are preserved from the source.

16. **Bellco Electric, Inc. v. Miller — Fifth Circuit and writ history**

    `Bellco Electric, Inc. v. Miller, 08-785 (La. App. 5 Cir. 3/24/09), 10 So. 3d 797, 799, writ denied, 2009-0863 (La. 5/29/09), 9 So. 3d 170.`

    Source: [Rosetta Nelson v. Teachers’ Retirement System of Louisiana](https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2011/2010ca1190-1.html).

17. **Succession of Blythe — Fifth Circuit, pre-public-domain form**

    `Succession of Blythe, 466 So. 2d 500, 501 (La. App. 5 Cir.), writ denied, 469 So. 2d 985 (La. 1985)`

    Source: [Rosetta Nelson v. Teachers’ Retirement System of Louisiana](https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2011/2010ca1190-1.html).

18. **Bouquet v. Wal-Mart Stores, Inc. — Supreme Court with public-domain pinpoint**

    `Bouquet v. Wal-Mart Stores, Inc., 2008-0309, p. 4 (La. 4/4/08), 979 So.2d 456, 458`

    Source: [Henry Pete v. Boland Marine](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2023/2021-ca-0626.html).

19. **Wainwright v. Fontenot — Supreme Court**

    `Wainwright v. Fontenot, 2000-0492 (La. 10/17/00), 774 So.2d 70`

    Source: [Henry Pete v. Boland Marine](https://law.justia.com/cases/louisiana/fourth-circuit-court-of-appeal/2023/2021-ca-0626.html).

20. **State v. Hearold — pre-1994 Supreme Court regional-only form**

    `State v. Hearold, 603 So. 2d 731 (La. 1992).`

    Source: [State v. Michael Deon Riley](https://law.justia.com/cases/louisiana/second-circuit-court-of-appeal/2025/56-131-ka.html).

#### 5. Style mechanics

**Dual citation system.** Louisiana’s post-1993 form combines a public-domain identifier with a Southern Reporter parallel:

`<docket>, p. <pin> (<court> <full date>), <volume> So.3d <first page>, <pin>`

The docket/date portion can identify the decision before a reporter page exists, while the Southern Reporter component supplies the traditional reporter key.

**Full dates are structural.** Louisiana parentheticals use numerical month/day/year, not merely the decision year:

`(La. App. 3 Cir. 8/15/07)`

A parser must not mistake the slashes or additional numbers for page material.

**Circuit number is load-bearing.** All five Court of Appeal forms must be recognized independently. `(La. App.)` without a circuit would not identify the deciding court.

**Cardinal-versus-ordinal variation.** The court rule’s ordinary forms use `1 Cir.`, while an actual First Circuit source uses `1st Cir.`. The ordinal is not hypothetical. Both should be treated as court signals.

**Rule punctuation versus actual opinions.** The Supreme Court rule’s model citations conventionally separate the public-domain citation and reporter parallel with a semicolon. The sampled appellate opinions frequently use a comma instead:

`2008-0309, p. 4 (La. 4/4/08), 979 So.2d 456, 458`

Real-opinion punctuation therefore deviates from the rule’s idealized presentation and should be accepted as evidence of actual practice.

**Docket letters are commonly omitted.** Opinion headers contain forms such as `56,131-KA`, but citations ordinarily use only `56,131`, consistent with Rule VIII’s instruction to omit the letter designation.

**Docket typography varies.** Actual sources contain:

- Comma-separated appellate dockets: `55,491`
- Hyphenated Supreme Court dockets: `01-2548`
- Four-digit years: `2008-0309`
- Two-digit years: `96-2669`
- Extraction variants with a lost hyphen or inserted spaces.

These variants are not reporter-volume numbers.

**Pinpoint syntax.** The public-domain component uses `p.` or `pp.`:

- `p. 17`
- `pp. 6-7`

The regional parallel then uses an ordinary reporter pin page.

**Short forms can preserve both systems.**

`Theophile, 2023-0396, p. 8, 371 So.3d at 492.`

This contains the public-domain docket and paragraph-like page location plus a regional reporter pin, but no reporter first page. It must inherit the first page from its antecedent.

**Writ history is pervasive.** A Court of Appeal citation is frequently followed by a separate Louisiana Supreme Court `writ denied` citation. These are distinct decisions and distinct first-page keys, even though they occur in one citation run.

**Pending publication.** Louisiana uses both three-underscore and four-underscore blank strings in real text. A subsequent Westlaw identifier does not resolve the missing Southern Reporter first page.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `(La.)` is the state/Supreme Court signal and forms the prefix of `(La. App. 1 Cir.)` through `(La. App. 5 Cir.)`. A shortest-prefix matcher would route every Court of Appeal citation to the Supreme Court.

**(b) Intermediate-court citations are district/division-specific:** **Yes.** The five numbered circuits are citation-level court identifiers. The distinction is mandatory for reliable jurisdiction mapping.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `So. 2d` and `So. 3d` span the Supreme Court and all five Courts of Appeal. Neither reporter can identify a Louisiana court by itself.

**(d) Court abbreviations contain apostrophes or ordinals:** **Yes for ordinals.** An actual First Circuit opinion uses `La. App. 1st Cir.` even though the rule commonly uses `La. App. 1 Cir.`. No apostrophe appears in the core court abbreviation, but apostrophes occur in party names and subsequent-history prose.

**(e) The same case is commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified as an error pattern.** Court of Appeal decisions and Supreme Court writ dispositions often share the same caption or are joined in one citation run. Those are separate adjudications and should not be collapsed into inconsistent attribution. No primary-source example established that one identical Louisiana opinion is commonly attributed to both levels.

#### 7. Not verified

- Quantitative Westlaw or LEXIS prevalence in Louisiana briefs and opinions.
- A single punctuation form consistently followed by all five circuits; the sources prove comma/semicolon and spacing variation.
- Whether `1st Cir.` is formally approved by the Supreme Court rule or is an entrenched First Circuit house variant. Its real use is proven, but its formal status was not.
- Common erroneous Supreme-versus-Court-of-Appeal attribution for the same opinion.
- Whether every pending `___ So. 3d ___` citation is later replaced consistently in electronic opinions after reporter pagination.
- A statewide universal sequence independent of docket number; Louisiana’s public-domain system is docket/court/date-based rather than a separate `YYYY-LA-N` series.
- Whether source-extraction anomalies such as `2400379`, `20130780`, and spaces around hyphens also appear identically in the court’s original PDF text layer. They are copied exactly from the linked public text and were not reconstructed.


---

## Batch 5 — S.W.3d family

**States covered:** Missouri, Tennessee, Kentucky, and Arkansas.

The documents used below are searchable, born-digital appellate opinions or electronically published court materials. Exact examples preserve the source’s punctuation, spacing, capitalization, apostrophes, docket formatting, and apparent typographical irregularities.

---

### Missouri

#### 1. Sources

1. **Ria Schumacher v. SC Data Center, Inc.**, Missouri Court of Appeals, Western District, 2025 — unusually dense with Supreme Court, Eastern, Western, and Southern District citations, an editorially bracketed district, and `Id.` short forms. [Opinion](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html)
2. **State v. Warren Eric Carter**, Missouri Court of Appeals, Western District, 2026 — dense criminal opinion citing all three appellate districts. [Opinion](https://law.justia.com/cases/missouri/court-of-appeals/2026/wd87713.html)
3. **McCarty v. Secretary of State**, Supreme Court of Missouri, 2025 — important because the court repeatedly uses generic `(Mo. App.)` parentheticals without an appellate district. [Opinion](https://law.justia.com/cases/missouri/supreme-court/2025/sc100876.html)
4. **R.M.A. v. Blue Springs R-IV School District**, Supreme Court of Missouri, 2025 — current `Mo. banc` practice, pending-publication citation, named prior-decision labels, and apostrophes in abbreviations. [Opinion](https://law.justia.com/cases/missouri/supreme-court/2025/sc100694.html)
5. **State v. Tate**, Supreme Court of Missouri, 2025 — current en-banc Supreme Court opinion with ordinary `S.W.3d` citations. [Opinion](https://law.justia.com/cases/missouri/supreme-court/2025/sc100676.html)
6. **Scott v. State**, Supreme Court of Missouri, 2025 — includes an intermediate decision cited with a generic `Mo. App.` parenthetical and `(mem.)`. [Opinion](https://law.justia.com/cases/missouri/supreme-court/2025/sc100916.html)
7. **Hensley v. Jackson County**, Supreme Court of Missouri, 2007 — born-digital example whose opinion header expressly identifies the Supreme Court as sitting en banc. [Opinion](https://law.justia.com/cases/missouri/supreme-court/2007/sc-88176-1.html)

#### 2. Court structure as cited

Missouri’s relevant appellate structure is:

- **Supreme Court of Missouri**, ordinarily cited in current opinions as `(Mo. banc)`.
- **Missouri Court of Appeals, Eastern District**, cited as `(Mo. App. E.D.)`.
- **Missouri Court of Appeals, Western District**, cited as `(Mo. App. W.D.)`.
- **Missouri Court of Appeals, Southern District**, cited as `(Mo. App. S.D.)`.

The judiciary’s own history explains that Missouri has one Court of Appeals divided into the Eastern, Southern, and Western Districts. The present district names date from legislation effective in 1979.

Current Supreme Court materials identify the court as sitting **en banc**, and current opinions express that status in citations as `Mo. banc`.

An older Supreme Court decision may instead appear with a plain `(Mo. <year>)` parenthetical. The sampled opinion includes:

`Charles F. Curry & Co. v. Hedrick, 378 S.W.2d 522, 533 (Mo. 1964)`

Actual practice does not always preserve the intermediate district. The Supreme Court’s *McCarty* opinion repeatedly uses `(Mo. App. 2020)`, `(Mo. App. 2011)`, and similar parentheticals without `E.D.`, `W.D.`, or `S.D.`. Thus, the court level may be explicit while the district is absent.

#### 3. Reporters in actual use

**Current published reporter.** Modern Missouri opinions overwhelmingly use `S.W.3d`; older authorities use `S.W.2d`. Both editions contain decisions from the Supreme Court and all three Court of Appeals districts. The reporter therefore cannot determine court level or appellate district without another signal.

**Historical state reporters.** Missouri decisions historically appeared in state-specific reporters, including `Mo.` and `Mo. App.`, but the exact cessation dates and final official volumes were not confirmed from a current Missouri primary source in this batch.

**Pending publication.** A recent Supreme Court decision can be cited with:

`No. SC100652, ___ S.W.3d ___, 2025 WL 843662, at *3 (Mo. banc Mar. 18, 2025)`

This combines a Supreme Court docket number, unresolved regional-reporter fields, a Westlaw identifier, a star pinpoint, and a full-date parenthetical.

**Neutral/public-domain format.** Missouri docket numbers such as `SC100652`, `WD87722`, `ED112408`, and `SD38517` identify the court or district operationally, but the reviewed rules and opinions did not establish a permanent neutral-citation system comparable to `YYYY Ark. N`.

**Vendor citations.** Westlaw is visibly used while regional pagination is pending and for memorandum or otherwise unreported dispositions. It is not the dominant form for fully reported Missouri appellate cases in the sampled opinions.

#### 4. Verbatim examples

1. **J.C.W. v. Wyciskalla — Supreme Court**

   `J.C.W. v. Wyciskalla, 275 S.W.3d 249 (Mo. banc 2009)`

   Source: [Schumacher](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html).

2. **Corozzo v. Wal-Mart Stores, Inc. — Western District**

   `Corozzo v. Wal-Mart Stores, Inc., 531 S.W.3d 566, 575 (Mo. App. W.D. 2017)`

   Source: [Schumacher](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html).

3. **Ste. Genevieve County Levee District No. 2 v. Luhr Bros., Inc. — Eastern District**

   `Ste. Genevieve Cnty. Levee Dist. #2 v. Luhr Bros., Inc., 288 S.W.3d 779, 783 (Mo. App. E.D. 2009)`

   Source: [Schumacher](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html).

4. **Collins v. Swope — Southern District**

   `Collins v. Swope, 605 S.W.2d 538, 540 (Mo. App. S.D. 1980)`

   Source: [Schumacher](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html).

5. **Groh v. Groh — source’s bracketed district preserved**

   `Groh v. Groh, 910 S.W.2d 747 (Mo. App. [W.D.] 1995)`

   Source: [Schumacher](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html).

6. **Charles F. Curry & Co. v. Hedrick — older Supreme Court form**

   `Charles F. Curry & Co. v. Hedrick, 378 S.W.2d 522, 533 (Mo. 1964)`

   Source: [Schumacher](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html).

7. **Missouri Municipal League v. Carnahan — district omitted**

   `Mo. Mun. League v. Carnahan, 303 S.W.3d 573, 586 (Mo. App. 2010)`

   Source: [McCarty](https://law.justia.com/cases/missouri/supreme-court/2025/sc100876.html).

8. **State v. Milazzo — pending reporter plus Westlaw**

   `State v. Milazzo, No. SC100652, ___ S.W.3d ___, 2025 WL 843662, at *3 (Mo. banc Mar. 18, 2025)`

   Source: [R.M.A.](https://law.justia.com/cases/missouri/supreme-court/2025/sc100694.html).

9. **State v. Thomas — Western District with footnote pinpoint**

   `State v. Thomas, 715 S.W.3d 557, 558 n.2 (Mo. App. W.D. 2025)`

   Source: [State v. Carter](https://law.justia.com/cases/missouri/court-of-appeals/2026/wd87713.html).

10. **State v. Ferguson — Eastern District**

    `State v. Ferguson, 568 S.W.3d 533, 540 (Mo. App. E.D. 2019)`

    Source: [State v. Carter](https://law.justia.com/cases/missouri/court-of-appeals/2026/wd87713.html).

11. **State v. Finch — Southern District**

    `State v. Finch, 398 S.W.3d 928, 929 (Mo. App. S.D. 2013)`

    Source: [State v. Carter](https://law.justia.com/cases/missouri/court-of-appeals/2026/wd87713.html).

12. **Vulgamott — bare `Id.` short form**

    `Id. at 388.`

    Source: [Schumacher](https://law.justia.com/cases/missouri/court-of-appeals/2025/wd87722.html); the antecedent is *Vulgamott v. Perry*.

13. **State v. Scott — generic intermediate attribution and memorandum signal**

    `State v. Scott, 636 S.W.3d 208 (Mo. App. 2021) (mem.)`

    Source: [Scott v. State](https://law.justia.com/cases/missouri/supreme-court/2025/sc100916.html).

#### 5. Style mechanics

**`Mo. banc` is a court signal, not explanatory surplus.** It identifies the Supreme Court and distinguishes it from the intermediate `Mo. App.` forms. The source opinions and the court’s own minutes both consistently describe the Supreme Court as sitting en banc.

**Intermediate district placement is terminal.** The usual form is:

`(Mo. App. E.D. <year>)`  
`(Mo. App. W.D. <year>)`  
`(Mo. App. S.D. <year>)`

However, the Supreme Court itself sometimes cites an intermediate opinion merely as `(Mo. App. <year>)`. A formatter cannot assume that every valid Missouri appellate citation contains the district.

**Editorial brackets can occur within the court parenthetical.** The exact `Mo. App. [W.D.]` example is a concrete reason not to require an entirely punctuation-free district token.

**Pending-publication runs are compound.** The *Milazzo* citation contains:

- Case name.
- `No.` and Supreme Court docket.
- Blank `S.W.3d` volume/page fields.
- Westlaw citation.
- Star pinpoint.
- `Mo. banc`.
- Full date.

**Memorandum status may follow the citation.** `(mem.)` appears outside the court/year parenthetical.

**Short forms.** Ordinary `Id.` citations may consist only of an interior page. They contain no first-page or court information and depend completely on the antecedent.

**Governing briefing rule.** [Missouri Rule 84.04](https://www.courts.mo.gov/courts/clerkhandbooksp2rulesonly.nsf/c0c6ffa99df4993f86256ba50057dcb8/988c5b6f0d74867086256ca6005215c9?OpenDocument=) governs appellate brief structure, authorities, and record references. I did not locate a separate current Missouri court-issued citation manual that displaced the forms used in the courts’ own opinions.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `Mo.` begins both `Mo. banc` and `Mo. App. ...`. A matcher that accepts the state prefix alone could map an appellate decision to the Supreme Court. The older plain `(Mo. 1964)` form increases the need to read the whole parenthetical.

**(b) Intermediate-court citations are district/division-specific:** **Usually yes, but not invariably.** `E.D.`, `W.D.`, and `S.D.` are real, substantive district signals. Yet actual Supreme Court opinions sometimes omit the district and use only `Mo. App.`.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `S.W.2d` and `S.W.3d` span the Supreme Court and every Court of Appeals district.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in the core court tokens.** The district signals are initials rather than ordinals. Apostrophes do occur in names and entity abbreviations, and brackets can occur within the district token.

**(e) The same case is commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** The sources establish district-specific versus generic intermediate attribution, but not common Supreme-versus-intermediate misattribution of one identical opinion.

#### 7. Not verified

- The primary-source cessation dates and last volumes of `Mo.` and `Mo. App.`.
- Whether Missouri formally designates `S.W.3d` as its “official reporter,” as Tennessee does expressly.
- A permanent Missouri neutral/public-domain citation system.
- Quantitative Westlaw or LEXIS prevalence.
- Whether bracketed `Mo. App. [W.D.]` is common or an isolated editorial repair.
- Common Supreme-versus-intermediate attribution drift for the same opinion.
- Whether generic `(Mo. App.)` is deliberately preferred in some Supreme Court house contexts or simply reflects source-level omission of available district information.

---

### Tennessee

#### 1. Sources

1. **Gilliam v. Gerregano**, Tennessee Supreme Court, 2025 — Supreme Court `S.W.3d` authorities and a lengthy Court of Appeals Westlaw citation with permission-to-appeal history. [Opinion](https://law.justia.com/cases/tennessee/supreme-court/2025/m2022-00083-sc-r11-cv.html)
2. **Cartwright v. Thomason Hendrix, P.C.**, Tennessee Supreme Court, 2025 — multiple published and unpublished Court of Appeals decisions from the same family of litigation. [Opinion](https://law.justia.com/cases/tennessee/supreme-court/2025/w2022-01627-sc-r11-cv.html)
3. **Shabanian v. Hosseini**, Tennessee Court of Appeals, 2025 — dense with docket-plus-Westlaw forms and real docket punctuation irregularities. [Opinion](https://law.justia.com/cases/tennessee/court-of-appeals/2025/w2024-00886-coa-r3-cv.html)
4. **State v. Jeffery Lynn Sanders**, Tennessee Court of Criminal Appeals, 2025 — dense with reported and unpublished Criminal Appeals citations and several deviations in periods, commas, spaces, and docket construction. [Opinion](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html)
5. **State v. Clyde Willis**, Tennessee Court of Criminal Appeals, 2025 — numerous Supreme Court authorities in `S.W.2d` and `S.W.3d`. [Opinion](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/w2023-01309-cca-r3-cd.html)

#### 2. Court structure as cited

Tennessee has three appellate courts reflected in ordinary case citations:

- **Tennessee Supreme Court:** `(Tenn.)`
- **Tennessee Court of Appeals:** `(Tenn. Ct. App.)`
- **Tennessee Court of Criminal Appeals:** `(Tenn. Crim. App.)`

The intermediate courts are separated by subject matter, not by citation-level geographic district. Their docket numbers often begin with `E`, `M`, or `W`, but the court parenthetical remains statewide. The docket itself also carries a court code, ordinarily `COA` or `CCA`.

Real opinions contain punctuation variants of the Criminal Appeals abbreviation, including:

- `Tenn. Crim. App.`
- `Tenn. Crim App.`
- `Tenn Crim. App.`

These variants appear in published court text and should not be replaced with a single imagined input form.

#### 3. Reporters in actual use

**Official reporter.** Tennessee Supreme Court Rule 4 expressly defines “publication” as publication in the official reporter, the **South Western Reporter 3d**. Reported Supreme Court opinions and qualifying intermediate opinions therefore use `S.W.3d` as the authoritative published form.

**Older regional editions.** Tennessee opinions continue to cite older decisions in `S.W.2d`. Both `S.W.2d` and `S.W.3d` contain decisions from the Supreme Court, Court of Appeals, and Court of Criminal Appeals.

**Unpublished decisions.** The dominant actual form is:

`<case>, No. <docket>, <year> WL <number>, at *<pin> (<court> <full date>)`

The citation can then add:

- `perm. app. granted`
- `perm. app. denied`
- `no perm. app. filed`

Rule 4 provides that most unpublished opinions remain persuasive unless they carry a `Not For Citation`, `DCRO`, or `DNP` designation; reported opinions are controlling.

**Neutral/public-domain format.** No statewide permanent neutral identifier was verified. Docket strings such as `M2024-00536-CCA-R3-CD` identify the proceeding but do not function as a year-sequence neutral reporter.

**Vendor prevalence.** Westlaw is very common for unpublished Tennessee intermediate decisions in the reviewed opinions. Fully reported cases use `S.W.3d` or `S.W.2d`.

#### 4. Verbatim examples

1. **Gilliam — lower Court of Appeals opinion and permission history**

   `Gilliam v. Gerregano, No. M2022-00083-COA-R3CV, 2023 WL 3749982 (Tenn. Ct. App. June 1, 2023), perm. app. granted, (Tenn. Nov. 21, 2023)`

   Source: [Gilliam](https://law.justia.com/cases/tennessee/supreme-court/2025/m2022-00083-sc-r11-cv.html). The missing hyphen between `R3` and `CV` and the comma after `granted` are preserved.

2. **Fisher v. Hargett — Supreme Court**

   `Fisher v. Hargett, 604 S.W.3d 381, 395 (Tenn. 2020)`

   Source: [Gilliam](https://law.justia.com/cases/tennessee/supreme-court/2025/m2022-00083-sc-r11-cv.html).

3. **Bredesen v. Tennessee Judicial Selection Commission — Supreme Court**

   `Bredesen v. Tenn. Jud. Selection Comm’n, 214 S.W.3d 419, 424 (Tenn. 2007)`

   Source: [Gilliam](https://law.justia.com/cases/tennessee/supreme-court/2025/m2022-00083-sc-r11-cv.html).

4. **Cartwright — lower Court of Appeals opinion**

   `Cartwright v. Thomason Hendrix, P.C., No. W2022-01627-COA-R3-CV, 2024 WL 1618895, at *12 (Tenn. Ct. App. Apr. 15, 2024), perm. app. granted, (Tenn. Aug. 28, 2024)`

   Source: [Cartwright](https://law.justia.com/cases/tennessee/supreme-court/2025/w2022-01627-sc-r11-cv.html).

5. **Cartwright v. Jackson Capital Partners — reported Court of Appeals decision**

   `Cartwright v. Jackson Cap. Partners, 478 S.W.3d 596 (Tenn. Ct. App. 2015)`

   Source: [Cartwright](https://law.justia.com/cases/tennessee/supreme-court/2025/w2022-01627-sc-r11-cv.html).

6. **Wallace v. Wallace — unpublished Court of Appeals decision**

   `Wallace v. Wallace, No. M2022-01279-COA-R3-CV, 2023 WL 7919928, at *7 (Tenn. Ct. App. Nov. 16, 2023),`

   Source: [Shabanian](https://law.justia.com/cases/tennessee/court-of-appeals/2025/w2024-00886-coa-r3-cv.html). The trailing comma is present in the source.

7. **In re Estate of Dates — irregular docket punctuation**

   `In re Estate of Dates, No. W2024-00488COA-R3-CV, 2024 WL 5245289 at *3 (Tenn. Ct. App. Dec. 30, 2024)`

   Source: [Shabanian](https://law.justia.com/cases/tennessee/court-of-appeals/2025/w2024-00886-coa-r3-cv.html). The absent hyphen before `COA` and absent comma before `at *3` are preserved.

8. **State v. Lee — Criminal Appeals abbreviation without a period after `Crim`**

   `State v. Lee, No. W2022-00626-CCA-R3-CD, 2023 WL 1956964, at *12 (Tenn. Crim App. Feb. 13, 2023)`

   Source: [State v. Sanders](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html).

9. **State v. Alder — reported Court of Criminal Appeals decision**

   `State v. Alder, 71 S.W.3d 299, 303 (Tenn. Crim. App. 2001)`

   Source: [State v. Sanders](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html).

10. **Rogers v. State — source’s internal docket spaces preserved**

    `Rogers v. State, No. M2010-01987-CCA-R3-5- PD, 2012 WL 3776675, at *60 (Tenn. Crim. App. Aug. 30, 2012)`

    Source: [State v. Sanders](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html).

11. **State v. Odom — Supreme Court**

    `State v. Odom, 137 S.W.3d 572, 589 (Tenn. 2004)`

    Source: [State v. Sanders](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html).

12. **State v. Cobble — unpublished decision and no-permission notation**

    `State v. Cobble, No. M2022-00598-CCA-R3-CD, 2023 WL 4611748, at *3 (Tenn. Crim. App. July 19, 2023)`

    Source: [State v. Sanders](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html); the source follows the citation with `no perm. app. filed.`

13. **State v. Walden — multiple punctuation omissions**

    `State v. Walden, No. M2022-00255-CCA-R3-CD, 2022 WL 17730431 *4 (Tenn Crim. App. Dec. 16, 2022)`

    Source: [State v. Sanders](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html). The missing comma before `*4` and missing period after `Tenn` are in the source.

14. **Lee — vendor short form**

    `Lee, 2023 WL 1956964, at *12.`

    Source: [State v. Sanders](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2025/m2024-00536-cca-r3-cd.html).

#### 5. Style mechanics

**The official reporter is expressly identified by rule.** [Tennessee Supreme Court Rule 4](https://tncourts.gov/courts/supreme-court/rules/supreme-court-rules/rule-4-publication-opinions-not-citation-designation) defines the official reporter as `South Western Reporter 3d`, regulates publication of intermediate decisions, and distinguishes controlling reported opinions from persuasive unpublished opinions.

**Unpublished opinions require more than a docket.** Actual citations normally include the docket, Westlaw number, star pinpoint, court, and full date. They frequently add the permission-to-appeal outcome. The Court of Appeals’ [Rule 12](https://www.tncourts.gov/courts/court-appeals/rules/court-appeals-rules/rule-12-citation-unpublished-opinions) and Court of Criminal Appeals’ [Rule 19](https://www.tncourts.gov/courts/court-criminal-appeals/rules/court-criminal-appeals-rules/rule-19-publication-opinions) govern publication and citation of intermediate opinions.

**Permission history is structurally attached.** Common suffixes include:

- `perm. app. granted`
- `perm. app. denied`
- `no perm. app. filed`

These can affect publication and precedential status under Rule 4.

**Court name punctuation is not uniform.** Real text includes `Tenn. Crim. App.`, `Tenn. Crim App.`, and `Tenn Crim. App.`. Exact punctuation matching alone would miss actual court-authored inputs.

**Docket grammar is noisy.** Normal forms such as `W2024-00886-COA-R3-CV` coexist with:

- A missing hyphen before `COA`.
- Added internal spaces.
- Missing `No.`
- Extra or malformed segments.

**Short forms can be vendor-only.** `Lee, 2023 WL 1956964, at *12.` has no court or first-page reporter data and must inherit its antecedent.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `(Tenn.)` is the state prefix of `(Tenn. Ct. App.)` and `(Tenn. Crim. App.)`.

**(b) Intermediate-court citations are district/division-specific:** **No geographically.** The court distinction is functional—Court of Appeals versus Court of Criminal Appeals. `E`, `M`, and `W` in dockets do not appear as court-parenthetical districts.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `S.W.2d` and `S.W.3d` span all three appellate courts. Rule 4 also expressly contemplates publication of qualifying intermediate decisions in the same official reporter.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in their standard forms.** The risk is punctuation omission, not apostrophes or ordinals. Typographic apostrophes appear in names such as `Comm’n`.

**(e) The same case is commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** Permission appeals produce separate intermediate and Supreme Court decisions under the same caption, but the sampled citations ordinarily identify each decision separately.

#### 7. Not verified

- A permanent neutral/public-domain citation system.
- The cessation date and final volume of any historic Tennessee-specific official reporter.
- Quantitative Westlaw or LEXIS prevalence.
- Whether the punctuation variants `Tenn. Crim App.` and `Tenn Crim. App.` were present in the court’s submitted manuscript or introduced during publication.
- Common erroneous attribution of one identical opinion to both the Supreme Court and an intermediate court.
- Whether all docket defects shown above are present in the original court-hosted PDF text layers rather than archive conversion. They are copied exactly from the linked public opinion text.

---

### Kentucky

#### 1. Sources

1. **Kevin Eugene Hudson v. Commonwealth**, Kentucky Court of Appeals, 2025 — extensive Supreme Court and Court of Appeals citations, pending `S.W.3d` pagination, Westlaw fallback, and named short forms. [Opinion](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2024-ca-0419-mr.html)
2. **Commonwealth v. Keith Lamar Bryant**, Kentucky Court of Appeals, 2025 — dense with both court levels and an unpublished Westlaw citation. [Opinion](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2023-ca-1323-mr.html)
3. **Aubrey Ellis Franklin v. Commonwealth**, Kentucky Court of Appeals, 2026 — recent `S.W.3d` citations and typographic apostrophes. [Opinion](https://law.justia.com/cases/kentucky/court-of-appeals/2026/2025-ca-0198-mr.html)
4. **In re Marcus Daniel Gale**, Supreme Court of Kentucky, 2025 — published Supreme Court opinion. [Opinion](https://law.justia.com/cases/kentucky/supreme-court/2025/2025-sc-0118-kb.html)
5. **Kentucky Board of Medical Licensure v. Wingate**, Supreme Court of Kentucky, 2025 — contains the court’s full current warning governing unpublished Kentucky decisions. [Opinion](https://law.justia.com/cases/kentucky/supreme-court/2025/2025-sc-0246-mr.html)
6. **W.I.S. v. K.M.B.**, Kentucky Court of Appeals, 2025 — discusses current RAP briefing and record-citation requirements. [Opinion](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2024-ca-1125-me.html)

#### 2. Court structure as cited

Kentucky has:

- **Supreme Court of Kentucky:** `(Ky.)`
- **Kentucky Court of Appeals:** `(Ky. App.)`

No district or division is included in ordinary Court of Appeals citation parentheticals. Current dockets distinguish the courts with `SC` and `CA`, but the remaining docket suffixes—such as `MR`, `DG`, `KB`, or `ME`—describe proceeding types rather than geographic appellate divisions.

A historical naming complication exists: Kentucky’s pre-1976 highest court was called the Court of Appeals. Kentucky’s citation rule nevertheless directs decisions of the present Supreme Court **and its predecessor court** to use the `(Ky.)` parenthetical, while decisions of the present intermediate Court of Appeals use `(Ky. App.)`.

#### 3. Reporters in actual use

**Post-1951 reporter practice.** Kentucky’s form-of-citations rule provides that cases reported after **January 1, 1951** are cited in `S.W.2d` or `S.W.3d`:

- Supreme Court and predecessor: `(Ky. <date>)`
- Present Court of Appeals: `(Ky. App. <date>)`

For cases reported before that date, both Kentucky Reports and the Southwestern citation are required.

**Shared reporter.** `S.W.2d` and `S.W.3d` contain both Supreme Court and Court of Appeals decisions. The court parenthetical is therefore indispensable.

**Pending publication.** Current opinions use a compound form such as:

`No. 2024-SC-0166-DG, ___ S.W.3d ___, 2025 WL 1717628, at *3 (Ky. Jun. 20, 2025)`

The citation may be followed by a statement that the opinion is to be published and has become final.

**Unpublished decisions.** RAP 40 requires opinions to state whether they are `TO BE PUBLISHED` or `NOT TO BE PUBLISHED`. A current Supreme Court notice says that unpublished Kentucky appellate decisions rendered after **January 1, 2003** may be cited for consideration if no published opinion adequately addresses the issue, but they are not binding precedent.

**Neutral/public-domain format.** Kentucky docket numbers are frequently used with Westlaw for unpublished decisions, but no permanent universal neutral-citation series was verified.

#### 4. Verbatim examples

1. **Davis v. Commonwealth — Supreme Court**

   `Davis v. Commonwealth, 484 S.W.3d 288 (Ky. 2016)`

   Source: [Hudson](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2024-ca-0419-mr.html).

2. **Mayfield v. Commonwealth — Court of Appeals**

   `Mayfield v. Commonwealth, 590 S.W.3d 300, 303-05 (Ky. App. 2019)`

   Source: [Hudson](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2024-ca-0419-mr.html).

3. **Osborne v. Commonwealth — pending Supreme Court publication**

   `Osborne v. Commonwealth, No. 2024-SC-0166-DG, ___ S.W.3d ___, 2025 WL 1717628, at *3 (Ky. Jun. 20, 2025)`

   Source: [Hudson](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2024-ca-0419-mr.html); the source then states `(to be published and final as of July 11, 2025)`.

4. **Dunn v. Commonwealth — Court of Appeals**

   `Dunn v. Commonwealth, 199 S.W.3d 775, 776 (Ky. App. 2006)`

   Source: [Hudson](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2024-ca-0419-mr.html).

5. **Dunn — named short form**

   `Dunn, 199 S.W.3d at 776`

   Source: [Hudson](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2024-ca-0419-mr.html).

6. **Commonwealth v. Reyes — Supreme Court**

   `Commonwealth v. Reyes, 764 S.W.2d 62, 64-65 (Ky. 1989)`

   Source: [Bryant](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2023-ca-1323-mr.html).

7. **Commonwealth v. Burkhead — Supreme Court**

   `Commonwealth v. Burkhead, 680 S.W.3d 877, 881 (Ky. 2023)`

   Source: [Bryant](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2023-ca-1323-mr.html).

8. **Commonwealth v. Bennett — Court of Appeals**

   `Commonwealth v. Bennett, 553 S.W.3d 268, 271 (Ky. App. 2018)`

   Source: [Bryant](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2023-ca-1323-mr.html).

9. **Thomas v. Commonwealth — Supreme Court**

   `Thomas v. Commonwealth, 95 S.W.3d 828, 829-30 (Ky. 2003)`

   Source: [Franklin](https://law.justia.com/cases/kentucky/court-of-appeals/2026/2025-ca-0198-mr.html).

10. **Commonwealth v. Frazier — Court of Appeals**

    `Commonwealth v. Frazier, 722 S.W.3d 541, 547 (Ky. App. 2025)`

    Source: [Franklin](https://law.justia.com/cases/kentucky/court-of-appeals/2026/2025-ca-0198-mr.html).

11. **Caneyville Volunteer Fire Department v. Green’s Motorcycle Salvage, Inc. — Supreme Court**

    `Caneyville Volunteer Fire Dep’t v. Green’s Motorcycle Salvage, Inc., 286 S.W.3d 790, 806 (Ky. 2009)`

    Source: [Franklin](https://law.justia.com/cases/kentucky/court-of-appeals/2026/2025-ca-0198-mr.html).

12. **Frazier — named short form**

    `Frazier, 722 S.W.3d at 547`

    Source: [Franklin](https://law.justia.com/cases/kentucky/court-of-appeals/2026/2025-ca-0198-mr.html).

13. **In re Gale — Supreme Court**

    `In re Gale, 694 S.W.3d 357 (Ky. 2024).`

    Source: [In re Gale](https://law.justia.com/cases/kentucky/supreme-court/2025/2025-sc-0118-kb.html). The final period appears in the source occurrence.

14. **Garrigus v. Commonwealth — unpublished Supreme Court/Westlaw form**

    `Garrigus v. Commonwealth, No. 2021-SC-0152-MR, 2022 WL 882287, at *1 (Ky. Mar. 24,`

    Source: [Bryant](https://law.justia.com/cases/kentucky/court-of-appeals/2025/2023-ca-1323-mr.html). The citation is split by a source footnote/page break at that point; I have not supplied the missing continuation.

#### 5. Style mechanics

**Rule-prescribed reporter form.** Kentucky’s form-of-citations provision requires Southwestern Reporter citations after January 1, 1951, with `(Ky.)` for the Supreme Court and predecessor and `(Ky. App.)` for the present Court of Appeals. The rule text and RAP 40 publication provisions are reproduced in [Cornell’s Kentucky citation-rule page](https://www.law.cornell.edu/citation/sample_kentucky); the current [RAP 40 text](https://govt.westlaw.com/kyrules/Document/N85757BB085B411EDAF06ABBBBED46FAA) is also publicly accessible.

**Historical court-name trap.** The former highest court was called the Kentucky Court of Appeals. The citation parenthetical—not the historical court’s natural-language name—distinguishes those decisions from the current intermediate court:

- Highest court or predecessor: `(Ky.)`
- Present intermediate court: `(Ky. App.)`

**Publication designation is prominent.** Kentucky opinions place `TO BE PUBLISHED` or `NOT TO BE PUBLISHED` on the face of the decision. The current unpublished-opinion notice expressly limits precedential force while permitting post-2003 unpublished decisions to be cited for consideration under stated conditions.

**Pending-publication form.** A Kentucky citation can combine a docket, blank `S.W.3d` fields, Westlaw, star pinpoint, court, full date, and a later finality statement. The blank first page cannot be reconstructed from the docket or Westlaw identifier.

**Named short forms.** Current opinions use forms such as:

- `Dunn, 199 S.W.3d at 776`
- `Frazier, 722 S.W.3d at 547`
- `Workman, 580 S.W.2d at 207`

**Page ranges.** The selected opinions generally use ASCII hyphens, including `303-05` and `64-65`, rather than typographic en dashes.

**Real text may interrupt citations at page or footnote boundaries.** The *Garrigus* occurrence ends mid-parenthetical in the extracted source. It is unsuitable for automatic completion and is included only to expose the breakage pattern.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `(Ky.)` is the state prefix of `(Ky. App.)`.

**(b) Intermediate-court citations are district/division-specific:** **No.** The present Court of Appeals is cited statewide as `Ky. App.`.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `S.W.2d` and `S.W.3d` contain decisions from both current appellate levels and the historical predecessor court.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in `Ky.` or `Ky. App.`.** Typographic apostrophes occur in party and agency abbreviations such as `Dep’t` and `Green’s`.

**(e) The same case is commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified as a current error pattern.** Kentucky instead has a historical structural hazard: a decision by the old highest “Court of Appeals” is properly cited `(Ky.)`, while a current Court of Appeals decision is `(Ky. App.)`.

#### 7. Not verified

- The exact last bound volume and publication date of Kentucky Reports, beyond the rule’s January 1, 1951 citation boundary.
- A Kentucky neutral/public-domain citation system.
- Quantitative Westlaw or LEXIS prevalence.
- Common erroneous attribution of one identical modern opinion to both appellate levels.
- Whether every post-2003 unpublished decision that practitioners cite includes the full RAP 40 explanatory treatment.
- The omitted continuation of the split *Garrigus* citation; it was deliberately not reconstructed.
- Whether pending `___ S.W.3d ___` citations are systematically updated in every archive copy once reporter pagination becomes available.

---

### Arkansas

#### 1. Sources

1. **George Rothwell v. Terry Rothwell**, Arkansas Court of Appeals, substituted opinion, 2025 — modern official citation, vacated prior citation, pending regional parallel, historical citations, modern parallels, and short forms. [Opinion](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-320-0.html)
2. **Kellco Custom Homes, Inc. v. Williams**, Arkansas Court of Appeals, 2025 — modern Supreme Court and Court of Appeals electronic citations with and without regional parallels. [Opinion](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-571.html)
3. **Kimberly Brahler Barnes v. Arkansas Department of Human Services**, Arkansas Court of Appeals, 2025 — dense modern parallel citations and typographic apostrophes. [Opinion](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-25-411.html)
4. **Kenneth Slocum v. State**, Arkansas Supreme Court, 2025 — current official citation and historical `Ark.`/`S.W.2d` parallel. [Opinion](https://law.justia.com/cases/arkansas/supreme-court/2025/cr-24-762.html)
5. **Jerry W. Walker v. Payne**, Arkansas Supreme Court, 2025 — historical `Ark. App.` parallel and modern electronic citations. [Opinion](https://law.justia.com/cases/arkansas/supreme-court/2025/cv-24-626.html)
6. **Wilder v. State**, Arkansas Supreme Court, 2025 — current Supreme Court electronic citations with and without regional parallels. [Opinion](https://law.justia.com/cases/arkansas/supreme-court/2025/cr-24-390.html)
7. **Arkansas Judiciary Citation Guidelines**, court-issued examples for both appellate courts and reported/unreported decisions. [Guidelines](https://arcourts.gov/courts/supreme-court/reporter/citation-guidelines)
8. **Arkansas Reporter of Decisions page**, documenting discontinuation of the bound official reporters and transition to official electronic reporting. [Reporter page](https://arcourts.gov/courts/supreme-court/reporter)

#### 2. Court structure as cited

Arkansas has:

- **Supreme Court of Arkansas:** `YYYY Ark. N`
- **Arkansas Court of Appeals:** `YYYY Ark. App. N`

Modern Arkansas citations generally do not need a court/year parenthetical because the official electronic citation itself identifies both the court and year:

- `2025 Ark. 96`
- `2025 Ark. App. 613`

The Court of Appeals sits in internal divisions, and opinion headers can state `DIVISION III`, but the division is not incorporated into the official case citation.

Pre-2009 bound citations distinguish the levels through:

- `Ark.` — Supreme Court.
- `Ark. App.` — Court of Appeals.

#### 3. Reporters in actual use

**Bound official reporters discontinued.** In 2009, the Supreme Court directed that publication of **Arkansas Reports** and **Arkansas Appellate Reports** be discontinued. Decisions handed down after **February 14, 2009** are officially reported electronically on the Arkansas Judiciary website. The bound reporters remain the official source for earlier decisions.

**Post-cessation official format.**

- Supreme Court: `YYYY Ark. <opinion number>`
- Court of Appeals: `YYYY Ark. App. <opinion number>`

The Arkansas Judiciary’s citation guidelines expressly apply that format to opinions issued on or after February 14, 2009.

**Regional reporter.** When available, `S.W.3d` is supplied as a parallel. A complete pinpoint run may contain:

`2009 Ark. 78, at 2, 301 S.W.3d 156, 157`

`S.W.3d` spans both appellate courts, while the Arkansas electronic citation identifies the deciding court.

**Historical parallels.**

- Supreme Court: `325 Ark. 38, 924 S.W.2d 237 (1996)`
- Court of Appeals: `91 Ark. App. 300, 210 S.W.3d 157 (2005)`

**Pending regional pagination.** A newly issued electronic opinion can carry:

`___ S.W.3d ___`

The Arkansas electronic citation remains complete and official even while the regional citation is unresolved.

**Vendor citations.** The official guidelines permit a Westlaw parallel where the regional citation is unavailable. Westlaw is optional; the official Arkansas electronic citation stands independently.

#### 4. Verbatim examples

1. **Rothwell — current Court of Appeals official citation**

   `2025 Ark. App. 613`

   Source: opinion header in [Rothwell](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-320-0.html).

2. **Rothwell — vacated prior opinion and pending regional parallel**

   `2025 Ark App. 431, ___ S.W.3d ___`

   Source: [Rothwell](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-320-0.html). The source omits the period after `Ark` in this occurrence.

3. **Keathley v. Keathley — historical Court of Appeals parallel**

   `Keathley v. Keathley, 76 Ark. App. 150, 61 S.W.3d 219 (2001)`

   Source: [Rothwell](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-320-0.html).

4. **Keathley — `Id.` retaining both reporter pinpoints**

   `Id. at 157, 61 S.W.3d at 224.`

   Source: [Rothwell](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-320-0.html).

5. **Jones v. Jones — modern Supreme Court full parallel**

   `Jones v. Jones, 2014 Ark. 96, at 7, 432 S.W.3d 36, 41`

   Source: [Rothwell](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-320-0.html).

6. **Branscum v. Branscum — modern Court of Appeals full parallel**

   `Branscum v. Branscum, 2022 Ark. App. 126, at 5–6, 642 S.W.3d 270, 274.`

   Source: [Rothwell](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-320-0.html).

7. **Bank of the Ozarks v. Walker — Supreme Court without pinpoint**

   `Bank of the Ozarks v. Walker, 2014 Ark. 223, 434 S.W.3d 357`

   Source: [Kellco](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-571.html).

8. **Kellco Custom Homes, Inc. v. Williams — Court of Appeals without regional parallel**

   `Kellco Custom Homes, Inc. v. Williams, 2024 Ark. App. 205.`

   Source: [Kellco](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-24-571.html).

9. **Ring v. Arkansas Department of Human Services — Court of Appeals double pinpoint**

   `Ring v. Ark. Dep’t of Hum. Servs., 2021 Ark. App. 146, at 5, 620 S.W.3d 551, 555.`

   Source: [Barnes](https://law.justia.com/cases/arkansas/court-of-appeals/2025/cv-25-411.html).

10. **Slocum v. State — historical Supreme Court parallel**

    `Slocum v. State, 325 Ark. 38, 924 S.W.2d 237 (1996).`

    Source: [Slocum](https://law.justia.com/cases/arkansas/supreme-court/2025/cr-24-762.html).

11. **Walker v. State — historical Court of Appeals parallel**

    `Walker v. State, 91 Ark. App. 300, 210 S.W.3d 157 (2005).`

    Source: [Walker](https://law.justia.com/cases/arkansas/supreme-court/2025/cv-24-626.html).

12. **Wilder v. State — modern Supreme Court parallel**

    `Wilder v. State, 2023 Ark. 137, 675 S.W.3d 424.`

    Source: [Wilder](https://law.justia.com/cases/arkansas/supreme-court/2025/cr-24-390.html).

13. **Lane v. State — modern official and regional pinpoints**

    `Lane v. State, 2019 Ark. 5, at 4, 564 S.W.3d 524, 529.`

    Source: [Wilder](https://law.justia.com/cases/arkansas/supreme-court/2025/cr-24-390.html).

14. **Official Supreme Court model with Westlaw fallback**

    `Foscue v. McDaniel, 2009 Ark. 223, 2009 WL 1098545.`

    Source: [Arkansas Citation Guidelines](https://arcourts.gov/courts/supreme-court/reporter/citation-guidelines).

15. **Official Court of Appeals model with Westlaw fallback**

    `Nestle USA, Inc. v. Drone, 2009 Ark. App. 311, 2009 WL 1076781.`

    Source: [Arkansas Citation Guidelines](https://arcourts.gov/courts/supreme-court/reporter/citation-guidelines).

#### 5. Style mechanics

**The official citation precedes the regional parallel.** Arkansas’s modern form is:

`<official electronic cite>, at <official pinpoint>, <regional first page>, <regional pinpoint>`

For example:

`2019 Ark. 5, at 4, 564 S.W.3d 524, 529`

The `at 4` location belongs to the official electronic opinion, while `529` belongs to the regional reporter.

**No final court/year parenthetical is normally needed.** `2025 Ark. 96` already encodes the Supreme Court and year; `2025 Ark. App. 613` encodes the Court of Appeals and year.

**Regional citation is optional where unavailable.** The court’s official guidelines permit the electronic citation alone or an optional vendor parallel.

**Substituted opinions can change the official citation.** *Rothwell* expressly vacated the earlier:

`2025 Ark App. 431, ___ S.W.3d ___`

and issued a substituted opinion as:

`2025 Ark. App. 613`

This is a real same-case/multiple-official-identifier event. The later citation supersedes the former; they should not be treated as parallel keys to one simultaneously operative opinion.

**Short forms can retain two pinpoint systems.**

`Id. at 157, 61 S.W.3d at 224.`

Here the first pin is to `Ark. App.`, and the second is to `S.W.3d`.

**Historical and modern formats coexist.** Current opinions freely cite:

- Pre-2009 `Ark.` or `Ark. App.` with regional parallel and year.
- Post-2009 electronic official citation, optionally with regional parallel.

**Court divisions are omitted.** Although the opinion header may say `DIVISION III`, the official citation remains `2025 Ark. App. 613`.

**Court-issued style authority.** The [Arkansas Citation Guidelines](https://arcourts.gov/courts/supreme-court/reporter/citation-guidelines) provide exact forms for published and unpublished opinions of both appellate courts. The [Reporter of Decisions page](https://arcourts.gov/courts/supreme-court/reporter) documents the 2009 transition.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes at the official-citation token level.** `Ark.` is a prefix of `Ark. App.`. A reporter matcher must prefer the full `Ark. App.` token.

**(b) Intermediate-court citations are district/division-specific:** **No.** Court of Appeals divisions appear in opinion headers but not in official citations.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `S.W.2d` and `S.W.3d` span both appellate courts. The electronic `Ark.` versus `Ark. App.` component resolves the court.

**(d) Court abbreviations contain apostrophes or ordinals:** **No.** `Ark.` and `Ark. App.` contain neither. Roman-numeral divisions appear outside the citation. Typographic apostrophes occur in party and agency abbreviations such as `Dep’t`.

**(e) The same case is commonly cited under Supreme-versus-intermediate attribution inconsistently:** **Not verified.** A different but concrete hazard is proven: a substituted Court of Appeals opinion can receive a later official opinion number after the original number is vacated.

#### 7. Not verified

- Quantitative Westlaw or LEXIS prevalence.
- Common erroneous Supreme-versus-Court-of-Appeals attribution for one identical opinion.
- Whether every archive removes or redirects a vacated official citation after a substituted opinion is released.
- Whether a subsequently assigned `S.W.3d` citation is retroactively inserted into every public copy of an opinion.
- Whether Court of Appeals division identifiers ever appear in practitioner-created parentheticals despite being absent from the official form.
- The precise publication-status treatment of every pre-July 2009 unpublished opinion; the current court page directs users to Rule 5-2 for those questions.


---

## Batch 6 — N.W.2d/N.W.3d family

**States covered:** Michigan, Wisconsin, Minnesota, Iowa, Nebraska, North Dakota, and South Dakota.

The sources are searchable, born-digital opinions or electronically issued court documents. Scanned bound reporters were not used for the verbatim examples. The `N.W.3d` transition is already visible across this family, but the local treatment differs sharply: Michigan omits periods (`NW3d`), Wisconsin layers neutral, official, and regional citations, Minnesota and Iowa ordinarily use regional citations alone, Nebraska retains state-specific official reporters, and North Dakota and South Dakota pair regional reporters with permanent public-domain identifiers.

---

### Michigan

#### 1. Sources

1. **Davis v. BetMGM, LLC**, Michigan Supreme Court, 2025 — dense with current `Mich App`, `NW3d`, older `NW2d`, dissent pinpoints, and intermediate-court short forms. [Opinion](https://law.justia.com/cases/michigan/supreme-court/2025/166281.html)
2. **C-Spine Orthopedics, PLLC v. Progressive Michigan Insurance Co.**, Michigan Supreme Court, 2025 — especially useful for current `NW3d`, pending-publication forms, and multiple Court of Appeals decisions in related litigation. [Opinion](https://law.justia.com/cases/michigan/supreme-court/2025/165537.html)
3. **People v. Czarnecki**, Michigan Supreme Court, 2025 — numerous blank `Mich`/`Mich App` and `NW3d` forms, Supreme Court orders, and unpublished Court of Appeals citations. [Opinion](https://law.justia.com/cases/michigan/supreme-court/2025/166654.html)
4. **People v. Kvasnicka**, published Michigan Court of Appeals opinion, 2025 — useful for the official `Mich App` form and the court’s distinctive semicolon-separated parallel citations. [Opinion](https://law.justia.com/cases/michigan/court-of-appeals-published/2025/371542.html)
5. **People v. Poole**, Michigan Supreme Court, 2025 — current Supreme Court treatment of published, unpublished, and pending-publication authorities. [Opinion](https://law.justia.com/cases/michigan/supreme-court/2025/166813.html)

#### 2. Court structure as cited

Michigan’s ordinary appellate structure consists of the **Michigan Supreme Court** and the **Michigan Court of Appeals**. Published cases are distinguished primarily through their official reporter tokens:

- Supreme Court: `Mich`
- Court of Appeals: `Mich App`

Current Michigan opinions omit periods from both reporter abbreviations. When official pagination is present, the year alone appears in the final parenthetical:

- `511 Mich 1; 993 NW2d 1 (2023)`
- `347 Mich App 380; 15 NW3d 306 (2023)`

The Court of Appeals is one statewide court for citation purposes. Panel composition appears in opinion headers, but there is no district or division token analogous to `Mo. App. W.D.` or `Wis. Ct. App. Dist. IV` in the reported citation.

For unreported Court of Appeals decisions, Michigan uses a prose form rather than a compact court parenthetical:

`unpublished per curiam opinion of the Court of Appeals, issued <date> (Docket No. <number>)`

That phrase itself supplies the court attribution.

#### 3. Reporters in actual use

**Official reporters remain active.** Michigan Supreme Court decisions are collected in the **Michigan Reports** (`Mich`), while published Court of Appeals decisions appear in the **Michigan Appeals Reports** (`Mich App`). Current published Court of Appeals opinions expressly state that they remain subject to revision until final publication in the Michigan Appeals Reports. Michigan’s court rules require qualifying Court of Appeals opinions to be published separately from Supreme Court opinions. No cessation date applies to either current official reporter.

**Regional reporters.** Michigan’s house style writes the editions without periods:

- `NW`
- `NW2d`
- `NW3d`

The regional parallel follows the official citation after a semicolon:

`347 Mich App 380; 15 NW3d 306 (2023)`

The `NW2d` and `NW3d` editions span both appellate levels. A bare regional citation therefore does not distinguish the Supreme Court from the Court of Appeals.

**Pending publication.** Michigan uses blanks in the official and regional fields:

`___ Mich App ___; ___ NW3d ___`

The date and docket number follow in parentheses, and a `slip op at` pinpoint may be added separately. This form has no safely recoverable official first page or regional first page at the time it is written.

**Neutral/public-domain format.** The reviewed 2025 opinions continue to rely on official reporters, regional reporters, slip-op pages, docket numbers, and dates. They do not display a permanent Michigan year-court-sequence identifier. A vendor-neutral system was publicly proposed in 2023, but I did not verify an operative adoption order or current use in issued opinions.

**Westlaw and LEXIS.** Westlaw or LEXIS may be used for unreported decisions, but Michigan’s own opinions commonly cite unpublished Court of Appeals cases by the court’s prose docket-and-date form without a vendor identifier. No prevalence percentage was established.

#### 4. Verbatim examples

1. **Davis v. BetMGM, LLC — Court of Appeals, `NW3d`**

   `Davis v BetMGM, LLC, 348 Mich App 402, 416; 19 NW3d 138 (2023).`

   Source: *Davis v. BetMGM, LLC*.

2. **Pappas v. Gaming Control Board — Court of Appeals, `NW2d`**

   `Pappas v Gaming Control Bd, 257 Mich App 647; 669 NW2d 326 (2003).`

   Source: *Davis v. BetMGM, LLC*.

3. **Wallace v. Suburban Mobility Authority for Regional Transportation — two official pinpoints**

   `Wallace v Suburban Mobility Auth for Regional Transp, 347 Mich App 380, 383, 392; 15 NW3d 306 (2023).`

   Source: *C-Spine Orthopedics*.

4. **Farrar v. Suburban Mobility Authority for Regional Transportation — Court of Appeals**

   `Farrar v Suburban Mobility Auth for Regional Transp, 345 Mich App 472; 7 NW3d 80 (2023).`

   Source: *C-Spine Orthopedics*.

5. **People v. Adamowicz — Court of Appeals, named procedural history**

   `People v Adamowicz (On Second Remand), 346 Mich App 213, 219; 12 NW3d 35 (2023),`

   Source: *People v. Czarnecki*. The trailing comma is present in the source sentence.

6. **People v. Taylor — Supreme Court order with blank official page**

   `People v Taylor, ___ Mich ___, ___; 12 NW3d 444 (2024).`

   Source: *People v. Czarnecki*.

7. **People v. Poole — fully pending Supreme Court publication**

   `People v Poole, ___ Mich ___; ___ NW3d ___ (April 1, 2025) (Docket No. 166813).`

   Source: *People v. Czarnecki*.

8. **People v. Osantowski — Court of Appeals with subsequent history**

   `People v Osantowski, 274 Mich App 593; 736 NW2d 289 (2007), rev’d in part on other grounds 481 Mich 103 (2008)`

   Source: *People v. Kvasnicka*.

9. **People v. Taylor — unpublished Court of Appeals form**

   `People v Taylor, unpublished per curiam opinion of the Court of Appeals, issued October 21, 2021 (Docket No. 349544).`

   Source: *People v. Czarnecki*.

10. **Davis — official-reporter short form with judicial attribution**

    `Davis, 348 Mich App at 419-420 (FEENEY, J., dissenting)`

    Source: *Davis v. BetMGM, LLC*.

#### 5. Style mechanics

**Semicolon-separated parallel reporters.** Michigan does not use the comma-separated parallel run common in Minnesota, Nebraska, or Wisconsin. Its characteristic form is:

`official reporter and pin; regional reporter and pin (year)`

For example:

`347 Mich App 380, 383, 392; 15 NW3d 306 (2023)`

The semicolon is structurally meaningful because it separates two reporter systems.

**Reporter abbreviations omit periods.** The court writes `Mich App`, `NW2d`, and `NW3d`, not `Mich. App.`, `N.W.2d`, or `N.W.3d`. That is a real house-style difference within the regional-reporter family.

**Multiple official pinpoints can precede one regional first page.** The *Wallace* example contains official pages `383, 392`, but only the regional first page `306`. A normalizer must continue to identify `347 Mich App 380` and `15 NW3d 306` as the two first-page citations rather than treating either pin as another case.

**Unpublished opinions use prose rather than a conventional reporter substitute.** The phrase `unpublished per curiam opinion of the Court of Appeals, issued ...` may be followed by a docket number but no vendor citation. MCR 7.215 requires the docket number and decision date when a post-1996 unpublished opinion is cited and explains that unpublished opinions are nonbinding.

**Pending-publication short forms can include `slip op at`.** Michigan may cite `___ Mich App at ___; slip op at 2`. The `at ___` component is not a resolvable reporter page.

**Rule.** [MCR 7.215](https://www.courts.michigan.gov/siteassets/rules-instructions-administrative-orders/michigan-court-rules/court-rules-book-ch-7-responsive-html5.zip/Court_Rules_Book_Ch_7/Court_Rules_Chapter_7/Court_Rules_Chapter_7.htm) governs publication, precedent, and citation of unpublished Court of Appeals opinions. The courts’ own opinions provide the more specific punctuation and parallel-reporter evidence.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `Mich` is a literal prefix of `Mich App`. Longest-token recognition is required, especially where a citation has no separate court parenthetical.

**(b) Intermediate-court citations are district/division-specific:** **No.** The Court of Appeals citation uses statewide `Mich App`; no geographic district or panel division is encoded.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `NW2d` and `NW3d` span both the Michigan Supreme Court and Court of Appeals. The official `Mich` or `Mich App` reporter, prose unpublished designation, or other court context is necessary.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in the court tokens.** Typographic apostrophes occur elsewhere—`plaintiff’s`, `Nat’l`, `rev’d`—and can appear within or immediately after the citation span.

**(e) The same case is commonly cited under supreme-court versus intermediate-court attribution inconsistently:** **Not verified as a recurring error.** Michigan frequently has separate Supreme Court orders and Court of Appeals opinions under the same caption, but the examples distinguish them through `Mich`, `Mich App`, docket numbers, or procedural-history language.

#### 7. Not verified

- Adoption or abandonment status of the 2023 proposed Michigan vendor-neutral citation system.
- Quantitative Westlaw/LEXIS use in Michigan appellate briefs.
- A common real-world pattern of one identical opinion being attributed to both appellate levels.
- Whether all blank `___ Mich App ___; ___ NW3d ___` citations are retroactively replaced in every electronic copy after pagination.
- A court-issued standalone citation manual prescribing the exact semicolon and abbreviation mechanics beyond the evidence supplied by current opinions and MCR 7.215.

---

### Wisconsin

#### 1. Sources

1. **Van Oudenhoven v. Department of Justice**, Wisconsin Supreme Court, 2025 — current Supreme Court, Court of Appeals, `N.W.3d`, `N.W.2d`, unpublished-order, and short-form practice. [Opinion](https://law.justia.com/cases/wisconsin/supreme-court/2025/2023ap000070-ft.html)
2. **Kaul v. Wisconsin State Legislature**, Wisconsin Supreme Court, 2025 — recent Supreme Court and Court of Appeals triple citations. [Opinion](https://law.justia.com/cases/wisconsin/supreme-court/2025/2022ap000790.html)
3. **Wisconsin Manufacturers & Commerce, Inc. v. Department of Natural Resources**, Wisconsin Supreme Court, 2025 — modern Court of Appeals authorities and association-name apostrophes. [Opinion](https://law.justia.com/cases/wisconsin/supreme-court/2025/2022ap000718.html)
4. **Brown v. Wisconsin Elections Commission**, Wisconsin Supreme Court, 2025 — current election authorities and a real source-level `N.W.2d`/`N.W.3d` inconsistency. [Opinion](https://law.justia.com/cases/wisconsin/supreme-court/2025/2024ap000232.html)
5. **State v. McAdory**, Wisconsin Supreme Court, 2025 — modern `WI App` identifiers, case labels, and older `Ct. App.` reporter forms. [Opinion](https://law.justia.com/cases/wisconsin/supreme-court/2025/2023ap000645-cr.html)

#### 2. Court structure as cited

Wisconsin has a **Wisconsin Supreme Court** and a **Wisconsin Court of Appeals**. Since 2000, the public-domain court identifiers are:

- Supreme Court: `WI`
- Court of Appeals: `WI App`

Examples:

- `2024 WI 15`
- `2024 WI App 38`

The Court of Appeals is administratively divided into Districts I through IV, and district numbers appear in opinion headers. The permanent public-domain citation, however, does not encode the district. All districts publish under `WI App`.

Before the public-domain system, a Court of Appeals decision could be identified by the parenthetical `(Ct. App. 1993)` following `Wis. 2d` and `N.W.2d`. Current citations to those older cases preserve that parenthetical.

#### 3. Reporters in actual use

**Public-domain citation.** Effective **January 1, 2000**, Wisconsin adopted permanent identifiers of the form:

- `YYYY WI N`
- `YYYY WI App N`

Pinpoints use numbered paragraphs:

`2024 WI 15, ¶5`

The initial citation ordinarily proceeds from public-domain citation to official reporter to regional reporter.

**Official reporter.** `Wis. 2d` remains part of the ordinary current triple citation. It spans both the Supreme Court and Court of Appeals; the neutral `WI` versus `WI App` component supplies the court level.

**Regional reporters.** Both `N.W.2d` and `N.W.3d` appear in current opinions. The regional reporter is the third component of the modern run:

`2024 WI App 38, 413 Wis. 2d 15, 10 N.W.3d 402`

`N.W.2d` and `N.W.3d` likewise span both appellate courts.

**Unpublished orders and opinions.** Wisconsin may cite an unreported disposition by docket number, court/date parenthetical, and a description such as `unpublished order`. The source set does not establish a universal vendor identifier for such dispositions.

**Westlaw and LEXIS.** Vendor citations occur in unreported cases but are not prevalent in the selected recent published opinions.

#### 4. Verbatim examples

1. **Van Oudenhoven — Court of Appeals triple citation**

   `Van Oudenhoven v. DOJ, 2024 WI App 38, 413 Wis. 2d 15, 10 N.W.3d 402.`

   Source: *Van Oudenhoven*.

2. **Amazon Logistics — Supreme Court with paragraph range**

   `Amazon Logistics, Inc. v. LIRC, 2024 WI 15, ¶¶4-5, 411 Wis. 2d 166, 4 N.W.3d 294`

   Source: *Van Oudenhoven*.

3. **State v. Braunschweig — Supreme Court, `N.W.2d`**

   `State v. Braunschweig, 2018 WI 113, ¶22, 384 Wis. 2d 742, 921 N.W.2d 199.`

   Source: *Van Oudenhoven*.

4. **Van Oudenhoven — unpublished Supreme Court order**

   `Van Oudenhoven v. DOJ, No. 2023AP70-FT, unpublished order (Wis. Nov. 12, 2024)`

   Source: *Van Oudenhoven*.

5. **Kaul — Court of Appeals**

   `Kaul v. Wis. State Legislature, 2025 WI App 3, ¶¶36, 43, 414 Wis. 2d 686, 17 N.W.3d 281.`

   Source: *Kaul*.

6. **Evers v. Marklein — Supreme Court**

   `Evers v. Marklein, 2024 WI 31, ¶10, 412 Wis. 2d 525, 8 N.W.3d 395.`

   Source: *Kaul*.

7. **Midwest Renewable Energy Association — Court of Appeals**

   `Midwest Renewable Energy Ass’n v. Pub. Serv. Comm’n of Wis., 2024 WI App 34, ¶71, 412 Wis. 2d 698, 8 N.W.3d 848`

   Source: *Wisconsin Manufacturers & Commerce*.

8. **Hess v. WEC — current Court of Appeals citation**

   `Hess v. WEC, 2024 WI App 46, ¶18, 413 Wis. 2d 285, 11 N.W.3d 201`

   Source: *Brown*.

9. **State v. McAdory — parenthetical case label**

   `State v. McAdory, 2024 WI App 29, 412 Wis. 2d 112, 8 N.W.3d 101 (McAdory II)`

   Source: *McAdory*.

10. **Town of Menasha v. Bastian — pre-neutral Court of Appeals form**

    `Town of Menasha v. Bastian, 178 Wis. 2d 191, 503 N.W.2d 382 (Ct. App. 1993).`

    Source: *McAdory*.

#### 5. Style mechanics

**Three-layer modern citation.** Wisconsin commonly supplies all of:

1. Public-domain identifier.
2. Official `Wis. 2d` citation.
3. Regional `N.W.2d` or `N.W.3d` citation.

The first-page keys in:

`2024 WI App 38, 413 Wis. 2d 15, 10 N.W.3d 402`

are separate citation records, while `WI App 38` also supplies the court directly.

**Paragraph pinpoints precede reporter parallels.** A citation can read:

`2024 WI 15, ¶¶4-5, 411 Wis. 2d 166, 4 N.W.3d 294`

The paragraphs apply to the opinion as a whole and are not reporter pages.

**No district in the permanent citation.** A District I and District IV opinion both use `WI App`. District information in a document header should not be expected in every citation string.

**Older cases require a parenthetical court signal.** `Wis. 2d` and `N.W.2d` alone do not distinguish the appellate level, so pre-2000 Court of Appeals citations use `(Ct. App. <year>)`.

**Named short forms can combine the official reporter with paragraph pins.** A source example is:

`Van Oudenhoven, 413 Wis. 2d 15, ¶¶27, 29, 33`

The public-domain identifier and regional citation are omitted, requiring antecedent resolution.

**Real-source reporter-edition error.** *Brown* contains one occurrence of the *Hess* citation as `11 N.W.2d 201`, while another occurrence uses `11 N.W.3d 201`. The latter aligns with the current series and complete citation. This is direct evidence that a court-authored opinion can contain an edition typo; a normalizer should preserve the source text rather than silently “correcting” it without evidence.

**Rule.** [Wisconsin Supreme Court Rule Chapter 80](https://docs.legis.wisconsin.gov/misc/scr/80) prescribes the public-domain forms, ordering of citation components, and paragraph pinpoints.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `WI` is a prefix of `WI App`. Exact or longest-token matching is required.

**(b) Intermediate-court citations are district/division-specific:** **Administratively yes, citation-form no.** Wisconsin has four Court of Appeals districts, but the permanent citation does not contain the district. A district-specific registry inference cannot rely on the citation string alone.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `Wis. 2d`, `N.W.2d`, and `N.W.3d` span both appellate levels. The public-domain identifier or older court parenthetical supplies the distinction.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in `WI` or `WI App`.** District headers use Roman numerals; party and entity abbreviations can contain typographic apostrophes such as `Ass’n` and `Comm’n`.

**(e) The same case is commonly cited under supreme-court versus intermediate-court attribution inconsistently:** **Not verified.** The directly demonstrated variation is a wrong regional **edition**, not conflicting court attribution.

#### 7. Not verified

- Quantitative use of Westlaw or LEXIS in Wisconsin appellate filings.
- Common attribution of one identical opinion to both appellate levels.
- Whether district numbers are routinely included in practitioner parentheticals despite their absence from the official public-domain citation.
- Whether every electronic opinion containing an edition typo is later corrected in the official reporter.
- A current citation example from each of the four Court of Appeals districts within this limited batch; the court’s structural existence is verified, but the permanent form is the same for all.

---

### Minnesota

#### 1. Sources

1. **Fletcher Properties, Inc. v. City of Minneapolis**, Minnesota Supreme Court, 2025 — Supreme Court and Court of Appeals decisions under the same caption, `N.W.2d`, `N.W.3d`, order citations, and named-decision short forms. [Opinion](https://law.justia.com/cases/minnesota/supreme-court/2025/a23-0191.html)
2. **Hoskin v. State**, Minnesota Supreme Court, 2025 — recent `N.W.3d`, first-series `N.W.`, apostrophes, and Westlaw short forms. [Opinion](https://law.justia.com/cases/minnesota/supreme-court/2025/a23-1275.html)
3. **Hook & Ladder Apartments, LP v. City of Minneapolis**, Minnesota Supreme Court, 2025 — recent Supreme Court cases, Court of Appeals cases, and unreported Westlaw authorities. [Opinion](https://law.justia.com/cases/minnesota/supreme-court/2025/a23-1048.html)
4. **State v. Hill**, Minnesota Supreme Court, 2025 — Supreme Court regional citations and named short forms. [Opinion](https://law.justia.com/cases/minnesota/supreme-court/2025/a23-0560.html)
5. **State v. Seeman**, Minnesota Supreme Court, 2025 — recent `N.W.3d`, `N.W.2d`, and short-form practice. [Opinion](https://law.justia.com/cases/minnesota/supreme-court/2025/a23-0571.html)

#### 2. Court structure as cited

Minnesota’s appellate courts are:

- **Minnesota Supreme Court:** `(Minn.)`
- **Minnesota Court of Appeals:** `(Minn. App.)`

The Court of Appeals is one statewide court and sits in three-judge panels. No district or division is encoded in its citation parenthetical.

The court distinction is carried almost entirely by the parenthetical because modern Minnesota opinions ordinarily cite the North Western Reporter without a state-specific official reporter:

- `947 N.W.2d 1, 6 (Minn. 2020)`
- `931 N.W.2d 410, 429–30 (Minn. App. 2019)`

When the case is unreported, the same court distinction appears after a docket, Westlaw identifier, and full date.

#### 3. Reporters in actual use

**Official publication.** Minnesota’s State Law Library states that official appellate opinions are those published by Thomson West in the **North Western Reporter or Minnesota Reporter**. Current opinions in the sample use `N.W.2d` and `N.W.3d` as the working published citation.

**Regional editions.**

- Historical first series: `N.W.`
- Recent historical/current: `N.W.2d`
- Current third series: `N.W.3d`

All three can appear in current born-digital opinions. The same series contains both Supreme Court and Court of Appeals cases, making the parenthetical essential.

**State-specific reporters.** Older Minnesota cases can be found in `Minn.`, but current opinion practice in the selected sources ordinarily supplies only the North Western citation. I did not verify a primary-source cessation date for routine Minnesota Reports citations; current court and library materials emphasize the North Western Reporter.

**Neutral/public-domain format.** No permanent year-court-sequence citation appears in the selected current opinions. The Court of Appeals’ precedential/nonprecedential classification is instead governed by Minn. R. Civ. App. P. 136.01.

**Nonprecedential and vendor citations.** Nonprecedential Court of Appeals opinions may be cited as persuasive rather than binding authority. Westlaw is common in the sampled citations to those decisions, normally with docket number, star pinpoint, `Minn. App.`, and full date.

#### 4. Verbatim examples

1. **Fletcher Properties — Supreme Court**

   `Fletcher Props., Inc. v. City of Minneapolis, 947 N.W.2d 1, 6 (Minn. 2020).`

   Source: *Fletcher Properties*.

2. **Fletcher Properties — Court of Appeals**

   `Fletcher Props., Inc. v. City of Minneapolis, 931 N.W.2d 410, 429–30 (Minn. App. 2019).`

   Source: *Fletcher Properties*.

3. **Fletcher II — Court of Appeals, `N.W.3d`**

   `Fletcher Props., Inc. v. City of Minneapolis (Fletcher II), 2 N.W.3d 544, 562 (Minn. App. 2024).`

   Source: *Fletcher Properties*.

4. **Interlocutory order citation**

   `No. A23-0191, Order at 2 (Minn. App. filed Feb. 24, 2023).`

   Source: *Fletcher Properties*.

5. **Demskie v. U.S. Bank National Association — Supreme Court, `N.W.3d`**

   `Demskie v. U.S. Bank Nat’l Ass’n, 7 N.W.3d 382, 387 (Minn. 2024)`

   Source: *Hoskin*.

6. **Zimmermann v. Benz — first-series `N.W.`**

   `Zimmermann v. Benz, 202 N.W. 272 (Minn. 1925)`

   Source: *Hoskin*.

7. **Jacobs v. City of Columbia Heights — Supreme Court**

   `Jacobs v. City of Columbia Heights, 9 N.W.3d 536, 540 (Minn. 2024)`

   Source: *Hook & Ladder*.

8. **Park v. Schneider — Court of Appeals Westlaw form**

   `Park v. Schneider, No. CX-9983, 1999 WL 540183, at *4 (Minn. App. July 27, 1999)`

   Source: *Hook & Ladder*.

9. **Hill — named short form**

   `Hill, 10 N.W.3d at 323`

   Source: *State v. Hill*.

10. **Seeman — named short form with page range**

    `Seeman, 5 N.W.3d at 171–72.`

    Source: *State v. Seeman*.

#### 5. Style mechanics

**Regional-only published form.** The dominant modern form is simply:

`<volume> N.W.3d <first page>, <pin> (<court> <year>)`

No state-specific reporter or neutral identifier precedes it.

**Court parenthetical is load-bearing.** Because `N.W.3d` spans both appellate courts, omission of `App.` changes the attributed court:

- `(Minn.)`
- `(Minn. App.)`

**Same-caption appellate sequence.** The *Fletcher* litigation generated a Court of Appeals decision, a Supreme Court decision, and a later Court of Appeals decision labeled `(Fletcher II)`. These are separate opinions with different first pages, not parallel citations. The assigned label can appear before the reporter.

**Order citations are structurally separate from case citations.** `No. A23-0191, Order at 2 ...` has neither a reporter first page nor a vendor identifier.

**Nonprecedential decisions.** Minn. R. Civ. App. P. 136.01 distinguishes precedential opinions from nonprecedential opinions and permits the latter to be cited as persuasive authority. Current terminology is “nonprecedential,” replacing the older informal “unpublished” label.

**Vendor short forms.** A named short form can consist of only a case name, Westlaw identifier, and star pin:

`Hoskin, 2024 WL 2131674, at *4–5, *10–12.`

It must inherit court and disposition information from the antecedent.

**Rule and guidance.** The State Law Library’s [case-reports guidance](https://mn.gov/law-library/how-do-i-find/case-reports-by-citation.jsp) gives the ordinary North Western Reporter form, while Rule 136.01 governs the precedential status of Court of Appeals opinions.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `(Minn.)` shares the state prefix with `(Minn. App.)`. A prefix-only parenthetical matcher would swallow the intermediate signal.

**(b) Intermediate-court citations are district/division-specific:** **No.** The Court of Appeals is cited statewide as `Minn. App.`.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `N.W.`, `N.W.2d`, and `N.W.3d` contain decisions from both appellate courts.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in the court tokens.** Typographic apostrophes occur frequently in citation spans, including `Nat’l Ass’n`.

**(e) The same case is commonly cited under supreme-court versus intermediate-court attribution inconsistently:** **Not verified as erroneous practice.** Same-caption cases at both levels are common enough to require first-page and procedural-history awareness, but the sampled opinions distinguish them correctly.

#### 7. Not verified

- A primary-source cessation date for routine citation to Minnesota Reports.
- A Minnesota permanent neutral/public-domain case identifier.
- Quantitative Westlaw or LEXIS prevalence.
- Common erroneous attribution of one identical opinion to both levels.
- Whether practitioners regularly supply a state-specific `Minn.` parallel when one exists; the current court opinions sampled do not.
- A court-issued citation manual specifying every abbreviation and punctuation detail beyond the published-opinion evidence and procedural rules.

---

### Iowa

#### 1. Sources

1. **Sikora v. State**, Iowa Supreme Court, 2025 — dense with `N.W.3d`, `N.W.2d`, first-series `N.W.`, older `Iowa`, and apostrophe-heavy authorities. [Opinion](https://law.justia.com/cases/iowa/supreme-court/2025/23-1766.html)
2. **State v. Manning**, Iowa Supreme Court, 2025 — current Supreme Court `N.W.3d` and an unpublished Court of Appeals Westlaw citation with subsequent history. [Opinion](https://law.justia.com/cases/iowa/supreme-court/2025/23-1390.html)
3. **State v. Mills**, Iowa Court of Appeals, 2025 — recent Supreme Court short forms and several unpublished Court of Appeals citations. [Opinion](https://law.justia.com/cases/iowa/court-of-appeals/2025/24-0770.html)
4. **State v. Wilson**, Iowa Court of Appeals, 2025 — a recent reported Court of Appeals decision in `N.W.3d`. [Opinion](https://law.justia.com/cases/iowa/court-of-appeals/2025/23-1647.html)
5. **Bright v. State** and **Diercks v. State**, Iowa Supreme Court, 2025 — pending `N.W.3d` form and a current named short form. [Bright](https://law.justia.com/cases/iowa/supreme-court/2025/24-1019.html) and [Diercks](https://law.justia.com/cases/iowa/supreme-court/2025/23-1729.html)

#### 2. Court structure as cited

Iowa has:

- **Iowa Supreme Court:** `(Iowa)`
- **Iowa Court of Appeals:** `(Iowa Ct. App.)`

The Court of Appeals is cited as one statewide court. No district or division is included.

Current published citations rely primarily on the regional reporter:

- `3 N.W.3d 540, 546 (Iowa 2024)`
- `14 N.W.3d 763, 767 (Iowa Ct. App. 2024)`

For unpublished Court of Appeals cases, the same parenthetical follows a docket number, Westlaw identifier, star pinpoint, and full date.

#### 3. Reporters in actual use

**Current rule.** Iowa Rule of Appellate Procedure 6.904 directs citations to Iowa cases to the **North Western Reporter** when reported. If a case has not been reported there, the writer may use an official or electronic source. The rule’s court parentheticals are `(Iowa)` and `(Iowa Ct. App.)`.

**Regional editions.** Current opinions use `N.W.3d`; older authorities use `N.W.2d` and first-series `N.W.`. All span both Iowa appellate courts.

**Historical official reporter.** Older decisions can carry an `Iowa` reporter citation, as the *Sikora* opinion’s historical authorities demonstrate. Current opinions ordinarily omit it in favor of the North Western Reporter. I did not confirm the exact cessation date of Iowa Reports from a primary Iowa court source in this batch.

**Pending publication.**

`Miller v. State, ___ N.W.3d ___ (Iowa 2025)`

shows that Iowa may cite a recent opinion with blank regional pagination and a court/year parenthetical. No separate permanent neutral identifier appears.

**Unpublished/vendor format.** Rule 6.904 contemplates docket and electronic-database citations for unpublished cases. Actual opinions use forms such as:

`No. 11-1677, 2012 WL 4550851, at *5 (Iowa Ct. App. Oct. 3, 2012)`

Westlaw is therefore prevalent in citations to unpublished Court of Appeals decisions, although no quantitative percentage was measured.

#### 4. Verbatim examples

1. **Terrace Hill Society Foundation v. Terrace Hill Commission — Supreme Court**

   `Terrace Hill Soc’y Found. v. Terrace Hill Comm’n, 6 N.W.3d 290, 294 (Iowa 2024)`

   Source: *Sikora*.

2. **State v. Slaughter — Supreme Court**

   `State v. Slaughter, 3 N.W.3d 540, 546 (Iowa 2024).`

   Source: *State v. Manning*.

3. **State v. Canady — Supreme Court**

   `State v. Canady, 4 N.W.3d 661, 668 (Iowa 2024)`

   Source: *State v. Manning*.

4. **State v. Howard — reported Court of Appeals case**

   `State v. Howard, 14 N.W.3d 763, 767 (Iowa Ct. App. 2024).`

   Source: *State v. Wilson*.

5. **State v. Bonert — unpublished Court of Appeals**

   `State v. Bonert, No. 11-1677, 2012 WL 4550851, at *5 (Iowa Ct. App. Oct. 3, 2012)`

   Source: *State v. Mills*.

6. **State v. Wade — unpublished Court of Appeals**

   `No. 16-0867, 2017 WL 2181450, at *5 (Iowa Ct. App. May 17, 2017).`

   Source: *State v. Mills*; the source introduces this as *State v. Wade*.

7. **State v. Cook — Supreme Court**

   `State v. Cook, 996 N.W.2d 703, 708 (Iowa 2023).`

   Source: *State v. Shaikoski*.

8. **Brown — named short form**

   `Brown, 5 N.W.3d at 615`

   Source: *State v. Mills*.

9. **Teig — named short form**

   `Teig, 8 N.W.3d at 500.`

   Source: *Diercks v. State*.

10. **Miller v. State — pending regional publication**

    `Miller v. State, ___ N.W.3d ___ (Iowa 2025)`

    Source: *Bright v. State*.

#### 5. Style mechanics

**Regional reporter is the primary published citation.** Iowa does not ordinarily prepend a current state-specific reporter or neutral identifier. Court attribution therefore lives in the terminal parenthetical.

**Unpublished citations use full dates.** The ordinary pattern is:

`No. <docket>, <year> WL <number>, at *<pin> (Iowa Ct. App. <date>)`

This differs from a published `N.W.3d` citation, whose parenthetical contains only court and year.

**Named short forms can be extremely compact.** `Teig, 8 N.W.3d at 500.` contains no court or first page and must inherit from its antecedent.

**No `supra` or `infra` for case citations.** Iowa Rule 6.904 prohibits those short-form signals, favoring `Id.` or shortened case names.

**Publication-stage blanks.** `___ N.W.3d ___ (Iowa 2025)` has neither a regional volume nor a first page. The court/year parenthetical gives jurisdiction but cannot create a canonical first-page key.

**Rule.** [Iowa Rule of Appellate Procedure 6.904](https://www.legis.iowa.gov/docs/ACO/CourtRulesChapter/6.pdf) governs citation form, court abbreviations, unpublished decisions, and short forms.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `(Iowa)` is the state prefix within `(Iowa Ct. App.)`.

**(b) Intermediate-court citations are district/division-specific:** **No.** The Court of Appeals is cited statewide.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `N.W.`, `N.W.2d`, and `N.W.3d` span both appellate courts.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in the court tokens.** Typographic apostrophes occur in case and entity abbreviations such as `Soc’y` and `Comm’n`.

**(e) The same case is commonly cited under supreme-court versus intermediate-court attribution inconsistently:** **Not verified.** Subsequent Supreme Court review can produce a second opinion under the same caption, but the sample distinguishes the separate decisions.

#### 7. Not verified

- A primary-source exact cessation date for Iowa Reports; a secondary citation guide places cessation in 1968, but that date was not primary-source-confirmed here.
- A permanent Iowa neutral/public-domain case identifier.
- Quantitative vendor-citation prevalence.
- Common erroneous attribution of a single opinion to both appellate courts.
- Whether every current published Court of Appeals decision receives an `N.W.3d` citation quickly enough to displace its earlier Westlaw form.
- Whether the source’s typographic en dash in some docket numbers is stable across the court PDF and archive HTML.

---

### Nebraska

#### 1. Sources

1. **Elbert v. Keating, O’Gara**, Nebraska Supreme Court, 2025 — current `Neb.`, blank `N.W.3d`, numerous reported `N.W.3d` parallels, and `supra note` short forms. [Opinion](https://law.justia.com/cases/nebraska/supreme-court/2025/s-23-893.html)
2. **State v. Sands**, Nebraska Court of Appeals, 2025 — current `Neb. App.` and pending `N.W.3d` publication, plus numerous Supreme Court authorities. [Opinion](https://law.justia.com/cases/nebraska/court-of-appeals/2025/a-24-508.html)
3. **State v. Blythe**, Nebraska Court of Appeals memorandum web opinion, 2025 — nonpermanent-publication warning and dense current `N.W.3d` citations. [Opinion](https://law.justia.com/cases/nebraska/court-of-appeals/2025/a-24-667.html)
4. **State v. Johansen**, Nebraska Court of Appeals, 2025 — another born-digital published intermediate opinion in the `Neb. App.` advance sheets. [Opinion](https://law.justia.com/cases/nebraska/court-of-appeals/2025/a-24-419.html)
5. **State v. Sanchez**, Nebraska Court of Appeals, 2025 — current Court of Appeals official-reporter form and blank regional pagination. [Opinion](https://law.justia.com/cases/nebraska/court-of-appeals/2025/a-24-636.html)

#### 2. Court structure as cited

Nebraska has:

- **Nebraska Supreme Court:** `Neb.`
- **Nebraska Court of Appeals:** `Neb. App.`

Ordinary published citations rely on the official reporter token rather than a separate court parenthetical:

- `318 Neb. 803, 19 N.W.3d 244 (2025)`
- `33 Neb. App. 554`

The year parenthetical is sufficient because `Neb.` and `Neb. App.` identify the court. The Court of Appeals is cited statewide; no district or division appears in the reporter citation.

#### 3. Reporters in actual use

**Official reporters.**

- `Neb.` — Nebraska Reports, Supreme Court.
- `Neb. App.` — Nebraska Appellate Reports, Court of Appeals.

Effective **January 1, 2016**, Nebraska designated the online certified PDF as the official opinion, beginning with Volume 275 of Nebraska Reports and Volume 16 of Nebraska Appellate Reports. The state-specific volume and page citations continue even though the authoritative version is electronic.

**Regional reporters.** Current opinions use `N.W.3d`; older cases use `N.W.2d`. A standard parallel is:

`316 Neb. 419, 5 N.W.3d 179 (2024)`

Both regional editions span the Supreme Court and Court of Appeals, while `Neb.` versus `Neb. App.` supplies the court level.

**Pending regional pagination.** A published opinion may already have an official state-reporter page while the regional citation remains blank:

`319 Neb. 390`  
`___ N.W.3d ___`

This is different from a jurisdictional blank: the official `Neb.` first-page citation is complete and usable even though the regional first page is unresolved.

**Memorandum web opinions.** A nonpermanently published Court of Appeals decision identifies itself as a `Memorandum Web Opinion`, gives a docket and date, and warns that it may not be cited except as allowed by § 2-102(E). It has no `Neb. App.` first page.

**Neutral/public-domain format.** Nebraska has an authoritative electronic publication system but not a permanent `YYYY NE N` citation. The official citation remains volume-page-based.

**Vendor citations.** The selected opinions rarely use Westlaw for Nebraska appellate cases. No prevalence percentage was established.

#### 4. Verbatim examples

1. **Elbert v. Young — Supreme Court**

   `Elbert v. Young, 312 Neb. 58, 977 N.W.2d 892 (2022).`

   Source: *Elbert v. Keating, O’Gara*.

2. **Saint James Apartment Partners — Supreme Court, `N.W.3d`**

   `Saint James Apt. Partners v. Universal Surety Co., 316 Neb. 419, 5 N.W.3d 179 (2024).`

   Source: *Elbert*.

3. **State ex rel. Hilgers v. Evnen — Supreme Court**

   `State ex rel. Hilgers v. Evnen, 318 Neb. 803, 19 N.W.3d 244 (2025).`

   Source: *Elbert*.

4. **Czech v. Allen — Supreme Court**

   `Czech v. Allen, 318 Neb. 904, 21 N.W.3d 1 (2025);`

   Source: *Elbert*. The terminal semicolon is part of the source’s string cite.

5. **D&M Roofing & Siding — `supra note` short form**

   `D&M Roofing & Siding, supra note 12, 316 Neb. at 968, 7 N.W.3d at 881.`

   Source: *Elbert*.

6. **State v. Sands — Court of Appeals official citation**

   `33 Neb. App. 554`

   Source: the official citation/header in *State v. Sands*.

7. **State v. Goynes — Supreme Court**

   `State v. Goynes, 318 Neb. 413, 16 N.W.3d 373 (2025).`

   Source: *State v. Sands*.

8. **State v. Boeggeman — dual pinpoints**

   `State v. Boeggeman, 316 Neb. 581, 592, 5 N.W.3d 735, 743 (2024),`

   Source: *State v. Sands*. The trailing comma is preserved.

9. **State v. Npimnee — Supreme Court**

   `State v. Npimnee, 316 Neb. 1, 2 N.W.3d 620 (2024).`

   Source: *State v. Blythe*.

10. **State v. Rezac — Supreme Court**

    `State v. Rezac, 318 Neb. 352, 15 N.W.3d 705 (2025).`

    Source: *State v. Blythe*.

#### 5. Style mechanics

**Official and regional parallels are comma-separated.** A standard full citation is:

`318 Neb. 803, 19 N.W.3d 244 (2025)`

Unlike Michigan, Nebraska does not use a semicolon between the reporters.

**The official state reporter can become usable before the regional reporter.** *Elbert* is officially `319 Neb. 390` while its `N.W.3d` field remains blank. That means one valid first-page key coexists with one unresolved parallel.

**Dual pinpoints.** A full citation may contain one pin in each reporter:

`316 Neb. 581, 592, 5 N.W.3d 735, 743`

The first-page keys remain `316 Neb. 581` and `5 N.W.3d 735`.

**Footnote-style `supra note`.** Nebraska’s opinions use forms such as:

`D&M Roofing & Siding, supra note 12, 316 Neb. at 968, 7 N.W.3d at 881.`

This differs directly from Iowa’s rule prohibiting `supra` for case short forms. The `supra note` reference may intervene between the case name and reporter pins.

**Memorandum opinions are explicitly nonpermanent.** The notice appears before the opinion text and restricts citation. A parser should not mistake the authorities cited inside the memorandum for a reporter citation assigned to the memorandum itself.

**Rules.** The [Reporter of Decisions Office](https://nebraskajudicial.gov/courts/appellate-courts-offices/reporter-decisions-office) explains the official electronic-version transition. [Neb. Ct. R. App. P. § 2-102(E)](https://nebraskajudicial.gov/supreme-court-rules/chapter-2-appeals/article-1-nebraska-court-rules-appellate-practice/%C2%A7-2-102-court-appeals) governs publication and citation of Court of Appeals opinions.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `Neb.` is a prefix of `Neb. App.`.

**(b) Intermediate-court citations are district/division-specific:** **No.** Published Court of Appeals cases use statewide `Neb. App.`.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `N.W.2d` and `N.W.3d` span both courts. The state official reporters distinguish them.

**(d) Court abbreviations contain apostrophes or ordinals:** **No.** Apostrophes may appear in party or firm names, as in `O’Gara`, but not in `Neb.` or `Neb. App.`.

**(e) The same case is commonly cited under supreme-court versus intermediate-court attribution inconsistently:** **Not verified.** Transfer or further review produces separate opinions, but no repeated misattribution of one opinion was established.

#### 7. Not verified

- Quantitative Westlaw or LEXIS prevalence.
- A Nebraska universal neutral citation independent of official volume/page numbers.
- Common attribution drift between the Supreme Court and Court of Appeals.
- Whether every advance-sheet official page remains unchanged at certification.
- A complete permanent citation for the 2025 Court of Appeals cases whose `N.W.3d` pages were still blank in the sourced documents.
- How frequently practitioners cite memorandum web opinions under the exceptions in § 2-102(E).

---

### North Dakota

#### 1. Sources

1. **State v. Wrigley**, North Dakota Supreme Court, 2025 — current `ND`, `N.W.3d`, blank regional pagination, historical `N.D.`, and paragraph pinpoints. [Opinion](https://law.justia.com/cases/north-dakota/supreme-court/2025/20240291.html)
2. **Anne Carlsen Center v. Murphy**, North Dakota Supreme Court, 2025 — current and pending `N.W.3d` forms. [Opinion](https://law.justia.com/cases/north-dakota/supreme-court/2025/20250168.html)
3. **Kraft v. State**, North Dakota Supreme Court, 2025 — dense with recent `N.W.3d` authorities and footnote pinpoints. [Opinion](https://law.justia.com/cases/north-dakota/supreme-court/2025/20250180.html)
4. **State v. Anderson**, North Dakota Supreme Court, 2025 — additional current Supreme Court practice. [Opinion](https://law.justia.com/cases/north-dakota/supreme-court/2025/20250078.html)
5. **Carver v. Miller**, North Dakota Court of Appeals, 1998 — born-digital Court of Appeals opinion using the `ND App` neutral identifier and regional parallel. [Opinion](https://law.justia.com/cases/north-dakota/court-of-appeals/1998/980064.html)

#### 2. Court structure as cited

North Dakota’s public-domain identifiers distinguish:

- **North Dakota Supreme Court:** `ND`
- **North Dakota Court of Appeals:** `ND App`

Examples:

- `2024 ND 233`
- `1998 ND App 12`

The Court of Appeals form is expressly prescribed by Rule 11.6 and demonstrated by actual opinions. No district or division identifier follows `ND App`.

The punctuation distinction is important:

- `ND` without periods is the electronic public-domain court identifier.
- `N.D.` with periods is the historical North Dakota Reports reporter abbreviation.

Rule 11.6 expressly warns about that distinction.

#### 3. Reporters in actual use

**Public-domain system.** North Dakota adopted medium-neutral citation for opinions released on or after **January 1, 1997**. The rule originally took effect March 5, 1997. The exact forms are:

- `YYYY ND N`
- `YYYY ND App N`

Paragraph pinpoints immediately follow the neutral citation, and the North Western parallel follows when available.

**Regional reporters.** Current opinions use `N.W.3d`; prior opinions use `N.W.2d`. A complete modern citation is:

`2024 ND 233, ¶ 8, 14 N.W.3d 898`

**Pending regional pagination.** North Dakota uses three ASCII hyphens in current source text:

`--- N.W.3d ---`

The neutral citation remains complete and permanent even when the regional fields are blank.

**Historical official reporter.** Rule 11.6 states that `N.D.` refers to North Dakota Reports, published from **1890 through 1953**. Historical cases may therefore have both `N.D.` and `N.W.` or `N.W.2d` citations.

**Vendor citations.** Current published opinions use the neutral and regional forms, not Westlaw. No vendor prevalence percentage was established.

#### 4. Verbatim examples

1. **Overbo v. Overbo — regional pagination pending**

   `Overbo v. Overbo, 2024 ND 233, ¶ 7, --- N.W.3d ---`

   Source: *State v. Wrigley*.

2. **City of Fargo v. Roehrich — Supreme Court**

   `City of Fargo v. Roehrich, 2021 ND 145, ¶ 6, 963 N.W.2d 248.`

   Source: *State v. Wrigley*.

3. **State v. Moses — Supreme Court**

   `State v. Moses, 2022 ND 208, ¶ 17, 982 N.W.2d 321`

   Source: *State v. Wrigley*.

4. **State v. Cromwell — historical `N.D.` parallel**

   `State v. Cromwell, 72 N.D. 565, 9 N.W.2d 914 (1943)`

   Source: *State v. Wrigley*.

5. **Roth v. Meyer — pending `N.W.3d`**

   `Roth v. Meyer, 2025 ND 116, ¶ 22, --- N.W.3d ---`

   Source: *Anne Carlsen Center*.

6. **Overbo v. Overbo — later completed regional citation**

   `Overbo v. Overbo, 2024 ND 233, ¶ 8, 14 N.W.3d 898`

   Source: *Anne Carlsen Center*.

7. **Aune v. State — paragraph and footnote pinpoint**

   `Aune v. State, 2024 ND 99, ¶ 6 n.1, 6 N.W.3d 833.`

   Source: *Kraft*.

8. **Almklov v. State — Supreme Court**

   `Almklov v. State, 2025 ND 27, ¶ 6, 17 N.W.3d 583`

   Source: *Kraft*.

9. **State v. Wiese — Supreme Court**

   `State v. Wiese, 2024 ND 39, ¶ 7, 4 N.W.3d 242.`

   Source: *State v. Anderson*.

10. **Carver v. Miller — Court of Appeals**

    `Carver v. Miller, 1998 ND App 12, 585 N.W.2d 139`

    Source: *Carver v. Miller*.

#### 5. Style mechanics

**Neutral citation comes first.**

`2024 ND 233, ¶ 8, 14 N.W.3d 898`

The regional reporter is a parallel, not the jurisdictional anchor.

**Paragraph pinpoint precedes the regional reporter.** The sequence is:

`neutral cite, ¶ pinpoint, regional cite`

A pin such as `¶ 6 n.1` can include a footnote marker before the regional citation.

**Punctuation distinguishes reporter from court.** `N.D.` is a reporter; `ND` is a court/database identifier. Stripping periods before classification would collapse two legally different tokens.

**Pending reporter uses hyphens, not underscores.** Current opinions contain `--- N.W.3d ---`. That variation should be recognized alongside underscore-based pending-publication forms from other states, but the blank regional key must remain unresolved.

**Court of Appeals form is separately sequenced.** `ND App` is not a district of the Supreme Court and should be matched before the shorter `ND` token.

**Rule.** [North Dakota Rule of Court 11.6](https://www.ndcourts.gov/legal-resources/rules/ndrct/11-6) prescribes the neutral formats, paragraph pins, regional parallels, and historical `N.D.` distinction.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **Yes.** `ND` is a literal prefix of `ND App`.

**(b) Intermediate-court citations are district/division-specific:** **No.** `ND App` has no district or division suffix.

**(c) A reporter edition spans multiple courts in the state:** **Yes.** `N.W.2d` contains both Supreme Court and Court of Appeals cases; the rule also contemplates regional parallels for both. The neutral identifier supplies the court.

**(d) Court abbreviations contain apostrophes or ordinals:** **No.** The key punctuation risk is periods versus no periods—`N.D.` against `ND`—rather than apostrophes or ordinals.

**(e) The same case is commonly cited under supreme-court versus intermediate-court attribution inconsistently:** **Not verified.**

#### 7. Not verified

- Recent frequency of North Dakota Court of Appeals sittings or post-1999 `ND App` opinions; the format and actual historical use are verified.
- Quantitative vendor-citation prevalence.
- Common erroneous attribution of one decision to both courts.
- Whether every `--- N.W.3d ---` string is updated in the public electronic opinion after publication.
- Whether any current filings use `NDApp` without a space; no such primary-source form was found.
- Whether first-series `N.W.` is still commonly encountered in born-digital modern briefs, as opposed to opinions citing historical authority.

---

### South Dakota

#### 1. Sources

1. **Earll v. Farmers Mutual Insurance**, South Dakota Supreme Court, 2025 — dense with modern `S.D.`, `N.W.3d`, `N.W.2d`, short forms, and pre-neutral authorities. [Opinion](https://law.justia.com/cases/south-dakota/supreme-court/2025/30732.html)
2. **Weiland v. Bumann**, South Dakota Supreme Court, 2025 — recent `N.W.3d`, `N.W.2d`, `Id.`, and paragraph-pin practice. [Opinion](https://law.justia.com/cases/south-dakota/supreme-court/2025/30309.html)
3. **State v. Tuopeh**, South Dakota Supreme Court, 2025 — current criminal citations and multiple recent `N.W.3d` authorities. [Opinion](https://law.justia.com/cases/south-dakota/supreme-court/2025/30365.html)
4. **Berwald v. Stan’s, Inc.**, South Dakota Supreme Court, 2025 — current `N.W.3d`, older regional citations, and apostrophes in party and organization names. [Opinion](https://law.justia.com/cases/south-dakota/supreme-court/2025/30783.html)
5. **Remington v. Iverson**, South Dakota Supreme Court, 2025 — another current born-digital opinion displaying the official public-domain header. [Opinion](https://law.justia.com/cases/south-dakota/supreme-court/2025/30480.html)

#### 2. Court structure as cited

South Dakota has one state appellate court: the **South Dakota Supreme Court**. There is no intermediate appellate court to encode in a state case citation.

The current public-domain identifier is:

`YYYY S.D. N`

Examples include:

- `2025 S.D. 20`
- `2025 S.D. 9`
- `2025 S.D. 16`

Paragraph pinpoints follow the neutral citation, and the regional parallel follows after that.

For pre-1996 cases without the public-domain identifier, the terminal court parenthetical is `(S.D. <year>)`.

#### 3. Reporters in actual use

**Public-domain citation.** South Dakota’s rule applies to decisions issued on or after **January 1, 1996**. The initial citation uses:

`YYYY S.D. N, ¶ <pin>, <North Western parallel>`

when the regional citation is available.

**Official reporter.** The South Dakota judiciary states that the bound **North Western Reporter** is the official reporter for South Dakota opinions. Current decisions use `N.W.3d`; older decisions use `N.W.2d` and first-series `N.W.`.

**Historical South Dakota Reports.** For cases before the 1996 public-domain system, SDCL 15-26A-69.1 permits citation to South Dakota Reports or the North Western Reporter. Current opinions preserve older forms such as `43 S.D. 106, 178 N.W. 146`.

**Pending publication.** The neutral citation is available immediately, even before the regional reporter. Current sourced examples already have `N.W.3d` pagination; no exact 2025 blank regional form was confirmed in the selected opinions.

**Vendor citations.** Westlaw and LEXIS were not prevalent in the selected Supreme Court opinions. No quantitative rate was established.

#### 4. Verbatim examples

1. **Acuity v. Terra-Tek, LLC — current `N.W.3d`**

   `Acuity v. Terra-Tek, LLC, 2024 S.D. 49, ¶ 13, 11 N.W.3d 96, 100`

   Source: *Earll*.

2. **In re Noem — Supreme Court**

   `In re Noem, 2024 S.D. 11, ¶ 48, 3 N.W.3d 465, 479.`

   Source: *Earll*.

3. **Larimer — short form retaining neutral and regional pins**

   `Larimer, 2019 S.D. 21, ¶ 6, 926 N.W.2d at 475.`

   Source: *Earll*.

4. **Barr v. Cole — `N.W.2d`**

   `Barr v. Cole, 2023 S.D. 60, ¶ 18, 998 N.W.2d 343, 349`

   Source: *Weiland*.

5. **Acuity — same current authority in another opinion**

   `Acuity v. Terra-Tek, LLC, 2024 S.D. 49, ¶ 13, 11 N.W.3d 96, 100.`

   Source: *Weiland*. This occurrence includes the terminal period.

6. **State v. Carter — current third-series citation**

   `State v. Carter, 2023 S.D. 67, ¶ 24, 1 N.W.3d 674, 685`

   Source: *State v. Tuopeh*.

7. **State v. Washington — Supreme Court**

   `State v. Washington, 2024 S.D. 64, ¶ 69, 13 N.W.3d 492, 512.`

   Source: *State v. Tuopeh*.

8. **Stock v. Garrett — no paragraph pinpoint in this occurrence**

   `Stock v. Garrett, 2025 S.D. 8, 17 N.W.3d 856`

   Source: *Berwald*.

9. **Wegner v. Siemers — full pinpoint run**

   `Wegner v. Siemers, 2018 S.D. 76, ¶ 4, 920 N.W.2d 54, 55`

   Source: *Berwald*.

10. **International Union of Operating Engineers — pre-neutral citation**

    `Int’l Union of Operating Eng’rs v. Aberdeen Sch. Dist., 463 N.W.2d 843, 844 (S.D. 1990)`

    Source: *Berwald*.

#### 5. Style mechanics

**Neutral citation plus paragraph plus regional reporter.** The canonical modern structure is:

`2024 S.D. 49, ¶ 13, 11 N.W.3d 96, 100`

The public-domain identifier and regional citation are separate records; the paragraph and final page are pinpoints.

**The regional reporter is officially authoritative but not jurisdictionally sufficient across the seven-state family.** Within South Dakota there is only one state appellate court, but a bare `N.W.3d` citation remains multistate and cannot identify South Dakota without a parenthetical, neutral citation, case metadata, or other context.

**Short forms may preserve both pinpoint systems.**

`Larimer, 2019 S.D. 21, ¶ 6, 926 N.W.2d at 475.`

The regional first page is absent and must come from the full antecedent.

**Pre-1996 form.** Older citations can consist solely of `N.W.2d` plus `(S.D. year)`, or may include a South Dakota Reports parallel. The neutral system must not be expected for historical opinions.

**Paragraph notation.** Current opinions use `¶` and `¶¶`; no reporter-page `at` is needed for the neutral component, though `at` remains in regional-reporter short forms.

**Rule.** [SDCL 15-26A-69.1](https://sdlegislature.gov/Statutes/15-26A-69.1) prescribes the post-1995 citation system and treatment of older cases. The judiciary’s [Opinions page](https://ujs.sd.gov/Supreme_Court/CurrentTerm.aspx) identifies the North Western Reporter as the official bound reporter.

#### 6. Risk flags

**(a) Supreme-court abbreviation prefix-collides with an intermediate court:** **No.** South Dakota has no state intermediate appellate court.

**(b) Intermediate-court citations are district/division-specific:** **Not applicable.**

**(c) A reporter edition spans multiple courts in the state:** **No for current state appellate courts**, because South Dakota has only its Supreme Court. However, `N.W.2d` and `N.W.3d` are multistate reporters, so a bare citation remains jurisdictionally ambiguous across states.

**(d) Court abbreviations contain apostrophes or ordinals:** **No in `S.D.`.** Typographic apostrophes occur in case names and entity abbreviations, including `Int’l` and `Eng’rs`.

**(e) The same case is commonly cited under supreme-court versus intermediate-court attribution inconsistently:** **Not applicable.**

#### 7. Not verified

- A current born-digital example with `2025 S.D. N` and blank `N.W.3d` pagination.
- Quantitative vendor-citation prevalence.
- Whether every pre-1996 case with an available `S.D.` reporter citation is routinely given that parallel in current filings.
- A separate court-issued citation manual beyond SDCL 15-26A-69.1.
- Whether nonopinion Supreme Court orders receive the same public-domain sequence.
- Any state intermediate appellate body whose decisions could be confused with `S.D.`; none was identified.


---

## Batch 7 — P.3d family

**States covered:** Arizona, Washington, Colorado, Oregon, Oklahoma, Kansas, New Mexico, Utah, Nevada, Idaho, Montana, Wyoming, Alaska, and Hawaiʻi.

The cited opinions are searchable, born-digital documents. Exact examples preserve source punctuation, spacing, apostrophes, reporter styling, blanks, and apparent text-layer irregularities.

---

### Arizona

#### 1. Sources

1. [Montenegro v. Fontes](https://law.justia.com/cases/arizona/supreme-court/2025/cv-24-0328-ap-el.html), Arizona Supreme Court, 2025.
2. [State v. Larriba-Tucker](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cr-24-0365.html), Court of Appeals, Division One, 2025.
3. [Hamlet v. State](https://law.justia.com/cases/arizona/court-of-appeals-division-two-published/2025/2-ca-cv-2024-0162.html), Court of Appeals, Division Two, 2025.
4. [Carson v. Gentry](https://law.justia.com/cases/arizona/supreme-court/2025/cv-24-0286-pr.html), Arizona Supreme Court, 2025.
5. [Garibay v. Fox](https://law.justia.com/cases/arizona/supreme-court/2025/cv-24-0292-pr.html), Arizona Supreme Court, 2025.
6. [Pruitt v. State](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cv-24-0407.html), Division One.
7. [Desert Mountain Energy Corp. v. Flagstaff](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cv-24-0448.html), Division One.
8. [State v. Crowe](https://law.justia.com/cases/arizona/court-of-appeals-division-two-published/2025/2-ca-cr-2024-0022.html), Division Two.
9. [State v. Clem](https://law.justia.com/cases/arizona/court-of-appeals-division-two-published/2025/2-ca-cr-2024-0097.html), Division Two.
10. [Arizona appellate-opinions and official-reports information](https://www.azcourts.gov/opinions), including the warning that only the bound Arizona Reports are the final official text.

#### 2. Court structure as cited

Arizona has the **Arizona Supreme Court** and a statewide **Arizona Court of Appeals** divided into **Division One** and **Division Two**. The divisions appear in opinion headings and docket numbers—`1 CA-...` and `2 CA-...`—but ordinary bound citations generally distinguish only Supreme Court from Court of Appeals:

- Supreme Court: `Ariz.` followed by a year-only parenthetical.
- Court of Appeals: `Ariz.` followed by `(App. <year>)`.

Regional-only or externally styled citations may instead use `(Ariz.)` and `(Ariz. Ct. App.)`. The routine local reporter form does not include `Div. 1` or `Div. 2`.

#### 3. Reporters in actual use

**Arizona Reports** remains the official reporter for both appellate levels. The Court of Appeals level is identified through `(App.)`, not a separate `Ariz. App.` reporter. The courts caution that slip opinions remain subject to correction and that the bound Arizona Reports contain the final official text.

`P.2d` and `P.3d` appear both as parallels and, for recent decisions not yet carrying Arizona Reports pagination, as the only reporter citation. In the latter situation, the parenthetical commonly carries the full court:

`573 P.3d 65, 70 ¶ 21 (Ariz. 2025)`

Modern Arizona opinions use numbered paragraphs, but Arizona has not adopted a permanent `YYYY-AZ-N`-type case identifier.

Westlaw and LEXIS occur for unpublished or not-yet-reported authorities, but the selected published opinions principally use `Ariz.` and `P.3d`.

#### 4. Verbatim examples

1. **Roundtree v. City of Page — Supreme Court, regional-only**

   `Roundtree v. City of Page, 573 P.3d 65, 70 ¶ 21 (Ariz. 2025).`

   Source: [Montenegro v. Fontes](https://law.justia.com/cases/arizona/supreme-court/2025/cv-24-0328-ap-el.html).

2. **State v. West — Supreme Court official reporter**

   `State v. West, 226 Ariz. 559, 562, ¶ 15 (2011).`

   Source: [State v. Larriba-Tucker](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cr-24-0365.html).

3. **State v. Girdler — Supreme Court**

   `State v. Girdler, 138 Ariz. 482, 488 (1983).`

   Source: [State v. Larriba-Tucker](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cr-24-0365.html).

4. **State v. Stuard — Supreme Court**

   `State v. Stuard, 176 Ariz. 589, 603 (1993)`

   Source: [State v. Crowe](https://law.justia.com/cases/arizona/court-of-appeals-division-two-published/2025/2-ca-cr-2024-0022.html).

5. **State v. Stroud — Supreme Court, paragraph pinpoint**

   `State v. Stroud, 209 Ariz. 410, 411, ¶ 6 (2005).`

   Source: [State v. Clem](https://law.justia.com/cases/arizona/court-of-appeals-division-two-published/2025/2-ca-cr-2024-0097.html).

6. **State v. Sanchez — Court of Appeals**

   `181 Ariz. 492, 495 (App. 1995)`

   Source: [State v. Larriba-Tucker](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cr-24-0365.html).

7. **White v. State — Court of Appeals, regional-only publication period**

   `White v. State, 259 Ariz. 310, ¶ 4 (App. 2025).`

   Source: [Pruitt v. State](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cv-24-0407.html).

8. **Turbin v. Superior Court — Court of Appeals**

   `Turbin v. Superior Court, 165 Ariz. 195, 196 (App. 1990)`

   Source: [Hamlet v. State](https://law.justia.com/cases/arizona/court-of-appeals-division-two-published/2025/2-ca-cv-2024-0162.html).

9. **State ex rel. Romley v. Superior Court — Court of Appeals, named label**

   `State ex rel. Romley v. Superior Court (Romley), 184 Ariz. 223, 225 (App. 1995).`

   Source: [Hamlet v. State](https://law.justia.com/cases/arizona/court-of-appeals-division-two-published/2025/2-ca-cv-2024-0162.html).

10. **Skaggs v. Fink — Court of Appeals**

    `Skaggs v. Fink, 256 Ariz. 437, ¶ 5 (App. 2023)`

    Source: [Carson v. Gentry](https://law.justia.com/cases/arizona/supreme-court/2025/cv-24-0286-pr.html).

#### 5. Style mechanics

Arizona’s local form relies on the **official reporter plus `(App.)`** to identify the intermediate court. That means `Ariz.` itself spans both levels.

Modern pinpoints use `¶`. A regional-only citation may combine a reporter-page pin and a paragraph pin, as in `70 ¶ 21`.

Division identity is prominent in the opinion’s docket and masthead but normally disappears from later case citations. A parser should not infer that `(App.)` means Division One merely because Division One publishes more decisions.

The state does not place the court parenthetical before the citation and does not normally require multiple parallel reporters.

#### 6. Risk flags

**(a) Prefix collision:** **Potentially yes.** In regional-only or Bluebook-oriented forms, `(Ariz.)` is the state prefix of `(Ariz. Ct. App.)`. In dominant local official-reporter form, the more immediate problem is that `Ariz.` covers both levels and `(App.)` supplies the distinction.

**(b) District/division-specific intermediate citations:** **Not ordinarily.** Division One and Division Two are real courts for administration and docketing, but ordinary reported citations generally use only `(App.)`.

**(c) Reporter edition spans multiple courts:** **Yes.** `Ariz.`, `P.2d`, and `P.3d` all occur in both Supreme Court and Court of Appeals decisions.

**(d) Apostrophes or ordinals in court abbreviations:** **No in the ordinary citation parenthetical.** Division headings use `Division One` and `Division Two`, rather than `1st` or `2d`.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified as a common practice.**

#### 7. Not verified

- A permanent Arizona neutral/public-domain case identifier.
- Quantitative Westlaw or LEXIS prevalence.
- Routine inclusion of Division One or Division Two in filed-brief parentheticals.
- Common attribution of one identical opinion to both appellate levels.
- Whether all recent P.3d-only citations are later replaced in every online copy by Arizona Reports pagination.

---

### Washington

#### 1. Sources

1. [In re Recall of Vet Voice Foundation](https://law.justia.com/cases/washington/supreme-court/2025/103510-0.html), Washington Supreme Court.
2. [State v. Erickson](https://law.justia.com/cases/washington/supreme-court/2025/102322-5.html), Supreme Court.
3. [State v. Lewis](https://law.justia.com/cases/washington/supreme-court/2025/103044-2.html), Supreme Court.
4. [Nelson v. Duvall](https://law.justia.com/cases/washington/supreme-court/2025/102894-4.html), Supreme Court.
5. [State v. Osborn](https://law.justia.com/cases/washington/court-of-appeals-division-i/2025/85723-7.html), Court of Appeals, Division I.
6. [Bain v. Metropolitan Mortgage Group, Inc.](https://law.justia.com/cases/washington/court-of-appeals-division-iii/2025/39761-8.html), Division III.
7. [State v. Celestine](https://law.justia.com/cases/washington/court-of-appeals-division-ii/2025/58364-1.html), Division II.
8. [Washington Reporter of Decisions style sheet](https://www.courts.wa.gov/appellate_trial_courts/supreme/?fa=atc_supreme.style), including current official-and-regional parallel rules.

#### 2. Court structure as cited

Washington has the **Washington Supreme Court** and a **Washington Court of Appeals** with Divisions I, II, and III. The official reporter tokens distinguish court level:

- Supreme Court: `Wn.2d` and now `Wn.3d`.
- Court of Appeals: `Wn. App.` and `Wn. App. 2d`.

The division is normally absent from the reported citation even though it appears in the opinion heading and docket.

#### 3. Reporters in actual use

Washington continues to use active state-specific official reporters and supplies the Pacific Reporter as a parallel. Current Supreme Court decisions may appear in `Wn.3d`; current intermediate decisions appear in `Wn. App. 2d`. Older series remain heavily cited.

The usual form is:

`official reporter first page, official pin, P.3d first page (year)`

The official style sheet directs the writer to use the official Washington reporter when available and to include the Pacific parallel. There is no permanent `YYYY-WA-N` neutral case identifier.

Vendor citations principally appear for unpublished decisions, which also carry a docket number and court/date parenthetical.

#### 4. Verbatim examples

1. **State v. Stevens — Supreme Court**

   `State v. Stevens, 158 Wn.2d 304, 309-10, 143 P.3d 817 (2006).`

   Source: [State v. Erickson](https://law.justia.com/cases/washington/supreme-court/2025/102322-5.html).

2. **State v. Hundley — Supreme Court**

   `State v. Hundley, 126 Wn.2d 418, 421, 895 P.2d 403 (1995)`

   Source: [State v. Lewis](https://law.justia.com/cases/washington/supreme-court/2025/103044-2.html).

3. **State v. Hutton — Court of Appeals**

   `State v. Hutton, 7 Wn. App. 726, 731-32, 502 P.2d 1037 (1972)`

   Source: [State v. Osborn](https://law.justia.com/cases/washington/court-of-appeals-division-i/2025/85723-7.html).

4. **State v. Jones — Court of Appeals**

   `State v. Jones, 140 Wn. App. 431, 437-38, 166 P.3d 782 (2007)`

   Source: [State v. Celestine](https://law.justia.com/cases/washington/court-of-appeals-division-ii/2025/58364-1.html).

5. **In re Personal Restraint of Arntsen — Supreme Court, `Wn.3d`**

   `In re Pers. Restraint of Arntsen, 2 Wn.3d 716, 724, 543 P.3d 821 (2024).`

   Source: [In re Recall of Vet Voice Foundation](https://law.justia.com/cases/washington/supreme-court/2025/103510-0.html).

6. **State v. Stalker — Court of Appeals**

   `State v. Stalker, 152 Wn. App. 805, 810-11, 219 P.3d 722 (2009)`

   Source: [State v. Osborn](https://law.justia.com/cases/washington/court-of-appeals-division-i/2025/85723-7.html).

7. **Preserve Agricultural Lands v. Adams County — Supreme Court**

   `Pres. Agric. Lands v. Adams County, 128 Wn.2d 869, 882, 913 P.2d 793 (1996).`

   Source: [Bain](https://law.justia.com/cases/washington/court-of-appeals-division-iii/2025/39761-8.html).

8. **Scott’s Excavating Vancouver, LLC v. Winlock Properties, LLC — Court of Appeals**

   `Scott’s Excavating Vancouver, LLC v. Winlock Props., LLC, 176 Wn. App. 335, 341-42, 308 P.3d 791 (2013).`

   Source: [Bain](https://law.justia.com/cases/washington/court-of-appeals-division-iii/2025/39761-8.html).

9. **State v. Zwald — source omission of reporter period**

   `State v. Zwald, 32 Wn App. 2d 62, 69, 555 P.3d 467 (2024).`

   Source: [State v. Celestine](https://law.justia.com/cases/washington/court-of-appeals-division-ii/2025/58364-1.html). The absence of a period after `Wn` is preserved.

10. **State v. Yishmael — Court of Appeals and affirmance history**

    `State v. Yishmael, 6 Wn. App. 2d 203, 213, 430 P.3d 279 (2018), aff’d, 195 Wn.2d 155, 456 P.3d 1172 (2020).`

    Source: [Nelson v. Duvall](https://law.justia.com/cases/washington/supreme-court/2025/102894-4.html).

#### 5. Style mechanics

Washington’s routine parallel run gives only the official reporter’s pinpoint. The Pacific citation generally supplies its first page but not a duplicate pin.

The reporter abbreviation itself identifies court level; no separate `(Wash. Ct. App.)` parenthetical is needed in ordinary local citations.

Divisions I–III are not carried into `Wn. App.` or `Wn. App. 2d` citations. Unpublished citations may include the division through source metadata or a court/date parenthetical, but that is not the normal reported form.

The selected source also proves punctuation drift: `Wn App. 2d` occurs without the expected period after `Wn`.

#### 6. Risk flags

**(a) Prefix collision:** **Yes at reporter-token level.** `Wn.` is the beginning of `Wn. App.`; full-edition matching is required.

**(b) District/division-specific intermediate citations:** **No in ordinary reported citations.** The court has three divisions, but the official reporter does not encode them.

**(c) Reporter edition spans multiple courts:** `P.2d` and `P.3d` **do**; the state-specific official reporter editions do not.

**(d) Apostrophes or ordinals in court abbreviations:** **No.** Division labels use Roman numerals outside the reporter token. Typographic apostrophes appear in party names and history signals such as `aff’d`.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- A Washington neutral/public-domain case identifier.
- Quantitative vendor-citation prevalence.
- Routine use of division-specific parentheticals in filed briefs.
- Common attribution drift between Supreme Court and Court of Appeals.
- Whether every source-level punctuation error such as `Wn App.` survives into the certified official version.

---

### Colorado

#### 1. Sources

1. [Willis v. Twin Shores Master Owners Ass’n](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html), Colorado Court of Appeals.
2. [Snedeker v. People](https://law.justia.com/cases/colorado/supreme-court/2025/24sc154.html), Colorado Supreme Court.
3. [Jefferson County Board of Equalization v. Dozier](https://law.justia.com/cases/colorado/supreme-court/2025/24sc553.html), Supreme Court.
4. [Ramirez v. KLM](https://law.justia.com/cases/colorado/court-of-appeals/2025/23ca2044.html), Court of Appeals.
5. [O’Connell v. Biomet](https://law.justia.com/cases/colorado/supreme-court/2025/23sc961.html), Supreme Court.
6. [Colorado neutral-citation information](https://www.coloradojudicial.gov/courts/supreme-court/opinions), covering `CO` and `COA`.

#### 2. Court structure as cited

Colorado uses permanent public-domain identifiers:

- **Colorado Supreme Court:** `YYYY CO N`
- **Colorado Court of Appeals:** `YYYY COA N`

The Court of Appeals decides cases in panels, but the neutral citation does not contain a panel, division, or district number. Older regional-only cases distinguish the levels with `(Colo.)` and `(Colo. App.)`.

#### 3. Reporters in actual use

The `CO` and `COA` public-domain formats apply to opinions issued on or after **January 1, 2012**. Pinpoints use numbered paragraphs. A Pacific Reporter parallel may follow, but the neutral identifier itself is complete and supplies the deciding court.

Older decisions and some current references use `P.2d` or `P.3d` with `(Colo.)` or `(Colo. App.)`. `P.3d` spans both courts.

Colorado once had state-specific official reports, but the exact final volumes and cessation dates were not confirmed from the primary materials reviewed here. Modern sourced practice is neutral citation plus paragraph pinpoints, often with a Pacific parallel.

#### 4. Verbatim examples

1. **Willis v. Twin Shores — Court of Appeals header**

   `2025COA37`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html). The opinion header omits spaces in this rendering.

2. **South Cross Ranches, LLC v. JBC Agricultural Management, LLC — Court of Appeals**

   `S. Cross Ranches, LLC v. JBC Agric. Mgmt., LLC, 2019 COA 58, ¶ 11.`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html).

3. **Lakeview Associates, Ltd. v. Maes — Supreme Court, regional-only**

   `Lakeview Assocs., Ltd. v. Maes, 907 P.2d 580, 583-84 (Colo. 1995).`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html).

4. **Ruiz v. Chappell — Court of Appeals**

   `Ruiz v. Chappell, 2020 COA 22, ¶ 8.`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html).

5. **Stanczyk v. Poudre School District R-1 — modified neutral identifier and affirmance**

   `Stanczyk v. Poudre Sch. Dist. R-1, 2020 COA 27M, ¶ 51, aff’d on other grounds, 2021 CO 57.`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html).

6. **Jordan v. Panorama Orthopedics & Spine Center, PC — Supreme Court**

   `Jordan v. Panorama Orthopedics & Spine Ctr., PC, 2015 CO 24, ¶ 18.`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html).

7. **Henderson v. Master Klean Janitorial, Inc. — older Court of Appeals**

   `Henderson v. Master Klean Janitorial, Inc., 70 P.3d 612, 615 (Colo. App. 2003);`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html). The source’s semicolon is preserved.

8. **Wycoff v. Grace Community Church of Assemblies of God — Court of Appeals**

   `Wycoff v. Grace Cmty. Church of Assemblies of God, 251 P.3d 1260, 1267-68 (Colo. App. 2010)`

   Source: [Willis](https://law.justia.com/cases/colorado/court-of-appeals/2025/24ca0593.html).

9. **Tancrede v. Freund — Court of Appeals**

   `Tancrede v. Freund, 2017 COA 36, ¶ 7.`

   Source: [Ramirez v. KLM](https://law.justia.com/cases/colorado/court-of-appeals/2025/23ca2044.html).

10. **Pulsifer v. Pueblo Professional Contractors, Inc. — Supreme Court**

    `Pulsifer v. Pueblo Professional Contractors, Inc., 161 P.3d 656 (Colo. 2007)`

    Source: [Snedeker v. People](https://law.justia.com/cases/colorado/supreme-court/2025/24sc154.html).

#### 5. Style mechanics

`CO` and `COA` are complete reporter-like identifiers. A regional parallel is not needed to determine the court.

Modified or corrected opinions can add a letter to the neutral number, as in `2020 COA 27M`.

Paragraph pinpoints precede any later history. A citation such as `2020 COA 27M, ¶ 51, aff’d ...` contains two distinct neutral citations to separate opinions.

Older `P.3d` citations remain common and require `(Colo.)` or `(Colo. App.)`.

#### 6. Risk flags

**(a) Prefix collision:** **Yes—directly.** `CO` is a literal prefix of `COA`.

**(b) District/division-specific intermediate citations:** **No.** Court of Appeals panels are not encoded in `COA`.

**(c) Reporter edition spans multiple courts:** `P.3d` **yes**; `CO` and `COA` are court-specific.

**(d) Apostrophes or ordinals in court abbreviations:** **No.** Letter suffixes such as `M` can occur after the opinion number.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- Exact cessation dates and final volumes of Colorado’s historical state-specific reporters.
- Quantitative Westlaw/LEXIS use.
- Common attribution drift between `CO` and `COA`.
- Whether every amended opinion suffix follows one closed set beyond the observed `M`.
- Routine use of panel or division identifiers in practitioner parentheticals.

---

### Oregon

#### 1. Sources

1. [Jared v. Harmon](https://law.justia.com/cases/oregon/supreme-court/2025/s070652.html), Oregon Supreme Court.
2. [Long v. Board of Parole](https://law.justia.com/cases/oregon/supreme-court/2025/s071146.html), Supreme Court.
3. [Perkett v. Burrows](https://law.justia.com/cases/oregon/court-of-appeals/2025/a180054.html), Oregon Court of Appeals.
4. [State v. Skotland](https://law.justia.com/cases/oregon/court-of-appeals/2025/a176291.html), Court of Appeals.
5. [State v. Ortiz](https://law.justia.com/cases/oregon/court-of-appeals/2025/a175738.html), Court of Appeals.
6. [State v. Wilcox](https://law.justia.com/cases/oregon/supreme-court/2025/s071582.html), Supreme Court.
7. [Oregon appellate style manual and advance sheets](https://www.courts.oregon.gov/publications/Pages/default.aspx).

#### 2. Court structure as cited

Oregon uses separate state reporters:

- **Oregon Supreme Court:** `Or`
- **Oregon Court of Appeals:** `Or App`

The Court of Appeals is cited statewide. No district or division identifier appears in the reported citation.

The official reporter token itself identifies court level, so the final parenthetical is usually only the year.

#### 3. Reporters in actual use

`Or` and `Or App` remain active. Current opinions carry “Cite as” headers such as:

- `Cite as 374 Or 381 (2025)`
- `Cite as 345 Or App 16 (2025)`

Oregon supplies `P2d` or `P3d` as regional parallels and omits periods in those reporter abbreviations. A typical citation is:

`372 Or 319, 549 P3d 534 (2024)`

There is no permanent `YYYY-OR-N` neutral identifier. Pending cases can appear as:

`___ Or ___, ___ P3d ___ (<date>)`

#### 4. Verbatim examples

1. **Jared v. Harmon — Supreme Court citation header**

   `Cite as 374 Or 381 (2025)`

   Source: [Jared v. Harmon](https://law.justia.com/cases/oregon/supreme-court/2025/s070652.html).

2. **Perkett v. Burrows — Court of Appeals citation header**

   `Cite as 345 Or App 16 (2025)`

   Source: [Perkett](https://law.justia.com/cases/oregon/court-of-appeals/2025/a180054.html).

3. **Indian Ridge I, LLC v. Lenahan — Court of Appeals**

   `Indian Ridge I, LLC v. Lenahan, 314 Or App 715, 721, 497 P3d 806 (2021)`

   Source: [Perkett](https://law.justia.com/cases/oregon/court-of-appeals/2025/a180054.html).

4. **State v. Gaines — Supreme Court**

   `State v. Gaines, 346 Or 160, 171-72, 206 P3d 1042 (2009).`

   Source: [Perkett](https://law.justia.com/cases/oregon/court-of-appeals/2025/a180054.html).

5. **State v. Skotland — Supreme Court**

   `State v. Skotland, 372 Or 319, 549 P3d 534 (2024)`

   Source: [State v. Skotland](https://law.justia.com/cases/oregon/court-of-appeals/2025/a176291.html).

6. **State v. Skotland — Court of Appeals and reversal history**

   `State v. Skotland, 326 Or App 469, 533 P3d 55 (2023), rev’d, 372 Or 319, 549 P3d 534 (2024)`

   Source: [State v. Skotland](https://law.justia.com/cases/oregon/court-of-appeals/2025/a176291.html).

7. **State v. Ortiz — Court of Appeals and Supreme Court reversal**

   `Ortiz, 325 Or App 134, 135, 528 P3d 795 (2023), rev’d, 372 Or 658, 554 P3d 796 (2024) (Ortiz I).`

   Source: [State v. Ortiz](https://law.justia.com/cases/oregon/court-of-appeals/2025/a175738.html).

8. **State v. Maciel-Figueroa — Supreme Court**

   `State v. Maciel-Figueroa, 361 Or 163, 165, 389 P3d 1121 (2017).`

   Source: [State v. Hlebechuk](https://law.justia.com/cases/oregon/court-of-appeals/2025/a179481.html).

9. **State v. Castilleja — Supreme Court with reconsideration history**

   `State v. Castilleja, 345 Or 255, 264, 192 P3d 1283, adh’d to on recons, 345 Or 473, 198 P3d 937 (2008).`

   Source: [State v. Wilcox](https://law.justia.com/cases/oregon/supreme-court/2025/s071582.html).

10. **Kragt v. Board of Parole — pending publication**

    `Kragt v. Board of Parole, ___ Or ___, ___ P3d ___ (Jan 16, 2025)`

    Source: [Long v. Board of Parole](https://law.justia.com/cases/oregon/supreme-court/2025/s071146.html).

#### 5. Style mechanics

Oregon omits periods from `P2d` and `P3d`.

A full parallel normally carries the official first page and any pin before the regional first page. Some citations provide a pin only for the official reporter.

Court hierarchy is encoded by `Or` versus `Or App`; the year-only parenthetical carries no independent court information.

Procedural history can contain two separate official-and-regional runs, as in the *Skotland* and *Ortiz* examples.

#### 6. Risk flags

**(a) Prefix collision:** **Yes.** `Or` is a literal prefix of `Or App`.

**(b) District/division-specific intermediate citations:** **No.**

**(c) Reporter edition spans multiple courts:** `P2d` and `P3d` **yes**; `Or` and `Or App` do not.

**(d) Apostrophes or ordinals in court abbreviations:** **No.** Apostrophes occur in history signals such as `rev’d` and `adh’d`.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.** Same-caption decisions at both levels are normally distinguished through complete procedural history.

#### 7. Not verified

- A statewide Oregon neutral citation.
- Quantitative vendor-citation use.
- Common court-attribution drift.
- Whether every pending blank citation is retroactively updated online.
- Any district or division form used for Oregon’s Court of Appeals.

---

### Oklahoma

#### 1. Sources

1. [Flintco, LLC v. Southroads Mall](https://law.justia.com/cases/oklahoma/supreme-court/2025/121387.html), Oklahoma Supreme Court.
2. [Black Emergency Response Team v. Drummond](https://law.justia.com/cases/oklahoma/supreme-court/2025/122370.html), Supreme Court.
3. [Snyder v. Smith](https://law.justia.com/cases/oklahoma/court-of-appeals-civil/2025/122288.html), Court of Civil Appeals, Division III.
4. [Parson v. State](https://law.justia.com/cases/oklahoma/court-of-appeals-civil/2025/121464.html), Court of Civil Appeals, Division I.
5. [Wonsch v. State](https://law.justia.com/cases/oklahoma/court-of-appeals-civil/2025/121868.html), Court of Civil Appeals, Division II.
6. [Mitchell v. State](https://law.justia.com/cases/oklahoma/court-of-criminal-appeals/2025/f-2024-321.html), Court of Criminal Appeals.
7. [Oklahoma citation-rule adoption order](https://www.oscn.net/applications/oscn/DeliverDocument.asp?CiteID=438448), establishing the official public-domain system.
8. [Oklahoma Court of Criminal Appeals citation rule](https://oklahoma.gov/content/dam/ok/en/oids/documents/occa-rules.pdf).

#### 2. Court structure as cited

Oklahoma has three appellate destinations with distinct public-domain identifiers:

- **Oklahoma Supreme Court:** `OK`
- **Oklahoma Court of Civil Appeals:** `OK CIV APP`
- **Oklahoma Court of Criminal Appeals:** `OK CR`

The Court of Civil Appeals has numbered divisions, and the division appears in the opinion heading. It does not normally appear in the public-domain citation.

#### 3. Reporters in actual use

Oklahoma adopted public-domain citation for opinions issued after **May 1, 1997**, with mandatory use beginning **January 1, 1998**. Published opinions receive numbered paragraphs and a Pacific Reporter parallel when available.

The exact formats are:

- `YYYY OK N`
- `YYYY OK CIV APP N`
- `YYYY OK CR N`

`P.2d` and `P.3d` span all three appellate courts. The public-domain identifier therefore supplies the decisive court signal.

Vendor citations are used for unpublished dispositions or while a regional citation is unavailable.

#### 4. Verbatim examples

1. **Flintco, LLC v. Southroads Mall — Supreme Court**

   `2025 OK 35`

   Source: [Flintco](https://law.justia.com/cases/oklahoma/supreme-court/2025/121387.html).

2. **Black Emergency Response Team v. Drummond — Supreme Court**

   `2025 OK 44`

   Source: [Black Emergency Response Team](https://law.justia.com/cases/oklahoma/supreme-court/2025/122370.html).

3. **Snyder v. Smith — Court of Civil Appeals**

   `2025 OK CIV APP 36`

   Source: [Snyder](https://law.justia.com/cases/oklahoma/court-of-appeals-civil/2025/122288.html).

4. **Parson v. State — Court of Civil Appeals**

   `2025 OK CIV APP 10`

   Source: [Parson](https://law.justia.com/cases/oklahoma/court-of-appeals-civil/2025/121464.html).

5. **Wonsch v. State — Court of Civil Appeals**

   `2025 OK CIV APP 22`

   Source: [Wonsch](https://law.justia.com/cases/oklahoma/court-of-appeals-civil/2025/121868.html).

6. **Mitchell v. State — Court of Criminal Appeals**

   `2025 OK CR 20`

   Source: [Mitchell](https://law.justia.com/cases/oklahoma/court-of-criminal-appeals/2025/f-2024-321.html).

7. **Oklahoma Gas & Electric Co. v. Oklahoma Corporation Commission — full parallel**

   `Oklahoma Gas & Electric Co. v. Oklahoma Corp. Comm'n, 2025 OK 15, 565 P.3d 418`

   Source: [Oklahoma Electric Cooperative v. Oklahoma Corporation Commission](https://law.justia.com/cases/oklahoma/supreme-court/2025/121909.html).

8. **Musonda v. State — official criminal-court rule model**

   `Musonda v. State, 2019 OK CR 1, 435 P.3d 694.`

   Source: [Oklahoma Court of Criminal Appeals citation rule](https://oklahoma.gov/content/dam/ok/en/oids/documents/occa-rules.pdf).

9. **Musonda — paragraph and regional pin model**

   `Musonda v. State, 2019 OK CR 1, ¶ 7, 435 P.3d 694, 696.`

   Source: [Oklahoma Court of Criminal Appeals citation rule](https://oklahoma.gov/content/dam/ok/en/oids/documents/occa-rules.pdf).

10. **Turner v. State — Court of Criminal Appeals**

    `2025 OK CR 18`

    Source: [Turner v. State](https://law.justia.com/cases/oklahoma/court-of-criminal-appeals/2025/f-2024-848.html).

#### 5. Style mechanics

The public-domain identifier comes before the Pacific parallel, and paragraph pins intervene between them.

The Court of Civil Appeals’ division number is not encoded in `OK CIV APP`. A citation can therefore establish the intermediate court without establishing Division I, II, III, or IV.

`OK` must not be accepted before testing for the longer `OK CIV APP` and `OK CR` forms.

The apostrophe in `Comm'n` occurs in the party or agency abbreviation, not the court identifier.

#### 6. Risk flags

**(a) Prefix collision:** **Yes—strongly.** `OK` is a prefix of `OK CIV APP` and shares the initial state token with `OK CR`.

**(b) District/division-specific intermediate citations:** **No in the neutral citation.** Civil Appeals divisions are real but omitted.

**(c) Reporter edition spans multiple courts:** **Yes.** `P.2d` and `P.3d` span the Supreme Court, Civil Appeals, and Criminal Appeals.

**(d) Apostrophes or ordinals in court abbreviations:** **No.** Division numbers occur only in headings; apostrophes occur in entity names such as `Comm'n`.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- Quantitative vendor-citation use.
- Common attribution drift between `OK`, `OK CIV APP`, and `OK CR`.
- Whether practitioners routinely add civil-appeals division information in explanatory parentheticals.
- A closed list of every suffix used for corrected, withdrawn, or modified Oklahoma public-domain opinions.
- Whether every unpublished civil disposition receives a stable publicly citable vendor identifier.

---

### Kansas

#### 1. Sources

1. [State v. Barnes](https://law.justia.com/cases/kansas/supreme-court/2025/125739.html), Kansas Supreme Court.
2. [Zaragoza v. Board of Johnson County Commissioners](https://law.justia.com/cases/kansas/supreme-court/2025/126732.html), Supreme Court.
3. [State v. Thille](https://law.justia.com/cases/kansas/supreme-court/2025/124495.html), Supreme Court.
4. [State v. Johnson](https://law.justia.com/cases/kansas/supreme-court/2025/126626.html), Supreme Court.
5. [State v. Hollins](https://law.justia.com/cases/kansas/supreme-court/2025/126348.html), Supreme Court.
6. [Johnson v. Bass Pro Outdoor World](https://law.justia.com/cases/kansas/supreme-court/2025/126314.html), Supreme Court.
7. [State v. Ervin](https://law.justia.com/cases/kansas/supreme-court/2025/126747.html), Supreme Court.
8. [State v. Zaragoza](https://law.justia.com/cases/kansas/court-of-appeals/2024/125833.html), Kansas Court of Appeals.

#### 2. Court structure as cited

Kansas uses separate official reporters:

- **Kansas Supreme Court:** `Kan.`
- **Kansas Court of Appeals:** `Kan. App. 2d`

The Court of Appeals is cited statewide, without a district or division parenthetical. A final year-only parenthetical is enough because the reporter identifies the court.

#### 3. Reporters in actual use

`Kan.` and `Kan. App. 2d` remain active official reporter forms. `P.3d` is routinely included as a parallel:

`318 Kan. 338, 351, 543 P.3d 508 (2024)`

`P.3d` spans both appellate levels. Kansas has not adopted a permanent `YYYY-KS-N` public-domain case identifier for reported opinions.

Unpublished Court of Appeals decisions use a docket number, Westlaw citation, star pin, and `(Kan. App. <date>)`.

#### 4. Verbatim examples

1. **State v. Showalter — Supreme Court**

   `State v. Showalter, 318 Kan. 338, 351, 543 P.3d 508 (2024)`

   Source: [State v. Ervin](https://law.justia.com/cases/kansas/supreme-court/2025/126747.html).

2. **State v. Dupree — Supreme Court**

   `State v. Dupree, 304 Kan. 43, 65, 371 P.3d 862 (2016)`

   Source: [State v. Barnes](https://law.justia.com/cases/kansas/supreme-court/2025/125739.html).

3. **State v. Zeiner — Supreme Court**

   `State v. Zeiner, 316 Kan. 346, 350, 515 P.3d 736 (2022).`

   Source: [State v. Thille](https://law.justia.com/cases/kansas/supreme-court/2025/124495.html).

4. **State v. Zaragoza — Court of Appeals**

   `64 Kan. App. 2d 358, 551 P.3d 175 (2024)`

   Source: [Zaragoza v. Board of Johnson County Commissioners](https://law.justia.com/cases/kansas/supreme-court/2025/126732.html), citing the lower decision.

5. **State v. James — Supreme Court**

   `State v. James, 309 Kan. 1280, 1298, 443 P.3d 1063 (2019).`

   Source: [State v. Hollins](https://law.justia.com/cases/kansas/supreme-court/2025/126348.html).

6. **State v. Bentley — Supreme Court**

   `State v. Bentley, 317 Kan. 222, 231, 526 P.3d 1060 (2023)`

   Source: [State v. Johnson](https://law.justia.com/cases/kansas/supreme-court/2025/126626.html).

7. **State v. Newman-Caddell — Supreme Court**

   `State v. Newman-Caddell, 317 Kan. 251, 258-59, 527 P.3d 911 (2023).`

   Source: [State v. Johnson](https://law.justia.com/cases/kansas/supreme-court/2025/126626.html).

8. **Nauheim v. City of Topeka — Supreme Court**

   `Nauheim v. City of Topeka, 309 Kan. 145, 149, 432 P.3d 647 (2019).`

   Source: [Zaragoza](https://law.justia.com/cases/kansas/supreme-court/2025/126732.html).

9. **State v. Crosby — Supreme Court**

   `State v. Crosby, 312 Kan. 630, 639, 479 P.3d 167 (2021).`

   Source: [State v. Thille](https://law.justia.com/cases/kansas/supreme-court/2025/124495.html).

10. **State v. Casteel — unpublished Court of Appeals form**

    `State v. Casteel, No. 127,236, 2025 WL 1671998, at *4 (Kan. App.`

    Source: [State v. Johnson](https://law.justia.com/cases/kansas/supreme-court/2025/126626.html). The source’s extracted occurrence breaks at the page boundary after `App.`; no missing date has been reconstructed.

#### 5. Style mechanics

Kansas parallel citations commonly carry matching official and Pacific pinpoints:

`Kan. first page, Kan. pin, P.3d first page`

The Court of Appeals reporter is `Kan. App. 2d`; the `2d` is a reporter-series designation, not an appellate district.

Unpublished citations use `Kan. App.` in the parenthetical even though published decisions use `Kan. App. 2d` as the reporter.

The broken *Casteel* occurrence illustrates why page-boundary fragments should not be silently completed.

#### 6. Risk flags

**(a) Prefix collision:** **Yes.** `Kan.` is a prefix of `Kan. App. 2d`.

**(b) District/division-specific intermediate citations:** **No.**

**(c) Reporter edition spans multiple courts:** `P.3d` **yes**; the official reporter editions are court-specific.

**(d) Apostrophes or ordinals in court abbreviations:** The core court token has no apostrophe. `2d` occurs in the intermediate reporter edition and can resemble an ordinal even though it is a series designation.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- A Kansas neutral/public-domain citation system.
- Quantitative vendor-citation prevalence.
- Common court-attribution drift.
- The missing continuation of the source-fragmented *Casteel* citation.
- Whether all current Court of Appeals cases promptly receive `Kan. App. 2d` and `P.3d` pagination.

---

### New Mexico

#### 1. Sources

1. [Butler v. Motiva Performance Engineering, LLC](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-40215-0.html), published Supreme Court opinion.
2. [State v. Cardenas](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39517-0.html), published Supreme Court opinion.
3. [Shook v. Wilson](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39689-0.html), published Supreme Court opinion.
4. [Martens v. City of Albuquerque](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39826.html), Supreme Court slip opinion citing the published Court of Appeals decision.
5. [Szantho v. Casa Maria of New Mexico, LLC](https://law.justia.com/cases/new-mexico/court-of-appeals/2025/a-1-ca-41167.html), Court of Appeals.
6. [Dilley v. University of New Mexico Sandoval Regional Medical Center](https://law.justia.com/cases/new-mexico/court-of-appeals/2025/a-1-ca-41208.html), Court of Appeals.
7. [Rule 23-112 NMRA citation requirements](https://laws.nmonesource.com/w/nmos/Rule-Set-23-NMRA#!b/23-112), reproduced and summarized by Cornell.

#### 2. Court structure as cited

New Mexico uses:

- **Supreme Court:** `NMSC`
- **Court of Appeals:** `NMCA`

The exact official formats are:

- `YYYY-NMSC-NNN`
- `YYYY-NMCA-NNN`

Paragraph pinpoints follow the neutral citation. Neither appellate court has citation-relevant districts or divisions.

#### 3. Reporters in actual use

Rule 23-112 requires the official neutral citation for all precedential appellate opinions. It also requires a parallel to the **New Mexico Reports**; a Pacific Reporter parallel is discretionary. The rule tells writers not to cite the unofficial hardbound New Mexico Appellate Reports.

The current system was operating by **1996**, when opinions such as `1996-NMSC-072` were issued. The exact original order date was not located, but the first verified neutral-citation year is 1996.

A slip opinion may initially have a blank “Opinion Number.” If selected for publication, the Chief Clerk assigns the vendor-neutral citation, and the New Mexico Compilation Commission authenticates and formally publishes it.

#### 4. Verbatim examples

1. **Butler v. Motiva Performance Engineering, LLC — Supreme Court**

   `2025-NMSC-037`

   Source: [Butler](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-40215-0.html).

2. **State v. Cardenas — Supreme Court**

   `2025-NMSC-020`

   Source: [Cardenas](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39517-0.html).

3. **Shook v. Wilson — Supreme Court**

   `2025-NMSC-022`

   Source: [Shook](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39689-0.html).

4. **Martens v. City of Albuquerque — Court of Appeals**

   `Martens v. City of Albuquerque, 2023-NMCA-037, ¶ 12, 531 P.3d 607.`

   Source: [Martens](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39826.html).

5. **Cummings v. Board of Regents — Court of Appeals**

   `Cummings, 2019-NMCA-034, ¶ 21, 444 P.3d 1058`

   Source: [Martens](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39826.html).

6. **Ferguson v. New Mexico State Highway Commission — Court of Appeals**

   `Ferguson v. New Mexico State Highway Commission, 1982-NMCA-180, ¶ 12, 99 N.M. 194, 656 P.2d 244.`

   Source: [Martens](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39826.html).

7. **Marrujo v. New Mexico State Highway Transportation Department — Supreme Court**

   `Marrujo v. New Mexico State Highway Transportation Department, 1994-NMSC-116, 118 N.M. 753, 887 P.2d 747`

   Source: [Martens](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-39826.html).

8. **Autovest L.L.C. v. Agosto — Supreme Court full parallel**

   `Autovest L.L.C. v. Agosto, 2025-NMSC-001, ¶ 25, 563 P.3d 811`

   Source: [Butler](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-40215-0.html).

9. **Wilson — Supreme Court**

   `Wilson, 2025-NMSC-003, ¶ 9, 563 P.3d 841`

   Source: [City of Roswell v. Sanchez-Gagne](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-40437.html).

10. **Bolen v. New Mexico Racing Commission — pending neutral and Pacific citation**

    `Bolen v. N.M. Racing Comm’n, 2025-NMSC-___, ¶ 11, ___ P.3d ___ (S-1-SC- 40427, June 2, 2025).`

    Source: [City of Roswell](https://law.justia.com/cases/new-mexico/supreme-court/2025/s-1-sc-40437.html). The source’s space after `S-1-SC-` is preserved.

#### 5. Style mechanics

New Mexico’s neutral citation is the **official citation**, not merely an optional parallel.

Current Rule 23-112 requires the New Mexico Reports parallel once available and makes `P.3d` discretionary. Real slip opinions can temporarily contain a blank neutral number and blank Pacific fields.

Paragraph pinpoints use `¶`. The New Mexico Reports and Pacific Reporter parallels retain their first pages; the paragraph is the preferred pinpoint.

The text layer frequently renders typographic apostrophes in agency abbreviations such as `Comm’n` and `Dep’t`.

#### 6. Risk flags

**(a) Prefix collision:** `NMSC` is not a literal prefix of `NMCA`, although both share the `NM` state stem. Exact matching remains necessary.

**(b) District/division-specific intermediate citations:** **No.**

**(c) Reporter edition spans multiple courts:** `P.3d` and New Mexico Reports **do**; `NMSC` and `NMCA` are court-specific.

**(d) Apostrophes or ordinals in court abbreviations:** **No in `NMSC` or `NMCA`.** Typographic apostrophes occur frequently in entity names.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- The exact date and number of the original order introducing the system; 1996 is the first verified issuance year.
- Quantitative vendor use.
- Common attribution drift between `NMSC` and `NMCA`.
- Whether every slip opinion selected for publication retains the same docket-based electronic URL after authentication.
- How often filed briefs omit the mandatory New Mexico Reports parallel before it becomes available.

---

### Utah

#### 1. Sources

1. [Water Horse Resources, LLC v. Duchesne County](https://law.justia.com/cases/utah/supreme-court/2025/20230642.html), Utah Supreme Court.
2. [Utah Legislature v. League of Women Voters](https://law.justia.com/cases/utah/supreme-court/2025/20230751.html), Supreme Court.
3. [State v. Hintze](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230902-ca.html), Utah Court of Appeals.
4. [State v. Logue](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230750-ca.html), Court of Appeals.
5. [Hofeling v. Utah Department of Corrections](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230745-ca.html), Court of Appeals.
6. [Utah State Law Library citation guidance](https://www.utcourts.gov/en/about/miscellaneous/law-library/research/utah.html).

#### 2. Court structure as cited

Utah uses:

- **Utah Supreme Court:** `UT`
- **Utah Court of Appeals:** `UT App`

The Court of Appeals is statewide. No district or division identifier appears in the public-domain citation.

#### 3. Reporters in actual use

Published opinions use a universal citation plus a Pacific parallel:

- `YYYY UT N`
- `YYYY UT App N`

The Utah State Law Library gives examples from **1999** for the Court of Appeals and **2001** for the Supreme Court and explains that published citations should contain the universal citation and Pacific Reporter citation. Current opinions use numbered paragraphs.

The `P.3d` parallel spans both appellate courts. The neutral identifier supplies court level.

Utah opinions are also collected in the Utah Reporter, which is a state collection of Utah cases from the Pacific Reporter. No separate current state volume-page citation appears in the selected opinions.

#### 4. Verbatim examples

1. **Water Horse Resources — Supreme Court**

   `2025 UT 43`

   Source: [Water Horse Resources](https://law.justia.com/cases/utah/supreme-court/2025/20230642.html).

2. **Utah Legislature v. League of Women Voters — Supreme Court**

   `2025 UT 39`

   Source: [Utah Legislature](https://law.justia.com/cases/utah/supreme-court/2025/20230751.html).

3. **State v. Hintze — Court of Appeals decision**

   `State v. Hintze (Hintze I), 2022 UT App 117, ¶ 2, 520 P.3d 1.`

   Source: [State v. Hintze](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230902-ca.html).

4. **Hintze II — Supreme Court**

   `State v. Hintze (Hintze II), 2025 UT 3, ¶¶ 39–98, 567 P.3d 506.`

   Source: [State v. Hintze](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230902-ca.html).

5. **Hintze II — Id. short form**

   `Id. ¶ 98.`

   Source: [State v. Hintze](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230902-ca.html).

6. **State v. Logue — Court of Appeals with certiorari history**

   `State v. Logue (Logue II), 2018 UT App 156, ¶ 1 n.1, 436 P.3d 136, cert. denied, 432 P.3d 1229 (Utah 2018)`

   Source: [State v. Logue](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230750-ca.html).

7. **Hofeling — source header spacing anomaly**

   `2025 UT App180`

   Source: [Hofeling](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230745-ca.html). The missing space before `180` is preserved from the archive text.

8. **Rodriguez v. State — Court of Appeals**

   `2025 UT App 82`

   Source: [Rodriguez](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20231061-ca.html).

9. **Compagni v. State — Court of Appeals**

   `2025 UT App 68`

   Source: [Compagni](https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230870-ca.html).

10. **New Star General Contractors v. Department of Transportation — Supreme Court**

    `2025 UT 32`

    Source: [New Star](https://law.justia.com/cases/utah/supreme-court/2025/20230439.html).

#### 5. Style mechanics

The neutral citation precedes the regional parallel, with paragraph pinpoints between them.

`UT` is complete on its own; `(Utah <year>)` can appear in later history but is not the ordinary identifier of a new Utah opinion.

Related decisions under the same caption are labeled `I`, `II`, and so on. *Hintze I* and *Hintze II* are separate opinions, not inconsistent court attributions.

A source-level missing space such as `UT App180` is a realistic extraction input.

#### 6. Risk flags

**(a) Prefix collision:** **Yes.** `UT` is a literal prefix of `UT App`.

**(b) District/division-specific intermediate citations:** **No.**

**(c) Reporter edition spans multiple courts:** `P.3d` **yes**; `UT` and `UT App` are court-specific.

**(d) Apostrophes or ordinals in court abbreviations:** **No.** Roman-numeral case labels such as `Hintze II` can occur adjacent to the citation.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified as error.** Same-caption decisions at different levels are explicitly labeled and carry different neutral identifiers.

#### 7. Not verified

- The exact date and order number originally adopting the Utah universal-citation system; the official law-library examples establish use by 1999.
- Quantitative Westlaw/LEXIS use.
- The exact official status of the Utah Reporter relative to the Pacific Reporter.
- Common court-attribution drift.
- Whether every header-spacing anomaly is present in the official PDF rather than archive extraction.

---

### Nevada

#### 1. Sources

1. [Backman v. Gelbman](https://law.justia.com/cases/nevada/court-of-appeals/2025/86396-coa.html), published Nevada Court of Appeals opinion.
2. [Urias v. District Court](https://law.justia.com/cases/nevada/supreme-court/2025/88977.html), Nevada Supreme Court.
3. [State v. Desavio](https://law.justia.com/cases/nevada/supreme-court/2025/86516.html), Supreme Court.
4. [Clark County Department of Family Services v. District Court](https://law.justia.com/cases/nevada/supreme-court/2025/88457.html), Supreme Court.
5. [AZG Limited Partnership v. Dickinson Wright PLLC](https://law.justia.com/cases/nevada/supreme-court/2025/87019.html), Supreme Court.
6. [Soldo-Allessio v. Ferguson](https://law.justia.com/cases/nevada/court-of-appeals/2025/87657-coa.html), Court of Appeals.

#### 2. Court structure as cited

Nevada has a **Nevada Supreme Court** and a statewide **Nevada Court of Appeals**. Published decisions from both can appear in **Nevada Reports** and carry a `Nev. Adv. Op.` number.

The Court of Appeals source is identifiable at issuance through its court heading and docket suffix `-COA`. Later full citations to Court of Appeals decisions often require `(Ct. App. <year>)`, because `Nev.` itself no longer guarantees Supreme Court authorship.

#### 3. Reporters in actual use

Nevada Reports remains active. An advance opinion has the form:

`<volume> Nev. Adv. Op. No. <number>`

Published Court of Appeals opinions also receive this form; *Backman* is `141 Nev. Adv. Op. No. 8`.

The permanent parallel is normally:

`Nev. first page, official pin, P.3d first page, regional pin (year)`

`P.3d` spans both appellate courts. Nevada has not adopted a permanent `YYYY-NV-N` neutral identifier.

#### 4. Verbatim examples

1. **Backman v. Gelbman — Court of Appeals advance opinion**

   `141 Nev. Adv. Op. No. 8`

   Source: [Backman](https://law.justia.com/cases/nevada/court-of-appeals/2025/86396-coa.html).

2. **Rivero v. Rivero — Supreme Court**

   `Rivero v. Rivero, 125 Nev. 410, 431, 216 P.3d 213, 228 (2009)`

   Source: [Backman](https://law.justia.com/cases/nevada/court-of-appeals/2025/86396-coa.html).

3. **Romano v. Romano — Supreme Court**

   `Romano v. Romano, 138 Nev. 1, 6, 501 P.3d 980, 984 (2022).`

   Source: [Backman](https://law.justia.com/cases/nevada/court-of-appeals/2025/86396-coa.html).

4. **Recontrust Co. v. Zhang — Supreme Court**

   `Recontrust Co. v. Zhang, 130 Nev. 1, 7-8, 317 P.3d 814, 818 (2014).`

   Source: [Backman](https://law.justia.com/cases/nevada/court-of-appeals/2025/86396-coa.html).

5. **Davis v. Ewalefo — Supreme Court**

   `Davis v. Ewalefo, 131 Nev. 445, 450, 352 P.3d 1139, 1142 (2015)`

   Source: [Backman](https://law.justia.com/cases/nevada/court-of-appeals/2025/86396-coa.html).

6. **Martinez Guzman v. Second Judicial District Court — Supreme Court**

   `Martinez Guzman v. Second Jud. Dist. Ct., 136 Nev. 103, 106, 460 P.3d 443, 447 (2020).`

   Source: [Urias](https://law.justia.com/cases/nevada/supreme-court/2025/88977.html).

7. **Morgan v. State — Supreme Court**

   `Morgan v. State, 134 Nev. 200, 204-06, 416 P.3d 212, 219-20 (2018).`

   Source: [State v. Desavio](https://law.justia.com/cases/nevada/supreme-court/2025/86516.html).

8. **Canarelli v. Eighth Judicial District Court — Supreme Court**

   `Canarelli v. Eighth Jud. Dist. Ct., 136 Nev. 247, 250, 464 P.3d 114, 119 (2020)`

   Source: [Clark County DFS](https://law.justia.com/cases/nevada/supreme-court/2025/88457.html).

9. **Reynolds v. Tufenkjian — Supreme Court**

   `Reynolds v. Tufenkjian, 136 Nev. 145, 147, 153-54, 461 P.3d 147, 150, 154 (2020).`

   Source: [AZG](https://law.justia.com/cases/nevada/supreme-court/2025/87019.html).

10. **Monahan v. Hogan — Court of Appeals**

    `Monahan v. Hogan, 138 Nev. 58, 62, 507 P.3d 588, 592 (Ct. App. 2022)`

    Source: [Soldo-Allessio](https://law.justia.com/cases/nevada/court-of-appeals/2025/87657-coa.html).

#### 5. Style mechanics

Nevada’s most important structural feature is that `Nev.` and `Nev. Adv. Op.` can now identify decisions from **either** appellate court.

For Court of Appeals cases, `(Ct. App.)` is load-bearing once the opinion is separated from its heading and `-COA` docket.

Full parallel runs frequently repeat the pinpoint in both reporters.

The advance-opinion form is temporary in pagination but permanent as useful opinion metadata; it is not a year-court neutral identifier.

#### 6. Risk flags

**(a) Prefix collision:** **Potentially yes.** Explicit `(Nev.)` and `(Nev. Ct. App.)` forms share the state prefix. More importantly, the local `Nev.` reporter itself spans both levels.

**(b) District/division-specific intermediate citations:** **No.**

**(c) Reporter edition spans multiple courts:** **Yes—strongly.** Both `Nev.` and `P.3d` can contain Supreme Court and Court of Appeals decisions.

**(d) Apostrophes or ordinals in court abbreviations:** **No.** Docket suffix `-COA` is alphabetic.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified as common**, but the shared official reporter creates a concrete attribution risk when `(Ct. App.)` or source metadata is omitted.

#### 7. Not verified

- A Nevada neutral/public-domain case identifier.
- Quantitative vendor use.
- How consistently external databases preserve `(Ct. App.)` for Nevada Court of Appeals cases.
- Common misattribution of one identical opinion.
- Whether every published Court of Appeals opinion receives both Nevada Reports and Pacific pagination.

---

### Idaho

#### 1. Sources

1. [Hill v. Emergency Medicine of Idaho](https://law.justia.com/cases/idaho/supreme-court-civil/2025/51240.html), Idaho Supreme Court.
2. [State v. Radue](https://law.justia.com/cases/idaho/court-of-appeals-criminal/2025/51089.html), Idaho Court of Appeals.
3. [Frauenholz v. Frauenholz](https://law.justia.com/cases/idaho/supreme-court-civil/2025/50978.html), Supreme Court.
4. [Yates v. Yates](https://law.justia.com/cases/idaho/supreme-court-civil/2025/51169.html), Supreme Court.
5. [State v. Von Ehlinger](https://law.justia.com/cases/idaho/court-of-appeals-criminal/2025/50995.html), Court of Appeals.
6. [Ortiz v. State](https://law.justia.com/cases/idaho/court-of-appeals-civil/2025/51036.html), Court of Appeals.

#### 2. Court structure as cited

Idaho has:

- **Idaho Supreme Court**
- **Idaho Court of Appeals**

Both publish in the `Idaho` reporter. A Supreme Court case ordinarily ends with a year-only parenthetical; a Court of Appeals case uses `(Ct. App. <year>)`.

The Court of Appeals is statewide and has no citation-relevant district or division.

#### 3. Reporters in actual use

The state-specific `Idaho` reporter remains active and is routinely paired with `P.3d`:

`168 Idaho 585, 590, 484 P.3d 866, 871 (2021)`

Because `Idaho` spans both appellate levels, the Court of Appeals parenthetical is essential.

Idaho has no permanent `YYYY-ID-N` neutral citation. Pending publication can appear with blanks in both state and Pacific reporters.

#### 4. Verbatim examples

1. **Elsaesser v. Gibson — Supreme Court**

   `Elsaesser v. Gibson, 168 Idaho 585, 590, 484 P.3d 866, 871 (2021)`

   Source: [Hill](https://law.justia.com/cases/idaho/supreme-court-civil/2025/51240.html).

2. **State v. Yzaguirre — Supreme Court**

   `State v. Yzaguirre, 144 Idaho 471, 474, 163 P.3d 1183, 1186 (2007)`

   Source: [State v. Radue](https://law.justia.com/cases/idaho/court-of-appeals-criminal/2025/51089.html).

3. **Horner v. Sani-Top — Supreme Court**

   `Horner v. Sani-Top, 143 Idaho 230, 237, 141 P.3d 1099, 1106 (2006).`

   Source: [Hill](https://law.justia.com/cases/idaho/supreme-court-civil/2025/51240.html).

4. **Conner v. Hodges — Supreme Court**

   `Conner v. Hodges, 157 Idaho 19, 27, 333 P.3d 130, 138 (2014)`

   Source: [Frauenholz](https://law.justia.com/cases/idaho/supreme-court-civil/2025/50978.html).

5. **State v. Billings — Court of Appeals**

   `State v. Billings, 137 Idaho 827, 54 P.3d 470 (Ct. App. 2002)`

   Source: [State v. Radue](https://law.justia.com/cases/idaho/court-of-appeals-criminal/2025/51089.html).

6. **State v. Pole — Court of Appeals**

   `State v. Pole, 139 Idaho 370, 79 P.3d 729 (Ct. App. 2003).`

   Source: [State v. Radue](https://law.justia.com/cases/idaho/court-of-appeals-criminal/2025/51089.html).

7. **State v. Ortega — Court of Appeals with double pin**

   `State v. Ortega, 157 Idaho 782, 787, 339 P.3d 1186, 1191 (Ct. App. 2014)`

   Source: [State v. Von Ehlinger](https://law.justia.com/cases/idaho/court-of-appeals-criminal/2025/50995.html).

8. **In re Estate of McKee — Supreme Court**

   `In re Est. of McKee, 153 Idaho 432, 437, 283 P.3d 749, 754 (2012)`

   Source: [Yates](https://law.justia.com/cases/idaho/supreme-court-civil/2025/51169.html).

9. **Pelayo v. Pelayo — Supreme Court, double ranges**

   `Pelayo v. Pelayo, 154 Idaho 855, 858-59, 303 P.3d 214, 217-18 (2013).`

   Source: [Yates](https://law.justia.com/cases/idaho/supreme-court-civil/2025/51169.html).

10. **Rose v. Martino — pending publication**

    `Rose v. Martino, ___Idaho ____, ____ P.3d _____ (2025)`

    Source: [Frauenholz](https://law.justia.com/cases/idaho/supreme-court-civil/2025/50978.html). The source’s spacing and unequal underscore groups are preserved.

#### 5. Style mechanics

Idaho routinely repeats the pinpoint in both the official and regional reporters.

The same official reporter covers both courts. The terminal `(Ct. App.)` is therefore not optional surplus.

Pending-publication blanks can directly adjoin the reporter name, as in `___Idaho`, and use different underscore counts.

No paragraph-based neutral pinpoint system appears in the selected current opinions.

#### 6. Risk flags

**(a) Prefix collision:** **Potentially yes** in explicit parentheticals: `(Idaho)` versus `(Idaho Ct. App.)`. In local official form, the larger issue is that `Idaho` spans both courts.

**(b) District/division-specific intermediate citations:** **No.**

**(c) Reporter edition spans multiple courts:** **Yes.** `Idaho` and `P.3d` both do.

**(d) Apostrophes or ordinals in court abbreviations:** **No.**

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- An Idaho neutral/public-domain identifier.
- Quantitative vendor use.
- Common omission of `(Ct. App.)` in real filings.
- Common Supreme/Court of Appeals attribution drift.
- Whether all pending blank citations are later updated in archived slip opinions.

---

### Montana

#### 1. Sources

1. [Planned Parenthood of Montana v. State](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0321.html), Montana Supreme Court.
2. [Summers v. Crestview Apartments](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0380.html), Supreme Court.
3. [Schultz v. Department of Public Health](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0377.html), Supreme Court.
4. [Kalina v. State](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0283.html), Supreme Court.
5. [Mullee v. State](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0345.html), Supreme Court.
6. [Montana neutral-citation order and models](https://www.law.cornell.edu/citation/sample_montana).
7. [Montana court opinions and rules portal](https://courts.mt.gov/library/mr/).

#### 2. Court structure as cited

Montana has a single state appellate court, the **Montana Supreme Court**. There is no intermediate appellate court.

Published opinions use the public-domain form:

`YYYY MT N`

Memorandum or noncitable dispositions can carry an `N` suffix, such as `2025 MT 73N`.

#### 3. Reporters in actual use

The Montana Supreme Court adopted neutral citation effective **January 1, 1998**. The neutral identifier is followed by paragraph pins, a Montana Reports parallel, and a Pacific Reporter parallel.

The modern full form is:

`YYYY MT N, ¶ pin, <volume> Mont. <page>, <volume> P.3d <page>`

The court’s order confirms that Montana Reports remains the official reporter and that the Pacific parallel continues alongside the neutral citation.

#### 4. Verbatim examples

1. **Planned Parenthood of Montana v. State — opinion identifier**

   `2025 MT 120`

   Source: [Planned Parenthood](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0321.html).

2. **Earlier Planned Parenthood decision — full triple citation**

   `Planned Parenthood of Montana v. State, 2022 MT 157, ¶¶ 2, 61, 409 Mont. 378, 515 P.3d 301.`

   Source: [Planned Parenthood](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0321.html).

3. **Sands v. Town of West Yellowstone**

   `Sands v. Town of W. Yellowstone, 2007 MT 110, ¶ 15, 337 Mont. 209, 158 P.3d 432.`

   Source: [Summers](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0380.html).

4. **Williams v. Board of County Commissioners of Missoula County**

   `Williams v. Bd. of Cnty. Comm’rs of Missoula Cnty., 2013 MT 243, ¶ 23, 371 Mont. 356, 308 P.3d 88`

   Source: [Schultz](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0377.html).

5. **Montana Democratic Party v. Jacobsen**

   `Mont. Dem. Party v. Jacobsen, 2024 MT 66, ¶ 18, 416 Mont. 44, 545 P.3d 1074`

   Source: [Planned Parenthood](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0321.html).

6. **Armstrong v. State**

   `Armstrong v. State, 1999 MT 261, ¶ 71, 296 Mont. 361, 989 P.2d 364.`

   Source: [Planned Parenthood](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0321.html).

7. **Fritzler v. Bighorn**

   `Fritzler v. Bighorn, 2024 MT 27, ¶ 7, 415 Mont. 165, 543 P.3d 571`

   Source: [Kalina](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0283.html).

8. **Cook v. Bodine**

   `Cook v. Bodine, 2024 MT 189, ¶ 10, 418 Mont. 49, 555 P.3d 236`

   Source: [Mullee](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0345.html).

9. **Estate of Harris v. Reilly**

   `Estate of Harris v. Reilly, 2025 MT 126, ¶ 16, 422 Mont. 383, 570 P.3d 552`

   Source: [Summers](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0380.html).

10. **Noncitable memorandum identifier**

    `2025 MT 73N`

    Source: [Kerr v. State](https://law.justia.com/cases/montana/supreme-court/2025/da-24-0442.html), which expressly states that the disposition is not precedent and may not be cited.

#### 5. Style mechanics

Montana supplies three layers: neutral citation, Montana Reports, and Pacific Reporter.

The same paragraph number applies across the neutral and reporter versions; the court does not need separate reporter-page pinpoints for modern opinions.

Suffixes are meaningful:

- `N` — noncitable memorandum disposition.
- `W` — withdrawal or vacatur order under the neutral-citation rules.
- `A` — amendment order.

Typographic apostrophes occur in names such as `Comm’rs`.

#### 6. Risk flags

**(a) Prefix collision:** **Not applicable.** No intermediate appellate court.

**(b) District/division-specific intermediate citations:** **Not applicable.**

**(c) Reporter edition spans multiple courts in the state:** **No for state appellate courts.** Montana has only its Supreme Court, although `P.3d` is multistate.

**(d) Apostrophes or ordinals in court abbreviations:** **No in `MT`.** Typographic apostrophes occur elsewhere.

**(e) Inconsistent Supreme/intermediate attribution:** **Not applicable.**

#### 7. Not verified

- Quantitative vendor-citation use.
- Whether all categories of substantive orders receive `MT` numbers.
- How consistently outside sources preserve `N`, `W`, and `A` suffixes.
- A current example of a withdrawn `W` or amended `A` identifier.
- Whether every noncitable `N` disposition is excluded from all reporter key spaces.

---

### Wyoming

#### 1. Sources

1. [Robin v. State](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0209.html), Wyoming Supreme Court.
2. [Hamann v. State](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0234.html), Supreme Court.
3. [Iverson v. State](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html), Supreme Court.
4. [Wiegand v. State](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0229.html), Supreme Court.
5. [Robinson v. State](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0164.html), Supreme Court.
6. [Wyoming neutral-citation order and models](https://www.law.cornell.edu/citation/sample_wyoming).

#### 2. Court structure as cited

Wyoming has one state appellate court, the **Wyoming Supreme Court**. There is no intermediate appellate court.

Its public-domain identifier is:

`YYYY WY N`

#### 3. Reporters in actual use

The neutral system applies to cases decided on or after **January 1, 2001**. Paragraph pinpoints follow the neutral citation.

For decisions from 2001 through 2003, filings were required to add the Pacific Reporter parallel. For decisions after December 31, 2003, the Pacific parallel is optional in filed documents, although the Supreme Court continues to include it when available. The Wyoming Reporter remains the official reporter.

Current opinions predominantly show `YYYY WY N, ¶ pin, P.3d first page, pin (Wyo. year)`.

#### 4. Verbatim examples

1. **Iverson v. State — opinion identifier**

   `2025 WY 19`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

2. **Lee v. State**

   `Lee v. State, 2024 WY 97, ¶ 12, 555 P.3d 496, 499 (Wyo. 2024);`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

3. **Kobielusz v. State**

   `Kobielusz v. State, 2024 WY 10, ¶ 24, 541 P.3d 1101, 1108 (Wyo. 2024)`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

4. **Walker v. State**

   `Walker v. State, 2022 WY 158, ¶ 17, 521 P.3d 967, 976 (Wyo. 2022)`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

5. **Barrett v. State**

   `Barrett v. State, 2022 WY 64, ¶ 36, 509 P.3d 940, 948 (Wyo. 2022)`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

6. **Blevins v. State**

   `Blevins v. State, 2017 WY 43, ¶ 26, 393 P.3d 1249, 1255 (Wyo. 2017)`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

7. **Person v. State**

   `Person v. State, 2023 WY 26, ¶ 71, 526 P.3d 61, 78 (Wyo. 2023)`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

8. **Law v. State — multiple-paragraph range**

   `Law v. State, 2004 WY 111, ¶¶ 25-29, 98 P.3d 181, 190-91 (Wyo. 2004)`

   Source: [Iverson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0203.html).

9. **Hamann v. State — opinion identifier**

   `2025 WY 75`

   Source: [Hamann](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0234.html).

10. **Robinson v. State — opinion identifier**

    `2025 WY 3`

    Source: [Robinson](https://law.justia.com/cases/wyoming/supreme-court/2025/s-24-0164.html).

#### 5. Style mechanics

Wyoming often supplies both the neutral citation and an explicit `(Wyo. <year>)` after the Pacific parallel, even though `WY` already identifies the court.

Paragraph pinpoints precede the regional reporter. Regional page pinpoints then follow the P.3d first page.

The neutral citation remains complete if the Pacific parallel is omitted.

#### 6. Risk flags

**(a) Prefix collision:** **Not applicable.** No intermediate appellate court.

**(b) District/division-specific intermediate citations:** **Not applicable.**

**(c) Reporter edition spans multiple courts in the state:** **No.** There is one state appellate court, though `P.3d` is multistate.

**(d) Apostrophes or ordinals in court abbreviations:** **No.**

**(e) Inconsistent Supreme/intermediate attribution:** **Not applicable.**

#### 7. Not verified

- Quantitative vendor use.
- A current case with blank P.3d pagination.
- Whether every Wyoming substantive order receives a `WY` identifier.
- How often practitioners omit the optional Pacific parallel.
- Whether Wyoming Reporter pagination is independently present in current filed citations or principally represented through the neutral/Pacific form.

---

### Alaska

#### 1. Sources

1. [Portfolio Recovery Associates, LLC v. Duvall](https://law.justia.com/cases/alaska/supreme-court/2025/s-18318.html), Alaska Supreme Court.
2. [Cassell v. State, Department of Fish & Game](https://law.justia.com/cases/alaska/supreme-court/2025/s-18476.html), Supreme Court.
3. [Collins v. State](https://law.justia.com/cases/alaska/supreme-court/2025/s-18175.html), Supreme Court.
4. [Burney and Townsend v. State](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13327.html), published Alaska Court of Appeals opinion.
5. [Macasaet v. State](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13574.html), published Court of Appeals opinion.
6. [Borkovec v. State](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13583.html), Court of Appeals memorandum opinion.
7. [Alaska appellate-publication and citation information](https://courts.alaska.gov/appellate/).
8. [Alaska Appellate Rule 214(d)](https://courts.alaska.gov/rules/docs/app.pdf), governing citation of unpublished decisions.

#### 2. Court structure as cited

Alaska has:

- **Alaska Supreme Court:** `(Alaska)`
- **Alaska Court of Appeals:** `(Alaska App.)`

The Court of Appeals is a statewide subject-matter court handling criminal and related matters. It has no district or division identifier in its citation.

Published slip opinions also carry court-specific opinion numbers:

- Supreme Court: opinion numbers such as `No. 7771`.
- Court of Appeals: opinion numbers such as `No. 2794`.

Opinion numbers are useful pending publication but are not a permanent year-based neutral system.

#### 3. Reporters in actual use

The official reporters are the **Pacific Reporter** and the **Alaska Reporter**, which contains Alaska cases excerpted from the Pacific Reporter. Current published cases use `P.3d`; older cases use `P.2d`.

Both reporters span the Supreme Court and Court of Appeals, so the parenthetical is load-bearing.

Before reporter publication, a slip opinion may be cited by case name, opinion number, court, and date. Alaska’s official law-library guidance gives the model:

`V.S.B. v. State, Op. No. 5537 (Alaska February 15, 2001)`

Memorandum opinions are nonprecedential. Current Rule 214(d), and the notices printed in real memorandum opinions, permit limited persuasive citation with an unpublished designation, notwithstanding a shorter court webpage description that says MOJs “may not be cited.” The rule and the actual opinion notice are the more specific current authorities.

#### 4. Verbatim examples

1. **McCoy v. State — Court of Appeals**

   `McCoy v. State, 80 P.3d 757, 764 (Alaska App. 2002).`

   Source: [Borkovec v. State](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13583.html).

2. **Godspeed Properties, LLC — Supreme Court**

   `Godspeed Props., LLC, 517 P.3d 31, 43 (Alaska 2022)`

   Source: [Portfolio Recovery Associates](https://law.justia.com/cases/alaska/supreme-court/2025/s-18318.html).

3. **Schultz v. Wells Fargo Bank, N.A. — Supreme Court**

   `Schultz v. Wells Fargo Bank, N.A., 301 P.3d 1237, 1241 (Alaska 2013)`

   Source: [Portfolio Recovery Associates](https://law.justia.com/cases/alaska/supreme-court/2025/s-18318.html).

4. **Alliance of Concerned Taxpayers, Inc. v. Kenai Peninsula Borough — Supreme Court**

   `All. of Concerned Taxpayers, Inc. v. Kenai Peninsula Borough, 273 P.3d 1123, 1126 (Alaska 2012)`

   Source: [Portfolio Recovery Associates](https://law.justia.com/cases/alaska/supreme-court/2025/s-18318.html).

5. **Interior Alaska Airboat Association v. State, Board of Game — Supreme Court**

   `Interior Alaska Airboat Ass’n v. State, Bd. of Game, 18 P.3d 686, 694-95 (Alaska 2001)`

   Source: [Cassell](https://law.justia.com/cases/alaska/supreme-court/2025/s-18476.html).

6. **Ridenour v. State — Court of Appeals**

   `Ridenour v. State, 539 P.3d 530, 539-40 (Alaska App. 2022)`

   Source: [Macasaet](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13574.html).

7. **Klemz v. State — Court of Appeals**

   `Klemz v. State, 171 P.3d 1169, 1172 (Alaska App. 2007)`

   Source: [Macasaet](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13574.html).

8. **Kim v. State — Court of Appeals**

   `Kim v. State, 390 P.3d 1207, 1209 (Alaska App. 2017)`

   Source: [Macasaet](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13574.html).

9. **Waters v. State — unpublished Court of Appeals**

   `Waters v. State, 1993 WL 13156700, at *4, n.1 (Alaska App. May 26, 1993) (unpublished)`

   Source: [Burney and Townsend](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13327.html).

10. **Mikell v. State — unpublished Court of Appeals**

    `Mikell v. State, 2001 WL 81795, at *1 (Alaska App. Jan. 31, 2001) (unpublished).`

    Source: [Mikell v. State](https://law.justia.com/cases/alaska/court-of-appeals/2025/a-13937.html).

#### 5. Style mechanics

Published Alaska cases are regional-reporter-centered; no Alaska-specific volume-page reporter token appears in the ordinary citation because the Alaska Reporter reproduces Pacific Reporter cases.

The court-level distinction is entirely in `(Alaska)` versus `(Alaska App.)`.

Slip opinions carry opinion numbers pending reporter publication. Memorandum decisions carry a separate memorandum number and an explicit nonprecedential notice.

Unpublished citations must state that status and identify an electronic source if publicly accessible. Westlaw star pagination is common.

#### 6. Risk flags

**(a) Prefix collision:** **Yes.** `(Alaska)` is the prefix of `(Alaska App.)`.

**(b) District/division-specific intermediate citations:** **No.**

**(c) Reporter edition spans multiple courts:** **Yes.** `P.2d`, `P.3d`, and the Alaska Reporter span both appellate courts.

**(d) Apostrophes or ordinals in court abbreviations:** **No.** Typographic apostrophes occur in entity names such as `Ass’n` and `Dep’t`.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- A permanent Alaska neutral/public-domain identifier.
- Quantitative Westlaw/LEXIS prevalence.
- Common misattribution of one opinion between appellate levels.
- Whether the court webpage’s categorical “may not be cited” language will be revised to match current Rule 214(d).
- Whether all published slip opinions retain stable opinion-number citations after Pacific pagination is assigned.

---

### Hawaiʻi

#### 1. Sources

1. [McDowell v. Kea](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-21-0000368.html), published Hawaiʻi Intermediate Court of Appeals opinion.
2. [Frankel v. Board of Land and Natural Resources](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-20-0000603-1.html), ICA correction order.
3. [Mālama Kakanilua v. State](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-22-0000486.html), published ICA opinion.
4. [Dailey v. Department of Land and Natural Resources](https://law.justia.com/cases/hawaii/supreme-court/2025/scwc-23-0000415.html), Hawaiʻi Supreme Court.
5. [McGuire v. County of Hawaiʻi](https://law.justia.com/cases/hawaii/supreme-court/2025/sccq-24-0000165.html), Supreme Court.
6. [Darny v. Department of Hawaiian Home Lands](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-22-0000456.html), nonpublication disposition showing the publication warning.

#### 2. Court structure as cited

Hawaiʻi has:

- **Supreme Court of Hawaiʻi**
- **Intermediate Court of Appeals**

Both published levels appear in West’s Hawaiʻi Reports and the Pacific Reporter. In local parallel citations:

- Supreme Court decisions usually end with the year alone.
- ICA decisions use `(App. <year>)`.

Regional-only or externally styled citations may use `(Haw.)` and `(Haw. Ct. App.)`. The ICA is statewide; the numbered trial-court circuits are not ICA divisions.

#### 3. Reporters in actual use

Published appellate opinions are expressly designated:

`FOR PUBLICATION IN WEST’S HAWAI‘I REPORTS AND PACIFIC REPORTER`

The state reporter and `P.3d` are normally supplied as parallels. Both span the Supreme Court and ICA, making the intermediate `(App.)` parenthetical essential.

Older opinions use `Haw.` and `P.2d`; newer opinions use `Hawaiʻi` and `P.3d`. The public archive’s text extraction inconsistently represents the ʻokina as:

- `Hawai#i`
- `Hawai i`
- `Hawai'i`

These are source-layer variants, not recommended normalized spellings.

Hawaiʻi has no verified permanent year-court-sequence neutral case citation. Nonpublication dispositions expressly state that they are not for publication in either reporter.

#### 4. Verbatim examples

The `#` and missing-ʻokina forms below are reproduced exactly from the linked archive’s born-digital text layer.

1. **Malulani Group I — Intermediate Court of Appeals**

   `Malulani Grp., Ltd. v. Kaupo Ranch, Ltd. (Malulani Grp. I), 133 Hawai#i 425, 428, 329 P.3d 330, 333 (App. 2014)`

   Source: [McDowell](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-21-0000368.html).

2. **Association of Apartment Owners of Wailea Elua v. Wailea Resort Co. — Supreme Court**

   `Ass'n of Apartment Owners of Wailea Elua v. Wailea Resort Co., 100 Hawai#i 97, 105-06, 58 P.3d 608, 616-17 (2002)`

   Source: [McDowell](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-21-0000368.html).

3. **Bhakta v. County of Maui — Supreme Court**

   `Bhakta v. Cnty. of Maui, 109 Hawai#i 198, 209, 124 P.3d 943, 954 (2005)`

   Source: [McDowell](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-21-0000368.html).

4. **Kiaʻi Wai v. Department of Water — Supreme Court**

   `Kia#i Wai v. Dep't of Water, 151 Hawai#i 442, 454, 517 P.3d 725, 737 (2022).`

   Source: [Frankel correction order](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-20-0000603-1.html).

5. **Kauaʻi Springs short-form quotation**

   `Id. at 455, 517 P.3d at 738 (quoting Kauai Springs, 133 Hawai#i at 164, 324 P.3d at 974).`

   Source: [Frankel correction order](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-20-0000603-1.html).

6. **Womble Bond Dickinson (US) LLP v. Kim — Supreme Court**

   `Womble Bond Dickinson (US) LLP v. Kim, 153 Hawai i 307, 319, 537 P.3d 1154, 1166 (2023).`

   Source: [Dailey](https://law.justia.com/cases/hawaii/supreme-court/2025/scwc-23-0000415.html).

7. **Honoipu Hideaway — short form retaining both reporters**

   `Honoipu, 154 Hawai i at 374, 550 P.3d at 1232`

   Source: [Dailey](https://law.justia.com/cases/hawaii/supreme-court/2025/scwc-23-0000415.html).

8. **Maesaka-Hirata — Supreme Court**

   `Maesaka-Hirata, 143 Hawai i 335, 354, 431 P.3d 708, 727 (2018)`

   Source: [McGuire](https://law.justia.com/cases/hawaii/supreme-court/2025/sccq-24-0000165.html).

9. **Neary v. Martin — historical Supreme Court**

   `Neary v. Martin, 57 Haw. 577, 580, 561 P.2d 1281, 1283 (1977)`

   Source: [McDowell](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-21-0000368.html).

10. **Larsen v. Pacesetter Systems, Inc. — historical Supreme Court**

    `Larsen v. Pacesetter Sys., Inc., 74 Haw. 1, 17-18, 837 P.2d 1273, 1282-83 (1992)`

    Source: [McDowell](https://law.justia.com/cases/hawaii/court-of-appeals/2025/caap-21-0000368.html).

#### 5. Style mechanics

The local form repeats the pinpoint in the Hawaiʻi Reports and Pacific Reporter.

Because both reporters span both appellate levels, the ICA’s `(App.)` parenthetical is structurally important. A year-only parenthetical ordinarily denotes a Supreme Court decision in this local form.

The ʻokina is a significant normalization hazard. The official typography uses `Hawaiʻi`, but archive text can render it as `Hawai#i`, `Hawai i`, or `Hawai'i`. Exact extraction and normalized matching should be treated as separate concerns.

The *Frankel* source is itself a correction order addressing the ʻokina in a cited name. That is direct evidence that quote/apostrophe treatment is a live editorial issue, not merely theoretical.

Nonpublication dispositions carry an explicit warning that they are not for publication in West’s Hawaiʻi Reports or the Pacific Reporter.

#### 6. Risk flags

**(a) Prefix collision:** **Potentially yes in external parentheticals**—`Haw.` versus `Haw. Ct. App.`. In dominant local parallel form, the distinction is year-only versus `(App. year)`, so the failure is more likely to arise from omission of `(App.)` than from prefix swallowing.

**(b) District/division-specific intermediate citations:** **No.** Trial-court circuit numbers are not ICA divisions.

**(c) Reporter edition spans multiple courts:** **Yes.** Hawaiʻi Reports and `P.3d` both span the Supreme Court and ICA.

**(d) Apostrophes or ordinals in court abbreviations:** The short abbreviation `Haw.` does not contain one, but the full jurisdiction name **Hawaiʻi** contains the ʻokina, and source systems represent it inconsistently. Typographic normalization is therefore a concrete high-risk requirement.

**(e) Inconsistent Supreme/intermediate attribution:** **Not verified.**

#### 7. Not verified

- A Hawaiʻi neutral/public-domain case identifier.
- Quantitative Westlaw or LEXIS prevalence.
- Common attribution of one opinion to both appellate levels.
- Whether all `#` substitutions originate in the public archive rather than the court’s PDF text layer.
- A primary-source cessation date for the older `Haw.` series styling; the change to `Hawaiʻi` appears editorial rather than a new reporter edition.
- Whether every nonpublication disposition may be cited for persuasive value under one uniform rule across all procedural settings.
