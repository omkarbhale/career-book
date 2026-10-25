# Switching: when and why, tenure and "job hopping", resigning, notice, non-competes, layoffs, searching while employed

Research notes for Part I. Keys refer to `sources.yaml`. Grades are defined in `README.md`.

## The one-paragraph version

In US data, switching jobs usually pays more than staying, but the premium is smaller and more cyclical than the internet says. In the Atlanta Fed series, job switchers' median wage growth beat stayers' in about **91% of months since 1997**, by **0.7 percentage points** on average. The gap peaked at **2.2 points in November 2022** and almost vanished in 2025. Too many moves carry a signal cost: in a field experiment, resumes showing fewer job changes got 40–50% more callbacks. Search from a job if you can. Employed searchers get more offers per application and higher offers. Callbacks fall sharply over the first eight months of unemployment, and past unemployment that has been followed by work seems not to matter. Notice and non-compete rules differ sharply by country (US, UK, Germany, India). In India, post-employment non-competes are generally void.

## Findings

### 1. The job-switcher premium (US). Grade: strong (official data; descriptive)
- Source: `atlantafed-wgt`, the Wage Growth Tracker data file downloaded 25 October 2026. "Job Switcher" sheet: 12-month moving averages of median wage growth, Jan 1997 – Sep 2026, 356 monthly observations. The calculations below are the researcher's own, from that file:
  - Switchers' wage growth exceeded stayers' in **91.3%** of months. The mean gap was **0.73 percentage points**.
  - The largest gap was **Nov 2022: switchers 7.7% vs stayers 5.5% (2.2 points)**, in the post-pandemic tight labour market.
  - The gap **reversed** in the Great Recession aftermath. The low point was Feb 2010, at switchers 2.0% vs stayers 2.6%.
  - Annual averages: 2022, 6.4 vs 4.8; 2023, 7.1 vs 5.5; 2024, 5.4 vs 4.9; **2025, 4.4 vs 4.3**; 2026 so far, 4.4 vs 3.7.
  - The latest release (Sep 2026, 3-month series, published 8 Oct 2026) puts switchers at 4.7% and stayers at 3.4%.
- Caveats from the methodology page: the measure is the *median of individual* wage changes. "Switcher" is broad: a different occupation or industry from a year ago, or a change of employer or duties in the past three months. People who move address drop out of the sample. These are not causal estimates, because people who switch differ from people who stay.
- For the book, the honest version is: "switching *tends* to pay more, especially when employers are short of people; in slack markets, the premium can disappear or reverse."

### 2. Internal moves vs external moves. Grade: moderate
- `bidwell2011`: external hires paid about 18–20% more than internal promotions into similar jobs, but rated lower for two years and more likely to exit. See `channels.md`.

### 3. Tenure norms (US). Grade: strong
- `bls-tenure2026`: median tenure with current employer was **4.1 years in January 2026**, up from 3.9 in January 2024. By age: **3.0 years for ages 25–34**, 9.6 for ages 55–64. Public sector 5.6 vs private 3.9.
- Implication: "job hopping" should be judged against the base rate. A two- or three-year stint for someone under 35 is close to the median.

### 4. Does "job hopping" hurt? Grade: strong (with scope limits)
- `cohn2021` (*Journal of the European Economic Association*; Cambridge repository abstract and Chicago Booth Review summary). It combines a lab experiment, a field experiment and an HR survey:
  - In the field, resumes listing fewer job changes got **40–50% more callbacks** than otherwise identical resumes with more changes.
  - The HR survey indicates recruiters read frequent changes as signalling poorer "work attitude", meaning reliability and cooperativeness. Those perceptions "largely account for the callback differences".
  - The authors caution that flux can also signal breadth and ambition.
- *Author view:* each move needs a story that makes sense: growth, scope, learning, a clear reason. Several sub-one-year stints in a row is where the signal turns negative.

### 5. Searching while employed vs unemployed. Grade: strong
- `faberman2017`: employed searchers receive more offers per application and higher-paid offers, even after controls. They are about three times more efficient per unit of effort.
- `kroft2013`: callbacks fall about 45% between one and eight months of unemployment, then flatten. The effect is stronger in tight markets.
- `eriksson2014` (*American Economic Review*; Swedish field experiment; IZA abstract opened). "No evidence that recruiting employers use information about **past** unemployment to sort workers, but some evidence that they use **contemporary** unemployment."
- `hiddenworkers2021`: 48% of employers filtered middle-skills candidates on gaps longer than six months.
- *Author view, synthesising:* if you can, start searching before you leave. If you're laid off, start immediately and treat the first months as the most valuable window. A gap followed by work is far less costly than a current long gap. Fill gaps with demonstrable activity (projects, contract work, study) and explain them plainly.

