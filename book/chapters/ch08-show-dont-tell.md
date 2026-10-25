---
id: ch08
status: final
---

::: scene {slug="INT. DEV'S FLAT — SATURDAY, 9:10 AM"}
The email from Lanternfish's recruiter is short and friendly.

> *Thanks again for Thursday! As a next step, we'd love to see how you approach a small problem. Attached is a take-home task: a service that takes in delivery events and flags lorries that are running late. It should take about three hours. Please send it back within a week, and shout if anything is unclear.*

Dev reads the task twice. Then she does the maths every conscientious candidate does. *About three hours* means three hours for the people who wrote it, who know the domain. She will want tests. And a nice README. And proper error handling. And maybe a little dashboard, to show she can do front-end too. If she starts now and works through Sunday...

She opens her spreadsheet and, before she can talk herself out of it, makes a new tab. She calls it *Take-homes (boundaries!)*, with the exclamation mark, because she knows herself.

The first row says: **Time cap: 4 hours. Not 14.**
:::

Dev is about to be judged on her work rather than on her description of it. That is good news, because work is harder to fake than talk. It is also a trap, because a task you can always improve has no natural end, and because some ways of watching people work measure something other than the work.

This chapter is about work samples: coding interviews, take-home tasks, case studies and presentations. Why employers use them, what they can and cannot see, how to prepare without memorising, and where to draw the line on unpaid labour.

::: pause
Before you read on: a take-home task says "should take about three hours". How long should you spend on it? And what, if anything, should you send along with the code? Commit to an answer; the chapter comes back to it.
:::

## Why employers ask you to show {#ch08.sec.why}

In [[ch01.sec.signals]] you met the idea of a costly signal: something hard to fake for people who lack the quality it advertises. A sample of your actual work is about as costly as a signal gets. Anyone can say "I write clean, well-tested code"; far fewer can produce it on demand.

The research agrees that work samples carry real information. In the classic 1998 summary of selection methods, work sample tests had the highest validity of all, at .54 [@schmidt1998]. The 2022 re-analysis, which argued that the old statistical corrections were too generous, brought that down to .33: still useful, but below structured interviews (.42) and job-knowledge tests (.40) [@sackett2022]. The same authors found that the methods built around the specific job, such as structured interviews, job-knowledge tests and work samples, generally beat broad measures [@sackett2023-iop].

Two things follow. First, a well-designed work sample is a fair way to be judged: it looks at the thing you will actually do. Second, it is still a sample. A three-hour exercise or a forty-minute coding round sees one slice of your film, under unusual conditions, and those conditions matter more than most candidates realise.

It also helps to know what a work sample cannot see, because those are the things you will have to show in other ways. It cannot see how you work with other people over months, how you take feedback on the third round of review, whether you warn people early when you are going to miss a date, or what you do when the problem is boring rather than clever. Those are the long game's skills, and Part II is about them. In the snapshot game, the only ways to show them are your stories ([[ch07]]) and the people who have watched you work ([[ch06]]). A work sample shows that you can do the task. It never shows that you will do it reliably for three years [!view].

## Being watched {#ch08.sec.watched}

::: receipts {source=behroozi2020} Does being watched change how well you code?
**What they did.** Researchers at North Carolina State University randomly assigned 48 computer-science students to solve a programming problem at a whiteboard in one of two settings: the traditional technical-interview format, with an interviewer present and watching, or a private setting with nobody in the room [@behroozi2020].

**What they found.** Performance was reduced by more than half simply by being watched by an interviewer. Measures of stress and cognitive load were significantly higher in the traditional format [@behroozi2020].

**What it cannot tell you.** It was a small study of students, at one university, on one task. It does not tell you how much the effect varies between people, or whether practice shrinks it. But it is a randomised experiment, so the difference between the two groups is hard to explain away.
:::

Think about what that result means. A traditional whiteboard interview is supposed to measure how well you solve problems. This experiment suggests it also, and perhaps mostly, measures how well you solve problems *while being stared at*, which is a skill most jobs use for about four minutes a year.

