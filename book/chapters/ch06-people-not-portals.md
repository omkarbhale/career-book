---
id: ch06
status: review
---

::: scene {slug="INT. DEV'S FLAT — TUESDAY, 11:15 PM"}
The job ad is perfect, which is the problem. *Backend Developer, Lanternfish. Help us build the software that keeps 4,000 lorries on time.* Testing background welcome. Python. Queues. Dev has a story in her story bank for every line of it, and a résumé that finally says what she did instead of what she was for.

Under the button that says **Apply** there is a small grey line: *Over 200 applicants.*

She has read [[ch03]]. She knows what 200 applicants means. She can feel her new, honest, carefully evidenced résumé sliding into a pile the size of a small town.

Her phone buzzes. It is Rex, who started his new job on Monday and has already updated his profile.

@rex: New headline. Be honest. "Chief Possibility Officer."

@dev: What does it mean?

@rex: That's the beauty of it. Nobody knows. They have to message me to find out.

Dev puts the phone face down. Then she picks it up again, because something in the ad has snagged. *Lanternfish.* She scrolls the company's people page, and there, third row, is a face she knows: Ana, from her second-year databases course, who once lent her a charger during an exam and whom she has not spoken to in five years.

@dev: I can't message her. That would be using her.
:::

Dev has just met the most over-performing channel in hiring, and her first instinct is to treat it as cheating. Most decent people have the same instinct. This chapter is about why it is wrong, and about the part of it that is right.

The short version: a large share of jobs are filled through people, not portals, and the evidence for that is strong. But the reason has little to do with schmoozing and a lot to do with what [[ch01.sec.signals|Chapter 1]] called signals. A referral is a signal sent by someone who has watched part of your film. Your job is not to "network". It is to let the people who already know your work say so, and to ask them well.

::: pause
Before you read on: think of ten people who know your work, however slightly. If you sent each of them a short, polite message asking for a small, specific piece of help, how many do you think would say yes? Write down a number. You will check it at the end of the chapter.
:::

## The portal and the person {#ch06.sec.portal}

Start with what Dev was about to do: press Apply and join the 200.

In [[ch03]] you met the funnel from the employer's side. Here is the same funnel, split by how candidates arrived. In one large US corporation that tracked the source of all 62,127 of its applicants, people referred by a current employee were **6.1% of applicants**, but 21.4% of the people interviewed, 27.3% of the people offered jobs and **29.1% of hires**. Applicants from internet job boards were the mirror image: 60.1% of applicants and 23.5% of hires [@brown2016].

