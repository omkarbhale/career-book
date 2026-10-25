# Fact-check log: front matter and Part I (Chapters 1 to 9)

**Scope.** "How to Use This Book" (`book/front/how-to-use.md`), the cast page (`book/front/cast.md`) and Chapters 1 to 9, including the claims inside figures, figure scripts, exercise answers, Myth Checks, Receipts, Field Notes and captions, together with the source registries they cite.

**Method.** Adversarial. The writers had already checked their own claims; this check assumed nothing they did. For every factual claim I found its citation, opened the source itself (the paper, its published abstract, the official page, the data file or, where a site refused scripted access, an Internet Archive copy), compared the claim with what the source says (direction, size, certainty, population, year, exact wording), and searched for a correction, retraction, failed replication or newer evidence. All 38 cited DOIs were checked against OpenAlex for retractions; none is retracted. Every source was opened on 25 October 2026.

**Two passes.** The front matter and Chapters 1 to 5 were checked first, claim by claim, and are logged one row per claim. Chapters 6 to 9 were checked afterwards under a faster method the book's owner asked for: claims grouped by source, each source opened once, and two tiers of rigour. A *full check* (open the source and search for contrary evidence) was used for headline numbers, every Myth Check, legal and regional facts and anything surprising. A *light check* (compare against the registry note, and open the source only if the wording or number differs or the note is thin) was used for background claims the registry already backs at strong or moderate. Those chapters are logged one row per source. The truth rules were the same in both passes.

**Verdicts.** *Confirmed*: the claim matches the source and survives the search for contrary evidence. *Fixed*: the text was changed (what changed is stated). *Downgraded*: the claim stands but its evidence grade or verdict was lowered. *Cut*: the claim was removed.

## Summary

**Front matter and Chapters 1 to 5 (one row per claim):**

| | Front matter | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claims checked | 11 | 26 | 45 | 32 | 11 | 23 | **148** |
| Confirmed | 5 | 20 | 30 | 24 | 8 | 16 | **103** |
| Fixed | 5 | 6 | 14 | 7 | 3 | 6 | **41** |
| Downgraded | 1 | 0 | 0 | 0 | 0 | 1 | **2** |
| Cut | 0 | 0 | 1 | 1 | 0 | 0 | **2** |

**Chapters 6 to 9 (one row per source or source group):**

| | Ch 6 | Ch 7 | Ch 8 | Ch 9 | Total |
| --- | --- | --- | --- | --- | --- |
| Entries | 18 | 15 | 5 | 21 | **59** |
| Confirmed | 17 | 11 | 5 | 18 | **51** |
| Fixed | 1 | 4 | 0 | 3 | **8** |

The cast page contains no factual claims (its people and companies are fictional), so it has no rows.

### The most serious problems found