::: figure {#ch08.fig.watched src="ch08/watched.svg"}
Alt: Two panels side by side. On the left, labelled "alone", Bea stands at a whiteboard covered in code. On the right, labelled "watched", the same whiteboard and the same Bea, now with sweat drops, and a seated figure with a clipboard and a fixed stare behind her. Below, under the heading "how much they solved", a long teal bar is labelled "alone" and a coral bar less than half as long is labelled "watched: less than half". A note at the bottom reads "schematic: in one trial with 48 students, performance fell by more than half when an interviewer watched".

Watched versus alone. Same people, same kind of problem, randomly assigned; the only difference was the audience. The bars are schematic, not exact values.
:::

It is not the only reason to treat a single technical interview with caution. One interview-practice platform, analysing people who interviewed repeatedly with different interviewers, reported that only about 20% of candidates scored consistently from one interview to the next, while the rest varied widely [@interviewingio2016!]. That is commercial data from a self-selected group, published by a company that sells interview practice, so it is weak evidence. But it fits with the experiment, and with what developers themselves report: in an analysis of discussions about technical interviews on one online forum, recurring complaints included a lack of real-world relevance, anxiety, heavy demands on time, and arbitrary, unwritten norms [@behroozi2019!].

::: myth {#ch08.myth.objective verdict=partly grade=moderate} "Technical interviews objectively measure coding skill"
Overstated. Work samples do predict job performance (a revised validity of .33 [@sackett2022]), so a technical exercise is not noise. But in a randomised trial, simply being watched cut students' whiteboard performance by more than half [@behroozi2020], and one platform reports that only about one candidate in five scores consistently across repeated interviews [@interviewingio2016]. A single technical round measures coding skill *plus* how you handle being observed, *plus* luck. The grade is moderate because the trial was small and the platform data commercial.
:::

So what do you do with that? Two things, one for your head and one for your preparation.

For your head: **one technical round is one noisy sample.** A bad one is not proof you cannot code, any more than a good one would prove you can. If you have done the job, and the evidence in your story bank says you have, a stumble at a whiteboard says more about the whiteboard than about you.

For your preparation: if being watched is the bottleneck, **practise being watched** [!view]. Solving problems alone in your room builds the skill, but not the skill under the conditions you will meet. Do mock interviews with a friend, a colleague or a practice service. Narrate while someone listens. The aim is not to stop feeling the eyes on you, but to have done this so many times with eyes on you that the eyes stop mattering as much.

## Preparing without memorising {#ch08.sec.prepare}

There is a cottage industry of technical interview preparation, and much of it amounts to memorising answers to hundreds of problems. Some memorising helps: you should know your basic data structures cold. But a memorised answer is brittle. The moment the interviewer changes one constraint, you are back to thinking, and thinking is what they wanted to see all along.

Study research points to a better way. In a major review of learning techniques, practice testing (retrieving something from memory, rather than reading it again) and spreading practice out over time earned the top rating for usefulness, while rereading and highlighting earned the bottom one [@dunlosky2013]. That research was on students, not candidates, but the translation is straightforward [!view]:

- **Solve, don't read.** Reading a worked solution feels like learning. Closing it and solving the problem from scratch the next day is learning.
- **Spread it out.** Forty minutes a day for three weeks beats a twelve-hour Sunday.
- **Learn patterns, not problems.** After each problem, write one line: "This was really a ___ problem." Over time you build a small set of shapes (two pointers, a queue, a hash map of counts) that cover many questions.
- **Practise the whole performance.** Talking, writing on a board or a shared editor, testing out loud, being interrupted. That last part is the subject of the next section.

Practice matters, but less than its fans claim: [[ch20]] looks at what the research on deliberate practice does and does not explain about getting good at work, including the famous 10,000 hours.

## Thinking out loud {#ch08.sec.out-loud}

Bea gets a chance to test all this sooner than she would like.

::: scene {slug="INT. BEA'S FLAT, ON A VIDEO CALL — TUESDAY, 2:00 PM"}
Bea has made it to the next round with the payments company: a live coding session in a shared editor. Ten minutes in, it is going the way her live coding usually goes. She has understood the problem, seen a good approach, and gone completely silent while she types it. The interviewer has unmuted twice to ask "How's it going?" and twice been told "Fine."

Then Bea remembers something Dev said on Sunday: *They can't score what they can't hear.*

@bea: Sorry, I've been quiet. Let me say what I'm doing. I'm keeping a map from account ID to the last transaction, because I only need the most recent one, so a list would be wasted. The tricky case is two transactions with the same timestamp, and I haven't handled that yet. Can I check whether that can happen?

The interviewer, who had been about to write *poor communication*, writes something else.
:::

Bea's silence was not a lack of thinking. It was thinking the interviewer could not see. In a live exercise, the interviewer is scoring your *process* as much as your answer: how you understand the problem, how you choose an approach, how you handle the bit that goes wrong. If you think silently, they score the only thing they can see, which is a person typing and occasionally sighing.

::: figure {#ch08.fig.out-loud src="ch08/out-loud.svg"}
Alt: Headed "Bea, thinking out loud", with her avatar, five numbered speech bubbles run down the page, each tagged with what it does. 1, "restate the problem": "So: for each account, return the most recent transaction?" 2, "try a tiny example": "Let me try three transactions for two accounts by hand first." 3, "say the simple version first": "Simplest version: sort everything by time, keep the last one per account." 4, "name the trade-off": "Sorting is n log n; one pass with a map is linear, so I'll do that." 5, "test out loud": "Edge case: two transactions with the same timestamp. Can that happen?" A note at the bottom reads "each bubble gives the interviewer something to score, and a chance to help".

Thinking out loud, annotated. Each bubble does a job the interviewer can see and score. None of them requires being clever; all of them require saying the thinking you are already doing.
:::

The five moves in the figure are craft rather than science [!craft], but each has a plain reason behind it. Restating the problem catches misunderstandings while they are cheap. A tiny example turns a vague task into a concrete one. Saying the simple version first gets a working answer on the board, which you can then improve, instead of a perfect answer you never finish. Naming the trade-off shows judgement, which is what separates a senior engineer from a fast typist. And testing out loud shows that you know code is not finished when it compiles.

Thinking out loud has a cost, and the evidence suggests what it is. Narrating while being watched is part of what makes the traditional format stressful in the first place [!view]. That is why it needs practice: the first few times, talking and thinking at once feels like patting your head and rubbing your stomach. By the tenth, it feels like explaining your work to a colleague, which is what it is.

::: craft
When you get stuck in a live exercise [!craft]. Say so, specifically: "I'm stuck on how to handle the duplicate timestamps." Then say what you would try. Interviewers often have a hint ready, and many score how you use a hint, not whether you needed one. Silence, by contrast, gives them nothing to work with. If your mind goes blank, go back to the tiny example: running something concrete through by hand almost always restarts the thinking.
:::

None of this sticks from reading about it. It sticks from doing it out loud, several times, which is what the next exercise is for.

:::: move {#ch08.move.talk-aloud} Talk-aloud practice
Pick a small problem from your field: a coding exercise, a short case question ("How many coffee machines does an office of 200 need?"), or a design question. Set a timer for 15 minutes and solve it **out loud**, using the five moves in [[ch08.fig.out-loud]]. Record yourself, or ask a friend to listen without helping.

Then listen back and count: how many of the five moves did you make? How long were your longest silences?

::: answer
Almost everyone has two or three silences of more than a minute on the first try, usually right after reading the problem and right before writing the main logic. Those are exactly the moments the interviewer most wants to hear. The fix is not to fill the silence with chatter but to narrate the decision you are making: "I'm choosing between a list and a map here; a map, because I need lookups."

Most people also skip the tiny example and the testing out loud, because they feel slow. They are the opposite: the example prevents you solving the wrong problem, and testing out loud catches bugs while the interviewer is still watching you be careful. Do the exercise three times over a week, on different problems, and the silences shrink.
:::
::::

## Pairing and system design {#ch08.sec.formats}

Two other formats are common in software hiring, and the same principles carry over.

In a **pairing** interview, you work on a problem with an interviewer as if you were colleagues: they may drive while you navigate, or the other way round. It is the format closest to real work, and it rewards exactly the habits in [[ch08.fig.out-loud]], plus one more: treating the interviewer as a collaborator. Ask what they would do. Accept a suggestion gracefully, or disagree with a reason. They are scoring whether they would like to pair with you on a Tuesday afternoon, and that is a fair question [!craft].

In a **system-design** round, usually for more experienced roles, you sketch how you would build something larger, such as a delivery-tracking service for 4,000 lorries, on a whiteboard or a shared canvas. There is no single right answer, which unnerves people who like right answers. The moves are the same five, scaled up [!craft]: clarify the requirements and the numbers (how many lorries, how many events a second, how fresh must the data be?), sketch the simplest design that works, then find where it breaks and name the trade-offs of each fix. Interviewers are mostly listening for judgement: what you chose not to build, and why.

Honesty about the evidence: we found no rigorous research on how well software take-homes or system-design rounds predict job performance. They resemble work samples, which do predict reasonably well [@sackett2022], and that is the best that can be said. Treat claims that any one format "really" reveals talent with the same scepticism as [[ch08.myth.objective]] suggests.

## The take-home task {#ch08.sec.take-home}

Back to Dev's Saturday and the Pause. How long should you spend on a take-home that says "about three hours"?

The answer we would give is: **about what they said, and tell them how long you spent** [!view]. The stated time is the employer telling you how much work they expect, and therefore how much work they are comparing. Spending fourteen hours does not make you look three times as good; it makes the comparison unfair to everyone who respected the brief, and it teaches the employer that their "three hours" is really fourteen. It also sets a pattern you will regret in Part II: the person who always over-delivers in secret becomes the person everyone quietly expects to work weekends.

::: trapdoor
**Gold-plating the take-home.** Spending a whole weekend to "stand out" feels like commitment. It usually buys a marginally better submission, a reviewer who cannot tell whether you would need a weekend for every task, and a tired Monday. Worse, it trains you to pay for opportunities with unpaid time, a habit that Part II will ask you to break. Respect the stated time, say how long you took, and let the README show what you would have done next.
:::

No study has compared take-home strategies, so most of what follows is craft [!craft]. It is built on the same idea as the rest of this chapter: make your thinking visible, and make it easy for a reviewer to score.

::: figure {#ch08.fig.scoping src="ch08/scoping.svg"}
Alt: A take-home task drawn as three numbered stages down the page, joined by arrows, with a clock beside them shaded for a "3-hour cap". 1, "before": read the brief twice; ask two questions; agree the time cap. 2, "during": start a timer; build the core first; test the core; stop at the cap. 3, "after", shaded coral: write the README: what I built; decisions and trade-offs; what I'd do with more time; how long I spent. A coral note with an arrow pointing to the third stage says "the README is part of the work sample". A note at the bottom reads "craft, not research: a way to scope, not a rule".

Scoping a take-home. The questions before and the README after take twenty minutes between them, and they are often what a reviewer remembers.
:::

**Before you start**, read the brief twice and write down what is unclear. Then ask. Most companies say "shout if anything is unclear", and they mean it: a good clarifying question is evidence of exactly the judgement they hope to hire. Dev's two questions were:

> *Is it fine to keep the data in memory rather than set up a database, given the time limit? And should I optimise for correctness or throughput if I have to choose?*

The recruiter forwarded them to Tomás, who replied within the hour: in memory is fine; correctness first. Two questions, and Dev now knows what "good" means to the person who will mark it.

:::: move {#ch08.move.questions} What would you ask before starting?
Here is a take-home brief. Before reading the answer, write the two or three questions you would send back before writing any code.

> *Build a simple API for a library: members can borrow and return books. Use any language. Should take 2–3 hours. Please include tests.*

::: answer
Strong questions resolve ambiguity that would change what you build, or what "good" means:

- "Should I persist data in a database, or is in-memory storage fine for this exercise?" (Changes the scope enormously.)
- "Are there rules I should enforce, such as a maximum number of loans per member or due dates?" (Changes the logic.)
- "What matters most to you here: API design, test coverage, or handling edge cases?" (Tells you what they will score.)

Weak questions are ones you could answer yourself ("What language should I use?" when the brief says any) or that signal anxiety rather than judgement ("Is it OK if it's not perfect?"). Two or three questions are plenty; twelve suggests you will need a lot of hand-holding. And if nobody answers within a day, make a sensible assumption and write it down in the README. That is a judgement call too, and a visible one.
:::
::::

**While you work**, start a timer. Build the core of the task first, so that whatever happens, you hand in something that works. Then test the core. Polish, extras and the little dashboard come last, if at all.

**When the timer goes off, stop**, and write the README. This is the part most candidates skip and most reviewers read first. Say what you built, what you decided and why, what you left out on purpose, what you would do next with more time, and how long you spent. A section called "What I'd do with another day" turns every gap in your code from a weakness into evidence of judgement: you knew it was there, and you chose.

:::: move {#ch08.move.time-box} Time-box a take-home
Take the library brief above, or a real one. Before you start, write a plan that fits inside the stated time, in blocks of 15 minutes: what you will build first, when you will write tests, and when you will stop to write the README. Then, if you can, do it, with a real timer, and compare your plan with what happened.

::: answer
A reasonable plan for a three-hour version: 15 minutes reading and sending questions; 90 minutes on the core (borrow, return, list); 30 minutes on tests for the core; 20 minutes on the README; 25 minutes of slack for the thing that goes wrong. Most people's first plan has no slack and no README time, and most people's actual run overshoots the core by half. That is normal; it is also the most useful thing the exercise teaches.

If you overshoot, say so in the README: "I spent 3 hours 40 minutes; the extra went on input validation." Honesty about the time is a signal in its own right, and it is one that the person who spent fourteen hours and claimed three cannot send. You will need exactly this skill, estimating and telling people early when you slip, in [[ch12.sec.estimates|Chapter 12]].
:::
::::

## When a test becomes free consulting {#ch08.sec.free-work}

Most take-homes are honest: a small, artificial problem designed to show how you work. A few are not. Learning to tell them apart protects your time, and occasionally your work.

::: craft {by=author} Where we draw the line on unpaid work
We think a take-home crosses from assessment into free labour when several of these are true: it is a real problem from the company's own backlog rather than an artificial one; it is open-ended, with no stated time; it would take more than an evening; it asks for production-ready polish; or the terms suggest the company will use or own what you produce. No study measures how common this is, so this is our view, not a finding.

When you see the signs, you have options short of walking away. Ask how long they expect it to take and how it will be assessed. Offer a smaller version, or to walk through how you would approach it in a call. Ask whether they pay for longer exercises (some companies do). And if the answer to every question is "just do it", you have learned something about how the company treats people's time, before you work there rather than after.
:::

## Cases and presentations {#ch08.sec.cases}

Not every work sample involves code. Consulting, product, design, analytics and many business roles use case interviews ("A client's sales have fallen 20%; what would you look at?") or presentations ("Prepare 15 minutes on how you would launch this product"). The research on work samples applies in spirit: these are attempts to see you do a version of the job [@sackett2023-iop]. But we found no rigorous evidence on how to do well in them specifically, so what follows is craft [!craft].

For a **case**, the moves are the same as for a coding problem, in a different costume. Restate the question and agree what a good answer looks like. Ask for the facts you need instead of assuming them. Lay out a simple structure for attacking the problem before diving in. Do the arithmetic out loud. End with a recommendation, even a provisional one, and say what would change your mind.

For a **presentation**, answer the question you were asked, not the one you wish you had been asked. Put the conclusion first: busy people decide in the first minute whether to follow the rest. One idea per slide. Leave a third of the time for questions, because the questions are the part of the presentation that shows how you think when you have not rehearsed. And, as with take-homes, respect the time: a fifteen-minute slot is not an invitation to bring forty slides.

::: ask
Q: Can I use AI coding assistants on a take-home?

A: Ask. Policies differ between companies and change quickly, and the brief may already say. If it is allowed, say in the README how you used it, and make sure you can explain every line, because the follow-up conversation will ask. If it is not allowed, do not. Either way, the work sample exists to show *your* judgement [!craft].

Q: The take-home is due in a week, but I'm working full-time. Can I ask for more time?

A: Yes. Ask early, give a reason and a date: "I can get this to you by next Wednesday; would that work?" Asking for a reasonable extension is a normal professional request, and the way you ask is itself a small signal.

Q: What if I can't solve the live problem at all?

A: Show everything you can: understand the problem, try examples, write the simplest version you can, explain where you are stuck and what you would try next. Interviewers can score a good process that runs out of time. They cannot score silence.

Q: Do I get feedback on a take-home if I'm rejected?

A: Sometimes, if you ask politely and briefly. Many companies do not give it, often for legal or time reasons. If they do, it is gold; write it down.
:::

## Dev's walk-through {#ch08.sec.walkthrough}

The following Tuesday, Dev finds out what the README was for.

::: scene {slug="INT. DEV'S FLAT, ON A VIDEO CALL WITH LANTERNFISH — THE FOLLOWING TUESDAY, 4:00 PM"}
Dev sent her take-home on Wednesday, after three hours and fifty minutes, with a README whose last section was called *What I'd do with another day*. Now Tomás and one of the panel engineers are walking through it with her.

@tomas: You stored the events in memory. What happens when the service restarts?

@dev: Everything's lost. I wrote that down: it's the first item in "another day". For real use I'd put them in a queue with persistence, and the late-lorry check would read from there.

@tomas: And you flagged a lorry as late when its expected time passed. What if the events arrive out of order?

@dev: Then I'd flag it wrongly. I've got a test that shows the bug, marked as a known failure. I ran out of time to fix it properly, and I'd rather show you the bug than hide it.

The engineer laughs. Tomás doesn't, but he writes something down, and Dev has learned what that means.

@tomas: Last thing. Why did you stop at four hours?

@dev: Because you said three, and I didn't want to show you a version of me that needs a weekend for everything.

@tomas: You'll hear from us by Friday. Morning. I don't do Friday afternoons.
:::

Look at what the walk-through actually tested: not whether Dev's code was perfect, but whether she understood its weaknesses, could explain her decisions and was honest about what she had not done. The README turned three gaps into three pieces of evidence. The failing test she chose to show is the clearest signal of the lot: specific, checkable and costly to fake, exactly as [[ch01.sec.signals]] promised. A candidate who hides a bug has to hope nobody finds it. A candidate who shows one has nothing left to hide.

On Friday morning, Lanternfish calls. What happens next, an offer, a negotiation, a counter-offer from Corvid and a resignation, is [[ch09]].

::: rewind
- Work samples are **costly signals**: hard to fake, close to the real job. They predict job performance (a revised validity of .33), though less than the old .54 estimate suggested.
- In a randomised trial, **being watched cut whiteboard performance by more than half**. A single technical round measures your skill, how you handle observation, and luck.
- Treat one technical round as **one noisy sample**, and practise under observation, because that is the condition you will be tested in.
- Prepare by **solving, not reading**: retrieval and spaced practice beat rereading. Learn patterns, not problems.
- **Think out loud**: restate the problem, try a tiny example, say the simple version first, name the trade-off, test out loud. Interviewers cannot score what they cannot hear.
- For take-homes: **ask before you start, respect the stated time, and write a README** that shows your decisions, what you would do next and how long you spent.
- A take-home that is real work, open-ended and long is free consulting; ask about scope, offer a smaller version, or decline.
:::

::: further {ref=more.sec.interview-prep}
This chapter taught the skill behind work samples, not a bank of practice problems. The appendix points to vetted places for structured technical-interview practice.
:::
