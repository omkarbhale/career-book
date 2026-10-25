---
id: ch12
status: review
---

::: scene {slug="INT. LANTERNFISH, BACKEND TEAM AREA — MONTH 4, FRIDAY, 4:47 PM"}
On Monday, Tomás had asked Dev how long it would take to add a new carrier, Northwind Freight, to the rates service. She had looked at the API documentation, which was short and confident, and said: "Three days. Thursday, to be safe."

On Wednesday morning she found out why the documentation was short. Northwind's test environment allowed ten requests a minute, returned prices in three different formats depending on the route, and occasionally returned nothing at all, with a cheerful *200 OK*. By Wednesday lunchtime she knew it was not a three-day job. It was more like eight.

She did not say so. She thought she could catch up. She worked late on Wednesday, later on Thursday, and when Tomás asked in Thursday's stand-up how Northwind was going, she heard herself say "Nearly there."

At 4:47 pm on Friday, she sends the message.

> *Hi Tomás, quick update: Northwind won't be ready today. The sandbox has been a lot harder than expected. Probably another week. Sorry!*

Three minutes later, Tomás is standing by her desk. He does not look angry. He looks like someone doing arithmetic.

@tomas: The account team is demoing Northwind rates to the customer on Monday at nine. I told them Thursday, because you told me Thursday.

@dev: I know. I'm sorry. I thought I could get it done.

@tomas: When did you know it wouldn't be?

There is a pause long enough for both of them to hear the answer.

@dev: Wednesday.

Tomás nods slowly. On the sticky note at the bottom of Dev's monitor, default number one, *Tell people about problems the day I find them*, has been looking at her all week.
:::

Meera said it would cost something within a month. It took a little over three.

Nothing dramatic has happened here. Nobody lied about anything important, and nobody was careless. A developer underestimated a task, as developers have done since there were developers, and then did what almost everyone does with bad news: held on to it, hoping it would turn into good news before anyone needed to hear it. The slip itself was ordinary. The two days of silence turned it into a Friday-afternoon surprise.

This chapter is about the least glamorous part of the long game, and possibly the most important: doing what you said you would do, and when you can't, saying so early. It covers how to make commitments that can be kept, why estimates go wrong in a predictable direction, why bad news gets held back and what it costs, how mistakes are actually judged, how to apologise in a way that repairs trust, how to say no, and how to work with your manager without "managing" anyone.

::: pause
Before reading on: what should Dev have done on Wednesday lunchtime, in one sentence? And a harder one: why didn't she? Write down your best guess at her reason. The chapter will test it.
:::

## The cheapest trust you will ever buy {#ch12.sec.cheapest}

[[ch10]] described trust as three dials: ability, benevolence and integrity. Reliability is where two of them meet. Each time you do what you said, by when you said, you show that you can do the work (ability) and that your word means something (integrity). Repeat that a few hundred times and people stop checking. That is what trust looks like from the inside: someone deciding they no longer need to verify you.

::: craft {by=author} Why we call reliability a superpower
We think reliability is the cheapest trust anyone can buy at work, and the most underrated. It does not need talent, charisma or seniority. It needs a habit of making commitments you can keep, tracking them, and telling people early when you can't. Brilliant people who are unreliable are exhausting to work with, because everything they touch needs a backup plan. Ordinary people who are reliable become the ones everyone wants on their project, because their "yes" can be built on.

Notice what reliability is not. It is not "never missing a deadline". Everyone misses deadlines. It is never letting a deadline *surprise* anyone.
:::

That last line is the whole chapter in one sentence. Dev did not damage Tomás's trust by being slow. She damaged it by letting him plan a customer demo around a date she already knew was wrong. The first is a competence problem, and competence problems are forgiven quickly. The second starts to look like an integrity problem, and those are not.

## The commitment loop {#ch12.sec.loop}

