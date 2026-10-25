# Fact-check log: Part III (Chapters 18–20)

An adversarial check of every factual claim in Part III so far: chapter text, figures, captions, exercise answers, Myth Checks, Receipts, Field Notes and Ask boxes. The aim was to prove the book wrong, then fix what turned up. The writers had already checked their own claims, and this check assumed nothing they did.

Checked on 25 October 2026 against Chapters 18–20 as merged to `main` in #10.

## Summary

| Verdict | Entries |
|---|---|
| Confirmed | 88 |
| Fixed (the sentence changed) | 10 |
| Downgraded (the grade shown to the reader was lowered) | 0 |
| Cut as unsupported | 0 |
| **Total** | **98** |

An "entry" is one source, with every claim in the chapter that cites it, plus one entry for each uncited factual claim found. A source cited in two chapters has an entry in each. No cited source turned out to be retracted.

**The most serious problems found**

1. **The rater's-role finding was presented as settled (Chapter 18).** The chapter's headline evidence, Scullen, Mount and Goff (2000), found that whether a rater was a boss, a peer or a report added little to ratings. A refutation search found Hoffman et al. (2010), who reanalysed two other large 360-degree data sets with a different model and found that the rater's role explains much more variance, and general performance even less. The chapter's main point survives, and is even strengthened, but the "added only a little" clause now carries that caveat, in the text and in the Receipts box. The new source is in `book/sources/ch18.yaml`.
2. **A figure printed numbers the source does not give (Chapter 18).** Figure 18.2 labelled 6% and 4% of variance as "the rater's role". Those are the remainders after the three shares the abstract reports (62 + 21 + 11 and 53 + 25 + 18). The full text could not be opened to confirm the role effects. The segment is now labelled "the rest, including the rater's role", which is what the arithmetic supports.
3. **A study count overclaimed (Chapter 18).** "In six studies, overconfident people gained status" counted all six of Anderson et al.'s studies. Only Studies 1–3 tested status, Study 4 tested why, and Studies 5–6 tested the reverse direction. The sentence now says three, and a fourth.
4. **The Field Note misdescribed the chapter's own evidence (Chapter 19).** It said most of the chapter's evidence came from "US and Western European firms". The face-time study is from a Southeast Asian bank, the remote-work trials are from a Chinese firm, and none of the chapter's firm studies is from continental Europe. The text now names the bank's region and describes the evidence's origin correctly.
5. **A premise was presented as a conclusion (Chapter 20).** Kambourov and Manovskii (2008) document rising occupational mobility. That human capital is largely occupation-specific is a finding they cite from other work, not one this paper concludes. The text now says so.

Smaller fixes, all listed below, include an uncited gloss replaced by the authors' own words, a narrowed population ("pay decisions" for "administrative decisions"), and three uncited claims now labelled as the book's view.

## Method

- **Batched by source, two tiers.** As the book's owner asked for Part III, each source was opened once and every claim citing it was checked together:
  - a **full check** (open the source, compare direction, size, certainty, population, year and wording, and search for corrections, retractions, failed replications or newer reviews) for headline numbers, every Myth Check, regional facts, claims carrying a chapter's main advice and anything surprising;
  - a **light check** against the registry's `supports` note for background claims already graded strong or moderate, opening the source only where a number, a count or the wording went beyond the note.

  The truth rules did not loosen: no number or quote stayed in print without being checked against a source.
- **Sources opened.** In practice the abstract of every cited DOI was re-read (via OpenAlex, or nature.com where OpenAlex had none), because that was faster than deciding which ones to skip; the exceptions are `eby2008` and `ross1979`, which have no machine-readable abstract and were light-checked against the registry. Full texts were read for the working-paper numbers: NBER w24343 (Benson, Li and Shue 2018/2019), NBER w26530 (Cullen and Perez-Truglia), the authors' June 2022 working paper of Benson, Li and Shue's "Potential" paper, NBER w25065 (Deming and Noray), and O'Boyle and Aguinis (2012) on the author's site. Web pages were re-read for every quotation and web-sourced figure: SHRM on Microsoft, LeanIn.Org, the Harvard corporate-governance summary of Cohen et al., the Resolution Foundation, Dropbox, StaffEng, Tanya Reilly's *Being Glue*, The Pragmatic Engineer and 80,000 Hours. Retraction and correction status was checked for every cited DOI through Crossref's `updated-by` records and OpenAlex's retraction flag.
- **Refutation searches.** These ran for every headline finding and Myth Check. The one that changed the text was Hoffman et al. (2010) against Scullen et al. (2000). Others found no newer evidence that contradicts what the book prints. The bell-curve and Dunning–Kruger boxes already present both sides, and the deliberate-practice box already includes Ericsson's reply.
- **Fixes were minimal.** Each kept the chapter's voice and its cross-references. No true claim was weakened to be safe.

