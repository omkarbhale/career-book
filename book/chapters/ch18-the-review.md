---
id: ch18
status: review
---

::: scene {slug="INT. DEV'S FLAT — SUNDAY, 3 PM"}
The email arrived on Friday: *Annual review cycle: self-assessments due by end of next week.* The form has three boxes and a drop-down. *What did you accomplish this year? How did you work with others? What do you want to develop next?* The drop-down asks Dev to rate herself from 1, *Not yet meeting expectations*, to 5, *Outstanding*.

She starts with the first box and types from memory.

> *This year I worked on the rates service and the reconciliation project. I helped the team with testing and onboarding. I improved my communication.*

She reads it back. Every word is true. It is also, almost exactly, the résumé she had at Corvid: a list of duties with her name on top. A year of work, and from memory it comes out as three sentences that anyone on her squad could have written.

So she opens the spreadsheet, scrolls past *Game 1*, *Game 2* and *Game 3*, and clicks on *Wins*.

Twenty-eight lines. The Northwind recovery and the early-warning habit that came after it. The invoice-sync race condition, with a link to Marcus's correction in the demo channel. The duplicate-shipment defect she caught before the reconciliation release. And between them, gaps: a run of seven empty weeks in the spring, five more in the autumn, the weeks when her calendar belonged to other people's interviews and a coffee machine.

She duplicates the tab and renames the copy *Self-review*. Then she texts Bea, who has survived three review cycles at Corvid.

@dev: How do you write a self-review?

@bea: At Corvid? You don't, really. There's a curve. Two "exceeds" per team, and they go round like the washing-up rota.

@dev: That can't be true.

@bea: It's not *officially* true.
:::

Of all the moments in the career game, this is the most ordinary and, for most people, the most consequential. Once or twice a year, someone looks back at months of your work and turns it into a paragraph and a number. The number often decides your pay rise, feeds your next promotion and follows you into the next review. And as [[ch01.sec.career-game]] warned, it says a surprising amount about the person who gave it.

This chapter opens the machine up. How a review is actually made; how much of a rating is about you and how much is about the rater, the system and the room; where bias gets in; and the parts you can genuinely influence, which are fewer than you would like and more than you might fear. It ends with Dev's first review, a rating she did not expect, and what she did about it.

::: pause
Before you read on, a guess. When researchers split the variation in performance ratings into its sources, what share do you think reflects the actual performance of the person being rated? Write down a percentage. The answer is a few pages away.
:::

## How a review is made {#ch18.sec.cycle}

Review systems differ a great deal between organisations, and some companies have abandoned formal ratings altogether. But most formal systems run some version of the same cycle, and it is worth knowing its parts before you try to influence any of them [!craft].

It starts, in theory, with **expectations**: at the beginning of the year, you and your manager agree what good looks like for your role and your work. Then comes **the year itself**, during which the evidence of your performance piles up, mostly in people's memories. Near the end, you write a **self-assessment**. Your manager writes a draft, often with input from others: at Lanternfish, Kai, as Dev's squad lead, writes a section ([[ch15.sec.promotion]]). Then the drafts go to **calibration**, a meeting where managers compare their proposed ratings across teams and adjust them. Finally there is **the conversation**, in which you hear the result, and behind it, **pay and promotion** decisions that use it.

That last link is often direct. At Microsoft until 2013, for example, each employee got a single rating from 1 to 5, built from their manager's assessment and a calibration process, and that one number drove merit pay, bonuses and stock awards [@shrm2013]. Calibration meetings are widespread, though they take many forms [@speer2019]. And companies that announce they have "got rid of ratings" rarely get rid of evaluation: as one side of a published expert debate put it, performance is always evaluated in some manner, and the alternatives to ratings may be worse [@adler2016]. A company with no ratings still decides who gets the raise. You just cannot see the number.

