---
id: ch13
status: final
---

::: scene {slug="INT. LANTERNFISH, BACKEND TEAM AREA — MONTH 6, TUESDAY, 10:12 AM"}
Dev has been thinking about the routing service's retry logic for a week, and this morning she writes it all down. She posts it in the team channel. It begins:

> *Hi all! So, a bit of background first. As some of you know, when we added Northwind back in month four, we discovered that their API sometimes returns an empty 200, which our retry logic treats as success, and this got me thinking about the wider question of how we handle partial failures across all the carrier integrations, because looking back through the incident log...*

It goes on for four hundred and eleven words. It contains a history of the retry logic, three options, a table, two caveats, a link to a blog post and, in the very last line, the actual question: *So, is everyone OK if I deploy option B on Thursday? It needs about 30 minutes of downtime on the staging environment.*

By the end of the day, the message has collected one reaction, an emoji of a pair of eyes, from someone on the platform team. Nobody has answered the question.

Kai, who is not on the backend team but reads its channel for entertainment, sends Dev a private message.

@kai: loved your essay 😅🙏 what's the ask??

@dev: It's in the last line.

@kai: oh no. nobody has ever reached the last line of anything 🫠

Dev scrolls back up through her four hundred and eleven words. Somewhere around word ninety, she can see the exact point where she would have stopped reading too.
:::

This is the opposite of Corporate Dev's problem in [[ch11]]. Corporate Dev said too little; this Dev says everything. Both versions have the same root: writing for yourself, not for the reader. The four-hundred-word message is the record of Dev's thinking, in the order she thought it. That is a perfectly good order for thinking. It is a terrible order for being read.

Most of the long game is played in words. Messages, documents, meetings, code reviews, one-to-ones, feedback: it is in these, far more than in any single dramatic moment, that colleagues form their picture of you and decide how much to trust it. This chapter is about the craft of talking and writing at work: putting the point first, the surprising ways tone gets lost, what emoji and thanks actually do, when to meet and when not to, how to disagree without damage, and feedback in both directions, including upward.

::: pause
Before reading on: think of the last message you sent at work that got no reply, or a reply that missed the point. Where in the message was the thing you actually needed from the reader: first line, middle, or end? Hold that answer.
:::

## Point first {#ch13.sec.point-first}

Everyone at work is reading on the way to something else. They are skimming the channel between meetings, glancing at email on a phone, scanning a document for the part that concerns them. Any message has to survive that kind of reading, and most don't.

There is some striking evidence about how readers behave, from an unusual place. Across more than 30,000 field experiments with *The Washington Post* and the website Upworthy, readers chose simpler headlines, with more common words and more readable writing, over more complex ones; a follow-up experiment found that readers paid more attention to simpler headlines and processed them more deeply [@shulman2024]. The twist: a sample of professional writers, including journalists, did not show that preference. The people writing the words read differently from the people they were writing for [@shulman2024]. These are news headlines, not workplace messages, so treat this as an analogy. But it describes Dev's message exactly. To her, every one of the four hundred and eleven words was necessary. To her readers, they were a wall.

The fix is old and simple, and practitioners have many names for it [!craft]: **put the point first.** Say what you need, or what you have concluded, in the first line. Then give the reason. Then the details, for anyone who wants them.

