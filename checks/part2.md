# Fact-check log: Part II (Chapters 10–17)

An adversarial check of every factual claim in Part II, *The Long Game*: chapter text, figures, captions, exercise answers, Myth Checks, Receipts, Field Notes and Ask boxes. The aim was to prove the book wrong, then fix what turned up. The writers had already checked their own claims, and this check assumed nothing they did.

Checked on 25 October 2026 against the chapters as merged to `main` in #6 and #7.

## Summary

| Verdict | Entries |
|---|---|
| Confirmed | 194 |
| Fixed (the sentence changed) | 44 |
| Downgraded (the grade shown to the reader was lowered) | 1 |
| Cut as unsupported | 0 claims cut whole; several unsupported clauses were removed inside "fixed" entries |
| **Total** | **239** |

An "entry" is one claim for Chapters 10–15 and one source (with every claim citing it) for Chapters 16–17, after the method change described below. No cited source turned out to be retracted, apart from the one the book already cites *as* a retraction.

**The most serious problems found**

1. **The chameleon finding was overstated (Chapters 10 and 14).** The book said that self-monitors ("chameleons") impress the people above and beside them but not the people below. The 2025 meta-analysis it cites (`lei2025`, read in full) does not show that. Supervisors' ratings of leadership effectiveness were not significant either, and the differences between rater groups were not significant. The only ratings that favoured chameleons were their own. The passages, an exercise answer and two Rewind bullets now say so.
2. **A misattributed study (Chapters 10 and 16).** Both chapters said Porath and Erez (2007) showed that merely *witnessing* rudeness hurts performance. The paper (read in full) tested rudeness aimed at the participant and imagined rudeness, and lists witnessing as future research. The witnessing result is their 2009 follow-up, now cited for it.
3. **"Warmth is judged first" was presented as settled (Chapters 10 and 11).** A replication of the classic Asch studies behind it (Nauts et al., 2014) found no primacy-of-warmth effect. The claim now reads as a tendency, and the replication is cited.
4. **A gender finding was generalised (Chapters 10, 12 and 17).** Bolino and Turnley (2005) found the link between going beyond your role and *work-family conflict* was stronger for women. The book said the costs in general fell more heavily on women. All three places are corrected.
5. **Boundary conditions added from nowhere (Chapters 11 and 14).** The "red sneakers" paper's boundary conditions are observer familiarity, intentionality and shared norms. The book added "the person's standing is already secure", which is not in any accessible text of the paper. It was removed as a finding in four places, and the inference is kept, labelled as the book's view.
6. **Two Field Note and table numbers were wrong.** The EU Whistleblower Directive covers private entities with *50 or more* workers, not "more than 50" (Chapter 16). In the Ctrip trial, *half of the home workers* returned to the office, not "over half the volunteers" (Chapter 14). Pew's 48% for childcare is among quitters *with children under 18*, not all quitters (Chapter 17).
7. **The generations Myth Check was upgraded (Chapter 14).** Its age-and-tenure clause rested on a blog paraphrase, and the meta-analysis predates Gen Z. The clause now cites the 2020 National Academies consensus report, which concludes that generational categories are not supported by research. On that evidence the verdict moved from "partly" to "busted".
8. **One grade was lowered (Chapter 15).** The Dunbar's-number Myth Check graded a single, contested statistical reanalysis "strong". It is now "moderate". An uncited "Dunbar disputes it" was replaced.

Smaller fixes, all listed below, include unsourced hedges replaced with sourced ones, causal wording on correlational studies, practitioner advice now labelled, absence claims reworded as "we found no…", and a quotation printed as Gallup's question wording that is not on Gallup's page.

## Method

- **Sources opened.** Every source was re-opened during this check, not taken from the registry's `supports` note. That meant abstracts via OpenAlex, Crossref, Europe PMC and publisher pages; full texts where open (PubMed Central, author-hosted PDFs, NBER); and official pages for every legal claim. Retraction and correction status was checked for every DOI through Crossref's `updated-by` records and OpenAlex's retraction flag. Corrections that exist are noted where relevant (Fiske 2002, Yang 2022, Cable 2013, Kish-Gephart 2010, Fredrickson 2005).
- **Refutation searches.** For headline findings, every Myth Check and anything surprising, a search was run for failed replications, critiques and newer reviews. Those searches produced the Nauts (2014), Corns (2018), Flynn (2003, OBHDP) and National Academies (2020) additions.
- **Method change partway through.** After Chapter 15 the book's owner asked for a faster, batched check. Chapters 16 and 17 were checked one source at a time, in two tiers:
  - a **full check** (open the source and search for refutations) for headline numbers, Myth Checks, legal facts and surprising claims;
  - a **light check** against the registry's `supports` note for background claims already graded strong or moderate, opening the source only if the wording or a number differed.

  The truth rules did not loosen: no number or quote was printed without being checked against a source.
