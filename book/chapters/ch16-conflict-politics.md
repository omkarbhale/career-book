---
id: ch16
status: review
---

::: scene {slug="INT. LANTERNFISH, SPRINT DEMO — TUESDAY, 3 PM"}
Every other Tuesday, each squad shows what it shipped. Today the payments squad is up, and Marcus, a senior engineer with a calm voice and very good slides, is presenting the fix for the invoice-sync bug that has been haunting Lanternfish for a month.

@tomas: This is the one that's been waking people up at 3 am?

"That's the one," says Marcus. "Turned out to be a race condition between the retry queue and the ledger write. Once we found it, the fix was small. I also added the logging, so if it ever comes back, we'll see it in minutes."

People clap. Someone posts a trophy emoji in the chat.

Dev is sitting very still. She found that race condition. She spent a Saturday reproducing it, wrote the patch and sent it to Marcus for review, because the ledger is his code. He reviewed it, merged it, and added the logging. *We* found it, apparently.

Kai, three seats away and now her lead, catches her eye. Dev looks at the floor and counts to ten. She gets to four.
:::

Every workplace has conflict in it, because every workplace is a group of people with different information, goals and memories trying to agree on what to do. Most of it is small: a disagreement about a design, a dispute about who did what, a colleague who is hard to work with. Some of it is not small at all.

This chapter is about all of it. Why credit disputes happen even between decent people, which disagreements help a team and which ones poison it, what "office politics" is when you strip away the sneer, how to speak up to people with power, how to handle people who make work difficult, and what to do when something is genuinely wrong. Underneath is the same model as the rest of Part II: you are in a repeated game ([[ch10]]), so how you fight matters at least as much as whether you win.

::: pause
Before you read on: what should Dev do in the next twenty-four hours? Write down your plan, including what, if anything, she should say, to whom, and where. You will compare it with what she actually does.
:::

## Why decent people over-claim credit {#ch16.sec.credit}

Dev's first theory is that Marcus stole her work. That is possible. But there is a more common explanation, and it is worth checking before you go to war.

In a classic set of studies, Michael Ross and Fiore Sicoly asked people who had done things together (married couples, basketball teams, student groups) how responsible each person was for various joint activities. People recalled their own contributions more easily than their partners', and as a result they claimed more responsibility than their partners gave them [@ross1979]. Nobody was lying. Your own work is simply more memorable to you: you were there for all of it, including the boring parts, while you saw only some of anyone else's. Later work found that asking people to think through each collaborator's contribution separately reduced the over-claiming [@savitsky2005].

