# How hiring works from the employer's side

Research notes for Part I. Keys refer to `sources.yaml`. Grades are defined in `README.md`.

## The one-paragraph version

From the inside, hiring is a funnel run by busy people with a quota. Industry data agrees on its shape, though not its exact numbers. Many people apply. A small share get a first conversation. About a third of finalists get an offer, and most offers are accepted. Gem's 2024 customer data says **0.4% of inbound applicants were hired**. The same data says **2.0% of candidates the employer went looking for** were hired. Small-business data from CareerPlug has **3% of applicants invited to interview** and **27% of interviews ending in a hire**. Software organises the pile. People, and the filters people configure, do the rejecting. The famous "6 seconds" resume screen comes from a vendor's study of 30 recruiters. That vendor was selling resume rewrites.

## 1. Funnel stages and conversion rates

### 1a. Gem 2025 Benchmarks (2024 data). Grade: moderate (vendor data)
- Source: `gem2025`. Stages: Application → Pre-onsite (recruiter screen, hiring-manager screen, technical assessment) → Onsite → Offer → Hire.
- Inbound applicants, 2024: **6%** reached pre-onsite. **20%** of those reached onsite. **35%** of onsites got offers. **0.4%** of inbound applicants were hired. In 2021 the first three rates were 11%, 29% and 48%.
- Application → hire across all candidates fell from **1.6% (2021) to 0.5% (2024)**. Gem's own reading is that a prospective applicant is "3× less likely" to be hired than three years earlier.
- Candidates the employer sourced (approached first) were hired at **2.0% vs 0.4%** for inbound applicants. That is 5× more likely, and it is selection: the recruiter already pre-vetted them.
- Offer acceptance rose from **81% (2021) to 84% (2024)**.
- Interviews per hire rose from **14 to 20**. Average time to hire rose from **33 to 41 days** (2021 to 2024).
- Caveat: Gem sells sourcing and CRM software, so "sourcing works" is its pitch. Its customer base skews to tech and enterprise. Use the shape, not the decimals.

### 1b. CareerPlug 2025 Recruiting Metrics (2024 data). Grade: moderate (vendor data, SMB and hourly skew)
- Source: `careerplug2025`. Covers 60,000+ small businesses and 10M+ applications.
- **180 applicants per hire**, up from 93 the year before. **3% of applicants invited to interview. 27% of interviews became hires.** Job-view-to-application rate was 4.7%.
- Caveat: these are mostly hourly and frontline roles, not professional ones.

### 1c. Peer-reviewed single-firm data. Grade: strong
- Source: `brown2016`. In one large US corporation with 62,127 applicants, each channel's share grows or shrinks as candidates move through the stages. Details are in `referrals.md`.

### 1d. Myth: "every corporate job gets 250 resumes". Grade: weak / unsupported as a precise figure
- Source: `sullivan2013`. The figure comes from Dr John Sullivan's ERE article of 20 May 2013. It is hedged in the original: "Although it varies with the company and the job, on average 250 resumes are received…". The article gives no traceable method. Later blogs misattribute it to Glassdoor. Current vendor data (1a, 1b) shows applicant counts vary from dozens to thousands by role and market.
- For the book, say "often hundreds, sometimes thousands; it depends on role, location and remote eligibility". Don't print a single number.

## 2. Recruiter vs hiring manager. Grade: moderate (practitioner consensus)
- Practitioner sources agree on the split. The **hiring manager** owns the need, the decision and usually the offer shape. The **recruiter** (internal talent acquisition, or an external agency) runs the process. That means sourcing, first screens, scheduling, candidate communication and offer logistics.
- `shrm2015-recruiters`: a SHRM conference write-up (28 April 2015) quoting recruiting consultant Gerry Eskenazi: "at the end of the day, [hiring] decisions are not ours. We're the project manager." It recommends a "hiring manager intake meeting" with a checklist and written service-level agreements.
- This is practitioner opinion, not research, but it is uncontroversial. Implication for candidates: the recruiter is your guide and advocate inside the process, not the decider. Questions about team, work and growth belong with the hiring manager. Questions about process, timing and comp ranges usually go to the recruiter.