- **Fixes were minimal.** Each kept the chapter's voice and its cross-references. No true claim was weakened to be safe. Where a fix needed a new source, the source was opened and added to that chapter's `book/sources/chNN.yaml`.

**New sources added** (all opened during this check):

- `porath2009`, `nauts2014`, `corns2018` and `flynn2003-time` in `book/sources/ch10.yaml`
- `manycoauthors-cable2013` in `book/sources/ch11.yaml` (new file)
- `nasem2020-generations` and `nber-digest2013-wfh` in `book/sources/ch14.yaml` (new file)
- `osborneclarke-whistleblowing` in `book/sources/ch16.yaml`

**What could not be verified, and how the book handles it**

- **Cable, Gino and Staats (2013).** Crossref lists a 2024 "Editor's Note" against it. The note's text is behind SAGE and was not read, so the book does not describe it.
- **Grandey (2003).** The sample could not be confirmed, so the book no longer names it.
- **Bellezza et al. (2014).** No accessible text shows that prior standing was tested.
- **EU Directive Article 8(3).** The threshold comes from a law firm's quotation of the Article and from the legislation.gov.uk copy surfaced in search; EUR-Lex refused automated access. The book says it read secondary sources.
- **Costanza et al. (2012).** The abstract was not readable (Springer blocked access). Its numbers are confirmed through two independent summaries.

Each chapter section below lists the problems found (one row each, with the source opened), then the sources whose claims were confirmed, with notes where a confirmation needed explaining.

## Chapter 10, First Principles: Trust Is the Whole Game

### Problems found (13)

