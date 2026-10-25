---
id: ch05
status: review
---

::: scene {slug="INT. DEV'S FLAT — WEDNESDAY, 10 PM"}
Dev's phone buzzes. It is Rex, from his new job, already.

@rex: Heard you're looking!! Sending my CV for inspiration. Don't copy it word for word, people will notice

She opens the attachment. It is beautiful. Two columns, a monogram, a photograph in which Rex looks like he is about to buy a yacht. The bullets are a parade:

> *Spearheaded a transformative, cross-functional quality initiative, driving a 300% uplift in stakeholder alignment.*
> *Visionary self-starter with a proven track record of delivering world-class outcomes in fast-paced environments.*
> *Single-handedly revolutionised deployment culture.*

Dev reads it twice. Then she opens her own, which says "Responsible for regression testing" and "Involved in release activities", and feels briefly worse. Then she reads Rex's again, more slowly, and feels better.

@dev: (to the empty room) What *is* a 300% uplift in alignment?

She knows Rex's deployment culture. She was there. It was a wiki page.
:::

Rex's résumé and Dev's have the same problem from opposite ends. Dev's is accurate and says almost nothing. Rex's says a great deal and is impossible to check. A stranger reading either one learns very little about the person who wrote it.

This chapter is about *paper you*: the résumé, the online profile, the portfolio and the occasional cover letter. In the language of [[ch01]], they are your trailer in its most compressed form, read by strangers, often quickly, with no chance for you to explain. That sounds hopeless until you know how they are actually read. Then it turns into a design problem, and design problems can be solved.

::: pause
Guess two things. First: how long does a recruiter spend on the first look at a résumé? Second: what do they look at in that time? Write down your answers; you will need them in a minute.
:::

## Two readers, two speeds {#ch05.sec.two-reads}

Every résumé is read at least twice, by readers asking different questions.

The **first glance** decides whether you go on the "maybe" pile. It is fast, because the reader has a stack, and it asks one question: *is this plausibly a fit?* The **full read** happens only if you pass. It is slower, often done by the hiring manager or just before an interview, and it asks a harder question: *is this true, and is this person someone I want to talk to?*

