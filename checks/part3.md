# Fact-check log: Part III (Chapters 18–22), the epilogue and the appendix

An adversarial check of every factual claim in Part III, *Making It Count*, in the epilogue and in the appendix *Left Out, on Purpose*: chapter text, figures, captions, exercise answers, Myth Checks, Receipts, Field Notes, Ask boxes and resource cards. The aim was to prove the book wrong, then fix what turned up. The writers had already checked their own claims, and this check assumed nothing they did.

Checked on 25 October 2026 in two batches: Chapters 18–20 as merged to `main` in #10, then Chapters 21–22, the epilogue and the appendix as merged in #12. For the appendix, the check also confirmed that every recommended resource exists as described, that its label is honest, and that its link works.

## Summary

| Verdict | Ch. 18–20 | Ch. 21–22, epilogue, appendix | All |
|---|---|---|---|
| Confirmed | 87 | 97 | 184 |
| Fixed (the sentence changed) | 11 | 10 | 21 |
| Downgraded (the grade shown to the reader was lowered) | 0 | 0 | 0 |
| Cut as unsupported | 0 | 0 | 0 |
| **Total** | **98** | **107** | **205** |

An "entry" is one source, with every claim in the chapter that cites it, plus one entry for each uncited factual claim found. A source cited in two chapters has an entry in each. No cited source turned out to be retracted, but one carries a formal correction that changes numbers the book printed (problem 1 below).

**The most serious problems found**

1. **Chapter 20's headline numbers came from an uncorrected paper.** Crossref lists a 2018 corrigendum to Macnamara, Hambrick and Oswald (2014), the meta-analysis behind the chapter's pause, figure, Receipts box, Myth Check and Rewind. The authors had misapplied an adjustment for dependent effect sizes. Corrected, deliberate practice explains 24% of performance differences in games (not 26%), 23% in music (21%), 20% in sports (18%), 5% in education (4%) and 1% in professions ("under 1%"), and 14% overall (12%). The professions estimate is not statistically significant (p = .377). All five places, the figure and its script now use the corrected figures and cite the corrigendum (`macnamara2018`, new in `book/sources/ch20.yaml`). The Receipts box gives the original numbers too. The chapter's argument is unchanged, and the pause's answer ("about 1%") still stands. The corrected 14% overall is also the figure Ericsson and Harwell cite, which the chapter already printed.
2. **The rater's-role finding was presented as settled (Chapter 18).** The chapter's headline evidence, Scullen, Mount and Goff (2000), found that whether a rater was a boss, a peer or a report added little to ratings. A refutation search found Hoffman et al. (2010), who reanalysed two other large 360-degree data sets with a different model and found that the rater's role explains much more variance, and general performance even less. The chapter's main point survives, and is even strengthened, but the "added only a little" clause now carries that caveat, in the text and in the Receipts box. The new source is in `book/sources/ch18.yaml`.
3. **A figure printed numbers the source does not give (Chapter 18).** Figure 18.2 labelled 6% and 4% of variance as "the rater's role". Those are the remainders after the three shares the abstract reports (62 + 21 + 11 and 53 + 25 + 18). The full text could not be opened to confirm the role effects. The segment is now labelled "the rest, including the rater's role", which is what the arithmetic supports.
4. **A study count overclaimed (Chapter 18).** "In six studies, overconfident people gained status" counted all six of Anderson et al.'s studies. Only Studies 1–3 tested status, Study 4 tested why, and Studies 5–6 tested the reverse direction. The sentence now says three, and a fourth.
5. **The Field Note misdescribed the chapter's own evidence (Chapter 19).** It said most of the chapter's evidence came from "US and Western European firms". The face-time study is from a Southeast Asian bank, the remote-work trials are from a Chinese firm, and none of the chapter's firm studies is from continental Europe. The text now names the bank's region and describes the evidence's origin correctly.
6. **A premise was presented as a conclusion (Chapters 20 and 22).** Kambourov and Manovskii (2008) document rising occupational mobility. That human capital is largely occupation-specific is a finding they cite from other work, not one this paper concludes. Both chapters now say so.
7. **A commercial, crowdsourced site carried an "Evidence-based" card (appendix).** The build labels a resource card from its source's `kind`, and Levels.fyi (`kind: data`, graded weak, flagged commercial) would have been printed as *Evidence-based*. It is now described in plain text without a card. The appendix's definition of *Evidence-based* was also narrower than the cards it labels: crisis lines and advice services are official public services, not research, statistics or law. The definition now includes them.
8. **A quotation was altered (Chapter 21).** Will Larson wrote that career ladders are "a tool that applies better against populations than people". The chapter printed "apply better against populations than people" inside quotation marks. It now quotes him exactly.
9. **Two findings were stretched beyond their samples (Chapter 22).** The boomerang-employee study covers managers rehired into one large data set, not "people who return to a former employer" in general. And Deming and Noray's "learning gains accumulate" is the explanation their model gives, not a separate finding. Both are now worded to match.
10. **A Field Note put the UK in the EU (Chapter 21).** After citing UK data, it said no data had been found for India "or elsewhere in the EU". It now says "India or the EU".