::: figure {#ch13.fig.point-first src="ch13/point-first.svg"}
Alt: Two message shapes side by side. On the left, "Story order": six beige blocks stacked from the top, labelled "background", "how we got here", "what I tried", "more context", "three options" and "caveats", with a strong coral block at the bottom, "the ask", and an arrow pointing to it with the note "most readers stop before here". On the right, "Point first": a strong teal block at the top, "the ask", then two lighter teal blocks, "why, in one line" and "what you need from them", then a dashed block, "details, if wanted", with the note "a reader who stops after one line still knows what to do".

The shape of a good message. Story order is how you think; point first is how people read. The content can be identical. Only the order changes.
:::

Here is Dev's message, rewritten:

> *Can I deploy the retry fix (option B) to staging on Thursday? It needs ~30 min of staging downtime, 2–2:30 pm.*
>
> *Why: we treat Northwind's empty 200s as success, and I think other carriers do the same. Details and the other options are in the doc, for anyone who wants them.*

Two short paragraphs. Everything else moved into a linked document, where it belongs and where the two people who care about retry logic can read it at leisure. The rewrite got three answers within the hour.

Notice what point-first is *not*. It is not brevity for its own sake. Rex's code reviews at Corvid, as [[ch01]] noted, were three words long, and nobody could act on them either. "Looks fine 👍" is short; it is not clear. The goal is not fewer words. It is the right first words.

Try it on someone else's message first; it is always easier to see the buried point in another person's writing.

:::: move {#ch13.move.rewrite} Rewrite a message
Rewrite this message so that a reader who stops after the first line knows what to do.

> *Hey team, hope everyone had a good weekend! So I was looking at the dashboard on Friday and I noticed that the error rate on the payments service has been creeping up since the deploy on Wednesday, it's not huge but it's about double what it normally is, I had a quick look at the logs and I think it might be related to the timeout change Sam made, but I'm not 100% sure, it could also be the traffic spike from the promotion. Anyway I wasn't sure who owns this now since the reorg, so I thought I'd flag it here in case anyone knows. Could someone take a look? Thanks!*

::: answer
One good version:

> *Who owns payments-service errors since the reorg? Error rate has been ~2× normal since Wednesday's deploy.*
>
> *Likely causes: Sam's timeout change or the promo traffic spike; I haven't confirmed which. Logs and dashboard link in thread. I can dig in tomorrow if nobody owns it.*

What changed:

- **The first line is the ask**, phrased as a question someone can answer. The original's real question ("who owns this?") was buried in the middle, and its request ("could someone take a look?") was addressed to nobody.
- **The key fact comes second**: "~2× since Wednesday" is the evidence that makes it urgent enough to read.
- **Uncertainty is kept, but compressed.** Honest hedging ("haven't confirmed which") belongs in the message; meandering doesn't.
- **There is an offer**, which makes the message a commitment, not just a worry. That is the loop from [[ch12]].
- **The greeting and sign-off went.** In a team channel they add length without adding warmth. In a first email to a stranger, keep them.
:::
::::

If that felt easy, try the same thing on the last long message you sent. It is usually harder, for the reason the headline study suggests: writers read their own words differently.

::: craft
**A few habits for point-first writing.** These come from practice rather than studies, but they are widely shared among people who write a lot for busy readers [!craft]. Make the first line something a reader could act on alone. If you need a decision, ask a question that can be answered with yes, no or a choice. Put deadlines and owners in the message, not just "soon" and "someone". Use one message per topic, so replies don't tangle. And before sending anything long, ask: if they only read the first line, would that be enough?
:::

## Tone doesn't travel {#ch13.sec.tone}

Kai's "loved your essay 😅🙏" was gentle teasing. Dev knew that because she knows Kai. A stranger reading the same words could easily have taken it as sarcasm. Written messages lose tone, and the people who write them consistently fail to notice.

In a set of five experiments, Justin Kruger and colleagues found that people overestimated how well their tone, whether sarcasm, humour or seriousness, would come across in email. The reason was simple: when senders reread their own messages, they "heard" them in the tone they intended, and assumed the reader would too [@kruger2005].

::: figure {#ch13.fig.tone-gap src="ch13/tone-gap.svg"}
Alt: Dev on the left and Kai on the right, with a message box between them reading "Oh great, another meeting." Dev's speech bubble, in gold, says "(said with a grin, obviously joking)", labelled "what you hear when you reread it". Kai's bubble, in coral, says "...is she annoyed with me?", labelled "what they get: their own guess". Under the message box: "what actually travels: the words". A line across the bottom: "Senders overestimate how well tone comes across in writing, because they hear their own voice when they reread it."

The tone gap. Your tone stays in your head; only the words leave. The reader fills the gap with their own guess, often their worst one.
:::

The practical consequences follow directly, though they are our inferences from the research rather than tested rules [!view]:

- **Assume sarcasm will not survive.** If a message only works with a raised eyebrow, it does not work in writing.
- **Say the tone outright when it matters.** "Quick question, no rush." "Not a criticism, just curious." "Good news first." Spelling out the tone feels clumsy to the writer and lands as clarity for the reader.
- **Read it once as the most anxious person who might receive it.** If they could reasonably read it as annoyed, rewrite it.

### The message at 10 pm

Time travels badly too. A message sent late in the evening says something about urgency whether or not the sender meant it to.

In eight pre-registered studies with over 4,000 participants, Laura Giurge and Vanessa Bohns found that people receiving non-urgent work emails after hours overestimated how quickly the sender expected a reply, an "email urgency bias" that added to their stress. A single line from the sender stating when they expected a response reduced it [@giurge2021]. Other research finds that organisational expectations to monitor email after hours are linked to more anxiety, worse health and lower relationship satisfaction, for employees and their partners, independent of how much time people actually spent on email [@becker2021], and to poorer detachment from work and more emotional exhaustion [@belkin2020].

So if you send messages at odd hours, as many people with flexible schedules do, say when you need an answer ("for tomorrow, no need to reply tonight") or schedule the message to arrive in working hours. The one-line note is one of the few communication habits in this chapter with direct experimental support [@giurge2021]. [[ch17]] returns to after-hours work as part of boundaries and burnout.

## Emoji, exclamation marks and the first message {#ch13.sec.emoji}

Kai writes the way Kai talks: warm, fast and generously decorated. 🙏 for thanks, 🫠 for despair, 🎉 for anything that has shipped. Inside Lanternfish, people love it. It makes the backend channel feel less like a terminal.

Then Kai sends a first message to a new client.

> *Hiii! 👋 So excited to be working with you!! Sharing the first designs here 🎨✨ lmk what you think!!*

The client replies, two days later, in a single formal line addressed to Tomás.

There is research on exactly this. In three experiments on work-related first impressions, a smiley emoticon in a message did not make the sender seem warmer, and it made them seem *less* competent, which in turn made recipients share less information; the effect depended on how formal the context was [@glikson2018]. That is about first contact with strangers in formal settings. Casual markers are not always a liability, though: a small descriptive study of exclamation marks in two professional email discussion lists found they rarely signalled excitability and often seemed to mark friendliness [@waseleski2006!].

The rule this suggests is the same one [[ch11]] gave for newcomers, applied to writing [!view]: **match down, not up.** With strangers, senior people and new clients, start one notch more formal and let the other person set the level. Once they send the first emoji, you can send the second. Inside a team where everyone writes like Kai, writing like a bank is the odd thing.

Kai, to their credit, laughs about it, rewrites their client template, and keeps the 🫠 for the team channel. The professionalism dial in [[ch14]] is the general version of this lesson.

## The thank-you you didn't send {#ch13.sec.gratitude}

Some of the most valuable messages at work are also the shortest, and people consistently undervalue them.

In three experiments, Amit Kumar and Nicholas Epley found that people expressing gratitude underestimated how positive the recipients would feel and overestimated how awkward the recipients would find it, and that those misjudgements kept people from expressing thanks they actually felt [@kumar2018]. Separately, experiments by Adam Grant and Francesca Gino found that a brief thank-you made helpers more likely to help again, including helping other people, because it made them feel socially valued; in a university fundraising call centre, a manager's thanks increased the number of calls fundraisers made [@grant2010]. Gino has had other papers retracted, so we lean on this study only alongside Kumar and Epley's, which points the same way.

The cheapest deposit in any trust ledger, in other words, is a specific thank-you: not "thanks!", but "thanks for spotting the certificate step; it saved the next new hire a day". It costs thirty seconds, it is almost always received better than you expect, and it is the opposite of the credit-grabbing [[ch10]] warned about.

## Meeting or message? {#ch13.sec.meetings}

Words at work come in two main containers: written messages and meetings. Choosing the wrong one wastes everyone's time.

Meetings matter more to people's working lives than they might seem. In two surveys, satisfaction with meetings turned out to be a distinct part of job satisfaction, and it predicted overall job satisfaction, more strongly for people who spent a lot of time in meetings [@rogelberg2010]. Bad meetings are not just a waste of an hour; they are a drag on how people feel about their jobs.

One kind of meeting is worth singling out, because it is so popular and the evidence on it is so clear.

::: myth {#ch13.myth.brainstorming verdict=busted grade=strong} Group brainstorming produces more and better ideas
A meta-analysis of brainstorming studies found that groups brainstorming together produce fewer ideas, and no better ones, than the same number of people working alone and then pooling their ideas, and the loss grows with group size [@mullen1991]. The studies were mostly in the laboratory, but the finding is very consistent. If you want ideas, have people write them down alone first, then meet to discuss, combine and choose.
:::

As a rough guide [!craft]:

- **Use a message** for information, status updates, simple yes-or-no decisions, and anything people need to be able to find again later.
- **Use a meeting** for genuine disagreement, decisions with several moving parts, anything emotionally loaded (bad news, feedback, conflict), and building relationships.
- **Use a document, then a meeting** for complex proposals: people read first, alone, then meet to discuss. That is the brainstorming finding applied to decisions.

And in any meeting you are in, be useful: know why you are there, say the one thing you came to say, and write down what was decided and who will do what. The person who sends the two-line summary afterwards is, in a small way, doing the commitment loop from [[ch12]] on everyone's behalf.

:::: move {#ch13.move.meeting-or-message} Meeting or message?
For each situation, decide: **message**, **meeting**, or **document then meeting**. Commit first.

1. You need to tell your team that the release has moved from Tuesday to Thursday.
2. Two senior engineers disagree about whether to split a service, and both have strong views.
3. You want to give a colleague feedback that their code reviews come across as harsh.
4. You need your manager to approve one day of leave next month.
5. You want to propose changing how the team runs its on-call rota.
6. The team needs ideas for reducing the number of support tickets.

::: answer
1. **Message.** Pure information, which people will want to find again. Lead with the new date.
2. **Document then meeting.** Ask each person to write their case down (a page, not a novel), share both, then meet to decide. Writing first separates the argument from the volume, and the meeting can focus on the real disagreement.
3. **Meeting**, one to one, in private. Feedback about how someone comes across is easy to misread in writing, as the tone research suggests [@kruger2005]. More on how in [[ch13.sec.feedback]].
4. **Message.** A meeting for a one-day leave request wastes two people's time.
5. **Document then meeting.** It affects everyone, people will have different constraints, and a written proposal lets them think before reacting.
6. **Alone first, then a meeting.** Ask everyone to write five ideas on their own, then meet to combine and choose. That is what the brainstorming evidence supports [@mullen1991].
:::
::::

## Disagreeing without damage {#ch13.sec.disagree}

Sooner or later, you will think a colleague, or your manager, is wrong, and you will have to decide whether and how to say so.

The research gives a sobering starting point. In a field study and two experiments, Ethan Burris found that managers rated employees who voiced *challenging* ideas (pointing out what was wrong with how things were done) as worse performers, and endorsed their ideas less, than employees who voiced *supportive* ideas, largely because challenging voice was seen as less loyal and more threatening [@burris2012]. A broader review of research on employee voice and silence describes why so many people with good concerns keep quiet [@morrison2014].

That is not an argument for staying silent. It is an argument for raising challenges in a way that reads as loyalty rather than threat. Burris's own explanation points at how. If managers react to challenges because they feel disloyal or threatening, then the challenge that works is the one that is clearly on the team's side. Here is a way to do that, inferred from that finding rather than tested as a script [!view]:

- **Start from the shared goal.** "I want Thursday's launch to go well, and I'm worried about one thing" lands very differently from "This plan won't work."
- **Raise it privately first** if it is about someone's decision, so they do not have to defend it in public.
- **Separate the idea from the person.** "The retry logic treats empty responses as success" is about the work. "You didn't think about empty responses" is about them.
- **Bring an option**, even a rough one. A problem with a proposed fix is a contribution; a problem alone can feel like an attack.
- **Then let it go**, if the decision goes the other way and nothing is unsafe or unethical. You said it; that was your job.

Keeping disagreement about the work, and away from the person, is the core skill. A meta-analysis of team conflict found that conflict about the task has no reliable overall harm, and can help when relationships stay good, while conflict that becomes personal is reliably damaging [@dewit2012]; [[ch16]] looks at that evidence and at what to do when disagreement turns into something worse.

And when a disagreement leaves you furious, there is one popular piece of advice to ignore.

::: myth {#ch13.myth.venting verdict=busted grade=moderate} Venting your anger gets it out of your system
In a laboratory experiment, angered people who vented by hitting a punching bag while thinking about the person who had provoked them became *more* angry and aggressive afterwards, not less. People who simply did nothing for a while did better [@bushman2002]. This was a lab study with student participants, so it says more about the next half-hour than about long workplace grudges. Ranting about a colleague, in the kitchen or in a private chat, is more likely to rehearse your anger than release it. Cooling off, or doing something that takes your mind off it, works better.
:::

## Feedback: why a third of it backfires {#ch13.sec.feedback}

Feedback is where talking at work gets hardest, and where the most confident advice turns out to be the least tested.

Start with the most important finding in this area, which most people who give feedback have never heard of.

::: receipts {source=kluger1996} The feedback paradox
**What they did.** Avraham Kluger and Angelo DeNisi pooled 607 effect sizes, from studies with over 23,000 observations, on what happens to performance when people receive feedback [@kluger1996].

**What they found.** On average, feedback improved performance, by a moderate amount (d = .41). But more than a third of the feedback interventions made performance *worse*. Feedback helped less the more it drew people's attention away from the task and towards themselves.

**What it cannot tell you.** It is a review of many different kinds of feedback, in many settings, so it does not give a recipe. And "attention to the self" is the authors' explanation, built into their own theory; it is consistent with their data, but it is an interpretation, not a direct measurement.
:::

Read that again: more than a third. Feedback is not a guaranteed good, like vitamins. It is a powerful intervention that can easily go wrong, and the best clue to *how* it goes wrong is where it points.

::: figure {#ch13.fig.feedback src="ch13/feedback.svg"}
Alt: Two parts. At the top, under "Feedback interventions, on average", a horizontal bar split into a larger teal segment labelled "the rest" and a coral segment labelled "made it worse", with the notes "more than a third of interventions" and "segment sizes approximate". Below, under "Where the feedback points", a double-headed arrow: teal to the left, "at the task", and coral to the right, "at the self". Under the teal end, a box quoting "The decision is in paragraph six. Put it in the first line." labelled "tends to help". Under the coral end, a box quoting "You're not a very clear writer, are you?" labelled "tends to backfire".

Feedback that helps versus feedback that hurts. The same observation, aimed at the work or at the person, has very different effects. The bar's proportions are drawn approximately; the study reports "more than a third".
:::

Feedback aimed at the **task**, what to change and how, keeps attention on the work. Feedback aimed at the **self**, who you are or what kind of person you are, pulls attention to self-protection, which is the review's best explanation for why so much feedback goes wrong [@kluger1996]. "The decision is in paragraph six" is task feedback. "You're a rambling writer" is self feedback, even if it is accurate, and it is much less likely to change anything.

That brings us to the most popular feedback technique in the world.

::: myth {#ch13.myth.sandwich verdict=busted grade=weak} The feedback sandwich (praise, criticism, praise) is the best way to give feedback
In a study of written peer feedback among medical students, students *believed* that "feedback sandwiches" improved their performance, but there was no evidence that it did [@parkes2013]. That is one study in a narrow setting, so it is not proof that the sandwich always fails. But we found no good evidence that it works, and the Kluger and DeNisi review gives a reason to worry about it: wrapping criticism in general praise can shift attention to how the person is doing, rather than what to change [@kluger1996]. Specific praise for specific things is worth giving on its own merits. It does not need to be used as bread.
:::

What about the popular frameworks? Kim Scott's *Radical Candor*, built on "care personally and challenge directly", is widely used in technology companies; it contrasts candour with "ruinous empathy" (caring but not challenging) and "obnoxious aggression" (challenging but not caring) [@scott2017!]. It is a practitioner model sold through workshops, and we found no peer-reviewed test of it. Its core advice, to be specific, keep feedback about the work and make it clear you are on the person's side, is consistent with the Kluger and DeNisi findings. Its memorable two-by-two grid is a teaching device, not a validated model.

Here is a structure that follows the evidence: specific, about the task, about behaviour you saw and its effect, with a clear request [!craft].

1. **Ask first, and choose the setting.** "Have you got ten minutes? I'd like to give you some feedback on the design doc." Private, unless it is praise.
2. **Describe what you saw**, specifically. "In the doc, the recommendation is in the last section."
3. **Say what effect it had.** "Two people in the review hadn't got that far, so we spent the meeting on background."
4. **Make a request**, not a verdict. "Next time, could you put the recommendation in the first paragraph?"
5. **Then listen.** They may know something you don't.

::: scene {slug="INT. LANTERNFISH, SMALL MEETING ROOM — MONTH 6, THURSDAY, 3 PM"}
It is their weekly one-to-one. Tomás waits until Dev has finished her agenda, then turns a page in his notebook.

@tomas: Can I give you some feedback? It's not small, but it's fixable.

@dev: ...Go on.

@tomas: The routing design review last week. You had a real objection to the caching approach: that it would serve stale rates during carrier outages. It was a good objection. It was also in paragraph six of your comment, after a lot of background. By the time anyone got there, the decision had been made. Two people told me afterwards they'd have changed their vote if they'd seen it.

Dev feels her face go hot.

@tomas: This isn't about you being unclear. You're one of the clearest thinkers on the team. It's about where you put the important thing. Lead with the objection, in one line. Then the reasoning. Would that work for you?

@dev: Yes. That's... fair. Kai said something similar about my chat messages.

@tomas: Kai is usually right about words. Wrong about fonts, but right about words.

He waits. Dev realises he is waiting for her to say something else, and that she has something else to say.

@dev: Can I give you some feedback too?

@tomas: Please.

@dev: You send messages at ten or eleven at night. Priority changes, questions. I know you're not expecting a reply. But for the first two months, I didn't know that, and I answered every one, from bed. I think the newer people still do.

Tomás is quiet for a moment.

@tomas: I had no idea. I write things down when I think of them, so I don't forget.

@dev: You could schedule them for the morning. Or just say "for tomorrow".

@tomas: I'll do both. Thank you. That's genuinely useful.

He writes it in the notebook, under his own name.
:::

## Hearing it, asking for it, and giving it upward {#ch13.sec.receiving}

Tomás gave feedback in exactly the shape the evidence supports. He asked first. He described something specific (the objection in paragraph six) and its effect (a decision made without it). He made it explicitly about the behaviour, not the person, with "this isn't about you being unclear", which is the task-not-self distinction said out loud. He made a request and checked it would work. And he did it privately, in a meeting, not in writing.

Dev, receiving it, did three things that are worth copying [!craft]. She did not argue or explain. She said what was fair. And she connected it to a pattern she had already heard, which turned one piece of feedback into a lesson rather than a sting. The urge to defend yourself when receiving feedback is strong, and it is exactly the self-focused reaction the Kluger and DeNisi review warns about. A useful default: say "thank you", ask one clarifying question, and decide what you think about it later, once the heat has gone.

You can also make feedback much more likely to happen. Feedback-seeking declines as people's tenure grows, and it rises with a learning orientation and a good relationship with one's manager, though its direct link to performance is small [@anseel2015]. In practice, people rarely volunteer useful feedback to colleagues; you usually have to ask [!view]. And general questions ("any feedback?") get general answers ("all good!"). Specific ones get real answers: "What's one thing I could do to make my design docs easier to review?" You will need every one of these habits in [[ch18]], where feedback arrives once a year, in writing, attached to a rating.

### Giving feedback upward

Dev's feedback to Tomás was the riskier half of that conversation. Burris's research is a reminder that challenging your manager can cost you [@burris2012]. Several features made hers land well [!view]:

- **She chose the moment.** Right after he had given her feedback, in a one-to-one, when the door was already open.
- **She asked permission first.** "Can I give you some feedback too?"
- **She described a specific behaviour and its effect on her**, rather than a judgement ("you don't respect our evenings").
- **She assumed good intent out loud** ("I know you're not expecting a reply"), which made it clearly loyal rather than threatening.
- **She offered a fix**, and a small one.

And it was about something the evidence supports: late-night messages really do raise people's stress about replying, and a one-line note really does help [@giurge2021]. Feedback upward lands best when it is small, specific, kind and clearly in the team's interest. Save the big structural complaints for when you have built a balance in the ledger, and consider [[ch16]] first.

:::: move {#ch13.move.feedback-script} Give feedback with a script
Pick a real piece of feedback you have been meaning to give, to a colleague or to your manager, or use this one: a teammate regularly joins the daily stand-up five to ten minutes late, so updates get repeated.

Write it out using the five steps: ask first, describe what you saw, say the effect, make a request, then listen. Keep it under 70 words before the listening part.

::: answer
For the stand-up example, a strong version:

> *"Have you got a minute? It's about stand-up. The last few weeks you've often joined around ten past. When that happens we end up repeating updates, and it pushes the meeting past the half-hour, which some people have calls after. Would it work for you to be there at the start? Or if the time's the problem, should we move it?"*

Notice what it does: it is specific ("around ten past", "the last few weeks"), it states an effect on other people rather than a judgement ("you're disrespectful"), it makes a request, and it offers a way out that assumes there might be a reason, because there often is (a clash, a school run, a time zone).

Check your own script for the two most common slips: a verdict about the person sneaking in ("you never...", "you're always..."), and a request so vague that nothing could change ("just be more mindful"). Both point the feedback at the self rather than the task, which is where, on the best explanation we have, feedback most often goes wrong [@kluger1996].
:::
::::

A few questions people tend to keep to themselves about all this.

::: ask
Q: Point-first feels rude. Won't people think I'm being curt?

A: In most working relationships, a clear first line reads as respect for the reader's time. If you worry about warmth, add it at the end ("thanks, and no rush") or in the tone, not by burying the point. With strangers and senior people, keep the greeting; just put the point straight after it.

Q: My manager never gives me feedback. What do I do?

A: Ask, and ask specifically: "What's one thing I could do differently in design reviews?" works far better than "any feedback?". If even specific questions get "all good", ask a peer you trust; people seek feedback more where the relationship is good [@anseel2015], and your best relationship for this may not be with your manager.

Q: Isn't feedback to your manager just risky? Why would I ever do it?

A: It can be risky, as Burris's research shows [@burris2012], which is why the size and shape matter. Small, specific, kind and clearly on the team's side is low risk and often appreciated. Large and structural, early in the relationship, is high risk. Build the ledger first.
:::

Dev, as it turned out, got to test all of this within a week.

::: scene {slug="INT. LANTERNFISH, BACKEND TEAM AREA — MONTH 7, MONDAY, 9:40 AM"}
Dev opens the team channel. There is a new message from Tomás, posted at 9:00 am exactly, with a small clock icon beside it that means it was scheduled.

> *For this week: I'd like a decision on the caching approach by Thursday. Dev has a concern about stale rates during outages; her one-line version is in the doc. Please read that first.*

Underneath, Dev has written, point first:

> *Concern: the cache will serve stale rates for up to an hour when a carrier is down. Proposal: cap it at 5 minutes and show "rates may be out of date". Details in the doc.*

It has eleven replies. Kai has reacted with a single 🎯, the most restrained Kai has ever been.

Dev looks at her sticky note. Under the five defaults and *Range, reason, checkpoint*, she adds a third line: *Point first. Then stop.*
:::

Over seven months, the long game has started to feel like her game. Dev has learned that trust is three dials and a ledger, that starting well is clarity, competence and connection, that reliability is mostly telling people early, and that the words you choose, and the order you put them in, decide whether anyone hears you at all. What she has not yet worked out is how much of herself to bring to work: how formal to be, which jokes to make, what to share. That is a setting, not a rule, and [[ch14]] is about how to find it.

::: rewind
- **Write for the reader, not for your thinking.** Story order is how you think; point first is how people read. Put the ask or the conclusion in the first line.
- Point-first is not brevity. **The goal is the right first words**, not fewer words: a three-word review is short and still useless.
- **Tone doesn't travel**: senders overestimate how well it comes across. Assume sarcasm won't survive, and say the tone outright when it matters.
- Late messages create **false urgency**. Say when you need a reply, or schedule the message; that one-line note is experimentally supported.
- **Match down**: with strangers and new clients, skip the smileys until they use one. **Thank people specifically**; it lands better than you expect.
- **Message for information, meeting for disagreement and emotion, document then meeting for complex decisions.** Brainstorm alone first, then together.
- **Disagree about the work, not the person**: start from the shared goal, raise it privately, bring an option. Venting rehearses anger rather than releasing it.
- **More than a third of feedback backfires**, and the best explanation is that it points at the self rather than the task. Be specific, describe behaviour and effect, make a request, and listen; skip the sandwich. Ask for feedback specifically, and give it upward small and kind.
:::
