---
id: ch01
status: final
---

::: scene {slug="INT. CORVID SYSTEMS, THIRD FLOOR — 7:40 PM"}
The office has the particular quiet of a building where everyone sensible has gone home. Dev is still at her desk, reading the same email for the third time.

> *Thank you for your interest in the Backend Engineer role. After careful consideration, we have decided to move forward with other candidates whose experience more closely matches our needs.*

She had wanted this one. The job description could have been written about her: the test harness she rebuilt last year, the flaky deployment scripts she quietly fixed, the queueing bug she found before the client did. She had applied with a carefully edited résumé and a cover letter she read aloud twice. Now it is row 47 of her spreadsheet, and like 45 of the 46 rows above it, the status column says *no*.

At the next desk, Rex is choosing between three offers.

@rex: One has a slide between floors. One has a four-day week. One has a CEO who used to be in a band. Which says "growth opportunity" to you?

@dev: The four-day week says "growth opportunity" to me.

@rex: See, you get it. You just have to play the game, Dev.

He means it kindly. That is the annoying part. Dev knows Rex's work: his code reviews are three words long and his tickets tend to reopen a week after he closes them. And she knows Bea's work, across the aisle: Bea, who rewrote the billing engine in a fortnight and mentioned it to nobody. Bea has been turned down after four phone screens in a row.

@dev: Rex has three offers. Bea has none. That's not a game. That's a bug.
:::

Dev is half right. It is a bug, if you think hiring exists to find the best person for the job. But it is also a game, in the precise sense of the word: a situation with rules, players and moves, where how well you play depends on understanding the rules rather than on wishing they were different.

This chapter is about why Rex wins that game and Bea loses it, why neither of them should copy the other, and why there are really *three* games that you will play over and over for the rest of your working life. Everything else in the book hangs off this idea, so it is worth getting right.

::: pause
Before you read on: why do you think Rex keeps getting offers and Bea keeps getting rejected? Write down two guesses, even rough ones. You will get to check them in a few pages.
:::

## The puzzle {#ch01.sec.puzzle}

If hiring did what it says on the tin, Bea would be buried in offers. She is better at the job than Rex by any measure that her colleagues would recognise: the code she writes, the problems she solves, the people she quietly unblocks.

Hiring does not see any of that. It sees a two-page document, a profile, a forty-minute phone call, perhaps a coding exercise and an afternoon of interviews with people who met her that morning. From those fragments, a group of strangers has to predict how she will perform over the next few years. Bea is very good at the job and not very good at those fragments. Rex is the other way round.

That is the puzzle in one sentence: **the skills that get you a job are not the same as the skills that make you good at it.** They overlap, sometimes a lot, but they are not the same skills, and they are not judged the same way. Once you see that, a great deal of career advice that sounds contradictory stops being contradictory. "Be yourself" and "polish your pitch" are not in conflict. They are instructions for different games.

## Three games {#ch01.sec.three-games}

Call the first one **the snapshot game**. It is everything between "I'd like a new job" and "I accept": deciding what to aim for, getting noticed, the résumé and the profile, the referral, the interviews, the work sample, the offer and the negotiation. Its defining feature is compression. People who do not know you judge you from a small, edited sample over a few hours, spread over a few weeks.

Call the second one **the long game**. It is everything after "I accept" that happens between people: the first week and the five-hundredth, the meetings, the messages, the deadlines met and missed, the colleague who becomes a friend, the manager who becomes a reference. Its defining feature is repetition. People who know you judge you from everything you do, every day, for years.

The third game hides inside the second. Call it **the career game**: being genuinely good at the work, and having that count. It is the performance review, the promotion case, the choice of what to get good at next, the day someone asks whether you want to manage people. Its defining feature is the cycle. Once or twice a year, people with a rubric and a budget look back at months of your work and write it down in a paragraph and a rating.