Smaller fixes, all listed below, include an uncited gloss replaced by the authors' own words, a narrowed population ("pay decisions" for "administrative decisions"), a trade-off no longer described as "a direct trade between mentoring and output", and five uncited claims now labelled as the book's view or softened.

## Method

- **Batched by source, two tiers.** As the book's owner asked for Part III, each source was opened once and every claim citing it was checked together:
  - a **full check** (open the source, compare direction, size, certainty, population, year and wording, and search for corrections, retractions, failed replications or newer reviews) for headline numbers, every Myth Check, regional facts, claims carrying a chapter's main advice and anything surprising;
  - a **light check** against the registry's `supports` note for background claims already graded strong or moderate, opening the source only where a number, a count or the wording went beyond the note.

  The truth rules did not loosen: no number or quote stayed in print without being checked against a source.
- **Sources opened.** In practice the abstract of every cited DOI was re-read (via OpenAlex, or nature.com where OpenAlex had none), because that was faster than deciding which ones to skip; the exceptions are `eby2008` and `ross1979`, which have no machine-readable abstract and were light-checked against the registry. Full texts were read for the working-paper numbers: NBER w24343 (Benson, Li and Shue 2018/2019), NBER w26530 (Cullen and Perez-Truglia), the authors' June 2022 working paper of Benson, Li and Shue's "Potential" paper, NBER w25065 (Deming and Noray), and O'Boyle and Aguinis (2012) on the author's site. Web pages were re-read for every quotation and web-sourced figure: SHRM on Microsoft, LeanIn.Org, the Harvard corporate-governance summary of Cohen et al., the Resolution Foundation, Dropbox, StaffEng, Tanya Reilly's *Being Glue*, The Pragmatic Engineer and 80,000 Hours in the first batch; HBR (Garvin; Hill), Paul Graham, Charity Majors, John Seely Brown's slides, Gardner Campbell's notes and the Atlanta Fed tracker in the second. The BLS Occupational Outlook Handbook refused scripted access, so its two medians were confirmed through search results quoting the pages. For the appendix, every resource link was requested, and every card's description was compared with its source (see that section). Retraction and correction status was checked for all 113 DOIs cited in Part III, the epilogue and the appendix, through Crossref's `updated-by` records and OpenAlex's retraction flag. One correction turned up (`macnamara2014`, problem 1); one DOI (`higgins2001`) has no Crossref record, and OpenAlex does not flag it.
- **Refutation searches.** These ran for every headline finding and Myth Check. The one that changed the text was Hoffman et al. (2010) against Scullen et al. (2000). Others found no newer evidence that contradicts what the book prints. The bell-curve and Dunning–Kruger boxes already present both sides, and the deliberate-practice box already includes Ericsson's reply.
- **Fixes were minimal.** Each kept the chapter's voice and its cross-references. No true claim was weakened to be safe.

**New sources added** (opened during this check): `hoffman2010` in `book/sources/ch18.yaml` and `macnamara2018` (the corrigendum) in `book/sources/ch20.yaml`.

**What could not be verified, and how the book handles it**

