---
id: ch20
status: review
---

::: scene {slug="INT. LANTERNFISH, A QUIET CORNER — WEDNESDAY, 5:30 PM"}
The learning-budget form has one question that matters: *What skill will you develop next year?* Dev has three browser tabs open, each a course, each with a countdown timer telling her the discount ends tonight.

The first is a cloud-infrastructure certification, because everyone on the platform squad seems to have it. The second is a machine-learning course, because Rex, leaning over the partition on his way to a meeting, has just told her that "everything else is dead in five years, trust me". The third she opened by accident.

She makes a new tab in the spreadsheet, *Skills*, and types the three course names into it. Then she stares at them, because none of them feels like an answer.

Her chat lights up. It is someone she barely knows, from the pricing squad.

> *Hi, sorry to bother you. We're designing the new pricing service and three different people told me you're the person who makes things testable. Could I grab 20 minutes?*

It is the third message like that this month. Dev looks at it for a while. Then she looks at her three tabs. Then she opens a fourth row in *Skills* and types, slowly, *the thing people already ask me for*.
:::

When Dev left Corvid, her testing background felt like something to apologise for: the tester who wanted to be a developer ([[ch04.sec.targets]]). Two and a half years later, it is the reason people from other squads seek her out. She did not plan that. Most people who end up very good at something did not plan it either, which raises the question this chapter tries to answer honestly: if you cannot predict the future, how do you choose what to get good at?

The popular answers are confident. Ten thousand hours. Follow the trend. Seventy per cent of learning happens on the job. Find a mentor. The evidence behind each of them is more interesting, and more useful, than the slogans. This chapter goes through it, and ends with a way of choosing that does not depend on knowing what the world will want in ten years.

::: pause
Before you read on, a guess. Researchers have measured how much of the difference in performance between people is explained by how much *deliberate practice* they have done. For people in professions (rather than music, sport or games), what share do you think it explains? Pick one: about 1%, about 10%, about 25% or about 50%.
:::

## Career capital {#ch20.sec.capital}

Start with what makes a skill worth the effort.

The most useful frame comes from practitioners rather than researchers. The careers organisation 80,000 Hours defines **career capital** as "anything that puts you in a better position to make a difference in the future": skills, connections, credentials, character and financial runway, with a warning against both neglecting it and endlessly collecting generic credentials [@todd2026!]. The phrase was popularised by Cal Newport's book *So Good They Can't Ignore You*, which argues that skill should come before passion [@newport2012!]. Both are frameworks, not findings, and we label them that way.

What does the evidence say about which skills hold their value? Two findings matter. First, a great deal of what people know at work is specific to their occupation or industry: in US data from 1968 to 1997, occupational mobility was high and rising, and the authors conclude that human capital is largely occupation-specific [@kambourov2008]. Skills travel well within a kind of work, and less well outside it. Second, in fast-changing fields, specific skills lose market value quickly. For graduates in applied science and engineering subjects such as computer science, the earnings premium is highest at entry and, in the working-paper version of the study, falls by more than half over the first decade, as the skills that jobs require change underneath them [@deming2020]. Returns to experience are, in the authors' framing, a race between learning on the job and skills going stale.

Put the frameworks and the evidence together and you get a working test for a skill worth building, which is our synthesis rather than anyone's measured result [!view]. Ask three questions:

- **Do many employers value it?** A skill only one company uses is a bet on that company.
- **Is it hard to acquire?** If anyone can pick it up in a month, it will not set you apart for long.
- **Does it go stale slowly?** Tools change fast; judgement about a kind of problem changes slowly. The deeper the skill sits beneath the tools, the longer it lasts.