| # | Claim (where) | Source opened | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| 10.3 | Indirect reciprocity evolves through reputation if chance of knowing reputation is "high enough relative to the cost of helping" (§shadow) | nowak1998 (title/record); nowak2006: full text on PMC (PMC3279745), rule q > c/b | fixed | The condition is relative to the cost-to-benefit ratio, not cost alone. Reworded; nowak2006 added as the citation for the rule. |
| 10.6 | Spirit of Axelrod's winning strategy: cooperate first, respond, forgive, be clear (§shadow, item 3) | axelrod1981 (abstract); nowak2006 full text | fixed | Had no citation. Added [@axelrod1981]. Nowak 2006 reports tit-for-tat's weakness: it cannot correct mistakes, and more forgiving strategies (generous tit-for-tat, win-stay lose-shift) do better when players err. Added one sentence: it strengthens the chapter's "forgive quickly" point. |
| 10.8 | "A high reading on one does not make up for a low reading on another" (Figure 10.2 caption, Rewind) | mayer1995 (abstract), colquitt2007 (abstract; a later secondary source reports the three dimensions intercorrelate above .60) | fixed | Not supported: the model and the meta-analysis treat the three as separable, additive predictors, not non-compensatory. Reworded to "a high reading on one does not guarantee the others". |
| 10.10 | Trust Equation formula; "Nobody has validated it" (Craft Note) | maister2000: trustedadvisor.com page (founder Charles H. Green, first in The Trusted Advisor, 2000); web search for validation studies found none | fixed | An absence claim; reworded to "We found no published validation of it". Formula confirmed. |
| 10.12 | "Warmth tends to be judged first" (§warmth; Ask box; Rewind) | fiske2007; nauts2014: abstract (OpenAlex/Hogrefe) | fixed | Refutation search found Nauts et al. (2014), a replication of the Asch studies usually cited for primacy of warmth: no primacy-of-warmth effect; warmth's role was context-dependent and competence at least as important. Added the caveat and source; softened "is judged first" in the Ask box and Rewind. |
| 10.13 | Others' warmth weighs more when judging others, competence when judging self (§warmth) | abele2007: abstract | fixed | Confirmed, but the same paper's Study 4 found another person's competence matters more when your outcomes depend on them, which describes colleagues. Added a short clause so the punchline does not overreach. |
| 10.14 | Bad is stronger than good; "some findings weakened, but broad asymmetry widely accepted" (§asymmetry) | baumeister2001: abstract; corns2018: full text (PMC6132407) | fixed | Review confirmed. The hedge was unsourced. Replaced with a sourced one: Corns (2018) states the principle is widely accepted and argues, on conceptual grounds, that it should be rejected. |
| 10.15 | Rudeness experienced, "or merely witnessed", or imagined lowered performance and helpfulness (§asymmetry) | porath2007: full text (people.uncw.edu PDF); porath2009: Crossref record + BPS Research Digest summary | fixed | Misattribution. The 2007 studies tested rudeness aimed at the participant (by the experimenter, then by a stranger) and imagined rudeness, and the paper lists "do witnesses of rudeness also decrease their task performance?" as future research. Witnessing is the 2009 follow-up. Split the sentence and added porath2009. |
| 10.21 | Favour returned after 5 minutes, not after a week; "you do not need to keep score, and neither does anyone else" (§reciprocity; Ask box; Rewind "fades within days") | burger1997: abstract; flynn2003-time: Stanford GSB abstract | fixed | Finding confirmed. "Neither does anyone else" overreached: Flynn (2003, OBHDP) found givers value a favour more as time passes while receivers value it less. Replaced with that sourced point. Rewind's "within days" corrected to "within a week" (only 5 minutes and 1 week were tested). |
| 10.24 | Helping time comes out of task time, which rewards track (§reciprocity) | bergeron2007: abstract | fixed | Stated as fact; the source is a theory paper that proposes it. Reworded as Bergeron's argument. |
| 10.25 | 98 couples; initiative → overload, stress, work-family conflict; "the link was stronger for women" (§reciprocity) | bolino2005: abstract | fixed | The gender difference was found only for work-family conflict. Made specific. |
| 10.29 | Self-monitoring linked to leadership "except, usually, when rated by subordinates"; "the people above and beside a chameleon like what they see" (§chameleons; Your Move 10.3 answer; Rewind) | lei2025: full text (PMC12130612), Table 3 and Discussion | fixed | The most serious problem in this chapter. The "subordinates" clause is right, but the study does not show bosses and peers are impressed. Supervisor ratings of leadership effectiveness were also non-significant (rho = .071, CI −.019 to .160), and subordinate–peer and subordinate–supervisor differences were not significant (H3 and H6 not supported). The authors conclude self-monitoring is positively related only to *self-rated* effectiveness. Rewrote the passage, the Your Move answer and the Rewind bullet to say this. |
| 10.35 | Coworker-rated delivery worse with surface, better with deep acting; only surface acting related to stress; "a study of service employees" (§acting) | grandey2003: abstract (Penn State record, via search) | fixed | Findings confirmed verbatim. The sample was not verifiable from any accessible page, so "of service employees" became "In a field study". |

### Confirmed (25 entries)

Every claim citing these sources matched the source as read: `axelrod1981`, `dalbo2005`, `nowak2006`, `fehr2000`, `mayer1995`, `colquitt2007`, `fiske2007`, `fiske2002`, `andersson1999`, `brown2013`, `gouldner1960`, `regan1971`, `cialdini2004`, `flynn2003`, `podsakoff2009`, `snyder1974`, `day2002`, `kilduff1994`, `fleeson2010`, `sutton2020`, `cha2019`, `ibarra2015`, `hochschild1983`, `hulsheger2011`, `psychsci2023-retraction`.

Notes on confirmed claims:

- `axelrod1981`: Matches abstract wording.
- `dalbo2005`: Lab money game; text already labels it an analogy.
- `fehr2000`: Cross-cultural variation (antisocial punishment) noted in registry caveats; not overclaimed here.
- `colquitt2007`: Correlational caveat already in text.
- `fiske2007`, `fiske2002`: The correction to Fiske et al. (2002) fixes missing minus signs in one paragraph; it does not touch the claims used.
- `andersson1999`: Theory paper, described as theory.
- `regan1971`: Direction only, no multiplier printed. Good.
- `cialdini2004`: The abstract supports "outside of awareness". Reciprocation's place in the review is confirmed only by a secondary summary; full text paywalled.
- `flynn2003`: "Give first, give small, give often" is the author's reading; tagged [!view].
- `podsakoff2009`: Halo caveat already present.
- `day2002`: Abstract gives no effect sizes; "slightly" is conservative and consistent with lei2025's "modest".
- `kilduff1994`: Internal promotions were among the 72 who stayed.
- `cha2019`: Quote exact.
- `ibarra2015`: Labelled as an essay.
- `psychsci2023-retraction`: Verdict "busted" is fair: the only evidence for the claim is retracted.
- Figures: Illustrative numbers are labelled as such.

