# Part III evidence base: growth at work

These are research notes, not book prose, for Part III of the book: being good at the work and having it count, covering reviews, promotions, choosing what to get good at, the IC-or-manager fork, and the long game. Chapter writers and fact-checkers should start at `INDEX.md`, which lists one line per key finding, then read the topic file for context and caveats.

## Files

| File | Covers |
|---|---|
| `INDEX.md` | One line per key verified finding, with grade and source key |
| `myths.md` | 20 popular claims with verdicts and "say this instead" lines; claims deliberately left out |
| `reviews.md` | Rating reliability (idiosyncratic rater effect), what goes into a rating, forced/stack ranking, calibration, abolishing ratings, what an individual controls |
| `self-assessment.md` | Self-assessment accuracy, the Dunning-Kruger debate and statistical-artefact critiques, gender gap in self-promotion, feedback seeking |
| `promotions.md` | Tournaments, performance vs potential vs visibility, the Peter Principle, "potential" ratings, sponsorship and the broken rung, internal vs external hires, tech promotion packets and levels, promotions and well-being |
| `getting-good.md` | Deliberate practice after the 10,000-hours debunk, experience vs expertise, feedback loops, learning techniques, 70-20-10, mentoring, career capital |
| `the-fork.md` | Dual ladders, best worker vs best manager, first-time manager transition, manager pay and well-being, Staff-plus paths, how to decide |
| `long-game.md` | Career plateaus, skill obsolescence and the "half-life of skills", mid-career change, age and the happiness curve |
| `motivation.md` | Self-determination theory, intrinsic motivation and incentives, job crafting, finding vs developing passion, the double edge of meaningful work |
| `money.md` | Income and happiness (Kahneman & Deaton 2010, Killingsworth 2021, their 2023 adversarial collaboration), lottery wealth, adaptation to raises, loss aversion, pay comparison |
| `regional.md` | Japan's seniority system, up-or-out, title inflation; known gaps |
| `sources.yaml` | Machine-readable source registry (format below) |

## How this part relates to Parts I and II

- **Reused, not redone.** Topics already covered are cited by their Part I or Part II keys and marked "(Part I)" or "(Part II)": mentoring effect sizes (`allen2004`, `eby2008`), mentor vs sponsor (`ibarra2010`), 10,000 hours (`ericsson1993`, `macnamara2014`, `macnamara2019`), feedback interventions (`kluger1996`), feedback-seeking meta-analysis (`anseel2015`), remote work and promotion (`bloom2015`, `bloom2024`), low-promotability tasks (`babcock2017`), selection validities (`sackett2022`) and switcher wage growth (`atlantafed-wgt`).
- **Grades kept.** No Part I or Part II grade is contradicted. One is upgraded with a reason: `bidwell2011` was **moderate** in Part I because only the Knowledge at Wharton summary could be opened. Part III read the *Administrative Science Quarterly* abstract (via OpenAlex), so the core finding is **strong** here. The paper's own figure is "around 18 percent" more pay for external hires; Part I's "18-20%" came from the Wharton summary. Part I's text is not wrong, just less precise.
- **Extended.** Part II's "10,000 hours" verdict (Overstated) is extended with the sports meta-analysis (`macnamara2016`) and Ericsson's reply (`ericsson2019`). The verdict stands.
- **Key uniqueness.** The Part I registry already has `cullen2023` (Cullen and Pakzad-Hurson, pay transparency). The Part III key for Cullen and Perez-Truglia's "Old Boys' Club" paper is therefore `cullen2023b`, so that keys stay unique across the book.

## Method

1. **Sources opened, not remembered.** Every entry in `sources.yaml` was opened during this research on 25 October 2026.
   - For DOI sources: the DOI was resolved at doi.org (all returned HTTP 302), bibliographic metadata was taken from the Crossref API, and the abstract and retraction status from the OpenAlex API. No Part III source is flagged as retracted by OpenAlex or carries a Crossref retraction notice.
   - Where OpenAlex had no abstract, the abstract was read on the publisher's page, a university repository, the Semantic Scholar API, PubMed Central or the authors' working paper, and `url_note` says which.
   - Web pages were fetched by script, or, for sites that refuse scripts (bls.gov, some HBR and Gallup pages), through a web-fetch tool, as noted in `url_note`.
   - Raw fetched copies are kept outside the repository.