1. **A Myth Check overturned by newer evidence (Ch 9, pay transparency).** "Pay transparency raises everyone's pay" was marked *busted*, grade *strong*, "probably wrong on average", on the strength of a study of laws protecting the right to *discuss* pay. A 2025 NBER working paper on laws requiring salary information *in job postings* (the kind the chapter's Field Note describes) found wages rose 1.3% to 3.6%, including for incumbent workers. The verdict is now *partly*, grade *moderate*, with both results; new source `arnold2025`.
2. **A claim contradicted by its own source (Ch 5, cover letters).** The chapter said "a generic letter is worse than none". The only experiment it cites shows the opposite: callback rates of 10.7% with no letter, 12.5% with a generic letter and 16.4% with a tailored one. The chapter had also said those group results were "only available as an image we could not verify"; the chart was read and the numbers are now in the text.
3. **A failed replication left out (Ch 2, unemployment gaps).** The chapter presented one US field experiment's finding (callbacks fall sharply over the first eight months out of work) as how employers behave, and built "the first months matter most" on it. A later US audit study of about 12,000 applications (Farber, Silverman and von Wachter 2017) found *no* link between unemployment duration and callbacks for experienced, college-educated applicants, and the published version of the Swedish study the chapter cites finds an effect only for current spells of nine months or more. The text, the gaps Myth Check and the Rewind now describe mixed evidence; the advice to start searching early still stands on other grounds.
4. **Misdescribed meta-analysis (Ch 3).** "A meta-analysis of 28 US field experiments since 1989" was wrong: 28 studies in total, 24 of them since 1989, which is the period the 36% and 24% figures describe.
5. **A survey statistic without its base (Ch 3).** "More than 90% of employers" used their recruiting software to filter or rank candidates; the report shows only 63% of employers used such software, so the 90% refers to those that do.
6. **Claims attributed to sources that do not make them.** The Atlanta Fed was cited for the caution that its data are "descriptive, not causal" (its page says nothing of the kind; now labelled as the book's view). Gem's customer base was said to lean "towards technology and large companies" and CareerPlug's data to be "mostly hourly and frontline jobs"; neither report says so. In Chapter 6, a two-firm study was summarised as showing that referral hiring could disadvantage women; what it found is that referrals brought more women in at every job level, though less so at higher levels. The "250 applications" figure was said to have been "later widely misattributed to Glassdoor", cited to a 2013 article that cannot report what happened later; cut.
7. **Grades and verdicts that overclaimed.** The sample Myth Check on the 10% brain myth showed *strong* evidence for a verdict resting on one teacher survey (now *moderate*). The typo Myth Check showed *strong* for a single vignette experiment in one region (now *moderate*). The LinkedIn photo Myth Check said *busted* when the evidence shows only that the "21 times" figure is unsupported, not that it is false (now *partly*).
8. **Smaller overstatements**, all fixed: a Pew percentage reported without its base (48% of quitters *with children*), "the most recent" re-analysis (unverifiable), a universal claim about what "nobody" in a research debate thinks, a medium effect called "small", and two legal summaries that went beyond their sources. In Chapters 7 and 9: "about a dozen" markets (a count the cited paper does not give), a claim that Google "did not publish" its interview data (unverifiable; now "not a published study"), and two UK legal points worded beyond the cited pages (health questions and non-competes).

### Registries

Where a research registry (`research/part1`, `research/part2`) described a source wrongly or recorded a second-hand reading, I added a corrected entry for the same work (same DOI or URL) to the relevant `book/sources/chNN.yaml`. The build keeps the first copy it reads, and `book/sources/` is read before `research/`, so the corrected entry is what readers see. The research registries were outside this check's file scope and were not edited; their entries for `eriksson2014`, `hiddenworkers2021`, `mohr2014`, `pew2022`, `powell2018`, `resumego2020-cover`, `sterkens2023` and `sullivan2013` should be brought into line by their owners.

New sources added, each opened and read: `javaranch2004` (howto), `bls-jolts2022` and `farber2017` (ch02), `rice2014` (ch04), `arnold2025` (ch09). Corrected copies: `powell2018` (ch01), `eriksson2014`, `pew2022` (ch02), `hiddenworkers2021`, `sullivan2013` (ch03), `mohr2014` (ch04), `resumego2020-cover`, `sterkens2023` (ch05).

### What this check could not do

Some sources could be read only in part, and the grades shown reflect that. The Indian caste and religion audit (`thorat2009`) was read through a research centre's summary; the original paper was not available. The 40 to 50% callback figure in `cohn2021` was read in the Chicago Booth Review summary and agrees with the published abstract's "substantially more callbacks", but the full paper was not opened. `brown2016`, `kline2022`, `kroft2013`, `faberman2017` and `farber2017` were read in their working-paper versions. `ladders2018` gives no sample size, and no one can check it.

---

## Front matter: "How to Use This Book"

| # | Claim | Source opened | Verdict |
| --- | --- | --- | --- |
| H1 | Conversational, second-person text improves recall and transfer; the benefit fades in studies longer than ~35 minutes. | `ginns2013`: ERIC record EJ1036785, abstract (retention d = 0.30, transfer d = 0.54; "small, non-significant effects" beyond 35 min). | **Fixed.** "Shrank to almost nothing" overstated "small, non-significant"; now "was small and no longer statistically reliable". |
| H2 | Placing words next to the parts of a picture, and signalling structure, helped understanding in lab studies. | `mayer2003`: full article (archived course copy). Spatial contiguity effect size .48 (1 experiment), signalling .74 (1). | **Confirmed.** Each rests on one experiment; registry grade *moderate* is right. |
| H3 | Seductive details hurt learning a little. | `cheng2026`: ERIC record EJ1510171 (g = −0.16, 177 effect sizes, 50 studies). | **Confirmed.** |
| H4 | Cutting seductive details helped in Mayer and Moreno's experiments. | `mayer2003` (coherence effect, median effect size .90, 5 experiments). | **Confirmed.** |
| H5 | Self-testing earned the top utility rating; rereading and highlighting the bottom one. | `dunlosky2013`: PubMed abstract. | **Confirmed.** (Practice testing shares the top rating with distributed practice.) |
| H6 | Working memory holds "about four [chunks], on the best current estimate". | `cowan2001`: PubMed abstract. | **Fixed.** A 2001 review cannot carry "best current estimate", and capacity models are still debated; now "according to an influential review of the evidence". |
| H7 | Teachers interested in neuroscience believed about half of neuromyths, including learning styles and left/right-brain learners. | `dekker2012`: full text on PMC (49%; 242 teachers, UK and Netherlands). | **Confirmed.** |
| H8 | Sample Myth Check: "You only use 10% of your brain", *busted*, grade *strong*; Dekker lists it among classic neuromyths. | `dekker2012` (lists it, citing the OECD). | **Downgraded.** Verdict stands; the only cited source is a survey that classifies the claim as a myth, so the badge is now *moderate* (its registry grade). |
| H9 | "Much of the research on hiring and on behaviour at work comes from the United States and Western Europe." | None cited. | **Fixed.** Rewritten as a statement about the research *this book* draws on, which readers can check on the References page. |
| H10 | Laws on pay transparency, non-compete clauses and notice periods were changing as the book was written. | None cited. Opened `ec-paytransparency` (EU Directive 2023/970, transposition deadline 7 June 2026), `cooley2026` (new US state laws, e.g. Virginia from 1 July 2026), `cms2025-uk-noncompete`. | **Fixed.** Now cited; "notice periods" cut because no change to them was verified. |
| H11 | The book's style owes a debt to the learner-centred approach Kathy Sierra and Bert Bates championed. | None cited. Opened the 2004 JavaRanch interview with both authors. | **Fixed.** Sourced (`javaranch2004`, new). |

## Chapter 1: Three Games

| # | Claim | Source opened | Verdict |
| --- | --- | --- | --- |
| 1.1 | Spence (Nobel laureate): the value of individuals to firms "is not directly observed, at least at the time of hiring". | `spence2001-lecture`: Nobel lecture PDF. | **Confirmed.** Exact wording. |
| 1.2 | "The most recent big revision" re-analysed the meta-analyses and cut most estimates by .10 to .20; validity measured by comparing candidates' scores with performance "later". | `sackett2022` (abstract and Table 3), `sackett2023-iop` (full text). | **Fixed.** Figures confirmed. "Most recent" cannot be verified (now "a major recent revision"); about 80% of validity studies are concurrent, on current employees (`sackett2023-iop`), so "candidates ... later" became "people ... on the job". |
| 1.3 | Structured interviews: corrected validity .42. | `sackett2022` Table 3. | **Confirmed.** |
| 1.4 | ".42, plus or minus .24"; 80% credibility interval .18 to .66. | `sackett2023-iop`. | **Confirmed.** Exact quote. |
| 1.5 | "A casual, unstructured conversation, the kind many interviews still are, does markedly worse." | Uncited. | **Fixed.** Now cited with the figure (.19, `sackett2022`); the unsourced claim about how common such interviews are was cut. |
| 1.6 | Receipts: the range-restriction correction had been applied too generously. | `sackett2022`, `sackett2023-iop`. | **Confirmed.** |
| 1.7 | Receipts: job-specific methods generally beat broad measures. | `sackett2023-iop` ("predictors ... specific to individual jobs ... tend to fare better"). | **Confirmed.** |
| 1.8 | Receipts: "most employers combine several [methods], which predicts better". | `sackett2023-iop` (use of multiple predictors is "widespread"; composites average .47 to .51). | **Fixed.** "Most" → "often". |
| 1.9 | Appearance, impression management and verbal and nonverbal behaviour shape interview ratings; "what you see in the interview may not be what you get on the job"; unstructured interviews especially affected. | `barrick2009`: PubMed abstract. | **Confirmed.** Exact quote; includes experimental designs, so the causal wording is supported. |
| 1.10 | In structured interviews, self-promotion correlated .26 with ratings across 13 studies. | `levashina2014`: author copy, Table 4. | **Confirmed.** |
| 1.11 | Interview anxiety correlates −.19 with ratings across 30 studies; "that is a small effect". | `powell2018`: published abstract (Semantic Scholar API) and the first author's slides. | **Fixed.** The authors call −.19 "a medium effect size in this research area"; text now says so. Searched further: a 2019 study by the same group (Schneider, Powell and Bonaccio, *International Journal of Selection and Assessment*, abstract read via OpenAlex) found near-zero correlations between interview anxiety and later job performance in one sample, which supports the chapter's point and is noted in the source entry. |
| 1.12 | Myth Check "The best candidate gets the job": *partly*, *strong*. | `sackett2022`, `sackett2023-iop`, `levashina2014`, `powell2018`. | **Confirmed.** |
| 1.13 | Spence: a signal works because "the cost of the signal is negatively correlated with the unseen characteristic that is valuable to employers". | `spence2001-lecture`. | **Confirmed.** Exact wording. |
| 1.14 | Axelrod and Hamilton: reciprocity-based cooperation can start in an unfriendly population, thrive, and resist invasion (model plus computer tournament). | `axelrod1981`: Science abstract via OpenAlex. | **Confirmed.** |
| 1.15 | Emotional-labour meta-analysis of 95 studies: surface acting and emotion-rule dissonance go with substantially worse well-being and attitudes and slightly worse performance; deep acting has weak links to impaired well-being. | `hulsheger2011`: abstract via OpenAlex. | **Confirmed.** |
| 1.16 | Authenticity meta-analysis of 75 studies: r = .40 with well-being, .37 with engagement; mostly Western, individualist measures. | `sutton2020`: abstract via OpenAlex. | **Confirmed.** Correlational, as the chapter says. |
| 1.17 | More than 4,000 managers; rater idiosyncrasy 62% and 53% of rating variance; performance about a fifth to a quarter. | `scullen2000`: abstract via OpenAlex (2,350 + 2,142 managers; 21% and 25%). | **Confirmed.** The chapter's caveats (developmental ratings; debate over rater variance) are accurate. |
| 1.18 | Sales workers at 131 firms: best salespeople promoted though other traits predicted management better; costly; Peter Principle. | `benson2019`: QJE abstract via OpenAlex. | **Confirmed.** |
| 1.19 | People born 1957 to 1964 held 12.9 jobs from 18 to 58, 4.5 of them at 25 to 34. | `bls-nlsy2025`: BLS release USDL-25-1322 (Internet Archive copy; bls.gov refuses scripts). | **Confirmed.** |
| 1.20 | Median tenure 4.1 years in January 2026; 3.0 years at ages 25 to 34. | `bls-tenure2026`: BLS release USDL-26-1532 (Internet Archive copy). | **Confirmed.** |
| 1.21 | US employment is mostly "at will", with state exceptions. | `lii-atwill`: Cornell LII. | **Confirmed.** |
| 1.22 | UK: at least a week's notice after a month in the job. | `govuk-notice`: GOV.UK. | **Confirmed.** |
| 1.23 | India: "notice is set by contract", typically 1 to 2 months, 3 to 6 for senior roles. | `khaitan-notice`: Khaitan & Co. | **Fixed.** Ranges confirmed; some state Shops and Establishments Acts set a one-month minimum, so "set mainly by contract" (as Chapter 2 already said). |
| 1.24 | Referred candidates: 6.1% of applicants, 21.4% of interviewees, 27.3% of offers, 29.1% of hires. | `brown2016`: New York Fed Staff Report 568, stage table. | **Confirmed.** |
| 1.25 | "A randomised experiment on LinkedIn" across 20 million people over five years: moderately weak ties helped most; weak ties mattered more in digital industries. | `rajkumar2022`: Science article (hosted copy). | **Fixed.** Several experiments, not one; findings confirmed. |
| 1.26 | Figure 1.2: 150 simulated people with correlation .42. | `book/figures/_src/ch01_figures.py` (seeded simulation with r = .42). | **Confirmed.** |

## Chapter 2: Stay, Go, or Grow?

| # | Claim | Source opened | Verdict |
| --- | --- | --- | --- |
| 2.1 | Pew: quitters cited low pay (63%), no advancement (63%), disrespect (57%), childcare (48%), inflexible hours (45%), benefits (43%). | `pew2022`: full page (the registry had used search-result text). | **Fixed.** The 48% is of quitters with a child under 18 at home; now stated. Corrected registry copy in `ch02.yaml`. |
| 2.2 | Turnover meta-analysis: many predictors, context-dependent. | `rubenstein2018`: abstract via OpenAlex. | **Confirmed.** |
| 2.3 | Gallup: of 7,272 US adults, about one in two had left a job "to get away from their manager"; page inconsistent on "at least" vs "up to" 70%. | `gallup2015`: page. | **Confirmed.** |
| 2.4 | Myth Check "People leave managers": *partly*, *weak*. | `gallup2015`, `pew2022`, `rubenstein2018`. | **Confirmed.** The grade is conservative, not inflated. |
| 2.5 | External hires paid about 18 to 20% more, lower ratings for two years, more likely to leave, promoted faster if they stay. | `bidwell2011`: Knowledge at Wharton article (Internet Archive copy) and the ASQ abstract ("around 18 percent"). | **Confirmed.** Wording matches the Wharton write-up the chapter names. |
| 2.6 | Gem: internal candidates 0.27% of applications, 12.56% of hires. | `gem2025`: report PDF. | **Confirmed.** |
| 2.7 | Gem's customer base "leans towards technology and large companies". | `gem2025`. | **Cut.** The report does not say this; replaced with "a customer base that is not a random sample of employers". |
| 2.8 | Switchers beat stayers in 91% of months, by 0.73 points on average, January 1997 to September 2026. | `atlantafed-wgt-data2026`: data file downloaded and recomputed (356 months; 91.3%; 0.729). | **Confirmed.** |
| 2.9 | Gap peaked at 2.2 points in November 2022 "when employers were desperate for people", and "briefly reversed" in "the slack market after the 2008 financial crisis". | Data file (peak 2022-11: 7.7% vs 5.5%; switchers behind June 2009 to September 2010). New: `bls-jolts2022`, BLS Monthly Labor Review (job openings at a series high in March 2022, historically high all year). | **Fixed.** Labour-market context now sourced; "briefly" → "for more than a year" (16 months). |
| 2.10 | Figure 2.2: annual averages (e.g. 2023 7.1% vs 5.5%; 2025 4.4% vs 4.3%). | Recomputed from the data file; matches `ch02_figures.py`. | **Confirmed.** |
| 2.11 | Figure 2.2 alt text "they spread widest in 2023"; caption "can vanish when [employers are not short of people], as ... in 2025". | Data file: the annual gap is widest in 2022 (1.63) not 2023 (1.61); the 2025 labour-market claim is unsourced. | **Fixed.** Alt: "both lines peak in 2023"; caption describes the pattern without the unsourced cause. |
| 2.12 | The switcher series counts some occupation or duty changes. | `atlantafed-wgt`: methodology page. | **Confirmed.** |
| 2.13 | "It is descriptive, not causal: the people who switch differ ..." cited to the Atlanta Fed. | `atlantafed-wgt`: the page makes no such statement. | **Fixed.** Relabelled as the book's view. |
| 2.14 | Field experiment: résumés with fewer job changes got 40 to 50% more callbacks. | `cohn2021`: JEEA abstract via OpenAlex and Cambridge repository; Chicago Booth Review summary for the 40 to 50%. | **Confirmed.** |
| 2.15 | The penalty came through inferred work attitude; the authors note moves can also signal ambition and breadth. | `cohn2021` abstract; Booth summary. | **Confirmed.** |
| 2.16 | Median tenure at 25 to 34: 3.0 years. | `bls-tenure2026`. | **Confirmed.** |
| 2.17 | Employed searchers get more offers per application, better pay, and are nearly three times as efficient. | `faberman2017`: working paper. | **Confirmed.** |
| 2.18 | "Employers read current unemployment as a signal ... and they read it fast": 12,000 résumés, callbacks 45% lower at eight months. | `kroft2013`: NBER working paper. Contrary evidence searched for and found: `farber2017`, NBER WP 21689. | **Fixed.** Kroft's jobs were sales, customer service and clerical (now stated); Farber et al. found no duration effect for experienced college-educated applicants (now stated; new source). |
| 2.19 | US: notice set by contract and policy, not a legal minimum. | `lii-atwill`. | **Confirmed.** |
| 2.20 | UK: a week's notice; garden leave on full pay. | `govuk-notice`: giving-notice and garden-leave pages. | **Confirmed.** |
| 2.21 | Germany: four weeks to the 15th or month end; two weeks in probation of up to six months. | `bgb622`: BGB §622, official English translation. | **Confirmed.** |
| 2.22 | India: notice mainly by contract, 1 to 2 months, 3 to 6 senior. | `khaitan-notice`. | **Confirmed.** |
| 2.23 | US: FTC ban struck down, appeal dismissed September 2025, "so state law governs". | `uschamber-ryan`: case page (motion 5 September, order 8 September 2025). | **Fixed.** Dates confirmed; now "there is no nationwide ban and state law sets the main rules", since federal law still applies case by case. |
| 2.24 | California voids most non-competes and bars attempts to enforce them. | `loeb2023-california` (SB 699, AB 1076). | **Confirmed.** |
| 2.25 | UK: "Restrictive covenants can be enforced in court." | `govuk-notice`: restrictive-covenants page ("Your company could take you to court"). | **Fixed.** Reworded to what GOV.UK says. |
| 2.26 | UK three-month cap never legislated; government reopened the question in late 2025; no outcome yet. | `cms2025-uk-noncompete` (28 November 2025). Searched for an outcome: the consultation closed 18 February 2026 and no response was found by 25 October 2026. | **Confirmed.** |
| 2.27 | India: Contract Act s.27 voids restraints of trade; post-employment covenants held void; restrictions during employment treated differently. | `barandbench-s27`. | **Confirmed.** |
| 2.28 | Swedish experiment with young applicants: no sorting on past unemployment, "some sign" of sorting on current unemployment. | `eriksson2014`: published AER abstract via OpenAlex; AER online appendix (applicants aged 23 to 32); IZA DP 6235. | **Fixed.** The published finding is sharper: past spells (even long ones) and short current spells did not matter; current spells of nine months or more did. Text and Myth Check updated; corrected registry copy. |
| 2.29 | 48% of employers filter middle-skills candidates with gaps over six months. | `hiddenworkers2021`: full report PDF. | **Confirmed.** |
| 2.30 | "Put plainly: the first months matter most." | Follows from 2.18 and 2.28. | **Fixed.** Now reflects mixed evidence: where a current gap hurts, it hurts more the longer it lasts. |
| 2.31 | Unemployed people have lower psychological and physical well-being; coping resources and appraisals matter more than demographics. | `mckeeryan2005`: abstract (104 studies). | **Confirmed.** |
| 2.32 | High-seniority men displaced in Pennsylvania mass layoffs: mortality 50 to 100% higher the next year, 10 to 15% after 20 years. | `sullivan2009`: QJE abstract; NBER WP 13626 ("mass-layoffs"). | **Confirmed.** |
| 2.33 | 47 programmes; 2.67 times the odds; effective components; skills plus motivation; more effective for the short-term unemployed. | `liu2014`: Psychological Bulletin abstract. | **Confirmed.** |
| 2.34 | Checklist: "Structure is part of what effective programmes provide." | `liu2014` lists goal setting, not "structure". | **Fixed.** Now cites goal setting. |
| 2.35 | Checklist: "a current gap reads worse the longer it is silent". | `kroft2013` tests duration, not silence. | **Fixed.** "In some markets a current gap costs more callbacks the longer it runs." |
| 2.36 | WARN Act: 60 days' notice; employers of 100 or more. | `warn-2102`, `warn-2101`: 29 U.S.C. via Cornell LII. | **Confirmed.** |
| 2.37 | Contact your state UI programme "as soon as possible", in the state where you worked. | `dol-ui`: DOL page (Internet Archive copy). | **Confirmed.** |
| 2.38 | UK redundancy: 2 years' service; 6 months to claim; notice, consultation, time off to look for work; fair selection. | `govuk-redundancy-pay` and GOV.UK redundancy overview and selection pages. | **Confirmed.** |
| 2.39 | India: Labour Codes in force 21 November 2025; final dues within two days of resignation; "we did not verify how that applies to layoffs". | `argus-labourcodes`. | **Fixed.** Date confirmed. The source says two *working* days, "similar to termination of employment"; text now says so. |
| 2.40 | Downsizing raises survivors' voluntary turnover via lower commitment; fair procedures soften it. | `trevor2008`: abstract. | **Confirmed.** Organisation-level data. |
| 2.41 | Myth Check "Any gap is fatal": *partly*, *strong*. | `kroft2013`, `farber2017`, `eriksson2014`, `hiddenworkers2021`. | **Fixed.** Verdict and grade stand (several field experiments); text now reports the contrary US result and Eriksson's nine-month threshold. |
| 2.42 | Skills are more portable than assumed; people move to occupations with similar tasks; task-specific skills explain much wage growth. | `gathmann2010`: abstract ("up to 52%"). | **Confirmed.** |
| 2.43 | Boomerang managers: similar first-year performance, improved less, more likely to leave, often for the same reasons. | `arnold2021`: abstract. | **Confirmed.** |
| 2.44 | Resignation styles differ and affect managers' reactions. | `klotz2016`: abstract. | **Confirmed.** |
| 2.45 | Rewind: "a current gap costs callbacks fast". | As 2.18. | **Fixed.** "Can cost callbacks, and more the longer it lasts." |

## Chapter 3: The View from the Other Side of the Table

| # | Claim | Source opened | Verdict |
| --- | --- | --- | --- |
| 3.1 | A recruiting consultant: hiring decisions "are not ours. We're the project manager." | `shrm2015-recruiters`: SHRM page. | **Confirmed.** Exact quote. |
| 3.2 | Gem, inbound 2024: 6% to first screen, 20% of those to final round, 35% of those offered, 0.4% hired. | `gem2025`. | **Confirmed.** Gem's stage names are "Pre-Onsite" and "Onsite". |
| 3.3 | Figure 3.2: about 60, 12 and 4 per 1,000; referral shares 6.1 / 21.4 / 27.3 / 29.1%. | `gem2025`, `brown2016`. | **Confirmed.** |
| 3.4 | CareerPlug: 180 applicants per hire in 2024 (93 the year before); 3% invited to interview; 27% of interviews end in a hire. | `careerplug2025`: report PDF. | **Confirmed.** |
| 3.5 | CareerPlug's data are "mostly hourly and frontline jobs". | `careerplug2025` (says "small businesses"; sectors include restaurants, retail, cleaning, personal care). | **Fixed.** Now describes the sectors the report lists. |
| 3.6 | Sourced candidates hired at 2.0% (five times inbound); referrals 1.64% of applications, 17.09% of hires. | `gem2025`. | **Confirmed.** |
| 3.7 | Job-board applicants 60.1% of applicants, 23.5% of hires. | `brown2016`. | **Confirmed.** |
| 3.8 | Hire rate 1.6% → 0.5% (2021 to 2024); interviews per hire 14 → 20; days to hire 33 → 41; offer acceptance 81% → 84%. | `gem2025`. | **Confirmed.** |
| 3.9 | Myth Check "250 applications": "the number traces to a 2013 article", hedged in the original, no method. | `sullivan2013`: ERE article. | **Fixed.** Quote and hedge confirmed; the article gives no source, so "traces to" became "the earliest source we found". Corrected registry copy. |
| 3.10 | "Later it was widely misattributed to Glassdoor." | `sullivan2013` cannot support it; searched, found only sites crediting Glassdoor without a link, and no primary source. | **Cut.** |
| 3.11 | Hidden Workers: "more than 90% of employers said they used their recruiting system to initially filter or rank candidates". | `hiddenworkers2021`: full report. | **Fixed.** Only 63% of employers used such a system; the report's 90% refers to employers using "their RMS". Base now stated; corrected registry copy. |
| 3.12 | 88% agree qualified high-skills candidates are screened out (94% middle-skills); 48% filter on gaps over six months. | `hiddenworkers2021`. | **Confirmed.** |
| 3.13 | 25 recruiters: 23 no auto-reject for formatting; 2 used match thresholds; all used knockout questions. | `enhancv2025-ats`. | **Confirmed.** |
| 3.14 | Myth Check "ATS rejects 75%": traced to a 2012 Preptel sales claim; company closed 2013; no method. | `interviewguys-ats-myth`. | **Confirmed.** |
| 3.15 | An HR consultant found no study behind the figure, as recounted by an ATS vendor. | `hiringthing-ats-myth` (Christine Assaf). | **Confirmed.** |
| 3.16 | "The most recent large re-analysis" of selection validity. | `sackett2022`. | **Fixed.** "A major recent re-analysis". Searched for later rebuttals: Huffcutt and Murphy (2023, *Industrial and Organizational Psychology*, commentary read in full at resolve.cambridge.org) welcome the ranking but stress that structured interviews have "the highest variability in validity (i.e., .42 +/− .24) among top predictors", which the book already reports; Ones and Viswesvaran (2023, cited) dispute the cognitive-ability estimate; no reversal of the ranking found. |
| 3.17 | Table: structured .42, job knowledge .40, work samples .33, cognitive ability .31, unstructured .19, experience .07. | `sackett2022` Table 3. | **Confirmed.** |
| 3.18 | 1998 summary: cognitive ability and structured interviews .51, unstructured .38. | `schmidt1998` Table 1. | **Confirmed.** |
| 3.19 | 21st-century data put cognitive ability at .22. | `sackett2023-gca`. | **Confirmed.** |
| 3.20 | Other researchers argue cognitive ability is being underestimated. | `ones2023`. | **Confirmed.** |
| 3.21 | "Nobody in that argument thinks the ranking is upside down." | Uncited universal claim. | **Fixed.** Now "the old and new estimates agree" on structured over unstructured and job-specific over general, cited to both tables. |
| 3.22 | White-sounding names got 50% more callbacks. | `bertrand2004`: NBER WP 9873. | **Confirmed.** |
| 3.23 | "A meta-analysis of 28 US field experiments since 1989, covering 55,842 applications": whites 36% more callbacks than African Americans, 24% more than Latinos, no change over 25 years. | `quillian2017`: PNAS abstract on PMC. | **Fixed.** 28 studies in total; 24 since 1989, the period the percentages describe. |
| 3.24 | 83,000+ applications to 108 large employers; Black names cut contact by 2.1 points; large variation by firm. | `kline2022`: IZA DP 14634. | **Confirmed.** |
| 3.25 | India: interview odds for Dalit applicants about two-thirds, Muslim applicants about one-third, of high-caste Hindu applicants. | `thorat2009`: GSDRC summary. | **Confirmed** (summary-level, as the chapter says). |
| 3.26 | Figure 3.3 and text: 63% chance of 46 noes at 1 in 100; 9% at 1 in 20. | Arithmetic: 0.99^46 = 0.630; 0.95^46 = 0.094. | **Confirmed.** |
| 3.27 | Search effort is reliably related to finding work. | `kanfer2001`: abstract. | **Confirmed.** |
| 3.28 | Exercise answers: 17, 83 and about 240 applications; 7%; about 14 referrals. | Arithmetic from `gem2025` rates. | **Confirmed.** |
| 3.29 | Effective programmes combined skills and motivation; goals, confidence, social support. | `liu2014`. | **Confirmed.** |
| 3.30 | StartWire: of 6,600 hires, almost half applied in the first week. | `startwire2011`: ERE article. | **Confirmed.** |
| 3.31 | Fewer people apply after a posting's first few days. | `fradkin-bu2025`: BU article. | **Confirmed.** |
| 3.32 | Rewind: "large, persistent callback gaps by race in the US and by caste and religion in India". | `quillian2017` shows persistence for the US only; the India evidence is one study. | **Fixed.** "Unchanged for decades" now attaches to the US only. |

## Chapter 4: Know What You're Selling

| # | Claim | Source opened | Verdict |
| --- | --- | --- | --- |
| 4.1 | Flashback: Spence's cost-of-signal idea. | `spence2001-lecture`. | **Confirmed.** |
| 4.2 | Past-behaviour questions predict slightly better: about .31 vs .25 to .26 "in the meta-analyses one major review summarises". | `levashina2014`. | **Fixed.** Those figures come from two of the three meta-analyses the review cites (a third reports .35 for situational questions alone); now "in two meta-analyses". |
| 4.3 | STAR is "a widely taught answer structure". | Practitioner convention. | **Fixed.** Labelled as craft. |
| 4.4 | Self-promotion .26 across 13 studies. | `levashina2014`. | **Confirmed.** |
| 4.5 | The 60/100 figure was popularised by a 2014 HBR article attributing it to an internal Hewlett-Packard report. | `mohr2014`: full text in the Internet Archive (live page paywalled). | **Confirmed.** Corrected registry copy records the archive reading. |
| 4.6 | That report "has never been published". | Searched; opened `rice2014`, a researcher's trace back to a McKinsey article whose first author said the claim came from confidential executive interviews and that he had no access to the HP document. | **Fixed.** Now says what can be shown, with the trace (new source). |
| 4.7 | Study 1 found no gender difference at 60% or 100% fit; later studies a significant but not robust difference; women reported a stronger wish to feel prepared. | `salwender2024`: abstract via OpenAlex and CiteDrive. | **Confirmed.** |
| 4.8 | 88% of employers admit exact-criteria filters screen out qualified people. | `hiddenworkers2021`. | **Confirmed.** |
| 4.9 | Years of experience predict performance at .07. | `sackett2022`. | **Confirmed.** |
| 4.10 | Flashback: skills travel as tasks. | `gathmann2010`. | **Confirmed.** |
| 4.11 | Small interview study: employers using GitHub read activity as evidence of skill, motivation and values, trusted more than résumés because hard to fake. | `marlow2013`: CSCW paper (7 employers, 6 job seekers). | **Confirmed.** |

## Chapter 5: Paper You

| # | Claim | Source opened | Verdict |
| --- | --- | --- | --- |
| 5.1 | TheLadders 2012: 30 recruiters over 10 weeks; about 6 seconds; almost 80% of time on name, titles, employers, dates, education; ends by recommending its rewriting service. | `ladders2012`: archived PDF. | **Confirmed.** |
| 5.2 | 2018 update: 7.4 seconds, no sample size. | `ladders2018`: archived PDF; HR Daily Advisor coverage. | **Confirmed.** |
| 5.3 | Readers don't look at your summary paragraph; "the eye-tracking suggests otherwise". | `ladders2012`, `ladders2018`. | **Fixed.** The 2018 update found the best-performing résumés opened with a short overview; both findings now stated. |
| 5.4 | Keyword-stuffed résumés were among the worst performers. | `ladders2018`. | **Confirmed.** |
| 5.5 | "Clean single-column layouts ... did best in the eye-tracking studies, and multiple columns and clutter did worst." | `ladders2018` ("clear, simple layouts", "multiple columns" among the worst; 2012 does not test layout). | **Fixed.** "Single-column" is not in the source, and only the 2018 study tested layout. |
| 5.6 | Some filters match exact criteria. | `hiddenworkers2021`. | **Confirmed.** |
| 5.7 | Claims anyone can make cannot separate people (Spence). | `spence2001-lecture`. | **Confirmed.** |
| 5.8 | 445 recruiters: several errors cut interview probability by 18.5 points, a few by 7.3; half the penalty via inferred traits. | `sterkens2023`: full text on PMC. | **Confirmed.** Recruiters were in Flanders, Belgium (now stated). |
| 5.9 | Typo Myth Check: *busted*, *strong*. | `sterkens2023`. | **Downgraded.** One vignette experiment in one region is *moderate* on the book's own scale; verdict stands. Corrected registry copy. |
| 5.10 | 482 recruiters; 2.3 times as likely to prefer two pages; 1.4 for entry level. | `resumego2018-length`. | **Confirmed.** |
| 5.11 | Sourced candidates hired at 2.0% vs 0.4% inbound. | `gem2025`. | **Confirmed.** |
| 5.12 | LinkedIn claims "up to 21x more profile views" and "36x more messages". | `sej-linkedin-photo`: article (15 March 2017). | **Confirmed.** |
| 5.13 | Myth Check verdict *busted* for the 21x claim. | As above; no evidence that the claim is false, only that it is unsupported. | **Fixed.** Verdict now *partly* ("a photo may well help; nobody has shown by how much"); exercise answer aligned. |
| 5.14 | GitHub study (repeat of 4.11). | `marlow2013`. | **Confirmed.** |
| 5.15 | Cover-letter experiment: 7,287 applications; tailored letters 53% more callbacks; 87% of 236 read letters; group results "only available as an image we could not verify"; evidence "conflicting". | `resumego2020-cover`: page and its results chart, read as an image. | **Fixed.** Chart read: 10.7% none, 12.5% generic, 16.4% tailored (16.4 / 10.7 = 1.53). Numbers now in text. The two sources answer different questions rather than conflict, so "conflicting" became "thin". Corrected registry copy. |
| 5.16 | "A generic letter is worse than none." | `resumego2020-cover` chart: generic 12.5% vs none 10.7%. | **Fixed.** Contradicted by the source; now "a generic letter adds little". |
| 5.17 | 1,000+ US hiring managers: 83% said "To Whom It May Concern" would have little or no effect. | `aacsb2020-twimc` (reporting Resume Companion). | **Confirmed.** |
| 5.18 | Some minority job seekers whiten résumés; less so for pro-diversity employers; diversity statements not associated with less discrimination. | `kang2016`: ASQ abstract via OpenAlex. | **Confirmed.** |
| 5.19 | EEOC: limit pre-employment information to qualifications; race, sex, national origin, age, religion irrelevant; no photographs before an offer. | `eeoc-prohibited` (photo "after an offer of employment is made and accepted"). | **Confirmed.** |
| 5.20 | National Careers Service: "You should not include your age, your date of birth, whether you're married or your nationality". | `ncs-cv`. | **Confirmed.** Exact quote. |
| 5.21 | Europass: "add a professional photograph of yourself". | `europass-cv`. | **Confirmed.** Exact quote. |
| 5.22 | Figure 5.3, regional cards. | As 5.19 to 5.21. | **Confirmed.** |
| 5.23 | Exercise answer 5: "Myth as stated". | As 5.13. | **Fixed.** "Partly at best, and region-dependent". |

## Chapter 6: People, Not Portals

| Source | Claims checked | Tier | Verdict |
| --- | --- | --- | --- |
| `brown2016` | Referred 6.1% of applicants, 21.4% of interviewees, 27.3% of offers, 29.1% of hires; job boards 60.1% and 23.5%; figure's "everything else" 33.8% and 47.4% (arithmetic); Myth Check "who you know". | Light (read in full for Ch 1 and 3) | **Confirmed.** |
| `gem2025` | Referrals 1.64% of applications, 17.09% of hires; job boards about a quarter of hires; sourced 2.0% vs inbound 0.4%. | Light (read for Ch 2 and 3) | **Confirmed.** |
| `careerplug2025` | Referrals 2% of applicants, 11.3% of hires; job boards 43.3% of hires. | Full (report PDF) | **Confirmed.** |
| `burks2015` | Nine firms; referred workers 10–30% less likely to quit; better on patents and truck accidents; similar on ordinary productivity; matching mechanism; people refer people like themselves. | Full (IZA working paper) | **Confirmed.** |
| `pallais2016` | Referrals carry information on performance and persistence that profiles lack. | Full (NBER working paper) | **Confirmed.** |
| `granovetter1973` | Boston-suburb job changers; of 54 who found jobs through contacts, 16.7% saw them often, 55.6% occasionally, 27.8% rarely; Myth Check on weak ties. | Full (published article scan) | **Confirmed.** |
| `rajkumar2022` | Inverted U; moderately weak ties most useful; digital vs less digital industries; per-connection chance "a fraction of one per cent". | Full (Science article) | **Confirmed.** Edge-level job-transmission probabilities in the paper's figures are below 0.005. |
| `gee2017` | 6 million Facebook users; most help through weak ties, but each strong tie worth more. | Full (Tufts record, abstract) | **Confirmed.** |
| `lester2021` | 50–60% of workers report using a referral; business-contact referrals for higher-skill, higher-wage jobs. | Full (NY Fed staff report) | **Confirmed.** |
| `pellizzari-via-brown2016` | A quarter to two-fifths of Europeans heard of their job through contacts. | Light | **Confirmed** in `brown2016` ("between 25% and 40%"). |
| `fresnostate2024-hidden` | "Likely originated from anecdotal evidence and informal surveys rather than rigorous, peer-reviewed research"; Myth Check "80% of jobs never advertised". | Full | **Confirmed.** Exact quote. |
| `flynn2008` | People underestimate compliance with direct requests by as much as half, overlooking the cost of saying no. | Full (abstract) | **Confirmed.** |
| `boothby2018` | Liking gap, lasting months among new room-mates. | Light (abstract) | **Confirmed.** |
| `regan1971` | Unsolicited soft drink → more raffle tickets, regardless of liking. | Light | **Confirmed (secondary).** No index carries the abstract; secondary accounts agree on the direction, which is all the chapter uses. |
| `burger1997` | Favour repaid after 5 minutes, not reliably after a week. | Light (abstract) | **Confirmed.** |
| `fernandez2019` | Referral hiring and women in two firms. | Full (abstract) | **Fixed.** The chapter said referral hiring "could disadvantage women ... more so at higher levels". The study found referrals *raised* women's representation at every level, though less at higher levels. Text now says so. |
| `topechelon-fees` | Agency fees as a share of first-year pay; examples 18–25%; retained search paid in instalments, usually more in total. | Full | **Confirmed.** |
| `govuk-agency-fees` | GB agencies "cannot charge you a fee for finding or trying to find you work"; extras such as CV writing allowed; separate rules for entertainment and modelling. | Full | **Confirmed.** Exact quote. |

## Chapter 7: Interviews, Decoded

| Source | Claims checked | Tier | Verdict |
| --- | --- | --- | --- |
| `sackett2022`, `schmidt1998` | Structured .42, unstructured .19; 1998 figures .51 and .38; "the most recent large review". | Light (read for Ch 1 and 3) | **Fixed.** Numbers confirmed; "most recent" → "a major recent review", as in Chapters 1 and 3. |
| `abc2013-google` | Bock: brainteasers "a complete waste of time"; "structured behavioral interviews, where you have a consistent rubric"; internal data "which it did not publish". | Full | **Fixed.** Quotes exact; whether Google ever published is unverifiable, so now "rather than a published study". |
| `rivera2012` | 120 interviews at elite firms; cultural similarity often outweighed productivity. | Light | **Confirmed.** |
| `levashina2014` | Past-behaviour .31 vs situational .25–.26 "in the meta-analyses"; self-promotion .26 across 13 studies; structure reduces impression effects. | Light (read for Ch 1 and 4) | **Fixed.** "Two meta-analyses", as in Chapter 4. |
| `barrick2009` | Self-presentation shapes ratings; quote. | Light (read for Ch 1) | **Confirmed.** |
| `barrick2010` | Rapport-stage impressions: r = .42 with ratings, .22 with offers; competence carried to separate interviewers, liking did not. | Full (PubMed abstract) | **Confirmed.** |
| `swider2016` | 163 mock interviews; much of first impressions' influence overlaps with job-related content; stronger on early answers. | Full (PubMed abstract) | **Confirmed.** |
| `ambady1993` | Silent clips under 30 seconds of *teachers* predicted end-of-semester ratings; Myth Check "seven seconds". | Full (article) | **Confirmed.** |
| `mehrabian-site`, `bigthink-mehrabian` | Mehrabian: "unless a communicator is talking about their feelings or attitudes, these equations are not applicable"; small lab studies (30 and 37 women); Myth Check "93% non-verbal". | Full | **Confirmed.** |
| `carney2016`, `forrt-powerposing` | Carney: "I do not believe that 'power pose' effects are real"; 2022 meta-analysis of 88 studies: self-report effects, no reliable physiological effects, behavioural effects likely inflated by publication bias. | Full | **Confirmed.** |
| `stewart2008` | 98 students; five trained handshake raters; handshake quality linked to hireability and extraversion. | Light (press release) | **Confirmed.** |
| `powell2018` | −.19 across 30 studies; "about 4%" of variance; Myth Check on nerves. | Light (read for Ch 1) | **Confirmed.** .19² = .036. |
| `blacksmith2016` | 12 studies; technology-mediated interviews rated lower (d = −.41); fairness warning. | Light (abstract) | **Confirmed.** |
| `eeoc-prohibited` | US: questions limited to qualifications; "explicitly prohibited from making pre-offer inquiries about disability"; other questions usable as evidence of intent; no photo before an offer. | Full | **Confirmed.** |
| `ukparl2020-health` | UK quote on health and disability questions; "an offer can be made conditional on health checks". | Full | **Fixed.** Quote exact. The source says questions "can only be asked when an applicant has been offered a job" and says nothing about conditional offers; wording now matches. |

## Chapter 8: Show, Don't Tell

| Source | Claims checked | Tier | Verdict |
| --- | --- | --- | --- |
| `schmidt1998`, `sackett2022`, `sackett2023-iop` | Work samples .54 (1998) → .33 (2022); structured interviews .42, job knowledge .40; job-specific methods beat broad measures. | Light (read for Ch 1 and 3) | **Confirmed.** |
| `behroozi2020` | Randomised trial, 48 computer-science students at NC State; performance more than halved when watched; higher stress and cognitive load; Receipts and Myth Check. | Full | **Confirmed.** |
| `interviewingio2016` | Only about 20% of repeat interviewees scored consistently. | Full | **Confirmed.** |
| `behroozi2019` | Hacker News complaints: relevance, anxiety, time, arbitrary norms. | Light | **Confirmed.** |
| `dunlosky2013` | Practice testing and spacing top-rated; rereading and highlighting bottom. | Light (read for front matter) | **Confirmed.** |

## Chapter 9: Offers, Negotiation, and the Exit

| Source | Claims checked | Tier | Verdict |
| --- | --- | --- | --- |
| `secfi-vesting` | Four years with a one-year cliff, 25% at the cliff. | Light | **Confirmed.** |
| `irs-p525` | US option taxation depends on statutory vs nonstatutory type and timing. | Full | **Confirmed.** |
| `tickertape-ctc` | CTC differs from in-hand pay. | Light | **Confirmed.** |
| `argus-labourcodes` | Labour Codes in force 21 November 2025; wage definitions changed; rules still being notified. | Light (read for Ch 2) | **Confirmed.** |
| `niederle2009` | "Across about a dozen real markets", early markets allow exploding offers and binding acceptances; lab: that combination gives inefficient early matching, relaxing either rule helps. | Full | **Fixed.** Findings confirmed; the paper gives no count of markets, so "a number of real markets". |
| `hallkrueger2012` | A third bargained; a third knew the precise pay at first meeting; about 40% could have stayed; bargainers earned more after adjustment. | Full (NBER abstract) | **Confirmed.** |
| `marks2011` | 149 employees; negotiators about US$5,000 higher. | Light (secondary coverage, as the chapter says) | **Confirmed.** |
| `galinsky2001` | First offers win and anchor settlements; focusing on own target or the other side's alternatives removes the advantage; Myth Check "never name a number first". | Full (PubMed abstract) | **Confirmed.** |
| `clockspot-paytransparency`, `nydol-paytransparency`, `cooley2026`, `ec-paytransparency`, `lockton2026-eu` | 13 states plus DC as of May 2026; New York's four-employee threshold; Virginia 1 July 2026, Maine 29 July 2026, Delaware 26 September 2027; EU directive rights and 7 June 2026 deadline; few member states fully transposed by late September 2026, not Germany or France. | Full | **Confirmed.** |
| `cullen2023` + new `arnold2025` | Myth Check "Pay transparency raises everyone's pay": *busted*, *strong*, "probably wrong on average". | Full, with contrary-evidence search | **Fixed.** Cullen and Pakzad-Hurson's −2% (laws on *discussing* pay) confirmed. The search found Arnold, Quach and Taska (NBER WP 34480, November 2025): salary-*posting* laws raised wages 1.3–3.6%, with spillovers to incumbent workers. Verdict now *partly*, grade *moderate*; Rewind updated. |
| `bowles2007` | Women penalised more for negotiating; 5.5 times greater effect; video study: male evaluators penalised only women, female evaluators everyone; Myth Checks. | Full (Gender Action Portal summary) | **Confirmed.** |
| `hernandez2019` | More racially biased evaluators gave Black negotiators lower salaries, through resistance to concessions. | Full (PubMed abstract) | **Confirmed.** |
| `leibbrandt2015` | 2,422 job seekers, nine cities; "negotiable" ads: women 21.2%, men 21.4%; 21% vs 7% overall; Myth Check "women don't negotiate". | Full (summary and NBER abstract) | **Confirmed.** |
| `schmidt1998` | Reference checks .26. | Light | **Confirmed** (Table 1). |
| `eeoc-ftc-background` | Written permission; copy of report and notice of rights before adverse action; equal treatment. | Full | **Confirmed.** |
| `agan2018` | Ban the box in New Jersey and New York City: no-record applicants called back 63% more where the question was asked; white–Black gap grew from 7% to 45%. | Full | **Confirmed.** |
| `govuk-dbs` | Basic, standard and enhanced checks; basic shows unspent convictions and conditional cautions; certificate issued to you. | Full | **Confirmed.** The certificate detail is on GOV.UK's "request a basic DBS check" page ("A paper certificate will then be posted to you"). |
| `bgb622`, `lii-atwill`, `govuk-notice`, `khaitan-notice`, `barandbench-s27`, `loeb2023-california`, `uschamber-ryan` | Notice periods and non-competes, recapping Chapter 2; UK non-competes "potentially enforceable ... if reasonable". | Light (read for Ch 1 and 2) | **Fixed.** All confirmed except the UK phrase: the cited GOV.UK page says only that your employer could take you to court, so the text now says that. |
| `klotz2016`, `shrm2016-resignation` | Seven resignation styles and shares (31%, 23.5%, 12.7%, 10%, 8.6%, 7.9%, 6.3%); managers' reactions; harmful resignations often respond to unfair treatment. | Light (SHRM article) | **Confirmed.** |
| `interviewguys-counteroffer`, `4dayweek-counteroffer` | The counter-offer figure circulates as 48% to 93% with no study; CEB figure of about 50% within a year; recruiters' interest; Myth Check. | Full | **Confirmed.** |
| `pew2022`, `arnold2021` | Quit reasons (63%, 63%, 57%); boomerang managers. | Light (read for Ch 2) | **Confirmed.** |