::: figure {#ch18.fig.cycle src="ch18/cycle.svg"}
Alt: A vertical timeline of a review year with five stops. 1, "Expectations", start of the year: what good looks like, agreed with your manager; marked with a gold star, "you shape this". 2, "The year", evidence piles up, mostly in memories; gold star, "you shape this". 3, "Self-review", your account of the year; gold star. 4, "Draft and calibration", your manager's draft compared with others' in a meeting; drawn with a dashed outline and labelled "a room you're not in". 5, "The conversation", you hear the rating; an arrow leads off to "pay, promotion, next year". A note at the bottom: "Most of your influence comes before the room, not after it."

The anatomy of a review cycle. The stars mark the stages you can shape; the dashed stage is where much of the outcome is decided, without you. Your influence on that room is exercised before it meets.
:::

Look at where the stars are. Three of the five stages are yours to shape, and all three come *before* the meeting you will never attend. By the time you hear the result, most of what could have changed it has already happened. That is the single most useful thing to know about reviews, and the rest of this chapter keeps coming back to it.

## How much of a rating is about you? {#ch18.sec.noise}

Now the uncomfortable part, and the answer to the pause.

In a study of more than 4,000 managers, each rated by seven people (two bosses, two peers, two direct reports and themselves), the researchers split the variation in the ratings into its sources. The raters' own idiosyncratic tendencies accounted for **62% and 53%** of the variance in the two data sets. The managers' actual performance, general and dimension-specific together, accounted for **21% and 25%** [@scullen2000]. Random error took 11% and 18%, and whether the rater was a boss, a peer or a report added only a little. If you guessed something like 50% or more for performance, you are in good company, and the data says otherwise.

::: figure {#ch18.fig.variance src="ch18/variance.svg"}
Alt: Two horizontal bars, one per data set, each split into segments that add up to 100% of the variation in ratings. Data set 1 (2,350 managers): the rater's own tendencies 62%, in purple; the ratee's performance 21%, in gold; random error 11%; the rater's role 6%. Data set 2 (2,142 managers): rater's tendencies 53%; performance 25%; random error 18%; rater's role 4%. A label above the bars reads "who rates you" over the purple and "what you did" over the gold. A note: "Shares of variance across many ratings, not of any one person's rating."

What goes into a rating, from Scullen, Mount and Goff (2000). Who rated a manager moved the numbers more than twice as much as how the manager performed. These were developmental ratings, not pay-setting reviews.
:::

Read that carefully, because it is easy to misread in both directions. It does *not* mean that 62% of your particular rating is about your manager. It is a share of the variation across thousands of ratings: if you want to predict how a given rating will come out, knowing who gave it tells you more than knowing how the person performed. Those were also ratings for development, not ratings tied to pay, and researchers still argue about how much of a rater's "idiosyncrasy" is noise and how much is a genuinely different, legitimate view. But other evidence points the same way. When two supervisors rate the same person's overall performance, their ratings agree at an average reliability of about **.52** [@viswesvaran1996]: real agreement, far from perfect.

::: receipts {source=scullen2000} The rater is part of the measurement
**What they did.** Scullen, Mount and Goff took two large sets of 360-degree ratings (2,350 and 2,142 managers), in which each manager was rated on three performance dimensions by seven people, and used statistical modelling to estimate how much of the variation came from five sources: the manager's general performance, their performance on the specific dimension, each rater's idiosyncratic tendencies, the rater's organisational perspective (boss, peer or report), and random error [@scullen2000].

**What they found.** Rater idiosyncrasy was the largest source by far, at 62% and 53%. Performance, general and specific combined, was 21% and 25%, less than half as large. Perspective effects were small, and random error was 11% and 18%.

**What it cannot tell you.** These were developmental ratings of managers, which carry no pay consequences; ratings that decide money may be cleaner, or more political. The model cannot tell a rater's bias from a rater's honest, different view of the same person. And it describes populations of ratings, not your review.
:::

Why do raters differ so much? Partly because they combine the same facts in different ways. In one experiment, managers given identical employee profiles clustered into three different "policies": some weighted task performance most heavily, some weighted counterproductive behaviour most, and some weighted both [@rotundo2002]. One manager's "solid, reliable" is another's "fine, but where's the initiative?". And partly because ratings drift from performance for reasons that have nothing to do with skill: measurement error, systematic non-performance factors such as how much the rater likes or sees you, and sometimes deliberate distortion, when raters have reasons to rate higher or lower than they believe [@murphy2008].

::: myth {#ch18.myth.rating verdict=partly grade=strong} Your rating measures your performance
It does measure it, partly: performance is a real and substantial source of variation in ratings. But in two large data sets, the raters' own tendencies explained more than twice as much variance as the ratees' actual performance [@scullen2000]. Two supervisors rating the same person agree at about .52 [@viswesvaran1996], raters weigh identical facts differently [@rotundo2002], and ratings drift for reasons that have nothing to do with the work, including deliberate distortion [@murphy2008]. A rating is a measurement taken with a noisy instrument, and the rater is part of the instrument.
:::

Two practical lessons follow, and they pull in slightly different directions [!view].

The first is for your self-esteem. **One rating from one manager is weak evidence about you.** Do not build your self-image on it, in either direction. A disappointing review from a manager you have worked with for eight months is a data point, not a verdict, and the same goes for a glowing one.

The second is for your strategy. Since the rater is part of the instrument, **making your work easy for the rater to see accurately is not vanity; it reduces the noise.** A manager who has a clear, specific record of what you did has less room to fill the gaps with impressions. That is the snapshot game's lesson from [[ch01.sec.signals]], replayed for an internal audience, and it is most of what you can do about the 62%.

## Curves {#ch18.sec.curves}

Bea's washing-up rota is a joke, but the system behind it is real. Under **forced distribution**, also called stack ranking or a forced curve, managers must place fixed shares of their people in each rating band: so many at the top, most in the middle, a few at the bottom, whatever the team actually did.

The case for it is that it stops managers rating everyone "exceeds" and makes them identify weak performers. A simulation gives that case its best hearing: a system that fired a fixed share of the bottom each year *could* noticeably raise a workforce's average potential, with most of the gain in the first several years [@scullen2005]. But the simulation left out morale, collaboration, gaming and legal costs, and experiments have since measured some of them. Raters found forced systems harder to use and less fair, especially for pay decisions and when the team's performance did not vary much, and that lowered their confidence in giving feedback [@schleicher2009]. In three experiments, forced ratings sped up individual work but slowed teamwork and reduced knowledge sharing [@loberg2021]. On a creative task, they raised stress without raising performance, and supervisors' ratings started tracking eloquent writing and strategic gaming more, and actual creativity less [@cardinaels2021].

Microsoft, one of the best-known users, ended its curve in November 2013, its HR head announcing "No more curve" and no "pre-determined targeted distribution" [@shrm2013]. That is a record of what one company did, not proof that curves fail. But the experimental evidence and that decision point the same way.

Underneath every curve sits an assumption: that performance in a team falls on a bell curve, so that the right shares can be fixed in advance.

::: myth {#ch18.myth.bell-curve verdict=partly grade=moderate} Performance follows a bell curve
This one is genuinely contested. Across 198 samples and more than 630,000 people, O'Boyle and Aguinis found that performance followed a heavy-tailed, "power law" distribution, with a few stars far ahead of the rest, not a bell [@oboyle2012]. But their measures were mostly outputs such as publications, awards and wins, and Beck, Beatty and Sackett showed that measures like those tend to produce skewed distributions, while measures that capture whole jobs, over a fixed period, for comparable roles, fit a normal curve better; they concluded that large departures from normality are often an artefact of measurement [@beck2014]. So neither "a bell" nor "a few superstars" is settled. What neither side supports is the assumption a forced curve makes: that every team of eight contains exactly the same shares of high and low performers.
:::

You may never work under a formal curve. Many companies use softer "guidelines" for how many people should land in each band, and a calibration meeting can work like a curve even without a rule. The practical point is to **know which system you are in**, because it changes what a rating means. Under a curve, your rating depends on your teammates as well as on you. A "meets expectations" in a strong team under a forced distribution may be a better result than an "exceeds" somewhere else.

## The room you're not in {#ch18.sec.calibration}

Calibration is where the dashed box in [[ch18.fig.cycle]] lives. Managers bring their proposed ratings to a meeting, compare them across teams, argue about the borderline cases and adjust. It exists because individual managers rate so differently, and there is some evidence that it helps. In two field studies, managers saw calibration as an attempt to improve rating quality; it came with more accountability and more information, and ratings after calibration correlated better with other measures of performance than ratings before it [@speer2019].

That is one of very few academic studies of calibration, and it does not test the question you probably care about: what happens to people whose manager argues weakly in the room. So what follows is our view, built from how calibration works rather than from a test of it [!view]. In calibration, **your rating is decided partly by people who mostly know you through your manager's summary.** Two things follow. Your manager needs to be able to say what you did, and why it mattered, in a sentence or two that strangers will accept. And it helps a great deal if someone else in the room has seen your work for themselves.

::: craft
**Give your manager the sentence.** Before review season, and ideally before each quarter's check-in, send your manager a short note: two or three of your most important results, each in one line, with the evidence attached (a link, a number, a name). Write it so that it would make sense to someone who has never met you. Managers in calibration often have a dozen people to represent and a few minutes for each; the one whose case is already written down is easier to argue for. This is practitioner advice, widely given and not tested as far as we know.
:::

Calibration is a smaller version of the hiring funnel in [[ch03.sec.funnel]]: a fixed budget, a panel of people who do not know you well, and noise. And the second need, someone in the room who has seen your work for themselves, is the beginning of a much bigger idea.

::: coming {ref=ch19}
In [[ch19]], the person who speaks for you in a room you are not in gets a name, a sponsor, and Part II's trust ledger turns out to be the currency they spend.
:::

## What else gets into the number {#ch18.sec.bias}

A rating carries the same social biases as any other human judgement. The evidence on this is real, and it is also mixed in size, so it is worth being precise about where the gaps show up and where they mostly do not.

Start with the ratings themselves. A meta-analysis of field studies found that women, on average, scored *slightly higher* than men on measures of job performance (d = −.11) [@roth2012]. A recent study of more than 20,000 employees at one multinational company found gender differences in performance and potential ratings that were statistically significant but small to negligible, slightly favouring men, and larger or smaller depending on the gender mix of the department [@kordsmeyer2026]. So the headline rating is not where the largest gaps usually appear.

They appear around it. **In the words.** In one Fortune 500 technology company, men and women were equally likely to be described as technically able in their reviews, but women were more often called "too aggressive" and men "too soft", and "taking charge" went with the highest ratings for men, but not for women [@correll2020]. **In "potential".** The same meta-analysis that found performance ratings slightly favouring women found that ratings of *promotion potential* favoured men [@roth2012], and [[ch19]] shows how much that matters. **In turning ratings into money.** In personnel data from a large service organisation, women and minority employees received less salary growth than white men *with the same performance-evaluation scores* [@castilla2008]. And in three experiments with 445 participants who had managerial experience, presenting a company as explicitly meritocratic made them award a man a larger bonus than an equally performing woman [@castilla2010]. Believing your system is fair, it seems, can make it less so.

None of this means that every disappointing review is bias, and none of it means that bias is rare. It means the gaps tend to live in the softer, less visible parts of the process: the adjectives, the judgement of "potential", the step from a rating to a pay rise. Castilla's own conclusion is that merit systems with little transparency or accountability can increase bias [@castilla2008]. That is mainly a job for organisations, and for any reader who will one day manage.

For the person being rated, the evidence suggests one partial defence, and it is the same as before: **concrete, checkable evidence.** Self and supervisor ratings agree more when they rest on non-judgemental performance indicators [@heidemeier2009]. "Caught a defect before go-live that was duplicating shipments in a client's ledger" is harder to reframe than "detail-oriented". It will not remove bias. It narrows the room bias has to work in.

::: flashback {ref=ch03.sec.bias}
[[ch03.sec.bias|Chapter 3]] made the same point about hiring: most rejections are arithmetic, some are not, and neither fact is a reason to stop. The funnel does not become neutral once you are inside the building.
:::

If you believe a rating was discriminatory, rather than merely wrong, you are no longer dealing with a review problem. Keep your records, and look at the employment-law starting points in [[more.sec.law]].

## The self-review {#ch18.sec.self-review}

Back to Dev's three boxes. The self-review is the stage of the cycle you control most completely, and the one most people treat as a chore. It is worth knowing how good people are at it, because the answer is: not very, and not in the way you might think.

Across 22 meta-analyses, the average correlation between people's self-evaluations of ability and their objective performance was **.29** [@zell2014]. At work, self-ratings and supervisor ratings agree at about ρ = .34, and in Western samples self-ratings run more lenient than supervisors' (d = 0.32) [@heidemeier2009]. So people have some insight into their own performance, roughly as much as a mediocre outside predictor. The insight is better for specific, objective and familiar tasks [@zell2014], which is a hint about how to write a self-review.

The errors are not evenly spread, either. When women and men described their own performance on a male-typed maths and science task, women rated themselves lower than equally performing men, even when there was no incentive to promote themselves at all [@exley2022]. And overconfidence pays, at least at first: in six studies, overconfident people gained status in groups because their confidence made them look competent [@anderson2012]. Self-review season rewards confident self-description, and confidence and accuracy are only loosely connected.

You have probably heard the most famous claim about self-assessment, and it deserves a check before it shapes how you read yours.

::: myth {#ch18.myth.dunning-kruger verdict=partly grade=strong} The Dunning-Kruger effect: the less skilled you are, the more confident you are
The original 1999 studies found that the lowest-scoring quarter on tests of grammar, logic and humour placed themselves around the 62nd percentile while scoring around the 12th [@kruger1999]. But much of that pattern is produced by regression to the mean and the general tendency to think we are above average [@krueger2002], and random numbers reproduce the famous graph [@nuhfer2016]. With better methods, one large study found a small effect confined to a tiny fraction of people [@gignac2024], while a large replication supports a real, modest deficit: low performers are worse at telling whether each of their answers is right [@jansen2021]. Overall, self-assessment and ability are *positively* correlated [@zell2014]. Low performers overestimate the most, but they are not the most confident people in the room.
:::

So what makes a good self-review? Nothing in the research shows that writing a better one raises your rating; that is our view, not a finding [!view]. But the evidence above says what a *more accurate* one looks like, and accuracy is the job. It is the standard [[ch05.sec.accuracy]] set for a résumé, applied to an audience that has seen part of the film: **accuracy, not modesty, and not inflation.**

In practice, that means four things [!craft]:

- **Lead with outcomes, not activity.** "Worked on the reconciliation project" is a duty. "Caught a defect before go-live that was duplicating shipments in a client's ledger, and proposed the flag-off release that let us keep the date" is a result. The three questions from [[ch04.fig.duty]] work here unchanged: what changed, by how much, who noticed?
- **Make it checkable.** Link the ticket, the pull request, the thank-you message, the corrected credit. Specific, objective claims are where self-assessments are most accurate [@zell2014], and they are what your manager can carry into calibration.
- **Credit precisely.** Say what the team did and what you did. The Marcus correction in [[ch16.sec.credit]] is a gift here: a written, public record of who did what.
- **Name the gaps yourself.** One honest sentence about what did not go well, and what you learned, does more for your credibility than a fifth success. It also takes the sting out of your manager having to raise it.

That is a story bank again, and it is no accident. The rows of the *Wins* tab are the raw material, the self-review is the cut, and the stories you rehearsed in [[ch04.sec.story-bank]] turn out to be the same kind of object: true, specific, and built to survive a follow-up question.

::: flashback {ref=ch11.sec.wins}
In [[ch11.sec.wins|Chapter 11]], Dev started writing one line a week about what she did and what changed because of it, on the grounds that by month nine nobody, including her, would remember month two.
:::

The *Wins* tab saved Dev, but it also showed her its holes. The empty weeks were not weeks when nothing happened. They were the weeks the helping trap of [[ch17.sec.helping]] ate, and the weeks she simply forgot. To fill them, she went back through her film the way [[ch04.sec.mining]] suggested: her sent messages, her closed tickets, the demo-channel history, and two colleagues she asked, "What do you remember me doing this year?" Kai remembered the onboarding sessions she ran for new testers. She had forgotten she had rewritten them.

::: figure {#ch18.fig.habit src="ch18/habit.svg"}
Alt: Three stacked panels. The first, "Every week: one line", shows a grid of 52 small squares for the weeks of Dev's year; most are filled in gold, but two runs of empty squares are labelled "spring: 7 empty weeks" and "autumn: 5 empty". The second, "Every quarter: three lines to your manager", shows four small notes, each with three short lines. The third, "Once a year: the self-review", shows a single page with five bullet stories and one paragraph. Arrows connect the panels, and a note under the first reads "Fill gaps from: sent messages, tickets, demo channel, and two colleagues who remember." A footer: "Illustrative: Dev's year, not data."

The year-long evidence habit. A line a week becomes three lines a quarter, which become the self-review. The gaps are where memory, yours and your manager's, will fill in for you.
:::

Try the cut on Dev's year before your own. It is much easier to be ruthless with somebody else's material.

:::: move {#ch18.move.self-review} Write the self-review from your story bank
Here is Dev's from-memory draft, and six lines from her *Wins* tab. Rewrite the draft as a self-review answer to "What did you accomplish this year?" in no more than 150 words. Then do the same for your own year, from your records rather than your memory.

> *This year I worked on the rates service and the reconciliation project. I helped the team with testing and onboarding. I improved my communication.*

1. Northwind integration: missed my Thursday estimate; told Tomás late, on the Friday afternoon; rebuilt the plan, delivered the following Wednesday as promised.
2. Since then, early warnings on every slip (range, reason, checkpoint); no surprise slips since.
3. Found and fixed the invoice-sync race condition (Saturday repro; reviewed and extended by Marcus).
4. Reconciliation release: caught a defect duplicating shipments in the client's ledger under load, which the squad thought was a flaky test; proposed shipping on the date with that shipment type switched off; client told two days early.
5. Rewrote the onboarding sessions for new testers; ran them for six people.
6. Filed the Old Faithful ticket; sat on the coffee committee.

::: answer
A strong rewrite might read:

> *My biggest result was the reconciliation release: before go-live I showed that a test failure the squad had written off as flaky was duplicating shipments in the client's ledger, and proposed shipping on the date with that shipment type switched off, telling the client two days early. I found and fixed the invoice-sync race condition that had been paging people at 3 am (Marcus reviewed it and added the logging). Early in the year I missed my Northwind estimate and told Tomás too late; since then I give a range, a reason and a checkpoint for every estimate, and nothing has slipped without warning. I also rewrote the onboarding sessions for new testers and ran them for six people. Next year I want to work at a larger scope than a single release.*

Notice what changed. **Outcomes lead**: the defect and the date, not "worked on". **Credit is precise**: Marcus is named for his part. **The miss is in it**, with what changed afterwards, which turns a weakness into evidence of reliability ([[ch12]]). **The coffee machine is not**: filing a ticket was a good deed, but it is not what this review is for, a point [[ch19]] makes at greater length.

For your own: if a sentence needs a number you do not have, use before-and-after or scale, as in [[ch04.sec.no-number]]. If you cannot point to evidence for a claim, either find some or cut it. And check your verbs: if you find yourself writing "helped" and "supported" where "led" and "decided" would be accurate, you are shading your work down, which the research on self-description finds women doing more than equally performing men [@exley2022].
:::
::::

Dev rates herself a 4, *Exceeds*, after a long look at the drop-down, and submits on Thursday.

## The conversation {#ch18.sec.conversation}

::: scene {slug="INT. LANTERNFISH, TOMÁS'S OFFICE — TUESDAY, 2 PM"}
Tomás has printed the review, which is unusual for him, and he does not slide it across the table straight away.

@tomas: I'm going to give you the number first, because otherwise you won't hear anything else. It's a three. Meets expectations.

Dev had prepared for several things. Not that one. In their last one-to-one, Tomás had used the word *exceeds*.

@dev: OK.

@tomas: I'll be straight with you about how it happened, because you'd find out anyway. I went into calibration with a four. I came out with a three.

@dev: What happened in the room?

@tomas: Fourteen people at your level across four squads, and a guideline of about a fifth at four or above. The director asked what you'd done that someone else at your level wouldn't have. I started listing things. The reconciliation release, the race condition, Northwind. Someone said the race condition was Marcus's fix, from the demo. I corrected it. But by then I was defending a list, not making a case. That one's on me as much as you.

@dev: And Kai's section?

@tomas: Glowing. Read it. It's mostly about onboarding and the coffee committee.

Dev looks at the page and does not read it.

@dev: Can I take this away and come back to you on Thursday? I'd rather not respond to it right now.

@tomas: I'd like that. Thursday at ten.
:::

Dev's first instinct, sitting in that chair, was to argue. Her second, which she followed, was to stop talking. Both instincts have reasons, and the evidence on feedback explains why the second one was right.

## Hearing it {#ch18.sec.hearing}

Feedback, on average, improves performance. But in a classic meta-analysis, more than a third of feedback interventions made performance *worse*, and feedback helped less the more it drew attention away from the task and towards the self [@kluger1996]. [[ch13.sec.feedback]] used that finding to explain how to give feedback. Here it explains how a review lands. A rating is about the most self-focused piece of feedback there is: a number, about you, compared with other people, with money attached. It is almost designed to make you think about yourself rather than the work [!view].

People are also not neutral seekers of feedback. Research on why people ask for it finds three motives at work: an instrumental one (to get better at something), and two defensive ones, protecting the ego and protecting the image others have of us [@ashford2003]. In a review conversation, the defensive motives tend to wake up first. That is what makes two opposite mistakes so tempting: arguing the number on the spot, or going quiet and resentful and asking for no more feedback at all [!craft]. The second gives up the one input you fully control: feedback-seeking has a small direct link to performance, and it fades with tenure unless you keep doing it on purpose [@anseel2015].

A few habits help you hear a review as information rather than a verdict [!craft]:

- **Separate the number from the content.** The number is mostly settled. The content, what your manager and others saw, what they think you should do differently, is where the information is. Ask about the content.
- **Ask the forward question.** "What would a four have looked like, this year, in that room?" is more useful than "Why did I get a three?", because the answer is something you can act on.
- **Take the pause.** "Can I come back to you on this?" is a perfectly professional sentence. It moves the conversation from the moment when your defences are highest to a moment when you have read the written review twice.

::: trapdoor
**Deciding the job is over because of one rating.** A disappointing review is a good moment to look at your options, and a bad moment to make the decision. Remember what a single rating is: one noisy measurement, with the rater and the room built in. If the rating is part of a pattern (no growth, no clear path, a manager who will not explain), that is a real push reason, and [[ch02.sec.push-pull]] is where to sort it. If it is one disappointing number after a good year, the cheaper move is usually to fix what fed it, and see what the next cycle says.
:::

## Disagreeing well {#ch18.sec.disagree}

Sometimes, after the pause, you still think the review is wrong. Then the question is not *whether* to say so but *how*, because disagreeing with your manager has costs. In a field study and two experiments, managers rated employees who voiced challenging ideas as worse performers than those who voiced supportive ones, partly because the challenges felt less loyal and more threatening [@burris2012]. The answer is not silence; it is to disagree in a way that is plainly on the same side.

::: scene {slug="INT. LANTERNFISH, TOMÁS'S OFFICE — THURSDAY, 10 AM"}
Dev has brought one page. She has rewritten it four times, mostly to make it shorter.

@dev: Three things. Two are facts and one is a request.

@tomas: Go on.

@dev: First, the review describes the reconciliation release as a squad achievement. It was. But finding the duplicate-shipment defect was mine, and so was the flag-off proposal. I've attached the ticket and the thread. Second, the race condition. It says "contributed to". I found it, reproduced it and wrote the fix; Marcus reviewed it and added the logging. That's in the correction he posted in the demo channel.

@tomas: Both fair. I can change the write-up. I can't change the rating; calibration's closed.

@dev: I know. That's the request. I'd like to agree now what a four looks like next year, in writing. And I'd like to send you three lines every quarter, so you're not defending a list next time.

Tomás writes something in his notebook and underlines it.

@tomas: Yes to both. And one more, from me. Kai's section is about the onboarding and the coffee committee because that's what Kai saw you do. The next time you do the work that matters, I'd like someone other than me and Kai to see it.
:::

Look at the structure of what Dev did. She **separated facts from judgements**: the facts (who found the defect, who wrote the fix) she corrected, with evidence; the judgement (a three or a four) she did not relitigate. She **knew what could change**: once calibration has closed, the rating is often fixed, but the written record, which later reviews and promotion committees will read, usually is not [!craft]. And she **turned the disagreement into a plan**: expectations for next year, a habit that gives her manager what he needs for the room, and a request that the conversation continue. That is disagreement as [[ch13.sec.disagree]] describes it: about the work, aimed at the future, and plainly on the same side.

Tomás, for his part, did something good managers do and many do not: he admitted his share. "I was defending a list, not making a case" is a sentence that will matter a great deal in the next chapter.

:::: move {#ch18.move.disagree} Rehearse a disagreement about a rating
Here are three ways Dev could have opened on Thursday. Rank them from best to worst and say why. Then write the opening two sentences you would use about a review of your own that you think was wrong.

1. "I've thought about it, and honestly I think the three is unfair. Everyone knows I carried the reconciliation release."
2. "Two facts in the write-up are wrong, and I've brought the evidence. I'd also like to agree what a four looks like for next year."
3. "It's fine, really. I know calibration is tough. I'll just try harder next year."

::: answer
**Best: 2. Then 3. Worst: 1.**

- **2** separates facts from judgement, brings evidence, and points the conversation at something that can still change. It treats the manager as an ally with a problem to solve, which makes them more likely to act like one.
- **3** is polite and costs nothing today, but it gives up the two things that could change (the written record and next year's expectations), and "try harder" is not a plan. It also teaches your manager that disappointing you is free.
- **1** argues the one thing that is usually closed (the number), leads with a judgement ("unfair") rather than facts, and claims credit too broadly ("carried"), which invites a dispute about the word rather than the work. It is the kind of challenge that the research suggests gets read as disloyal [@burris2012].

For your own: start with the strongest *fact*, not the strongest *feeling*. Keep it to two or three points. And end with what you would like to happen next.
:::
::::

## What you control {#ch18.sec.control}

Put the chapter together and you get an honest, slightly sobering list. Much of what decides a rating is out of your hands. But the parts in your hands are concentrated in a few habits, and most of them happen long before the review.

| You can't control | You can influence |
| --- | --- |
| How idiosyncratic your rater is | Whether more than one person has seen your work first-hand |
| Whether there is a curve | Knowing the system, and reading your rating against it |
| What is said in calibration | Whether your manager walks in with a short, checkable account of your year |
| Bias in language, "potential" and pay | How much concrete evidence there is to reframe |
| Whether anyone volunteers feedback | Asking for it, specifically, all year |

The table is our synthesis of the evidence in this chapter, not a tested programme [!view]. Two of its rows deserve a word more.

**Expectations come first.** A review of a century of appraisal research, covering scale formats, rater training, rating sources and more, ends by calling for more attention to performance *management*, what happens all year, than to the mechanics of the rating [@denisi2017]. Pulakos and O'Leary argue that review systems fail precisely when they become administrative steps cut off from day-to-day expectation-setting and guidance [@pulakos2011]. You cannot fix your company's system. But you can fix the version of it that applies to you, by agreeing at the start of the year what good looks like, and checking it at every quarter.

**Feedback is yours to ask for.** People ask for feedback less as their tenure grows, and more when they have a learning orientation and a good relationship with their manager [@anseel2015]. Its direct link to performance is small, which argues for asking well rather than constantly: specific questions, about the work, a few times a year, and especially before the cycle closes rather than after it. Used that way, feedback stops being only something a review does to you and becomes a way of getting better at things, which is the subject of [[ch20]].

:::: move {#ch18.move.expectations} Set expectations for the year
Draft the note you would send your manager at the start of a review year (or the start of next quarter, if the year is under way). It should fit on one screen and contain:

1. the two or three results that would make this an excellent year, in your words;
2. for each, how you would both know it had happened;
3. one question about what the *next* level of your role looks like;
4. a proposed rhythm for checking in (for example, three lines from you every quarter).

::: answer
Strong notes share three features.

- **Results, not activities.** "Ship the carrier integrations" is an activity; "new carriers live within two weeks of signing, without on-call pages" is a result someone can check.
- **The evidence is agreed in advance.** If you both know what would count, the review becomes a comparison rather than a debate, and the self-review almost writes itself.
- **It asks about the next level early.** That question tells your manager you are thinking about growth, and the answer tells you whether this year's work is the right kind of evidence for it, which is the subject of [[ch19]].

If your manager never replies, send it anyway, and keep it. A record that you asked what good looks like, in writing, at the start of the year, is useful in any review conversation that follows.
:::
::::

A few things people want to ask about reviews and rarely do.

::: ask
Q: Should I rate myself high, to anchor my manager?

A: We found no evidence that a high self-rating pulls a manager's rating up, and some reason to think inflation costs you: self-promotion tends to annoy listeners more than self-promoters expect [@scopelliti2015]. Rate yourself where your evidence puts you. If that is a four, say four, and show why.

Q: My manager is the problem. What then?

A: Managers form relationships of different quality with different people on the same team, and the quality of that relationship is driven mostly by the manager [@dulebohn2012]. You cannot fix that alone. You can make sure other people see your work (a skip-level, a partner team, a project lead), keep your evidence in writing, and, if the pattern holds over more than one cycle, treat it as a real push reason ([[ch02]]).

Q: My company says it has no ratings. Does any of this apply?

A: Almost all of it. Someone still decides who gets the raise and who gets promoted [@adler2016]; the judgement has just moved somewhere you cannot see it. Ask your manager how pay and promotion decisions are actually made, and keep the evidence habit anyway.
:::

Dev, that Sunday, did the one thing on the list that cost nothing.

::: scene {slug="INT. DEV'S FLAT — SUNDAY, 9 PM"}
Dev opens the spreadsheet. The *Self-review* tab is done; she saves it and leaves it alone. Then she makes a fresh *Wins* tab for the new year, and this time she adds a column the old one never had.

*What I did. What changed. Who saw it.*

She looks at the third column for a long time. For most of last year's lines, the honest answer would have been *Tomás*, or *nobody*.

She types the first line of the new year anyway, and in the third column she writes *Tomás, Kai*, and then, after a moment, *the payments squad, at demo*. It is a start.
:::

That third column is where the next chapter begins. A review asks whether you did your job well. A promotion asks whether you are already doing the next one, and it asks a committee of near-strangers to decide. In [[ch19]], Dev finds out that a list of good things is not the same as a case.

::: rewind
- A review turns months of film into a paragraph and a number, through a cycle: **expectations, the year, the self-review, the manager's draft and calibration, and the conversation**. Most of your influence comes before the room you are not in.
- **Ratings are noisy measurements.** In two large data sets, raters' own tendencies explained 62% and 53% of rating variance, and the ratee's performance 21% and 25%. One rating is weak evidence about you.
- Because the rater is part of the instrument, **making your work easy to see accurately reduces noise.** That is translation, not vanity.
- **Forced curves** may weed out some low performers early, but they cost collaboration and rating accuracy, and whether performance even follows a bell curve is contested. Know which system you are in.
- **Calibration** decides part of your rating through your manager's summary. Give your manager a short, checkable account of your year, and make sure others see your work first-hand.
- **Bias** in headline ratings is often small; the larger gaps tend to appear in review language, in "potential" and in turning ratings into pay. Concrete evidence narrows the room it has.
- People's **self-assessments** are only moderately accurate, and women tend to shade theirs down. Write the self-review for accuracy: outcomes, evidence, precise credit and one honest gap. The Dunning-Kruger meme is overstated.
- **Hear it, then disagree well**: separate the number from the content, take the pause, correct facts with evidence, and turn the disagreement into next year's expectations.
:::

::: further {ref=more.sec.law}
This chapter treats a review as a measurement problem. If you believe a rating or a pay decision was discriminatory, it has become a legal one, and [[more.sec.law]] points to official starting points on employment rights in the regions the book covers.
:::