- **Scullen et al. (2000), full text.** Not openly available. The perspective-effect percentages are not in the abstract, so the figure no longer labels the remainder as the rater's role alone.
- **Hoffman et al. (2010), full text.** Read at abstract level only. The book prints no number from it.
- **Open Library records (appendix).** The four book cards that link to Open Library (Hill, Fournier, Greenhalgh, McDowell) could not be fetched: the site answered automated requests with a human-verification page or refused the connection. None returned "not found", and a search engine indexes `OL19860807W` as *The Manager's Path*. All four books were confirmed to exist as described through publisher, retailer and library listings. Whether each record still loads should be checked by hand in a browser.

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

### Problems found (3)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| macnamara2014 + macnamara2018 | Deliberate practice explained 26 / 21 / 18 / 4 / under 1% of performance variance in games, music, sports, education and professions (§practice; pause answer; Figure 20.2 and its alt text and caption; Receipts; Myth Check; Rewind) | full: abstract; Crossref `updated-by`; the 2018 corrigendum read in full | fixed | These are the original, uncorrected numbers. The corrigendum (Table 1) gives 24 / 23 / 20 / 5 / 1%, 14% overall, and professions r = .09, p = .377. Every place now uses the corrected figures and cites both papers; the Receipts box also gives the originals and the authors' statement that the substance of their conclusions did not change. The caption's "in every domain studied, deliberate practice mattered" became "in most domains", because the professions estimate is not significant. The pause answer ("about 1%") stands. Found by the correction scan run with the second batch. |
| kambourov2008 | US 1968–97 occupational mobility high and rising; "the authors conclude that human capital is largely occupation-specific" (§capital) | full: abstract | fixed | Mobility is confirmed. The specificity of human capital is cited in the abstract as "recent findings", not concluded by this paper. Reworded to say the authors note it matters because other research found human capital largely specific to an occupation or industry. |
| (uncited) | "Most people who end up very good at something did not plan it either" (opening) | none | fixed | A claim about most people with no source. Reworded as the book's suspicion ("Plenty of people … we suspect"). |

### Confirmed (27 entries)

Every claim citing these sources matched the source as read: `todd2026`, `newport2012`, `deming2020`, `ericsson1993`, `ericsson2019`, `macnamara2016`, `macnamara2019`, `quinones1995`, `sackett2022`, `choudhry2005`, `kahneman2009`, `derue2009`, `kluger1996`, `anseel2015`, `dunlosky2013`, `cepeda2006`, `clardy2018`, `johnson2018`, `allen2004`, `eby2008`, `dragoni2014`, `higgins2001`, `ibarra2010`, `flynn2008`, `okeefe2018`, `chen2015`, `ng2008`.

Notes on confirmed claims:

- `ericsson2019`: 29% (61% after correction for attenuation) against the 14% "reported by Macnamara, Hambrick, & Oswald (2014, 2018)": the book prints 29% and 14%, and 14% is the corrected overall figure. The Myth Check ("partly", strong) presents both camps.
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

## Chapter 21, The Fork: Expert or Manager?

### Problems found (5)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| larson2020 | No technical-leadership track at some companies; four Staff archetypes, Tech Lead about one per eight engineers; ladders "apply better against populations than people" (§fork; §expert; Myth Check) | full: live page | fixed | The page reads "career ladders are a tool that applies better against populations than people". The chapter's quotation had changed the verb. It now quotes exactly. The other claims match. |
| emanuel2026 | Proximity raised code feedback, gains among juniors; seniors wrote less code, "a direct trade between mentoring and output" (§job) | full: QJE abstract | fixed | The abstract reports "a trade-off: experienced engineers write less code"; that the time went on mentoring is the authors' interpretation (see Part II, 11.22). Reworded to "a trade-off between helping others and their own output". |
| (uncited) Field Note | "We did not find verified data on title … inflation in India or elsewhere in the EU" (Field Note, after UK data) | none | fixed | "Elsewhere" implied the UK is in the EU. Now "India or the EU". |
| (uncited) | "Most careers reach a fork like this one" (opening) | none | fixed | A prevalence claim with no source. Softened to "Many careers". |
| (uncited) | After the pendulum essay: "In many organisations it is not [permanent], provided you leave the door open" (§trial) | none | fixed | A claim about organisations with no source beyond one practitioner's view. Labelled as the book's view ([!view]). |

