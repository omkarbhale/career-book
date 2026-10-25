---
id: ch11
status: final
---

::: scene {slug="INT. LANTERNFISH, BACKEND TEAM AREA — WEEK 2, WEDNESDAY, 6:40 PM"}
Dev has been fighting her laptop since lunch. The integration tests for the carrier-rates service will not run on her machine. They run on everyone else's. She has read the setup guide four times, reinstalled two tools and found a forum thread from 2019 that ends with someone writing *nvm fixed it* and never saying how.

There is a chat channel called #backend-help with forty people in it. She has typed a question there three times and deleted it three times. Each version sounded, to her, like *I am not as good as you thought when you hired me*.

This is not the Dev who worked at Corvid. That Dev was funny in stand-ups and asked blunt questions in code reviews. This one has appeared in her place over the last eight working days. Her messages begin *Hi all, hope you are well* and end *Kind regards, Devika*. At stand-up she says "No blockers", in the voice of a hostage reading a prepared statement. She eats lunch at her desk, so nobody will see her not knowing who to sit with.

Her phone buzzes. It is Rex, who has a tip for every occasion.

@rex: Week two! Remember: big entrance. Make them remember you. 🚀

She looks at the empty office, the failing test and the deleted question, and decides that, in a way, she is making them remember her. Just not in the way Rex means.
:::

Kai's name for this person, which Dev will hear later in the week and not enjoy, is **Corporate Dev**.

Most people meet a version of Corporate Dev in their first weeks somewhere new. Stiffer than usual, more formal, slower to ask and quicker to apologise, working late on problems that a colleague could solve in four minutes, because asking feels like evidence against you. It feels like professionalism. It is mostly fear, and it costs more than it seems to.

This chapter is about starting well: what the research says actually predicts a good start, why asking is cheapest now, what is true and false about first impressions, why you are probably more liked than you think, and how to keep the promises your trailer made without performing them. It is the long game's opening, played with all the rules from [[ch10]] in force from the first morning.

::: pause
Before reading on: when you start a new job, what do you think matters most for how well the first year goes? Rank these: (a) impressing your manager with an early big win, (b) knowing exactly what is expected of you, (c) feeling accepted by the team, (d) believing you can do the job. Hold your ranking; the research has a view.
:::

## Ninety days is a convention, not a law {#ch11.sec.ninety}

The phrase "the first ninety days" is everywhere: in onboarding plans, in management books, in the probation clause of many contracts. It sounds like science. It is mostly convention.

The phrase was made famous by Michael Watkins's book *The First 90 Days*, written for leaders changing roles. Its central idea is the "breakeven point", when the organisation needs you as much as you need the job, and its advice is to get there faster by learning quickly, matching your strategy to the situation and securing early wins [@watkins2003!]. That is useful practitioner thinking. But we found no research suggesting that ninety days is a special threshold.

