# Offers: negotiation, pay transparency, equity, counteroffers, exploding offers, checks

Research notes for Part I. Keys refer to `sources.yaml`. Grades are defined in `README.md`.

## The one-paragraph version

First offers anchor outcomes. In the lab, whoever makes the first offer tends to do better, unless the other side deliberately focuses on their own alternatives and targets. Only about a third of US workers report bargaining over pay before accepting their job. In a survey of 149 employees, those who negotiated reported about $5,000 more per year. Gender differences in *asking* are real but conditional. When a job ad says pay is negotiable, the gap in who negotiates disappears. The backlash is also real: evaluators penalised women more than men for asking in experiments, and more-biased evaluators penalised Black negotiators. Pay-transparency laws are spreading: 13 US states plus DC as of May 2026, and an EU directive due June 2026, though most member states missed the deadline. These laws make ranges visible, and one study finds they compress wages by about 2%. The "80% of counteroffer-accepters leave within six months" figure has no traceable study. Exploding offers are a known market failure in labs and in some real markets.

## Findings

### 1. Anchoring: first offers. Grade: strong (lab)
- `galinsky2001` (*JPSP*, three experiments). "Whichever party, the buyer or seller, made the 1st offer obtained a better outcome", and first offers "were a strong predictor of final settlement prices". The advantage was **eliminated** when the receiving negotiator focused on the opponent's alternatives, the opponent's reservation price, or their own target. This held face-to-face and by email.
- *Author view, from this evidence:*
  - When you know the market range (now often posted, see §5), anchoring with a well-justified number at the high end is supported.
  - When the employer anchors first, the counter-move is to think explicitly about your target and your alternatives, which is exactly what removed the effect in the experiments.
  - Caveat: these are lab negotiations between students over business deals, not salary talks with a future boss. The relationship component matters more in a job negotiation (see §3).

### 2. Who negotiates, and what it's worth. Grade: moderate
- `hallkrueger2012` (*AEJ: Macroeconomics*, representative US survey). About a third of workers "bargained over pay before accepting their current jobs". About a third had precise pay information at first meeting (wage posting). About 40% "could have remained on their earlier jobs" when they accepted, a stronger bargaining position than unemployed seekers have. In the NBER working-paper version (w16033), "Wages are higher among bargainers than non-bargainers, after adjusting for the differing compositions of the groups."
- `marks2011` (*Journal of Organizational Behavior*; reported by strategy+business). A survey of 149 employees: those who negotiated rather than accepting the first offer "boosted their annual pay by an average of US$5,000". The most competitive negotiators gained most. Caveat: self-report, small sample, selection (people who negotiate may differ), and the article was read via secondary coverage only. Grade weak–moderate.

### 3. Gender: asking, and backlash. Grade: strong
- `leibbrandt2015` (*Management Science*; natural field experiment with 2,422 job seekers responding to real ads on 18 job boards in nine US cities; summarised by the Harvard Kennedy School Gender Action Portal):
  - Without a statement that pay was negotiable, men were more likely to negotiate than women.
  - **With an explicit "wage is negotiable" statement, the difference disappeared.** Women and men initiated at 21.2% and 21.4%.
  - Overall, negotiation initiation was 21% with the statement vs 7% without.
  - Adding "negotiable" cut the gender gap *in applications* by about 45%. Men were drawn to ads where negotiability was ambiguous.
- `bowles2007` (*OBHDP*, four experiments; summarised by the Gender Action Portal). Evaluators penalised female candidates more than male candidates for initiating salary negotiations. The negative effect on willingness to work with the candidate was "5.5 times greater if the candidate is female". In the video study, male evaluators penalised only women, while female evaluators penalised all negotiators. The authors' reading: women's reluctance can be a *rational* response to social costs.
- *Author view:* "just ask" is incomplete advice. What helps everyone is to:
  - ask about negotiability explicitly ("Is there flexibility on base?"), which removes the ambiguity that drives the gender gap;
  - justify asks with market data and role scope;
  - frame asks relationally ("I'm excited, and I want to make this work").
  These are practitioner tactics consistent with, but not directly tested by, the studies above.

### 4. Race and negotiation. Grade: strong
- `hernandez2019` (*JAP*, three studies). Evaluators higher in racial bias expected Black job seekers to negotiate less. When Black candidates did negotiate, they were awarded lower starting salaries. The mechanism appeared to be evaluators "more resistant to making concessions to Black than to White job seekers".
- For the book: be honest that negotiation advice is not identity-neutral. Posted ranges (§5) reduce the room for this bias, but only partly.

### 5. Pay-transparency laws. Grade: strong (law), moderate (effects)
- **US states** (`clockspot-paytransparency`, a vendor summary, cross-checked against official pages where opened): as of May 2026, **13 states plus DC** have effective pay-range posting laws: California, Colorado, Connecticut, DC, Hawaii, Illinois, Maryland, Massachusetts, Minnesota, New Jersey, New York, Rhode Island, Vermont and Washington. Later laws:
  - Virginia, from 1 July 2026, no employee threshold; it also bans salary-history inquiries.
  - Maine, from 29 July 2026, 10+ employees.
  - Delaware, from 26 September 2027, more than 25 employees.

  Those three are from `cooley2026` (law-firm alert). Official check: New York State Labor Law §194-b requires employers with **four or more employees** to list compensation ranges for advertised jobs, promotions and transfers (`nydol-paytransparency`). Many states with posting laws also ban salary-history questions (vendor summary, not individually verified).
