# Part II research: first-principles conduct at work

This folder is the evidence base for Part II of the book: how to interact, behave and act at work.
It holds **research notes for writers**, not book prose. Every factual claim points to a source key in `sources.yaml`, and every source carries a strength grade.

## Files

| File | Covers |
| --- | --- |
| `INDEX.md` | One line per key finding, with grade and source key. Start here. |
| `sources.yaml` | Machine-readable source registry (format below). |
| `myths.md` | Popular claims checked: debunked, overstated, unsupported, or holds. |
| `first-principles.md` | Repeated games and reputation, trust, reciprocity, warmth and competence |
| `authenticity.md` | Self-monitoring, felt authenticity, emotional labour, code-switching, "whole self" |
| `formality.md` | Register, email and chat, emoji, humour, swearing, gratitude |
| `relationships.md` | Friendship, friend-to-manager, favours, gossip, romance, alcohol, boundaries, loneliness |
| `teams.md` | Psychological safety, Project Aristotle, feedback, conflict, difficult conversations |
| `power.md` | Political skill, influence, visibility and credit, managing up, mentors and sponsors, saying no, meetings |
| `remote.md` | Remote and hybrid trials, collaboration, proximity bias |
| `newcomers.md` | Onboarding evidence, first impressions, the "first 90 days" |
| `mistakes.md` | How mistakes are judged, error culture, apologies |
| `burnout.md` | Burnout definitions and measurement, causes, interventions, always-on work |
| `leaving.md` | Why people quit, resigning well, boomerangs, layoffs |
| `ethics.md` | Slippery slopes, ethical fading, whistleblowing, retractions |
| `culture.md` | Hofstede, tightness and looseness, Meyer's Culture Map |

## How to read the notes

Each topic file separates three kinds of statement:

- **Evidence**: what a study, meta-analysis or dataset found.
- **Practitioner model**: a framework from a consultant, author or company that has not been tested like a study (e.g. Radical Candor, the Trust Equation, the Culture Map).
- **Researcher's synthesis**: my interpretation or suggested book angle. This is opinion. Writers may adopt it as the author's view or reject it.

## Grading scale

| Grade | Meaning |
| --- | --- |
| **strong** | Meta-analysis, large pre-registered or multi-lab study, randomised or natural experiment, official statistics, or a foundational and widely replicated finding. |
| **moderate** | Well-designed single study or several smaller consistent studies; respected review or theory; correlational field data with good design. |
| **weak** | Small, single or unreplicated study; self-report survey with undisclosed method; commercial or self-interested source; practitioner model without validation. |
| **myth-or-unsupported** | The claim is contradicted by stronger evidence, retracted, or has no support. |

A grade applies to *what the source can support as used here*, not to the authors. A strong study can be cited weakly if stretched beyond its sample.

**Flags** in `sources.yaml`:

- `retracted`: the paper has been retracted (Crossref title marked RETRACTED and OpenAlex `is_retracted`). Never cite as evidence.
- `commercial`: published by an organisation that sells a related product (e.g. Gallup's Q12, Maslach Burnout Inventory, training).
- `self-interested`: the publisher benefits from the conclusion.
- `practitioner`: practitioner writing, not peer-reviewed research.
- `not-peer-reviewed`: internal or grey literature.
- `coauthor-with-retractions`: not itself retracted (checked on 2026-10-25), but a co-author has retracted papers elsewhere. Pair it with converging evidence.

## Source registry format (`sources.yaml`)

YAML was chosen over BibTeX because it holds the research annotations (grade, sample, caveats, flags, topics) alongside the bibliographic fields, and it is easy to convert.

- **Keys** are lowercase first-author family name (ASCII) plus the year the work is conventionally cited by (the print or issue year), with a letter suffix for same author and year (`mehrabian1967a`, `mehrabian1967b`). Organisations use a short lowercase name (`who2019`, `pew2022`, `google2015`).
- **Keys are permanent.** Never rename one; add a new key instead. Where a paper appeared online a year before its issue, the key uses the issue year and the record notes the difference.
- Bibliographic fields: `type`, `authors` (`"Family, Given"`), `year`, `title`, `container`, `publisher`, `volume`, `issue`, `pages`, `doi`, `url`.
- Verification fields: `url_checked` (date opened), `url_note` (how it was checked), `secondary_urls` (where details beyond the abstract came from).
- Research fields: `kind` (evidence | review | theory | data | practitioner), `design`, `supports`, `sample`, `grade`, `caveats`, `flags`, `topics`.
- The Part I researcher uses the same key format in `research/part1/`. Duplicate entries across the two registries are expected and fine.

## Method

1. **Candidate sources** came from the brief's topic list, plus the meta-analyses and replications that test each claim.
2. **Bibliographic verification** for every DOI source: the DOI was resolved at doi.org (all resolved, HTTP 301/302), and metadata (authors, title, journal, volume, issue, pages, year) was taken from Crossref, not from memory. OpenAlex was queried for the abstract, citation count and retraction status.
3. **Content verification**: each `supports` line is based on the abstract (from OpenAlex, Semantic Scholar or Europe PMC). Where no abstract was retrievable, details were checked through web search results and the URL is listed in `secondary_urls`, or the claim is restricted to what the title states (noted as "title-level").
4. **Web sources** (Gallup, Pew, SHRM, WHO, Google re:Work, HBR, author pages) were fetched and their text read on 2026-10-25. Figures quoted are those on the page.
5. **Not included because they could not be opened**: the US Surgeon General's 2023 loneliness advisory (HTTP 403 from hhs.gov and cdc.gov) and the NYT article on Project Aristotle (HTTP 403). The popular "Sponsor Effect" statistics and practitioner books such as *Difficult Conversations* were not verified and are not in the registry.

## Known limitations

- Abstract-level verification: effect sizes are quoted only where the abstract or an opened page states them. Writers who need more detail (e.g. which apology component matters most, named resignation styles) must read the full text first.
- Much of the evidence comes from WEIRD samples (Western, Educated, Industrialised, Rich, Democratic) and from US workplaces; `culture.md` discusses this.
- "Formality calibration" and "friend becomes manager" have thin direct evidence. The notes say so and mark heuristics as the author's view.
