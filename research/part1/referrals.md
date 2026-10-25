# Referrals: interview rates, hire rates and outcomes

Research notes for Part I. Keys refer to `sources.yaml`. Grades are defined in `README.md`.

## The one-paragraph version

Referrals are the most over-performing channel in hiring, and that holds across peer-reviewed firm data and vendor data alike. Referred candidates are a small slice of applicants but a large slice of hires. In one large US corporation, they were **6% of applicants and 29% of hires**. In Gem's 2024 data, **1.6% of applications and 17% of hires**. In CareerPlug's small-business data, **2% of applicants and 11% of hires**. Firms benefit too. Referred workers quit less, and in some industries they do better on rare, high-stakes measures. The benefit is mostly *better matching*, not referred people being better in general. It comes with a fairness cost: people refer people like themselves.

## Findings

### 1. Referred candidates are far more likely to advance at each stage. Grade: strong
- Source: `brown2016` (Table 3, one large US corporation, 62,127 applicants). Shares of each stage by channel:

| Channel | Applicants | Interviewed | Offered | Hired |
|---|---|---|---|---|
| Internet job board | 60.1% | 40.0% | 23.6% | 23.5% |
| Firm website | 14.8% | 10.1% | 9.6% | 10.6% |
| Own initiative | 10.1% | 7.7% | 7.0% | 5.6% |
| **Referred by current employee** | **6.1%** | **21.4%** | **27.3%** | **29.1%** |
| Campus recruitment | 2.1% | 6.9% | 11.2% | 7.6% |

- Their linear probability model (Table 4) finds a referral raises the interview probability by 7.3 percentage points and the offer probability by 2.4 points, with controls.
- Earlier single-firm studies find the same. In Fernandez & Weinberg (1997), referred applicants at a retail bank had advantages at the interview and offer stages. That was not explained by better resumes or timing (`fernandez1997`, working-paper abstract).

### 2. The same pattern shows up in vendor data. Grade: moderate (corroboration)
- `gem2025`: referrals were 1.64% of applications and 17.09% of hires. Internal candidates were 0.27% and 12.56%.
- `careerplug2025`: referrals were 2% of applicants and 11.3% of hires.
- Treat these as corroboration of the direction. The magnitudes depend on each vendor's customers and tagging.

### 3. Outcomes after hire: lower quits, a starting-pay edge that fades. Grade: strong
- `brown2016`: referred hires start with a wage advantage that "dissipates by the third year". From year five the relationship reverses. Referred workers have "substantially less turnover". Promotion rates were the same on average.
- `burks2015` (nine large firms; call centres, trucking, high-tech): referred workers were **10–30% less likely to quit**. They did substantially better on rare "high-impact metrics" (patents, avoiding truck accidents). They were similar on ordinary productivity metrics. Referrals generated higher profit per worker, driven by lower turnover and recruiting costs.
- `pallais2016` (three field experiments on oDesk): referrals carry information about performance and persistence that a worker's observable traits don't. Referred workers did especially well when working directly with their referrer. There was no evidence they worked harder to protect the referrer's reputation.

### 4. Why it works: matching information, not magic. Grade: strong
- `burks2015` ran four statistical tests. All indicate firms gain mainly because referrals select workers who **fit the job better**. The tests rule out referrals selecting higher overall quality, monitoring or coaching, and enjoying working with friends.
- Workers refer people like themselves "not only in characteristics but in behavior (e.g. unsafe workers refer other unsafe workers)" (`burks2015`).
- *Author view:* for a candidate, a referral is valuable because it carries trusted information. So a weak referral ("I don't really know them, but sure") carries less. The best referral is from someone who has seen your work.

### 5. Business contacts vs friends and family. Grade: strong
- `lester2021` (NY Fed Survey of Consumer Expectations, 2013–2018): referrals from **business contacts** are used more for high-skill jobs. They come with higher starting wages but shorter tenures, because those workers keep meeting other firms. Referrals from **family and friends** are used more for low-skill jobs. They come with lower starting wages and less turnover. They are relied on by people who struggle to get offers through other channels.
- This connects to `networking.md`: what helps is *professional* weak and medium ties.

### 6. The fairness problem. Grade: moderate (mixed evidence)
- `fernandez2019` (two firms' administrative data): with gender homophily, referral hiring "can disadvantage women when an old boys' network is in place". The disadvantage is larger at higher levels. Yet overall it "is a desegregating force… It promotes women's representation strongly at all levels, but less so at higher levels."
- `burks2015`: workers refer people like themselves.
- *Author view:* referral-heavy hiring rewards people who already have networks. The book should be honest about this and give readers without networks a plan for building weak ties (see `networking.md`). It should not pretend that a meritocratic cold-application route is equivalent.

## Practical implications to carry into the chapter (author view, labelled)
- Asking for a referral is normal. Many employers run formal referral programmes (`brown2016` studies one); that is practitioner knowledge, not a measured prevalence here.
- Make referring you easy. Send a short note with the job link, a two-line pitch and your resume. The referrer's credibility is on the line, so give them true, specific things to say.
- A referral gets you looked at. It does not get you hired: offer-stage shares in the `brown2016` table converge.

## Sources in this file
`brown2016`, `fernandez1997`, `gem2025`, `careerplug2025`, `burks2015`, `pallais2016`, `lester2021`, `fernandez2019`.
