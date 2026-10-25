---
id: ch21
status: review
---

::: scene {slug="INT. LANTERNFISH, TOMÁS'S OFFICE — TUESDAY, 9:30 AM"}
Tomás has drawn a box on the whiteboard and written RELIABILITY SQUAD inside it. Under the box are five short lines, one for each engineer, and above it one longer line with nothing on it.

@tomas: We're splitting the platform team. The new squad owns testability, release safety and the on-call tooling, which is mostly the work you've been doing anyway. I'd like you to lead it.

@dev: Lead it as in tech lead? Or lead it as in one-to-ones?

@tomas: As in one-to-ones. Five people. You'd hire the sixth. You'd still be in the code a bit, at first.

@dev: Is it a promotion?

@tomas: The pay goes up a little. The job changes a lot. That's the honest answer.

Dev looks at the empty line above the box. Six months ago, after a year of building the case, she was promoted to senior engineer. This is the first offer in her working life that she did not have to ask for, and her first feeling, to her surprise, is not delight. It is something closer to *wait*.

@dev: Can I have a week?

@tomas: Take two. And talk to Kai. Kai will tell you what I won't.

On her way out she passes the integrations team's corner. Rex, who has been managing it for four months, has a new line on his profile and a new sign on his desk: HEAD OF ENGINEERING EXCELLENCE. Two of his five engineers have booked time with Tomás this week. Nobody has said why.
:::

Most careers reach a fork like this one, often earlier than people expect and rarely at a convenient moment. Down one road you keep doing the work yourself, and get better and broader at it. Down the other you stop doing much of the work yourself and start doing it *through other people*. Organisations tend to present the second road as the obvious next rung. It isn't, and this chapter is about why, and about how to choose.

It is not a management manual. How to manage people well is a book of its own, and [[more.sec.managing]] points to good ones. This chapter is about the decision: what the job actually is, who tends to be good at it, what the other road looks like, why you might want it, and how to try it without betting your career on a guess.

::: pause
Before you read on, write down the three best reasons you can think of for becoming a manager: yours, if you are facing the choice, or the ones people usually give. Keep the list. Later in the chapter you will sort it, and you may be surprised which reasons survive.
:::

## A fork, not a ladder {#ch21.sec.fork}

Here is the first thing to get straight, because almost everything else follows from it: **managing people is a different job, not a higher grade of the same one.**

That sounds obvious when it is written down, and it is routinely forgotten in practice. One experienced engineering leader puts it bluntly: management "is not a promotion" but "a change of profession" [@majors2017!]. That is a practitioner's opinion, but it describes the work accurately. A senior engineer is judged on what they build and how well. A manager is judged on what their *team* builds, whether the people on it grow and stay, and whether the right people get hired. The inputs, the outputs and the feedback loops all change at once.

So why does it look like a ladder? Partly because pay and status rise when you take it, and partly because many organisations offer no other way up. In the practitioner research on senior engineering roles, some companies had no technical-leadership track at all and pushed experienced engineers into management [@larson2020!]. Even where a "dual ladder" exists, with a technical route and a managerial route that are supposed to be equal, the research is cautious. A study of nearly 1,500 engineers and scientists in nine US organisations questioned whether dual ladders deliver what they promise, and found that as engineers got older their preferences shifted towards interesting technical work rather than advancement on either ladder [@allen1986]. And a study of one research and development organisation found that the ladder you climb is steered by the person you report to: people whose supervisors had been promoted on the technical ladder were more likely to be promoted technically themselves [@katz1995].

Those are old studies of particular labs, so treat them as a warning rather than a measurement. The warning is that a dual ladder on paper is not always a dual ladder in practice [!view]. Before you choose a road, find out whether it actually goes anywhere where you work.

