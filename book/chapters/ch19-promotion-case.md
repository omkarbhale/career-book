---
id: ch19
status: final
---

::: scene {slug="INT. LANTERNFISH, A SMALL MEETING ROOM — FRIDAY, 4:10 PM"}
Tomás closes the door and sits down, and then, uncharacteristically, apologises before he has said anything.

@tomas: I know. It's Friday afternoon. I hate this as much as you're about to. But the committee met this morning, and I didn't want you refreshing your email all weekend.

Six months ago, after her first review, Tomás nominated Dev for promotion to senior engineer in the spring round. She spent three weekends on the case, in a new spreadsheet tab called *Promotion case*. It was thorough. It had twenty-three items, every one of them true, every one with a link: the reconciliation release, the race condition, Northwind, the onboarding sessions, two conference-room demos, a design document, a dozen code reviews she was proud of, and the coffee committee, under *Leadership*.

@tomas: It's a not yet.

He reads her the committee's note, because he thinks she should hear the actual words.

> *Consistently strong at current level. The case lists many contributions, but the committee could not identify impact at senior scope. Re-nominate when there is evidence of impact beyond the squad.*

@dev: I put twenty-three things in it.

@tomas: I know. I think that was part of the problem.
:::

The review in [[ch18]] asked whether Dev had done her job well. A promotion asks a different question: whether she is already doing the *next* one. That sounds like a small change of wording. It changes almost everything about how the evidence has to be assembled, who has to see it, and what counts.

This chapter is about how promotion decisions are really made: by whom, on what evidence, and why the best performer is not always the person promoted. It is also where several of the book's threads finally meet. Part I's rules for signals turn out to be the rules for a promotion case. Part II's trust ledger turns out to be the currency the decision is paid in. And the uncomfortable evidence about who gets seen, and who gets judged to have "potential", turns out to matter more here than anywhere else.

::: pause
Dev's case listed twenty-three true, evidenced things she had done. Why might a committee find it *weaker* than a case with five? Write down two reasons before you read on.
:::

## Inside the room {#ch19.sec.room}

Start with the structure, because it explains a lot of what feels arbitrary.

Economists model promotion as a **tournament**: the prize, a higher job with a pay jump, goes to whoever ranks first among the candidates, not to everyone who clears a bar. That model explains why the pay difference between levels is often large and lumpy, rather than a smooth reward for each extra unit of output [@lazear1981]. Inside real firms, it is also a process of learning. In a classic study of twenty years of one company's personnel records, career moves reflected both what employees learned and what the *firm* learned about them; there were fast tracks, and pay varied a lot within a single level [@baker1994]. A promotion, in other words, is partly a contest and partly the organisation making up its mind about who you are.

How the decision is made varies with the size of the company. One practitioner account describes three stages: in small companies, managers meet and decide; as they grow, a semi-formal committee uses written expectations for each level and short write-ups from managers; at large technology companies, formal **promotion packets** (self-, peer- and manager reviews) go to **committees** of senior engineers and managers, who judge them against detailed job ladders [@orosz2019!]. That is one experienced observer's description rather than a study, but anyone who has sat on such a committee will recognise it.

And the ladder is not a checklist. When Dropbox published its engineering career framework, it said plainly that the framework "is not meant to be a promotion checklist" but a picture of what impact looks like at the next level [@todi2021!]. Another practitioner puts it more bluntly: "career ladders are a tool that applies better against populations than people" [@larson2020!]. The committee is not ticking boxes. It is forming a judgement, from a packet, about someone most of its members have barely met, much as the interview panel with a scoring sheet did in [[ch07.sec.structure]], except that this time the candidate is not in the room.

