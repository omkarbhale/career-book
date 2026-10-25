# Positioning: resumes, cover letters, keywords, LinkedIn, portfolios and GitHub

Research notes for Part I. Keys refer to `sources.yaml`. Grades are defined in `README.md`.

## The one-paragraph version

Peer-reviewed evidence on *how to write* a resume is thin. Most popular "data" on it comes from resume-writing companies. What is solid:
- Recruiters skim first and read second (`hiring-funnel.md`).
- Spelling errors cost interviews, with a measured 7–18 percentage-point penalty in a recruiter experiment.
- Who you appear to be, through your name, race or age, changes callbacks in large audit studies. That is not your fault and not fully in your control, but it is part of the honest picture.
- On GitHub, hiring developers read activity as evidence that's hard to fake, but that rests on one small interview study.
- Cover letters: commercial studies say tailored ones help, and hiring-manager surveys disagree with each other.
- "LinkedIn photos get 21× more views" is LinkedIn's own unsourced marketing figure.

## Findings

### 1. Spelling errors carry a real penalty. Grade: strong
- Source: `sterkens2023` (*PLOS ONE*), a scenario experiment with **445 recruiters**. Compared with error-free resumes:
  - error-laden resumes cut interview probability by **18.5 percentage points**;
  - resumes with fewer errors cut it by **7.3 points**.
- About half the penalty is explained by recruiters inferring lower interpersonal skills (9.0%), conscientiousness (12.1%) and mental ability (32.2%).
- Caveat: a vignette experiment, not real hiring. It does cover lower-skilled jobs and resumes with just a few errors, extending earlier work.

### 2. What the first skim looks at. Grade: weak (commercial), but consistent
- From `ladders2012` and `ladders2018`. Job titles, employers, dates and education draw most of the first glance. Clean single-column layouts with clear headers do best. Clutter, multiple columns and keyword stuffing do worst.
- *Author view:* the top third of page one carries the most weight. Put your most relevant title and achievement there.

### 3. Resume length. Grade: weak
- Source: `resumego2018-length`. A simulated hiring exercise run by a resume-writing service in 2018 with **482 recruiters and hiring managers**. Of 7,712 resumes chosen, 5,375 were two pages. They report recruiters were "2.3 times as likely to prefer two-page resumes", and 1.4× for entry-level.
- Caveat: commercial, not peer-reviewed. Participants knew it was a simulation. "Chosen" isn't the same as hired.
- *Author view:* length should follow content. One page for early career is a sensible default; two pages for substantial experience is fine. Where norms differ by country, see `regional.md`. A US resume, a UK CV and an Indian "biodata" are different documents.

### 4. Keywords: real but misunderstood. Grade: moderate
- Recruiters search their ATS for terms, and employers configure filters on exact credentials and skills (`hiddenworkers2021`: 88% of employers agree qualified candidates are filtered out for not matching exact job-description criteria).
- `ladders2018` warns that keyword stuffing does badly with the human reader.
- *Author view:* use the posting's own words for skills you genuinely have (for example "PostgreSQL" rather than "relational databases" if that's what they wrote), and put them in context. Never use white-text or hidden-keyword tricks. Practitioners widely report that recruiters spot them; that is not measured here.

### 5. Cover letters: weak and conflicting evidence. Grade: weak
- `resumego2020-cover`: a commercial field experiment from 15 July 2019 to 10 January 2020. **7,287 fictitious applications** to real job-board postings, in three groups: no cover letter, generic, tailored. The company reports tailored letters got a **"53% higher callback rate"** than no letter. In its survey of 236 hiring professionals, 87% said they read cover letters. Its results table is an image, so the per-group callback rates were not verifiable from the text. Run by a resume-writing service.
- `aacsb2020-twimc`: summarises a Resume Companion survey (another resume-services company) of 1,000+ US hiring managers. **83%** said "To Whom It May Concern" would have little or no impact on whether they'd interview you.
- *Author view, labelled:* when an application has a field for one, a short letter tailored to the role likely helps a little and costs little. Never send a generic one. The best "cover letter" is often a referral message (`referrals.md`).