### Confirmed (22 entries)

Every claim citing these sources matched the source as read: `majors2017`, `allen1986`, `katz1995`, `garvin2013`, `hoffman2021`, `graham2009`, `benson2019`, `lazear2004`, `artz2017`, `dragoni2014`, `hill2007`, `todi2021`, `bls2026a`, `bls2026b`, `johnston2013`, `boyce2012`, `cohen2023`, `resolution2012`, `chan2001`, `kennedy2021`, `badura2020`, `ditella2010`.

Notes on confirmed claims:

- `majors2017`: "Is not a promotion", "a change of profession" and "like a pendulum" are on the live page. "Every few years" is a fair paraphrase of "never more than 2-3 years removed from hands-on work".
- `allen1986`: "Nearly 1,500 engineers and scientists in nine U.S. organizations": exact.
- `garvin2013`: The quotation ("ended up trying to prove the opposite case—that managers don't matter. Luckily, we failed"), "a third to half", the 2008 turnover and retention comparison and the behaviours are all on the HBR page. The chapter labels it weak, company-reported evidence.
- `hoffman2021`: Turnover effect, causal designs, inconsistent other outcomes, and rewards to good people managers: exact.
- `graham2009`: "Can blow a whole afternoon", one-hour intervals and half-day units are on the essay page.
- `artz2017`: The abstract confirms "U.S. and British data" and the within-job longitudinal result.
- `hill2007`: The HBR summary reads "Most new managers initially fail this test because of a set of common misconceptions". The chapter's "most initially struggle" is softer, not stronger, and fits a box that busts an untraceable "60% fail" figure. The Myth Check ("busted", weak) is honest: it rests on the absence of a primary source, and says so.
- `bls2026a`, `bls2026b`: $135,980 and $175,140 (May 2025) and "5 years or more" are confirmed through search results quoting the BLS pages (direct fetches refused, HTTP 403). The comparison is correctly caveated as two occupations' medians.
- `badura2020`: 100 primary studies, 1,154 effect sizes, three types "only modestly correlated", and links to emergence, behaviour and effectiveness: exact.
- `chan2001`, `kennedy2021`: The three-factor definitions match Kennedy et al.'s summary, which is cited for them.
- `ditella2010`: No machine-readable abstract; light-checked against the registry (working-paper abstract).
- The Myth Check "Management is the only way up" ("partly", moderate) is fair.
- Figures: Figure 21.2 is labelled "illustrative calendars, not data". Figures 21.1 and 21.3 restate the text.

## Chapter 22, The Whole Career

### Problems found (3)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| kambourov2008 | Occupational and industry moves common and rising, 1968–97; "[Chapter 20] drew the other half of that finding, that much of what you learn is specific to a kind of work" (§loops; Rewind) | full: abstract (as in Chapter 20) | fixed | Occupation-specific human capital is a finding the paper cites, not its own. Reworded to "the research those authors build on finds". |
| deming2020 | Premium for applied STEM majors falls by more than half in the first decade (working paper); flatter profiles; sorting out with age; "the authors find that ability matters relatively more in slower-changing careers because 'learning gains accumulate'" (§skills; Myth Check) | full: QJE abstract; NBER w25065 full text | fixed | The numbers are confirmed. The quoted clause sits in the working paper's sentence "Within the framework of the model, this is explained by …", so it is the model's explanation of a finding, not a finding. Reworded to "the authors' model explains why ability pays relatively more …". |
| arnold2021 | "People who return to a former employer" perform as well at first, improve less, are more likely to leave again, often for the same reasons (§strength) | full: abstract | fixed | The study covers 1,318 managers rehired into management positions, from one large longitudinal data set. Reworded to "In one large data set, managers rehired by a former employer …". |

### Confirmed (34 entries)