**New source added** (opened during this check): `hoffman2010` in `book/sources/ch18.yaml`.

**What could not be verified, and how the book handles it**

- **Scullen et al. (2000), full text.** Not openly available. The perspective-effect percentages are not in the abstract, so the figure no longer labels the remainder as the rater's role alone.
- **Hoffman et al. (2010), full text.** Read at abstract level only. The book prints no number from it.

## Chapter 18, The Review

### Problems found (5)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| scullen2000 + hoffman2010 | 4,000+ managers, seven raters each; rater idiosyncrasy 62% / 53%, performance 21% / 25%, error 11% / 18%; rater's role "added only a little" (§noise; Figure 18.2; Receipts; Myth Check; Rewind) | full: abstract; refutation search found hoffman2010 (abstract, Crossref) | fixed | All abstract numbers and the rater design are confirmed. Hoffman et al. (2010), modelling source as second-order factors in two other large samples, found source effects explain "(much) more variance" and general performance "(much) less" than previously believed. Added that caveat to the "added only a little" sentence and to the Receipts box, and added the source. Figure 18.2's 6% / 4% "rater's role" segment is only the remainder of the abstract's shares (the full text could not be opened), so it is relabelled "the rest, including the rater's role" in the figure, its script and its alt text. |
| anderson2012 | "In six studies, overconfident people gained status in groups because their confidence made them look competent" (§self-review) | full: abstract | fixed | Studies 1–3 showed the status gain; Study 4 showed overconfidence produces a behaviour pattern that looks competent; Studies 5–6 showed the status motive increases overconfidence. Reworded to "in three studies … and a fourth found that their confidence made them look competent". |
| schleicher2009 | Forced systems harder and less fair "especially for pay decisions" and when performance varied little; lower feedback confidence (§curves) | light: abstract | fixed | The abstract says "used for administrative purposes", which is broader than pay. Reworded to "when the ratings fed administrative decisions such as pay". |
| zell2014 | .29 across 22 meta-analyses; better for specific, objective, familiar tasks; "roughly as much as a mediocre outside predictor" (§self-review; Myth Check; Make it checkable) | full: abstract | fixed | Numbers and moderators are confirmed. The "mediocre outside predictor" comparison had no source. Replaced with the authors' own conclusion, "only moderate insight". |
| ashford2003 | Three motives for seeking feedback (instrumental, ego defence, image protection); "in a review conversation, the defensive motives tend to wake up first" (§hearing) | light: abstract | fixed | The three motives are confirmed. The second sentence is an extrapolation no source tests. It is now labelled as the book's expectation ([!view]). |

### Confirmed (30 entries)

Every claim citing these sources matched the source as read: `viswesvaran1996`, `rotundo2002`, `murphy2008`, `shrm2013`, `speer2019`, `adler2016`, `scullen2005`, `loberg2021`, `cardinaels2021`, `oboyle2012`, `beck2014`, `roth2012`, `kordsmeyer2026`, `correll2020`, `castilla2008`, `castilla2010`, `heidemeier2009`, `exley2022`, `kruger1999`, `krueger2002`, `nuhfer2016`, `gignac2024`, `jansen2021`, `kluger1996`, `anseel2015`, `burris2012`, `denisi2017`, `pulakos2011`, `scopelliti2015`, `dulebohn2012`.

Notes on confirmed claims:

- `shrm2013`: The page confirms the single 1–5 rating built from the manager's assessment plus calibration, its link to merit pay, bonus and stock, the November 2013 end, and Brummel's wording ("No more curve" … "no longer be a pre-determined targeted distribution"). The system dates from the 2011 reviews, so "until 2013" is fair.
- `speer2019`: "Two field studies" is in the abstract.
- `loberg2021`: "Three experiments" is in the abstract. "Slowed teamwork" means the team task took longer.
- `oboyle2012`: The full text (author's PDF) confirms the measures were publications, award nominations (Emmys, Grammys, Oscars and others), election results and wins, matching "outputs such as publications, awards and wins".
- `beck2014`: The quotation "in many cases an artifact of measurement" is exact. The bell-curve Myth Check ("partly", moderate) is fair: the dispute is open.
- `kruger1999`: 12th versus 62nd percentile, bottom quartile, humour, grammar and logic: exact.
- `gignac2024`: 7–9 percentile points, confined to about 0.2% of participants, as the box says ("a tiny fraction").
- `jansen2021`: The nature.com abstract confirms "a large-scale replication … approximately 4,000 participants in each of two studies". The Dunning–Kruger Myth Check ("partly", strong) is fair.
- `castilla2010`: Three experiments, 445 participants with managerial experience: exact.
- `kordsmeyer2026`: N = 20,199; moderated by departmental gender composition: exact.
- `heidemeier2009`: ρ = .34 and d = 0.32 (Western samples): exact.
- `burris2012`: "A field study and two experiments" is in the abstract.
- `adler2016`: Both quoted arguments are on the "retain ratings" side of the debate, as the text says.
- `dulebohn2012`: "Driven mostly by the manager" matches "leader behaviours and perceptions" being the strongest antecedents.
- Calibration Craft Note and "the written record usually is not [closed]": labelled as practitioner advice and [!craft].
- Figures: Figure 18.3 is labelled "Illustrative: Dev's year, not data". Figure 18.1 is a description of a typical cycle, labelled [!craft] in the text.

## Chapter 19, The Promotion Case

### Problems found (3)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| cullen2023b | Face time with the manager speeds promotion, about a third of the gender gap; smokers +0.70 pay grades over ten quarters; men moved to a male manager +0.60 grades, about 14.6% salary; "at a large financial institution" (§potential; Myth Check) | full: AER abstract; NBER w26530 full text | fixed | Every number is confirmed in the working paper (0.70 at 10 quarters, p = .002; non-smokers 0.07, n.s.; 0.60, "roughly equivalent to a 14.6% increase in salary"). The working paper identifies the firm as "a large commercial bank in Southeast Asia". The text now says so, because it is the only face-time evidence in the chapter and the Field Note's claim about where the evidence comes from depended on it. |
| (uncited) Field Note | "Most of the evidence in this chapter comes from US and Western European firms" (Field Note) | checked against the chapter's own sources | fixed | Wrong as stated. The face-time study is from Southeast Asia, the two remote-work trials are from a Chinese firm, the well-being studies include British panel data, and none of the firm studies is from continental Europe. Rewritten as "Most … comes from US firms, with a few from elsewhere (Britain, China and Southeast Asia among them), and almost all of it from workplaces where promotion is a contest". |
| (uncited) | "Over-claiming is likely to be found out by the committee member who asks the other people involved" (§credit) | none | fixed | A prediction with no source. Labelled as the book's view ([!view]). |

### Confirmed (30 entries)

Every claim citing these sources matched the source as read: `lazear1981`, `baker1994`, `orosz2019`, `todi2021`, `larson2020`, `benson2019`, `lazear2004`, `ross1979`, `sarsons2021`, `exley2022`, `scopelliti2015`, `rudman1998`, `ibarra2010`, `allen2004`, `eby2008`, `ng2005`, `leanin2025`, `benson2026`, `roth2012`, `bloom2015`, `bloom2024`, `babcock2017`, `reilly2026`, `bidwell2011`, `cohen2023`, `hamaaki2012`, `kahn1988`, `resolution2012`, `johnston2013`, `boyce2012`.

Notes on confirmed claims:

- `benson2019`: 131 firms (published version; the working paper has 214). The working paper's text reads "Doubling sales credits increases the probability that a worker will be promoted by 14.3 percent relative to the base probability" and "a 7.5 percent decline in the sales performance of each of the newly-promoted manager's subordinates": exact. Both Myth Checks ("partly", strong) are fair.
- `benson2026`: The June 2022 working paper gives annual promotion rates of 12.62% (men) and 10.98% (women), and a potential rating moving from 2 to 3 is worth 8.98 percentage points, against 3.24 for the same step in performance. This matches "12.6% against 11.0%" and "about nine percentage points, more than the equivalent step in performance". The published abstract confirms "approximately half" and that women later outperform.
- `baker1994`: "Twenty years of personnel data from one firm": exact.
- `bidwell2011`: The registry had only a secondary write-up; the ASQ abstract is now read. It says promoted workers had "significantly better performance for the first two years", "lower rates of voluntary and involuntary exit", and that external hires were "paid around 18 percent more" and "promoted faster". All match.
- `todi2021`, `larson2020`, `reilly2026`, `orosz2019`: Quotations re-read on the live pages; exact. All are labelled practitioner in the text.
- `leanin2025`: 93 per 100, the 11th year of the broken rung, and 31% versus 45% for sponsors: exact on the live page. Its advocacy and self-selection caveats are in the text.
- `cohen2023`: $455 a week and the industries are confirmed on the authors' summary.
- `resolution2012`: 37% to "nearly 60%", 2000 to 2008: exact.
- `boyce2012`: "A large sample of randomly selected British workers": confirms "a British study".
- `johnston2013`: Short-term job attributes, negligible health and happiness effects, mental health worse two years on: exact.
- `ibarra2010`: Labelled practitioner. "We found no peer-reviewed study that estimates how much sponsorship causes promotion" is honestly worded as an absence.
- Figures: Figure 19.3 is labelled "Illustrative, not a formula". Figures 19.1 and 19.2 restate the text's own framing.

## Chapter 20, What to Get Good At

### Problems found (2)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| kambourov2008 | US 1968–97 occupational mobility high and rising; "the authors conclude that human capital is largely occupation-specific" (§capital) | full: abstract | fixed | Mobility is confirmed. The specificity of human capital is cited in the abstract as "recent findings", not concluded by this paper. Reworded to say the authors note it matters because other research found human capital largely specific to an occupation or industry. |
| (uncited) | "Most people who end up very good at something did not plan it either" (opening) | none | fixed | A claim about most people with no source. Reworded as the book's suspicion ("Plenty of people … we suspect"). |

### Confirmed (28 entries)

Every claim citing these sources matched the source as read: `todd2026`, `newport2012`, `deming2020`, `ericsson1993`, `macnamara2014`, `ericsson2019`, `macnamara2016`, `macnamara2019`, `quinones1995`, `sackett2022`, `choudhry2005`, `kahneman2009`, `derue2009`, `kluger1996`, `anseel2015`, `dunlosky2013`, `cepeda2006`, `clardy2018`, `johnson2018`, `allen2004`, `eby2008`, `dragoni2014`, `higgins2001`, `ibarra2010`, `flynn2008`, `okeefe2018`, `chen2015`, `ng2008`.

Notes on confirmed claims:

- `macnamara2014`: 26 / 21 / 18 / 4 / under 1%, and "important, but not as important as has been argued": exact. The pause answer and Figure 20.2 match.
- `ericsson2019`: 29% (61% after correction for attenuation) against the 14% reported by Macnamara and colleagues: the book prints 29% and 14%, which is fair. The Myth Check ("partly", strong) presents both camps.
- `macnamara2016`: 18% overall, 1% among elites, no earlier start: exact.
- `deming2020`: The NBER working paper's abstract says the return to applied STEM degrees "declines by more than 50 percent in the first decade": exact.
- `choudhry2005`: 32 of 62 (52%) declined on all outcomes, 13 (21%) on some, and 1 (2%) improved on all: exact.
- `kahneman2009`: The quotation is exact (capitalised in the source).
- `clardy2018`: "Needs to be set aside" is exact.
- `todd2026`: The definition is exact on the live page, and the page warns against "generically accumulating credentials".
- `newport2012`: Labelled practitioner; only the book's thesis is used.
- `quinones1995`: ρ = .27, amount .43, task .41: exact.
- `derue2009`: 225 experiences, 60 managers, diminishing returns offset by feedback: exact. Figure 20.3's curves are labelled "shape illustrative".
- `dragoni2014`: "Show" and "tell", and those with no exceptional leader in their careers: exact.
- `ng2008`: Ten dimensions; no relation with task performance, creativity or training: exact.
- 70-20-10 Myth Check ("partly", moderate): fair. The origin story is honestly left out.
- Figures: Figure 20.1 is labelled "A thinking tool, not a measurement".