Most broken commitments at work were never really commitments. "I'll look into it." "Should be fine." "Let me get back to you." Each of these sounds like a promise to the listener and like nothing in particular to the speaker. Nobody wrote it down, nobody agreed what "it" was, and three weeks later, both people remember a different conversation.

A reliable commitment goes round a loop.

::: figure {#ch12.fig.commitment-loop src="ch12/commitment-loop.svg"}
Alt: Six boxes arranged in a loop, titled "The commitment loop". Down the left: "1, Hear the ask: what do they actually need?"; "2, Clarify: what, by when, and what does done mean?"; "3, Say it out loud: 'Rates by Thursday, tested, in staging.'", highlighted in gold. Across and up the right: "4, Track it: somewhere you will see it tomorrow"; "5, Deliver, or renegotiate early, the day you know", highlighted in teal; "6, Close the loop: tell them it's done; don't make them ask". A dashed arrow runs from step 6 back to step 1. A note says "Step 5's second half is not failure. It is the loop working."

The commitment loop. Most broken commitments fail at step 2 (nobody agreed what "done" meant) or step 5 (the slip was known but not said). Renegotiating early is part of the loop, not a way out of it.
:::

None of the steps is clever, and that is the point [!craft]. Two of them do most of the work.

**Step 2, clarify**, prevents the most common failure, which is not lateness but mismatch. "Add Northwind" could mean "rates appear in the test environment" or "rates, booking and tracking, tested, in production". If those two definitions meet for the first time on Monday at nine, someone is going to have a bad morning. You may remember this from [[ch08]]: on her Lanternfish take-home, Dev asked two clarifying questions and set herself a time cap before writing a line of code. In the snapshot game she did step 2 instinctively, because she knew she was being watched. In the long game, on a Monday, with the documentation looking short and confident, she skipped it.

**Step 5, renegotiate early**, is the one people treat as failure, and it is the opposite. When you find out a commitment cannot be kept as made, telling the person the same day *is* keeping your word, in the only form still available. It turns a broken promise into new information.

Step 6 is the quiet one. A commitment is not finished when the work is done; it is finished when the person who asked knows it is done. "Merged and deployed, here's the link" costs ten seconds and saves someone a check-in message. Done often enough, it is the difference between a colleague people chase and a colleague people trust.

:::: move {#ch12.move.vague} Rewrite a vague commitment
Rewrite each of these as a commitment that could actually be kept and checked. Add whatever you would need to ask.

1. "I'll look into the login bug."
2. "Should have the report to you soon."
3. "Sure, I can help with the migration."
4. "Let me get back to you on that."

::: answer
Good rewrites add three things: **what** exactly, **by when**, and **what "done" means**, and sometimes a question that clarifies scope.

1. "I'll find out whether the login bug is in our service or the identity provider's, and tell you which by end of day tomorrow. Fixing it is a separate estimate."
2. "You'll have the first full draft of the report by Thursday noon. It will have the figures but not the recommendations; those need the finance team's input, which I'll chase today." (Notice the honest scope.)
3. "I can give the migration two afternoons this week, Tuesday and Thursday. Which part would help most: writing the scripts or testing them?"
4. "I don't know yet. I'll ask the platform team today and reply by Wednesday, even if the answer is 'still unknown'."

The last one matters most. A commitment to *report back by a date*, even with no answer, is still a commitment you can keep. "Still unknown, here's why, next update Friday" is a perfectly reliable message.
:::
::::

Clarifying the commitment fixes half of Dev's problem. The other half is the estimate itself, and that has a cause researchers have studied for decades.

## Why your estimates are optimistic {#ch12.sec.estimates}

Dev's three days became eight. That is not unusual, and it is not random.

In a classic set of five studies, Roger Buehler, Dale Griffin and Michael Ross asked people to predict when they would finish tasks, academic and otherwise, and then checked. People's predictions of their own completion times were consistently too optimistic, a pattern known as the **planning fallacy** [@buehler1994]. The studies also showed *why*. When people predicted, they focused on how the task would go if things went to plan, rather than on how similar tasks had actually gone before. And when their past predictions had failed, they explained the failures away as one-offs: external, temporary and specific to that occasion [@buehler1994].

Two findings in the same paper are the useful ones.

**Your past is the cure.** When people were told to connect relevant past experiences with their prediction, the optimistic bias disappeared [@buehler1994]. Dev spent three years at Corvid watching integrations with outside systems go wrong, from the testing side. Did any of them finish as fast as the plan said? Not one. She knew that. She just did not look.

**Other people are less optimistic about you than you are.** Observers predicting someone else's completion time were not optimistic at all; they *over*estimated it, and they made more use of past experience [@buehler1994]. A colleague's guess at how long your task will take is a useful correction to your own.

Those studies used students and personal or academic tasks, not software projects, but the pattern will be familiar to anyone who has worked in a team. Here is how to turn it into practice [!craft]:

- **Estimate from history, not from the plan.** Ask "how long did the last three things like this take?" before asking "how long should this take?"
- **Give a range, with the reason for its width.** "Three to eight days, depending on how good their test environment is. I'll know by Wednesday." That is more useful to a manager than a confident number, and much more honest.
- **Ask someone else to guess.** Ten seconds of "how long do you think this is?" from a teammate is a cheap second opinion from exactly the person the research says is less biased.
- **Name your checkpoint.** Say when you will know more, and commit to an update then, good news or bad.

None of this makes you a perfect estimator. It makes you a *calibrated* one, which is what people actually need: someone whose "three days" means three days, and whose "three to eight" means it really might be eight.

## Telling people early {#ch12.sec.early}

Now the harder question from the Pause: why didn't Dev say something on Wednesday?

She was not lazy or dishonest. She was doing something so common in software that researchers have a name for it. People on troubled projects are reluctant to pass bad news about a project's status up the line, and that reluctance, sometimes called the **mum effect**, is a recognised contributor to "runaway" projects that overrun badly [@smith2001]. The bad news does not disappear. It just arrives later, larger, and with less time to do anything about it.

Why do people keep mum? One recent set of experiments points at a fear many people will recognise. Across five studies with over 4,000 participants, people were less likely to ask for a deadline extension when the request would be visible to a supervisor, because they worried about looking incompetent, and they handed in worse work as a result. Yet the people receiving extension requests did not react negatively to them [@whillans2022]. In other words, the fear of asking was much larger than the cost of asking.

If your guess in the Pause was "she was afraid of looking bad", you were right, and you were also describing a well-documented misjudgement. Dev imagined that saying "this will slip" on Wednesday would make her look incompetent. What actually made her look less reliable was saying it on Friday.

::: figure {#ch12.fig.bad-news src="ch12/bad-news.svg"}
Alt: A chart with time running left to right from "Wednesday: Dev knows" to "Friday 4:47 pm: Dev says", each marked with a dashed vertical line. A teal curve labelled "options left" starts high and falls steeply towards Friday. A coral curve labelled "cost of the surprise" starts low and rises towards Friday. A teal box pointing at Wednesday lists "move the demo, cut scope, get help, or warn the customer". A coral box pointing at Friday says only "apologise". A note says "Illustrative shapes, not data".

Bad news early versus late. On Wednesday, the same news comes with four options. On Friday afternoon, it comes with one. The curves are a sketch of the logic, not measurements.
:::

Look at what Tomás could have done with Wednesday's news: moved the demo, shown rates for two of Northwind's three route types, borrowed someone from another team to help with the sandbox, or warned the account team to set expectations. On Friday at 4:47 pm, he can do none of those. He can only spend his weekend rewriting the demo plan. Tomás's rule in [[ch11]], "bad news on a Tuesday is information; bad news on a Friday afternoon is a surprise", is not a personality quirk. It is a description of how options shrink.

::: trapdoor
**"I'll catch up."** The most expensive sentence in the long game is the one you say to yourself on Wednesday: *I'm behind, but I'll catch up, and then nobody needs to know.* Sometimes you do catch up. When you don't, you have converted an ordinary estimating error, which people forgive easily, into a pattern of hiding, which they don't. Unless you are genuinely sure you will catch up without heroics, say it the day you know [!view].
:::

A good early warning is short, and it brings options, not just problems. Dev's Wednesday message could have looked like this:

> *Northwind is going to take longer than I said. Their sandbox is rate-limited and inconsistent, so it's looking like 7–8 days, not 3. Options: (a) demo Monday with rates for road freight only, which I can have ready Thursday; (b) move the demo a week; (c) borrow someone for two days to build the retry layer. I'd go with (a). Can we talk for ten minutes today?*

Four sentences. The problem, the reason, the options and a recommendation. No grovelling, because nothing has gone wrong yet: this is the loop working.

:::: move {#ch12.move.early-warning} Write the early-warning message
Pick a real piece of work you are doing now, or one from the last year that slipped. Write the message you would send (or should have sent) the day you knew it would be late. Keep it under 80 words. Include: what is late, by how much, why, at least two options, and what you recommend.

::: answer
Check your message against four tests.

- **Could the reader act on it today?** If the options are vague ("we could look at scope"), sharpen them into decisions someone can make.
- **Is the "why" one sentence?** The reader needs enough to judge the new estimate, not your full debugging history. [[ch13]] has more on putting the point first.
- **Did you recommend something?** People who bring a recommendation along with the problem are much easier to say yes to, and it shows you have thought about their position, not just yours.
- **Is the tone calm?** An early warning is not an apology, because nothing has broken yet. Save "sorry" for when you have actually let someone down.

If writing it made you uncomfortable, notice that discomfort. It is the same fear that made people in the extension experiments hold back, and it is usually larger than the real cost [@whillans2022].
:::
::::

## How mistakes are actually judged {#ch12.sec.judged}

Sometimes the warning comes too late, or the mistake is the kind you only discover afterwards. Then the question is how bad it really is, and the research offers two findings that pull in opposite directions.

The comforting one: after a blunder or public failure, people expect to be judged more harshly than they actually are [@savitsky2001]. People also overestimate how much others notice their actions at all [@gilovich2000]. The colleague you are sure is still thinking about your mistake has, most likely, moved on to their own.

The sobering one: bad impressions form faster and stick harder than good ones [@baumeister2001]. So the mistakes that *are* noticed weigh more than you would like.

Put them together and you get a simple policy. Most mistakes loom much larger to you than to anyone else, so don't spiral, don't over-explain, and don't spend a week punishing yourself. But the ones people notice matter, so own them quickly, fix them visibly, and move on.

There is also a popular idea that mistakes can actually *help* you, and it is worth checking before you rely on it.

::: myth {#ch12.myth.pratfall verdict=partly grade=weak} Making a mistake makes people like you more (the pratfall effect)
The idea comes from a 1966 study in which students listened to recordings of a person who came across as either highly competent or mediocre. When the highly competent person then spilled a cup of coffee, they were rated as *more* likeable; when the mediocre person did the same, they were rated as *less* likeable [@aronson1966]. That is one small, old study with an all-male sample, and the effect only helped people who were already seen as highly competent. It does not show that mistakes make you likeable in general, and for a newcomer whose competence is still unproven, it predicts the opposite. If there is a lesson, it is that a small slip will not ruin a strong reputation, not that slips are good strategy.
:::

## Apologies that repair {#ch12.sec.apology}

When a mistake has cost someone something, the next move is an apology. Most people know they should apologise. Fewer know that what counts as a good apology depends on what went wrong.

::: receipts {source=kim2004} Apology or denial?
**What they did.** Peter Kim and colleagues ran two experiments in which someone accused of a past trust violation, either about competence (a failure of skill) or about integrity (a failure of honesty), responded by apologising or by denying it, and participants then rated how much they trusted that person [@kim2004].

**What they found.** For competence failures, apologising repaired trust better than denying. For integrity accusations, denying worked better, *unless* there was later evidence of guilt, in which case apologising worked better.

**What it cannot tell you.** These were experimental scenarios, not long working relationships. And the denial finding is about *accusations*, not about things you actually did: once guilt is evident, denial backfires. It is not permission to deny what you did; it is a reason never to need to.
:::

For workplace purposes, the practical reading is straightforward. **If you made a competence mistake, such as a bad estimate, a bug or a missed step, apologise plainly.** It works, and it is the right thing to do. **If you made an integrity mistake, such as hiding something or misrepresenting it, do not deny it once it is known**, because that converts one problem into two. Dev's situation is mostly the first kind, with a small edge of the second: the slip was competence, but the two days of silence look a little like concealment. That is why her apology needs to address the silence, not just the delay.

What goes into a good apology? Research by Roy Lewicki and colleagues presented apologies built from up to six components, singly and in combination, and found that apologies containing more of the components were more effective than those containing fewer, that some components mattered more than others, and that apologies worked better after competence failures than integrity ones [@lewicki2016]. We have not read which components ranked highest, so we will not pretend to tell you. Here instead is a structure that covers the usual elements, built from that research and from practice [!craft]:

::: figure {#ch12.fig.apology src="ch12/apology.svg"}
Alt: Five rows, each pairing a coloured label with a sentence from Dev's apology to Tomás. "Name it": I said Northwind would be ready Friday, and I knew on Wednesday it wouldn't. "Own it": That's on me. I should have told you that day. "Impact": It cost you a scramble before the demo and a weekend of worrying. "Fix": Rates and booking work now; tracking lands Wednesday. Demo notes attached. "Prevent": From now on, you hear the day I know, and I'll check in at the halfway point. Below a rule: "Missing on purpose: 'but', 'if', and a speech." Then, in bold: "Then the most important part: do it."

Anatomy of an apology. Each sentence does one job. The structure is a practitioner's guide informed by research showing that fuller apologies tend to work better; the research does not say which part matters most.
:::

Two things are missing from that apology on purpose. There is no "but" ("I'm sorry, but the documentation was terrible"), which turns an apology into a defence. And there is no "if" ("I'm sorry if that caused problems"), which turns it into a question about whether there was a problem at all. And then comes the part no formula captures: actually doing what the last line promises. An apology repairs trust the way a deposit fills a ledger, which is to say, only once it clears.

Why do people find this so hard? A review of the research suggests three common barriers: not caring enough about the person harmed, feeling that apologising threatens your own self-image, and believing that apologies will not work anyway [@schumann2018]. The second is the one capable people struggle with. An apology for a competence mistake can feel like a confession of incompetence. The evidence above says the opposite: it is the move that best repairs trust after exactly that kind of failure.

One last apology finding is small but useful. In four studies, "superfluous" apologies, saying sorry for things you clearly did not cause, such as "I'm sorry about the rain", increased trust a little, by signalling that you cared [@brooks2014]. That is not a case for apologising for everything; constant apology dilutes the real ones. It is a case for the small "sorry you got caught up in that" when a colleague has had a rough day, which costs nothing and lands well.

::: scene {slug="INT. LANTERNFISH, SMALL MEETING ROOM — MONDAY, 8:15 AM"}
Dev is in before Tomás, which has never happened before. She has written the apology three times. The final version fits on one screen.

She reads it out rather than sending it. It names the slip, owns the silence, says what is ready now (rates and booking for road freight, which she finished on Sunday afternoon with a cup of tea and no heroics) and what lands Wednesday, and ends with the new rule.

Tomás listens all the way through.

@tomas: Okay. Thank you. That's a good apology.

@dev: You're allowed to be annoyed.

@tomas: I was annoyed on Friday. Here's the thing, though. I'm not annoyed that it slipped. Estimates slip. Mine slip. I'm annoyed I found out with thirteen minutes of the week left.

@dev: I know.

@tomas: So let's fix the actual problem. Next estimate, you give me a range and a date you'll know more. And if it's slipping, I want to hear it the same day, even if it's only "this might be slipping". I'd rather have ten false alarms than one Friday.

@dev: Deal.

@tomas: Now. Can we show road freight at nine?

They can. The demo goes fine. The customer asks only about road freight anyway.
:::

## Teams that talk about errors do better {#ch12.sec.culture}

Tomás's "ten false alarms" line is a small piece of culture-building, and the research suggests it matters beyond Dev.

In a study of hospital units, Amy Edmondson found something that looked backwards at first: units with better relationships and more coaching from their nurse managers had *higher* detected rates of drug errors. Her interpretation was that people in those units were more willing to report errors, not that they made more [@edmondson1996]. Actual error rates could not be measured, so that is an interpretation, but it grew into one of the most influential ideas in organisational research, psychological safety, which [[ch16]] explores. In the same spirit, a study of 65 Dutch and 47 German organisations found that firms with an "error management culture", where errors were discussed openly and detected, analysed and fixed quickly, tended to achieve their goals and be more profitable [@vandyck2005]. That is correlational, but it points the same way.

You cannot build a team's culture alone. But each time you report your own slip early, you make it slightly cheaper for the next person to report theirs. Reliability is contagious, in a small way, and so is hiding.

## Saying no, so your yes means something {#ch12.sec.no}

There is a quiet threat to reliability that has nothing to do with estimates: saying yes to too much. Every yes is a commitment, and you can only keep so many. A person who agrees to everything becomes, by simple arithmetic, a person who breaks commitments.

So why do people say yes so often? Partly because no feels expensive. Across studies, people asking for help underestimated by as much as 50% how likely others were to say yes, because they forgot how awkward it is to refuse [@flynn2008]. That awkwardness is real, and it pushes people into yeses they cannot afford. On the other side, in experiments about declining social invitations, people who said no overestimated how angry or hurt the other person would be, and how much it would cost them future invitations [@givi2024]. Those were invitations to social events, not work requests, so treat the finding as suggestive at work. But the direction is consistent: saying no costs less than it feels like.

Saying yes costs more than it feels like, too. As [[ch10]] showed, helping beyond your role has real costs in overload and stress, and they fall more heavily on women [@bolino2005], who are also asked more often to take on low-promotability tasks [@babcock2017]. [[ch17]] takes that pattern seriously. For now, the point is simpler: an overloaded person cannot be reliable.

::: chairs {left="The Yes" right="The No"}
@left: People like me. I'm helpful, I'm a team player, I make everyone's life easier.

@right: For about a week. Then you're late on all of it, and they like you less than if you'd said no on Monday.

@left: But saying no feels rude.

@right: Saying no on Monday is a little awkward. Saying yes and delivering nothing is rude. Ask anyone who's been on the receiving end.

@left: So I should just refuse things?

@right: No. Say yes to the things you can actually do, and say a clear, kind no to the rest, with an alternative if you have one.

@left: And if the person asking is my manager?

@right: Then don't say no. Say "yes, and here's what moves to make room for it." Let them choose. That's their job.
:::

The Right chair's last line is the most useful script in this chapter, so here it is in plain form. When your manager asks you to take something on and your plate is full, the reliable answer is rarely a flat no. It is a priority question: "I can do that. To make room, I'd move the Northwind tracking work to next week. Is that the right trade?" That keeps your commitments honest and puts the decision with the person who owns priorities [!view].

:::: move {#ch12.move.decline} Decline gracefully
Write a short reply to each request. Keep the relationship; protect your commitments.

1. A colleague from another team asks you to review a 2,000-line pull request "today if possible". You are already behind.
2. Your manager asks you to also organise the team's quarterly offsite.
3. A friend at work asks you to cover their on-call shift this weekend, for the third time this month.

::: answer
Strong replies tend to do three things: answer quickly (a slow no is worse than a fast one), give a short, true reason tied to priorities, and offer what you *can* do.

1. "I can't do a proper review today: I'm behind on Northwind. I could do the first 500 lines tomorrow morning, or point you to someone who knows that service well. Which helps more?"
2. "Happy to help with the offsite. Right now it would push the Northwind tracking work back about a week. Is that the right trade, or could I own just the venue and someone else take the agenda?" (The priority question, with a smaller offer.)
3. "I can't this weekend. I've covered a few recently and I need this one off. If you're stuck, I can do a weekday evening next week." This one is a boundary as well as a scheduling answer, and [[ch17]] has more on boundaries.

Notice what none of them contains: a long apology, a pile of excuses, or "maybe". "Maybe" is the worst answer of all, because it is a commitment-shaped hole that someone else has to plan around.
:::
::::

## Working with your manager {#ch12.sec.manager}

The relationship that most affects your reliability, and how it is judged, is the one with your manager. It is worth understanding how that relationship works.

Leader-member exchange theory, one of the longest-running ideas in leadership research, describes how managers form relationships of different quality with different members of the same team [@graen1995]. Some get trust, information and latitude; others get instructions and checking. A meta-analysis of 247 studies found that the quality of those relationships is driven most by what leaders do and how they see their people, but also by followers' own characteristics and by the relationship itself, and that it is linked to many of the outcomes people care about at work [@dulebohn2012].

The leader's behaviour matters most, and you cannot control it. But you are not a bystander. The practitioner classic on this is John Gabarro and John Kotter's 1980 essay "Managing Your Boss", which argued, in essence, for consciously working with your manager to get the best results for you, them and the organisation, by understanding their goals, pressures and preferred way of working, as well as your own [@gabarro1980!]. That is advice, not evidence, but it is consistent with the research and with common sense.

In practice, for most people in their first years, "managing up" comes down to a few habits [!craft]:

- **Learn what your manager is anxious about.** Tomás hates surprises. Another manager might hate being copied on everything, or hate finding out about problems from their own boss. Knowing which is half the job.
- **Use your one-to-ones.** Come with your own agenda: what you have done, what is at risk, what you need. A one-to-one where your manager has to drag information out of you is a wasted half-hour for both of you.
- **No surprises, in either direction.** Tell your manager about risks early, and tell them about wins too, briefly; the Wins notes from [[ch11]] make that easy.
- **Ask for help before you need rescuing.** People say yes to direct requests far more than you expect [@flynn2008], and managers are, in principle, paid to.

There is one awkward finding to keep in mind. In a field study and two experiments, managers rated employees who voiced *challenging* ideas (criticisms of how things were done) as worse performers than employees who voiced *supportive* ones, partly because the challenges felt less loyal and more threatening [@burris2012]. That does not mean you should stop challenging. It means *how* you raise a challenge matters, which is the subject of [[ch13]].

## The ticket nobody files {#ch12.sec.ticket}

Reliability is mostly about your own commitments. But there is a second kind, harder to see: the small, shared jobs that everyone assumes someone else has done.

::: scene {slug="INT. LANTERNFISH, KITCHEN — TUESDAY, 9:05 AM"}
Old Faithful is showing E-07 again. The sign from Dev's first day, WHOEVER BROKE THIS, WE KNOW, is still taped to its side, curling at the corners. Someone has added, in biro, *still don't*.

@kai: It's been doing this every week since you started. Someone reported it ages ago.

@dev: Who?

@kai: ...Someone. Tomás asked on your first day.

Dev opens the facilities request system on her phone and searches for "coffee". There is one result, from two years ago, about the old machine. Old Faithful does not exist in the system at all.

She files a ticket. It takes four minutes. She includes the error code, the fact that it means the drip tray sensor, how often it happens (she checks the kitchen channel: eleven times in four months), and a photo.

The next morning, facilities replies. A technician comes on Thursday and replaces a faulty sensor. Old Faithful stops crying wolf about its drip tray, and over the following months finds several new ways to break.

@kai: You *filed* it? Nobody files it.

@dev: I noticed.

At the next stand-up, Tomás thanks her for it in front of the team, and then, being Tomás, adds it to the team's list of things that need an owner.
:::

Four months, forty people walking past a broken machine every day, and nobody filed the ticket, because everybody assumed somebody had. Each person's "probably" was reasonable. Together, they added up to four months of E-07.

Every team has jobs like this: the flaky test everyone reruns, the out-of-date document everyone works around, the follow-up email nobody sends after the meeting. Picking up one of these, occasionally, and closing it properly, is reliability at its most visible, because nobody asked you to [!view]. The caution, which [[ch17]] develops, is "occasionally". Filing the ticket is a deposit. Becoming the person who maintains the coffee machine forever is a job nobody gave you, and nobody will promote you for.

A few questions about all this tend to go unasked, so here they are.

::: ask
Q: My manager wants a single number, not a range. What do I do?

A: Give the number, but attach the condition and the checkpoint: "Five days, assuming their API behaves; I'll know by Wednesday whether it does." That is a single number and an honest one. Most managers who ask for one number really want to know when they will stop being uncertain.

Q: Isn't telling my manager every possible slip just covering myself?

A: It can be, if every message is "this might slip" with no detail or options. The test is whether the message helps them decide something. A warning with options is information; a vague worry, repeated, is noise. Tomás asked for "even if it's only 'this might be slipping'", but plenty of managers prefer one well-timed message to ten anxious ones. Ask yours which they prefer.

Q: What if I made a mistake that nobody has noticed?

A: If it affects anyone else, tell them, now. You will be judged less harshly than you fear [@savitsky2001], an apology works well for competence mistakes [@kim2004], and a mistake that is discovered later, after you knew about it, starts to look like an integrity problem rather than a competence one. That is a much worse trade.
:::

The Northwind work landed on the Wednesday, as promised in the apology. That week, Dev added a second line to the sticky note under her five defaults: *Range, reason, checkpoint.* Then, on Friday, she sent Tomás a message at 11 am, unprompted: the tracking work was done, merged and deployed, with a link.

Tomás replied with a single thumbs-up. From Tomás, Kai told her later, that is practically a speech.

::: coming {ref=ch18}
In [[ch18]], all of this shows up again in Dev's first performance review, because reliability turns out to be one of the things reviews reward most consistently, and one of the easiest to evidence if you wrote it down.
:::

Reliability is mostly what you do. But a lot of it is what you say, and how: the early warning, the clear commitment, the apology that fits on one screen. [[ch13]] is about talking and writing at work, where Dev is about to discover that a message can be reliable and still be four hundred words too long.

::: rewind
- **Reliability is the cheapest trust you can buy.** It needs no talent, only a habit: make commitments you can keep, track them, and never let a deadline *surprise* anyone.
- Run every commitment round the **loop**: hear, clarify (what, by when, what "done" means), say it out loud, track, deliver or **renegotiate early**, and close the loop.
- Your estimates are **optimistic in a predictable way** (the planning fallacy). Estimate from your history, give a range with its reason, ask a colleague to guess, and name the checkpoint.
- People hold back bad news because they fear looking incompetent, and they **overestimate the cost of asking** for more time. Tell people the day you know, with options and a recommendation.
- Most mistakes **loom larger to you than to others**, but noticed ones stick. Own them fast, fix them visibly, move on. The pratfall effect is too weak to count on.
- For **competence mistakes, apologise plainly**: name it, own it, state the impact, fix it, prevent it, with no "but" and no "if". Never deny what you actually did.
- **Say no** so your yes means something; with your manager, turn no into a priority question. Saying no costs less than it feels like.
- Work **with** your manager: learn what they worry about, own your one-to-ones, no surprises either way. And now and then, file the ticket nobody files.
:::
