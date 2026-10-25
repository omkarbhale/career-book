# How well hiring methods predict job performance

Research notes for Part I. Source keys refer to `sources.yaml`. Grades: **strong / moderate / weak / myth-or-unsupported** (defined in `README.md`).

## The one-paragraph version

Employers use many tools to guess who will do the job well. Decades of meta-analysis rank them. The famous 1998 ranking (Schmidt & Hunter) put cognitive ability tests, work samples and structured interviews near the top with validities around .5. A 2022 re-analysis (Sackett, Zhang, Berry & Lievens) argued that earlier corrections for "range restriction" were too generous. It cut most estimates by .10 to .20 and put **structured interviews first (.42)**. **Unstructured interviews come in at about half that (.19).** The ranking holds up better than the exact numbers, and the field is still arguing over the numbers.

What this means for a candidate: the employer is trying to predict, and their tools are noisy. Even the best single method correlates around .4 with later performance. Doing well on the day and being good at the job are related but different skills. That is the thesis of Part I.

## Findings

### 1. Schmidt & Hunter (1998): the classic table. Grade: strong (as a historical estimate)
- Source: `schmidt1998`. A meta-analytic summary of 19 selection procedures drawn from 85 years of research.
- Operational validities for overall job performance (corrected for criterion unreliability and range restriction):
  - general mental ability (GMA) .51
  - work sample tests .54
  - structured interviews .51
  - unstructured interviews .38
  - job knowledge .48
  - integrity tests .41
  - reference checks .26
  - years of education .10
  - graphology .02
  - age −0.01
  - (These S&H values are reproduced in Sackett et al. 2022, Table 3.)
- The best two-method combinations were GMA + integrity test (.65), GMA + work sample (.63) and GMA + structured interview (.63). This is stated in the abstract.
- Caveat: these numbers are now widely regarded as inflated. See finding 2. Quote them only next to the revision.

### 2. Sackett, Zhang, Berry & Lievens (2022): the revision. Grade: strong
- Source: `sackett2022`, Table 3 ("Comparison of Schmidt and Hunter's (1998) validity estimates with present study's validity estimates").
- The argument: the "artifact distributions" used to correct for range restriction were not representative of real applicant pools. They often came from predictive studies with large restriction and were then applied to concurrent studies with little. The result was systematic overcorrection.
- Revised mean operational validities (ρ), with S&H 1998 values in brackets:

| Method | Revised ρ | S&H 1998 |
|---|---|---|
| Structured interviews | **.42** | .51 |
| Job knowledge tests | .40 | .48 |
| Empirically keyed biodata | .38 | .35 |
| Work sample tests | .33 | .54 |
| Cognitive ability tests | .31 | .51 |
| Integrity tests | .31 | .41 |
| Assessment centres | .29 | .37 |
| SJT (knowledge) | .26 | n/a |
| Conscientiousness (overall) | .19 | .31 |
| **Unstructured interviews** | **.19** | .38 |
| Job experience (years) | .07 | .18 |

- The abstract states it directly: "Structured interviews emerged as the top-ranked selection procedure", and mean estimates fell by ".10–.20 points".
- The paper also reports Black–White subgroup differences (d) for each method. Cognitive tests show the largest (d = .79) and structured interviews a small one (.23). This is the validity–diversity tradeoff, and it is useful context for why many employers favour interviews.
- Caveat: these are correlations with mostly supervisor ratings. A correlation of .42 still leaves most of the variance in performance unexplained.

### 3. A newer meta-analysis puts cognitive ability lower still. Grade: strong (with an active debate)
- Source: `sackett2023-gca`. It covers 21st-century studies only: 153 samples, N = 40,740. The mean observed validity is .16 and the corrected validity .22, against .31 in Sackett 2022 and .51 in S&H 1998.
- The counter-view: `ones2023` (Ones & Viswesvaran, *Industrial and Organizational Psychology*, 2023). They argue that range-restriction corrections in concurrent studies are appropriate and "disagree with the assertion that the operational validity of cognitive ability is much lower than previously reported."
- For the book: present this as a live scientific dispute about magnitudes. Nobody in it claims that cognitive ability is useless or that unstructured interviews beat structured ones.

### 4. Inside structured interviews: past-behaviour vs situational questions. Grade: strong
- Source: `levashina2014` (a narrative and meta-analytic review in *Personnel Psychology*).
- Both question types predict performance. Past-behaviour questions ("Tell me about a time when…") show slightly higher validity on average. The meta-analyses cited in the review report these mean **uncorrected** validities:
  - Taylor & Small (2002): situational .25, past-behaviour .31
  - Huffcutt et al. (2004): situational .26, past-behaviour .31
- Job complexity moderates this. Situational questions lose validity for high-complexity jobs in some meta-analyses. Past-behaviour questions hold steady (about .30 and .31).
- This is the evidence behind behavioural interviewing and the STAR answer format (see `interviewing.md`).

### 5. Impression management works, somewhat, even in structured interviews. Grade: strong
- Source: `levashina2014`, Table 4. This is a meta-analysis of impression management (IM) tactics in structured interviews, using observed mean correlations with interview ratings:
  - self-promotion r = .26 (k = 13, N = 2,202)
  - nonverbal IM .18
  - other-focused IM (for example, ingratiation) .13
  - defensive IM .12
- Structure reduces but does not remove these effects. Being able to state your accomplishments clearly is a real, measurable lever. It is also a gap between "good at getting hired" and "good at the job".

## What it means for the book (author view, labelled)
- *Author view:* Treat a hiring process as a measurement instrument with known error bars. Candidates should prepare for the instrument as it is: give structured answers and concrete evidence, and use a work-sample mindset. Don't take a rejection as a verdict on your worth.
- *Author view:* When you later sit on the other side of the table, as Part II will have you do, push for structure.

## Sources in this file
`schmidt1998`, `sackett2022`, `sackett2023-gca`, `ones2023`, `levashina2014`.