::: figure {#ch16.fig.credit src="ch16/credit.svg"}
Alt: Three pie charts of the same bug fix. The first, "how Dev remembers it", is mostly Dev's colour with a thin slice for Marcus: "found it, reproduced it, wrote the patch". The second, "how Marcus remembers it", gives Marcus about half: "reviewed it, knew the ledger, added the logging". The third, "listed out, step by step", shows six labelled slices, four of Dev's and two of Marcus's, which both of them agree on. A note under the first two says "each remembers their own part best". A banner reads "illustrative numbers: the direction is the finding".

The credit gap. The slices are invented for the story; what the research shows is the direction: each person in a joint task remembers their own part best, and listing every contribution step by step narrows the gap.
:::

Credit is not only distorted by memory, though. It is also distorted by bias, and the evidence on that is strong. Among academic economists, women who co-authored more papers, especially with men, became *less* likely to get tenure, while men's co-authorship carried no such penalty; follow-up experiments confirmed that people give women less credit for group work [@sarsons2021]. That is one profession, but the mechanism, an audience deciding who did the work of a group, is everywhere. Credit disputes are not only about two people's memories. They are also about whose contribution the room is inclined to notice.

So the first move in a credit dispute is to find out which problem you have: a memory problem, a bias problem or, occasionally, a theft. The first is by far the most common [!view], and it is fixed by talking.

::: scene {slug="INT. LANTERNFISH, A SMALL MEETING ROOM — WEDNESDAY, 9:15 AM"}
Dev has asked Marcus for ten minutes. She has written down what she wants to say, and she starts with the work, not with him.

@dev: Can I check something about the invoice fix? I want to make sure we've got the record straight, because it might come up in reviews.

"Sure," says Marcus.

@dev: The way I remember it, I found the race condition on the Saturday, reproduced it and wrote the patch, and you reviewed it, fixed my handling of the ledger lock and added the logging. Yesterday it sounded as if your team had found it.

Marcus is quiet for a moment. "I spent two days in that ledger code," he says. "In my head it was... mine. I genuinely didn't think about the Saturday. You're right. I'll fix it."
:::

That afternoon Marcus posts in the demo channel: *Correction to yesterday: Dev found and fixed the race condition; I reviewed and added the logging. Thanks, Dev, that Saturday saved us a lot of 3 am pages.* It gets more reactions than the demo did.

Look at what Dev did and did not do. She did not reply in the chat during the demo, where the audience would have watched a fight. She raised it privately, quickly and specifically. She described events, not motives: "the way I remember it", not "you took credit". She left Marcus room to have made an honest mistake, which he had. And she said why it mattered, which was not her pride but the record. This is the fix that research on over-claiming suggests, unpacking who did what step by step [@savitsky2005], turned into a conversation.

::: coming {ref=ch19}
Credit stops being a matter of pride in [[ch19]], where a promotion case has to show what *you* did inside work that many people touched, to a committee that was not there.
:::

The best defence against credit disputes, though, is to make them unnecessary.

:::: move {#ch16.move.credit} Share credit in writing
You have just finished a three-week project with two colleagues. Write the four- or five-line message you would post to the team, or send to your manager, when it ships. Make sure a reader who was not there could tell who did what.

::: answer
A strong version names specific contributions, including your own, without either boasting or hiding:

> The new export job is live. Priya designed the file format and talked two customers through it; Sam built the retry logic, which is why it survived last night's outage; I wrote the scheduler and the tests. Export failures are down from about 30 a week to zero so far. Thanks both.

Why it works: everyone's part is *specific*, which makes it believable and hard to dispute; your own contribution sits in a list with everyone else's, which is the least braggy way to record it; and the result comes with a number. It also corrects for the over-claiming bias in advance, because you did the unpacking for everyone [@savitsky2005].

Common weaknesses: "great teamwork, everyone!" (warm, but erases who did what, and in a biased room, vagueness tends to default to whoever is most visible [@sarsons2021]); listing everyone except yourself (kind, and it leaves your review with nothing to point to); or writing it only to your manager, when the team is the audience that will remember.
:::
::::

## Fight about the work, not each other {#ch16.sec.conflict}

The Marcus conversation worked partly because it stayed on the work. That turns out to be the most useful distinction in the whole research literature on conflict.

Researchers separate **task conflict**, disagreements about the work itself (what to build, how, what the data means), from **relationship conflict**, friction between people (irritation, distrust, personal dislike), and sometimes a third kind, **process conflict**, about who does what and when. An early field study of 105 work groups found that relationship conflict reliably hurt, while task conflict hurt groups doing routine work but not groups doing non-routine work, and that norms encouraging open conflict actually increased relationship conflict [@jehn1995].

For a while, textbooks taught that task conflict is good for teams. Then a 2003 meta-analysis found that task conflict, like relationship conflict, was negatively related to team performance and satisfaction [@dedreu2003]. A larger and more recent meta-analysis, of 116 studies covering 8,880 groups, untangled the two findings: relationship and process conflict are reliably bad, while task conflict has no reliable overall effect, and it can help, notably for the quality of decisions, when relationship conflict stays low [@dewit2012].

::: figure {#ch16.fig.conflict src="ch16/conflict.svg"}
Alt: A two-by-two grid. The horizontal axis is "task conflict: disagreeing about the work", from low to high. The vertical axis is "relationship conflict: friction between people", from low to high. Bottom left, "quiet": "fine, unless it's silence". Bottom right, shaded teal, "productive debate": "can improve decisions". Top left, "a feud": "people dislike each other, about nothing in particular". Top right, shaded coral, "the spiral": "every disagreement is personal". A dashed coral arrow labelled "the leak" runs from the productive-debate corner up to the spiral.

Task conflict and relationship conflict. Disagreeing about the work can help, but only in the bottom-right corner; the danger is the leak upwards, when an argument about the design becomes an argument about who is stupid.
:::

The practical skill, then, is not avoiding disagreement or encouraging it, but stopping the leak: keeping arguments about the work from becoming arguments about the people. That is easier to say than to do, because to the person on the receiving end, criticism of their design often *feels* like criticism of them.

::: myth {#ch16.myth.task-conflict verdict=partly grade=strong} Task conflict is good for teams
The claim has a kernel of truth and a large overstatement. Disagreement about the work has no reliable overall effect on team performance across 116 studies, and it can help decision quality and some kinds of team, but only when relationship conflict is low [@dewit2012]. An earlier meta-analysis found it negatively related to performance and satisfaction [@dedreu2003], and a field study found that norms encouraging open conflict increased relationship conflict [@jehn1995]. "Fight more about the work" is risky advice. "Disagree about the work in ways that do not become personal" is better advice, and much harder to follow.
:::

How do you stop the leak? A few habits follow from the research, though none of them has been tested as an intervention, so treat them as our synthesis [!view]:

- **Name the object of the disagreement.** "I think the retry logic will double-charge customers" is about the retry logic. "I don't think you've thought this through" is about you.
- **Separate the idea from its owner**, out loud if necessary: "This is my proposal, so feel free to tear it apart; I won't take it personally."
- **Make disagreement routine.** A team that disagrees every week about small things finds it easier to disagree about big ones without it feeling like a betrayal.
- **Repair quickly.** If an argument has got personal, say so and step back: "I think I got sharp there. Can we go back to the design?"

:::: move {#ch16.move.task-person} Separate the task from the person
Rewrite each of these so that it is about the work rather than the person, without losing the point.

1. "You always over-engineer things."
2. "Did you even test this?"
3. "This is the third time your team has missed the deadline."
4. "I don't think you understand what the customer needs."

::: answer
1. "I think we could ship a simpler version first: the plug-in system adds two weeks, and I'm not sure we'll need it this year. What am I missing?" (Specific, about the design, and it invites the other person to explain rather than defend.)
2. "I ran it against last week's data and it fails on refunds; can we add a test for that case?" (Turns an accusation into a fact and a request.)
3. "This is the third slip on this integration. Can we look at what's blocking it? If the estimates are wrong, I'd rather plan around better ones." (Still names the pattern, which matters, but points at the cause rather than the people.)
4. "My understanding from the customer calls is that they care most about speed, not configurability. Have you heard something different?" (Brings evidence and assumes the other person might have some too.)

The pattern: describe what you saw, say what it causes, and ask a real question. None of these rewrites is softer about the problem; they are more precise about it. Precision is what keeps a disagreement in the bottom-right corner of [[ch16.fig.conflict]].
:::
::::

## Politics, the honest version {#ch16.sec.politics}

::: scene {slug="INT. LANTERNFISH, THE KITCHEN — MONDAY, 8:50 AM"}
Lanternfish has hired a new engineer. Dev hears him before she sees him: a laugh she would recognise anywhere.

@rex: Dev! I *told* you we'd end up working together.

@dev: You told me no such thing. You told me Lanternfish was "a bit small for your vision".

@rex: Visions grow, Dev. Have you seen my new headline?

He shows her his profile. It says *Visionary-in-Residence*.

By lunchtime Rex has introduced himself to the head of sales, the facilities manager and the CEO, has been added to four chat channels, and has volunteered for the committee deciding what to do about Old Faithful.
:::

Rex is good at what most people call "office politics", and most people say the phrase with a sneer. The research treats it differently. Organisational psychologists define **political skill** as a measurable competence with four parts: *social astuteness* (reading people and situations), *interpersonal influence* (getting people to move), *networking ability* (building and using connections) and *apparent sincerity* (seeming to mean it). In the studies that developed the measure, political skill predicted managers' performance ratings and was unrelated to general mental ability [@ferris2005]. Meta-analyses have since found that it relates to job performance, career success, reputation and satisfaction, and predicts task performance beyond personality and intelligence [@munyon2015], with stronger links in more socially demanding jobs [@bing2011].

In other words, the social side of getting things done is a real skill, it is distinct from being clever, and it matters. Treating it as dirty does not make it go away. It just means that the people who are good at it, honestly or otherwise, decide more than their share.

The fourth component has an irony built into it. The research measures *apparent* sincerity, how sincere you seem. Our argument, which is the argument of Part II, is that the cheapest and most reliable way to seem sincere for years is to be sincere [!view]. Over one meeting, someone can perform sincerity. Over a hundred, the performance gets expensive, and the people watching are the same people every time.

Which influence tactics actually work? A meta-analysis of the research found that two had positive effects on work outcomes: **ingratiation** (being agreeable, complimenting, doing favours) and **rationality** (making a reasoned case with evidence); other tactics mattered only in particular situations [@higgins2003]. Ingratiation sounds grubby, and it can be; but in practice much of it is ordinary warmth, the "friendly colleague" from [[ch15]]. Rationality is the honest heart of politics: bring evidence, and bring it to the right people.

::: myth {#ch16.myth.eq verdict=partly grade=strong} Emotional intelligence matters more than IQ
Emotional skills matter at work, modestly. A meta-analysis found that measures of emotional intelligence correlate about .24 to .30 with job performance and add some prediction beyond cognitive ability and personality [@oboyle2011]. Another found that *ability-based* emotional intelligence predicts performance inconsistently: positively in jobs heavy in emotional labour, less so or even negatively in others, and that many popular "EQ" measures overlap heavily with personality and ability [@joseph2010]. None of that supports the claim that emotional intelligence matters *more* than general mental ability. Political skill, which is related but measured differently, is a better-evidenced way to describe the social competence people usually mean.
:::

### The Old Faithful committee {#ch16.sec.committee}

The coffee machine gives Dev a small, low-stakes lesson in all of this. The committee is five people: the facilities manager, someone from finance, Kai, Rex and Dev, who is there because she filed the repair ticket that nobody else would ([[ch12]]).

At the first meeting, Rex pitches an espresso robot with an app, a loyalty scheme and a price that makes the finance representative put down her pen. It is a wonderful pitch. It does not survive the question "what's the budget?", and the meeting ends with nothing decided.

Dev's approach is less exciting and works better. She pulls the ticket history: the machine has broken twenty-three times in five months, almost always the same part, and each repair has cost a morning of someone's time. Before the second meeting she talks to each committee member separately. She asks the facilities manager what a service contract would cost, asks finance what she could approve without a fight, and asks Rex whether his robot has a cheaper cousin. Then, at the meeting, she proposes a service contract now and a proper replacement fund for next year, credits the facilities manager for the contract quote and Rex for "making us think about what we actually want from coffee", and it passes in ten minutes.

That is political skill with nothing hidden in it: social astuteness (she knew finance's real constraint), rationality (she brought data), networking (she talked to people before the meeting rather than ambushing them in it) and generosity with credit, which costs nothing and corrects the bias from the start of this chapter.

::: craft
**Pre-wire the meeting.** Experienced people rarely bring a contested proposal to a meeting cold. They talk to each person who will be in the room beforehand, find out their constraints and objections, adjust the proposal, and make sure nobody is surprised. The meeting then confirms a decision rather than fighting over one. This is practitioner advice, widely followed, and not tested as far as we know. Its one rule: what you say in private must match what you say in the room. Pre-wiring with different stories for different people is not politics; it is a con, and in a repeated game it gets found out.
:::

Rex, for his part, takes the defeat of the espresso robot with total good humour, and two days later, at the coffee machine, gives Dev a piece of advice that is better than anything in his pitch.

@rex: That thing with Marcus. Smart. Never fight about credit in public. Thank people in public, fix the record in private.

Dev realises that Rex has been doing exactly that for years, and that he is genuinely good at it. She also notices that his first ticket at Lanternfish, closed with a flourish on his second day, has been reopened.

## Speaking up to people with power {#ch16.sec.voice}

Disagreeing with a peer is one thing. Disagreeing with your manager, or your manager's manager, carries a different kind of risk, and the research is honest about it.

In one field study and two experiments, managers rated employees who voiced *challenging* ideas, proposals to change how things were done, as worse performers than employees who voiced *supportive* ideas, and they endorsed the challenging ideas less; the difference was explained by whether managers saw the speaker as loyal or as threatening [@burris2012]. A wider review of why employees speak up or stay silent with concerns describes the same tension: voice helps organisations, and individuals often pay for it [@morrison2014].

That is not a reason to stay silent. It is a reason to raise challenges in a way that is heard as loyalty rather than threat. These suggestions follow from Burris's finding about loyalty and threat, but they are inferences, not tested scripts [!view]:

- **Lead with the shared goal.** "I want this launch to land with the warehouse clients, and I'm worried about one thing" frames you as on the same side.
- **Go private first.** A manager challenged in front of their own manager has to defend their position; one challenged in a one-to-one can change it.
- **Bring options, not just objections.** "Here are two ways we could reduce the risk" is harder to hear as an attack.
- **Disagree once, clearly, then commit or escalate.** Relitigating a decision every week is how a task conflict becomes a relationship conflict.

### Psychological safety {#ch16.sec.safety}

Whether people speak up depends a great deal on the team, not only on the person. Amy Edmondson defined **psychological safety** as a shared belief in a team that it is safe to take interpersonal risks, like admitting a mistake, asking a naïve question or challenging a plan. In a study of 51 teams in one manufacturing company, it predicted how much teams engaged in learning behaviour, which in turn predicted their performance [@edmondson1999]. A meta-analysis of 136 samples, covering more than 22,000 people and nearly 5,000 groups, has since found it related to performance and to going beyond the job, over and above related factors such as engagement [@frazier2017].

Psychological safety is not the same as comfort, though. One study found it also has a downside path: it can reduce average work motivation, which the authors called "slacking off in comfort", with the net effect depending on context [@deng2019]. The useful version is *safe to speak up*, not *safe from standards*. Tomás's squad, where people admit mistakes in stand-up and also get told when their work is not good enough, is the version that works.

::: myth {#ch16.myth.google verdict=partly grade=weak} Google proved psychological safety is the key to great teams
Google's re:Work guide describes an internal study of 180 teams, 115 in engineering and 65 in sales, which concluded that how a team worked together mattered more than who was on it, and ranked psychological safety first among five factors [@google2015]. But the study was internal, never peer-reviewed, and published without data or effect sizes, from one unusual company; the guide itself is now archived as a record. Psychological safety does matter, and the reason we know is the peer-reviewed research [@edmondson1999; @frazier2017], not Google. The grade on this verdict is for Google's study; the underlying idea has strong support.
:::

## Difficult people {#ch16.sec.difficult}

Some conflict is not about a decision or a piece of credit but about a person who makes everything harder. The research gives two reasons to take this seriously rather than shrugging it off.

First, rudeness is contagious and costly. In three experiments, people who experienced rudeness, or merely witnessed it, or were even asked to imagine it, performed worse on both routine and creative tasks and were less willing to help others [@porath2007]. Theory and later research describe how incivility spirals, with each rude act inviting a slightly ruder one back [@andersson1999]. Second, one persistently negative team member, someone who withholds effort, spreads negative mood or violates basic norms of respect, can damage the whole team, through a sense of unfairness, a worse mood and lower trust [@felps2006].

What can you do about a difficult colleague, as a peer with no authority over them? Our suggestions, which are practitioner experience rather than tested rules [!craft]:

- **Don't join the spiral.** Answer rudeness with flat politeness, not an equal and opposite rudeness. It feels weak; it is the only move that does not escalate.
- **Move important things into writing.** A difficult person's version of events tends to drift. A short email after a conversation ("to confirm, we agreed X by Friday") protects you without accusing anyone.
- **Talk about the behaviour, once, privately.** "When you interrupted me three times in the review, I couldn't finish the point about the refunds" is specific, about an act, and hard to argue with.
- **Keep a dated note of incidents** if the pattern continues. You may never need it; if you do, nothing else will substitute for it.
- **Find out whether it is just you.** If several people have the same problem, it is a team problem, and it belongs with the person's manager.

Difficult *managers* are harder, because the power runs the other way. The leader-member exchange research shows that managers form relationships of very different quality with different people on the same team, and that these relationships matter for how people are treated and how they perform [@dulebohn2012]. A classic practitioner essay argues that it is worth managing that relationship deliberately: understanding your manager's goals, pressures and preferred way of working, as well as your own [@gabarro1980!]. Sometimes that fixes things. Sometimes the honest conclusion is that a manager is the problem, and then the choices are to escalate, to move teams, or to leave, which is the question [[ch02]] started with and [[ch17]] comes back to.

::: trapdoor
**The 11 pm message.** Conflict feels most urgent late at night, which is when people send the message that turns a disagreement into a feud. Write it if you must; send it in the morning, after reading it as if you were the recipient. Remember from [[ch13]] that people consistently overestimate how well their tone comes across in writing [@kruger2005]: the message that feels firm to you will read as furious to them.
:::

::: ask
Q: What if the difficult person is a high performer the company won't touch?

A: That happens, and it is one of the most demoralising things at work. Keep the dated notes, raise the pattern with your manager as a team cost rather than a personal complaint (the research on negative team members is useful here [@felps2006]), and protect your own work with written agreements. If nothing changes and it is affecting your health, that is information about the organisation, not about you.

Q: Isn't "pre-wiring" a meeting just manipulation?

A: It is manipulation only if you tell different people different stories, or hide what you are doing. Talking to people before a decision, so that their concerns shape it, is consultation. The test is simple: would you be comfortable if everyone in the meeting knew exactly what you had said to everyone else?
:::

## When something is actually wrong {#ch16.sec.wrong}

Not every conflict is a personality clash. Sometimes the problem is harassment, discrimination, bullying, fraud, a safety risk or a law being broken, and then the advice in the rest of this chapter (stay calm, assume good faith, keep it on the task) can become dangerous, because it treats a real wrong as a misunderstanding.

The research on unethical behaviour at work is clear that it rarely comes from one rotten person alone. A meta-analysis of more than thirty years of studies found that unethical choices come from individual characteristics ("bad apples"), from the nature of the moral issue ("bad cases") and from the environment, such as culture, incentives and leadership ("bad barrels"), together [@kishgephart2010]. And ordinary employees matter enormously in stopping it: in a study of corporate fraud in large US companies between 1996 and 2004, frauds were brought to light mostly by employees, the media and industry regulators, rather than by auditors or the financial regulator [@dyck2010].

Speaking up about wrongdoing is a different act from speaking up about a design, and it calls for a different path. The general shape, which is ours and not a legal procedure [!view]:

::: figure {#ch16.fig.escalation src="ch16/escalation.svg"}
Alt: A ladder with six rungs, from the bottom: "1. talk to the person, if it's safe"; "2. write it down: dates, facts, witnesses"; "3. your manager, or theirs"; "4. HR, or a formal grievance"; "5. the reporting channel: whistleblowing or ethics line"; "6. outside: a regulator, a lawyer, a public body". A dashed coral arrow labelled "skip" jumps from the bottom rung to the fourth. Below the ladder, a coral box headed "skip rungs when" lists: "harassment or discrimination", "safety or a crime", "the problem is your manager", "you fear retaliation". At the bottom, a teal note: "keep your notes at every rung", and a smaller one: "a general guide, not legal advice".

An escalation ladder. Most workplace problems are solved on the lowest rungs, but the rungs are not compulsory: for harassment, safety, crime, or when the problem is the person you would normally report to, go straight to the rung that can act. This is a general guide, not legal advice.
:::

The ladder's most important feature is the box underneath it. You do not have to "try talking to them first" if the person is harassing you, if someone is in danger, if the problem is your own manager, or if you have reason to fear retaliation. Retaliation is a real risk, which is why many legal systems protect people who complain. The rules differ a lot by country, and the Field Note below covers the regions we could verify.

::: field {regions="US, UK, EU, India"} Where to take it
**United States.** The Equal Employment Opportunity Commission says harassment based on protected characteristics becomes unlawful when enduring it becomes a condition of continued employment, or when it is "severe or pervasive" enough to create a work environment a reasonable person would find intimidating, hostile or abusive; petty slights and isolated incidents, unless extremely serious, usually do not meet that bar. Retaliating against someone for complaining or taking part in an investigation is itself unlawful [@eeoc-harassment]. In the 2025 fiscal year, retaliation was alleged in 54,350 of the 88,201 charges the EEOC received (61.6%), more than any other basis; these are allegations, not findings [@eeoc-charge-stats].

**United Kingdom.** Whistleblowing law protects workers who report wrongdoing "in the public interest", such as a crime, a danger to health and safety, or a cover-up, and the government's guidance now lists sexual harassment among protected disclosures. Personal grievances are generally not covered by whistleblowing law and go through your employer's grievance procedure; the Acas Code says to raise them formally, in writing, with a manager who is not the subject of the grievance, and gives workers a right to be accompanied at the meeting [@govuk-whistleblowing].

**European Union.** Under the Whistleblower Protection Directive (2019/1937), private-sector organisations with more than 50 workers must set up internal reporting channels, acknowledge a report within seven days and give feedback within three months, and whistleblowers are protected from retaliation. We read this in a European Parliament briefing rather than the Directive's own text, and national laws may go further [@eu-whistleblower2019].

**India.** Under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, every employer must set up an Internal Complaints Committee; a district Local Committee handles complaints from workplaces with fewer than ten workers and complaints against the employer, and a complaint is to be made in writing within three months of the last incident. We read this in the Ministry of Women and Child Development's handbook, not the Act itself [@india-posh2013]. For other wrongdoing, the Companies Act requires a "vigil mechanism" for reporting concerns only in listed companies and certain others, such as companies that accept public deposits or have borrowed more than ₹50 crore from banks and public financial institutions; most private companies are not required to have one [@india-companies177].

**Everywhere else**, and for the details in these regions: we did not verify the rules, and they change. Check an official source before you rely on any of this, and get advice for a specific case. [[more.sec.law]] says where to start.
:::

:::: move {#ch16.move.escalate} When to escalate
For each situation, decide which rung of [[ch16.fig.escalation]] you would start on, and why.

1. A colleague keeps scheduling meetings over your lunch break, apparently without noticing.
2. A senior colleague makes comments about your appearance in front of clients, and has done so three times.
3. You notice that the numbers in a report going to a customer have been changed to hide a missed service level.
4. Your manager takes credit for your work in a presentation to their boss.
5. A teammate who is going through a hard time has started snapping at people in meetings.

::: answer
1. **Rung 1.** Almost certainly a misunderstanding. "Could we avoid 12:30 to 1:30? That's my lunch" solves most of these.
2. **Rung 3 or 4, possibly skipping straight to 4**, and start rung 2 (notes) today. This is harassment territory, it is repeated, the person is senior, and it is happening in front of clients. You do not owe them a private chat first. Many people go to their own manager; if your manager is close to the person, or unresponsive, go to HR or use a formal grievance. The Field Note above summarises the regional rules we could verify.
3. **Rung 2, then rung 3 or 5**, depending on who changed the numbers. This is a possible integrity breach affecting a customer, exactly the kind of wrongdoing that employees are most likely to be the ones to spot [@dyck2010]. Write down what you saw, precisely and without speculation. If your manager is not involved, take it to them; if they are, or you are not sure, use the internal reporting channel. [[ch17]] looks at how these things usually start: with one small, reasonable-sounding step.
4. **Rung 2, then a careful rung 3**: a private conversation with your manager, using the credit-dispute approach from earlier in this chapter. It may be the memory problem; it may not be. If it keeps happening, and especially if it affects your review or promotion, the skip-level manager is a reasonable next step. Making your work visible in writing as you go ([[ch16.move.credit]]) is the best prevention.
5. **Rung 1, gently, or not at all for now.** This is a person under strain, not a wrong. A quiet "you seemed rough today, are you all right?" is kinder and more effective than any ladder. If it continues and is hurting the team, it becomes a conversation for your lead.

Most real situations are mixtures. The rule of thumb: the more harm, the more power the other person has over you, and the more it involves people outside the team, the higher you start.
:::
::::

## Answering the pause {#ch16.sec.pause}

What did your plan for Dev look like? If it involved replying in the demo chat, telling the squad what Marcus had done, or saying nothing and nursing a grudge for six months, you are in large company: those are the three most natural reactions. What Dev actually did was slower and less satisfying in the moment: wait a day, talk to him privately, describe the events rather than the motives, and let him fix the record himself. It worked because the problem was memory, not malice, which is the common case. If it had been malice, the same conversation would have produced useful evidence: a clear account, raised promptly, that nobody could call an ambush.

::: scene {slug="INT. LANTERNFISH, THE KITCHEN — FRIDAY, 5:30 PM"}
The service engineer has been and gone. Old Faithful, under contract for the first time in its life, makes a coffee that is almost good.

Rex raises his cup.

@rex: To the committee. I still say the robot would have changed lives.

@dev: It would have changed the budget.

@rex: Same thing, at the right scale.

He wanders off to help someone in sales with a slide deck, cheerfully, for an hour. Dev looks at his reopened ticket on the board, now two weeks old, and thinks about the gap between how much Rex helps people and how much of his own work gets finished. It is the first time she has watched his film rather than his trailer, and it is more complicated, and more likeable, than she expected.

Then she looks at her own week, and finds a gap of a different kind.
:::

Dev has learned to fight about the work and not the people, to keep a record, to do politics in the open and to know when something belongs higher up the ladder. What she has not learned yet is when to stop: how much helping is too much, what happens when the pressure to cut a corner comes from a deadline everyone shares, and how to stay herself when the job starts to push back. That is [[ch17]], the last chapter of the long game.

::: rewind
- **Most credit disputes are memory, not theft.** People remember their own contributions best and over-claim in good faith; credit is also biased, notably against women in group work. Raise it privately, describe events not motives, and unpack who did what.
- **Share credit in writing, specifically, including your own part.** It prevents disputes and corrects the bias in advance.
- **Fight about the work, not each other.** Relationship and process conflict reliably hurt teams. Task conflict can help decisions only when it doesn't leak into relationship conflict; "task conflict is good" is overstated.
- **Political skill is real, measurable and distinct from intelligence.** Reasoned argument and ordinary warmth are the influence tactics that work. The cheapest way to seem sincere for years is to be sincere.
- **Challenging voice carries risk.** Frame it around shared goals, go private first, bring options, disagree once and then commit or escalate. Psychological safety means safe to speak up, not safe from standards.
- **Rudeness spreads, and one negative member can sink a team.** Don't join the spiral; move important things into writing; keep dated notes.
- **When something is actually wrong, use the ladder, and skip rungs** for harassment, discrimination, safety, crime, a problem with your own manager, or fear of retaliation. The rules differ by country; check an official source.
:::

::: further {ref=more.sec.law}
This chapter points at the law but cannot advise on it. [[more.sec.law]] lists official starting points for employment rights and workplace disputes in the regions the book covers, and says where to get advice on a specific case.
:::