Every claim citing these sources matched the source as read: `bls-nlsy2025`, `lazear1981`, `ference1977`, `yang2019`, `brown2026`, `campbell2010`, `ng2008`, `quinones1995`, `blanchflower2021`, `galambos2020`, `davidson2010`, `sonnentag2012`, `deci2017`, `cerasoli2014`, `allan2019`, `bunderson2009`, `kim2020`, `hu2017`, `okeefe2018`, `chen2015`, `newport2012`, `kahneman2010`, `killingsworth2021`, `killingsworth2023`, `ditella2010`, `grund2007`, `boyce2013`, `wrzesniewski2001`, `oprea2019`, `grant2014`, `ng2005`, `atlantafed-wgt`, `bidwell2011`, `faberman2017`.

Notes on confirmed claims:

- `ference1977`: The quoted "early rapid upward mobility followed by inevitable leveling-off" is in the abstract.
- `yang2019`: No abstract via OpenAlex or Crossref; the White Rose repository abstract confirms 1977–2017, 72 empirical sources, the two plateau types, the moderators and the antecedents.
- `brown2026`, `campbell2010`: The slide text "(perhaps as low as 5 years)" and the attendee's note "Most skills we teach have a half-life of about five years" are both exact. The half-life Myth Check ("partly", strong) is fair: the decay is strongly evidenced, the number is not.
- `cerasoli2014`: k = 183, N = 212,468; quality versus quantity; crowding out: exact.
- `killingsworth2021`: 1,725,994 reports from 33,391 employed US adults: "1.7 million" and "more than 33,000" are right.
- `boyce2013`: Germany (N = 28,723) and the UK (N = 20,570): "large German and British samples" is right.
- `oprea2019`: 14 studies; g = 0.26, 0.31 and 0.39; task-performance gains only in healthcare: exact.
- `grant2014`: Study 2 was "a field quasi-experiment within a health care system": exact.
- `davidson2010`: 129 sabbatees and 129 matched controls; the moderators match.
- `allan2019`: Figure 22.2's ranges (r ≥ .70; .44 to .49; up to .33) match the abstract.
- `okeefe2018`: The "eggs in one basket" quotation is exact. The passion Myth Check ("partly", moderate) is fair.
- `atlantafed-wgt`: "Usually beats stayers', but by a small margin … shrinks when the market is slack" matches the Part I recomputation of the tracker data (switchers ahead in 91% of months, by 0.73 points on average; behind from mid-2009 to late 2010; see `checks/part1.md`, 2.8–2.9).
- `bidwell2011`: Abstract confirms around 18% more pay and better early performance for promoted workers. "Because they start the long game from zero" is the book's gloss on the paper's specific-skills explanation.
- `blanchflower2021`, `ditella2010`: No machine-readable abstract; light-checked against the registry.
- Figures: Figures 22.1 and 22.3 restate the story; Figure 22.2 is checked above.

## Epilogue, The Loop

### Confirmed (1 entry)

The epilogue makes no new factual claims. The one generalisation ("a good reference is just a trailer someone else cuts from your film …") is labelled as the book's view. The fourteen scorecard statements match Chapter 1's, word for word. Out of this check's scope, and reported rather than changed: Chapter 1's exercise is headed "Your two scorecards" but lists three, which the epilogue's "Your three scorecards, revisited" makes visible.

## Appendix, Left Out, on Purpose

### Problems found (2)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| levelsfyi | Resource card: crowdsourced pay by company, level and location, weighted by proof (§pay-data) | full: About page; the build's label rule (`tools/bookkit/render.py`) | fixed | The card's text was accurate, but the build prints **Evidence-based** on any card whose source is `kind: data`, and this source is commercial, self-reported and graded weak. Moved out of a card into a plain paragraph that says it is self-reported and commercial. |
| (uncited) | "Each card is labelled by what it rests on: Evidence-based (research, official statistics or law)" (introduction) | checked against the cards | fixed | Several cards labelled *Evidence-based* are official public services, not research, statistics or law (the 988 Lifeline, NHS talking therapies, Tele-MANAS, Acas, Investor.gov, SEBI). The definition now reads "research, official statistics, the law, or an official public service", which matches what is labelled. |