::: figure {#ch21.fig.fork src="ch21/fork.svg"}
Alt: A road rises from Dev, labelled "senior engineer", and splits in two. The left road, purple, is "the manager track", with stops at "team lead", "engineering manager" and "director"; a purple box beside it reads "judged on: your team's results, whether people grow and stay, who you hire". The right road, teal, is "the expert track", with stops at "staff engineer" and "principal engineer"; a teal box reads "judged on: technical impact, at ever wider scope". Two dashed arrows cross between the roads in both directions, labelled "the pendulum: people do switch back and forth". A gold sign at the bottom reads "first, check both roads exist where you work".

The fork. Both roads lead somewhere senior, by different routes and judged on different things. The dashed crossings are the part most people do not know about: the choice is often more reversible than it looks.
:::

## What managing actually is {#ch21.sec.job}

If you want to know whether you would like a job, the first question is what you would actually be doing all day. For management, the answer is less glamorous and more interesting than the title suggests.

The best-known attempt to pin it down inside a technology company came from Google. Its people-analytics team, faced with engineers who doubted managers did much, set out to test the question, and in the words of the project's co-lead "ended up trying to prove the opposite case---that managers don't matter. Luckily, we failed" [@garvin2013!]. In its data, teams with high-scoring managers had less turnover, and retention was related more strongly to manager quality than to seniority, performance, tenure or promotions. The behaviours its best managers shared were mostly unglamorous: developing and motivating the people who report to them, communicating strategy, removing roadblocks, giving useful feedback regularly and making team goals clear [@garvin2013]. One manager it quotes says he spends "a third to half" of his time looking for ways to help his team grow. That is one company describing its own internal research in a business magazine, so it is weak evidence. But a stronger study points the same way.

::: receipts {source=hoffman2021} People management is a real skill, and it shows up in who stays
**What they did.** Mitchell Hoffman and Steven Tadelis used personnel data from a large high-tech firm, where employees answered surveys about their managers' interpersonal skills with their teams, which the authors call *people management skills*. To get closer to cause and effect than a simple correlation, they looked at what happened to new workers joining a team and to workers who switched managers [@hoffman2021].

**What they found.** Managers with better people management skills had markedly lower turnover on their teams, and the research designs support a causal reading. The skills did not consistently improve most other outcomes the firm measured. And the firm noticed: better people managers themselves received higher performance ratings, more promotions and larger pay rises [@hoffman2021].

**What it cannot tell you.** It is one company, the skills are measured by the people being managed, and attrition is only one outcome, if an expensive one. It does not tell you whether *you* would be good at it, only that being good at it is a measurable, rewarded skill, distinct from being good at the work.
:::

Put those together and you get a picture of the job that rarely appears in a job description. Managing is mostly about other people's work: whether they know what matters, whether they are stuck, whether they are growing, whether they are about to quit, whether the team needs someone it has not hired yet. Your own output becomes something you produce in the gaps.

It also changes the shape of your day, which matters more than people expect. The programmer and investor Paul Graham described two kinds of schedule: the *manager's schedule*, where the day is cut into one-hour slots and you change what you are doing every hour, and the *maker's schedule*, where you need half a day at a time to do anything hard, and a single meeting "can blow a whole afternoon" [@graham2009!]. That is an essay, not a study, but anyone who has done both will recognise it. The manager's job is built from the one-hour slots. You cannot keep the maker's schedule and do it well.

::: figure {#ch21.fig.week src="ch21/week.svg"}
Alt: Two weekly calendars side by side, Monday to Friday, nine to five, labelled "illustrative calendars, not data". The left calendar, "Dev, senior engineer", is mostly long teal blocks marked "build", with a short grey stand-up each morning, one planning meeting and one review. The right calendar, "Kai, squad lead", is broken into many small blocks: one-to-ones, "plan", "hire", "road(map)", "help (unblock)", "upset (someone is)", meetings, and a few white blocks marked "mine (own work)", one of which, on Thursday, is crossed out. Under the calendars: "the job is in the small boxes".

The same week, two jobs. The calendars are invented, but the shapes follow the maker's and manager's schedules. Managing is not the left calendar with extra meetings; it is a different calendar.
:::

There is evidence that this trade-off starts even before anyone has the title. In a study of software engineers at a large US firm, sitting near teammates increased feedback on code, with the gains concentrated among junior engineers, while the senior engineers wrote less code: a direct trade between mentoring and output [@emanuel2026]. Every senior person who has spent an afternoon unblocking a colleague has felt this. Management makes it the whole job.

::: scene {slug="INT. THE NOODLE BAR — THURSDAY, 8 PM"}
Kai has been a squad lead for nearly two years, and has the look of someone asked to review a film they are still in.

@kai: What do I actually do? Okay. Monday I had five one-to-ones. One was about a promotion case, one was about a sick parent, and one was a designer telling me the roadmap is wrong, which it is. Tuesday I interviewed two people and rejected one of them, which I'll think about until Saturday.

@dev: When do you design?

@kai: I design on Fridays, if nobody's upset. Somebody is usually upset.

@dev: That sounds awful.

@kai: Some weeks it is. But last month someone I hired as a junior shipped the onboarding redesign on her own, and I didn't touch a single screen. Best thing I've made all year, and I didn't make it.

@dev: Would you do it again?

@kai: Yes. But I'd want someone to have told me that I'd be bad at it for the first six months, and that the being-bad was normal.

Dev writes *bad at it for six months, normal* on a napkin, and then, because it is Thursday and the rules are the rules, puts it in her pocket and changes the subject.
:::

Kai can say all of this over noodles because it is about the job, not about anyone in it.

::: flashback {ref=ch15.sec.promotion}
When Kai first became Dev's lead, the two of them wrote down their rules on a sticky note: TUESDAYS = LEAD, THURSDAYS = NOODLES. Kai is still keeping them. Asking a friend what the job is like, over noodles, is fine; asking about anyone's review is not.
:::

## Who turns out to be good at it {#ch21.sec.who}

If managing is a different job, being excellent at the old one should not, on its own, predict being excellent at the new one. The evidence says it doesn't, and sometimes the relationship runs the wrong way.

Remember the study from [[ch01.sec.career-game]]. Across sales workers in 131 firms, companies promoted their best salespeople into management, even though better sales performance before promotion predicted *worse* performance as a manager [@benson2019]. What did predict success as a manager was a history of collaborating with colleagues, and firms did not reward it with promotion. In the working-paper version of the study, salespeople who had never collaborated, the "lone wolves", did particularly badly as managers [@benson2019]. This is the pattern the Peter Principle describes, measured in real personnel data.

Two cautions keep it honest. First, some of the slump after any promotion is simple statistics: people are promoted after a good run, part of every good run is luck, and luck does not get promoted with you, so average performance falls even when the organisation promotes sensibly [@lazear2004]. Second, technical skill is not irrelevant. In US and British survey data, a boss's technical competence was the single strongest predictor of workers' job satisfaction, and workers' well-being rose when their boss became more competent [@artz2017]. Both findings can be true at once: people want a manager who *could* do their job, but the *best* person at the job is not automatically the best person to manage it [!view].

The transition is also learnable, and it goes faster with help. A study that followed 110 new first-line leaders over about ten months found that they learned their role faster when their own manager both showed them good leadership and explained the job, and that the effect was strongest for people who had never worked for an exceptional leader themselves [@dragoni2014]. If you are offered the role, one of the best predictors you can check in advance is whether the person offering it will show you and tell you.

::: myth {#ch21.myth.sixty verdict=busted grade=weak} 60% of new managers fail in their first two years
This statistic is everywhere in management training, usually credited to research by CEB (now Gartner). Our researchers could find it only on secondary pages, such as training vendors' sites, with wording that varies between "fail" and "underperform", and could not trace a primary report or method. Without one, we cannot tell what "fail" meant, who was counted or when. What the evidence we could check does support is less dramatic and more useful: the transition is hard, the best performers are not reliably the best managers [@benson2019], and new leaders learn the role faster when their own manager models it and explains it [@dragoni2014]. The practitioner research on new managers says most initially struggle because of misconceptions about what being in charge means [@hill2007!], which is a reason to get help, not a percentage.
:::

### Rex, promoted {#ch21.sec.rex}

Which brings us to Rex, who has been a manager for four months and is having a harder time than his new sign suggests.

He got the job for real reasons. He is warm, persuasive and well connected; he can sell a plan to a room; and in [[ch16]] Dev watched him read people better than almost anyone at Lanternfish. Those things matter in management. What he never had to do, in eight years of moving on every year or so, was the slow part of the long game: following through, week after week, on things nobody is watching. His team has noticed. One-to-ones move when something more exciting comes up. Promises made in planning do not always survive to the sprint. He champions his engineers' ideas brilliantly in meetings and forgets to tell them what happened afterwards.

None of this makes Rex a bad person, and none of it is unusual. It is a gentle version of exactly what the evidence predicts: an organisation promoted someone for the most visible things he did well, and the job turned out to be made of the things he did least [!view]. The snapshot game got Rex into management. The long game is what management mostly is.

## The other road: senior, staff, principal {#ch21.sec.expert}

If management is not the only way up, what is the other way? In many technology companies it is a set of senior individual-contributor levels, usually called something like *staff* and *principal* engineer. The practitioner literature is the best guide we have here, because the research has not caught up.

Will Larson's interviews with engineers at these levels found four common shapes of the job: the **Tech Lead**, who guides the approach and execution of a team and is the most common (in his estimate, roughly one per eight engineers); the **Architect**, responsible for the direction and quality of a critical area; the **Solver**, who goes deep on one hard problem after another; and the **Right Hand**, who extends an executive's attention, borrowing their scope and authority [@larson2020!]. What they share is *scope*: the expert track does not mean doing the same work more expertly forever. It means having technical judgement that changes more of the organisation's outcomes, often through influence rather than authority. That is why levels frameworks describe impact at each level rather than tasks. Dropbox, publishing its own, stressed that it "is not meant to be a promotion checklist" [@todi2021!], and Larson's line that career ladders "apply better against populations than people" is worth remembering whichever road you take [@larson2020].

Does the expert road pay? In US official statistics for May 2025, the median annual wage was $135,980 for software developers and $175,140 for computer and information systems managers, an occupation that typically asks for five or more years of related experience [@bls2026a; @bls2026b]. Those are medians of two whole occupations, not the same person on two tracks, and senior individual contributors at large technology firms can earn more than many managers. But the general direction is clear and worth saying plainly: in most places, management pays more at the median.

::: myth {#ch21.myth.only-way verdict=partly grade=moderate} Management is the only way up
It depends heavily on where you work. Managers do earn more at the median in US data [@bls2026a; @bls2026b], and some companies have no senior technical track at all [@larson2020]. But dual ladders exist, if unevenly, and the ladder you climb is partly steered by who you report to [@katz1995]. Engineers' own preferences shift with age towards interesting technical work rather than advancement on either ladder [@allen1986]. And the evidence that "up" makes you happier is weak: promotions in general raise pay and job satisfaction briefly, with negligible effects on health and happiness, and mental health was worse two years later in one large panel study [@johnston2013; @boyce2012]. Management is one way up, often the best-paid one. Whether it is the only one is a fact about your employer, which you can check.
:::

While you are checking, look at what the titles on each road actually mean, because a title is not always what it seems.

::: field {regions="US, UK"} When "manager" is just a word
Titles are partly a currency, and some employers pay in them. In the US, salaried workers must earn above a threshold to be exempt from overtime pay, and researchers found a sharp jump in "manager" job titles for salaried jobs paid just above that threshold, with no such jump elsewhere; the practice was more than 50% more common where state worker protections were weaker, and concentrated in retail, food service, cleaning and hotels [@cohen2023]. In the UK, a think tank reported that the share of retail "managers" earning under £400 a week rose from 37% to nearly 60% during the 2000s [@resolution2012!].

So when you compare a management offer, inside or outside your company, compare scope, level and pay, not the title [!view]. We did not find verified data on title or "designation" inflation in India or elsewhere in the EU, so we have not guessed; the same check applies everywhere.
:::

## Why do you want it? {#ch21.sec.why}

Now go back to the list you wrote at the start of the chapter. Of everything in this decision, your reasons are the part you know best and examine least.

Psychologists who study leadership have a useful frame for this. Kim-Yin Chan and Fritz Drasgow proposed that *motivation to lead* comes in three distinct types [@chan2001]: **affective-identity** motivation, the extent to which you enjoy leading others and see yourself as a leader; **social-normative** motivation, the extent to which you treat leadership as a responsibility or duty; and **non-calculative** motivation, the extent to which you are drawn to leading even when it costs you or brings you little personal benefit [@kennedy2021]. A meta-analysis of 100 studies found that the three types are only modestly related to each other, and that each is generally associated with emerging as a leader, leading in better ways and performing more effectively in leadership roles [@badura2020].

Notice what is *not* on that list: wanting the title, the pay or the status. Those are perfectly legitimate things to want, and you should be honest that you want them. But they are not what the research links to doing the job well, and on two of them the evidence about what you will actually get is sobering. Promotions in general have negligible effects on happiness and health [@johnston2013], and promoted British workers showed worse psychological well-being afterwards [@boyce2012]. On the other side of the ledger, status is stickier than money: in German panel data, people adapted to income gains within about four years but did not adapt to gains in status [@ditella2010]. So the title will keep feeling good. Whether the job does is a separate question.

::: scene {slug="EXT. A PARK NEAR MEERA'S HOUSE — SATURDAY, 11 AM"}
Meera has brought coffee in a flask and her own mug, as always. Today it says WORLD'S OKAYEST MANAGER.

@dev: Is that a joke?

@meera: It's a goal. My first team gave it to me after a year. It was the nicest thing anyone had said about my management up to that point, and they were right.

@dev: Why did you do it? The first time.

@meera: Honestly? Because it was the next box on the chart, and because I wanted to be in the room where decisions got made. Neither of those is a reason to manage people. They're reasons to want a title.

@dev: So what's a good reason?

@meera: You get a kick out of other people getting better. You'd rather fix why the team is stuck than fix the bug yourself. And you can stand being interrupted. If you have the first two and can learn the third, try it. If you only have the reasons I had, you'll spend years learning the other two the hard way.

@dev: Did you learn them?

@meera: Mostly. Look at the mug.
:::

Meera's test is experience, not evidence, but notice how closely her "good reasons" track the research: enjoying the work of leading, feeling a responsibility to the team, wanting it even when it costs you. Her "bad reasons" are the ones the well-being evidence suggests will not deliver.

:::: move {#ch21.move.reasons} Why do you want it?
Sort each reason into **about the work** (you want what managers actually do), **about the reward** (pay, title, status, influence) or **about escape** (something wrong with your current job). Then mark the ones you would still want if the pay stayed the same.

1. "I like helping people on my team get unstuck."
2. "It's the only way to get a pay rise here."
3. "I'm bored of my current work."
4. "I want a say in what the team works on."
5. "If I don't take it, someone worse will."
6. "My friends from university are all managers now."
7. "I'm good at spotting when someone's about to quit."
8. "I'm tired of being told what to do."

::: answer
- **1. Work.** This is affective-identity motivation in plain words, and the strongest reason on the list.
- **2. Reward.** Legitimate, and worth checking: is it true? If a senior technical track exists, it may not be. If it really is the only route, say so honestly to yourself, and weigh it against the rest of this list.
- **3. Escape.** Boredom is a real push ([[ch02]]), but management is a strange cure for it. Ask first whether a different project or skill would fix it ([[ch20]]).
- **4. Mixed.** Influence over direction is part of the job, but much of it comes through persuasion rather than authority, on both tracks. A staff engineer often has more say over *technical* direction than a manager does.
- **5. Work, mostly.** This is social-normative motivation, a sense of duty to the team, which the research links to leading well [@badura2020]. Check that it is about the team and not about the rival.
- **6. Reward**, of the comparison kind, and the weakest reason here. Their jobs are not your job.
- **7. Work.** Noticing people is a large part of what good managers do, and the attrition evidence says it is worth a lot [@hoffman2021].
- **8. Escape**, and a warning sign. Managers are told what to do too, by more people, and are also responsible for what their team does.

Reasons that survive "would I still want it at the same pay?" are usually about the work. If most of yours are reward or escape, that does not mean "never". It means the trial in the next section matters even more.
:::
::::

## Try before you choose {#ch21.sec.trial}

The best feature of this decision, and the one people least often use, is that you can usually test it before you make it.

There are several ways to try management without taking the job permanently: an *acting* lead role while a manager is on leave, a fixed-term "tour of duty" leading a project or a small team, leading the onboarding of a new hire, or running a hiring loop from start to finish. Each gives you a sample of the real work, the one-to-ones, the interruptions and the responsibility for other people's results, at lower stakes. None of these formats has been tested in research that we could find, so treat this section as craft [!craft]. But the logic is the same as a take-home task in [[ch08]]: a work sample tells you more than an interview, and that is true when you are the one deciding.

Reversibility is the other half. A practitioner essay argues that the best frontline engineering managers stay close to hands-on work and the best senior engineers have often spent time managing, and recommends swinging between the two "like a pendulum" every few years [@majors2017!]. That is one experienced person's view, not a finding. But it is a useful corrective to the idea that the fork is permanent. In many organisations it is not, provided you leave the door open when you go through it.

::: figure {#ch21.fig.way-back src="ch21/way-back.svg"}
Alt: A loop drawn as a path in four stops. Stop 1, gold, "agree it in writing first": how long, what good looks like, how you would step back. Stop 2, purple, "do the real job": one-to-ones, hiring, planning, interruptions. Stop 3, "check in at weeks 4 and 8": what is energising, what is draining, what do the team say? Stop 4 splits three ways: "take it", "not yet" and "step back". A teal dashed arrow runs from "step back" back to the start, labelled "the way back, agreed in advance". A note reads "stepping back is a result, not a failure".

The trial loop. The first stop is the one people skip, and it is the one that makes the last stop safe.
:::

A trial is only as good as what you agree before it starts.

::: craft
**Designing a management trial.** Agree four things before you start, and write them down in a message to the person offering the role.

1. **Length.** Long enough to hit a hard week: two to three months is common. Two weeks tells you about the calendar, not the job.
2. **What good looks like.** Not "the team ships more", which takes longer than a trial and depends on many things, but signals you can see sooner: one-to-ones held every week, one hire or one hard conversation handled well, the team's own view of how it is going.
3. **Checkpoints.** Two, with the person who offered the role. Ask them to show you and tell you, in the sense of the study above [@dragoni2014].
4. **The way back.** What happens if you decide against it: which work you return to, how it is explained to the team, and an agreement that stepping back will not count against you.

Ask the team too, at the end, in a way that lets them be honest. They are the people who know.
:::

Now write yours.

:::: move {#ch21.move.trial} Design a trial
You have been offered a lead role. Write the four-part message from the craft note above, in under 150 words, to the person who offered it. Then write one sentence you could say to your team if you decided to step back at the end.

::: answer
A strong version, using Dev's case:

*"I'd like to try it before I commit. Could we make it a three-month acting role, starting next sprint? I'll hold weekly one-to-ones with all five, run the hire for the sixth seat, and lead planning. Could we check in at week four and week eight, and could you sit in on one of my one-to-ones early on and tell me what you saw? If at the end either of us thinks it isn't right, I'd go back to the platform work as a senior engineer, and we'd tell the squad together that it was a trial that worked as a trial."*

And for the team: *"This was a three-month trial, and it did its job: we learned who should lead this squad, and it isn't me, for now."*

What makes it strong: a fixed length, signals that can be checked within the trial, an explicit request for show-and-tell, and a way back agreed before anyone needs it. The team sentence treats stepping back as an outcome rather than an apology, which is how it should be heard [!view].
:::
::::

Kai's other piece of advice was to talk to somebody who has done the job, which is cheap, and which almost nobody does with enough honesty.

:::: move {#ch21.move.interview} Interview a manager
Find a manager whose job you could plausibly have in two years, ideally not your own manager. Ask for thirty minutes, and ask these five questions. Write down the answers.

1. What did your calendar look like last week? (Ask to see it, if they are willing.)
2. What part of the job did you not expect?
3. What do you miss from before?
4. What is the hardest conversation you have had this year, without names?
5. If you went back to individual work tomorrow, what would happen?

::: answer
There are no right answers, but there are revealing ones. If question 1 shows a calendar you would hate, take that seriously: the calendar *is* the job ([[ch21.fig.week]]). Question 2 usually surfaces the people work: performance problems, personal crises, someone who is about to leave. Question 3 tells you what you would give up. Question 4 tests whether you could live with the hardest part. And question 5 tells you whether the way back exists at that company, which no career framework will tell you as reliably as someone who has looked for it [!view]. If they say "I couldn't", ask why.
:::
::::

## Choosing, and saying so {#ch21.sec.saying}

Dev ran her trial. It was, in her later description, "the most useful three months I've ever hated about half of".

Some of it she liked more than she expected. One-to-ones turned out to be a lot like testing: asking careful questions until the real problem surfaced. She was good at spotting the engineer who had gone quiet. She ran a hiring loop with a structured scoring sheet that Meera would have framed ([[ch07]]). Some of it she liked less than she feared. By week three she had not written code in eleven days, and found herself reviewing pull requests at eleven at night to feel like herself. By week eight, the honest answer to "what's energising?" was "the people", and to "what's draining?" was "everything between the people". And by week ten she had noticed something else: one of the squad's engineers had been quietly doing half of the lead's job for months, organising, unblocking and asking how people were, and was better at it than Dev.

So she chose the expert track, for now, and the way she said it mattered as much as the choice.

::: chairs {left="The Lead" right="The Expert"}
@left: You were good at it. The team liked you. People don't get offered this twice.

@right: People get offered it more than once if they say no well. And "good at it" after three months is a low bar. I was good at the parts that look like testing.

@left: Those are most of the parts.

@right: And the rest is the calendar. I would be a decent manager who missed building things every single day.

@left: You'd get more say over what the team builds.

@right: I'd get more say over who builds it. A staff engineer gets more say over *how* it's built. That's the say I actually want.

@left: Fine. But don't make it sound like you're turning down a gift.

@right: I'm not turning it down. I'm saying "not yet, and here's who should have it now".
:::

Neither chair is wrong, which is the point. The fork is a choice between two good jobs, and the reasons that decide it are personal: what you want your days to contain.

::: craft
**Saying no to the lead role, well.** A useful shape: thank them, say what you learned, say what you want instead, and point at someone if you honestly can. Dev's version, to Tomás:

*"Thank you for the trial. I learned that I like the people part more than I expected, and the calendar much less. I'd like to stay on the technical track and work towards staff, starting with the release-safety work. And I think the squad already has its lead: she has been doing half the job for months, and the team goes to her first. I'd be glad to help her through her own trial."*

It turns a no into information, keeps the door open for later, and gives the organisation a better answer than the one it asked for. This is craft, not research [!craft], but it follows from the same rule as every good exit in this book: leave through a door you would be happy to walk back through ([[ch02.sec.boomerangs]]).
:::

Tomás took it well, partly because Dev had made it easy, and partly, she suspects, because he had seen it coming at week eight. Two months later the engineer Dev had named began her own trial, with show-and-tell from Tomás and an occasional lunch with Kai. As far as anyone can tell, she is going to be very good at it.

Rex's story is slower. By the end of his first year as a manager, one of his engineers has moved teams and another is talking to recruiters. He has noticed, which is to his credit, and he has started asking Kai for lunch. Dev does not know yet what he will decide. Neither, she suspects, does Rex.

::: ask
Q: My company has no senior technical track. Is management my only choice?

A: At that company, possibly, and you should find out for certain by asking someone who has tried to rise without managing. If the answer really is no, you have three honest options: manage, accept a plateau that may suit you better than you think ([[ch22]]), or treat the expert track as a reason to look elsewhere. That last one is a perfectly good pull ([[ch02]]).

Q: If I turn it down, will I be passed over for ever?

A: Sometimes, at some companies, for a while. But a no that comes with a reason, a plan and a better candidate is very different from a no that sounds like reluctance to take responsibility [!view]. Organisations remember who helped them solve the problem.

Q: I'm already a manager, and I don't like it. Is it too late?

A: Usually not. The pendulum view [@majors2017] is a practitioner's opinion rather than a finding, but it describes a route that exists in many organisations if you ask for it [!view]. Frame it the way Dev did: what you learned, what you want instead, and how the team will be looked after. Then look at [[ch22]], which is about exactly this kind of turn.

Q: Isn't refusing to manage a bit selfish? Someone has to do it.

A: Someone has to, and it should be someone who wants the work, because the people being managed bear the cost when it is someone who doesn't. The attrition evidence [@hoffman2021] is, among other things, a measure of how much a good manager matters to the people they manage.
:::

Dev has chosen depth over the lead role, for now, and has learned that the fork is less permanent than it looks. The next chapter, [[ch22]], takes the longest view in the book: what happens to a career over decades, why plateaus and turns are normal, and how the next move, when it comes, can be made from strength. It is also where the loop that began in [[ch01]] comes round again, on the way to the [[epi]].

::: rewind
- **Managing is a different job, not a higher grade of the same one.** You are judged on your team's results, on whether people grow and stay, and on who you hire.
- **People management is a real, measurable skill.** In one large firm it cut attrition and was rewarded with ratings, promotions and pay. Most of the job is in the one-hour slots.
- **The best doer is not reliably the best manager.** Firms promote top performers whose results predict worse management; collaboration predicts better. A competent boss still matters to the people they manage.
- **The "60% of new managers fail" figure is untraceable.** The transition is hard, and new managers learn faster when their own manager shows and tells.
- **The expert track** (staff, principal) is about wider technical impact, often through influence. Whether it really exists is a fact about your employer: check.
- **Management usually pays more at the median, but promotions don't reliably make people happier.** The motives linked to leading well are enjoying it, feeling responsible for the team, and wanting it even when it costs you.
- **Try before you choose:** a fixed-term trial with success signals, checkpoints and a way back agreed in advance. Stepping back is a result, not a failure.
- **Say no well:** what you learned, what you want instead, and who should have it now.
:::

::: further {ref=more.sec.managing}
This chapter is about whether to manage, not how. If you take the role, or are trying it, [[more.sec.managing]] points to a research-based account of how new managers learn the job and to two practitioner guides written for people who have just made the jump.
:::
