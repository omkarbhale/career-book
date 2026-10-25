---
id: ch07
status: review
---

::: scene {slug="INT. LANTERNFISH, MEETING ROOM “THE DEPOT” — THURSDAY, 10:00 AM"}
The room is named after a lorry depot, which Dev decides is either charming or a warning. Three people sit across the table: Tomás, the engineering manager, bearded and calm in a blue plaid shirt; and two engineers from the backend team, each with a laptop and a single printed sheet.

One of the engineers reads her name off the sheet and smiles.

> *Dev. As in developer?*

@dev: Not yet.

It gets a laugh, which helps. Then Tomás leans forward.

@tomas: Tell me about a time you found a problem that nobody else had noticed. What did you do, and what happened?

For two seconds Dev's mind is a clean white wall. Then, from somewhere behind the wall, her story bank opens: the queueing bug, the one she found two days before go-live, before the client did. She starts talking.

While she talks, Tomás writes. Not much. A few words, and then something in a column on the right-hand side of his sheet. When she finishes, the second engineer asks the next question from *her* sheet, and Dev notices that it is printed, not improvised.
:::

Dev has walked into a measurement. She does not know yet what it measures, how it is scored, or how much the way she talks about the queueing bug matters compared with the bug itself. This chapter is about those things: what interviews are for, how good ones work, and how to show the people across the table what you can actually do, as yourself.

::: pause
Before you read on: what do you think Tomás is writing in the right-hand column? And would you rather be interviewed by someone with a printed sheet, or by someone who "just has a conversation"? Commit to an answer.
:::

## What an interview is for {#ch07.sec.for}

An interview is the employer's attempt to predict the film from a trailer, as [[ch01.sec.noise]] put it. Some interviews are much better at that than others, and the difference is not charm, or the interviewer's experience, or how hard the questions are. It is **structure**.

In a structured interview, every candidate for a role gets the same job-related questions, and every answer is scored against the same scale. In an unstructured one, the interviewer chats, follows their curiosity and forms an overall impression. In the most recent large review of how well selection methods predict job performance, structured interviews came top, with an average correlation of **.42** with later performance; unstructured interviews managed **.19**, less than half as much [@sackett2022]. Both numbers were higher in the classic 1998 estimates (.51 and .38), before the 2022 re-analysis argued that an earlier statistical correction had been applied too generously [@schmidt1998; @sackett2022]. The ranking survived the revision. The gap between them did too.

Laszlo Bock, then Google's head of people operations, put the same point bluntly, saying that brainteasers were "a complete waste of time" and that what worked were "structured behavioral interviews, where you have a consistent rubric" [@abc2013-google]. That was one employer describing its own internal data, which it did not publish, so treat it as a well-informed opinion rather than a finding. But it points the same way as the meta-analyses.

So the answer to the Pause is: Tomás is probably scoring your answer, against a scale, on a sheet that every other candidate's interviewers will also fill in. And if you had a choice, you should prefer that interviewer. The printed sheet is on your side.

## Structure is kindness {#ch07.sec.structure}

::: scene {slug="INT. MEERA'S KITCHEN, ON A VIDEO CALL — THURSDAY, 8:30 PM"}
Meera is holding a mug up to the camera. It says STRUCTURE IS KINDNESS.

@meera: Somebody gave it to me after I made a whole department use scoring sheets. They meant it as a joke. I use it every day.

@dev: It felt like being marked in an exam.

@meera: It's the opposite of an exam. In an exam, someone wrote the questions to catch you out. A good scoring sheet says, before anyone meets you, what a great answer to each question looks like. Then everyone gets the same questions and the same chance.

@dev: And without it?

@meera: Without it, I'd be scoring you on whether you reminded me of me. My gut likes people who went to my kind of university and laugh at my kind of jokes. My gut is not a hiring tool.
:::

Meera's "kindness" is two kindnesses. To the candidate, structure means being judged on the same questions as everyone else, against a standard written down before anyone walked in. To the interviewer, it is protection against their own instincts, which, as you will see later in this chapter, have a well-documented habit of preferring people who are like them [@rivera2012].

Here is what a scoring sheet usually looks like.