::: figure {#ch20.fig.compound src="ch20/compound.svg"}
Alt: A two-by-two grid titled "Skills that compound". The horizontal axis runs from "few employers value it" to "many employers value it"; the vertical axis runs from "easy to pick up" to "hard to acquire". Bottom left: "a hobby". Bottom right: "a commodity: everyone has it soon". Top left: "a niche: a bet on one market". Top right, shaded gold with a star: "career capital: it compounds". In the top right sit two dots: "Dev: making systems testable" and "Bea: zero-downtime migrations". In the bottom right, a dot labelled "this year's hot tool" has a dashed arrow sliding left and down, labelled "goes stale". A note: "A thinking tool, not a measurement."

Skills that compound. The top-right corner holds skills that many employers need and few people have, and the deeper they sit beneath particular tools, the longer they stay there. This is our framework, not a measured map.
:::

Notice where Dev's skill sits. "Testing" alone is a crowded field, and "backend development" is a big one. **Making systems testable**, knowing how distributed systems fail and designing them so the failures can be caught before customers see them, sits where the two overlap, and that overlap is much rarer than either. Many of the most valuable skills look like this: not a single rare talent, but an unusual combination of two ordinary ones [!view]. Dev's QA years were not a detour. They were half of the combination.

## What practice explains {#ch20.sec.practice}

Once you have chosen a skill, the next question is how to get good at it, and the most famous answer is a number.

The number comes, indirectly, from a 1993 study of violin students, which argued that expert performance results largely from years of deliberate practice, meaning effortful activity designed specifically to improve, and which was later popularised as "ten thousand hours" [@ericsson1993]. The idea is attractive because it is democratic: anyone can practise.

Then researchers tested it across domains. A 2014 meta-analysis found that deliberate practice explained 26% of the differences in performance in games, 21% in music, 18% in sports, 4% in education, and **less than 1% in professions** [@macnamara2014]. If you picked "about 1%" for the pause, you were right, and in very good company if you did not.

::: figure {#ch20.fig.practice src="ch20/practice.svg"}
Alt: Five horizontal bars, each drawn as a full-length outline representing 100% of the differences in performance, with the part explained by deliberate practice filled in purple. Games: 26%. Music: 21%. Sports: 18%. Education: 4%. Professions: under 1%, a sliver too thin to see, with an arrow labelled "your job is here". The empty part of the first bar is labelled "everything else". A note: "Share of differences in performance explained by deliberate practice. Macnamara, Hambrick and Oswald (2014)."

What practice explains, to scale. In every domain studied, deliberate practice mattered, but it explained a minority of the differences between people, and in professions almost none of them.
:::

That result contradicts a very popular idea, so it is worth opening up.

::: receipts {source=macnamara2014} The meta-analysis behind the myth-busting
**What they did.** Macnamara, Hambrick and Oswald gathered the studies that had measured both deliberate practice and performance, in every major domain where the idea had been tested, and pooled them to estimate how much of the variation in performance practice could account for [@macnamara2014].

**What they found.** Practice explained 26% of the variance in games, 21% in music, 18% in sports, 4% in education and under 1% in professions. Their conclusion was measured: deliberate practice is important, but not as important as had been argued.

**What it cannot tell you.** The studies it pooled defined and measured practice in different ways, and Ericsson, the theory's originator, argued that many of them counted activities that did not meet his strict definition, and that studies using it found larger effects [@ericsson2019]. And "explains little of the difference *between* people" is not the same as "does little for any one person": practice can matter a great deal to your own improvement while other things (prior skill, the job, luck) explain more of why you differ from someone else.
:::

The debate since then is worth knowing, because it points somewhere useful. A later meta-analysis in sport found that practice explained 18% of the variance overall but only 1% among elite athletes, and that the athletes who reached the top had not started their sport earlier [@macnamara2016]. A careful replication of the original violin study found a real but much smaller effect of practice [@macnamara2019]. Ericsson's reply, restricting the analysis to studies that matched his original definition of deliberate practice (individualised training, designed by a teacher, aimed at specific weaknesses), found that it explained 29% of the variance, against 14% across the broader set of studies [@ericsson2019].

The two camps disagree about the size of the effect. They agree about something more useful: **the design of practice matters far more than the hours**. Hours of ordinary work, repeating what you can already do, are not deliberate practice in anyone's definition.

::: myth {#ch20.myth.ten-thousand verdict=partly grade=strong} Ten thousand hours of practice makes you an expert
Practice matters, which is why this is not simply busted. But across domains, deliberate practice explained a minority of the differences in performance, and less than 1% in professions [@macnamara2014]; among elite athletes, 1% [@macnamara2016]; and a replication of the original violin study found a much smaller effect than the original [@macnamara2019]. Even the theory's originator argues for strictly designed practice, not hours [@ericsson2019]. There is no threshold of hours that turns anyone into an expert.
:::

## Experience is not expertise {#ch20.sec.experience}

If practice explains so little in professions, what about plain experience? Surely ten years in a job makes you better at it.

Sometimes. A meta-analysis of work experience and job performance found an overall correlation of .27, but the *kind* of measure mattered: experience counted as the **amount** of relevant work done (ρ = .43) or at the level of specific **tasks** (.41) predicted performance far better than time-based measures such as years in the job [@quinones1995]. That fits Part I's most surprising number: in the revised hiring research, years of job experience predict a new hire's performance at only .07 [@sackett2022], which is why [[ch04.sec.close-enough]] told you not to be put off by "five years required".

The most sobering evidence comes from medicine. A systematic review of 62 evaluations found that in 52% of them, physicians' quality of care *declined* with years in practice on every outcome measured, and in another 21% it declined on some outcomes; only 2% found steady improvement [@choudhry2005]. Years in practice also stand in for how long ago a doctor trained, so this is not simply "doctors get worse". It is a warning that experience without updating does not automatically become expertise.

What separates the two? The best answer comes from an unusual paper in which two research traditions that usually disagree, one known for documenting the flaws of intuition and one for studying experts who rely on it, set out to find where they agreed. Their conclusion: intuitive expertise can be trusted only when the environment is **regular enough to be predictable**, and the person has had the chance to **learn its regularities through practice with feedback**. And, crucially, "subjective experience is not a reliable indicator of judgment accuracy" [@kahneman2009]. Feeling sure is not evidence of being right.

So for each part of your job, the question is not "how long have I done this?" but **"do I find out, quickly and clearly, whether I was right?"** Where the answer is yes (a test passes or fails; a customer churns or stays this week), experience tends to become skill. Where the answer is no (an architecture decision that plays out over three years, a hire, a strategy), experience can accumulate for a decade without teaching you much, and your confidence will grow anyway.

## Building practice into the job {#ch20.sec.loop}

Most jobs do not come with a coach, a curriculum or fast feedback. That is why a decade at work can be a decade of improvement, or one year repeated ten times. The lever the evidence points to is to **design practice into the work you already do** [!view].

Three ingredients have evidence behind them, and a fourth is craft.

**A notch beyond what you can do, but not three notches.** In a study of 225 on-the-job experiences of 60 managers, more challenging assignments developed more leadership skill, but with diminishing returns: each extra step of difficulty helped less than the one before [@derue2009]. A stretch assignment is valuable; a sink-or-swim one is less valuable than it feels.

**Feedback, fast and about the task.** In the same study, access to feedback offset those diminishing returns: the most challenging experiences paid off when people could find out how they were doing [@derue2009]. Feedback helps on average, but less, and sometimes harmfully, when it turns attention from the task to the self [@kluger1996]. And you usually have to ask for it, deliberately, because people seek feedback less as their tenure grows [@anseel2015]. [[ch13.sec.receiving]] has the scripts, and the quarterly three lines from [[ch18.sec.disagree]] are a ready-made occasion to use them.

**Retrieval and spacing, for anything you need to know.** For learning material, two techniques earned the top rating for usefulness in a major review: testing yourself and spacing your practice out over time; rereading and highlighting earned the bottom rating [@dunlosky2013]. The best gap between sessions grows with how long you need to remember [@cepeda2006]. If you are learning a new codebase, a regulation or a domain, explain it to yourself from memory and come back to it next week, rather than reading the documentation twice.

**Artificial feedback where the real kind is slow.** Where the job will not tell you quickly whether you were right, make it [!craft]. Write down your prediction before a decision ("this design will need a rewrite within a year if traffic doubles"), with your reasons, and look at it when the outcome arrives. Run a short review after things go well, not only after they go wrong. Ask someone who will see the result to tell you about it.

::: figure {#ch20.fig.loop src="ch20/loop.svg"}
Alt: A loop of four steps around a centre labelled "one sub-skill at a time": "1, pick one sub-skill"; "2, do it for real, a notch harder"; "3, get feedback, fast, about the task"; "4, write down what you'll change", which leads back to step 1. Below the loop, a small chart titled "Challenge pays, with diminishing returns", with "challenge" on the horizontal axis and "skill gained" on the vertical: a line labelled "without" rises and then flattens, and a line labelled "with feedback" keeps rising. A note under the chart: "shape illustrative, after DeRue and Wellman (2009)".

A learning loop at work. Challenge develops skill with diminishing returns; feedback keeps the returns coming. The curves show the shape of the finding, not its data.
:::

Here is what that looked like for Dev. That week she closed the three course tabs, spent the learning budget on a book about how distributed systems fail and two days at a testing conference, and sent the pricing engineer a time for Tuesday. Then, over the following year, she picked one sub-skill: **designing test seams into a service before it is built**, rather than retrofitting tests afterwards. She got reps by offering a thirty-minute design review to every squad starting a new service, which also answered the messages from people like the pricing engineer. She got fast feedback by asking each squad, three months later, which of her suggestions they had used and which had been a waste of time, and she kept a running log of the answers. And she wrote down her predictions ("this queue will be the hard thing to test") so she could check them. None of it took extra hours. It took the hours she was already spending, arranged differently.

:::: move {#ch20.move.stretch} Design one stretch assignment
Pick one sub-skill you want to improve over the next three months. Design a stretch assignment for it, inside your current job, by answering five questions:

1. **The sub-skill**, narrow enough to practise (not "leadership" but "running a design review with people senior to me").
2. **The reps**: where, in your existing work, will you do it at least once a fortnight?
3. **The notch**: what makes it harder than what you already do comfortably, but not three notches harder?
4. **The feedback**: who will tell you how it went, how soon, and what specific question will you ask them?
5. **The record**: where will you write your predictions and what you learned?

::: answer
Strong designs have three things in common.

- **The sub-skill is narrow.** "Get better at system design" cannot be practised; "write the failure-modes section of design documents, and have a senior engineer critique it" can. Narrow skills give you a clear sense of whether you are improving.
- **The reps already exist.** The best stretch assignments are hidden inside work you were going to do anyway. If the plan needs ten extra hours a week, it will not survive the first busy month.
- **The feedback question is specific and about the task.** "Any feedback?" gets "looked good". "Which risk did I miss in the design review?" gets an answer. Feedback about the work helps more reliably than feedback about you [@kluger1996].

A common weakness is the notch. People either choose something they can already do (no stretch) or something wildly beyond them (diminishing returns, and often a bruising failure). If you are unsure, start one notch lower than you think, with the best feedback you can get. The evidence suggests feedback is what makes harder challenges pay [@derue2009].
:::
::::

## Seventy, twenty, ten {#ch20.sec.seventy}

If you work somewhere with a learning-and-development team, you have probably met a confident split of how people learn at work.

::: myth {#ch20.myth.seventy verdict=partly grade=moderate} 70% of learning happens on the job, 20% from other people and 10% from courses
The direction is plausible: most of what you know about your job, you learned doing it. The numbers are not measurements. A critical review of the "70% rule" found its evidential basis weak, citing sloppy scholarship, inconsistent concepts and research problems, and concluded that it "needs to be set aside" [@clardy2018]. A qualitative study of the framework in the Australian public sector found that it did not build manager capability as hoped, partly because organisations assumed that unstructured experience would build capability by itself [@johnson2018!]. The usual origin story, 1980s research on executives, could only be traced through secondary sources, so we do not repeat it.
:::

The second half of that verdict is the useful part. "Learn on the job" is good advice only when the job contains the ingredients from the last section: a notch of stretch, feedback, and some deliberate structure. Left to itself, a job mostly teaches you to do what you already do, a little faster.

## Mentors, plural {#ch20.sec.mentors}

The other piece of standard advice is to find a mentor. It is good advice with a modest evidence base.

Meta-analyses find that mentoring is associated with career benefits, but its effects on objective outcomes such as pay and promotion are small, and its effects on how people feel about their careers are larger [@allen2004; @eby2008]. Part of that may even be selection: promising people attract mentors. Where the evidence is more specific, it is also more useful. New first-line leaders learned their roles faster when their own boss both **modelled** good leadership ("show") and **gave them information** about the job ("tell"), especially if they had never worked for an exceptional leader before [@dragoni2014]. That is a finding about the manager's job, and [[ch21]] returns to it.

Two ideas make mentoring more useful than the single wise-elder model suggests. The first is from theory: development usually comes from a **network** of relationships rather than one mentor, varying in how close they are and what they offer [@higgins2001]. Different questions need different people. The person who can teach you to design for testability is rarely the person who can tell you how promotion committees think, and neither may be the person who can help you decide whether to manage. The second is the distinction from [[ch19.sec.ledger]]: a mentor advises, a sponsor advocates [@ibarra2010]. You probably need both, and they are rarely the same person.

::: scene {slug="INT. BEA'S KITCHEN — SATURDAY, 4 PM"}
Bea's laptop is open on the kitchen table, as it was nearly three years ago, but this time it is showing her inbox, and she has turned it round so Dev can see.

@bea: That one's from a payments company in Berlin. That one's from someone at a bank. That one wants to know if I'll speak at a conference, and the answer is no.

Two years ago, Bea wrote a small tool at Corvid so that she could change the new billing engine's database without taking it offline. She put it on the internet, with Corvid's permission, because it seemed rude not to. Then she kept fixing it, every time someone found a case it did not handle, for two years. It now has a history of every bug anyone ever reported, a manual Bea rewrote three times, and a following among people who move money for a living and cannot afford downtime.

@dev: You're one of the best people in the world at this. Do you know that?

@bea: I'm one of the only people in the world who cares this much about it. That's not the same thing.

@dev: It sort of is. That's what rare means.

@bea: I didn't choose it. I just kept refusing to let a migration go out untested.

@dev: That's choosing. Slowly. For two years.

Bea thinks about this, and takes a biscuit, and does not argue, which for Bea is agreement.
:::

Bea's story is the career-capital argument in miniature, and it closes a loop from Part I. Her film was always excellent; what she lacked was a trailer. Two years of public, specific, checkable work, with a history that cannot be faked, has become one without her trying, exactly the kind of strong signal that [[ch01.move.signal]] rated highest, and a standing work sample, the kind of evidence [[ch08]] is about. She will still dread the phone screens. But the next time she plays the snapshot game, she will not be playing it empty-handed.

:::: move {#ch20.move.mentors} Two mentors for two questions
1. Write down the two most important questions about your work that you cannot answer yourself right now. Make them specific: "How do senior engineers here decide when a design is good enough?" not "How do I grow?"
2. For each question, name one person who could genuinely help with *that* question: someone who has done the thing, recently, and whom you could reach.
3. Write the first message to one of them: what you are trying to learn, why them, and a small, specific ask (thirty minutes, one document reviewed, one meeting you could sit in on).

::: answer
Good answers separate the questions, because different questions need different people. A typical pair is one **craft** question (how to get better at a specific skill) and one **career** question (how decisions about people like you are made here). A good craft mentor is often someone a few years ahead in the same kind of work; a good career mentor is often someone more senior, sometimes in a different team [!craft].

The message works best when the ask is small and concrete. People underestimate how likely others are to say yes to a direct request for help [@flynn2008], so the main risk is not asking at all. "Would you be my mentor?" is a large, vague commitment that many busy people will politely avoid. "Could you look at my design document's failure-modes section and tell me what a senior engineer would add?" is easy to say yes to, and it often turns into a relationship anyway.
:::
::::

## Choosing without predicting the future {#ch20.sec.choosing}

That leaves the question from the opening scene. Rex says machine learning; the platform squad says cloud certifications; the pricing engineer says testability. How do you choose when nobody, including Rex, knows what will matter in ten years?

Two pieces of evidence help, from the research on interest. People who believe that passions are found rather than developed are less interested in topics outside their existing interests, expect a found passion to bring endless motivation, and lose interest faster when a new interest gets difficult [@okeefe2018]. So interest is not only something you discover; it often grows as you get better at something. But the opposite belief is not the only route to a good working life: people who believe in finding the right fit can also end up satisfied and successful [@chen2015]. Neither belief is a trap. Expecting a skill to feel like a calling before you are any good at it may be.

::: craft {by=author} A portfolio, not a prediction
We think the honest answer is to stop trying to predict, and to build a small portfolio instead.

**One deep skill** that is already pulling you: something people ask you about, which sits on the top-right of [[ch20.fig.compound]], and which your current job gives you reps and feedback for. This is where most of your deliberate effort goes.

**One or two adjacent skills** that make the deep one more valuable: for Dev, designing interfaces that other teams depend on, and writing well enough that her design reviews travel without her.

**One small exploratory bet**, chosen partly because it is new: a course, a side project, a few months on a different kind of problem. Most bets will not pay. That is what makes it a bet, and it is also how you find the next deep skill before you need it.

Trends matter, and Rex is not wrong that some tools will reshape the work. But a trend is most valuable when it compounds with what you already have. "Machine learning" in general is a crowded field to enter from scratch; "how to test systems that include machine-learning models" is a corner of it where Dev would start halfway up. Ask of any new skill: *does this make my existing capital worth more, or does it start me again from zero?* Sometimes starting from zero is right. It should be a choice, not a fashion.
:::

Try it on your own skills, in the tab Dev opened at the start of the chapter.

:::: move {#ch20.move.portfolio} Your skill portfolio
Make your own *Skills* tab with three rows and four columns.

| | The skill | Why it compounds | Where the reps and feedback come from | What I'll do this quarter |
| --- | --- | --- | --- | --- |
| Deep | | | | |
| Adjacent | | | | |
| Exploratory | | | | |

Fill it in, then check each row against the three questions from [[ch20.sec.capital]]: do many employers value it, is it hard to acquire, and does it go stale slowly?

::: answer
Three things to check.

- **Is the deep skill something people already ask you about?** If not, it may be an aspiration rather than a deep skill, which is fine, but then it belongs in "exploratory" until the job gives you reps and feedback for it. The signal Dev ignored for a year was the messages in her chat.
- **Does the reps-and-feedback column name real things?** "Online course" is a source of information, not of reps. If the deep skill has no feedback in your current job, that is worth raising with your manager, or a reason to look for a job that has it ([[ch22]]).
- **Is the exploratory bet small?** It should cost a few hours a week, not your evenings for a year. If it starts to compound with your deep skill, promote it.

If your portfolio is all exploratory, you are collecting rather than building. If it has no exploratory row, you are optimising for the world as it is now. Both are common. Neither is fatal; one row at a time is how portfolios change.
:::
::::

Some questions people ask about this, usually late in a career conversation.

::: ask
Q: I'm a generalist. Is that bad?

A: Not necessarily. Many valuable skills are combinations, and a generalist can be the person who connects specialists. But "generalist" can also mean "never practised anything deliberately". The test is the same: can you name something you are getting measurably better at, with feedback?

Q: Should I get a certification?

A: Sometimes a credential is a genuine knockout, a requirement you cannot be hired without ([[ch04.sec.close-enough]]). Otherwise, treat it as one input to career capital among several, and be wary of collecting generic credentials, which even the frameworks that champion career capital warn against [@todd2026!]. A certificate is usually a weaker signal than work someone can inspect [!view].

Q: I'm in my forties. Is it too late to get good at something new?

A: Age is largely unrelated to core task performance, creativity and performance in training, according to a meta-analysis across ten dimensions of job performance [@ng2008]. The constraint is rarely age; it is usually time and the absence of reps. The loop in [[ch20.fig.loop]] works the same at any age.
:::

A year later, Dev's *Skills* tab looked like this.

::: scene {slug="INT. DEV'S FLAT — ONE YEAR LATER, SUNDAY, 9 PM"}
The *Skills* tab has three rows, and a year of notes under the first.

*Deep: making systems testable, before they're built.* Thirty-one design reviews, a log of which suggestions the squads actually used, and a column of predictions that is right more often than it was a year ago.

*Adjacent: designing interfaces other squads depend on. Writing.*

*Exploratory: how you test a system that includes a model.* Rex has been insufferable about this, exactly as predicted.

Then her phone buzzes. It is Tomás, which on a Sunday is unusual.

@tomas: No emergency. Can we grab half an hour tomorrow? There's something I'd like you to think about. It's not a project.
:::

It is, as Dev half suspects, the biggest skill choice of all, disguised as a promotion.

::: coming {ref=ch21}
In [[ch21]], Tomás asks whether she wants to lead a team. Managing people is not a harder version of engineering but a different job, with its own skills to build from scratch, and the chapter looks at who succeeds at it and how to try it without betting a career on it.
:::

Whatever she decides, the method is the same as for any other skill: choose on purpose, practise in the job, get feedback, and keep the portfolio honest.

::: rewind
- **Career capital** is a practitioner idea, not a finding, but the evidence behind it is real: much human capital is specific to an occupation, and specific skills in fast-changing fields lose value quickly.
- A skill worth building is **valued by many employers, hard to acquire, and slow to go stale**. Rare combinations of ordinary skills often beat single rare talents. Dev's QA years were half of hers.
- **Ten thousand hours is a myth.** Deliberate practice explained under 1% of performance differences in professions; both sides of the debate agree that the design of practice matters far more than the hours.
- **Experience is not expertise.** The amount of relevant work predicts performance better than years served, and experience becomes skill only where the work is regular and gives you feedback. Feeling sure is not evidence of being right.
- **Build practice into the job**: one narrow sub-skill, reps a notch harder, fast feedback about the task, and written predictions where real feedback is slow. Challenge pays with diminishing returns; feedback keeps it paying.
- **70-20-10 is a slogan, not a measurement.** Learning on the job works only when the job has stretch, feedback and some structure.
- **Mentoring helps modestly**; think of a network of people for different questions, and remember that advice and advocacy are different things.
- **Choose a portfolio, not a prediction**: one deep skill, one or two adjacent ones, and a small exploratory bet.
:::
