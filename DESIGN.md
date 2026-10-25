# DESIGN.md: the book's bible

This is the single reference for everyone who works on the book: designer, researchers, chapter writers, fact-checkers and editor. If a chapter and this file disagree, either the chapter changes or this file does, in the same pull request. Never leave the two out of step.

Contents: [1 The book](#1-the-book) · [2 Thesis and through-line](#2-thesis-and-through-line) · [3 Scope](#3-scope) · [4 Table of contents](#4-table-of-contents) · [5 Cast, jokes and arc](#5-cast-running-jokes-and-narrative-arc) · [6 Voice and tone](#6-voice-and-tone) · [7 Element catalogue](#7-element-catalogue) · [8 Visual language](#8-visual-language) · [9 Claim policy](#9-claim-policy) · [10 Length](#10-length-targets) · [11 Writer assignments](#11-writer-assignments) · [12 Status of the evidence](#12-status-of-the-evidence)

---

## 1. The book

**Title:** *Two Games, One You*
**Subtitle:** *A field guide to landing the job and being yourself at work*

**Audience.** Early- to mid-career people (roughly the first fifteen years of working life, including students about to start) who want to get a job, change jobs, or get better at the one they have. The examples lean towards technology jobs, because the protagonist is a software tester becoming a developer, but nothing depends on writing code, and the book is meant to be useful to anyone who works with other people.

**Readers are global.** The research base is mostly American and Western European, and the book says so where it matters. Practice that differs by region (notice periods, at-will employment, pay-transparency laws, non-competes, what an employer may ask, CV conventions) goes in **Field Notes** naming only the regions we could verify: currently the US, the UK and EU (Germany in particular) and India. Where a region is missing, we say we did not find verified data; we never guess.

**Format.** A static website built from Markdown sources (`python3 tools/build.py` into `docs/`, served by GitHub Pages at https://omkarbhale.github.io/career-book/). The licence is MIT (see `LICENSE`).

**Style.** Inspired by the learner-centred approach of the *Head First* series, without its name, element names or trade dress. `research/style/README.md` records what we borrow, adapt and avoid, and why.

---

## 2. Thesis and through-line

### The thesis

> Getting a job and doing a job are different games. In the **snapshot game**, strangers judge an edited trailer of you, quickly and noisily. In the **long game**, colleagues watch the whole film, every day, for years. The skills differ, so learn both. But play them as **one person**: learn the snapshot game without shame, play the long game without a mask, and keep the trailer a true cut of the film.

This answers both halves of the owner's brief at once. Part I takes "getting a job is a different skill from doing it" seriously and teaches that skill without apology. Part II takes "not an act, but simply who you are" seriously and builds conduct from first principles rather than etiquette. The thesis says why these are one book: the same person plays both games, and each game feeds the other.

### The through-line: the loop

The two games form a loop (Figure 1.3):

1. The **snapshot game** gets you into a job.
2. The **long game** in that job produces skills, stories, a reputation and people who will vouch for you.
3. Those become the raw material of your **next snapshot**: the evidence in your résumé, the stories in your interviews, the referral that gets you seen.

Every chapter should be able to say where it sits on the loop. Part I chapters regularly point *forward* to the long game ("this is why the trailer must be true"), and Part II chapters regularly point *back* to the snapshot game ("this is how today becomes your next interview story"). The epilogue closes the loop on the page: Dev, now a trusted colleague, refers Bea, and the long game of one person becomes the snapshot of another.

### Three rules (the book's spine)

Chapter 1 states them; every later chapter is an elaboration of one or more.

1. **Learn the snapshot game without shame.** Making real value legible is translation, not spin. (Part I.)
2. **Play the long game without a mask.** Good defaults beat good performances. (Part II.)
3. **Keep the two honest with each other.** The trailer must never promise what the film cannot deliver; a good film deserves a trailer. (Both parts; the loop.)

### Recurring metaphors

- **Trailer / film** for snapshot / long game. Use it; do not overuse it (at most a handful of times per chapter).
- **Signals** (Spence): strong signals are specific, checkable and costly to fake.
- **Repeated game** (Axelrod): at work, people remember.
- **The dial** (Chapter 14): professionalism is a setting you adjust, not a costume.

---

## 3. Scope

### Added beyond the brief, and why

| Addition | Where | Why |
| --- | --- | --- |
| Whether to switch at all, internal moves, layoffs, career changers | Ch 2 | "How to get a job" starts with "should I?"; a layoff is how many people enter the snapshot game. |
| How hiring works from the employer's side, with funnel numbers | Ch 3 | Most job-search misery comes from misreading the funnel; the numbers are well sourced (`gem2025`, `careerplug2025`). |
| Bias and discrimination in hiring | Ch 3, Ch 5, Ch 9 | Honesty: the snapshot game is not fair, and audit studies show by how much (`bertrand2004`, `quillian2017`, `kline2022`, `thorat2009`). Readers deserve to know what is and isn't about them. |
| Offers, negotiation, pay transparency, resigning, notice and counter-offers | Ch 9 | The end of the snapshot game has large money consequences and strong evidence. |
| Mistakes and apologies | Ch 12 | Reliability includes recovering well; the research is clear and useful (`kim2004`, `savitsky2001`). |
| Remote and hybrid work | Ch 14, Ch 11 | Much early-career work is now partly remote; the evidence is strong (`bloom2015`, `bloom2024`, `emanuel2026`). |
| Workplace romance, alcohol and loneliness | Ch 15 | Part of office relationships whether or not a book mentions them. |
| Ethics and speaking up | Ch 16, Ch 17 | "Who you are" is tested most under pressure (`kishgephart2010`, `welsh2015`). |
| Burnout and boundaries | Ch 17 | Being yourself includes being a person with limits (`who2019`, `panagioti2017`). |
| Myth Checks throughout | everywhere | Careers advice is full of confident folklore (both research bases list 50+ checked myths). |

### Left out, and why

| Left out | Why |
| --- | --- |
| Managing people | A different book; the audience is mostly individual contributors. Ch 15 and Ch 17 touch on a friend becoming your manager and on growth, and stop there. |
| Freelancing, starting a business | A different game with different rules. |
| Detailed legal advice | Laws change and differ; the book points at laws and tells readers to check. |
| Salary figures by role or city | They date in months and vary by market; Ch 9 teaches how to find them. |
| Interview question banks and coding drills | Plenty exist elsewhere and they date quickly; Ch 7 and Ch 8 teach the skill behind them. |
| Personality typing (MBTI and similar) | Weak evidence for workplace decisions; not needed for the argument. |
| Clinical mental-health advice | Ch 17 explains burnout as the WHO defines it and points to professional help. |
| Immigration and visas | Too jurisdiction-specific to cover responsibly; Ch 2 names it as a factor and stops. |

---

## 4. Table of contents

The spine lives in `book/book.toml` (titles, order, one-line summaries, "what it will cover"); this section is the full brief. Evidence keys resolve in `research/part1/sources.yaml`, `research/part2/sources.yaml` or `book/sources/*.yaml`; the topic files in `research/part1/` and `research/part2/` hold the detail and caveats. Writers must read the cited topic files before drafting.

Cross-references: **Back** lists chapters this one must refer to; **Forward** lists chapters it must set up. Use chapter ids (`[[ch07]]`) until the target chapter exists, then refine to section ids.

### Front matter (done)

- **How to Use This Book** (`howto`): who it is for and not for; the idea in one paragraph; how it is built to teach (with sources); a live sample of every element; how to read evidence grades; reading routes; honest limits.
- **Meet the Cast** (`cast`): the six characters, running jokes, model sheet (Figure B.1).

### Opening

#### Chapter 1: Two Games, One You (`ch01`, done, the exemplar)

- **Purpose.** Set up the thesis, the two games, the loop and the cast; teach the reader how the book's elements work by using them.
- **Key ideas.** Hiring is prediction under uncertainty; the best single method correlates about .42 (±.24) with performance; interviews also reward self-promotion and punish nerves; strong signals are specific, checkable and costly to fake; work is a repeated game; acting is expensive; you will play both games many times; the loop; the quadrant; the three rules.
- **Evidence.** `sackett2022`, `sackett2023-iop`, `barrick2009`, `levashina2014`, `powell2018`, `spence1973`, `spence2001-lecture`, `axelrod1981`, `hulsheger2011`, `sutton2020`, `bls-nlsy2025`, `bls-tenure2026`, `brown2016`, `rajkumar2022`, `lii-atwill`, `govuk-notice`, `khaitan-notice`.
- **Figures.** 1.1 two games compared; 1.2 what r = .42 looks like (simulated); 1.3 the loop; 1.4 the quadrant; 1.5 map of the book.
- **Exercises.** Signal or noise?; your two scorecards (revisited in the epilogue); which game is it?
- **Forward.** Every chapter, via the map; explicitly Ch 2, 3, 4, 5, 6, 8, 9, 10, 11, 14, 17 and the epilogue.

### Part I: The Snapshot Game (getting or switching a job)

#### Chapter 2: Stay, Go, or Grow? (`ch02`, assignment A)

- **Purpose.** Decide whether to switch at all, and how: push versus pull, moving internally, timing, searching while employed, and what to do when the decision is made for you.
- **Key ideas.** Separate what is wrong here from what is right there; switchers' wage growth beats stayers' in most months, but by little on average and not always (`atlantafed-wgt`); many short stints cost callbacks (`cohn2021`); external hires are paid more but rated lower at first, so internal moves deserve a look (`bidwell2011`); employed searchers get more and better offers (`faberman2017`); current unemployment cuts callbacks, past unemployment much less (`kroft2013`, `eriksson2014`); why people really quit (`pew2022`); boomerangs (`arnold2021`); layoffs: notice rules, health and well-being costs, what to do in week one (`warn-2102`, `mckeeryan2005`, `sullivan2009`, `trevor2008`); career changers: what transfers.
- **Myth Checks.** "Job hoppers always earn more" (overstated); "Any gap on your résumé is fatal" (overstated); "People leave managers, not companies" (weak; `gallup2015`, `pew2022`).
- **Field Notes.** Notice and non-competes in the US, UK and EU, and India (`govuk-notice`, `bgb622`, `khaitan-notice`, `uschamber-ryan`, `loeb2023-california`, `barandbench-s27`, `cms2025-uk-noncompete`).
- **Figures.** 2.1 push and pull, as a balance; 2.2 switchers versus stayers, a simple annotated chart using only the verified summary numbers; 2.3 stay, go or grow, as a decision path.
- **Exercises.** Push or pull? (sort reasons); your runway (months of savings and notice); the conversation before you leave (draft it).
- **Story.** Dev asks her manager at Corvid about moving into development and gets "maybe next year". She decides to search while employed. The spreadsheet gains a *Runway* tab. Rex's six jobs in eight years become a talking point.
- **Back:** ch01 (many games). **Forward:** ch03, ch09 (resigning, notice), ch17 (leaving, from the other end).

#### Chapter 3: The View from the Other Side of the Table (`ch03`, assignment A)

- **Purpose.** Show hiring as the employer experiences it, so the reader stops taking the funnel personally and starts playing it well.
- **Key ideas.** Requisitions, recruiters and hiring managers: who wants what (`shrm2015-recruiters`, weak); funnel numbers: about 0.4% of inbound applicants hired in one large dataset, with referred and sourced candidates converting far better (`gem2025`), 180 applicants per hire at small firms (`careerplug2025`); hiring has slowed (`gem2025`); what applicant tracking systems actually do: knockout filters configured by people (`hiddenworkers2021`); validity of selection methods (`sackett2022`, `schmidt1998`); bias in the funnel (audit studies: `bertrand2004`, `quillian2017`, `kline2022`; India: `thorat2009`); most rejections are statistics, not verdicts; morale.
- **Myth Checks.** "ATS software rejects 75% of résumés" (unsupported; `interviewguys-ats-myth`); "Every job gets 250 applications" (unsupported number; `sullivan2013`).
- **Figures.** 3.1 the funnel, inbound versus referred (verified numbers only); 3.2 who's in the room: the people behind one job opening; 3.3 why 40 rejections can be normal (an illustrative probability chart labelled as such).
- **Exercises.** Funnel maths; decode a job ad (must-haves versus wish lists); rejection reframing.
- **Story.** Meera (mug: ASK ME ABOUT MY FUNNEL) walks Dev through a requisition from her side. Dev recolours her 46 noes as funnel arithmetic. Bea points out that the funnel is not neutral, and the chapter takes her seriously.
- **Back:** ch01 (noise), ch02. **Forward:** ch05 (paper and ATS), ch06 (referrals), ch07 (structured interviews).

#### Chapter 4: Know What You're Selling (`ch04`, assignment A)

- **Purpose.** Turn experience into evidence: an inventory of results, a story bank, and targets chosen on purpose.
- **Key ideas.** Duties versus outcomes; a story bank of 8 to 12 true stories covers most interview questions, because past-behaviour questions are common and slightly more predictive than hypotheticals (`levashina2014`); choosing targets where what you want, what they need and what you can show overlap; applying when you are close rather than perfect (the "100% fit" myth: `mohr2014`, `salwender2024`); career changers translating rather than overselling; employers reading hard-to-fake evidence such as code history (`marlow2013`, weak). Much of this chapter is craft: label it.
- **Myth Check.** "Women only apply when they meet 100% of the requirements" (unsupported as stated).
- **Figures.** 4.1 from duty to evidence (a before-and-after transformation); 4.2 the story bank grid (stories against what they show); 4.3 the target overlap.
- **Exercises.** Duty to evidence (rewrite three); your first five stories; a target list of ten.
- **Story.** Dev and Bea build story banks at Bea's kitchen table. Bea discovers she has twelve good stories she has never told anyone. Spreadsheet tab: *Story bank*.
- **Back:** ch01 (signals). **Forward:** ch05, ch07, ch11 (stories are made in the long game).

#### Chapter 5: Paper You (`ch05`, assignment A)

- **Purpose.** The résumé, profile and portfolio as a trailer: compressed, true evidence that survives a fast read and a slow one.
- **Key ideas.** Bullets that carry outcomes; typos cost real interviews (`sterkens2023`); length rules are folklore (`resumego2018-length`, weak); the six-second claim and what it actually measured (`ladders2012`, `ladders2018`); cover letters: weak evidence either way (`resumego2020-cover`, `aacsb2020-twimc`); profiles and photos (`sej-linkedin-photo`); portfolios and code (`marlow2013`); names and discrimination on paper (`bertrand2004`, `kline2022`, `thorat2009`); regional CV norms (`ncs-cv`, `europass-cv`, `eeoc-prohibited`).
- **Myth Checks.** "Recruiters read your résumé for 6 seconds" (overstated); "Your résumé must be one page" (unsupported as a rule); "LinkedIn photos get 21 times more views" (unsupported); "A typo or two doesn't matter" (false).
- **Field Note.** CV conventions: photos, age, marital status (US, UK, EU, India), from `regional.md`.
- **Figures.** 5.1 anatomy of a résumé as a trailer; 5.2 the first glance and the full read; 5.3 regional CV differences.
- **Exercises.** Fix three bullets; spot the myth; the follow-up test (could you defend each line for five minutes?).
- **Story.** Dev rewrites hers; Rex's is too polished to believe; Bea refuses to "brag" until Dev reframes it as accuracy. Spreadsheet tab: *Bullets that work*.
- **Back:** ch01 (signals, trapdoor on upgrading), ch03 (ATS), ch04. **Forward:** ch06, ch07, ch09 (background checks).

#### Chapter 6: People, Not Portals (`ch06`, assignment B)

- **Purpose.** Referrals, weak ties and asking for help, done honestly, without becoming someone who "networks".
- **Key ideas.** Referrals are a small share of applicants and a large share of hires (`brown2016`, `gem2025`, `careerplug2025`); referred hires stay longer and fit better (`burks2015`, `pallais2016`); weak ties help up to a point (`granovetter1973`, `rajkumar2022`, `gee2017`); 50 to 60% of job seekers use a contact (`lester2021`); people underestimate how willing others are to help (`flynn2008`); reciprocity and its half-life (`regan1971`, `burger1997`); the liking gap (`boothby2018`); referrals can entrench sameness (`fernandez2019`); recruiters and agencies (`govuk-agency-fees`, `topechelon-fees`); the "hidden job market" percentage (`fresnostate2024-hidden`).
- **Myth Checks.** "80% of jobs are never advertised" (the percentage is unsupported; the mechanism is real); "Weak ties are always better than strong ties" (overstated); "It's not what you know, it's who you know" (half-true).
- **Figures.** 6.1 your tie map (strong, weak, dormant); 6.2 the referral funnel (`brown2016` numbers); 6.3 anatomy of a good ask.
- **Exercises.** Map your ties; write a four-sentence ask; guess-then-check (how many people would say yes?).
- **Story.** Dev messages Ana, a university acquaintance now at Lanternfish, nervously; Ana replies within an hour and refers her. Rex's profile headline is now "Chief Possibility Officer". Spreadsheet tab: *People*.
- **Back:** ch01 (the loop), ch03. **Forward:** ch07, ch15 (relationships), ch17 (giving back), epilogue (Dev refers Bea).

#### Chapter 7: Interviews, Decoded (`ch07`, assignment B)

- **Purpose.** What interviews measure and how to show it: structured and behavioural questions, stories that land, nerves, formats, the law, and interviewing the employer back.
- **Key ideas.** Structure beats gut feel (`sackett2022`); past-behaviour versus situational questions (`levashina2014`); impression management and where presenting becomes pretending (`levashina2014`, `barrick2009`); early impressions and rapport (`barrick2010`, `swider2016`; thin slices were about teachers: `ambady1993`); nerves are a small, real effect (`powell2018`); "culture fit" (`rivera2012`); brainteasers (`abc2013-google`); illegal questions (`eeoc-prohibited`, `ukparl2020-health`); questions to ask them, and red flags.
- **Myth Checks.** "Interviewers decide in the first seven seconds" (overstated); "93% of communication is non-verbal" (false as generalised; `mehrabian-site`); power posing (`carney2016`, `forrt-powerposing`); "A firm handshake matters" (true-ish, small; `stewart2008`); "If you're nervous, you've blown it" (overstated).
- **Figures.** 7.1 anatomy of a story answer; 7.2 what a structured scoring sheet looks like; 7.3 nerves, to scale.
- **Exercises.** Two-minute story; spot the unlawful question (with Field Note); five questions to ask them.
- **Story.** Dev interviews at Lanternfish with Tomás and a panel; Bea redoes a phone screen using her story bank; Meera (mug: STRUCTURE IS KINDNESS) explains scoring sheets. Spreadsheet tab: *Questions for them*.
- **Back:** ch01 (noise, self-presentation), ch04. **Forward:** ch08, ch11 (promises made in interviews), ch14 (culture).

#### Chapter 8: Show, Don't Tell (`ch08`, assignment B)

- **Purpose.** Work samples: technical interviews, take-home tasks, case studies and presentations; preparing without memorising; boundaries on unpaid work.
- **Key ideas.** Work samples predict reasonably well (`sackett2022`); being watched can halve performance on a coding task (`behroozi2020`); single-interview scores are noisy (`interviewingio2016`, weak); narrate your thinking; scoping a take-home and asking questions first; when a task is free consulting [!view]; case interviews and presentations for non-technical roles (craft, labelled).
- **Myth Check.** "Technical interviews objectively measure coding skill" (overstated).
- **Figures.** 8.1 watched versus alone (`behroozi2020`); 8.2 scoping a take-home; 8.3 thinking out loud, annotated.
- **Exercises.** Talk-aloud practice; what would you ask before starting?; time-box a take-home.
- **Story.** Dev's Lanternfish take-home: she asks two clarifying questions and caps her time. Bea's live coding goes better once she narrates. Spreadsheet tab: *Take-homes (boundaries!)*.
- **Back:** ch01 (strong signals), ch07. **Forward:** ch09, ch12 (estimates).

#### Chapter 9: Offers, Negotiation, and the Exit (`ch09`, assignment B)

- **Purpose.** Read and negotiate an offer, understand regional pay rules, handle checks and references, resign well, and arrive ready for Part II.
- **Key ideas.** Total compensation; India's CTC versus take-home (`tickertape-ctc`, weak; `argus-labourcodes`); anchoring and first offers (`galinsky2001`); who bargains and what it is worth (`hallkrueger2012`); gender and race penalties for negotiating, and what reduces them (`leibbrandt2015`, `bowles2007`, `hernandez2019`); pay transparency by region (`clockspot-paytransparency`, `nydol-paytransparency`, `cooley2026`, `ec-paytransparency`, `lockton2026-eu`) and its effect on pay (`cullen2023`); exploding offers (`niederle2009`); background checks (`eeoc-ftc-background`) and ban-the-box (`agan2018`); resigning: notice (`govuk-notice`, `bgb622`, `khaitan-notice`, `lii-atwill`), resignation style (`klotz2016`), counter-offers, boomerangs (`arnold2021`).
- **Myth Checks.** "Never name a number first" (overstated); "Women don't negotiate" (overstated); "Negotiating is always free" (false for some); "Pay transparency raises everyone's pay" (unsupported); "80% of people who accept a counter-offer leave" (unsupported).
- **Field Notes.** Pay transparency (US states, EU directive, UK, India); notice and final pay; background checks.
- **Figures.** 9.1 what's really in an offer; 9.2 how an anchor pulls; 9.3 notice and pay rules by region.
- **Exercises.** Compare two offers; draft a counter; write the resignation (two versions, and which one Corvid remembers).
- **Story.** Lanternfish offers; Dev negotiates once, calmly; Corvid counter-offers; Meera (mug: IT DEPENDS) helps her think; Dev leaves well, handing over her test suite properly. Spreadsheet tabs: *Offers*, then *Feelings* (deleted the next morning).
- **Back:** ch02 (resigning), ch05 (checks). **Forward:** Part II (ch10, ch11), ch17 (pay and promotion).

### Part II: The Long Game (being yourself at work, from first principles)

#### Chapter 10: First Principles: Trust Is the Whole Game (`ch10`, assignment C)

- **Purpose.** The model under all of Part II: repeated interactions, what trust is made of, reciprocity, warmth and competence, and why authentic defaults beat performances.
- **Key ideas.** Repeated games and reputation (`axelrod1981`, `nowak2006`, `nowak1998`, `fehr2000`); trust as ability, benevolence and integrity (`mayer1995`, `colquitt2007`); the Trust Equation as a practitioner heuristic (`maister2000`, weak); bad impressions outweigh good (`baumeister2001`); reciprocity (`regan1971`, `burger1997`, `flynn2003`); helping beyond the role, and its costs (`podsakoff2009`, `bolino2005`, `bergeron2007`); warmth and competence (`fiske2002`, `fiske2007`); rudeness spreads (`porath2007`); self-monitoring (`day2002`, `lei2025`, `kilduff1994`); felt authenticity (`fleeson2010`, `sutton2020`, `cha2019`, `ibarra2015`); surface versus deep acting (`hulsheger2011`, `grandey2003`).
- **Myth Check.** "Inauthenticity makes people feel immoral" (retracted; `gino2015`; cite only as a myth's origin).
- **Figures.** 10.1 three things trust is made of; 10.2 the repeated game, round by round; 10.3 surface acting versus deep acting.
- **Exercises.** Trust audit of one working relationship; write your five defaults.
- **Story.** Dev's first morning at Lanternfish: Old Faithful, the coffee machine, breaks, and how each person responds becomes the chapter's case study. Meera (mug: SAME TEAM) on the phone that evening.
- **Back:** ch01 (repeated game, acting), ch09. **Forward:** every Part II chapter.

#### Chapter 11: The First Ninety Days (`ch11`, assignment C)

- **Purpose.** Starting well: learning how the place really works, first impressions without performance, asking questions, early wins, and keeping the promises the trailer made.
- **Key ideas.** Role clarity, self-efficacy and social acceptance drive newcomer success (`bauer2007`); information-seeking helps (`morrison1993`); feedback-seeking declines with tenure, so ask early (`anseel2015`); "90 days" is a convention, not a law (`watkins2003`, weak); onboarding that lets people show their best selves helped retention (`cable2013`, flagged); fast trait judgments from faces (`willis2006`) and the liking gap (`boothby2018`); people judge your blunders less harshly than you expect (`savitsky2001`); proximity and feedback for juniors (`emanuel2026`).
- **Myth Check.** "The first 90 days are a magic window" (unsupported as a number).
- **Figures.** 11.1 what makes a newcomer succeed; 11.2 the liking gap; 11.3 a first-month map (people, tools, unwritten rules).
- **Exercises.** Map your first month; list the promises your trailer made; three questions to ask this week.
- **Story.** "Corporate Dev": stiff, over-formal, afraid to ask. Kai rescues her at lunch. Tomás sets expectations in their first one-to-one. Dev starts a *Wins* tab in the spreadsheet (paid off in Ch 17).
- **Back:** ch07 (promises), ch10. **Forward:** ch12, ch13, ch14, ch17 (brag document).

#### Chapter 12: Reliability, the Boring Superpower (`ch12`, assignment C)

- **Purpose.** Commitments, estimates, follow-through, mistakes, saying no, and working with your manager.
- **Key ideas.** Reliability as the cheapest trust you can buy [!view]; estimates and telling people early; how mistakes are actually judged (`savitsky2001`, `gilovich2000`); apologies: competence versus integrity failures (`kim2004`), complete apologies (`lewicki2016`), superfluous apologies (`brooks2014`); error-reporting cultures (`edmondson1996`); saying no costs less than people expect (`givi2024`); the manager relationship differs within a team and matters (`dulebohn2012`); asking for help (`flynn2008`).
- **Myth Check.** The pratfall effect (holds weakly; one small 1966 study, `aronson1966`).
- **Figures.** 12.1 the commitment loop; 12.2 bad news early versus late; 12.3 anatomy of an apology.
- **Exercises.** Rewrite a vague commitment; write the early-warning message; decline gracefully.
- **Story.** Dev misses an estimate and tells Tomás on a Friday afternoon (his least favourite kind of surprise). Recovery. Dev files the Old Faithful ticket that nobody else files.
- **Back:** ch08 (estimates), ch10, ch11. **Forward:** ch13, ch16, ch17.

#### Chapter 13: Talking and Writing at Work (`ch13`, assignment C)

- **Purpose.** Messages, meetings, async writing, disagreement, and feedback in both directions.
- **Key ideas.** People overestimate how well their tone comes across in writing (`kruger2005`); after-hours messages and reply expectations (`giurge2021`, `becker2021`, `belkin2020`); smileys and first impressions (`glikson2018`); gratitude is undervalued (`kumar2018`); feedback helps on average but often backfires (`kluger1996`); the feedback sandwich (`parkes2013`); Radical Candor as a practitioner model (`scott2017`); meetings (`rogelberg2010`) and brainstorming (`mullen1991`); challenging voice is penalised more than supportive voice (`burris2012`); venting (`bushman2002`).
- **Myth Checks.** The feedback sandwich (unsupported); "Group brainstorming produces more ideas" (debunked); "Venting anger gets it out of your system" (debunked).
- **Figures.** 13.1 point first: the shape of a good message; 13.2 the tone gap; 13.3 feedback that helps versus feedback that hurts.
- **Exercises.** Rewrite a message; give feedback using a script; meeting or message?
- **Story.** Dev's 400-word chat message that should have been two lines; Kai's emoji habit; Tomás gives Dev hard feedback well, and Dev gives him some back.
- **Back:** ch10, ch12. **Forward:** ch14, ch16.

#### Chapter 14: The Professionalism Dial (`ch14`, assignment D)

- **Purpose.** When to be formal or casual, humour that lands, what to share about your life, culture and code-switching, remote and hybrid presence: being yourself at the right setting.
- **Key ideas.** Professionalism as a dial set by context [!view]; humour raises status when it lands and costs when it fails (`bitterly2017`), not equally for everyone (`evans2019`); positive humour and well-being (`mesmermagnus2012`); profanity (`defrank2019`, weak); non-conformity as a privilege of status (`bellezza2014`); code-switching and its costs (`mccluney2021`, `mccluney2019`); self-disclosure and status (`gibson2018`); work-home boundaries (`kreiner2006`, `rothbard2005`); authenticity and power (`cha2019`); culture varies more within countries than between them (`taras2016`); cultural values predict modestly (`taras2010`, `hofstede2011`); tight and loose cultures (`gelfand2011`); the Culture Map as a practitioner framework (`meyer2014`); remote and hybrid evidence (`bloom2015`, `bloom2024`, `yang2022`, `emanuel2026`, `gajendran2007`, `elsbach2010`, `bernstein2018`).
- **Myth Checks.** "Gen Z and millennials are fundamentally different at work" (overstated; `costanza2012`); "Open-plan offices increase collaboration" (debunked; `bernstein2018`).
- **Field Note.** Directness and hierarchy across cultures, with the caveat that individuals vary more than countries.
- **Figures.** 14.1 the dial; 14.2 humour: reward and risk; 14.3 culture within versus between countries.
- **Exercises.** Read the room (scenarios); the disclosure decision; your remote-presence plan.
- **Story.** Dev's joke at the all-hands lands badly, and she recovers; Kai shares more than Dev would; a conversation about code-switching with a colleague; the Old Faithful chat channel.
- **Back:** ch01 (author's view on limits), ch10, ch13. **Forward:** ch15, ch16.

#### Chapter 15: Office Friendships (`ch15`, assignment D)

- **Purpose.** Friendship at work: its benefits and costs, boundaries, gossip, romance, alcohol, loneliness, and when a friend becomes your manager.
- **Key ideas.** Workplace friendship is a mixed blessing (`methot2016`); friendship and work norms conflict (`pillemer2018`); promotion strains friendships (`sias2004`, weak); closeness takes time (`hall2019`); the liking gap (`boothby2018`, `mastroianni2021`); "best friend at work" (`gallup2022`, weak, commercial); the Ben Franklin effect (`jecker1969`, `niiya2016`, weak); gossip, mostly neutral and sometimes protective (`robbins2020`, `feinberg2012`); dating a superior (`malachowski2012`); romance prevalence (`shrm2023`, weak); alcohol (`frone2006`, `sayette2012`); switching off (`sonnentag2012`); loneliness (`gallup2024`, `ozcelik2018`).
- **Myth Check.** "Dunbar's number limits you to 150 relationships" (unsupported; `lindenfors2021`).
- **Figures.** 15.1 friendly to friends, a spectrum; 15.2 hours to friendship; 15.3 a boundary map.
- **Exercises.** Boundary scripts; the friend-becomes-manager scenario; who would you call?
- **Story.** Dev and Kai become friends. Kai is promoted to lead the design and test squad, and both have to renegotiate.
- **Back:** ch06 (weak ties), ch10, ch14. **Forward:** ch16, ch17, epilogue.

#### Chapter 16: Conflict, Politics, and Difficult People (`ch16`, assignment D)

- **Purpose.** Disagreement, credit, gossip, difficult colleagues and managers, psychological safety, and what to do when something is actually wrong.
- **Key ideas.** Political skill as an honest capability (`munyon2015`, `bing2011`, `ferris2005`); influence tactics (`higgins2003`); people over-claim credit (`ross1979`); credit is biased by gender (`sarsons2021`); task versus relationship conflict (`dewit2012`, `dedreu2003`); voice and its risks (`burris2012`); psychological safety (`edmondson1999`, `frazier2017`, `deng2019`; Project Aristotle as internal evidence: `google2015`); rudeness (`porath2007`); difficult behaviour and team spillover (`felps2006`); ethics: bad apples, cases and barrels (`kishgephart2010`); slippery slopes (`welsh2015`); who detects fraud (`dyck2010`); escalation and wrongdoing.
- **Myth Checks.** "Task conflict is good for teams" (overstated); "Emotional intelligence matters more than IQ" (overstated; `joseph2010`, `oboyle2011`); "Google proved psychological safety is the key" (overstated).
- **Figures.** 16.1 task versus relationship conflict; 16.2 the credit gap; 16.3 an escalation ladder.
- **Exercises.** Separate the task from the person; share credit in writing; when to escalate.
- **Story.** A colleague presents Dev's fix as his own. Rex joins Lanternfish (his trailer worked again; headline "Visionary-in-Residence"), and Dev sees his film up close. The Old Faithful committee becomes a politics lesson.
- **Back:** ch10, ch13, ch14. **Forward:** ch17.

#### Chapter 17: Growing Without Losing Yourself (`ch17`, assignment D)

- **Purpose.** Visibility without bragging, reviews and promotion, sponsors, boundaries and burnout, integrity under pressure, and knowing when to play the snapshot game again.
- **Key ideas.** Self-promotion misfires (`scopelliti2015`) and backlash is unequal (`rudman1998`); a brag document as the long game's evidence locker [!craft]; mentoring's small objective effects (`allen2004`, `eby2008`) and sponsorship (`ibarra2010`, practitioner); low-promotability tasks (`babcock2017`); burnout as the WHO defines it (`who2019`), measurement problems (`rotenstein2018`), organisational versus individual fixes (`panagioti2017`), long hours (`pega2021`), demands and resources (`bakker2007`, `maslach2001`, `maslach2016`); slippery slopes (`welsh2015`); why people quit (`pew2022`), resigning well (`klotz2016`), boomerangs (`arnold2021`).
- **Myth Checks.** "10,000 hours makes you an expert" (overstated; `macnamara2014`, `macnamara2019`); the critical positivity ratio (debunked; `brown2013`); ego depletion (overstated; `hagger2016`); the Hawthorne effect (debunked as told; `levitt2011`).
- **Figures.** 17.1 the brag document; 17.2 demands and resources; 17.3 back to the loop: when the long game says "time to move".
- **Exercises.** Start your brag document; a burnout inventory; stay, go or grow, revisited (a callback to Ch 2).
- **Story.** Dev's first review: the *Wins* tab becomes a brag document. She notices she has become the unofficial Old Faithful mechanic and stops. A recruiter calls about a great job; she weighs it using everything she has learned.
- **Back:** ch02 (stay or go), ch11, ch12, ch16. **Forward:** epilogue.

#### Epilogue: The Loop (`epi`, assignment D)

- **Purpose.** Close the loop on the page and give the whole book on one page.
- **Content.** A year on: Dev refers Bea to Lanternfish; Bea's trailer finally matches her film. Rex asks Dev for a reference and Dev gives an honest one; Rex's headline is now just "Engineer". The reader revisits their scorecards from Your Move 1.2. The book on one page: the three rules and one line per chapter.
- **Back:** ch01 (scorecards, loop), ch06 (referrals), every chapter in the one-page summary.

---

## 5. Cast, running jokes and narrative arc

All characters and companies are fictional. Do not change a character's facts without changing this section in the same pull request.

| Character | Facts | Role | Arc |
| --- | --- | --- | --- |
| **Dev** (Devika Rao), she/her, 27 | QA engineer at Corvid Systems (IT services, insurance clients) for three years; moves to Lanternfish (a ~200-person logistics-software company) as a backend developer at the end of Part I. Mustard hoodie, teal hair clip, laptop with stickers. Careful, wry, allergic to fakery. | Protagonist | Part I: from "I won't play" to playing well as herself. Part II: from stiff "Corporate Dev" to a trusted colleague with boundaries. Epilogue: refers Bea. |
| **Bea** (Beatriz Santos), she/her, 31 | Senior engineer at Corvid. Headphones, round glasses, green cardigan. Brilliant, private, dreads phone screens, sharp about unfairness in hiring. | All film, no trailer | Learns to build a trailer (Ch 4, 5, 7, 8) without losing herself; joins Lanternfish via Dev's referral (epilogue). |
| **Rex** (Rex Calloway), he/him, 29 | Six jobs in eight years. Red blazer, big grin. Generous, funny, superb in interviews; his work trails off. | All trailer | Appears in Part I as the foil. Joins Lanternfish in Ch 16; Dev sees his film. Starts to change by the epilogue. Never a villain. |
| **Meera** (Meera Iyer), she/her, 54 | Dev's first team lead; now an engineering director elsewhere; has hired 200+ people. Grey bun, glasses, plum shawl, always a mug. | The voice from the other side of the table | Mentor throughout; her advice is labelled as experience, never as evidence. |
| **Tomás** (Tomás Rivera), he/him, 41 | Engineering manager at Lanternfish. Beard, blue plaid shirt. Calm, direct, hates Friday-afternoon surprises. | Hiring manager in Part I, manager in Part II | Has to live with whom he hired; models giving and receiving feedback. |
| **Kai** (Kai Mensah), they/them, 26 | Product designer at Lanternfish. Lavender hair, hoop earring, striped top. Open, warm, overshares. | Office friendship | Becomes Dev's friend (Ch 11), then her squad lead (Ch 15). |

Minor characters (use sparingly, introduce with one line): **Ana**, Dev's university acquaintance at Lanternfish who refers her (Ch 6); Dev's manager at Corvid (Ch 2, Ch 9), unnamed or named once.

Character speech is opinion and story, not evidence. A character may *say* something the research supports, but the surrounding prose carries the citation.

### Running jokes, and who owns which beat

Parallel writers must use these beats and no others for the same joke, so the jokes accumulate instead of colliding.

| Joke | Beats |
| --- | --- |
| **The Spreadsheet**: Dev's job search grows tabs | Ch 1: *Game 1*, *Game 2*, *Should I stay?* · Ch 2: *Runway* · Ch 3: *Funnel maths* · Ch 4: *Story bank* · Ch 5: *Bullets that work* · Ch 6: *People* · Ch 7: *Questions for them* · Ch 8: *Take-homes (boundaries!)* · Ch 9: *Offers*, then *Feelings* (deleted next morning) · Ch 11: *Wins* · Ch 17: *Wins* becomes her brag document |
| **Meera's mugs**: never an accident | Ch 1: THE MAP IS NOT THE TERRITORY · Ch 3: ASK ME ABOUT MY FUNNEL · Ch 7: STRUCTURE IS KINDNESS · Ch 9: IT DEPENDS · Ch 10: SAME TEAM · Ch 17: REST IS PRODUCTIVE (she is on leave) |
| **Rex's profile headline** | Ch 1 (mention only): "Builder. Dreamer. Disruptor." · Ch 6: "Chief Possibility Officer" · Ch 16: "Visionary-in-Residence" · Epilogue: "Engineer." |
| **Old Faithful**, the Lanternfish coffee machine | Ch 10: breaks on Dev's first day; responses reveal people · Ch 12: Dev files the ticket nobody files · Ch 14: the chat channel and its jokes · Ch 16: the coffee committee as office politics · Ch 17: Dev stops being its unpaid mechanic |
| **Dev's name** | At most once per part: "Dev, as in developer?" "Not yet." / "Now, yes." |

### Narrative arc and timeline

- **Part I** covers about four months: Dev decides to search (Ch 2), learns the funnel (Ch 3), builds her evidence (Ch 4, 5), gets a referral (Ch 6), interviews (Ch 7, 8), negotiates and resigns (Ch 9). Bea runs a parallel, slower search.
- **Part II** covers about fourteen months at Lanternfish: first day (Ch 10), first quarter (Ch 11), a missed estimate (Ch 12), learning to write and give feedback (Ch 13), finding her register (Ch 14), friendship with Kai and Kai's promotion (Ch 15), a credit dispute and Rex's arrival (Ch 16), her first review and an outside offer (Ch 17).
- **Epilogue**: a year on, Dev refers Bea.

Each chapter opens with a scene that puts its problem in front of a character before the prose explains it, and ends with Dev one step further on.

---

## 6. Voice and tone

**The voice is a smart, kind colleague who has read the research and done the job**, talking to you over coffee. Second person, active voice, short sentences mixed with longer ones, British-leaning spelling (as in the front matter and Chapter 1: *organisation*, *colour*, *programme*), with *résumé* for the document and *CV* where a region uses it.

| Do | Don't |
| --- | --- |
| "Hiring is a bet placed with very little evidence. Here is how good the bets are." | "Studies have shown that it is important to consider that hiring may be imperfect." |
| "Structured interviews correlate about .42 with later performance [@sackett2022]." | "Interviews are basically useless." / "Research proves interviews work." |
| "This is craft advice: experienced managers do it; nobody has tested it. [!craft]" | Presenting a practitioner tip as a finding. |
| "Bea is very good at the job and not very good at the fragments hiring sees." | "Bea needs to step up her game!" |
| "You may disagree; here is our argument. [!view]" | "Obviously, everyone knows that..." |
| Name the uncomfortable thing ("the funnel is not neutral") and source it. | Pretend the game is fair, or tell the reader it is all rigged and nothing helps. |
| "If you remember one thing from this section..." | "In this section we will discuss..." |

**Rules of thumb.**

- Lead with the reason to care, then the idea, then the evidence, then what to do.
- One idea per section. If a section has two ideas, it is two sections.
- Numbers are concrete: "6.1% of applicants but 29.1% of hires", not "far more likely".
- Never condescend. The reader is an adult with a real problem, possibly a painful one (a layoff, a hostile colleague). Write as if they are smart and tired.
- No corporate jargon unless you are making fun of it, and then only once.
- People-first, plain language about identity; use the pronouns given in §5; for real people whose pronouns are unknown, use their name or "they".

### Rules for humour

1. **A joke must carry the point** or make it easier to remember. If deleting it loses nothing, delete it. The research on "seductive details" says decorative fun costs a little learning (`cheng2026`; see `research/style/README.md`).
2. **Punch at situations, institutions, the book itself, or Rex's headline.** Never at the reader, never at a group of people, never at someone's accent, body, background or identity.
3. **Specific beats wacky.** "A CEO who used to be in a band" is funnier than "a CEO who is a wizard", because it is the kind of thing that happens.
4. **No more than one laugh line every few paragraphs** in serious sections (layoffs, discrimination, harassment, burnout). Some sections should have none.
5. **Running jokes advance.** Each beat adds something (§5); never repeat a beat.
6. **Characters can be funny; evidence cannot.** Do not make jokes inside a Myth Check verdict or a Receipts box, except in the title.

---

## 7. Element catalogue

The syntax for each element is in `WRITING-GUIDE.md`; `book/front/how-to-use.md` shows a live sample of each.

| Element | Syntax | Use it for | Rules |
| --- | --- | --- | --- |
| **Scene** | `::: scene {slug="INT. PLACE — TIME"}` with `@dev:` lines | Putting the chapter's problem in front of a character | Open every chapter with one; 2 to 4 per chapter. Scenes show; prose explains. |
| **Pause** | `::: pause` | A question to commit to before the answer arrives | 1 to 2 per chapter; the chapter must answer it later. |
| **Your Move** | `:::: move {#chNN.move.slug} Title` with an inner `::: answer` | Exercises that make the reader retrieve, sort, apply or draft | 2 to 4 per chapter, numbered automatically. Answers explain why, not just what. |
| **Ask Anyway** | `::: ask` with `Q:` and `A:` paragraphs | The questions readers hold back, including sceptical ones | 1 per chapter, 2 to 4 questions. |
| **Two Chairs** | `::: chairs {left="The X" right="The Y"}` with `@left:` / `@right:` | Two ideas arguing, to show both sides | At most 1 per chapter; both chairs must score points. |
| **Trapdoor** | `::: trapdoor` | A common, costly mistake | 0 to 2 per chapter; say what it costs and what to do instead. |
| **Myth Check** | `::: myth {#chNN.myth.slug verdict=busted\|partly\|holds grade=strong\|moderate\|weak} The myth` | A popular claim, with a verdict and the grade of the evidence behind the verdict | Every myth assigned to the chapter in §4; cite the sources that test it. |
| **Receipts** | `::: receipts {source=key} Title` | Opening up one important study: what they did, found, and cannot tell you | 0 to 2 per chapter, for the evidence the chapter leans on hardest. |
| **Field Note** | `::: field {regions="US, UK, India"} Title` | Where practice differs by region | Name only regions you verified; say what is missing. |
| **Craft Note** | `::: craft` | Practitioner experience that no study has tested | Label honestly; keep it practical. |
| **Author's View** | `::: craft {by=author} Title` | Our argument, clearly marked as opinion | At most 1 per chapter. |
| **Flashback / Coming Soon** | `::: flashback {ref=ch03}` / `::: coming {ref=ch10}` | Making a backward or forward thread visible | 1 to 3 per chapter; one or two sentences each. |
| **Rewind** | `::: rewind` | The chapter's points worth keeping | Exactly one, at the end; 5 to 8 bullets; no new information. |
| **Figure** | `::: figure {#chNN.fig.slug src="chNN/name.svg"}` with an `Alt:` paragraph and a caption | A picture that explains one idea | 3 to 5 per chapter (§8). |

Inline labels: `[!craft]`, `[!view]`, `[!unverified]`. Citations: `[@key]`, `[@key, p. 12]`, `[@a; @b]`, and `[@key!]` to show the grade inline.

**Density.** On average no more than one box per 400 words, never two boxes back to back without prose between them (a Coming Soon directly after a Rewind is the exception), and the main thread of the chapter must make sense if every box is skipped. Digressions go in boxes, which keeps them labelled as separate from the argument.

---

## 8. Visual language

### Style

Friendly, hand-drawn cartoons and diagrams: round line caps, slightly wobbly lines, flat fills, a handwritten face (*Caveat*) for labels, and an uppercase grotesque (*Bricolage Grotesque*) for headings inside figures. Two accent colours carry meaning everywhere: **coral** for the snapshot game and Part I, **teal** for the long game and Part II; gold marks goals and highlights; plum marks evidence and myths. No photographs, no stock art, no raster images, no imitation of any other book's look.

### SVG conventions

- **One file per figure**, standalone, under `book/figures/<page-id>/<name>.svg`.
- **Root:** `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 W H" class="fig">`, no width or height. W is 560 to 680 for normal figures. A figure is drawn at the column's width, so on a phone (about 340 px wide) it shrinks to roughly half size: labels that carry meaning use `t` (24 units, about 12 px on a phone); `t-sm` (20) is for secondary notes only; `t-sans` (17) is for short uppercase headings. Nothing smaller. Every figure also gets an "Open full size" link for zooming.
- **Colours only through classes** from `book/figures/figure.css`, which the build copies into every figure (`python3 tools/build.py --sync-figure-style`). The classes read CSS custom properties, so every figure follows the light and dark themes. Hard-coded colours (`fill="#..."`) fail the build.
- **Stroke weights:** `k` 2.5 (default outline), `k-thin` 1.5 (details), `k-thick` 4 (emphasis and paths); `k-dash` for paths not yet taken; `k-a1`/`k-a2`/... recolour a stroke.
- **Fills:** `f-paper`, `f-soft`, `f-a1`..`f-a4` (soft tints), `f-a1s`..`f-a4s` (strong), `f-ink`, `f-mute`; skin `f-skin1`..`f-skin4`; hair `f-hair1`..`f-hair4`; cast signatures `f-dev`, `f-bea`, `f-rex`, `f-meera`, `f-tomas`, `f-kai`.
- **Text:** `t` (handwritten, 24), `t-sm` (20), `t-lg` (30), `t-xl` (40), `t-sans` (17, uppercase label), `t-mid`/`t-end` alignment, `t-mute`, `t-a1`/`t-a2`/`t-a4` colour, `t-bold`.
- **Hand-drawn feel:** straight lines become gentle quadratic curves with a small random offset; arrows have open, hand-drawn heads. `tools/figkit.py` (`Pen`) does this deterministically, so regenerating a figure gives the same file.
- **Allowed:** `<g>`, shapes, paths, `<text>`, `<defs>`, `<clipPath>`, `<title>`. **Forbidden** (the build fails): `<script>`, `<image>`, `<foreignObject>`, links, external references, inline font families, colour literals.
- **Ids:** any id inside a figure is fine; the build prefixes it with the figure id when inlining, so figures cannot collide.

### Characters

The cast is defined once in `tools/figkit.py` (`CAST`), drawn as **avatars** (`book/figures/cast/<key>.svg`, used beside speech), **heads**, and **full figures** (`figkit.person`). The model sheet is `book/figures/cast/model-sheet.svg` (Figure B.1). Each character keeps their signature detail in every drawing: Dev's teal clip and mustard hoodie, Bea's headphones and glasses, Rex's red blazer and grin, Meera's grey bun and mug, Tomás's beard and plaid, Kai's lavender hair and hoop. Draw them with `figkit` rather than by hand so they stay on model.

### Numbering, captions and alt text

- Figures number themselves per page: Figure 1.3 in Chapter 1, A.1 in the front matter, E.1 in the epilogue. Never type a figure number; cross-reference by id: `[[ch01.fig.loop]]` renders "Figure 1.3".
- **Caption:** one or two sentences saying what to notice and why it matters. A caption is not the alt text.
- **Alt text** (an `Alt:` paragraph inside the figure block, at least 25 characters; the build checks): describe what the figure *shows and says*, in reading order, including every label that carries meaning. A reader who cannot see the figure must get the same idea from the alt text.
- Simulated or illustrative data must say so in the caption and in the figure itself.

---

## 9. Claim policy

1. **Every factual claim cites a source**, inline, with `[@key]`. Statistics, research findings, laws, dates, quotes and historical facts are all factual claims.
2. **Every source is one a person on this project opened** during this work, recorded with its URL, the date opened (`url_checked` or `accessed`) and a note of what was read (abstract, full text, a secondary copy). A writer who cites a key from a research registry must read the topic file's caveats and, for any number they print, check that the registry's `supports` field states it.
3. **Every source is graded**: `strong`, `moderate`, `weak` or `myth-or-unsupported` (definitions in the research READMEs and on the site's References page). The grade is what the source can support *as used here*.
4. **The grade is visible where it matters**: in every reference list (automatic), in every Myth Check (the verdict's evidence grade) and Receipts box, and inline with `[@key!]` when a sentence leans on weak evidence.
5. **Opinion and craft are labelled**: `[!craft]` or a Craft Note for practitioner advice; `[!view]` or an Author's View for our arguments. Characters' lines are story, not evidence.
6. **Unverifiable claims are cut.** If something matters but cannot be verified, it may appear only marked `[!unverified]`, with a reason. Prefer cutting.
7. **Never invent** a study, statistic, quote, author, date or URL. Never round a number into a different claim. Never cite a retracted paper as evidence (the build refuses).
8. **Quotes are short, attributed and necessary.** No copied images, ever.
9. **Myths** get a Myth Check with a verdict (*Busted*, *Partly true*, *Holds up*), the grade of the evidence behind the verdict, and the sources that test the claim. A myth's origin may be cited with its `myth-or-unsupported` grade showing.
10. **Commercial and self-interested sources** carry their flags into the reference list automatically; say so in the text when you lean on one.

---

## 10. Length targets

| Part | Target | Range |
| --- | --- | --- |
| Front matter (2 pages) | 2,300 words | done |
| Chapter 1 | 5,500 words | done (about 5,400 words of prose, plus alt text) |
| Chapters 2 to 17 | 5,000 words each | 4,500 to 6,000 |
| Epilogue | 1,200 words | 800 to 1,500 |
| **Whole book** | **about 90,000 words** | 85,000 to 100,000 |

Plus 3 to 5 figures and 2 to 4 exercises per chapter.

**Why.** At around 200 words a minute, a 5,000-word chapter is a 25-minute sitting, under the 35-minute point where a conversational style stops helping on its own (`ginns2013`); the boxes and exercises break it into segments of five to ten minutes. Seventeen chapters is what the agreed scope needs without cramming: eight on getting a job, eight on conduct at work and one to frame both, each with room for a story, the evidence and practice. About 90,000 words is a normal length for a substantial non-fiction book: long enough to be complete, short enough to finish.

---

## 11. Writer assignments

Four balanced, self-contained assignments, two per part. Each writer owns their chapter files, figures and source files outright (§ ownership in `WRITING-GUIDE.md`), and reads this whole document, the Chapter 1 exemplar and the relevant research topic files before starting.

| Assignment | Chapters | Words | Research files to read first |
| --- | --- | --- | --- |
| **A: Part I, deciding and preparing** | Ch 2 *Stay, Go, or Grow?*; Ch 3 *The View from the Other Side of the Table*; Ch 4 *Know What You're Selling*; Ch 5 *Paper You* | about 20,000 | `research/part1/switching.md`, `channels.md`, `hiring-funnel.md`, `selection-methods.md`, `positioning.md`, `regional.md`, `myths.md`; `research/part2/leaving.md` |
| **B: Part I, the encounter and the exit** | Ch 6 *People, Not Portals*; Ch 7 *Interviews, Decoded*; Ch 8 *Show, Don't Tell*; Ch 9 *Offers, Negotiation, and the Exit* | about 20,000 | `research/part1/referrals.md`, `networking.md`, `channels.md`, `interviewing.md`, `selection-methods.md`, `offers-negotiation.md`, `switching.md`, `regional.md`, `myths.md`; `research/part2/first-principles.md` (asking for help) |
| **C: Part II, foundations** | Ch 10 *First Principles: Trust Is the Whole Game*; Ch 11 *The First Ninety Days*; Ch 12 *Reliability, the Boring Superpower*; Ch 13 *Talking and Writing at Work* | about 20,000 | `research/part2/first-principles.md`, `authenticity.md`, `newcomers.md`, `mistakes.md`, `power.md` (managing up, saying no), `formality.md` (writing), `teams.md` (feedback, meetings), `myths.md` |
| **D: Part II, people and growth** | Ch 14 *The Professionalism Dial*; Ch 15 *Office Friendships*; Ch 16 *Conflict, Politics, and Difficult People*; Ch 17 *Growing Without Losing Yourself*; Epilogue | about 21,000 | `research/part2/formality.md`, `authenticity.md`, `culture.md`, `remote.md`, `relationships.md`, `power.md`, `teams.md`, `ethics.md`, `burnout.md`, `leaving.md`, `myths.md` |

Hand-offs between assignments are only through this document: the story beats in §4 and §5 fix what happens in each chapter, so writers do not need each other's drafts. If you need to change a beat another writer depends on, change it here first.

---

## 12. Status of the evidence

Both evidence bases (`research/part1/`, `research/part2/`) were merged before this table of contents was finalised, and the chapter briefs above are built from them. Known gaps that writers must respect rather than fill with guesses:

- **India**: no verified data on tenure, referral use or switching premia (`research/part1/regional.md`); India-specific equal-treatment law for private employers not verified. Field Notes on these topics must say so.
- **UK and EU**: no verified switcher/stayer wage data; the EU pay-transparency directive and UK Equality Act s.60 were read through secondary summaries.
- **Abstract-level verification** for many Part II sources: before printing an effect size, check that the registry's `supports` field states it, or read the paper.
- **Thin direct evidence** on formality calibration and on friends becoming managers (Ch 14, Ch 15): rely on craft and author's view, labelled.