::: figure {#ch07.fig.scoring-sheet src="ch07/scoring-sheet.svg"}
Alt: A clipboard holding an interviewer's scoring sheet. At the top: "Q3. Tell me about a time you found a problem nobody else had noticed." Below it, a scale from 1 to 5 with anchors: 1, "vague, or someone else did it"; 3, "clear problem, clear personal action, some result"; 5, "noticed early, acted, checked the result, and changed something so it would not recur". A box labelled "evidence heard" holds handwritten notes: "queue bug, 2 days before go-live", "wrote a repro, paired with dev", "added a test to the nightly suite". On the row of score boxes, the 4 is circled in coral. At the foot of the sheet: "score alone, then discuss". Meera's plum mug sits beside the clipboard, labelled STRUCTURE IS KINDNESS.

A structured scoring sheet. The question and the anchors are written before the interview, and each interviewer scores alone before the panel compares notes. Notice that the anchors reward specific evidence, not confidence.
:::

Look at what the anchors reward: a clear problem, *your* action, a result you can describe, and what changed afterwards. None of them says "seemed confident" or "great communicator". That is the most useful thing a candidate can learn about structured interviews: **the sheet is listening for evidence**. Which means the best preparation is the evidence you assembled in [[ch04]].

::: craft
How good panels run [!craft]. Interviewers agree the questions and anchors in advance, each asks a different subset, and each writes their score *before* hearing anyone else's, so that the most senior or the most confident person in the room does not set everyone's number. Then they discuss the differences. You will not usually see any of this as a candidate. But you can ask, at the end, "How do you decide between candidates?", and the answer tells you a lot about how decisions get made there.
:::

## Two kinds of question {#ch07.sec.questions}

Structured interviews mostly use two kinds of question, and it is worth knowing which is which.

- **Past-behaviour questions** ask what you did. "Tell me about a time you found a problem nobody else had noticed." "Describe a disagreement with a colleague and how it ended."
- **Situational questions** ask what you would do. "Suppose a release is due tomorrow and you find a serious bug at 5 pm. What do you do?"

Both predict performance. Past-behaviour questions do slightly better on average: in the meta-analyses summarised in a major review, their average (uncorrected) validities were about .31, against about .25 to .26 for situational questions [@levashina2014]. The likely reason is the one [[ch01.sec.signals]] gave for strong signals: a description of something that happened is specific and checkable, and the interviewer can ask follow-up questions about it ("What did your manager say? What would you do differently?") that a rehearsed fiction struggles to survive.

That is the honest case for preparing stories. It is not a trick. It is what the instrument is built to measure.

## The story answer {#ch07.sec.story}

You will have met the most widely taught structure for answering past-behaviour questions: **Situation, Task, Action, Result**, usually shortened to STAR. Nobody seems to agree where it came from, and it does not matter. What matters is what the anchors on a scoring sheet listen for, and a good story answer is built to give it to them.

::: figure {#ch07.fig.story src="ch07/story.svg"}
Alt: Headed "a two-minute answer, roughly to scale": a horizontal bar running from 0 to 2 minutes, divided into four numbered segments, with each segment explained in a numbered row below. "Situation and task" is short, about 20 seconds: "the queue was dropping 1 in 2,000 messages; nobody had spotted it". "What I did" is the longest, about 70 seconds: "noticed a pattern in the test logs, wrote a reproduction, paired with the developer on the fix, added a nightly test". "Result" is about 20 seconds: "fixed two days before go-live; no repeats in a year". "What I'd keep" is about 10 seconds: "now I check retries first". A note below reads "a rule of thumb, not a finding: most of the time goes on what you did".

Anatomy of a story answer. Set the scene quickly, spend most of your time on what *you* did, land a result someone could check, and close with what you learned. The proportions are a craft rule of thumb, not a research finding.
:::

Five things turn a story into a good answer [!craft]:

1. **Start in the middle.** One or two sentences of context. The interviewer does not need the history of the client's insurance platform.
2. **Say "I".** Panels are trying to score *your* contribution. "We fixed it" leaves them guessing whether you watched. Say "we" for the team's work and "I" for yours, and be accurate about both.
3. **Spend most of the time on action.** Your decisions, what you tried, what did not work. This is where the follow-up questions will come from, so make it the part you know best.
4. **Land a result.** A number if there is one, a consequence if there is not: "the client never saw it", "the team now tests every merge".
5. **Stop.** Two minutes is plenty. If they want more, they will ask, and their follow-up question is a better guide to what they care about than your guess.

Dev's queueing-bug answer in the opening scene worked because it was already in the story bank she built in [[ch04.sec.story-bank|Chapter 4]], with the details checked and the result written down. If you skipped that chapter, now is the time: every past-behaviour question is a request for a story you either have ready or have to improvise. Under pressure, people do not rise to the occasion; they fall back on what they prepared [!view].

:::: move {#ch07.move.two-minute} The two-minute story
Pick one story from your story bank (or, if you skipped [[ch04]], one piece of work you are proud of). Set a timer for two minutes and tell it out loud, to a wall or a patient friend, using the shape in [[ch07.fig.story]]. Record yourself if you can bear it.

Then check: How long was the context? How many times did you say "we" when you meant "I"? Did you name a result? Where did the timer go off?

::: answer
Almost everyone's first attempt has the same three faults: the context takes a minute, the action is mostly "we", and the result is either missing or vague ("it went well"). That is not a flaw in you; it is how people tell stories to friends, who already know the background and do not need to score anything.

Fix the context first, because it gives you time back. Then go through the action and mark each sentence "I" or "we" honestly. Then find the checkable result: a time, a count, a consequence, a quote from someone. A second attempt is usually much better than the first, and the third is better still. That is why the exercise says out loud: reading a story silently feels fluent in a way that saying it does not.
:::
::::

## Presenting, not pretending {#ch07.sec.presenting}

There is an uncomfortable finding hiding in the interview research. Interviews do not only respond to what you did; they respond to how you present it.

In a meta-analysis of impression management in *structured* interviews, candidates' self-promotion (describing their accomplishments and qualities favourably) correlated .26 with interviewers' ratings across 13 studies [@levashina2014]. A wider meta-analysis found that appearance, impression management and verbal and nonverbal behaviour all shape interview ratings, and warned that "what you see in the interview may not be what you get on the job", especially in unstructured interviews [@barrick2009]. Structure reduces the effect. It does not remove it [@levashina2014].

For someone like Bea, who dislikes talking about herself, that sounds like bad news. It is better news than it looks. The effect means that **clearly stating true accomplishments is rewarded**. The interviewer cannot score what you do not say. The line that matters is not between modest and confident; it is between presenting and pretending.

::: chairs {left="The Understatement" right="The Overstatement"}
@left: I say "I helped a bit with the billing engine." It's polite, and nobody can call me a show-off.

@right: I say "I architected the company's revenue platform." Big words, big impression.

@left: And when they ask what you actually did?

@right: I talk faster. When they ask what *you* did, they write down "helped a bit".

@left: That's not fair. I rewrote the whole thing in a fortnight.

@right: Then why didn't you say so?

@left: Because it sounds like you.

@right: It doesn't. I'd have said "revenue platform". You'd have said "I rewrote the billing engine in two weeks and it's run without an incident since". One of those is checkable. Guess which one they trust.
:::

Both chairs score. Understatement is a real cost in the snapshot game, because the scoring sheet cannot reward work it never hears about. Overstatement buys a good first minute and then collapses under follow-up questions, and if it survives the interview, you will meet it again in [[ch11]], when you have to deliver what the trailer promised. The answer is the one [[ch01.sec.signals]] gave: **translate, don't fabricate**. Say exactly what you did, as specifically as you can, and let the specificity do the persuading [!view].

Presenting well raises a handful of practical questions that people rarely ask out loud.

::: ask
Q: Is it all right to say "I don't know"?

A: Yes, followed by how you would find out, or what you would guess and why. A confident wrong answer is worse than an honest "I don't know, but here's how I'd approach it", and on a structured scoring sheet, the reasoning is usually what gets scored [!view].

Q: Can I bring notes into the room?

A: A notebook with your questions for them is normal everywhere. Reading your answers from notes in a face-to-face interview looks less natural; a few prompt words are fine. On the phone, nobody can see your notes at all [!craft].

Q: What if the interviewer clearly has no structure and just chats?

A: Bring the structure yourself. Answer their questions with stories anyway, and use the conversation to make sure your three strongest pieces of evidence come up before the end. You are helping them do a better job, which they will not notice and will appreciate.

Q: Should I follow up after the interview?

A: A short thank-you note that mentions something specific is courteous and costs nothing. We found no good evidence that it changes outcomes, so do it because it is kind, not because it is a tactic.
:::

## First impressions, measured {#ch07.sec.first-impressions}

Popular advice about the opening of an interview is full of precise-sounding numbers: interviewers decide in seven seconds, or ninety, or "before you sit down". What does the evidence say?

Early impressions do matter. In one study, candidates who made a better impression in the rapport-building chat at the start of an interview received higher interview ratings (a correlation of .42) and were more likely to get internship offers (.22). Interestingly, judgements about competence carried over to separate interviewers who had not seen the opening, while judgements about liking and similarity did not [@barrick2010]. Another study of 163 mock interviews found that much of the influence of first impressions overlapped with job-related content (part of what comes across early is verbal and social skill that the job really needs) and that the opening coloured how early answers were scored more than later ones [@swider2016].

What the evidence does *not* show is a fixed moment when the decision is made. The famous "thin slices" research, in which strangers watched silent video clips of under 30 seconds and predicted end-of-term ratings surprisingly well, was about university teachers, not job candidates [@ambady1993]. It is a fascinating result. It is not evidence that your interview is over before you sit down.

::: myth {#ch07.myth.seven-seconds verdict=partly grade=strong} "Interviewers decide in the first seven seconds"
The precise timing is folklore; the underlying effect is real but smaller and more reasonable. Impressions formed in the opening rapport-building correlate with later ratings and offers [@barrick2010], and they colour how early answers are scored [@swider2016]. But no study shows that a decision is fixed at a particular second, and the best-known "thin slices" study was about teachers' classroom ratings, not interviews [@ambady1993]. Arrive on time, be warm, and have a crisp answer to "tell me about yourself". Then relax: the rest of the interview counts.
:::

Two more pieces of interview folklore are worth clearing up while we are here.

::: myth {#ch07.myth.nonverbal verdict=busted grade=strong} "93% of communication is non-verbal"
False as a general rule, and its own author says so. The 7–38–55 split comes from Albert Mehrabian's experiments on how people communicate feelings and attitudes, such as liking or disliking, through single words and tone of voice. His own site states that "unless a communicator is talking about their feelings or attitudes, these equations are not applicable" [@mehrabian-site]. The original studies were small laboratory tasks [@bigthink-mehrabian]. In an interview, the words carry the evidence. Tone and posture matter, but they do not outweigh what you say by twelve to one.
:::

The second is a pre-interview ritual you may have seen recommended.

::: myth {#ch07.myth.power-pose verdict=busted grade=strong} "Power-pose for two minutes before your interview"
The hormonal and behavioural claims do not hold up. The first author of the original 2010 study later wrote: "I do not believe that 'power pose' effects are real" [@carney2016]. A 2022 meta-analysis of 88 studies found effects on how powerful people *said* they felt, but no reliable effects on physiological measures, and behavioural effects that were probably inflated by publication bias [@forrt-powerposing]. If standing tall makes you feel better, do it; it costs nothing. Just do not expect it to change your hormones or your score.
:::

And the handshake? In a study of 98 students in mock interviews, the quality of a candidate's handshake, scored by trained raters, was associated with interviewers' hiring recommendations, and handshake quality was linked to extraversion [@stewart2008]. So the old advice holds up, a little: a reasonable handshake, where handshakes are the custom, is one more small part of a good opening. It was a small student sample, and the effect is not a reason to practise on your friends.

## Nerves, to scale {#ch07.sec.nerves}

If you are someone who gets nervous in interviews, you have probably been told that interviewers can smell fear, that nerves sink candidates, that you must "seem confident". Here is the actual size of the problem.

A meta-analysis of 30 studies found that candidates who reported more interview anxiety received lower ratings from interviewers, with an average correlation of **−.19** [@powell2018]. That is a real effect: nerves cost something. But square the correlation to see how much of the variation in ratings goes along with anxiety, and you get about **4%**.

::: figure {#ch07.fig.nerves src="ch07/nerves.svg" size=small}
Alt: Headed "about 4 in 100 of the differences in interview ratings go along with nerves", a grid of 100 small squares, ten by ten, with four filled in coral. Below, the other ninety-six, left pale, are labelled "the other 96: what you say, what you've done, the questions, the interviewer, the day". A note at the bottom reads "illustration: −.19 squared ≈ .04 (a meta-analysis of 30 studies)".

Nerves, to scale. Across 30 studies, anxiety went along with about 4% of the differences in interview ratings. That is worth managing, and nowhere near a verdict.
:::

Two cautions keep that picture honest. A correlation is an average across many people and settings, and for some individuals nerves matter much more than for others; Bea is probably one of them. And a correlation cannot say which way the link runs: some people who are less prepared, or less suited to the job, may be more nervous for good reason [!view]. Either way, the headline is the same: **being nervous does not mean you have blown it.**

::: myth {#ch07.myth.nerves verdict=partly grade=strong} "If you're nervous, you've blown it"
Overstated. Across 30 studies, more anxious candidates did receive somewhat lower ratings, but the correlation was −.19 [@powell2018]: anxiety went along with about 4% of the differences in ratings. The other 96% is everything else: what you say, what you have done, the questions and the interviewer.
:::

What helps? The research on interview anxiety does not hand out a tested cure, so what follows is craft [!craft]. Prepare the content so thoroughly that nerves have less to work with: stories you have told out loud, not just written down. Practise under conditions as close to the real thing as you can manage, with someone watching, because being watched is the part that is hard ([[ch08]] has evidence on exactly this). It is fine to say "Give me a moment to think" or even "I'm a bit nervous; I'll start again". Interviewers are people, and most of them remember being on the other side.

::: scene {slug="INT. BEA'S FLAT — FRIDAY, 4:30 PM"}
Bea has a phone screen with a payments company. Her last four went badly, so this time she has done something she has never done before: she has stuck her story bank to the wall above her desk, twelve index cards, one per story, each with three bullet points and a number circled in red.

@bea: It's a phone call. They can't see the wall.

The recruiter asks her to describe a project she is proud of. Bea looks at the card that says BILLING ENGINE — 2 WEEKS — ZERO INCIDENTS SINCE, takes a breath, and tells it, in about ninety seconds, saying "I" every time she means it. The recruiter asks a follow-up. Bea knows the answer, because it is the second bullet point.

Afterwards, she texts Dev.

@bea: They want me for the next round. I read off the wall like a newsreader.

@dev: That's not reading, that's preparation. And next time the cards will be in your head.

@bea: Next time they'll be laminated.
:::

Bea has found the one advantage of a phone screen: nobody can see your notes. Use it [!craft]. Have your story bank, the job ad, your questions for them and a glass of water in front of you. Stand up if it helps your voice. And smile, because it is audible.

## Phone, video and panels {#ch07.sec.formats}

Many first interviews now happen over the phone or video, and the evidence on these formats is thin but worth knowing. A meta-analysis of 12 studies found that interviewers gave lower ratings in technology-mediated interviews than face to face (an effect size of d = −.41), and applicants liked them less too [@blacksmith2016]. The authors warned that interviewing some candidates by video and others in person could be unfair, and called for more research, because much of what we know about interviews comes from face-to-face settings [@blacksmith2016]. Most of those studies predate the years in which video interviewing became routine, so the gap may have changed.

What that means for you: on video, you are working against a slight headwind that has nothing to do with you. Remove what you can of it [!craft]. Test the link and the microphone beforehand. Put the camera at eye level and a light in front of you rather than behind. Look at the camera when you make a key point, and at the faces when you listen. Keep your story notes just below the camera, where glancing at them looks like thinking.

Panels add a different challenge: several people, each with their own sheet. Answer the person who asked, then include the others with your eyes as you go. If two panellists ask conflicting things, say so lightly and answer both [!craft]. And if you are interviewing across cultures, you face a related question: how formal and how direct to be with people you have just met. [[ch14.sec.culture|Chapter 14]] treats that as a dial to set, at work as much as in interviews.

## "Culture fit" {#ch07.sec.fit}

Sooner or later you will be told that a role went to someone who was a better "culture fit". It is worth knowing what that phrase can mean in practice.

In one of the most detailed studies of hiring, a sociologist interviewed 120 people who made hiring decisions at elite US investment banks, law firms and consultancies, and observed their processes. Employers looked for candidates who were culturally similar to themselves in leisure pursuits, experiences and self-presentation, and this shared culture often outweighed concerns about how productive candidates would be [@rivera2012]. That was one elite sector, studied qualitatively, but the mechanism is the one Meera described: unstructured judgement drifts towards "like me".

There are two lessons, one for each side of the table. As a candidate, genuine common ground helps and pretending to share it does not, because the film will contradict the trailer quickly. As an interviewer, which you will be one day, ask what "fit" actually means in behaviours ("we argue openly about designs", "we write things down") and score those, instead of asking whether you would enjoy a drink with the candidate [!view]. The same choice turns up inside companies: promotion panels weigh evidence against rubrics too, as [[ch19]] shows, and the same risk of "like me" applies [!view].

## Questions they shouldn't ask {#ch07.sec.law}

Most interviewers ask lawful, job-related questions. Some do not, often through carelessness rather than malice. It helps to know where the lines are in your region.

::: field {regions="US, UK"} What an employer may ask before an offer
**United States.** The federal Equal Employment Opportunity Commission says that pre-employment questions should be limited to what is needed to judge whether someone is qualified, and that race, sex, national origin, age and religion are irrelevant to that. Questions about disability before a job offer are explicitly prohibited. Most other questions about protected characteristics are not banned outright by federal law, but asking them can be used as evidence of an intent to discriminate. The EEOC also advises employers not to ask for a photograph before an offer [@eeoc-prohibited]. States add their own rules.

**United Kingdom.** "It is generally unlawful under the Equality Act 2010 ... for an employer to ask a job applicant about their health or disability ... during the initial stages of a recruitment process, except in a few specific circumstances" [@ukparl2020-health]. An offer can be made conditional on health checks. We verified only this health rule for the UK.

**EU and India.** We did not verify general rules on interview questions for the EU or for private employers in India, so we have not summarised them. If a question feels wrong, check your local equality body or labour ministry.
:::

If you are asked something you should not be, you have choices, and none of them is perfect [!craft]. You can answer, if you do not mind. You can redirect to the job: "Is there a requirement of the role you're concerned about? I'm happy to talk about that." Or you can decline politely. Whichever you choose, write down what was asked, by whom, and when, while it is fresh. And notice what it tells you about the place.

:::: move {#ch07.move.unlawful} Spot the question
Using the Field Note, sort these questions into **fine** (job-related), **problem in the US**, **problem in the UK**, or **both**. Some may be fine in one place and not the other.

1. "Do you have any health conditions we should know about?"
2. "Tell me about a time you disagreed with your manager."
3. "How old are you?"
4. "Our team is on call one week in six. Would that work for you?"
5. "Where are your parents from?"
6. "Have you ever taken time off work for stress?"
7. "Are you planning to start a family in the next few years?"

::: answer
1. **Both.** Pre-offer disability questions are explicitly prohibited in the US [@eeoc-prohibited], and health and disability questions are generally unlawful in the early stages of recruitment in the UK, with a few exceptions [@ukparl2020-health].
2. **Fine.** A classic past-behaviour question. Have a story ready.
3. **A problem in the US**: age is irrelevant to qualification and asking can be evidence of discrimination [@eeoc-prohibited]. We did not verify the UK rule for age questions, so this book cannot tell you.
4. **Fine.** It describes a real requirement of the job and asks whether you can meet it. That is exactly the kind of question the law expects.
5. **A problem in the US**: national origin is irrelevant to qualification [@eeoc-prohibited]. UK: not verified here.
6. **Both**, for the same reason as question 1: it is a health question.
7. **A problem in the US**, as a question about sex [@eeoc-prohibited]. UK: not verified here. Everywhere: a red flag about the people asking.

Notice the pattern: lawful questions are about the job's requirements; problem questions are about who you are. When in doubt, that distinction is a good guide to how to redirect.
:::
::::

## Interview them back {#ch07.sec.ask-them}

At the end of most interviews comes "Do you have any questions for us?" Many people treat it as a final test to be passed with a clever question. Treat it instead as the one part of the interview that is for you. You are about to spend years in this film. This is your only chance to watch a few frames before you sign.

No study has shown that asking good questions changes whether you get an offer, so this section is craft [!craft]. But a few kinds of question reliably tell you things the job ad will not:

- **The work.** "What would I be working on in the first three months?" "What does doing this job well look like after six months?"
- **The team.** "How do disagreements about technical decisions get settled?" "Who would I work with most closely?"
- **The manager.** "How do you prefer to hear bad news?" "How do you give feedback?"
- **The risk.** "Why is this role open?" "What's the hardest part of this job that the ad doesn't mention?"

And listen for red flags [!view]: nobody can describe what the role is for; interviewers who contradict each other about the job; open contempt for the person who had the role before; pressure to decide on the spot ([[ch09]] has evidence on exploding offers); or questions from the Field Note above. One red flag may be a bad day. Several are a pattern, and you are about to be inside it.

::: scene {slug="INT. LANTERNFISH, “THE DEPOT” — THURSDAY, 10:52 AM"}
@tomas: We've got eight minutes. What would you like to ask us?

Dev opens her notebook to a page headed *Questions for them*, which is also, as of last night, a new tab in her spreadsheet.

@dev: What would a new backend developer have done after three months, if it had gone really well?

Tomás answers properly: one service owned end to end, two on-call weeks survived, one thing made measurably faster. The engineers add details. Dev writes them down.

@dev: And how do you prefer to hear bad news?

@tomas: Early. Any day except Friday afternoon. Friday afternoon bad news is the worst kind of bad news.

Everyone laughs, including Tomás, but Dev underlines it twice.
:::

Dev's two questions did two jobs. They told her what success would look like, which she will need in [[ch11.sec.promises|Chapter 11]] when she has to keep the trailer's promises. And they told her something real about the man who might be her manager. File that Friday-afternoon remark; it comes back in [[ch12.sec.early|Chapter 12]].

:::: move {#ch07.move.questions} Five questions for them
Think of a role you want, or one you are interviewing for. Write five questions you would genuinely want answered before accepting it: at least one each about the work, the team, the manager and the risks. Then, for each, write what answer would worry you.

::: answer
Good questions share two features: they cannot be answered from the website, and you actually care about the answer. "What's the culture like?" fails both; everyone says "collaborative". "Tell me about the last time the team disagreed about a technical decision. How did it end?" passes, because it asks for a story, and stories are harder to polish than adjectives.

The second half of the exercise matters more than the first. Deciding *in advance* what a worrying answer sounds like protects you from the very human tendency to hear what you want to hear when you want the job. If you can't name a worrying answer, the question probably isn't telling you anything.
:::
::::

Dev leaves the Depot with a good feeling and the knowledge that good feelings after interviews are not reliable data. Two days later, Lanternfish emails: they would like to see some of her work. A take-home task, due in a week. It is time to stop telling and start showing.

::: rewind
- An interview is a **measurement**, and structure makes it a better one: structured interviews predict job performance at about .42, unstructured ones at about .19.
- **The scoring sheet is listening for evidence**: a clear problem, your action, a checkable result. Prepare stories, not adjectives.
- Past-behaviour questions ("tell me about a time...") predict slightly better than hypotheticals. A good story answer starts in the middle, says "I", spends most of its time on action, lands a result, and stops.
- Self-promotion does raise interview ratings. The line that matters is **presenting versus pretending**: say exactly what you did, as specifically as you can.
- First impressions count but are not final; "seven seconds", "93% non-verbal" and power posing are folklore. A reasonable handshake helps a little.
- Nerves go along with about **4%** of the differences in ratings across 30 studies. Prepare out loud, practise being watched, and do not treat nerves as a verdict.
- "Culture fit" without structure drifts towards "like me". Know which questions an employer may ask in your region, and use the end of the interview to **interview them back**.
:::

::: further {ref=more.sec.personality}
Some employers add personality questionnaires to interviews. This chapter did not cover them; the appendix explains what the science of personality testing does and does not support, and where to read it.
:::