::: myth {#ch11.myth.ninety-days verdict=busted grade=moderate} The first 90 days are a magic window that decides your future
The ninety-day figure comes from practitioner writing and contract convention [@watkins2003], not from research that found a threshold there. What the evidence does support is the general idea behind it: how newcomers adjust early on is linked to their later performance, satisfaction, commitment and likelihood of staying [@bauer2007]. So the early months matter. But there is no cliff at day 91, and a slow start is not a verdict; first impressions, as this chapter shows, are sticky rather than permanent [@baumeister2001].
:::

Where does the number come from, then? Partly from probation periods, which are a legal and contractual matter rather than a psychological one, and which vary a lot between countries: in Germany, for example, probation can last up to six months, with two weeks' notice on either side during it [@bgb622], while in the US most employment is "at will" anyway [@lii-atwill]. [[ch09.sec.checks]] covered what probation means; your contract says what yours is. Probation is a legal fact about your job; "the first ninety days" is a story about it.

The useful question is not how long the window is. It is what, during those early months, actually predicts a good start.

## What actually predicts a good start {#ch11.sec.predicts}

Researchers who study "organisational socialisation", the process of turning a new hire into an insider, have been asking this for decades. The clearest answer comes from a meta-analysis by Talya Bauer and colleagues, which pooled 70 samples of newcomers [@bauer2007].

They found three markers of a newcomer's adjustment that sat between everything that happens in the first months and the outcomes everyone cares about. What organisations do to bring people in, and how actively newcomers seek information, were linked to these three markers; and the markers, in turn, were linked to job satisfaction, commitment, performance and staying [@bauer2007]. The three were:

- **Role clarity**: knowing what you are supposed to do, and what good looks like.
- **Self-efficacy**: believing you can do it.
- **Social acceptance**: feeling liked and included by your colleagues.

We will call them **clarity, competence and connection**, which is our shorthand for Bauer's three, not theirs. (Strictly, the second is *belief* in your competence. Belief matters because people who think they can do something try more and hide less.)

::: figure {#ch11.fig.newcomer src="ch11/newcomer.svg"}
Alt: A diagram in three tiers. At the top, two boxes: "What you do: ask, and ask again; seek feedback early; get to know people" and "What they do: onboarding that explains; clear goals, a buddy; people who include you". Arrows lead down to three circles: gold "Clarity: I know what good looks like here", coral "Competence: I can do this", and teal "Connection: they want me here". Arrows from all three circles lead down into a box: "A good start: better performance, more satisfied, more likely to stay".

What makes a newcomer succeed, after Bauer and colleagues' meta-analysis. Both you and the organisation feed the three middle circles, and the circles, not the inputs, are what go with a good first year.
:::

Now look back at your Pause ranking. Option (a), the early big win, is not on the list. Options (b), (c) and (d) are the list. The links in the meta-analysis are correlational, so they do not prove that clarity *causes* good performance, but they do point at where to spend your energy. An impressive early win may help, mostly by building the other three. Chasing one at the expense of clarity and connection is the Rex strategy, and it tends to produce a big entrance followed by a confused second act.

Corporate Dev, notice, is starving all three. She is not asking, so she has little clarity. She is stuck alone for hours on a setup problem, which is a fast way to stop believing you can do the job. And she is eating lunch at her desk.

The rest of this chapter takes the three in turn.

## Clarity: ask now, while it's cheap {#ch11.sec.clarity}

The single most useful thing a newcomer can do is also the one Corporate Dev is avoiding: ask questions.

In a study that followed 135 new staff accountants through their first six months, those who sought information more often had mastered their jobs better, understood their roles and the culture better, and fitted in socially better [@morrison1993]. Other research on newcomers lists the same proactive moves (seeking information and feedback, building relationships, negotiating what the job involves, framing things positively) and finds that some of them, though not all, go with better self-rated performance and satisfaction [@ashford1996].

There is also a timing argument, and it is the strongest reason to ask now. A meta-analysis of thirty years of research on feedback-seeking found that people seek feedback less as their tenure grows and as they get older [@anseel2015]. Part of the reason is obvious: the longer you have been somewhere, the more you feel you *should* know, so asking feels costlier. In week two, nobody expects you to know where the deployment scripts live. In month eighteen, the same question is awkward. **You will never again be allowed to ask so many questions for free.** Spend that allowance.

To be fair to the evidence, the same meta-analysis found that feedback-seeking's *direct* link to performance is small [@anseel2015]. Asking is not magic. What it buys you is mainly clarity, and clarity, as the last section showed, is one of the three things that go with a good start.

### The three questions that matter most

Not all questions are equal. A newcomer can ask "where is the stapler?" a hundred times and learn little. The questions that build clarity are about how the place really works, which is rarely what the onboarding document says. Three are worth asking explicitly, ideally of your manager in your first weeks [!craft]:

1. **What does good look like here, at three months and at a year?** Ask for examples, not adjectives.
2. **How does work actually flow?** Who decides priorities, who needs to be told about what, and what happens when something goes wrong.
3. **What do people here wish newcomers knew sooner?** The answers are usually the unwritten rules.

::: scene {slug="INT. LANTERNFISH, SMALL MEETING ROOM — WEEK 2, THURSDAY, 10 AM"}
Tomás has a notebook with a single heading: *Dev, 1:1 #1*. He gets straight to it.

@tomas: Three things I'd like us to agree today. What you're working on, what good looks like by the end of month three, and how we'll talk.

@dev: Of course.

@tomas: Month three: you own the carrier-rates service day to day. You know where it breaks and you can change it safely. You've shipped one real improvement, small is fine. And people on other teams know you're the person to ask about it. That's it. I'm not expecting heroics.

@dev: That's very clear. Thank you.

@tomas: How we'll talk: half an hour every week, your agenda first. And I don't like surprises. If something's going sideways, tell me early. Bad news on a Tuesday is information. Bad news on a Friday afternoon is a surprise.

@dev: Understood.

@tomas: ...You haven't asked me anything.

@dev: I think I'm fine for now.

Tomás writes something in the notebook. Dev cannot see what. She spends the afternoon wondering, and the evening still fighting the integration tests.
:::

Tomás has done his half of the work. He has given Dev exactly the clarity Bauer's research points at: what good looks like, by when, and how they will communicate. He has even, without knowing it, set the stage for [[ch12]], where Friday afternoons become a problem. But a one-to-one only works if both people use it, and Corporate Dev has just turned down an open invitation to ask questions, in a meeting designed for questions.

Why would a capable person do that?

## Why asking feels so expensive {#ch11.sec.asking}

Corporate Dev's logic goes like this: *They hired a competent person. Competent people don't ask basic questions. If I ask, they'll realise I'm not competent.* Every step feels reasonable. Two of them are wrong.

The first wrong step is about what asking signals. In a set of experiments, people who asked for advice were seen as *more* competent, not less, especially when the task was hard and when the person being asked was the one doing the judging [@brooks2015]. That paper's co-authors include a researcher with retractions elsewhere, so we lean on it only alongside converging evidence. That evidence is the second point.

The second wrong step is about how people respond, and you met the evidence in [[ch06.sec.asking]]. Across six studies in the lab and in the field, people underestimated by as much as 50% how likely others were to agree to a direct request for help, because they forgot how awkward it is to say no [@flynn2008]. You imagine the colleague sighing at your question. In fact, saying no to someone's face is uncomfortable, so people say yes far more often than you expect.

::: flashback {ref=ch10.sec.warmth}
In [[ch10]], we saw that people often judge warmth first and competence second, but judge *themselves* the other way round. Corporate Dev is working flat out on a question nobody is asking yet ("is she competent?") while neglecting the one they are ("is she one of us?").
:::

Corporate Dev's silence is also hiding a cost. Every hour spent stuck alone on a problem a colleague could solve in four minutes is an hour of nothing much for the team, and a small drain on the very self-belief that Bauer's research links to a good start. The heroic newcomer who never asks is not saving anyone time. They are spending it, quietly, in a way nobody can see.

::: craft
**How to ask well, so asking stays cheap.** Experienced engineers and managers tend to agree on a few habits [!craft]. Say what you have already tried ("I've reinstalled the toolchain and checked the setup guide; the rates tests still fail with a certificate error"). Ask in the shared channel rather than privately, so the answer helps the next person too. Time-box being stuck: if you have made no progress in, say, thirty to sixty minutes, ask. And write down the answer, so you only ask once. Nobody minds a newcomer's question. Some people mind the same question three times.
:::

## First impressions: fast, sticky, not permanent {#ch11.sec.impressions}

Newcomers worry about first impressions for good reason, and also for some bad ones. It is worth separating what is true from what is folklore.

**True: impressions form fast.** In a series of experiments, people's judgements of a face's trustworthiness, competence and likeability after a tenth of a second already lined up closely with judgements made with no time limit; extra time mostly made people more *confident* in what they had already decided [@willis2006].

**Mostly true: warmth tends to be read first** [@fiske2007], though not in every study [@nauts2014]. Whether people think you are on their side colours how they read everything else, as [[ch10]] showed.

**False: fast means accurate.** Those split-second judgements are quick, not correct, and the research does not claim they are [@willis2006]. A colleague's first read of you is a guess based on very little.

**Half-true: you never get a second chance.** Bad impressions are stickier than good ones and form faster [@baumeister2001], so a poor first week costs more than a great one gains. But sticky is not permanent. Impressions update with evidence, and in a job, unlike an interview, the evidence keeps coming every day. That is the long game's great kindness to newcomers: you get hundreds of second chances, as long as you use them.

There is a related comfort. People overestimate how much others notice their appearance and actions, an effect researchers call the *spotlight effect* [@gilovich2000]. And after a public blunder, people expect to be judged more harshly than they actually are [@savitsky2001]. The stand-up where you mumbled, the question you think made you look slow: most of your colleagues have forgotten it by lunch. [[ch12]] uses the same research to handle bigger mistakes.

## Connection: you are more liked than you think {#ch11.sec.connection}

Corporate Dev eats at her desk because she is sure the team would rather she didn't join them. This is one of the most consistent errors in social psychology, and it has a name.

After conversations with strangers, people reliably underestimate how much their conversation partner liked them and enjoyed their company. Erica Boothby and colleagues called this the **liking gap**, and found that among new university room-mates it persisted for months [@boothby2018]. A follow-up found it in groups and work teams too, where it was largest between peers, and where it related to how well teams could work together [@mastroianni2021]. Other research finds that people expect talking to strangers to be more unpleasant than it turns out to be, and underestimate other people's interest in connecting [@epley2014].

::: figure {#ch11.fig.liking-gap src="ch11/liking-gap.svg"}
Alt: Dev and Kai stand at either end of a lunch table. Dev's thought bubble, in coral, says "I talked too much. Kai thinks I'm dull." Kai's thought bubble, in teal, says "She's funny. Lunch again on Thursday?" Below, under the heading "After the same conversation", two bars: a short coral bar labelled "how much Dev thinks Kai liked her" and a long teal bar labelled "how much Kai actually did", with a dashed arrow between their ends labelled "the gap". A note says "Illustrative bar lengths; the gap is real, its size varies".

The liking gap. After a conversation, people reliably underestimate how much the other person liked them. The bar lengths here are invented; the direction is what the research finds.
:::

So the newcomer's fear is mostly wrong in a predictable direction. You are probably more liked than you think. The practical conclusion is not "be more likeable"; it is "believe the evidence more than your own anxiety, and keep showing up". Sit with people at lunch, even when it feels like an intrusion. Accept the invitation. Say yes to the coffee. The cost you are imagining is smaller than you are imagining it.

::: scene {slug="INT. LANTERNFISH, KITCHEN — WEEK 3, MONDAY, 12:50 PM"}
Kai finds Dev at her desk with a sandwich and an expression of intense concentration on a terminal that is not doing anything.

@kai: Right. You're coming to lunch. It's not optional; it's onboarding.

The lunch table is loud. Old Faithful, working again, gurgles in the corner. Kai makes introductions at speed, and then, when the others drift off, leans in.

@kai: Can I tell you something? You sign your chat messages "Kind regards".

@dev: Is that bad?

@kai: It's lovely. It's like getting a letter from a bank. People think you're brilliant and slightly terrifying. Someone asked if you were annoyed with them.

@dev: I'm not annoyed. I'm stuck. The rates tests won't run on my machine and I've lost two days to it.

@kai: Two *days*? Ask in #backend-help. Someone on platform answers everything in four minutes. They live for it.

@dev: Won't it look like I don't know what I'm doing?

@kai: You're three weeks in. You *don't* know what you're doing. Nobody expects you to. They do expect you to ask.

Dev posts the question at 1:30 pm, with the error message and the three things she has tried. At 1:34 pm, someone replies: a certificate the setup guide forgot to mention. The tests go green at 1:41.

She deletes "Kind regards" from her chat signature. It feels like taking off a tie.
:::

Kai did in five minutes what three weeks of anxiety could not: supplied evidence. The liking gap, the underestimation of help, the spotlight effect: all three are errors of guessing, and all three are corrected by asking. That is also why a good onboarding buddy is worth so much more than a good onboarding document.

## Being near people helps juniors most {#ch11.sec.proximity}

Connection is not only about lunch. For newcomers, especially junior ones, being near colleagues seems to change how much they learn.

A study of software engineers at a Fortune 500 company, published in 2026, compared engineers who sat near their teammates with those who didn't. Sitting near teammates increased the feedback engineers got on their code by 18.3% and improved code quality, and the gains were concentrated among junior engineers. There was a trade-off: senior engineers who sat near juniors wrote less code themselves, apparently because mentoring took up their time [@emanuel2026].

If you are new and junior, that is a reason to be where your team is, at least some of the time, and to make your work easy to comment on: small pull requests, drafts shared early, questions asked where others can see them. If you are new and fully remote, it is a reason to build the equivalent on purpose: regular pairing, a standing call with your onboarding buddy, and asking for reviews rather than waiting for them [!craft]. [[ch14]] looks at remote and hybrid work in more depth, including what the large trials found.

## Start a notch more formal, then let the room set the level {#ch11.sec.calibrate}

Corporate Dev's instinct was not entirely wrong. It was just stuck.

There is some evidence that newcomers have good reason to start slightly careful. In work-related first contacts, a smiley emoticon did not make senders seem warmer, and it made them seem less competent [@glikson2018]. And breaking a workplace's dress or formality norms on purpose can raise people's perceived status, but only when observers know the setting and its norms and see the break as deliberate [@bellezza2014]. A newcomer's casual note can easily read as not knowing the rules yet [!view]. Both these findings point the same way: casualness is a privilege the room grants you, not one you claim on day one.

So here is a rule of thumb that we think works better than either Corporate Dev or Rex's big entrance [!view]: **start a notch more formal than you expect the room to be, watch how people actually talk, and match down as the relationships form.** The mistake is not starting formal. It is staying formal after the room has told you, three times, that it is not.

::: coming {ref=ch14}
[[ch14]] turns this into the professionalism dial: a setting you adjust by context, rather than a costume you wear all day. [[ch13]] looks at the same question in writing, where tone is even easier to misread.
:::

## Bring your best self, not your interview self {#ch11.sec.best-self}

There is one more finding about starting well, and it connects the first ninety days back to the argument of [[ch10]].

In a field study at a business-process outsourcing company in India, new hires went through one of several versions of onboarding. Those whose onboarding invited them to reflect on and express their "best selves" (what they were like at their best, and how they could bring that to the job) had higher customer satisfaction and were more likely to still be there six months later than those whose onboarding focused on pride in the organisation [@cable2013]. This is a single field site, and one of the co-authors has retractions elsewhere, so treat it as promising rather than settled. (Her co-authors report that she did not collect the field data and that they have reproduced its results, but those data are confidential, so nobody else can check [@manycoauthors-cable2013!].) But it fits the evidence on authenticity in [[ch10]]: people do better when the job asks for their best real self, not a corporate costume.

Most organisations will not run that kind of onboarding for you. You can run it yourself.

::: craft {by=author} Onboard your best self
We think the most useful private exercise in a new job is to write down, in your first week, three or four moments when you were at your best at work, and what you were doing in them. Not achievements for a résumé: *moments*. Then look for the first chance, in the new job, to do that thing again.

Dev's list, when she finally makes one, includes "asking the blunt question in code review that everyone else was thinking". Corporate Dev has not asked a blunt question in three weeks. The list is a way of remembering who you were before you were new.
:::

## Keep the promises your trailer made {#ch11.sec.promises}

Here is the part of starting a new job that Part I set up and nobody warns you about.

To get this job, you told stories. In your résumé and your interviews, you described the best real scenes from your film: the problems you solved, the way you work, what you care about. If you followed Part I, every one of those stories was true. But true is not the same as *current*. Your new colleagues heard, or heard about, the trailer. Now they are going to watch the film, and the first thing they will check, without meaning to, is whether the two match.

::: flashback {ref=ch07}
In [[ch07]], Dev told the Lanternfish panel true stories from her story bank about how she works. Those stories got her the job. They are also, now, a set of expectations.
:::

Every story you told is a small promise. "I'm the person who makes systems testable" is a promise to make *these* systems testable. "I ask the hard questions" is a promise to ask them here, in week three, when it is scary. Corporate Dev, in other words, was not only being unhappy. She was breaking promises her trailer had made.

This is why the best early wins are not grand gestures. They are the first scenes of the film that match the trailer. Watkins's advice to secure early wins [@watkins2003!] is sensible practitioner advice, but the win that matters most is usually the one that confirms you are who you said you were.

::: trapdoor
**Fixing the place before you understand it.** The opposite of Corporate Dev is the newcomer who arrives with a list of everything that is wrong and starts proposing rewrites in week two. Some of what looks broken from outside is broken. Some of it is a scar from a problem you have not heard about yet. Proposing big changes before you understand why things are the way they are spends trust you have not yet deposited, and the first time you are wrong about a reason, it costs you twice. Ask why first; propose second; and make your first changes small, real and easy to undo [!craft].
:::

Keeping your trailer's promises starts with knowing exactly what they were, so write them down.

:::: move {#ch11.move.promises} The promises your trailer made
Think of the last job you got, or the one you are aiming for. List three things you said or implied about yourself in your résumé, profile or interviews. For each one, write:

1. What would the first visible proof of it look like in the new job?
2. When, realistically, could you show it?
3. What might stop you? (Be honest: fear, a different context, or a claim that was a little ahead of the truth.)

::: answer
Strong answers turn every claim into a specific, early, *small* scene. "I improve test reliability" becomes "in my first month, find the flakiest test in the suite, find out why, and fix it or write up why not". "I'm a clear communicator" becomes "write the onboarding notes I wish I'd had, and share them with the next new hire".

The third question is the important one. Most broken trailer promises are not lies; they are claims that were true in the old context and get harder in the new one, usually because of fear (Corporate Dev) or because the new place works differently. If a claim was ahead of the truth, the honest fix is the one [[ch01]] gave the Film in its argument with the Trailer: go and shoot some better scenes, fast, and stop repeating the claim until you have.
:::
::::

## The Wins tab {#ch11.sec.wins}

There is one more habit worth starting in the first ninety days, and the payoff comes much later.

New jobs are a blur. By month nine, you will not remember what you did in month two: the bug you found, the document you wrote, the person you unblocked. Neither will your manager. And when the first performance review arrives, the person writing it will be summarising a year of your film from memory, which, as [[ch01]] noted, makes ratings say a lot about the rater.

So keep a record, starting now. One line per week is enough: what you did, and what changed because of it. Specific, checkable, with names and numbers where you have them, the same rules that made a strong résumé line in Part I. This is not a brag file; it is notes. The point is not to impress anyone yet. It is to make sure that when the career game's first review comes round, the evidence exists.

::: coming {ref=ch18}
In [[ch18]], Dev's weekly notes become her self-review, and the gap between what she remembers and what she wrote down turns out to be most of the difference between a vague review and an accurate one.
:::

The first ninety days are also the right time to plan the first ninety days, so try sketching yours.

::: figure {#ch11.fig.first-month src="ch11/first-month.svg" size=small}
Alt: A vertical timeline titled "A first month, as a plan" with four numbered stops. Week 1, "Learn the map": who decides what, how work flows, where questions go. Week 2, "Ask, shadow, fix something small": pair with someone; ship one tiny, real change. Week 3, "Own one real task": end to end, with a check-in halfway, not at the end. Week 4, "Check the target": ask what good looks like at three months. A teal box below says "every week: meet two people, and ask more questions than feels comfortable". A note says "Practitioner advice, not a finding: adapt it to your job".

A first month as a plan. The weeks are a practitioner's suggestion, not a research finding; the point is that each week feeds clarity, competence or connection on purpose.
:::

Notice that the plan is mostly questions and small things. That is deliberate: in the first month, small real scenes beat big promised ones.

:::: move {#ch11.move.first-month} Map your first month
Using [[ch11.fig.first-month]] as a starting point, sketch your own first month in a new job (or, if you are not starting one, the first month of a new project or team). For each week, write one thing you will do for **clarity**, one for **competence** and one for **connection**.

::: answer
A good map has three features.

- **Every week touches all three.** Most newcomers overload competence (tasks, tickets, proving themselves) and neglect connection, which is the trap Corporate Dev fell into. If a week has no connection item, add one: a coffee, a lunch, a pairing session.
- **The competence items get bigger gradually.** A tiny real change in week two, one owned task in week three. Small early wins build the self-belief that Bauer's research links to a good start, and they are easy to undo if you got something wrong.
- **There is an explicit check on clarity.** Somewhere around week four, ask your manager directly: "What does good look like at three months, and am I on track?" If your manager has already told you, as Tomás did, ask again anyway. The answer will have changed, or your understanding will have.
:::
::::

Plans are easier than questions, so here is the last exercise, and the one to do first.

:::: move {#ch11.move.three-questions} Three questions to ask this week
Write three questions you will ask someone at work this week that you have been putting off, for fear of looking slow or new. For each, note who you will ask and where (a shared channel, a one-to-one, a coffee).

::: answer
Good questions here usually fall into three groups:

- **Questions that unblock you**: the setup problem, the unclear requirement, the acronym everyone uses. Ask these in shared channels, with what you have tried.
- **Questions about how the place works**: "Who should I tell before I change this?", "Why is it done this way?", "What do you wish you'd known in your first month?" Ask these one to one; people answer more honestly.
- **Questions about you**: "What does good look like for me at three months?", "Is there anything I should be doing differently?" Ask these of your manager, early, while feedback-seeking is still cheap [@anseel2015].

If writing the questions felt uncomfortable, that is the feeling the research says you are misjudging. People will say yes more often than you expect [@flynn2008].
:::
::::

A few things people wonder about their first months, and rarely ask.

::: ask
Q: What if my onboarding is terrible: no plan, no buddy, a manager who is never around?

A: Then build the three middle circles yourself. Ask the clarity questions in writing if you cannot get a meeting. Find an informal buddy: the person who answers questions in the shared channel is usually delighted to be asked. And keep the Wins notes anyway, because a chaotic start is exactly when nobody else will remember what you did.

Q: I'm naturally quiet. Do I have to become a lunch-table person?

A: No. Connection does not require being the loudest at lunch. One-to-one coffees, helping in the shared channel, and pairing on a problem all build it. What matters is that you are not *absent*: present in the ways that suit you.

Q: I made a real mistake in my first month. Is it over?

A: Almost certainly not. You will be judged less harshly than you expect [@savitsky2001], first impressions update with evidence, and the long game gives you hundreds of chances to add new evidence. How you handle the mistake matters more than the mistake. That is [[ch12]].
:::

Dev, meanwhile, had started handling her first weeks rather better, and she had started writing them down.

::: scene {slug="INT. DEV'S FLAT — WEEK 6, SUNDAY EVENING"}
Dev opens the spreadsheet. The tabs from the job search are still there: *Game 1*, *Story bank*, *Bullets that work*, *Offers*. She hasn't looked at them in weeks. It is strange how quickly the snapshot game stopped feeling like her whole life.

She adds a new tab, and calls it *Wins*.

Row 1: *Week 3. Fixed the missing-certificate step in the setup guide after losing two days to it. Next new hire got set up in an hour.*

Row 2: *Week 4. Found why the rates tests flake at midnight (time zones, obviously). Fixed. Nightly build green four nights running.*

Row 3: *Week 5. Asked the blunt question in the routing design review: what happens when a carrier's API is down for an hour? Nobody knew. We added a fallback.*

She looks at row 3 for a while. It is the first thing she has done at Lanternfish that the Corvid Dev would have done. It is also the first time she has noticed that the trailer and the film are starting to match.

Her phone buzzes. Rex again.

@rex: How's the big entrance going?

@dev: Skipped it. Doing the film instead.

@rex: ??

She puts the phone face down and adds row 4 before she forgets it.
:::

A few weeks later, Dev gives her first big estimate, and that is where [[ch12]] begins. Starting well is mostly about clarity, competence and connection. Staying trusted is mostly about something duller: doing what you said you would do, and saying so early when you can't.

::: rewind
- "**The first ninety days**" is a practitioner's convention and a common probation length, not a threshold found in research. The early months matter, but there is no cliff at day 91.
- A good start goes with three things: **clarity** (knowing what good looks like), **competence** (believing you can do it) and **connection** (feeling accepted). Both you and your organisation feed them.
- **Ask now.** Information-seeking helps newcomers, feedback-seeking declines with tenure, and you will never again be able to ask so many questions for free.
- Asking costs less than it feels like: people **underestimate how often others will say yes**, and seeking advice can make you look *more* competent.
- First impressions are **fast, sticky and not permanent**, and not necessarily accurate. You get hundreds of second chances; use them.
- You are probably **more liked than you think** (the liking gap). Believe the evidence over your anxiety, and keep showing up.
- **Start a notch more formal, then match down** as the room tells you its level. Corporate Dev's mistake was not starting formal; it was staying there.
- Your trailer made promises. **Keep them early, in small, real scenes**, and start a weekly record of what you did and what changed, for the reviews to come.
:::