::: figure {#ch01.fig.three-games src="ch01/three-games.svg"}
Alt: Three bands, one per game. The snapshot game, Part I, drawn as an instant photo of Dev with a résumé and a stopwatch: judged by strangers, in hours; they see a trailer you edit; what wins is clear, honest signals. The long game, Part II, drawn as a film strip of everyday moments: judged by colleagues, every day; they see the whole film, uncut; what wins is being reliably yourself. The career game, Part III, drawn as a staircase rising to a star beside a checklist: judged by managers and panels, in cycles; they see the film, summarised; what wins is good work, made visible.

The three games compared. Each band is the argument of one part of the book in miniature.
:::

A film metaphor helps here, and we will lean on it throughout. In the snapshot game, employers see your **trailer**: a short cut of your best scenes, edited by you. In the long game, colleagues watch the **film**: all of it, including the slow middle and the bits you would have cut. In the career game, the film gets **reviewed**: someone who has seen parts of it writes the summary that decides what you get to make next.

The trailer, the film and the review are judged by different audiences, on different evidence, at different speeds. So they reward different skills.

| | The snapshot game | The long game | The career game |
| --- | --- | --- | --- |
| Rewards | making your value easy to see quickly | creating value reliably, with other people | getting good at work that matters, and making it visible |
| Punishes | being vague, being nervous, being invisible | being unreliable, being unkind, being fake | invisible work, drifting, the wrong next role |
| Main skill | translation: turning real work into clear evidence | conduct: how you behave when it counts and when it doesn't | judgement: what to get good at, and how to show it |
| Where it lives | Part I, Chapters 2 to 9 | Part II, Chapters 10 to 17 | Part III, Chapters 18 to 22 |

You may have noticed that "being fake" appears only in one column. That is not an accident, and we will come back to it.

## Why the snapshot game is so noisy {#ch01.sec.noise}

Start with the employer's problem, because it explains most of what feels unfair about hiring.

An employer hiring you is placing a bet on how you will perform in the future, using evidence gathered over a few hours today. The economist Michael Spence, who won a Nobel prize partly for thinking about exactly this, put the difficulty plainly: the value of individuals to firms "is not directly observed, at least at the time of hiring" [@spence2001-lecture]. Employers cannot watch the film before they buy the ticket. They have to infer it from signals.

How good are they at inferring? Organisational psychologists have been measuring this for decades, by comparing how candidates scored on a selection method with how they performed on the job later. The most recent big revision of that research, a re-analysis of the meta-analyses, concluded that earlier estimates had been too optimistic and cut most of them by .10 to .20 [@sackett2022]. The best single method left standing was the **structured interview**, in which every candidate gets the same job-related questions, scored against the same scale. Its estimated correlation with later job performance, after the standard statistical corrections, is **.42** [@sackett2022; @sackett2023-iop].

A correlation of .42 is a respectable number in this field, and it is easy to misread. Here is what it looks like.

::: figure {#ch01.fig.correlation src="ch01/correlation.svg"}
Alt: A scatter plot of 150 simulated people, with interview score on the horizontal axis and job performance a year later on the vertical axis. The cloud of dots slopes upward with a dashed trend line labelled "trend: r = .42". A few dots in the top left are highlighted in teal and labelled "fumbled the interview, star on the job"; a few in the bottom right are highlighted in coral and labelled "aced the interview, struggled on the job".

What a correlation of .42 looks like. The people are simulated, but the relationship has the strength of the best single selection method in the 2022 review. The trend is real: higher interview scores go with better performance on average. So is the scatter around it.
:::

Look at the cloud rather than the line. On average, people who interview better do perform better, which is why structured interviews are worth using. But there are plenty of people in the top left, who would have been excellent and interviewed badly, and plenty in the bottom right, who interviewed beautifully and then struggled. Bea lives in the top left. Rex, on his less good days, visits the bottom right.

And that is the *best* method, on average. The researchers themselves warn that the figure is really ".42, plus or minus .24": in some settings structured interviews predict well, and in others they barely predict at all [@sackett2023-iop]. A casual, unstructured conversation, the kind many interviews still are, does markedly worse.

::: receipts {source=sackett2022} The validity league table, revised
**What they did.** Sackett, Zhang, Berry and Lievens re-examined the meta-analyses that employers and textbooks have relied on for decades to rank selection methods, and showed that a statistical correction (for "range restriction") had usually been applied too generously, inflating most estimates [@sackett2022].

**What they found.** Most methods that ranked high before still ranked high, but lost .10 to .20 of validity. Structured interviews moved to the top, at .42. Methods built around the specific job (structured interviews, job-knowledge tests, work samples) generally beat broad measures [@sackett2023-iop].

**What it cannot tell you.** These are averages across many studies and jobs, and the plausible range for structured interviews runs from .18 to .66, so any one company's process may be much better or much worse. They also describe each method used alone; most employers combine several, which predicts better [@sackett2023-iop].
:::

### What else the interview is measuring {#ch01.sec.what-else}

If interviews only partly measure how good you will be at the job, what else are they measuring? Some of the answer is useful: how clearly you explain your work, how you think on your feet, whether you are pleasant to talk to. Some of it is closer to luck. Two findings matter for Dev and Bea.

The first is **self-presentation**. A meta-analysis of the employment-interview research found that the impressions candidates create (through appearance, impression management, and verbal and nonverbal behaviour) shape interviewers' ratings, and concluded that "what you see in the interview may not be what you get on the job", with unstructured interviews especially affected [@barrick2009]. Even in *structured* interviews, candidates' self-promotion correlated .26 with their ratings across 13 studies [@levashina2014]. Rex self-promotes the way other people breathe.

The second is **nerves**. Across 30 studies, candidates who reported more interview anxiety got lower ratings from interviewers, with an average correlation of −.19 [@powell2018]. That is a small effect, not a death sentence. But Bea's phone screens go badly in a way her code reviews never do, and some of the reason is that she dreads them.

Put those together and the puzzle from the opening scene looks less like a bug. Rex is very good at exactly the things interviews over-reward. Bea is very good at the things they under-observe.

::: myth {#ch01.myth.best-candidate verdict=partly grade=strong} The best candidate gets the job
On average, better candidates do tend to win: that is what a positive validity coefficient means, and structured, job-related processes do better than gut feel [@sackett2022; @sackett2023-iop]. But for any single hire, the noise is large. The best single method predicts with a correlation of about .42, plus or minus .24 [@sackett2023-iop], and interview ratings also respond to self-promotion and nerves [@levashina2014; @powell2018]. The person who gets the offer is often not the person who would have done the job best. And merit is not the only thing that tilts the odds: [[ch03]] looks at the evidence that bias enters the funnel too.
:::

That much noise raises some fair questions, and one awkward one.

::: ask
Q: If hiring is this noisy, why bother preparing at all? Isn't it a lottery?

A: Noise is not the same as randomness. A noisy measure still moves with the thing it measures, which is why the trend line in [[ch01.fig.correlation]] slopes up. Preparation moves the parts you control: how clearly your evidence comes across, how much your nerves get in the way, and how many people can vouch for you. Part I is about exactly those parts.

Q: So should I just become more like Rex?

A: Learn what Rex is good at, yes. Become Rex, no. Keep reading: the second game is where that plan falls apart.

Q: I don't work in tech. Is this for me?

A: Yes. Dev happens to be an engineer, but the evidence in this chapter comes from research on all kinds of jobs.
:::

## Signals, not secrets {#ch01.sec.signals}

If employers can only see signals, the snapshot game is won by sending good ones. That raises an obvious worry: isn't "sending good signals" just a polite name for spin?

Spence's answer is useful here, and it turns on cost. A signal only tells an employer anything if it is harder to send for people who lack the quality it advertises. In his words, a signal can distinguish people because "the cost of the signal is negatively correlated with the unseen characteristic that is valuable to employers" [@spence2001-lecture]. A claim that everyone can make for free carries no information, however confidently it is made.

Look at Dev's résumé through that lens. "Detail-oriented team player with strong communication skills" costs nothing to write, and the person reading it knows that. Compare it with a line that is expensive to fake:

> Rebuilt the regression suite so it runs in 40 minutes instead of 6 hours; the team now tests every merge instead of once a night.

Anyone can type that sentence too. But only someone who did the work can survive the follow-up questions: *How did you parallelise it? What broke? What did you leave out, and why?* In the snapshot game, a specific, checkable claim is a strong signal precisely because it invites checking. That is the whole trick, and it is not a trick at all. You are not inventing value; you are **making real value legible**.

::: craft
Translate, don't fabricate. A useful test for any line on a résumé or any claim in an interview: could you happily spend five minutes being questioned about it? If yes, make it more specific. If the thought makes you nervous, the line is either vague (fix it with numbers, names and outcomes) or not quite true (cut it). Experienced hiring managers tend to probe hardest where a candidate sounds most polished.
:::

The difference between a signal and noise is easier to feel than to define, so try sorting a few.

:::: move {#ch01.move.signal} Signal or noise?
Here are eight things a hiring manager might see about a candidate for Dev's target role. For each one, decide: **strong signal** (specific, checkable, costly to fake, related to the job), **weak signal**, or **noise**. Commit to your answers before you open the reveal.

1. "Hard-working, passionate team player."
2. "Cut a nightly 6-hour test run to 40 minutes by running suites in parallel."
3. A link to a small open-source project with a year of commit history and a README explaining a design decision.
4. "Proficient in 14 programming languages."
5. "Found 212 defects in 2025, 31 of them rated critical by the client."
6. A former manager who, unprompted, tells the hiring manager the candidate was the person the team called when releases went wrong.
7. "Led a team of five."
8. A degree from a famous university, for a role that does not mention one.

::: answer
- **1. Noise.** Free to write, impossible to check, and on half the résumés in the pile.
- **2. Strong.** Specific, about a result rather than a duty, and easy to probe in an interview.
- **3. Strong.** A year of real history is expensive to fake, and the README shows thinking, not just typing. [[ch05]] and [[ch08]] look at what portfolios do and do not prove.
- **4. Weak, possibly negative.** A number this large invites doubt, and the reader cannot tell which of the fourteen you could use tomorrow.
- **5. Moderate.** Specific and checkable, but about activity more than outcome. What changed because of those defects?
- **6. Very strong.** Someone is risking their own reputation on yours, which is exactly why referrals carry so much weight. [[ch06]] has the evidence.
- **7. Weak.** Checkable, but it says nothing about what the team achieved or what leading meant.
- **8. A real signal, but of what?** It says something about the person at eighteen. Its weight here depends on the employer, which is the theme of [[ch03]].

Notice the pattern: the strong signals describe things that **happened**, in enough detail to be questioned, and some of them come from other people. That last point is the bridge to the second game.
:::
::::

If your honest signals are not getting through, there is a tempting shortcut. It is the most expensive mistake in the snapshot game.

::: trapdoor
**Upgrading the trailer.** When the honest trailer is not working, the temptation is to improve it with a slightly grander title, a rounder number, a skill you have read about. Resist it. Interviews probe, references get called and background checks exist ([[ch09]]). Even if none of that catches you, you will get the job the trailer promised, and then you will have to do it, in front of people who will watch the whole film [!view].
:::

## The long game {#ch01.sec.long-game}

Now turn the camera round. Suppose Dev gets the job. Everything that made the snapshot game hard flips.

The people judging her are no longer strangers with an hour; they are colleagues with years. They do not see an edited sample; they see her on deadline days and quiet days, in meetings and in messages, when things go well and when she breaks the build. And they are not making one decision. They are making thousands of small ones: whether to ask her opinion, whether to trust her estimate, whether to cover for her, whether to mention her name when someone asks who is good.

Game theorists have a name for this kind of situation: a **repeated game**. Using a model of players who may meet again, and the results of a famous computer tournament, Robert Axelrod and William Hamilton showed that cooperation based on reciprocity (roughly: cooperate with those who cooperate with you) can get started even in an unfriendly population, thrive against a wide range of other strategies, and resist being invaded once it is established [@axelrod1981]. The shortcuts that win a single encounter tend to lose a repeated one, because the other players remember.

That is the long game in one line: **at work, people remember.** Your reputation is not something you broadcast; it is the running total of how you have treated people, as recorded in their memories.

::: coming {ref=ch10}
[[ch10]] builds Part II on this foundation: what the research says trust is made of, why reciprocity runs so much of working life, and how to behave well by default rather than by script.
:::

### Why acting doesn't scale {#ch01.sec.acting}

Here is where Rex's strategy breaks. A trailer can be a performance, because it lasts an hour. A film cannot, because it lasts years, and keeping up a performance for years is expensive.

The research on **emotional labour** measures this cost. *Surface acting* means displaying feelings you do not have, such as the bright smile over gritted teeth; *deep acting* means actually trying to feel what the situation calls for. A meta-analysis of 95 studies found that surface acting, and the gap between felt and required emotion, go with substantially worse well-being and job attitudes, and with slightly worse performance, while deep acting showed only weak links to impaired well-being [@hulsheger2011]. On the other side of the ledger, a meta-analysis of 75 studies found that people who feel more authentic report higher well-being (r = .40) and more engagement at work (r = .37) [@sutton2020].

Both of those are correlations, so they do not prove that faking it *causes* burnout; people who are already struggling may also act more. And most of the authenticity studies use Western, individualist ideas and measures of authenticity, as the meta-analysis itself points out [@sutton2020]. But both findings point the same way as common sense: pretending to be someone else, all day, is tiring.

::: chairs {left="The Trailer" right="The Film"}
@left: Let's be honest, I'm the reason anyone shows up. Two minutes, best shots, big music.

@right: And then I have to live up to you. Do you know how many people walk in expecting explosions?

@left: Nobody buys a ticket for "replies to messages promptly and owns her mistakes".

@right: Nobody stays for the explosions either. They stay for the story.

@left: So what, I should be boring?

@right: You should be *true*. Show my best scenes, the real ones. Cut what's dull. Never add what isn't there.

@left: And if the film is a bit thin?

@right: Then that's my job, not yours. Go and wait in the editing room while I shoot some better scenes.
:::

The Film's position has a more familiar name, one you have probably seen on a poster.

::: craft {by=author} Why "be yourself" is practical advice
"Be yourself" sounds like a poster in a dentist's waiting room. We think it is the most practical advice in this book, for three plain reasons. Acting is expensive to keep up. The people around you will see the film anyway. And whatever version of you gets hired is the version you will have to keep being for years.

Two limits, though. "Yourself" does not mean "unfiltered": you can be entirely genuine and still choose your words, your moment and your volume, and [[ch14]] is about exactly that dial. And being yourself is easier for some people than others. Who can afford to bring their whole self to work depends on power and on prejudice, and Part II deals with that honestly rather than pretending it away.
:::

## The career game {#ch01.sec.career-game}

Being good at your job and being seen to be good at it sound like the same thing. The evidence says otherwise, and the gap between them is where the third game lives.

Start with the review itself. In a study of more than 4,000 managers, each rated by bosses, peers, direct reports and themselves, the raters' own idiosyncratic tendencies accounted for over half of the variation in the ratings (62% and 53% in two data sets), while the managers' actual performance accounted for about a fifth to a quarter [@scullen2000]. Those were development ratings rather than pay-setting reviews, and researchers still argue about how much of a rater's "idiosyncrasy" is noise and how much is a genuinely different view. But the direction is hard to miss: a rating tells you a lot about the person giving it.

Promotion has its own trap. A study of sales workers across 131 firms found that companies promoted their best salespeople to manager even when other qualities predicted managerial success better, and that this was costly: the pattern the "Peter Principle" predicts [@benson2019]. Being excellent at the job you have is not the same as being right for the next one.

So the career game borrows from both of the others. It needs a film worth reviewing, which is the long game. And it needs the people who judge your work to see it clearly, inside your own company: that is the snapshot game's skill of honest translation, played for a different audience. Part III puts the two together, and adds the questions neither answers: what to get good at, whether to manage, and how to think about a career that lasts decades.

::: coming {ref=ch19}
[[ch19]] opens up a real promotion decision, and shows why the signals that win interviews in Part I and the trust you build in Part II turn out to be the currency promotions run on.
:::

## You will play all three games many times {#ch01.sec.many-times}

If the snapshot game happened once, you could grit your teeth, get through it, and forget about it. It doesn't.

In the United States, people born between 1957 and 1964 held an average of 12.9 jobs between the ages of 18 and 58, including 4.5 jobs between 25 and 34 alone [@bls-nlsy2025]. In January 2026 the median worker had been with their current employer for 4.1 years, and workers aged 25 to 34 for just 3.0 years [@bls-tenure2026]. Each of those changes means a fresh round of the snapshot game. Each of the stretches in between is a round of the long game, with the career game's reviews and promotion rounds coming round every year or so.

So this is not one exam followed by a career. It is three interleaved games, played for forty years. That is the best argument for learning all of them properly: they keep coming back.

::: field {regions="US, UK, India"} How often, and how fast, you can move
The tenure and job-count figures above are American, from the Bureau of Labor Statistics. We did not find comparable figures for India or the UK that we could verify, so we have not guessed.

The *speed* of a switch also varies. Most US employment is "at will": by default, either side can end it at any time, for almost any reason, with exceptions that vary by state [@lii-atwill]. In the UK, you must give at least a week's notice once you have been in a job for a month, and your contract may require more [@govuk-notice]. In India, notice is set by contract, typically one to two months for non-managerial staff and three to six months for senior roles [@khaitan-notice]. A three-month notice period changes how you run a job search. [[ch09]] has the details.
:::

## The loop {#ch01.sec.loop}

So far the three games sound like separate rooms. They are not. They are connected by a loop, and the loop is the most important idea in this chapter.

::: scene {slug="INT. A CAFÉ NEAR CORVID — SATURDAY, 10 AM"}
Meera, Dev's first team lead, now runs engineering somewhere else. She has brought her own mug to the café, because she always does. Today it says THE MAP IS NOT THE TERRITORY.

@meera: When I hire, I have forty-five minutes and a stranger. I'm not choosing the best engineer. I'm choosing the best engineer I can *see*.

@dev: So I need to be easier to see.

@meera: That's half of it. Do you know how I found my last three hires? For two of them, someone I'd worked with said, "You need to meet this person." I trusted the person saying it, because I'd watched them for years.

@dev: So the long game at your last job is the snapshot at your next one.

@meera: And in between, there's a third game: getting good at something that matters, and making sure it counts when the reviews come round. Most people only notice that one when they lose it.

@dev: You're going to tell me there's a spreadsheet for that too.

@meera: There's a spreadsheet for everything, Dev. Drink your coffee; it's getting cold.
:::

Meera's story is an anecdote, but it points at something the data shows. In one US company that tracked where its hires came from, candidates referred by current employees were 6.1% of applicants but 21.4% of interviewees, 27.3% of offers and 29.1% of hires [@brown2016]. A referral is a signal sent by someone else, about you, from inside the long game, which is why it is so hard to fake and so heavily weighted.

It is not only close friends who matter. A randomised experiment on LinkedIn, run across more than 20 million people over five years, found that weak ties raised job mobility, but only up to a point: moderately weak ties (people you share a few connections with) helped most, and weak ties mattered more in digital industries, strong ties in less digital ones [@rajkumar2022]. Your next job may well come through someone you worked with once and liked.

::: figure {#ch01.fig.loop src="ch01/loop.svg"}
Alt: A circle split into three arcs around a portrait of Dev labelled "one you, in all three games". The top arc, in coral, is Part I, the snapshot game, running through "apply", "interview" and "offer" to a star marked "you're hired". The right-hand arc, in teal, is Part II, the long game, running down through "do the work" and "earn trust". The left-hand arc, in purple, is Part III, the career game, running back up through "get good" and "get reviewed" to a point labelled "reputation, skills, stories, people: your next trailer", where the snapshot game begins again.

The loop. The snapshot game gets you in; the long game builds trust; the career game turns good work into skills, reviews and promotions. Together they produce everything your next snapshot will be made of.
:::

Follow the loop round and the games stop looking like opposites. The long game and the career game are where your next trailer gets shot. The skills you build, the problems you solve and the people who watched you solve them become the evidence, the stories and the referrals of your next job search. The snapshot game, in turn, decides which film you get to make next. And the second time round, you play it from strength.

This is why the book is one book and not three. Each part will make you better at one game, but the real return comes from playing them as one loop.

## Where are you now? {#ch01.sec.quadrant}

Put the two skills on two axes and the cast sorts itself out.

::: figure {#ch01.fig.quadrant src="ch01/quadrant.svg"}
Alt: A two-by-two grid. The horizontal axis is "good at doing the job (the film)" and the vertical axis is "good at getting hired (the trailer)". Top left, "All trailer": Rex, "great in interviews, hard to work with". Bottom right, "All film": Bea, "brilliant at the work, invisible on paper". Bottom left, "Not yet": "where everyone starts, at something". Top right, shaded gold with a star, "One you": "a true trailer of a good film". Dev sits near the bottom middle, labelled "Dev, today", with a dashed arrow pointing up into the gold quadrant.

Two skills, four places to be. Rex has the trailer without the film; Bea has the film without the trailer. Dev is somewhere in between, and the arrow is this book.
:::

Bea's problem and Rex's problem look like opposites, but they have the same shape: one game is strong and the other is weak. Bea does not need to become a better engineer to get hired; she needs a trailer that is as good as her film. Rex does not need a better trailer; he needs a film that lives up to it, or he will keep having to make new trailers. Most people are somewhere in the middle, strong in places and invisible in others, which is where Dev is.

:::: move {#ch01.move.scorecards} Your two scorecards
Score yourself from 1 (not at all) to 5 (completely) on each statement. Be honest; nobody is checking.

**The snapshot game**

1. I can describe my best piece of work in two minutes, including what changed because of it.
2. My résumé or profile shows results, not just duties.
3. I know at least five people who work somewhere I might like to work.
4. I can talk about my work in an interview without my nerves taking over.
5. I know roughly what people in my role are paid in my market.

**The long game**

6. People come to me for help, and not only with my own work.
7. When I say I will do something by a certain day, I do it, or I warn people early.
8. I can disagree with someone without it becoming personal.
9. I could name three colleagues who would recommend me without being asked twice.
10. I behave much the same way whether or not my manager is in the room.

**The career game**

11. I know how my work is judged, by whom, and when.
12. I keep a record of what I have done and what changed because of it.
13. I can name the skill I am deliberately getting better at this year.
14. I know what the next level of my role asks for, and whether I want it.

::: answer
Add up each section: questions 1 to 5 give your **trailer** score, 6 to 10 your **film** score, and 11 to 14 your **career** score (out of 20).

- **Film well ahead of trailer?** You are on Bea's side of the grid. The good news is that this is the easier gap to close: you already have the material, and Part I is about cutting it into a trailer. Start with [[ch04]].
- **Trailer well ahead of film?** You are on Rex's side. You will probably keep getting offers, but every new job hands you a new audience who will see the film. Read Part II before your next interview, starting with [[ch10]].
- **Trailer and film both low?** Welcome to "not yet". Everyone starts here, at something. Read the book in order.
- **Career score lowest?** That is common, and often the cheapest gap to close: items 11 and 12 are habits you can start this week. Part III begins at [[ch18]].
- **Everything high?** Then read for the evidence. There are plenty of popular claims in all three games that the research does not support, and knowing which is which is its own advantage.

Keep your scores. You will meet them again in [[epi]].
:::
::::

## One you {#ch01.sec.one-you}

Here, then, is the argument of the book: three games, three rules, and one thread that ties them together. Everything after this chapter is the detail.

1. **Learn the snapshot game without shame.** It has rules that have little to do with how good you are at your job, and knowing them is not cheating. Making real value easy to see is translation, not spin. That is Part I.
2. **Play the long game without a mask.** At work you are watched for years, by people who remember. Good defaults beat good performances, because defaults are cheap to keep up and performances are not. That is Part II.
3. **Make the work count, honestly.** Get good at things that matter, and make sure the people who judge your work can see it as it is. That is Part III.

**The thread: one you.** Keep the games honest with each other. Never let a trailer, or a promotion case, promise what the film cannot deliver, and never let a good film go without a trailer. The trailer should be a true cut of the film.

That thread is what Dev was missing in the opening scene. She was not wrong that the game felt rigged. But she had assumed that the only way to win it was to become Rex, and since she did not want to become Rex, she had stopped trying to play. There is another way to win: play the game well *as yourself*.

::: figure {#ch01.fig.map src="ch01/map.svg" size=small}
Alt: A map of the book drawn as a transit line running from top to bottom. It starts at stop 1, "Start: three games". The coral Part I section, the snapshot game, has stops 2 to 9: Stay or go?, The other side, Your evidence, Paper you, People not portals, Interviews, Show your work, and Offer and exit, then a star, "you're hired". The teal Part II section, the long game, has stops 10 to 17: Trust, First 90 days, Reliability, Talk and write, The dial, Friends at work, Conflict, and Under pressure. The purple Part III section, the career game, has stops 18 to 22: The review, The promotion case, What to get good at, Expert or manager?, and The whole career. The line ends at "Epilogue: the loop", and a dashed arrow labelled "the next move, made from strength" curves from there back up to the start.

The map of the book. Each part is one game; the dashed arrow is the loop that takes you round again, better equipped.
:::

The edges of that map are where it gets interesting, because real moments do not always belong to one game.

:::: move {#ch01.move.which-game} Which game is it?
For each moment, decide whether it is mainly **snapshot** (strangers, a short sample, one decision), mainly **long game** (people who know you, repeated over time), or a mixture.

1. A recruiter's first phone call.
2. Your third month on a new team.
3. A teammate asking you for help at 4:55 pm on a Friday.
4. A take-home coding exercise.
5. A hiring manager phoning someone you used to work with, to ask about you.
6. Your first week in a new job.
7. Your annual performance review.
8. Being asked whether you want to manage people.

::: answer
1. **Snapshot.** A stranger, twenty minutes, one decision: do you go through to the next round?
2. **Long game.** The novelty has worn off, and people are now judging the film.
3. **Long game**, and a classic one. Nobody will remember the Friday you said yes; plenty will remember a pattern of noes.
4. **Snapshot**, though a better one than most, because it shows real work ([[ch08]]).
5. **Both, and this is the loop in action.** A snapshot decision is being made, using evidence from your long game.
6. **Both.** You are being judged quickly by people who will later know you well, which is why first impressions matter and also why they can be overwritten ([[ch11]]).
7. **The career game**, and the clearest example of it: a year of film, summarised by someone else, often written and read like a trailer. [[ch18]] looks at how to make sure it reflects the film.
8. **The career game**, and one of its biggest decisions. Being good at your current job does not settle it ([[ch21]]).

The most interesting moments in a career sit at the edges, where one game feeds the other.
:::
::::

::: scene {slug="INT. DEV'S FLAT — SUNDAY, LATE"}
Dev opens the spreadsheet. It has one tab, called *Applications*, with 47 rows and 46 noes. She renames the tab *Game 1*. Then she adds two more, *Game 2* and *Game 3*, and sits looking at the empty grids for a while.

Then she texts Bea.

@dev: I'm going to learn the game. Not become Rex. Learn it.

@bea: Good. Teach me after.

@dev: Deal. Step one: work out whether I should even leave.

She adds a third tab, *Should I stay?*, and closes the laptop before she can add a fourth.
:::

That question, whether to switch at all, is where the snapshot game really starts, and it is the subject of [[ch02]].

::: rewind
- Working life is **three different games**: a *snapshot game* in which strangers judge an edited trailer of you, a *long game* in which colleagues watch the whole film, and a *career game* in which the film gets reviewed and decides what you do next.
- Hiring is **prediction under uncertainty**. The best single method, the structured interview, correlates about .42 with later performance, plus or minus .24, and ratings also respond to self-promotion and nerves.
- In the snapshot game, **strong signals are specific, checkable and costly to fake**. Make real value legible: translate, never fabricate.
- At work you are in a **repeated game**: people remember, reciprocity wins over time, and keeping up an act is costly.
- In the career game, **ratings say a lot about the rater**, and the best performer is not always the best person to promote.
- You will play all three games **many times**: US workers aged 25 to 34 have a median of three years with their current employer.
- The games form a **loop**: the long game and the career game produce the skills, stories, reputation and referrals of your next snapshot.
- The book's thread: **one you**. Learn the snapshot game without shame, play the long game without a mask, make the work count honestly, and keep the trailer a true cut of the film.
:::