::: figure {#ch05.fig.two-reads src="ch05/two-reads.svg"}
Alt: Two small résumé pages, stacked. The first, labelled "The first glance: seconds, for everyone", has the headline, job titles, dates and education highlighted in gold, with the question "Is this plausibly a fit?" and the note "looks at: titles, employers, dates, education". An arrow labelled "only if you pass" leads to the second page, "The full read: minutes, if you pass", where the bullets are highlighted and question marks sit beside them, with the question "Is it true, and is it them?" and the note "looks at: what changed, by how much; what to ask about".

The same page, read twice. The first glance checks the scaffolding; the full read tests the claims. A good résumé is designed for both.
:::

How fast is the first glance? You have probably heard a precise answer.

::: myth {#ch05.myth.six-seconds verdict=partly grade=weak} Recruiters read your résumé for six seconds
The number comes from a 2012 eye-tracking study by TheLadders, a job site, which watched thirty recruiters over ten weeks and reported that they spent "about 6 seconds" on their initial fit or no-fit decision, with almost 80% of that time on names, current and previous titles and employers, dates and education [@ladders2012]. It was never peer-reviewed, and the same document ended by recommending the company's own résumé-rewriting service [@ladders2012]. A 2018 update reported an average of 7.4 seconds but gave no sample size [@ladders2018]. So the seconds are shaky. The underlying point holds up: the first pass is a brief skim of the page's scaffolding, which fits everything we know about funnels with hundreds of applicants ([[ch03.sec.funnel]]). The skim is not the evaluation; it is the gate to it.
:::

If your guess for the pause was "a few seconds", you were right in spirit. If you guessed the reader looks at your carefully worded summary paragraph, you are in good company, and the eye-tracking suggests otherwise [@ladders2012!]. That leads to the most useful design principle in this chapter: **make the scaffolding carry the message**. Titles, employers, dates and the first lines of the page must say "plausible fit" on their own [!view]. Then the bullets have to survive the full read.

## The anatomy of a trailer {#ch05.sec.anatomy}

A résumé has a handful of parts, and each has one job.

::: figure {#ch05.fig.anatomy src="ch05/anatomy.svg"}
Alt: A one-page résumé, drawn as lines and blocks, with the header shaded gold and a coral bar beside the top part of the page. Arrows from the right label each part: "headline: your one-line answer (Ch 4)" at the top; "titles, employers, dates: read first" at the first job line; "bullets: what changed, by how much" at the bullet points; "skills: the ad's words, if they are true" at the skills line; "education: short, unless it's your best" at the bottom. A note under the page: "where the first skim lands: titles, names and dates up top".

A résumé as a trailer. Each part has one job, and the parts the first skim reads (headline, titles, employers, dates) must make the case before the bullets get a chance.
:::

- **The headline** sits under your name. It is your one-line answer from [[ch04.sec.one-line]], compressed: what you do, one strong piece of evidence, and what you are aiming at. "Test automation engineer moving into backend development; cut a 6-hour regression run to 40 minutes" does more in a second than a paragraph of adjectives.
- **Titles, employers and dates** are the skeleton the first glance reads. Use your real title; if it is unusual, add a plain description in brackets ("Quality Engineer II (test automation)"). Never upgrade it: a title is exactly the kind of fact a reference or background check can confirm ([[ch09]]).
- **Bullets** are where the full read happens: three to five per recent role, each one a piece of evidence. The next section is about writing them.
- **Skills** use the employer's own words for things you can genuinely do. If the ad says "PostgreSQL", write "PostgreSQL", not "relational databases". Recruiters search for terms, and some filters match exact criteria [@hiddenworkers2021]. Stuffing in words you cannot back up fails the full read, and a 2018 eye-tracking update found keyword-stuffed résumés among the worst performers with human readers [@ladders2018!].
- **Education** is short unless it is your strongest evidence, as it often is for new graduates.

What about format? The evidence is thin and commercial, but consistent: clean single-column layouts with clear section headings did best in the eye-tracking studies, and multiple columns and clutter did worst [@ladders2018!]. Rex's two-column masterpiece is the kind of design that looks impressive on a screen and gets lost in a skim, and some applicant tracking systems also mangle columns and tables [!craft]. Boring formatting is a gift to a tired reader.

## Bullets that work {#ch05.sec.bullets}

Dev opens a new tab, *Bullets that work*, and pastes in her old bullets, one per row, with an empty column next to each for the rewrite.

A bullet that works is a duty put through the three questions from [[ch04.fig.duty]]. In practice it has a recognisable shape: **a strong verb, what you did, and what changed**, with a number or another kind of specificity in it [!craft].

| Before | After |
| --- | --- |
| Responsible for regression testing. | Cut the nightly regression run from 6 hours to 40 minutes by running suites in parallel; the team now tests every merge. |
| Involved in release activities. | Rewrote the deployment scripts after two failed releases; no release has failed on deployment since (14 and counting). |
| Worked with the client on defects. | Found a queueing bug in the payments service two days before go-live, before the client did; wrote the reproduction the developers used to fix it. |

Notice three things about the "after" column. Each bullet leads with something Dev *did*, not something she was responsible for. Each one has a result a stranger can picture. And each one is an invitation: *How did you parallelise the suites? Why did the releases fail? How did you find the bug?* Those are exactly the questions Dev wants to be asked, because she has good answers. A bullet that invites a question you want to answer is doing its job twice: once on paper, and again in the interview ([[ch07]]).

:::: move {#ch05.move.fix} Fix three bullets
Rewrite each bullet so that it would survive both the first glance and the full read. Invent plausible details where you need them.

1. "Hard-working team player with excellent communication skills."
2. "Managed social media accounts."
3. "Helped improve onboarding for new hires."

::: answer
1. **Delete it.** This is not a bullet; it is three claims that cost nothing to make and that every reader skips ([[ch01.sec.signals]]). If communication really is a strength, prove it in a bullet about something you communicated: *"Wrote the incident summaries the leadership team now uses as its template; cut follow-up questions after outages from dozens to a handful."*
2. *"Ran the company's two social accounts; moved from daily promotional posts to weekly how-to videos, which tripled comments in six months and became the team's main source of trial sign-ups."* "Managed" is a duty; the change in approach is evidence, and "tripled" is checkable.
3. *"Rebuilt the first-week onboarding checklist with three recent hires; new engineers now ship their first change in their first week instead of their third."* "Helped improve" hides both your role and the result; this names both.

A test for any bullet: imagine the interviewer reads it aloud and says, "Tell me more." If your heart sinks, the bullet is either vague or not quite true. If you want to start talking, it is ready.
:::
::::

## Too good to be true {#ch05.sec.too-polished}

Back to Rex, because his résumé teaches the most important lesson in this chapter by getting it exactly backwards.

Every line on it is designed to impress, and almost none of it can be checked. "Visionary self-starter" costs nothing to write. "A 300% uplift in stakeholder alignment" sounds like a number but measures nothing anyone could verify. "Single-handedly revolutionised deployment culture" is the kind of claim that makes an experienced reader reach for the phone to call a reference. In Spence's terms, these are signals that everyone can send, so they cannot separate the people who did the work from the people who did not [@spence2001-lecture]. To an experienced reader, we would argue, they also hint that the writer had nothing more specific to say [!view].

Rex gets interviews anyway, because he is superb once he is in the room, and because a polished page clears the first glance easily. But the full read is where his résumé starts working against him, and the follow-up questions are where it fails.

::: craft
**The follow-up test.** For every line on your résumé, write the two questions an interviewer is most likely to ask about it, and answer them out loud. If the answers are specific and you enjoy giving them, the line stays. If the answers are vague, sharpen the line until they are not. If you cannot answer at all, the line goes. Experienced interviewers probe hardest where a candidate sounds most polished, which makes this the cheapest interview preparation there is.
:::

Try it on someone else's résumé first. It is much easier to be ruthless with a stranger's.

:::: move {#ch05.move.follow-up} The follow-up test
Here are three lines from Rex's résumé and three from Dev's new one. For each, write the first question a sharp interviewer would ask, and predict whether the writer will enjoy answering it.

1. Rex: "Spearheaded a transformative, cross-functional quality initiative."
2. Rex: "Driving a 300% uplift in stakeholder alignment."
3. Rex: "Single-handedly revolutionised deployment culture."
4. Dev: "Cut the nightly regression run from 6 hours to 40 minutes."
5. Dev: "No release has failed on deployment since (14 and counting)."
6. Dev: "Found a queueing bug in the payments service before the client did."

::: answer
1. *"What was the initiative, and what changed because of it?"* Rex will answer warmly and at length, and by the end the interviewer will know it was a set of meetings. **Not enjoyable**, under a sharp interviewer.
2. *"How did you measure alignment?"* There is no good answer. **Painful.**
3. *"Who else was involved?"* "Single-handedly" invites exactly the question that finds the other people. **Painful**, and a reference call will finish the job.
4. *"How did you get it down to 40 minutes?"* Dev can talk about this for half an hour. **Enjoyable.**
5. *"What was failing before?"* A good story about a mistake, a fix and a result. **Enjoyable**, and it fills the "mistake owned" column in her story bank.
6. *"How did you find it?"* A story about curiosity and persistence. **Enjoyable.**

The pattern is the book's thread in miniature: lines that are specific and true get *better* under questioning; lines that are polished and vague get worse. The trailer must survive the film [!view].
:::
::::

## Accuracy, not bragging {#ch05.sec.accuracy}

Dev's problem was vagueness. Bea's is different, and it surfaces when Dev sends her the *Bullets that work* tab to try.

::: scene {slug="INT. CORVID SYSTEMS, A QUIET MEETING ROOM — THURSDAY, 12:30 PM"}
Bea has a sandwich in one hand and a pen in the other, and she has crossed out more than she has written.

@bea: I can't put "rewrote the billing engine". It sounds like bragging. Three of us worked on it.

@dev: Who designed it?

@bea: Me.

@dev: Who wrote most of it?

@bea: Me. The others did the migration scripts.

@dev: So "maintained and enhanced" is accurate?

@bea: ... No.

@dev: Then it's not modest. It's wrong. Write what happened. Credit the others. That's not bragging, that's a correct sentence.

Bea writes: *Designed and wrote most of a new billing engine in two weeks, with two colleagues handling data migration; month-end billing went from two days of manual fixes to an overnight run.*

She looks at it for a long time.

@bea: It feels like someone else.

@dev: It's the most *you* sentence on the page.
:::

Dev is right, and the reason is worth spelling out.

::: craft {by=author} Understating is not humility
Bea's instinct is a good one in the long game: people who boast about their work are tiring to work with, and credit-claiming damages trust ([[ch16]]). But a résumé is not a conversation with colleagues who already know the story. It is a document for strangers who will assume that what you leave out did not happen.

So we think the honest standard for paper is **accuracy, not modesty**. Write what you did, at its true size, and name what others did. If that sentence makes you uncomfortable because it is big, the discomfort is not a reason to make it smaller and wrong. If it makes you uncomfortable because it is bigger than what happened, that is a reason to fix it. The goal is a trailer that is a true cut of the film: no scenes added, and no good scenes left on the floor.

This is our view, not a measured finding. It is also the same rule the book will apply to promotion cases in [[ch19]].
:::

## Small things that cost a lot {#ch05.sec.typos}

Not every rule about résumés is folklore. One of the best-evidenced is also the most boring.

::: myth {#ch05.myth.typos verdict=busted grade=strong} A typo or two doesn't matter
In an experiment in which 445 recruiters rated résumés for job interviews, résumés with several spelling errors cut the probability of an interview invitation by 18.5 percentage points, and even résumés with just a few errors cut it by 7.3 points [@sterkens2023]. About half of the penalty came from what recruiters inferred about the candidate from the mistakes: lower conscientiousness, lower mental ability and weaker interpersonal skills [@sterkens2023]. It was a scenario experiment rather than real hiring decisions, but the effect was large and the mechanism plausible. Typos are cheap signals of carelessness, read by people looking for a reason to shorten the pile.
:::

The fix is cheap and dull. Read your résumé aloud, slowly. Read it backwards, bullet by bullet, so that you see words rather than meaning. Ask someone who has not seen it before to read it, because your eyes will correct mistakes your brain knows should not be there [!craft]. And check the details that matter most: names of employers, job titles, dates, and the name of the company you are applying to, which is the one people most regret getting wrong.

## How long should it be? {#ch05.sec.length}

::: myth {#ch05.myth.one-page verdict=busted grade=weak} Your résumé must be one page
There is no peer-reviewed evidence for a one-page rule. The only sizeable test we found is commercial: a résumé-writing service ran a simulated hiring exercise with 482 recruiters and hiring managers, and reported that they were 2.3 times as likely to prefer two-page résumés, and 1.4 times as likely for entry-level roles [@resumego2018-length]. That is unpublished, run by a company that sells résumés, and measured preference in a simulation rather than hiring. It does not prove two pages are better. It does show that the one-page "rule" is a convention, not a law.
:::

Length should follow content [!view]. Early in a career, one page is a sensible default, because you rarely have two pages of strong evidence and padding dilutes it. With substantial experience, two pages is normal and fine. Beyond that, ask whether every line would survive the follow-up test. Regional habits differ too: a US résumé, a UK CV and an academic CV are different documents, and the Field Note below covers what we could verify.

## Profiles, portfolios and code {#ch05.sec.profiles}

Paper you is not only paper. Online profiles and portfolios do two jobs a résumé cannot: they make you **findable**, and they can show **work** rather than describe it.

Findability matters because recruiters do not only wait for applications; they go looking. In one vendor's data, candidates whom recruiters sourced were hired at 2.0%, against 0.4% for people who applied through the front door [@gem2025]. That is mostly because the recruiter chose them, but you can only be chosen if you can be found. A profile with your real current title, a clear headline in the spirit of your one-line answer, and the skills you would want a recruiter to search for is a channel in its own right [!view]. Professional networks are also how weak ties find you, which is the subject of [[ch06]].

::: myth {#ch05.myth.photo verdict=busted grade=weak} LinkedIn profiles with a photo get 21 times more views
The claim, that profiles with a photo get "up to 21x more profile views" and "36x more messages", is LinkedIn's own and is repeated widely in marketing articles [@sej-linkedin-photo]. We found no published method, dataset or study behind it. A photo may well help on a platform built around people; nobody has shown by how much, and the "21x" should not be quoted as a finding.
:::

Portfolios show work instead of describing it, which makes them costly signals in exactly Spence's sense. In a small interview study of employers who used GitHub to evaluate developers, employers read public activity as evidence of skill, motivation and values, and trusted it more than résumés precisely because it was hard to fake [@marlow2013!]. That study is small and dated, and plenty of excellent engineers have no public code because their work belongs to their employer, so the *absence* of a portfolio is rarely held against an experienced candidate [!view]. But for a career changer, a new graduate or someone whose title undersells them, a small, real piece of work with a history behind it can do what no bullet can. Outside software, the same logic applies to writing samples, design work, case studies and published analyses: one finished, explained piece beats ten unexplained ones.

Dev starts one: a small open-source tool that runs test suites in parallel, the idea behind her best bullet, rewritten from scratch on her own time with a README explaining the design decisions. It is not impressive in size. It is impressive in being *real*, and it gives an interviewer something to look at that is not her description of herself.

## Cover letters {#ch05.sec.cover}

Do cover letters matter? The honest answer is that nobody has tested it well.

The evidence we have is commercial and conflicting. A résumé-writing service sent 7,287 fictitious applications to real job postings with no cover letter, a generic letter or a tailored one, and reported that tailored letters received a 53% higher callback rate than no letter; in its survey of 236 hiring professionals, 87% said they read cover letters [@resumego2020-cover!]. The study is unpublished, and its group-by-group results were only available as an image we could not verify. A different résumé-services company surveyed more than 1,000 US hiring managers and reported that 83% said "To Whom It May Concern" would have little or no effect on whether they offered an interview [@aacsb2020-twimc!].

From that, a modest rule [!view]: when an application has a place for a letter, send a short one written for this job; when it does not, do not force one. A good letter is three short paragraphs: why this role, the one or two pieces of evidence that make you a fit (straight from your story bank), and what you would like to happen next. A generic letter is worse than none, because it is a costless signal that you did not take the trouble. And often the best cover letter is not a letter at all, but a colleague of the hiring manager saying your name ([[ch06]]).

## Names, and what paper cannot fix {#ch05.sec.names}

::: flashback {ref=ch03.sec.bias}
[[ch03.sec.bias|Chapter 3]] set out the audit studies: identical applications with different names get different callback rates, in the US by race and in India by caste and religion [@bertrand2004; @kline2022; @thorat2009].
:::

That evidence lands hardest on paper, because paper is where a name arrives alone. Some job seekers respond by "whitening" their résumés: concealing or downplaying racial cues in their applications. A study combining interviews, a laboratory experiment and an audit of employers found that some minority job seekers do this and others refuse to; that applicants whitened less when an employer described itself as valuing diversity; and that, in the audit, those pro-diversity statements were not associated with less discrimination against unwhitened résumés [@kang2016].

We are not going to tell you what to do with that. Whether to change how you present yourself, to protect your chances or to refuse on principle, is a decision about your identity and your circumstances, and readers will reasonably decide differently. What we can say is what the evidence implies for strategy: an employer's statements about diversity are weak evidence of how it screens; the route in matters, because a referral puts a person who vouches for you in front of your name ([[ch06]]); and none of this is a verdict on you [!view].

:::: field {regions="US, UK, EU, India"} What goes on a CV
::: figure {#ch05.fig.regions src="ch05/regions.svg"}
Alt: Four stacked cards headed "What goes on the page, by region". US: no photo; the EEOC tells employers to avoid asking for one before an offer; age, religion and origin are irrelevant. UK: "not your age, date of birth, whether you're married or your nationality", from the National Careers Service. EU: Europass, the EU's CV tool, suggests adding a professional photo; national habits vary, not verified. India: no official guidance we could verify; ask people in your sector what employers there expect. Note: "Only what we verified; everywhere else, check local norms."

Conventions differ by region, and in some places nobody publishes them. These are the only rules we could verify.
:::

- **US.** The Equal Employment Opportunity Commission advises that pre-employment information should be limited to what is essential for judging qualifications, treats characteristics such as race, sex, national origin, age and religion as irrelevant to that judgement, and advises employers against requesting photographs before an offer [@eeoc-prohibited]. Our reading is that a US résumé should leave out the photo and personal details [!view].
- **UK.** The government's National Careers Service advises: "You should not include your age, your date of birth, whether you're married or your nationality" [@ncs-cv].
- **EU.** Europass, the EU's official CV tool, tells users to "add a professional photograph of yourself" [@europass-cv]. That is consistent with photos being more customary in parts of continental Europe, but we did not verify how common they are in any particular country.
- **India.** We found no official guidance on CV conventions that we could verify, so ask people who hire in your field what they expect.
::::

Most résumé advice online mixes all of this together, with great confidence. Time to sort some of it.

:::: move {#ch05.move.myths} Spot the myth
A friend sends you this advice, which they found online. Mark each line **holds**, **partly** or **myth**, and say what the evidence actually supports.

1. "Recruiters spend six seconds on your résumé, so nothing below the top third matters."
2. "Keep it to one page or it goes in the bin."
3. "A couple of typos won't matter if the content is strong."
4. "Put the job ad's keywords in white text so the robots find them."
5. "Always add a photo; profiles with photos get 21 times more views."
6. "Use the posting's own words for skills you actually have."

::: answer
1. **Partly.** The first pass is a quick skim of titles, employers, dates and education [@ladders2012!], so the top of the page must make the case. But anyone who passes the skim gets a full read, and that is where the bullets lower down earn the interview.
2. **Myth.** There is no evidence for a one-page rule; the only test we found was commercial and leaned the other way [@resumego2018-length!]. Length should follow content.
3. **Myth.** Even a few errors cut interview chances by 7.3 percentage points in a recruiter experiment [@sterkens2023].
4. **Myth, and a trap.** There is no study behind the idea that software rejects most résumés unseen ([[ch03.sec.ats]]), and the humans who read the result will see the trick. Keyword stuffing did badly with human readers [@ladders2018!].
5. **Myth as stated, and region-dependent.** The "21 times" figure has no published basis [@sej-linkedin-photo]; and on a US résumé, a photo goes against official advice to employers [@eeoc-prohibited].
6. **Holds**, with the condition attached. Employers search for terms and filter on exact criteria [@hiddenworkers2021], so the posting's words for skills you genuinely have help both the search and the skim.
:::
::::

Three more questions come up whenever this chapter's advice meets a real search.

::: ask
Q: Should I tailor my résumé for every application?

A: Tailor the top third and the order of your bullets for each *kind* of role, and the skills section for each ad, using its words for things you can do. Rewriting the whole document every time is rarely worth it [!craft]. Your target list from [[ch04.move.targets]] tells you how many versions you need; usually two or three.

Q: How do I explain a gap on my résumé?

A: In one plain line, in the place where the gap appears: "2025: career break to care for a family member" or "2025–26: laid off in a reduction of 120 roles; completed a course in data engineering". The evidence suggests that a past gap followed by work matters far less than a current one ([[ch02.sec.layoffs]]). Silence invites guessing; a line closes the question.

Q: Isn't all this just teaching people to market themselves better than they deserve?

A: It is teaching people whose work is better than their paper to fix the paper. The whole chapter rests on one rule: put on paper only what would survive questioning. Followed honestly, it helps Bea far more than it helps Rex.
:::

By Sunday evening, both résumés are done.

::: scene {slug="INT. DEV'S FLAT — SUNDAY, 6 PM"}
The *Bullets that work* tab has two columns, *Before* and *After*, and nineteen rows. Dev's new résumé is one page. Bea's is two, because she has eight years of things that happened.

Dev's phone buzzes. It is Rex again.

@rex: Did my CV help??

@dev: It really did. Thank you.

She means it. It showed her exactly what not to do.

Bea sends a message too, a screenshot of her new top third, with a single line underneath.

@bea: It still feels like someone else.

@dev: It's you. Just legible.

Dev's résumé goes out to three targets from her list on Monday morning. One of them is Lanternfish, a logistics-software company she has never heard of until this week. And, it turns out, a university acquaintance of hers works there.
:::

Paper you is finished, or at least finished enough: a page that survives a skim, bullets that survive a read, and a portfolio that shows the work instead of describing it. But paper is the coldest way into the funnel. The warmest is a person, and that is the subject of [[ch06]]. After that, the paper becomes a script for the conversation: every bullet you wrote is a question you will be asked in [[ch07]], and every claim on it is something a background check or a reference may test in [[ch09]].


::: rewind
- Every résumé is read twice: a **first glance** that checks titles, employers, dates and education, and a **full read** that tests the claims. Design for both.
- The **six-second** figure comes from a small, commercial study; the lesson that survives is that the scaffolding at the top of the page must make the case on its own.
- **Bullets that work** have a strong verb, what you did and what changed, with specificity a stranger can picture, and they invite questions you want to answer.
- **Too polished is a signal too.** Claims that cost nothing to make carry no information. Use the **follow-up test** on every line.
- **Accuracy, not modesty, not hype.** Write what you did at its true size and credit others; leaving out what happened is not humility.
- **Typos cost real interviews**: 7.3 to 18.5 percentage points in a recruiter experiment. Length should follow content; the one-page rule is a convention.
- **Profiles make you findable, portfolios show work.** Cover letters have weak evidence either way: short and tailored, or not at all.
- Names still change callbacks, and diversity statements are weak evidence of fair screening. CV conventions differ by region; we print only what we verified.
:::