- **EU** (`ec-paytransparency`, `lockton2026-eu`): Directive (EU) 2023/970 gives job seekers "a right to information on pay prior employment" and "a prohibition to ask salary history". Member states had to transpose it by **7 June 2026**. As of 23 September 2026, only a few had fully transposed: Greece, Italy, Lithuania, Malta and others per the Lockton table. Germany and France had not.
- **Effects** (`cullen2023`, *Econometrica*; NBER w28903 page opened): US state laws protecting coworkers' right to discuss pay led wages to "decline by approximately 2%". The effect is muted where workers have low individual bargaining power. The mechanism is that transparency reduces individual bargaining power. Caveat: this is about pay-*discussion* protections, not range-posting mandates; extrapolating to posting laws is an inference.
- *Author view:* in transparent jurisdictions, the posted range is your anchor information. Use the range plus your evidence to place yourself within it.

### 6. Equity and total compensation basics (tech). Grade: strong for the definitions, weak for "what's typical"
- **Tax treatment (US)**, from `irs-p525` (IRS Publication 525): it distinguishes **nonstatutory** (NSO) and **statutory** (incentive, ISO) stock options and sets out when income arises:
  - NSOs: income at grant only if the option has a readily determinable fair market value, which is rare for private companies; otherwise at exercise.
  - ISOs: special treatment, but they can trigger the alternative minimum tax.
  - Restricted property is taxed when it is no longer subject to a "substantial risk of forfeiture".
  Not tax advice. Readers outside the US need local rules; India and the UK differ and weren't verified here.
- **Vesting:** "The most common schedule is a four-year vesting plan with a one-year cliff… 25% of your options after the first year" (`secfi-vesting`, a vendor that sells equity financing). Prevalence is not independently verified.
- *Author view:* compare offers on **total compensation**, meaning base, bonus (expected, not maximum), equity (annualised, discounted for risk and illiquidity in private firms) and benefits, rather than on base alone. Ask for the equity terms in writing: number of units, strike price, vesting, refreshers, and the post-departure exercise window.

### 7. Counteroffers. Grade: myth-or-unsupported for the famous statistic
- "80% (or 90%) of people who accept a counteroffer leave within 6–12 months": no traceable study. Two commercial career sites (`interviewguys-counteroffer`, `4dayweek-counteroffer`) document the trail. The figure appears variously as 48%, 66%, 80%, 89%, 90% and 93%, and cited sources are untraceable. Both mention a CEB/Gartner figure of about 50% leaving within 12 months, "cited by Harvard Business Review". **That CEB source was not opened; treat it as unverified.**
- Note the interest: recruiters, who earn fees when you move, are the main propagators (`4dayweek-counteroffer` makes the same point).
- *Author view:* treat a counteroffer as a normal decision. Ask yourself why it took a resignation to get the raise, and whether the reasons you started looking are fixed by money.

### 8. Exploding offers. Grade: moderate (lab plus market observation)
- `niederle2009` (*AEJ: Microeconomics*): across about a dozen markets, those where deals happen far in advance tend to be ones where exploding offers are acceptable and reneging is not. In the lab, exploding offers plus binding acceptances produced **inefficient early contracting**. Relaxing either one made matching happen later, with better information and higher efficiency.
- *Author view:* it is normal to ask for more time. Name a specific date and reason ("I'm finishing another process and want to give you a firm yes by Friday"). An employer who won't allow a few days is telling you something about how decisions get made there.

### 9. Background and reference checks
- **US** (strong; regulator): `eeoc-ftc-background`. When an employer uses a background-reporting company, it "must ask for your written permission before getting the report". If it might reject you because of the report, it "must give you a copy of the report and a 'notice of rights'". It must treat applicants equally regardless of protected characteristics.
- **Ban-the-box** (strong): `agan2018` (QJE; Cato research brief by the authors opened). About 15,000 fictitious applications in New Jersey and New York City. Employers who asked about records called applicants without a felony conviction 63% more. After ban-the-box laws removed the question, the white–Black callback gap among affected employers rose from about **7% to 43–45%**, depending on version. This is evidence of statistical discrimination when information is removed.
- **UK** (strong; government): DBS checks come in basic (unspent convictions and conditional cautions), standard and enhanced, and results go directly to the applicant (`govuk-dbs`).
- **Reference checks as a predictor** (strong, historical): reference checks had a validity of .26 in `schmidt1998`. They were excluded from the 2022 revision for insufficient information (`sackett2022`).
- **India:** background verification (BGV) by third-party firms is common in IT and services. **Not verified with a credible source in this pass**, so leave it out or mark it practitioner knowledge.

## Sources in this file
`galinsky2001`, `hallkrueger2012`, `marks2011`, `leibbrandt2015`, `bowles2007`, `hernandez2019`, `clockspot-paytransparency`, `cooley2026`, `nydol-paytransparency`, `ec-paytransparency`, `lockton2026-eu`, `cullen2023`, `irs-p525`, `secfi-vesting`, `interviewguys-counteroffer`, `4dayweek-counteroffer`, `niederle2009`, `eeoc-ftc-background`, `agan2018`, `govuk-dbs`, `schmidt1998`, `sackett2022`.
