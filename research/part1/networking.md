# Networking, weak ties and the "hidden job market"

Research notes for Part I. Keys refer to `sources.yaml`. Grades are defined in `README.md`.

## The one-paragraph version

Granovetter's 1973 idea holds up, with refinements. Weak ties bridge to information your close friends don't have. In 1973 the evidence was 54 people in a Boston suburb. In 2022 it was a randomised experiment on 20 million LinkedIn users. That experiment found an **inverted U**: moderately weak ties help most, the weakest and the strongest less. Weak ties mattered more in digital industries. A Facebook study found most people get job help through one of their many weak ties, but a single strong tie is worth more at the margin. The "hidden job market" is half true. Surveys consistently find **50–60% of workers say they used a contact** to find their job. The specific claim that "70–80% of jobs are never advertised" has no traceable rigorous source.

## Findings

### 1. Granovetter (1973): the original evidence. Grade: moderate
- Source: `granovetter1973`. In "a random sample of recent professional, technical, and managerial job changers living in a Boston suburb", among those who found the job through contacts (N = 54), **16.7%** saw that contact "often" (at least twice a week), **55.6%** "occasionally" and **27.8%** "rarely" (once a year or less).
- The contact was often "someone only marginally included in the current network… such as an old college friend or a former workmate or employer".
- The theory is that weak ties bridge to other social circles, so they carry *new* information. Strong ties carry *redundant* information.
- Caveat: tiny and local sample; contact frequency is one proxy for tie strength. Correlational.

### 2. The 2022 causal test on LinkedIn. Grade: strong
- Source: `rajkumar2022` (*Science*). LinkedIn's "People You May Know" experiments (2015 and 2019) randomly varied how many weak vs strong ties were recommended. Over 20 million people, ~2 billion new ties and 600,000 new jobs.
- Findings:
  1. The effect is nonlinear. There is an inverted U between tie strength and "job transmission", meaning later working at the contact's company.
  2. Moderately weak ties by mutual connections, and the weakest ties by interaction intensity, produced the most mobility.
  3. Weak ties helped more in **more digital** industries. Strong ties helped more in **less digital** ones.
- Their non-experimental (OLS) estimates reproduced the "paradox of weak ties", where strong ties look better. Only the experimental estimates revealed the inverted U. This is a nice teaching point about correlation vs causation.
- Caveats: the per-tie probability of a job transmission is a fraction of a percent. The outcome is measured only on LinkedIn. The users were not told they were in experiments, which drew ethics criticism (`acs2022-linkedin`).

### 3. Facebook: many weak ties, but each strong tie is worth more. Grade: strong
- Source: `gee2017` (6 million Facebook users, *Journal of Labor Economics*). "Most people are helped through one of their numerous weak ties but a single stronger tie is significantly more valuable at the margin."
- How to reconcile this with Granovetter (author synthesis, labelled): you have many more weak ties than strong ones. Most help therefore *arrives* through weak ties, even if any single strong tie is more likely to help. Both messages are true. `rajkumar2022`'s inverted U is consistent with both.

### 4. How common is finding a job through contacts? Grade: strong (consistent survey evidence)
- `lester2021` summarises Topa (2011): "Most surveys of job seekers find between 50 and 60 percent of workers report using a referral to find employment." Firm surveys range from "just under 40 percent of hires" to "significantly more than 50 percent".
- `pellizzari-via-brown2016`: 25–40% of respondents in most European countries heard about their current job through informal contacts (European Community Household Panel; secondary citation).
- In firm-side data, referrals are 11–29% of hires (see `referrals.md`), while internal moves are another large share (`gem2025`: 12.56% of hires).

### 5. The "hidden job market" claim, separated into true and myth
| Claim | Verdict | Grade |
|---|---|---|
| Many jobs are filled through contacts, referrals and internal moves rather than cold applications | True | strong (`lester2021`, `brown2016`, `gem2025`) |
| Applying through a contact massively raises your odds of being interviewed | True | strong (`brown2016`) |
| "70% / 80% / 85% of jobs are never advertised" | No traceable rigorous source. "Likely originated from anecdotal evidence and informal surveys" (`fresnostate2024-hidden`). Note that a job filled by referral may still have been publicly posted; "filled via a contact" is not the same as "never advertised". | myth-or-unsupported |
| You must network instead of applying | False dichotomy. Job boards still produce a quarter or more of hires (`gem2025` 24.6%; `careerplug2025` 43.3%; `brown2016` 23.5%) | moderate |

### 6. What networking is for (synthesis; evidence plus author view)
- Evidence: weak and medium professional ties carry new information (`granovetter1973`, `rajkumar2022`). Business-contact referrals lead to higher starting wages (`lester2021`). A referral changes how your application is processed (`brown2016`).
- *Author view:* networking is not schmoozing strangers at events. Done well, it means:
  1. keeping in light touch with former colleagues, classmates and managers, who are the "marginally included" ties in Granovetter's sample;
  2. being someone others would honestly vouch for, so they *can* refer you (Part II ties in here);
  3. asking specific, easy questions ("Is the team hiring? Would you be comfortable referring me?") rather than vague ones ("Can I pick your brain?").

## Sources in this file
`granovetter1973`, `rajkumar2022`, `acs2022-linkedin`, `gee2017`, `lester2021`, `pellizzari-via-brown2016`, `brown2016`, `gem2025`, `careerplug2025`, `fresnostate2024-hidden`.