### Confirmed (40 entries)

Every resource below exists as described, its label is honest, and its link responded, except as noted: `hill2019`, `fournier2017`, `zhuo2019`, `hoffman2021`, `camuffo2020`, `wasserman2013`, `govuk-selfemployed`, `sba-guide`, `startupindia`, `lusardi2014`, `investorgov`, `govuk-workplace-pensions`, `sebi-investor`, `acas`, `eeoc-charge`, `dol-whd`, `youreurope-work`, `india-osh-code`, `uscis-work`, `govuk-workvisas`, `eu-immigration-portal`, `india-evisa`, `who2022-mhwork`, `nhs-talking`, `lifeline988`, `telemanas`, `bls-oews`, `ons-ashe2025`, `eurostat-ses`, `techinterviewhandbook`, `mcdowell2025`, `behroozi2020`, `barrick1991`, `pittenger2005`, `ipip`, `greenhalgh2024`, `osc2015`, `retractionwatch`, `bergstrom2020`, `openalex`.

Notes on confirmed resources:

- **Links.** 29 pages returned HTTP 200, `sba-guide` by way of a redirect to the SBA counselling page that carries the guide. The five DOIs (`barrick1991`, `camuffo2020`, `hoffman2021`, `lusardi2014`, `osc2015`) resolve at doi.org to the publisher (HTTP 302); the publishers refuse scripted requests, which is not a dead link. `bls-oews` and `dol-whd` refuse scripted requests (HTTP 403); both were read through a web-fetch tool during research, and the BLS site was confirmed live through search in this check. Princeton University Press refused scripted requests, but the page loads through a web-fetch tool. The four Open Library links are covered under "What could not be verified".
- `hill2019`: Nineteen new managers through their first year (O'Reilly listing of the HBR Press 2019 edition). Labelled *Evidence-based*: it is qualitative research, and the card says so ("the research-based place to start").
- `fournier2017`, `zhuo2019`, `techinterviewhandbook`, `mcdowell2025`: Labelled *Practitioner view*, correctly. Fournier went from tech lead to CTO (retailer listings). Zhuo became a manager at 25 (publisher and retailer descriptions; her own book page does not say so). The interviewing.io post confirms McDowell, Mroczka, Lerner and Mamano and the free chapters, and Lerner runs interviewing.io, the mock-interview company the card mentions.
- `wasserman2013`: "Almost ten thousand founders" is on the publisher's page.
- `camuffo2020`: The abstract confirms a randomised trial with 116 Italian startups over about a year, with the same general training for both groups.
- `acas`: Template letters and dispute resolution "without going to an employment tribunal" are on the Acas pages.
- `eeoc-charge`: The page gives the 180- and 300-day filing deadlines, so "including deadlines" is right.
- `lifeline988`: "The 988 Lifeline is available 24/7/365", free and confidential, by call, text or chat: on the live site.
- `telemanas`: 14416, 24x7, 20 languages: from the PIB release (the Tele-MANAS site failed a certificate check during research).
- `india-osh-code`: Effective 21 November 2025, per the PIB release recorded in the registry.
- `investorgov`: The site has a "How to Avoid Fraud" section, as the card says.
- `bls-oews`, `ons-ashe2025`, `eurostat-ses`: About 830 occupations; ASHE by occupation and industry; the Structure of Earnings Survey is four-yearly: all match the registry.
- `barrick1991`: "Later re-analyses have revised many of the field's estimates, as Chapter 1 explains": Chapter 1 explains the Sackett et al. (2022) revision.
- `behroozi2020`: Watched students did less than half as well: matches the registry (48 students, randomised).
- `osc2015`: Effects "half the size of the originals on average": matches the abstract.
- `greenhalgh2024`: The 7th edition (Greenhalgh and Dijkstra, Wiley, 2024) is confirmed in publisher and library listings.
- `bergstrom2020`, `greenhalgh2024`, `lusardi2014`, `pittenger2005`: `kind: review`, labelled *Evidence-based*. That is fair for a review article and for two research-methods books by working scientists.
- The appendix's map figure shows the same ten topics as its ten sections.