2. **Working-paper figures are labelled.** Several key papers (`benson2019`, `benson2026`, `cullen2023b`, `deming2020`) were checked at abstract level in the published version, but their effect sizes were read in the NBER or author working paper. The notes say "working paper" wherever a number comes from one, because published numbers can differ.
3. **Title-level entries.** A few sources had no readable abstract. They are cited only for what their title states and are marked "title-level" (`hiller2023`, `gignac2023`, `killingsworth2024`, `greenberg1983`).
4. **Primary first.** Order of preference: meta-analyses and peer-reviewed studies; government statistics; large-sample industry data that discloses its method; then practitioner writing. Commercial, advocacy or self-interested sources carry `flags` and are named as such in the notes (`leanin2025`, `gallup2025`).
5. **Evidence, practitioner opinion and author view are kept apart.** Topic files tag statements as **Evidence**, **Practitioner** or **Researcher's synthesis** (the researcher's opinion, which writers may adopt as the author's view or reject). Anything not verified is marked **not verified** and must not be printed as fact. `myths.md` lists these claims.
6. **Validation.** A generator builds `sources.yaml` from the cached Crossref records plus hand-written annotations. It checks that the file parses, that every key cited in these notes exists in the Part I, II or III registry, and that every Part III key is cited somewhere.

## Grades

Same scale as Parts I and II:

| Grade | Meaning |
|---|---|
| **strong** | Meta-analysis, large or well-identified field study (natural experiment, randomised design, firm personnel data with credible identification), official statistics. Can carry a headline claim. |
| **moderate** | A single good study with scope limits (one firm, one country, lab task); respected review or theory; a strong source read only through a reliable summary. Can be stated with caveats. |
| **weak** | Small or qualitative studies, commercial surveys, practitioner frameworks and essays, secondary reports of an unseen original. Use as illustration, never as proof. |
| **myth-or-unsupported** | No traceable evidence, or contradicted by better evidence. Print only to debunk. |

A finding's grade can differ from its source's grade. In `myths.md`, the grade is for the evidence behind the verdict.

## `sources.yaml` format

Part III follows the **Part II** format (see `research/part2/README.md`), because it carries the research fields (kind, design, sample, grade, caveats, flags, topics) that writers use.

- **Keys**: lowercase first-author family name plus the year the work is conventionally cited by (print or issue year), with a letter suffix where needed (`bls2026a`, `bls2026b`, `cullen2023b`). Organisations get a short lowercase name (`leanin2025`, `gallup2025`, `shrm2013`). Undated web pages use the access year (`brown2026`). **Keys are never renamed once written.**
- **Issue year vs online year**: `benson2026` circulated as a working paper from 2021 ("Benson, Li & Shue 2021/2022") and appeared in the *American Economic Review* in 2026. The key uses the issue year, and the record explains the history.
- **Fields**: `type`, `authors` (`"Family, Given"`), `year`, `title`, `container`, `volume`, `issue`, `pages`, `doi`, `url`, `url_checked`, `url_note`, `secondary_urls`, `kind` (evidence | review | theory | data | practitioner), `design`, `supports`, `sample`, `grade`, `caveats`, `flags` (commercial | self-interested | practitioner | not-peer-reviewed), `topics` (derived from which notes cite the key).

## Known gaps (for a follow-up pass)

- **Calibration** has only one academic study (`speer2019`); what happens to people whose manager advocates weakly in the room is untested.
- **Sponsorship's causal effect** on promotion lacks a peer-reviewed estimate here. The mechanisms are documented; the popular percentages are not verified.
- **Mid-career change** has thin direct evidence beyond occupational-mobility data.
- **Regional**: no India-, China- or Korea-specific promotion or title-inflation data was opened; current Japanese age-wage tables were not opened.
- **Tech levels**: only practitioner sources; levels.fyi data and company ladders beyond Dropbox were not opened.
- **New-manager research**: Linda Hill's book and Ashford and Tsui (1991) could not be read in full.
- **The first-time manager "60% fail" figure, GE's vitality curve, the Hewlett "Sponsor Effect" numbers and the WEF skills-change figure** remain unverified (`myths.md`, "Claims deliberately left out").