::: figure {#ch06.fig.referral-funnel src="ch06/referral-funnel.svg"}
Alt: Two stacked bars side by side, one for applicants and one for hires, from one large US firm. In the applicants bar, job boards fill 60.1% and referrals a thin coral sliver of 6.1%. In the hires bar, job boards shrink to 23.5% and referrals grow to 29.1%, the largest single slice. A label between the bars says "referred: 6.1% of who applies, 29.1% of who gets hired". A third segment in each bar, "everything else", covers the company website, applying on your own initiative, campus recruiting and other channels: 33.8% of applicants and 47.4% of hires.

The referral effect, in one firm's numbers [@brown2016]. Referred candidates were a sliver of the people who applied and the biggest single group of the people hired. Every stage of the funnel tilted their way.
:::

That is one company, so check it against others. In a recruiting-software vendor's customer data for 2024, referrals were 1.64% of applications and 17.09% of hires [@gem2025]. In data from more than 60,000 small businesses, referrals were 2% of applicants and 11.3% of hires [@careerplug2025]. Both vendors sell recruiting software, and their customers are not a random sample of employers, so treat the exact numbers loosely. The direction is the same in all three: **a referred candidate is worth several cold ones**.

There is a second detail in those numbers that matters as much as the first. Job boards still produced roughly a quarter of hires in the large firm and in the vendor data, and more than two-fifths in the small-business data [@brown2016; @gem2025; @careerplug2025]. Portals work. They just work at a much lower yield per application. You do not have to choose between applying and asking; you have to stop treating applying as the only move.

## Why a referral works {#ch06.sec.why}

It is tempting to think a referral works because hiring is corrupt: friends hire friends, and the rest of us queue. Some of that happens, and we will come back to it. But the best evidence says the main mechanism is more boring and more useful. **A referral carries information that a résumé cannot.**

A study of nine large firms in call centres, trucking and high-tech found that referred workers were 10% to 30% less likely to quit than other hires, and did markedly better on rare but important measures such as patents and avoiding truck accidents, while being about the same on ordinary productivity [@burks2015]. When the researchers tested *why*, the evidence pointed to matching: referrers sent people who fitted the particular job, and people like themselves [@burks2015]. Field experiments in an online labour market reached a similar conclusion: referrals carried information about how well and how persistently someone would work that the employer could not get from the worker's profile [@pallais2016].

Now connect that to [[ch01.sec.signals]]. A strong signal is specific, checkable and costly to fake. A referral from someone who has worked with you scores on all three. It is specific ("she rebuilt our regression suite"), it is checkable (the hiring manager can ask the referrer), and it is expensive, because the referrer is spending their own reputation. If you turn out to be a disaster, it is their judgement that looks bad. That is why employers weight it so heavily, and why [[ch01.move.signal]] rated "a former manager who vouches for you" as the strongest signal on the list.

Two consequences follow, and both shape how you should ask.

- **A referral is only as good as what the referrer knows.** "I don't really know her, but sure, put my name down" carries almost none of that information. The best referral comes from someone who has seen your work [!view].
- **A referral gets you looked at, not hired.** The biggest lift in the firm data is at the door: referred candidates were a far larger share of interviewees than of applicants [@brown2016]. After that you still have to interview, which is the subject of [[ch07]].

::: myth {#ch06.myth.who-you-know verdict=partly grade=strong} "It's not what you know, it's who you know"
Half true, and the half that is false is the important half. Who you know clearly matters: referred candidates were 6.1% of applicants and 29.1% of hires in one firm [@brown2016]. But referrals mostly work by carrying information about what you know and how you work, which is why referred hires fit the job better and quit less [@burks2015; @pallais2016]. A contact who cannot vouch for your work opens a door that your work then has to walk through. The better version: **it's who knows what you can do.**
:::

## Weak ties, strong ties {#ch06.sec.ties}

So who should you ask? The classic answer comes from a 1973 paper with one of the best titles in social science: "The strength of weak ties".

Mark Granovetter studied professional, technical and managerial workers in a Boston suburb who had recently changed jobs. Among the 54 who had found their job through a personal contact, only 16.7% saw that contact often; 55.6% saw them occasionally and 27.8% rarely, once a year or less [@granovetter1973]. His explanation was structural. Your close friends know the same people and hear the same news you do. Your acquaintances move in other circles, so they are the ones who hear about things you have not heard about [@granovetter1973].

That was 54 people, in one suburb, in the early 1970s. Nearly fifty years later the idea got a much bigger test. LinkedIn randomly varied the "People You May Know" suggestions shown to more than 20 million users, which changed how many weak and strong ties people formed, and then tracked who later moved to a connection's company [@rajkumar2022]. Weak ties did help, but not in a straight line. The relationship was an **inverted U**: moderately weak ties (people with whom you share a few mutual connections) were the most useful, and both the very weakest and the strongest were less so. Weak ties mattered more in digital industries; strong ties mattered more in less digital ones [@rajkumar2022].

A study of 6 million Facebook users adds the last piece. Most people who got help finding a job got it through a weak tie, simply because they had so many of them, but any single strong tie was worth more than any single weak one [@gee2017]. Both things are true at once: you have dozens of acquaintances for every close friend, so most help *arrives* through acquaintances, even though each friend is more likely to help.

::: figure {#ch06.fig.tie-map src="ch06/tie-map.svg"}
Alt: A target diagram with Dev's avatar at the centre. The inner ring, labelled "strong ties", holds Bea and Meera. The middle ring, shaded gold and labelled "moderately weak ties: the sweet spot", holds dots labelled "Ana, from uni" (in coral), "ex-teammate", "a Corvid client" and "meetup organiser". The outer ring, labelled "very weak ties" and "a name, a like, a badge", holds faint dots. A note at the side reads "most job help arrives from the middle ring, because there are so many people in it".

A tie map. The middle ring is where most new information lives: people who know you a little, move in other circles, and would still recognise your name. Ana is in it.
:::

Put the three studies together and the advice gets specific. The people most likely to know about a job you have not heard of are the ones on the edge of your network: the ex-colleague from two jobs ago, the person from your course, the client you got on well with, the organiser of the meetup you went to twice. Ana, in other words. Your best friend may be more willing, but they hear the same news as you.

::: myth {#ch06.myth.weak-ties verdict=partly grade=strong} "Weak ties are always better than strong ties"
Overstated. Granovetter's insight holds up: acquaintances carry new information [@granovetter1973]. But the large LinkedIn experiment found an inverted U, with *moderately* weak ties most useful and the weakest ties less so, and strong ties more useful in less digital industries [@rajkumar2022]. On Facebook, each strong tie was worth more than each weak tie, even though most help came through weak ties because people had so many [@gee2017]. Ask widely, but do not skip your friends.
:::

One honest caveat about all of this. In the LinkedIn experiment, the chance that any single new connection led to a job was a fraction of one per cent [@rajkumar2022]. Ties matter in aggregate, over years. Adding 300 strangers on a Tuesday night is not a job search; it is a Tuesday night.

## The "hidden job market" {#ch06.sec.hidden}

If you have read any careers advice at all, you have met a number that sounds like a conspiracy: 70%, or 80%, or 85% of jobs are never advertised. It is usually followed by a course you can buy.

The mechanism behind the claim is real. Surveys of job seekers have consistently found that **50% to 60% of workers report using a referral or contact** to find their job [@lester2021]. In most European countries, between a quarter and two-fifths of people heard about their current job through informal contacts [@pellizzari-via-brown2016]. Referrals and internal moves together are a large share of hires in employer data [@gem2025].

But "found through a contact" is not the same as "never advertised". Plenty of jobs are posted publicly *and* filled by someone a current employee recommended. And the percentage itself has no traceable origin: one review of the claim concluded that it "likely originated from anecdotal evidence and informal surveys rather than rigorous, peer-reviewed research" [@fresnostate2024-hidden!].

::: myth {#ch06.myth.hidden-market verdict=partly grade=strong} "80% of jobs are never advertised"
The percentage is unsupported; the mechanism is real. Nobody has traced the 70–80% figure to a study [@fresnostate2024-hidden]. What the evidence does show is that half or more of workers use a contact to find a job [@lester2021], and that referred candidates are hugely over-represented among hires [@brown2016]. Many of those jobs were advertised too. So keep applying, and also ask: the two are not alternatives. (The grade is for the evidence on the mechanism; the percentage itself has none.)
:::

## Asking for help, and why you are wrong about the answer {#ch06.sec.asking}

Back to Dev, staring at Ana's photo. Her objection was not really "this is unfair". It was "this is awkward, and she'll say no, or she'll say yes and resent it".

On the first part, the evidence is clear that she is probably wrong. In a series of studies, with requests made both in the lab and out in the field, people who needed help underestimated how likely others were to agree to a direct request, by as much as half. The reason was a blind spot: they thought about what saying yes would cost the helper, and forgot what saying no would cost them [@flynn2008]. And after conversations, people tend to underestimate how much the other person liked them, a "liking gap" that lasted for months among new university room-mates [@boothby2018]. Put together: you are probably more liked than you think, and people are more willing to help than you think.

There is an ethical edge in that same finding, and it is worth taking seriously. If people say yes partly because refusing is costly, then a good ask makes refusing easy. That is not just politeness. It means the yeses you get are real ones, from people who actually want to help, which is the only kind of referral worth having [!view].

On the second part, resentment, the answer is in how you ask. A good ask is short, specific and easy to act on, and it leaves a clean exit.

::: figure {#ch06.fig.good-ask src="ch06/good-ask.svg"}
Alt: A chat message from Dev to Ana, annotated in four numbered parts. Part 1, "the bridge": "Hi Ana, it's Dev from second-year databases: you saved my exam with a charger." Part 2, "the specific ask": "I've seen Lanternfish is hiring a backend developer, and I'd love to apply. Would you be comfortable referring me, or telling me who to talk to?" Part 3, "make it easy": "I can send the link, my résumé and two lines on why I fit, so it takes you two minutes." Part 4, "the clean exit": "And if it's not a good time or you don't know my work well enough, no problem at all." A side note reads "four sentences, one ask, no guilt". A crossed-out bubble above reads "Hey stranger! Can I pick your brain sometime?"

Anatomy of a good ask. Each part does one job: remind them who you are, say exactly what you want, make it cheap to do, and make it easy to decline. The crossed-out version does none of them.
:::

Each of the four parts earns its place.

1. **The bridge** reminds them who you are and why you are writing to them rather than to anyone else. Specific beats warm: the shared course, the project, the conference talk.
2. **The specific ask** says exactly what you want. "Would you refer me for this role?" can be answered. "Can I pick your brain?" is a request for an unspecified amount of an unspecified thing, and the honest answer to it is usually "not this month".
3. **Make it easy** puts the work on you. A referrer has to fill in a form or forward an email; give them the link, your résumé and two true sentences they can paste. Those sentences are their reputation on the line, so make them specific and checkable ([[ch01.sec.signals]] again).
4. **The clean exit** gives them a dignified way to say no, or to say "I don't know your work well enough to refer you, but here's who's hiring". That second answer is often more useful than a reluctant referral.

The structure is craft rather than science: nobody has run a trial of four-sentence messages against five-sentence ones [!craft]. But each part follows from evidence you have now seen: referrals carry information, people are more willing than you expect, and a reluctant yes helps nobody.

::: trapdoor
**The ask that costs the asker nothing and the helper everything.** "Can I pick your brain?", "Do you know anyone hiring?", a request for a referral to a role you have not read, or a message to 40 people at once with the name changed. Each one hands the other person a job: working out what you want, whether you fit, and what to say. Most people quietly decline by not replying, and you learn nothing. Do the work first: read the role, decide what you are asking for, and write the two sentences you would want them to say.
:::

### Informational conversations {#ch06.sec.informational}

Not every ask is for a referral. Often the most useful thing you can ask someone in the middle ring is twenty minutes of their time: what is the team like, what does the job really involve, what would make an application stand out? This is sometimes called an informational interview, and it works for the same reasons a referral does. You learn things that are not on the job ad, and the other person gets to see a little of how you think.

::: craft
Running an informational conversation. Ask for a specific, short slot ("twenty minutes, any day next week"), come with three real questions you could not answer from the website, and stop on time. Ask about them and their work before you ask about openings. End with two questions: "Is there anyone else you think I should talk to?" and "Would it be all right if I followed up when I apply?" Then send a two-line thank-you that mentions something specific they said. None of this has been tested in a study; it is what experienced people on both sides of these conversations tend to recommend [!craft].
:::

## Give before you need {#ch06.sec.give}

The best time to ask someone for help is after you have spent years being someone they would want to help. This is where the snapshot game borrows from the long game, and it is the first place the [[ch01.sec.loop|loop]] becomes something you can act on.

Reciprocity is one of the oldest findings in social psychology. In a classic study, people who were given an unsolicited soft drink by a stranger later bought more of his raffle tickets, whether or not they liked him [@regan1971]. But the pull fades: in another set of studies, people repaid a small favour five minutes later, but showed no reliable pull to repay it a week later [@burger1997]. So reciprocity is not a bank account you can fill once and draw on for a decade. It is closer to a habit: small, frequent, honest exchanges that keep relationships warm.

That suggests a different picture of "networking" from the one most people dread. Not working a room of strangers with a stack of business cards, but a few cheap habits, kept up over years [!view]:

- **Help in small ways, often.** Answer the question in the team chat. Review the pull request. Send the article you read that made you think of them. Introduce two people who should know each other.
- **Keep the middle ring warm.** When a former colleague changes jobs, congratulate them. When you read something by a classmate, say so. A message every year or so is enough to keep someone in the middle ring instead of the outer one.
- **Refer other people.** When you see a role that fits someone you have worked with, tell them, and offer to refer them if you can honestly vouch for their work. It is the most direct way to be the kind of tie you hope to have.
- **Do work worth vouching for.** This is the big one, and it is the whole of Part II. Nobody can refer you warmly for work they never saw or did not rate.

::: craft {by=author} Why we think "networking" is the wrong word
"Networking" makes it sound like a separate activity, done in a separate place, by a separate, more extrovert version of you. We think that is why so many people hate it and so few do it well. Almost everything that makes a referral valuable happens in the long game: the work people saw, the help you gave, the way you behaved when things went wrong. The snapshot-game part is small and learnable: noticing a role, asking clearly, making it easy. So if the word makes you wince, drop it. You are not networking. You are letting people who know your work say so.
:::

## The fairness problem {#ch06.sec.fairness}

::: scene {slug="INT. CORVID SYSTEMS, KITCHEN — WEDNESDAY, 12:40 PM"}
Dev tells Bea about Ana while the kettle boils.

@bea: So the trick to getting hired is already knowing someone who works there.

@dev: The trick is someone who's seen your work saying so.

@bea: Which is easier if your parents' friends are engineers, you went to the right university and you play five-a-side with the hiring manager. I didn't, and I don't.

@dev: You have me.

@bea: I have you. Lucky me. What about everyone who doesn't have a you?
:::

Bea is right, and the book should say so plainly. People tend to refer people like themselves, in characteristics and even in behaviour [@burks2015]. In two firms' data, referral hiring could disadvantage women where an established male network was in place, and more so at higher levels, although overall, network recruitment brought more women in rather than fewer [@fernandez2019]. And the kind of contact matters: in US survey data, referrals from business contacts were used more for high-skill jobs and came with higher starting wages, while referrals from family and friends were used more for low-skill jobs, came with lower starting wages, and were relied on most by people who struggled to get offers through other channels [@lester2021].

So a referral-heavy labour market rewards people who already have professional networks, and those networks are not handed out at random. That is a real unfairness, and no amount of good advice makes it disappear.

What advice can do is shift who has those networks. If you are starting with few professional ties, the evidence points in a hopeful direction: the most useful ties are not intimate ones but moderately weak, professional ones [@rajkumar2022; @lester2021], and those can be built. Communities of practice (meetups, open-source projects, professional groups, alumni networks, online forums in your field) are places where strangers watch a little of your work and become the middle ring. A year of answering questions well in one of them builds exactly the kind of tie that can later say "I've seen what she can do" [!view].

And if you are on the inside, Bea's question is also addressed to you. When you refer, refer for evidence, not for familiarity, and look for good people outside your own circle. [[ch19]] will show that the same dynamic, people vouching for people like themselves, shapes who gets sponsored for promotion.

## Recruiters and agencies {#ch06.sec.recruiters}

Sometimes the person who reaches out is not someone you know but someone paid to find you. Recruiters come in two kinds, and it helps to know which is which.

**In-house recruiters** work for the employer. When one of them contacts you, you have been "sourced": someone looked at your profile and decided you were worth a message. In one vendor's 2024 data, sourced candidates were hired at 2.0% against 0.4% for people who applied cold, five times the rate [@gem2025]. Most of that is selection (the recruiter picked you because you looked like a fit), but it means a findable, accurate profile is a channel in its own right. [[ch05]] covers what makes a profile worth finding.

**Agency recruiters** work for a separate firm that the employer pays when it hires someone they introduced. The fee is usually a percentage of the new hire's first-year pay: "contingent" agencies are paid only if a hire happens, while "retained" search firms are paid in instalments and usually cost more in total. One fee guide written for agencies gives examples in the range of 18% to 25% [@topechelon-fees!]. That is illustrative rather than survey data, but it tells you whose money is on the table.

That incentive shapes the relationship. An agency recruiter wants you placed, and quickly, which is often what you want too. It is not always aligned with your interests on which job is right for you, or on how hard to push on salary when a quick yes earns the fee [!view]. Treat a good agency recruiter as a useful, knowledgeable ally with a commission, which is exactly what they are.

::: field {regions="UK, US"} Who pays the recruiter
In Great Britain the rule is explicit: "Recruitment agencies cannot charge you a fee for finding or trying to find you work." They can charge for optional extras such as CV writing or training, and entertainment and modelling agencies have separate rules [@govuk-agency-fees]. In the US, agency fees are normally paid by the employer, typically as a percentage of first-year pay [@topechelon-fees]. We did not verify the rules for India or the rest of the EU. Wherever you are, treat a request for an upfront "placement fee" as a reason to stop and check [!view].
:::

## Dev writes to Ana {#ch06.sec.ana}

::: scene {slug="INT. DEV'S FLAT — WEDNESDAY, 9:05 PM"}
Dev has written the message four times. The first version was 300 words and apologised twice. The second asked Ana to "keep her in mind", which Dev realised would require Ana to remember her. The fourth is four sentences long. It mentions the charger.

She sends it at 9:05 and opens her spreadsheet to have something to do with her hands. She adds a tab called *People* and starts listing names: Ana; two former teammates who left Corvid; the client tester she got on well with; Bea, obviously; the organiser of the testing meetup she went to twice.

At 9:52 her phone buzzes.

> *Dev! Of course I remember. The charger was the best investment I made that year. I'm on the platform team, not backend, but I know Tomás who's hiring and he's lovely. Send me the stuff and I'll put you in today. Also, honestly, it's nice to hear from you.*

@dev: Bea. She said yes. In under an hour.

@bea: Of course she did. You were nice to her once and you asked properly.

@dev: That can't be all it is.

@bea: It isn't. Now you have to be as good as the two sentences she's about to paste.
:::

Dev's experience is an anecdote, but it is exactly the pattern the research predicts: a moderately weak tie, a specific ask, a quick yes from someone happier to help than Dev expected. Notice what made it work: not Dev's charm, but the fact that the two sentences she gave Ana were true. In the next chapter she has to live up to them in a room with Tomás.

::: coming {ref=ch07}
A referral gets you into the room. [[ch07]] is what happens there: what interviews actually measure, how to tell a story that lands, and what to do about nerves.
:::

## Your moves {#ch06.sec.moves}

:::: move {#ch06.move.tie-map} Map your ties
Draw three rings on a page, like [[ch06.fig.tie-map]], with you at the centre.

1. In the **inner ring**, write up to five people who know you well: close colleagues, friends in your field, a mentor.
2. In the **middle ring**, write as many people as you can who know you a little and have seen *some* of your work: former teammates, classmates, clients, people from a community you take part in. Aim for twenty.
3. Next to each middle-ring name, write one specific thing they have seen you do.
4. Circle the three middle-ring people most likely to hear about roles you want.

::: answer
Most people find the inner ring easy and the middle ring surprisingly long once they start: former colleagues from two jobs ago, the person who reviewed your code once, the classmate who went into your target industry. If your middle ring has fewer than ten names, that is useful information, not a verdict. It tells you where the long-game work is: picking one community and showing up in it regularly.

The third step is the important one. A name you cannot attach to a piece of work is an outer-ring tie wearing a middle-ring label. Those people may still pass on news of a job, but they cannot vouch for you, so ask them for information ("Is the team hiring? Who should I talk to?") rather than a referral.
:::
::::

:::: move {#ch06.move.ask} Write a four-sentence ask
Pick one real person from your middle ring and one real role. Write a message to them using the four parts in [[ch06.fig.good-ask]]: the bridge, the specific ask, make it easy, and the clean exit. Four sentences, no apologies.

Then check it against these questions. Could they answer it with "yes" or "no"? Could they act on it in two minutes? Would a "no" feel easy to send?

::: answer
Here is a version for someone you know less well than Dev knows Ana:

> *Hi Sam, we met at the testing meetup in March, when you gave the talk on flaky tests. I've seen your team is hiring a QA lead and I'm planning to apply; would you be open to a 15-minute call about what the team needs, or to pointing me to the right person? I've put the role and a short summary of my background below so you don't have to look anything up. And if you're swamped, no worries at all.*

Notice that it asks for information, not a referral, because Sam has seen Dev's questions at a meetup, not her work. A referral request would put Sam in an awkward spot. The most common weaknesses in first drafts are an ask that is too vague ("any advice?"), too big ("could you get me an interview?"), or buried in the third paragraph. If yours runs to more than five sentences, the extra ones are probably apologies. Cut them.
:::
::::

Now return to the number you wrote down at the start of the chapter.

:::: move {#ch06.move.guess} Guess, then check
At the start of this chapter you guessed how many of ten people would say yes to a short, specific request for help.

This week, send three asks from your *People* list: one for information, one for an introduction and, if there is someone who genuinely knows your work, one for a referral. Write down your prediction for each before you send it. Record what happens.

::: answer
If you are like the people in Flynn and Lake's experiments, your guess was too low: they underestimated how likely others were to agree to a direct request by as much as half [@flynn2008]. Your setting differs from theirs, so your numbers will too: a message is easier to leave unanswered than a request made to someone's face, and some people will simply not see yours. Silence is not a no; one polite follow-up after a week is normal.

The point of the exercise is calibration. Most people who avoid asking are not avoiding rejection; they are avoiding a rejection that is much less likely than they think. The only way to update that belief is to collect your own data. Dev's first datapoint took 47 minutes.
:::
::::

::: ask
Q: Isn't asking for a referral just using people?

A: Not if what you ask them to say is true and you make it easy to decline. Employers run referral schemes because referrals help them hire people who fit and stay [@burks2015]. You are giving your contact a chance to help their own team. The line is crossed when you ask someone to vouch for work they have not seen, or pressure them when they hesitate.

Q: I'm an introvert. Do I have to go to networking events?

A: No. The evidence is about ties, not events, and the most useful ties are people who have seen your work [@rajkumar2022; @burks2015]. Writing, code, answering questions in a forum and doing good work alongside people all build them, quietly.

Q: What if someone refers me and I don't get the job?

A: That is normal. A referral gets you looked at; it does not get you hired. Thank them either way, tell them how it went, and you have kept a tie warm for next time.

Q: Should I connect with the hiring manager before I apply?

A: If you have a genuine reason (a mutual contact, a shared community, something they wrote that you can respond to), a short, specific message is fine. A cold "I've applied, please look at my application" mostly adds to their inbox [!craft].
:::

Dev's *People* tab is not finished, and it never will be. That is the point. The snapshot game is about to get much more intense for her, but the tab she just started will matter long after it ends. In [[ch15]] some of these people become friends; in [[ch19]] a few of them become the people who vouch for her on the inside, which turns out to be how promotions work too; and in [[epi]] it is Dev's turn to be someone's Ana.

::: rewind
- Referred candidates are a sliver of applicants and a large share of hires: **6.1% of applicants and 29.1% of hires** in one large firm, with the same direction in vendor data.
- Referrals work mainly because they carry **information about fit** from someone who has seen your work; referred hires fit better and quit less. A referral is a strong signal because the referrer's reputation is on the line.
- **Moderately weak ties** (former colleagues, classmates, people who know you a little) help most; strong ties still matter, especially outside digital industries.
- The "80% of jobs are never advertised" figure has no traceable source; what is true is that half or more of workers find jobs through contacts. **Apply and ask**; they are not alternatives.
- People **underestimate how willing others are to help**. A good ask has four parts: the bridge, the specific ask, make it easy, and a clean exit.
- Reciprocity fades, so **give small and often**. Networking is mostly the long game: being someone people can honestly vouch for.
- Referral hiring **favours people who already have networks**. Build professional ties in communities of practice, and when you refer, refer for evidence.
- In-house recruiters work for the employer; agency recruiters are paid by the employer, usually a share of first-year pay. In Great Britain they may not charge you for finding work.
:::