### 6. Resigning well. Grade: practitioner opinion, plus the UK legal points
- Legal (UK): give at least the contractual notice; the statutory minimum is one week after a month's service. "You may be in breach of your contract if you do not give enough notice". Resigning "in the 'heat of the moment'" can be retracted only if the employer agrees (`govuk-notice`).
- *Author view:* resign in person or on a call, then confirm in writing. Thank people; keep the reason short and true. Don't burn bridges: the people you leave become your weak ties (`networking.md`), and references and back-channel checks exist. Prepare for a counteroffer conversation (`offers-negotiation.md` §7). Hand over properly; it's the last impression you leave.

### 7. Notice periods by region
| Region | What the rule is | Grade / source |
|---|---|---|
| **US** | Employment is "at will" by default: "terminated either by employer or employee at any time and for almost any reason". Notice is customary (two weeks is the common norm; *practitioner, unverified*), not legally required unless a contract says so. Mass layoffs and plant closings at employers with 100+ employees require **60 days' written notice** under the WARN Act. | strong: `lii-atwill`, `warn-2102`, `warn-2101` |
| **UK (GB)** | Employee: at least **one week** after a month's service, or the longer contractual period. Employer, statutory minimum: one week (1 month–2 years' service), then one week per year of service, up to **12 weeks** after 12 years. Contracts usually specify longer (often a month or three; *practitioner, unverified*). Garden leave is allowed. | strong: `govuk-notice` |
| **EU example: Germany** | Basic notice is **four weeks** to the 15th or the end of a month. The employer's notice rises with service, from 1 month (2 years) to 7 months (20 years). During probation (max six months), notice is two weeks. | strong: `bgb622` |
| **India** | Set mainly by contract. Khaitan & Co reports non-managerial employees "usually serve a notice period of 1 to 2 months", and senior roles 3 to 6 months. Direct case law on long notice periods is limited. The four Labour Codes came into force on **21 November 2025**, consolidating 29 central laws. Commentary notes final dues must be paid within two days of resignation under the new framework. Notice "buyouts" and withheld relieving letters are common practitioner topics, not verified here. | moderate: `khaitan-notice`, `argus-labourcodes`, `barandbench-labourcodes` |

### 8. Non-competes and gardening leave
- **US federal:** the FTC's 2024 nationwide non-compete ban was vacated by a federal district court. The FTC moved to dismiss its appeal on 5 September 2025, and the Fifth Circuit dismissed it on **8 September 2025** (`uschamber-ryan`). The rule is not in force; **state law governs**.
- **California:** Business and Professions Code §16600 voids non-competes, with narrow exceptions. Since 1 January 2024, SB 699 and AB 1076 bar employers from entering into or attempting to enforce void non-competes, "regardless of where and when the contract was signed", and required notices to affected employees (`loeb2023-california`, law-firm alert).
- **UK:** non-competes ("restrictive covenants") can be enforced in court (`govuk-notice`). The previous government's 2023 plan to cap them at **three months** was not legislated. In November 2025 the government published a working paper reopening options, including a statutory length limit and a ban below a salary threshold (`cms2025-uk-noncompete`, law-firm update dated 28 Nov 2025). **No outcome was found as of this research.**
- **Gardening leave (UK):** an employer "may ask you not to come into work… during your notice period. This is called 'garden leave'" (`govuk-notice`).
- **India:** Indian Contract Act s.27 makes agreements in restraint of trade void. Courts treat restraints *during* employment as permissible. In *Percept D'Mark v Zaheer Khan*, the Supreme Court held that a restrictive covenant extending beyond the term of the contract is void (`barandbench-s27`, law-firm commentary). Non-solicitation and confidentiality clauses are analysed separately.

### 9. Layoffs
- **US:** 60-day WARN notice for covered plant closings and mass layoffs (`warn-2102`). A mass layoff at a single site generally means 50–499 employees *and* 33% of the workforce, or 500+ (`warn-2101`). Several states have their own "mini-WARN" laws; *not verified here*.
- **UK:** statutory redundancy notice follows the same minimum scale as dismissal notice, and pay in lieu of notice is possible if the contract allows (`govuk-notice`).
- *Author view:* a layoff is an event, not a verdict. The research suggests the employer side reads *current* long gaps, not layoffs per se. That matches `eriksson2014`: past unemployment didn't matter. Say "my role was eliminated in a reduction of N%" plainly, and move on to what you did.

## Sources in this file
`atlantafed-wgt`, `bidwell2011`, `bls-tenure2026`, `cohn2021`, `faberman2017`, `kroft2013`, `eriksson2014`, `hiddenworkers2021`, `govuk-notice`, `lii-atwill`, `warn-2101`, `warn-2102`, `bgb622`, `khaitan-notice`, `argus-labourcodes`, `barandbench-labourcodes`, `uschamber-ryan`, `loeb2023-california`, `cms2025-uk-noncompete`, `barandbench-s27`.
