# Part I evidence base: getting or switching a job

These are research notes, not book prose, for Part I of the book. Chapter writers and fact-checkers should start at `INDEX.md`, which lists one line per key finding, then read the topic file for context and caveats.

## Files

| File | Covers |
|---|---|
| `INDEX.md` | One line per key verified finding, with grade and source key |
| `myths.md` | 33 popular claims with verdicts; claims deliberately left out |
| `hiring-funnel.md` | Funnel stages and conversion rates, recruiter vs hiring manager, what ATSs do, resume-screen timing |
| `selection-methods.md` | Validity of selection methods (Schmidt & Hunter 1998 → Sackett et al. 2022 and 2024), past-behaviour vs situational questions, impression management |
| `referrals.md` | Referral interview, offer and hire rates; post-hire outcomes; mechanisms; fairness |
| `networking.md` | Weak ties (Granovetter 1973; LinkedIn 2022; Facebook 2017); the "hidden job market" |
| `channels.md` | Cold applications, being sourced, agencies, internal moves, timing, searching while employed |
| `positioning.md` | Resumes, typos, length, keywords, cover letters, audit-study discrimination, GitHub and portfolios, LinkedIn |
| `interviewing.md` | Behavioural and STAR, technical interviews, anxiety, first impressions, power posing, culture fit, questions to ask, legality |
| `offers-negotiation.md` | Anchoring, who negotiates, gender and race backlash, pay transparency, equity basics, counteroffers, exploding offers, background checks |
| `switching.md` | Switcher vs stayer wage growth (with original analysis of Atlanta Fed data), tenure, job hopping, resigning, notice, non-competes, layoffs, unemployment spells |
| `regional.md` | US / UK–EU / India comparison table and known gaps |
| `sources.yaml` | Machine-readable source registry (format below) |

## Method

1. **Sources opened, not remembered.** Every entry in `sources.yaml` points at a URL opened during this research (25 October 2026). Pages were fetched by script and saved outside the repository, or, for a few sites that block scripts, opened through a web-fetch tool, as noted in `url_note`. Abstracts of four journal articles came from the NCBI E-utilities API; those entries carry a `url_opened` field.
2. **Citations checked.** DOIs, volumes and pages were checked against the Crossref API wherever a DOI exists. Where only a working-paper or secondary copy could be opened, `url_note` says so, and claims are limited to what that copy shows.
3. **Primary first.** The order of preference: peer-reviewed papers and meta-analyses; government statistics and statutes; large-sample industry data that discloses its method; then commentary. Commercial or self-interested sources are flagged `commercial: true`, and the conflict is named in `caveats`.
4. **Evidence, practitioner opinion and author view are kept apart.** Topic files mark non-evidence as *Author view* or *practitioner*. Anything not verified is marked **unverified** and must not be printed as fact.
5. **Original analysis is labelled.** The switcher/stayer statistics in `switching.md` §1 were computed by the researcher from the Atlanta Fed's downloadable data file (sheet "Job Switcher", 12-month moving averages, January 1997 – September 2026).

## Grades

| Grade | Meaning |
|---|---|
| **strong** | Peer-reviewed meta-analysis or well-designed experiment or field study; official statistics; statute or regulator text. Can carry a headline claim. |
| **moderate** | A single good study with scope limits; large vendor datasets with a disclosed method; peer-reviewed work read only through a reliable secondary summary; law-firm summaries of current law. Can be stated with caveats. |
| **weak** | Small or unpublished studies, commercial surveys, qualitative opinion data, or a secondary report of an unseen original. Use as illustration, never as proof. |
| **myth-or-unsupported** | No traceable evidence, or contradicted by better evidence. Print only to debunk. |

A finding's grade can differ from its source's grade. For example, a strong source can show that a popular claim is unsupported.

## `sources.yaml` format

YAML is used instead of BibTeX because the registry carries research metadata (grade, sample, caveats, commercial flag) that BibTeX has no fields for. A build step can generate BibTeX or CSL-JSON from it.

- **Top-level key** is a stable lowercase id. The pattern is `firstauthorYEAR` (e.g. `granovetter1973`), with a suffix to disambiguate (`sackett2023-gca`). Organisations get a short slug (`gem2025`, `govuk-notice`). The year in a key is the year the item was first seen (for example its online-first year). The `year` field is canonical: `sackett2023-gca` has `year: 2024`. **Keys are never renamed once written.** New keys are added; obsolete ones are marked with a `deprecated:` field rather than deleted.
- **Fields** (all string values are double-quoted):
  - `type`: article, conference-paper, working-paper, report, industry-report, industry-study, industry-survey, government, statute, dataset, news, web, note
  - `authors`: list of strings, as given by the source or Crossref
  - `year`: integer, the publication year. For undated live pages it is the access year, and `caveats` says so.
  - `title`, `venue`
  - `doi` (optional): verified via Crossref
  - `url`: the page opened
  - `url_note` (optional): what exactly was opened, and any alternative URLs
  - `url_opened` (optional): the machine endpoint actually fetched, when it differs from `url`
  - `accessed`: ISO date
  - `supports`: what the source supports, with key numbers
  - `sample`: sample and context
  - `grade`: one of the four grades above
  - `caveats`
  - `commercial`: boolean
  - `conflicts` (optional)
  - `topics`: list of tags

Validate with any YAML parser. The research run checked that it parses and that every key cited in these notes exists, with no unused keys.

## Known gaps (for a follow-up pass)
- India-specific labour-market data (referral use, tenure, switching premia) is not yet sourced. See `regional.md`.
- UK and EU wage data for job switchers is not sourced.
- Primary text of the UK Equality Act s.60, the EU Directive 2023/970 and the ASQ Bidwell paper could not be opened, because those sites block automated access. Secondary summaries were used and labelled.