### 6. Who you appear to be changes callbacks (audit studies). Grade: strong
- `bertrand2004`: fictitious resumes to help-wanted ads in Boston and Chicago. **White-sounding names received 50% more callbacks** than African-American-sounding names with the same resume.
- `quillian2017` (*PNAS* meta-analysis of every available US field experiment; 55,842 applications, 26,326 positions). Since 1989, white applicants received on average **36% more callbacks than equally qualified African Americans** and 24% more than Latinos. They found **no change** over 25 years for African Americans, and modest evidence of decline for Latinos.
- `kline2022` (QJE; earlier as IZA DP 14634): **83,000+ fictitious applications** to 108 of the largest US employers. Distinctively Black names reduced contact by **2.1 percentage points**, about 9% of the Black mean contact rate. Discrimination was concentrated in some firms: the top quintile accounted for nearly half of lost contacts. The average gender gap was insignificant but varied by firm.
- India: `thorat2009` (Thorat, Attewell & Rizvi, Indian Institute of Dalit Studies working paper; a correspondence study of graduate applicants to the urban private sector, including multinationals and prominent Indian firms). As summarised by GSDRC, the odds of a Dalit applicant being invited to interview were about **two-thirds**, and of a Muslim applicant about **one-third**, of the odds for an equally qualified high-caste Hindu applicant. Grade **moderate**: only the GSDRC summary was opened. A version also appears as a chapter in *Blocked by Caste* (2010), which was not opened.
- For the book: name these effects honestly. What a reader can control is the channel. Referrals and direct contact reduce reliance on a cold name-screen. *Author view.*

### 7. GitHub and portfolios for tech roles. Grade: weak-to-moderate (qualitative)
- `marlow2013` (CSCW 2013, Carnegie Mellon). Interviews with **seven employers** who used GitHub to evaluate candidates and **six job seekers**, drawn from a survey of 128 respondents. Employers read profile cues as evidence of technical skill, motivation and values. They trusted those cues *more than resumes* because work on GitHub is visible and behaviour traces are hard to fake.
- Caveat: small, early, self-selected sample from 2013. Many working engineers have little public code because their work is proprietary. *Author view:* a portfolio helps most where you lack conventional signals, as a career-changer, new graduate or self-taught developer. Its absence is rarely a dealbreaker for experienced hires.

### 8. LinkedIn. Grade: weak
- "Profiles with a photo get up to 21x more profile views… 36x more messages", attributed to LinkedIn (`sej-linkedin-photo`). No primary LinkedIn document, dataset or method was found. Treat it as platform marketing (myth-or-unsupported as a precise figure).
- Real mechanism (moderate): recruiters source candidates, and sourced candidates are hired at about 5× the inbound rate (`gem2025`). Being findable, with a clear headline, current title and skills, is a channel.
- Reminder from `rajkumar2022`: LinkedIn connections to moderately weak ties have causal effects on job mobility. That makes LinkedIn a networking tool more than a resume host.

### 9. Gendered application behaviour: "women apply only at 100%". Grade: myth-or-unsupported as stated
- `mohr2014` (*Harvard Business Review*) popularised the line "Men apply for a job when they meet only 60% of the qualifications, but women apply only if they meet 100% of them". The source cited was a Hewlett-Packard internal report that has never been published.
- `salwender2024` (*European Journal of Social Psychology*, four studies): Study 1 found "no gender difference… neither at 60% nor at 100% qualification fit". Later studies found "a significant, but not robust gender difference". Women robustly reported a higher desire to be prepared.
- For the book: apply when you meet the core of a role. The 60/100 split is folklore. *Author view, informed by the replication.*

## Sources in this file
`sterkens2023`, `ladders2012`, `ladders2018`, `resumego2018-length`, `hiddenworkers2021`, `resumego2020-cover`, `aacsb2020-twimc`, `bertrand2004`, `quillian2017`, `kline2022`, `thorat2009`, `marlow2013`, `sej-linkedin-photo`, `gem2025`, `rajkumar2022`, `mohr2014`, `salwender2024`.