::: figure {#ch19.fig.room src="ch19/room.svg"}
Alt: A room with a table seen from above and a packet in the middle labelled "the packet". Around the table: Tomás, labelled "your manager: your advocate"; a plain figure labelled "a director from another squad"; another labelled "a senior engineer who's never met you"; and an empty seat drawn with a dashed outline, labelled "saw your work first-hand?". Outside the door, a small figure of Dev labelled "you: not invited", and beside her a note: "the packet: what changed, at what scope, who says so". A note at the bottom: "They know you through the packet, your manager, and anyone who has seen your work."

Inside the promotion room. Most people at the table know you only through the packet and your manager's summary. The dashed chair is the one you can do most about.
:::

That is the same room as the calibration meeting in [[ch18.sec.calibration]], with higher stakes. And it is the same machine as the hiring funnel in [[ch03]]: a limited number of slots, a panel that does not know you well, a decision made on a compressed sample of your work. A promotion case is a snapshot game played inside the building.

::: scene {slug="INT. A CAFÉ NEAR LANTERNFISH — SATURDAY, 11 AM"}
Meera has read the case on her phone, twice, while her tea went cold. Today's mug says ASK ME ABOUT CALIBRATION, and Dev, for once, does.

@meera: I sit on these committees. Twice a year I read forty packets in two days. Do you want to know what I'm actually asking when I read one?

@dev: Please.

@meera: Not "is she good?" Everyone in the pile is good, or their manager wouldn't have put them in it. I'm asking, "Is she already doing the next job, and who besides her manager says so?"

@dev: And mine?

@meera: Yours says you're an excellent engineer at your current level. Twenty-three times. The three things that might be senior work are buried at items nine, fourteen and twenty. I had to go looking for them, and the committee won't.

She scrolls to the end.

@meera: And Dev. Old Faithful is not a promotion case.
:::

Meera's account is experience, not evidence: one director's view of how committees read. But it fits the practitioner descriptions above, and it answers the pause.

## The best performer is not always promoted {#ch19.sec.peter}

Before getting to what makes a case work, it is worth knowing what committees and managers actually reward, because it is not quite what they say.

The best evidence comes from sales, where performance is easy to measure. Across 131 firms, companies promoted their best salespeople to manager, even though sales performance *negatively* predicted how well they would do as managers, while collaboration experience, which did predict managerial success, was not rewarded [@benson2019]. In the working-paper version of the study, doubling a worker's sales raised their chance of promotion by 14.3% relative to the base rate, and doubling a new manager's pre-promotion sales was associated with a 7.5% *fall* in each of their team members' sales [@benson2019]. Firms did weight sales less when the manager's job carried more responsibility, so they partly knew what they were doing.

There is also a statistical reason that needs no incompetence at all. People are promoted after a good run, and part of any good run is luck. So, on average, performance after a promotion falls a little even when the firm promotes sensibly, simply because the luck does not come too: regression to the mean [@lazear2004]. Some of what looks like the Peter Principle is the same effect that makes sequels disappoint.

::: myth {#ch19.myth.best-performer verdict=partly grade=strong} Promotions go to the best performer
Current performance is a large driver of promotion, so the claim is partly true: firms really do promote their top performers [@benson2019]. But "best at this job" is not "best for the next one". In sales data from 131 firms, top sellers were promoted even though sales performance predicted *worse* management, and collaboration, which predicted better management, was not rewarded [@benson2019]. Some apparent post-promotion decline is just luck running out [@lazear2004]. The popular Peter Principle, that people rise until they are incompetent, goes further than this evidence: firms promote the best doer rather than the best future manager, and partly correct for it.
:::

That finding matters in two directions. For the reader hoping to be promoted, it says current performance is still the biggest single input: being excellent at your job is necessary. For the reader who is being promoted *into management* because they are excellent at something else, it is a warning, and [[ch21]] is about exactly that fork.

::: coming {ref=ch21}
In [[ch21]], Rex is promoted to manager fast, and the gap between being good at one job and being ready for the next becomes very visible.
:::

## The case is a trailer {#ch19.sec.trailer}

Here is the idea this chapter has been building towards: **a promotion case is a trailer for an internal audience.** Everything Part I said about signals applies, unchanged.

::: flashback {ref=ch01.sec.signals}
In [[ch01.sec.signals|Chapter 1]], a signal carried information only if it was hard to fake for people who lacked the quality it advertised. Strong signals were specific, checkable and costly to fake. In [[ch05.sec.accuracy|Chapter 5]], the standard for paper was accuracy, not modesty.
:::

A committee reading a packet is in exactly the position of a hiring manager reading a résumé: strangers, short on time, predicting future performance from a compressed sample. So the same three tests decide whether a line in a promotion case carries weight. Is it **specific**: what changed, by how much, for whom? Is it **checkable**: is there an artefact, a number, a person the committee could ask? Is it **costly to fake**: would only someone working at the next level have been able to do it?

::: figure {#ch19.fig.trailer src="ch19/trailer.svg"}
Alt: Two columns side by side, headed "Part I: a résumé line" in coral and "Part III: a promotion-case line" in purple, with three rows. Specific: "Cut the test run from 6 hours to 40 minutes" beside "Made carriers testable for 3 squads: live in 2 weeks, not 6". Checkable: "Ask me how I parallelised it" beside "The harness, the dashboards, and two squad leads who use it". Costly to fake: "Only the person who did it survives the follow-up" beside "Work beyond my squad that others now depend on". A banner underneath reads "Same rules. Different audience."

The case as a trailer. The rules that made a résumé line strong in Part I make a promotion-case line strong in Part III. What changes is the audience, and the bar: the evidence has to show the next level, not the current one.
:::

Now the pause. Why might twenty-three good items be weaker than five? Three reasons, which are our reading of how committees work rather than a tested finding [!view].

**Volume is not scope.** Twenty-three examples of excellent work at your current level prove, very convincingly, that you are excellent at your current level. A committee asked "is she doing the next job?" learns nothing new from the twentieth. Published level frameworks describe what *impact* looks like at the next level [@todi2021!]; in our reading, that mostly means *scope* (whose problems you solve, how far your decisions reach) and *judgement*, not quantity.

**Weak items dilute strong ones.** Readers judge a list partly by its average. A coffee committee next to a cross-team design document does not add to the design document; it makes the reader wonder what else is filler. This is exactly how an over-stuffed résumé reads ([[ch05.sec.too-polished]]).

**Nobody else vouches.** A case that only you and your manager can confirm asks the committee to take two interested parties' word for it. That is the subject of the next section.

So a good case is a **cut**, not an archive. It makes one claim (I am already working at the next level), supports it with three or four of your strongest pieces of evidence at that level, names what is still missing, and points to people who have seen it.

### Credit, again {#ch19.sec.credit}

Most work at senior scope is shared, which makes credit the hardest part of a case to write honestly. Two pieces of research from earlier chapters apply with extra force. People in joint work recall their own contributions more easily and claim more responsibility than their partners would give them [@ross1979]. And audiences give women less credit for group work: among economists, women who co-authored more papers, especially with men, became less likely to get tenure, while men did not [@sarsons2021].

The case has to do what Dev did with Marcus in [[ch16.sec.credit]]: describe the team's goal, then exactly what you did, then what others did. Over-claiming is likely to be found out by the committee member who asks the other people involved [!view]. Under-claiming hands your evidence to someone else.

And there is a documented pull towards under-claiming. When asked to describe their own performance on a male-typed task, women rated themselves lower than equally performing men, even with nothing to gain from modesty [@exley2022]. Meanwhile self-promoters overestimate how much listeners enjoy it [@scopelliti2015], and in 1990s experiments, self-promotion raised women's perceived competence but cost them in likeability and hireability [@rudman1998]. That is a genuine bind, and no wording dissolves it. The best available answer is the one [[ch05.sec.accuracy]] gave: write what happened, at its true size, with the evidence attached, and let the evidence do the promoting. A checkable fact is harder to dismiss as bragging than an adjective.

:::: move {#ch19.move.case} Draft your case in five lines
Write a promotion case for your next level in exactly five lines:

1. **The claim**, in one sentence: what you are already doing that belongs to the next level.
2. **Evidence one**, your strongest example at that level: what changed, at what scope, with a checkable artefact.
3. **Evidence two**, a different kind of example (for instance, technical if the first was organisational).
4. **The gap**: the one thing the next level asks for that you have shown least, and what you are doing about it.
5. **Who can vouch**: two people, other than your manager, who have seen the work first-hand.

::: answer
Here is the case Dev eventually wrote, six months after the "not yet":

1. *For the last six months I have been leading testability across three squads, which is senior-level scope.*
2. *I designed the carrier-integration test harness now used by payments, rates and shipping; new carriers go live in about two weeks instead of six, with no launch incidents since (harness repo, release dashboard).*
3. *I wrote and ran the cross-squad design review that changed how we stub external APIs; four teams adopted the approach (design doc, review notes).*
4. *Gap: I have mentored one engineer formally. I am now pairing weekly with a new joiner on the shipping squad.*
5. *Can vouch: the shipping squad lead, and the engineering director, who reviewed the harness design.*

Notice what is not there: the coffee committee, the dozen good code reviews, the excellent work at her current level. All true, all left out. Notice too that line 4 *volunteers a weakness*. Committees look for gaps anyway; naming yours, with a plan, shows the judgement the next level asks for and removes the surprise [!view].

If you cannot fill line 1 honestly, that is the most useful result this exercise can give you. It means the next step is not a better case but different work, and your manager is the person to ask for it.
:::
::::

## The ledger, spent {#ch19.sec.ledger}

Line 5 of that case is not decoration. It is where Part II pays out.

::: flashback {ref=ch10.sec.ledger}
In [[ch10.sec.ledger|Chapter 10]], every working relationship kept a trust ledger: small deposits, heavier withdrawals, and a balance that would be spent later, "in a promotion meeting you are not invited to".
:::

This is that meeting. When Tomás tells a committee "I've watched her work for two years, and she is already doing this job", he is doing what a referrer does when they tell a hiring manager "you need to meet this person" ([[ch06.sec.why]]). He is spending his own reputation on yours. If he is right, his judgement gains credit in that room. If he is wrong, it is *his* withdrawal, and the committee will remember it the next time he argues for someone.

That is the core of what people mean by a **sponsor**. A mentor gives you advice; a sponsor uses their own standing to advocate for you, in rooms you are not in. The distinction comes from practitioner writing, which argued that high-potential women were over-mentored and under-sponsored [@ibarra2010]. It is useful, but it is worth being honest about the evidence underneath it.

**Mentoring** has been studied a great deal, and its measured effects on objective career outcomes such as pay and promotion are small; the effects on how people feel about their careers are larger [@allen2004; @eby2008]. A meta-analysis of career success found that sponsorship from the organisation related more strongly to career *satisfaction* than to salary and promotion, which went more with human capital and demographics [@ng2005]. A large industry survey of US and Canadian companies found that 31% of entry-level women said they had a sponsor, against 45% of men [@leanin2025!]; that survey is run by an advocacy organisation with a consulting partner, and its companies select themselves. We found no peer-reviewed study that estimates how much sponsorship *causes* promotion. Popular percentages exist; we could not verify them, so we leave them out.

What *is* well documented are the mechanisms a sponsor works through: advocacy in calibration and committees ([[ch18.sec.calibration]]), first-hand exposure of decision-makers to your work, and judgements of "potential", which the next section shows matter a great deal. So treat sponsorship as plausible and important, not proven, and notice that the useful kind is not someone who likes you. It is someone with standing who has *seen* your work, and has seen enough of it to be willing to stake their judgement.

::: figure {#ch19.fig.ledger-spent src="ch19/ledger-spent.svg"}
Alt: At the top, a ledger page headed "What Tomás has seen, two years", with teal deposits: "warned me early, every time since Northwind", "found the race condition on a Saturday", "stopped a bad release, with evidence", "harness now used by three squads", "fixed the credit record, calmly". An arrow labelled "spent in the room" runs down to Tomás, at the committee table, saying "I'll stake my judgement on this." Below him, a smaller ledger headed "Tomás's own ledger with the committee" shows two possible entries: a teal "if he's right: his judgement gains credit" and a coral "if he's wrong: his withdrawal, not hers". A note: "Illustrative, not a formula."

The trust ledger, spent. A sponsor can only spend what you deposited where they could see it, and every time they vouch for you, they are betting their own ledger.
:::

For Dev, the ledger got spent the Monday after the "not yet", and it started with Tomás changing her work rather than her case.

::: scene {slug="INT. LANTERNFISH, TOMÁS'S OFFICE — MONDAY, 9:30 AM"}
Tomás has a whiteboard behind him with three squad names on it and a lot of arrows.

@tomas: I've been thinking about Friday. The committee wasn't wrong. Your best work is real, but it's all inside the squad, and the only people who've seen it are me and Kai.

@dev: So what do I do, get louder?

@tomas: No. Bigger. Every squad that adds a carrier rebuilds the same fragile test setup. You already fixed it for ours. I want you to fix it for all three, and I want the shipping squad lead and the director to see you do it. Present the design at the cross-squad review. Ask the director to review it; she'll say yes.

@dev: And if it doesn't work?

@tomas: Then we'll know, and so will I. Next round, I'm putting my name on this case, properly. I'd rather do that with a case I can say in one sentence.
:::

Notice what Tomás did and did not do. He did not promise a promotion. He changed the *work*, so that it would produce evidence at the next level's scope, and he arranged for two more people with standing to see it first-hand. That is sponsorship as a practice rather than a feeling, and it is mostly about exposure and scope, not praise [!view].

:::: move {#ch19.move.sponsor} Find your sponsor (and be one)
1. List up to five people with standing in your organisation (two levels up, or senior in a neighbouring team) who influence promotions, and next to each, write what they have **seen first-hand** of your work in the last six months. Be strict: "heard about" does not count.
2. Pick one name with a blank or thin entry. Write one concrete way they could see your work directly in the next quarter: a design review, a demo, a problem of theirs you could help with.
3. Now reverse it. Name one person more junior than you whose work you have seen first-hand and rate highly. Write one sentence you could say about them, specifically, in a room they are not in.

::: answer
Most people find that step 1 is sobering: plenty of senior people *know who you are*, very few have *seen your work*. That is the gap a sponsor fills, and it is why a sponsor cannot be recruited with a coffee. They have to be given something real to see.

Good step-2 answers are about *their* problems, not your visibility: "the director worries about launch incidents; ask her to review the harness design" is better than "present at the all-hands". The first gives her first-hand evidence about something she cares about; the second is performance.

Step 3 is not charity. Sponsoring someone is a deposit in your own ledger, it builds the judgement committees value at senior levels, and it corrects the imbalance that leaves some people over-mentored and under-sponsored [@ibarra2010]. The sentence should be as specific as a résumé line: "She rebuilt our on-call rota and halved weekend pages" beats "she's great".
:::
::::

## Potential, and who gets seen {#ch19.sec.potential}

So far: performance matters most, the case must show the next level, and someone with standing must vouch. The rest of the evidence on promotion is about the inputs that are not quite performance, and they are where the decision is least fair.

::: receipts {source=benson2026} "Potential" and the gender promotion gap
**What they did.** Benson, Li and Shue studied personnel data from a large North American retailer, where managers rated management-track employees on a "Nine Box" grid of current performance against future *potential*, and those ratings fed promotion decisions [@benson2026].

**What they found.** Women received *higher* performance ratings than men but substantially *lower* potential ratings, and the potential gap explained about half of the gender gap in promotions. Women then outperformed men who had been given the same potential rating, which suggests that their potential had been underestimated. In the working-paper version, men's annual promotion rate was 12.6% against 11.0% for women, and moving up one step on the potential scale raised the chance of promotion by about nine percentage points, more than the equivalent step in performance.

**What it cannot tell you.** It is one firm, in retail, and the precise numbers come from the working paper rather than the published article. It shows that potential ratings were lower than later performance justified; it cannot say exactly why managers judged as they did.
:::

That study fits a wider pattern. The meta-analysis from [[ch18.sec.bias]] found field ratings of performance slightly favouring women, but ratings of promotion potential favouring men [@roth2012]. "Potential" is a forecast, made with little evidence, about how someone will perform in a job they have not yet done. It is exactly the kind of judgement where stereotypes have the most room.

**Face time** is the other input. Using the quasi-random rotation of managers at a large commercial bank in Southeast Asia, Cullen and Perez-Truglia found that employees who got more face-to-face interaction with their manager were promoted faster, a mechanism that could explain about a third of the firm's gender gap in promotions [@cullen2023b]. Their most memorable finding, from the working paper, is about smoking breaks: smokers newly assigned to a manager who smoked gained 0.70 pay grades more over the next ten quarters, a gain that non-smokers did not see [@cullen2023b]. Nobody's job was to smoke. The smoking break was simply where the manager got to know people. The same working paper found that men moved from a female to a male manager rose 0.60 pay grades more, about 14.6% in salary, than men moved to another female manager [@cullen2023b]. That is the "like me" drift that [[ch07.sec.fit]] found in hiring, operating inside the building: similarity buys time together, and time together buys advancement.

Remote work shows the same mechanism from the other side. Call-centre staff randomly assigned to work from home performed better but were promoted less, given their performance [@bloom2015]; in a later trial, two days a week at home showed no promotion penalty [@bloom2024]. [[ch14.sec.remote]] discussed what that means for your working pattern; here the point is narrower. Promotion decisions lean on what decision-makers have seen, and they see some people more than others, for reasons that have little to do with the work.

Put those findings together and one of the most comforting pieces of career advice needs a qualification.

::: myth {#ch19.myth.great-work verdict=partly grade=strong} Do great work and promotion will follow
Great work is the biggest single input: firms promote on current performance [@benson2019]. But it is not the only one, and the others are not neutral. Judgements of "potential" explained about half of one large retailer's gender promotion gap [@benson2026]; more face time with the manager sped promotion at a large financial firm [@cullen2023b]; randomly assigned home workers were promoted less, given their performance [@bloom2015]; and women are asked more often than men to take on tasks that do little for promotion [@babcock2017]. Great work is necessary. Whether it is seen, by whom, and how it is judged decides much of the rest.
:::


The cumulative result shows up at the very first rung. In the 2025 edition of one large industry survey, for every 100 men promoted from entry level to manager, 93 women were, the eleventh year of what its authors call the "broken rung" [@leanin2025!]. That report covers self-selected US and Canadian companies, is published by an advocacy organisation, and changes every year, so treat the number as an indication, not a law.

::: craft {by=author} Legible, not loud
None of this means you should start taking smoking breaks, or that the cure for being under-seen is to perform yourself louder. We think the honest response has two parts.

For you: make sure the people who will judge your potential have **direct evidence** of your work, not just your manager's summary of it, by doing some visible work of the next level (a design review, a cross-team problem, a demo to people outside your squad). That is translation, the Part I skill: making real value legible to the audience that has to judge it. It is not self-promotion, because it adds nothing that is not there.

For anyone who rates "potential", which will one day include you: ask what *evidence* the rating rests on. If the answer is a feeling, the evidence in this section suggests that is exactly where bias lives. Rate potential from what people have done, and give people the chance to do it.
:::

## Glue work, and the coffee machine {#ch19.sec.glue}

Back to Meera's line. Why isn't Old Faithful a promotion case, when Dev's handling of the coffee committee showed real political skill ([[ch16.sec.committee]])?

[[ch17.sec.helping]] introduced the problem: some helpful work holds a team together and does little for the career of the person doing it. In field and laboratory studies, women were asked more often than men to do these **low-promotability tasks**, and accepted more often, driven by a shared expectation that women would say yes [@babcock2017]. The engineer Tanya Reilly, whose talk named this kind of thing **glue work** (onboarding, noticing dropped work, reviewing designs, keeping a team pointed the same way), makes the distinction that matters here: managed deliberately, she argues, glue work "demonstrates and builds strong technical leadership skills"; left unconscious, "it can be career limiting" [@reilly2026!]. That is a practitioner's argument, not a study. But it gives a usable test [!view]:

- Glue work **counts** when it operates at the next level's scope, changes something others depend on, and can be evidenced. Dev's onboarding sessions would count if she had redesigned onboarding across teams and cut new testers' ramp-up time, measurably.
- Glue work **does not count** when it is maintenance at the current scope, no matter how much it helps. Keeping a coffee machine alive helps forty people every morning, and tells a promotion committee nothing about whether you can do a senior engineer's job.

The coffee committee was good politics and a real deposit in several ledgers. It belongs in the long game, where it earned Dev goodwill. It does not belong in the career game's evidence, where it made the reader wonder about the other twenty-two items.

:::: move {#ch19.move.glue} Audit your week for glue work
Take last week's calendar and task list. Put every item that took more than half an hour into one of four boxes:

1. **Core work** your role is judged on.
2. **Promotable glue**: coordinating or helping work at the next level's scope, with an outcome you could evidence.
3. **Necessary glue**: work that matters to the team but will never count for you.
4. **Drift**: things you do because you once did them.

Then, for every item in boxes 3 and 4, write one of: *keep* (and say why), *share* (with whom), *hand over* (to whom, with what written down), or *stop*.

::: answer
Two patterns show up in almost every audit.

- **Box 3 is real and should not be zero.** Teams need it done, and doing your share is part of the long game ([[ch10]]). The question is whether *your share* has quietly become *everyone's share*. If one person holds most of a team's necessary glue, that is a team problem worth raising with the manager, not a personal virtue, especially given the evidence on who gets asked [@babcock2017].
- **Box 4 is where the hours hide.** Dev's audit found two recurring meetings she no longer needed to attend and a code-review rota she had volunteered for in her first month. Old Faithful, at least, was already gone, handed over the way [[ch17.sec.helping]] suggested: written down, with a real owner. "Hand over, with what written down" is the usual answer for box 4 too.

The most valuable move is often to promote an item from box 3 to box 2: take the onboarding you already run and make it a cross-team improvement with a measurable result. Same care, larger scope, and now it is evidence.
:::
::::

## Inside, or outside? {#ch19.sec.inside}

A deferred promotion is a natural moment to wonder whether you would be valued more elsewhere. Sometimes you would. The strongest evidence we found on internal promotion versus external hiring is the investment-bank study from [[ch02.sec.ask]]: workers promoted into a job performed significantly better for their first two years than external hires into similar jobs, and were less likely to leave or be let go, yet the external hires were paid around 18% more and, if they stayed, were promoted faster [@bidwell2011]. The inside path pays less up front but starts faster, because you already know the systems and the people; the outside path pays more, and you are judged harder.

That trade-off is real at every promotion decision, and [[ch02]] gave the tools for weighing it. Two cautions apply when the comparison is "a promotion here" against "a better title there". First, titles are partly a currency. In the United States, firms show a sharp jump in the number of jobs titled "manager" just above the salary threshold at which overtime pay stops being required ($455 a week in the period studied), concentrated in retail, food service and hotels [@cohen2023]; [[ch21]] has more on title inflation. Compare scope, level and pay, not the words on the door. Second, the money at promotion is worth asking about directly. Pay jumps between levels are the tournament's prizes [@lazear1981], but pay also varies a lot *within* a level [@baker1994], so "promoted" can mean the bottom of the new band. The habits from [[ch09.sec.dev-negotiates]] carry over almost unchanged: find out the range for the new level, decide in advance what you would be pleased with, and make one well-founded ask. So does the warning in [[ch09.sec.not-free]], that asking is not equally free for everyone; the cleanest fix, a published range for every level, is one only the organisation can make [!view].

::: field {regions="Japan, US"} Promotion clocks and promotion contests
Most of the evidence in this chapter comes from US firms, with a few from elsewhere (Britain, China and Southeast Asia among them), and almost all of it from workplaces where promotion is a contest. Some systems run partly on a clock. Japan's hallmark practices, seniority-based pay and lifetime employment, have been eroding: in official wage-survey data, the age-wage profile has flattened, and fewer young university graduates stay with one employer [@hamaaki2012]. In up-or-out systems, such as law-firm partnership or academic tenure, you are promoted by a deadline or you leave, an arrangement economists explain as a commitment device that protects both sides [@kahn1988].

We did not find verified evidence on promotion practices or title inflation in India, or current figures on seniority pay elsewhere in Asia, so we do not describe them here.
:::

A deferred promotion raises a few questions that people rarely ask out loud.

::: ask
Q: Should I get an outside offer to force a promotion?

A: It sometimes works, and the evidence that outsiders are paid more [@bidwell2011] means the comparison is real. But it is a one-shot move in a repeated game. Use it only if you would genuinely take the offer, because a bluff that gets called costs you the offer *and* some trust. [[ch09.sec.counter]] covers counter-offers from the other side.

Q: Isn't sponsorship just favouritism with a nicer name?

A: It can be, which is why the useful test is evidence. A sponsor who argues from first-hand knowledge of your work is giving the committee information it lacks. A sponsor who argues from liking you is adding noise. The cure for favouritism is not to abolish advocacy; it is to make sure more people, and more kinds of people, get the exposure that lets someone vouch for them.

Q: My manager won't sponsor me. What now?

A: Ask directly what evidence they would need. If the answer is vague, find the evidence a different way: work that brings you into contact with other senior people, and a skip-level conversation about what the next level looks like. If, after a cycle or two, nobody with standing has seen your work and your manager will not help, that is a real push reason, and the outside path may simply be the faster one ([[ch02]]).
:::

## Six months later {#ch19.sec.later}

The autumn round came. Dev's case was five lines long, and it was the one from [[ch19.move.case]].

::: scene {slug="INT. LANTERNFISH, TOMÁS'S OFFICE — TUESDAY, 11 AM"}
Not a Friday, Dev notices.

@tomas: You're promoted. Senior engineer, from next month.

@dev: What happened in the room?

@tomas: I read your first line, and then I didn't have to say much. The director said she'd reviewed the harness design and that three squads use it. The shipping lead had written a peer statement that was better than mine. Someone asked about mentoring, and I pointed at line four. It took eleven minutes.

@dev: And the coffee machine?

@tomas: Not mentioned. By anyone. Congratulations.
:::

That evening Dev opens the *Promotion case* tab one more time. The first version, with its twenty-three rows, is still there, and she does not delete it. Then she texts Meera.

@meera: Congratulations. Enjoy it this week. Then go and do the job you just got.

Meera's advice is wiser than it sounds. In panel data, promotions raised job satisfaction and perceptions of pay and security in the short term, but had negligible effects on health and happiness, and mental health had worsened two years after promotion [@johnston2013]. A British study found that healthier people are the ones who get promoted, rather than promotion making people healthier, and that psychological well-being tended to decline afterwards [@boyce2012]. Those are averages, and they are not a reason to turn a promotion down. They are a reason to want it for what the job *is*: the scope, the problems, the pay. The feeling will fade; the work will not.

Dev's promotion was not really won in the committee room. It was won in the six months before it, by changing the work she did and who saw it. And the work itself, making three squads' systems testable, turns out to be something bigger than a promotion case. In [[ch20]] it becomes a skill that compounds, and the question changes from "how do I get to the next level?" to "what should I get good at?"

::: rewind
- A promotion asks a different question from a review: **are you already doing the next job, and who besides your manager says so?**
- Promotions work like **tournaments**, decided by committees that know you mostly through a **packet** and your manager. Level guides describe the next level; they are not checklists.
- Firms tend to promote the **best doer**, not the best future manager, and some post-promotion slump is regression to the mean. The Peter Principle in its popular form goes further than the evidence.
- **The case is a trailer**: Part I's rules (specific, checkable, costly to fake) apply unchanged. Make it a cut, not an archive: one claim, a few pieces of next-level evidence, an honest gap, and people who can vouch.
- **Sponsors spend their own trust on yours.** The causal evidence for sponsorship is thinner than practitioner books suggest, but its mechanisms (advocacy, exposure, "potential") are well documented. A sponsor needs to have *seen* your work.
- **"Potential" and face time** are where promotion is least fair: in one large retailer, potential ratings explained about half of the gender promotion gap, and exposure to the decision-maker speeds promotion. Great work is necessary, not sufficient. Make your work legible to the people who judge it, and rate others' potential from evidence.
- **Glue work counts** when it operates at the next level's scope and can be evidenced; maintenance does not, however helpful. Old Faithful is not a promotion case.
- Internal promotees tend to **perform better early but are paid less** than external hires. Compare scope, level and pay, not titles, and do not expect a promotion to make you happier for long.
:::

::: further {ref=more.sec.pay-data}
This chapter did not cover what the next level actually pays in your market. Pay bands vary a great deal within a level, and [[more.sec.pay-data]] explains which kinds of salary data hold up and how to read them before you negotiate an internal offer.
:::