## Chapter 11, The First Ninety Days

### Problems found (7)

| # | Claim (where) | Source opened | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| 11.9 | 135 new staff accountants over six months; information-seeking "became better at their jobs" (§clarity) | morrison1993: abstract | fixed | The source reports that seeking frequency *was related to* mastery, role clarity, culture and integration. Reworded from "became better" to "had mastered … better" to avoid implying cause. |
| 11.14 | "Most people like being asked something they know, and find it uncomfortable to refuse" (§asking) | flynn2008: abstract | fixed | The second half is the paper's mechanism; the first half had no source. Rewrote as "saying no to someone's face is uncomfortable, so people say yes far more often than you expect". |
| 11.15 | Warmth judged first (flashback; §impressions) | fiske2007; nauts2014 | fixed | Same caveat as 10.12: "often" and "mostly true", with nauts2014 cited. |
| 11.16 | Face judgements formed after 100 ms and "barely changed with more time"; extra time mostly adds confidence (§impressions) | willis2006: abstract | fixed | Mostly right, but judgements did change: from 100 to 500 ms they became more negative and more differentiated. What held was that the 100 ms judgements correlated highly with untimed ones. Reworded to say that. |
| 11.22 | Fortune 500 engineers: proximity +18.3% feedback, better code, gains for juniors; seniors wrote less code "because they spent time mentoring" (§proximity) | emanuel2026: abstract; NBER w31880 full text (revised June 2026) | fixed | Numbers confirmed. The paper calls the seniors' lower output "consistent with mentorship consuming a meaningful share of their time"; softened "because" to "apparently because". |
| 11.24 | Red-sneakers effect works only when observers know the norms, see it as deliberate, "and the person's status is already secure" (§calibrate) | bellezza2014: abstract; replication search | fixed | The abstract's boundary conditions are familiarity with the setting, intentionality and shared norms; "status already secure" is not in it and could not be verified from any accessible page. Cut that condition; added a labelled [!view] line keeping the paragraph's logic. No replication or failure found. |
| 11.25 | Best-self onboarding in an Indian BPO raised customer satisfaction and six-month retention (§best-self) | cable2013: abstract; Crossref record (a 2024 "Editor's Note" registered as a correction); manycoauthors-cable2013: Many Co-Authors page | fixed | Finding confirmed. Crossref lists a July 2024 Editor's Note against the paper; its text sits behind SAGE (HTTP 403) and could not be read, so the book does not describe it. The Many Co-Authors page shows the co-authors report Gino did not collect the field data and that they hold it and replicated the results (the lab study's data are missing). Added that, labelled as the authors' own unverifiable report. |

### Confirmed (19 entries)

Every claim citing these sources matched the source as read: `watkins2003`, `bauer2007`, `lii-atwill`, `govuk-notice`, `bgb622`, `khaitan-notice`, `ashford1996`, `anseel2015`, `brooks2015`, `flynn2008`, `gilovich2000`, `savitsky2001`, `boothby2018`, `mastroianni2021`, `epley2014`, `glikson2018`.

Notes on confirmed claims:

- `watkins2003`: Practitioner; flagged `!` inline.
- No research finds ninety days is a threshold (§ninety; Myth Check): Worded as "we found no research", which is honest. Verdict "busted", grade moderate, fair.
- `govuk-notice`: Employee rule from "Giving notice"; employer minimum (one week from one month to two years) from the notice-periods page the registry also lists.
- `bgb622`: Basic notice is four weeks to the 15th or end of a month; "basic four weeks" is a fair compression.
- `khaitan-notice`: Source says senior roles 3–6 months.
- `bauer2007`: "Clarity, competence, connection" is labelled the book's shorthand. Correlational caveat present.
- `brooks2015`: No independent replication or failure found. The co-author caveat is in the text.
- `mastroianni2021`: The registry had not retrieved the abstract; it is now read and matches.
- Figures: Figure 11.3 is labelled practitioner advice; Figure 11.2's bar lengths are labelled illustrative.

## Chapter 12, Reliability, the Boring Superpower

### Problems found (5)