## 3. What applicant tracking systems (ATS) actually do

### 3a. The "75% of resumes are rejected by ATS / never seen by a human" claim. Grade: myth-or-unsupported
- Origin: secondary sources consistently say it began as a 2012 sales claim by Preptel, a resume-optimisation company that closed in 2013. No study, sample or method was ever published (`interviewguys-ats-myth`). HR consultant Christine Assaf investigated and found no supporting research. This is reported in `hiringthing-ats-myth`, an ATS vendor's blog, so it is not neutral.
- The original Preptel material was **not located**. Treat the origin story as well-corroborated but secondary.

### 3b. What employers configure. Grade: moderate (large survey, but self-report)
- Source: `hiddenworkers2021`. A Harvard Business School and Accenture report surveying 2,275 executives and 8,720 "hidden workers" in the US, UK and Germany.
  - More than 90% of employers use their recruiting management system to "initially filter or rank" candidates: 94% for middle-skills roles, 92% for high-skills.
  - **88%** of employers agreed qualified high-skills candidates are "vetted out of the process because they do not match the exact criteria established by the job description". The figure is 94% for middle-skills.
  - **48%** filtered middle-skills candidates on employment gaps longer than six months.
- So filtering is real, but **people set the knockout rules**. Typical rules are degree requirements, exact credential names and gaps. The software does not reject anyone autonomously.

### 3c. Small recruiter sample on auto-reject settings. Grade: weak
- Source: `enhancv2025-ats`. 23 of 25 US recruiters said their systems do not auto-reject for formatting. 2 of 25 used match-score thresholds or auto-rejection on missing skills. All used knockout questions on work authorisation, licences or location. This comes from a resume-tool vendor with a tiny convenience sample, so it is corroboration only.

### 3d. Practical upshot (author view, labelled)
- *Author view:* the real risks are knockout questions you answered "wrong", and a human doing a seconds-long skim. Format matters because humans skim, and because some parsers mangle columns and tables. See `positioning.md`. Mirroring the job's own words for skills you genuinely have helps both recruiter keyword searches and the human skim.

## 4. How long resume screens really take

### 4a. TheLadders 2012 eye-tracking study: "6 seconds". Grade: weak
- Source: `ladders2012`, from an archived copy of the original PDF. It ran with **thirty professional recruiters over 10 weeks**. It reported recruiters spent "about 6 seconds on their initial 'fit/no fit' decision". It also reported that almost 80% of review time went on name, current and previous titles and companies, start and end dates, and education.
- **Who ran it:** TheLadders, a job site, under its head of UX design (Will Evans). The same document compares TheLadders' own profiles favourably with LinkedIn's. It ends: "Turn to a professional for resume rewrites" and links to TheLadders' resume-rewriting service. It was never peer-reviewed.

### 4b. TheLadders 2018 update: "7.4 seconds". Grade: weak
- Source: `ladders2018`, archived original PDF. "The average initial screen clocking in at just 7.4 seconds in 2018." It was a two-stage study: a timed stage where recruiters didn't know they were being timed, then lab eye-tracking. **No sample size is given in the report.** It recommends clear layouts with bold titles and section headers. It warns against multiple columns, clutter and keyword stuffing.

### 4c. Interpretation. Grade: moderate (consistent with mechanism)
- The number measures the first keep-or-skip glance, not the full evaluation of a shortlisted resume. It fits the funnel data (1a, 1b): when hundreds apply, the first pass has to be fast.
- *Author view:* the robust lesson isn't "6 seconds". It is that **titles, employers, dates and the top third of page one** do most of the work in the first pass. Design for a skim, then reward a read.

## Sources in this file
`gem2025`, `careerplug2025`, `brown2016`, `sullivan2013`, `shrm2015-recruiters`, `interviewguys-ats-myth`, `hiringthing-ats-myth`, `hiddenworkers2021`, `enhancv2025-ats`, `ladders2012`, `ladders2018`.