| # | Claim (where) | Source opened | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| 12.1 | "Competence problems are forgiven quickly"; integrity problems "are not" (§cheapest) | lewicki2016: abstract; kim2004: abstract | fixed | Uncited and stated absolutely. Reworded to "relatively easy to repair … harder", citing lewicki2016, whose abstract reports apologies worked better after competence-based than integrity-based violations. |
| 12.6 | "People who bring a recommendation … are much easier to say yes to" (Your Move 12.2 answer) | n/a | fixed | Practitioner advice stated as fact; tagged [!craft]. |
| 12.12 | Superfluous apologies "increased trust a little" (§apology) | brooks2014: abstract; BPS Research Digest summary (14 Oct 2013) | fixed | The source does not describe the effects as small. The field study's effect was large (47% vs 9% lent a phone), and the lab studies used neutral-greeting controls; the digest notes the field study had no such control. Removed "a little"; softened the mechanism to "apparently". |
| 12.17 | Helping costs "fall more heavily on women" (§no) | bolino2005: abstract | fixed | As 10.25: only the work-family-conflict link was stronger for women. Made specific. |
| 12.23 | "Reliability turns out to be one of the things reviews reward most consistently" (Coming Up box) | none found | fixed | No source in the chapter or in research/part3. Cut the claim; kept "one of the easiest things to evidence in a review". |

### Confirmed (19 entries)

Every claim citing these sources matched the source as read: `buehler1994`, `smith2001`, `whillans2022`, `savitsky2001`, `gilovich2000`, `baumeister2001`, `aronson1966`, `kim2004`, `lewicki2016`, `schumann2018`, `edmondson1996`, `vandyck2005`, `flynn2008`, `givi2024`, `babcock2017`, `graen1995`, `dulebohn2012`, `gabarro1980`, `burris2012`.

Notes on confirmed claims:

- Commitment loop; reliability as cheapest trust (§loop; Author's View): Labelled [!craft] / Author's View.
- `buehler1994`: Every sub-claim matches the abstract (Studies 3–5). Student samples caveat already in text.
- `smith2001`: Registry also notes a close replication (Petter et al. 2016).
- `whillans2022`: N = 4,151.
- `aronson1966`: Verdict "partly", grade weak: fair. Later studies on gender and self-esteem moderators exist, which only strengthens "do not count on it".
- `lewicki2016`: The chapter correctly declines to name a top component.
- `edmondson1996`: The interpretation caveat is already in the text.
- `vandyck2005`: Correlational caveat present.
- `givi2024`: Social-invitation caveat present.
- `graen1995`, `dulebohn2012`: The in-group/out-group gloss is a standard description of the theory; no number or quote rests on it.
- `gabarro1980`: Labelled practitioner.
- Figures: Figure 12.2 is labelled "illustrative shapes, not data".

## Chapter 13, Talking and Writing at Work

### Problems found (4)

| # | Claim (where) | Source opened | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| 13.8 | Exclamation marks "mostly worked as markers of friendliness" (§emoji) | waseleski2006: abstract | fixed | The abstract says they *rarely* marked excitability and *may* mark friendly interaction. Reworded to "rarely signalled excitability and often seemed to mark friendliness". |
| 13.18 | Self-aimed feedback is "where a third of feedback goes wrong"; "mostly when it points at the self" (§feedback; Your Move 13.3 answer; Rewind) | kluger1996: abstract | fixed | These lines turned the authors' explanatory theory into a measured attribution, contradicting the chapter's own Receipts box ("an interpretation, not a direct measurement"). Reworded all three as the review's best explanation. |
| 13.19 | Myth: feedback sandwich is best (busted, weak); students believed it helped "but their performance did not actually improve" (Myth Check) | parkes2013: abstract (Europe PMC: two studies, N = 20 and N = 350) | fixed | The abstract says there was "no evidence" sandwiches improved performance, not that performance was shown not to improve. Reworded to match. |
| 13.21 | "People rarely volunteer useful feedback to colleagues" (§receiving) | none | fixed | Unsourced generalisation; tagged [!view]. |

### Confirmed (19 entries)

Every claim citing these sources matched the source as read: `shulman2024`, `kruger2005`, `giurge2021`, `becker2021`, `belkin2020`, `glikson2018`, `kumar2018`, `grant2010`, `rogelberg2010`, `mullen1991`, `burris2012`, `morrison2014`, `dewit2012`, `bushman2002`, `kluger1996`, `scott2017`, `anseel2015`.

Notes on confirmed claims:

- `shulman2024`: Labelled an analogy.
- Point-first habits (Craft Note): Labelled [!craft].
- `becker2021`: The "independent of time spent" clause was not in the abstract; the paper's methods confirm the control.
- `grant2010`: Co-author caveat present.
- `mullen1991`: Fewer ideas and lower quality than nominal groups; loss grows with group size.
- `bushman2002`: Rumination group angriest and most aggressive; doing nothing did best.
- `scott2017`: Practitioner and commercial flags shown.
- Figures: Figure 13.3's bar is labelled "segment sizes approximate".

## Chapter 14, The Professionalism Dial

### Problems found (5)

| # | Claim (where) | Source opened | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| 14.5 | Self-monitoring–leadership link disappears with subordinate raters; "adapting helps you get noticed by the people above and around you … does much less for how the people who work for you experience you" (§not-fake) | lei2025: full text (PMC12130612), Table 3 and Discussion | fixed | Same overreach as 10.29. Supervisors' effectiveness ratings were also non-significant; only self-ratings favoured chameleons. Rewritten. |
| 14.10 | "Once a relationship exists, casual markers mostly read as friendliness"; exclamation marks "mainly worked as signs of warmth" (§notch) | waseleski2006: abstract | fixed | The study (200 exclamations on two professional discussion lists) says nothing about established relationships, and its abstract says exclamations *may* mark friendliness. Reworded here, and the same "once a relationship exists" framing was corrected in Chapter 13. |
| 14.11 | Red sneakers: deliberate non-conformity raises status only when observers know the norm, see it as deliberate "and already credit you with standing" (§notch; Author's View in §code-switching; Rewind) | bellezza2014: abstract (OpenAlex; OUP page, full text paywalled) | fixed | The abstract's boundary conditions are observer familiarity, intentionality and shared norms. Prior standing is not among them, and no accessible text shows it was tested. Removed it as a finding in all three places. The inference that it is easier for the established is kept, labelled as the book's reading. |
| 14.35 | Myth: Gen Z and millennials fundamentally different (partly, moderate); "some apparent differences reflected age or time in the job" (Myth Check) | costanza2012: secondary summaries (NeoAcademic, ScienceForWork; Springer page blocked); nasem2020-generations: National Academies press release and report page | fixed | The 20 studies / 19,961 workers / "small to near zero" result is confirmed. The age-or-tenure clause was found only in a blog's paraphrase, so it now cites the 2020 National Academies consensus report, which says exactly that. The meta-analysis compared Traditionals, Boomers, Gen X and Millennials, not Gen Z; the text now says so. With the National Academies verdict that generational categories are "not supported by research", the verdict moves from "partly" to "busted". |
| 14.36 | Ctrip: nine months WFH, +13% performance, attrition halved, promotion rate fell given performance, "over half the volunteers later chose to return to the office" (table) | bloom2015: abstract; nber-digest2013-wfh: NBER Digest summary | fixed | The abstract says "over half of them switched", meaning all experimental employees, in either direction. The NBER Digest says *half of the home workers* chose to return, citing loneliness and promotion. Corrected and sourced. |

### Confirmed (40 entries)

Every claim citing these sources matched the source as read: `kruger2005`, `gelfand2011`, `day2002`, `fleeson2010`, `hulsheger2011`, `ibarra2015`, `glikson2018`, `defrank2019`, `baruch2007`, `mesmermagnus2012`, `bitterly2017`, `evans2019`, `kim2004`, `ashforth2000`, `kreiner2006`, `rothbard2005`, `sutton2020`, `gibson2018`, `phillips2009`, `cha2019`, `burris2012`, `ragins2008`, `mccluney2021`, `mccluney2019`, `hewlin2003`, `hofstede2011`, `meyer2014`, `taras2010`, `taras2016`, `bloom2024`, `yang2022`, `emanuel2026`, `gibbs2023`, `gajendran2007`, `elsbach2010`, `cristea2019`, `bernstein2018`.

Notes on confirmed claims:

- Dial, not costume; "our argument, not a finding" (§dial; Figure 14.1): Labelled [!view].
- `ibarra2015`: Labelled an essay.
- `baruch2007`: Qualitative; flagged `!`.
- Humour ladder (Figure 14.3): Labelled "our ranking … not a measured scale".
- `rothbard2005`: Satisfaction and commitment.
- `phillips2009`: Theory, described as such.
- `ragins2008`: Theory.
- `mccluney2021`: The design manipulated speech, name and hairstyle; the book's summary is fair.
- `mccluney2019`: Caveat present.
- `hewlin2003`: Theory.
- `meyer2014`: Practitioner and commercial flags shown.
- `taras2016`: Dimension-level splits (e.g. 83.4% within for individualism) in the NC State press release match.
- `yang2022`: The 2021 correction fixes a colour-key label in Fig. 1 only.
- Figures: Figure 14.4 is labelled "illustrative curves"; its 80/20 bar matches taras2016.

## Chapter 15, Office Friendships

### Problems found (4)

| # | Claim (where) | Source opened | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| 15.10 | Myth: about 150 relationships (busted, strong); reanalysis CIs about 2 to 520; "Dunbar disputes the reanalysis" (Myth Check) | lindenfors2021: abstract (CIs 4–520 and 2–336) | downgraded | Numbers confirmed. The grade shown was "strong" for a single statistical reanalysis of a contested method; lowered to "moderate". "Dunbar disputes the reanalysis" had no source and no published reply was found in a search; replaced with "That is one reanalysis, and the argument is not over". The verdict stays "busted": the claim as stated, a fixed limit derived from brain size, is not supported by its own method. |
| 15.11 | ~1 in 5 employees lonely "a lot of the day yesterday": 25% remote, 21% hybrid, 16% on-site (§loneliness; Rewind) | gallup2024: Gallup article; Gallup press release (via search) | fixed | Percentages confirmed. The quoted phrase is not on the article page, so it is no longer printed as a quotation; paraphrased as "a lot of loneliness on the previous day", matching Gallup's press release. |
| 15.13 | "Working from home is not the cause of loneliness for most people" (§loneliness) | gallup2024 | fixed | Uncited causal claim. Replaced with a sourced descriptive one: three-quarters of fully remote workers in Gallup's data did not report loneliness. |
| 15.24 | "Many companies require such relationships to be disclosed" (§romance) | none | fixed | A prevalence claim in the same paragraph that says "we found no reliable data on how common particular policies are". Rewritten as the book's labelled view of what a sensible policy does. |

### Confirmed (25 entries)

Every claim citing these sources matched the source as read: `methot2016`, `pillemer2018`, `gallup2022`, `hall2019`, `boothby2018`, `mastroianni2021`, `epley2014`, `flynn2008`, `jecker1969`, `niiya2016`, `ozcelik2018`, `dorescruz2021`, `robbins2020`, `feinberg2012`, `feinberg2014`, `bushman2002`, `sayette2012`, `frone2006`, `peters2006`, `shrm2023`, `malachowski2012`, `pierce1996`, `sonnentag2012`, `givi2024`, `sias2004`, `graen1995`, `dulebohn2012`.

Notes on confirmed claims:

- `pillemer2018`: Theory, described as such.
- `gallup2022`: The chapter already treats it as a claim from a commercial, self-interested source.
- Four-stop friendship map (Figure 15.1): Labelled "ours, not a research instrument".
- `hall2019`: The release states the three figures and that "hours spent working together just don't count as much".
- `sias2004`: Grade weak shown inline.
- Figures: Figure 15.3 is labelled "our suggestions, not findings"; Figure 15.2 is labelled "approximate figures, from Hall (2019)".

## Chapter 16, Conflict, Politics, and Difficult People

### Problems found (2)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| porath2007 | Rudeness "experienced, or merely witnessed" lowered performance and helpfulness (§difficult) | full (see 10.15) | fixed | Same misattribution as Chapter 10; split the sentence and added porath2009 for witnessing. |
| eu-whistleblower2019 + osborneclarke-whistleblowing | Directive: internal channels for private entities "with more than 50 workers", 7-day acknowledgement, 3-month feedback (Field Notes) | full: EPRS briefing (registry); Osborne Clarke commentary read; legislation.gov.uk and EUR-Lex refused automated access | fixed | Off by one. Article 8(3) covers entities with **50 or more** workers, as quoted by the law-firm commentary and the legislation.gov.uk copy surfaced in search; the EPRS briefing's "more than 50" leaves out an entity with exactly 50. Corrected and the second source added. |

### Confirmed (26 entries)

Every claim citing these sources matched the source as read: `ross1979`, `savitsky2005`, `sarsons2021`, `jehn1995`, `dedreu2003`, `dewit2012`, `ferris2005`, `munyon2015`, `bing2011`, `higgins2003`, `oboyle2011`, `joseph2010`, `burris2012`, `morrison2014`, `edmondson1999`, `frazier2017`, `deng2019`, `google2015`, `andersson1999`, `felps2006`, `dulebohn2012`, `gabarro1980`, `kruger2005`, `kishgephart2010`, `dyck2010`, `eeoc-harassment`, `eeoc-charge-stats`, `govuk-whistleblowing`, `india-posh2013`, `india-companies177`.

Notes on confirmed claims:

- `ross1979`: The chapter avoids the unverified "sums to over 100%" line, as the registry warns.
- `savitsky2005`: Abstract not retrievable; the finding is described the same way by later papers.
- `dewit2012`: Myth "task conflict is good" (partly, strong): fair.
- `oboyle2011`: Its dominance analysis also gives EI "substantial relative importance", so "partly" (not "busted") is the right verdict for "EQ matters more than IQ".
- `google2015`: Myth (partly, strong) is fair.
- `kishgephart2010`: A 2010 "Clarification" is registered against it (title only read); nothing in the abstract-level claim depends on it.
- `eeoc-charge-stats`: 54,350 / 88,201 = 61.6%.
- Figures: Figure 16.1 is labelled "illustrative numbers"; Figure 16.3 is labelled "a general guide, not legal advice".

## Chapter 17, Staying Yourself Under Pressure

### Problems found (5)

| Source | Claims covered | Check | Verdict | What was wrong, and what changed |
|---|---|---|---|---|
| bakker2007 | JD-R: demands → strain, resources → motivation, buffering (§jdr; Your Move 17.1; §pause); "Critics say the model is so flexible that it is hard to prove wrong" | light: abstract | fixed | Model claims confirmed. The "critics say" line named no critic and had no citation. Reworded: the authors present the model as flexible (the abstract calls it "the more flexible JD-R model"), and the falsifiability point is labelled as the book's view. |
| brown2013, fredrickson2005, fredrickson2013 | Myth: positivity ratio (busted, strong): 2.9 ratio; "entirely unfounded" (Myth Check; referenced from Ch. 10) | full: brown2013 abstract (quote exact); Crossref shows a 2013 correction notice to fredrickson2005 | fixed | Confirmed. Added the journal's formal correction (fredrickson2013, already in the registry, cited only for the fact of the correction) so the reader sees the original was corrected, not just criticised. |
| bolino2005 | Initiative → overload, stress, work-family conflict, "more strongly for women" (§helping) | full (see 10.25) | fixed | Only the work-family-conflict link was stronger for women; made specific. |
| givi2024 | Decliners expected the inviter to be "far more upset" and to stop inviting them (§no; Ask box) | light: abstract | fixed | The abstract says decliners *overestimate* the anger and the effect on future invitations; it gives no size. Removed "far". |
| pew2022 | 2021 quitters: low pay 63%, no advancement 63%, disrespected 57%, "childcare problems (48%)", flexibility 45%, benefits 43% (§leave) | full: Pew page | fixed | The 48% is among quitters *with a child under 18 in the household*, not all quitters. Corrected. The other five figures match. |

### Confirmed (21 entries)

Every claim citing these sources matched the source as read: `who2019`, `maslach2001`, `rotenstein2018`, `pega2021`, `becker2021`, `belkin2020`, `hulsheger2011`, `sonnentag2012`, `giurge2021`, `panagioti2017`, `hagger2016`, `baumeister2001`, `podsakoff2009`, `bergeron2007`, `babcock2017`, `flynn2008`, `welsh2015`, `tenbrunsel2004`, `kishgephart2010`, `ordonez2009`, `burris2012`, `govuk-working-hours`, `eu-wtd2003`, `dol-flsa-hours`, `india-osh-code`.

Notes on confirmed claims:

- `who2019`: The page says it "should not be applied to describe experiences in other areas of life".
- `rotenstein2018`: 109,628 individuals.
- `panagioti2017`: 20 comparisons from 19 studies, 1,550 physicians.
- `hagger2016`: The abstract reports a small effect with a CI including zero. "Partly" is fair given the continuing debate the box describes.
- `podsakoff2009`, `bergeron2007`: Bergeron is already described here as "a theory paper".
- `tenbrunsel2004`: Theory, described as such; the gloss is the paper's titular concept.
- `eu-wtd2003`: Time-sensitive: true as of the check date.
- `india-osh-code`: Coverage limits are already stated as unverified in the text.
