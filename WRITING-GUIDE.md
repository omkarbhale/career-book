# Writing guide

How to take an assignment from `DESIGN.md` to a finished chapter that builds, reads well and holds up to a fact-check. Read `DESIGN.md` first (especially §4 for your chapters, §5 for the cast, §6 for voice and §9 for the claim policy), then read Chapter 1 (`book/chapters/ch01-three-games.md`) as the worked example. Imitate it.

## 1. What you own

Parallel writers never edit the same file. For a chapter with id `chNN` you own, and only you edit:

| Path | What it holds |
| --- | --- |
| `book/chapters/chNN-short-name.md` | the chapter (the file name must start with `chNN-`) |
| `book/figures/chNN/*.svg` | its figures |
| `book/figures/_src/chNN_figures.py` | optional: the script that generates them with `tools/figkit.py` |
| `book/sources/chNN.yaml` | sources you add that are not already in a research registry |

The appendix *Left Out, on Purpose* is owned the same way by assignment F: `book/back/left-out.md`, `book/sources/more.yaml` and any figures under `book/figures/more/`.

Every id you create starts with your chapter id (`ch07.sec.star`, `ch07.fig.rubric`, `ch07.move.questions`), so two writers can never create the same id.

You **do not** edit `research/`, other chapters, `tools/`, `book/theme/`, `book/figures/figure.css` or `book/figures/cast/`. Two shared files may need a one-line change: `book/book.toml`, to retitle your own chapter or update its summary (edit only your own lines), and `DESIGN.md`, only to change a story beat or brief, and only in the same pull request as the chapter that needs it. If you need anything else changed, ask the designer or editor.

## 2. From assignment to finished chapter: the checklist

Copy this into your pull request description and tick it off.

- [ ] **Research.** Read your chapter's brief in `DESIGN.md` §4 and every research topic file it lists. Note each finding you will use, its key and its grade, and its caveats.
- [ ] **Verify.** For every number or quote you will print, check that the source's `supports` field states it, or open the source and read it. If you need a source that is not in a registry, open it, read it, and add it to `book/sources/chNN.yaml` (§5). Never cite from memory.
- [ ] **Outline.** Write the section headings (one idea each), and place the scenes, figures, exercises and Myth Checks on the outline. Check against the brief: every key idea, assigned myth and planned figure has a place.
- [ ] **Draft.** Open with a scene. Lead each section with why it matters. Cite as you write.
- [ ] **Figures.** Draw 3 to 5 (§6). Each teaches one idea, has alt text and a caption, and works in both themes and at phone width.
- [ ] **Exercises.** 2 to 4 *Your Move* boxes with answers that explain; 1 or 2 *Pause* questions that the chapter later answers.
- [ ] **Cross-references.** Every **Back** and **Forward** in your brief appears as a `[[...]]` link. Prefer section ids once the target exists.
- [ ] **Going Further.** If DESIGN.md §13 assigns your chapter a pointer, add it after the Rewind.
- [ ] **Part III only.** Revisit every evidence pointer against `research/part3/` once it lands (DESIGN.md §12).
- [ ] **Labels.** Practitioner advice carries `[!craft]` or sits in a Craft Note; opinion carries `[!view]` or sits in an Author's View.
- [ ] **Self-edit.** Read it aloud. Cut every sentence that does not teach, show or move the story. Check the density rule (no more than one box per ~400 words; never two boxes back to back). Check the humour rules (DESIGN.md §6). Check that the chapter still makes sense with every box skipped.
- [ ] **Length.** 4,500 to 6,000 words of prose.
- [ ] **Build passes.** `python3 tools/build.py` exits with `ok:`. Look at your chapter in a browser, in light and dark themes and at phone width (§8).
- [ ] **Status.** Set `status: review` in your front matter when it is ready for the fact-checker; the editor sets `final`.

## 3. Book Markdown: the syntax

Chapters are Markdown with a small set of additions. The build (`tools/bookkit/`) implements exactly this; anything else is an error, not a guess.

### Front matter

```markdown
---
id: ch07
status: draft
---
```

`status` is `draft`, `review` or `final`. The title comes from `book/book.toml`; do not write a `#` heading. Start sections at `##`.

### Ordinary Markdown

Paragraphs; `## Section {#ch07.sec.slug}` headings (give an id to every section you or anyone else might link to); `*emphasis*`, `**strong**`, `` `code` ``; `[link text](https://...)`; bullet and numbered lists (indent nested lists by two or more spaces); `> quotes`; pipe tables; fenced code blocks. Type typographic characters directly or let the build convert: straight quotes become curly quotes, `--` becomes an en dash and `---` an em dash. There are no images: pictures are figures.

### Citations and labels

```markdown
Referred candidates were 6.1% of applicants but 29.1% of hires [@brown2016].
Two sources at once [@sackett2022; @sackett2023-iop]. A page: [@levashina2014, p. 257].
Show the grade inline when the sentence leans on weak evidence [@ladders2018!].
This is practitioner advice [!craft]. This is our argument [!view]. We could not check this [!unverified].
```

Citations number themselves per chapter and link to the chapter's reference list.

### Cross-references

```markdown
[[ch07]]                       → "Chapter 7"
[[ch07:full]]                  → "Chapter 7, “Interviews, Decoded”"
[[ch01.fig.loop]]              → "Figure 1.3"
[[ch01.move.signal]]           → "Your Move 1.1"
[[ch01.sec.signals]]           → "“Signals, not secrets” in Chapter 1"
[[ch01.sec.signals|signals]]   → your own link text
[[more.sec.managing]]          → "“Managing people” in “Left Out, on Purpose”"
```

Links work forward and backward. The build fails on any id that does not exist, so link to chapter ids (`[[ch12]]`) until the chapter you are pointing at exists, then tighten to section ids. The appendix's section ids are declared in `book/book.toml` (`sections = [...]`), so they work before the appendix is written; once it is, the build checks that every declared section exists. Each chapter page automatically lists the chapters that link to it ("Threads into this chapter").

### Ids

Ids look like `<page>.<kind>.<slug>`: `sec` for headings, `fig` for figures, `move` for exercises, `myth` for Myth Checks, `box` for any other box you want to link to. Slugs are lowercase words joined by hyphens. Ids are permanent once published: other chapters link to them.

### Speech

A paragraph that starts `@name:` is a line of dialogue with the speaker's avatar. Speakers are the cast keys in `book/book.toml`: `dev`, `bea`, `rex`, `meera`, `tomas`, `kai`. Inside a Two Chairs box the speakers are `@left:` and `@right:`.

```markdown
@meera: I'm not choosing the best engineer. I'm choosing the best engineer I can *see*.
```

### Elements

Every element is a fenced block, opened with three or more colons, an element name, optional attributes in `{...}`, and an optional title, then closed with a line holding the same number of colons. Elements can contain any Markdown, including other elements.

```markdown
::: scene {slug="INT. LANTERNFISH, KITCHEN — 8:55 AM"}
Old Faithful is making a noise like a dial-up modem.

@kai: Don't touch it. Nobody touches it.
:::

::: pause
Before reading on: who do you think will fix the machine?
:::

:::: move {#ch10.move.defaults} Your five defaults
Write down five things you will do by default, whatever the situation.

::: answer
There is no single right list, but strong ones are behaviours, not traits...
:::
::::

::: ask
Q: Isn't this just being nice?

A: No. Being nice is a mood. Defaults are decisions you make once.
:::

::: chairs {left="The Script" right="The Default"}
@left: I tell you exactly what to say.

@right: I tell you who to be, and let you find the words.
:::

::: trapdoor
**Over-promising in week one.** ...
:::

::: myth {#ch07.myth.seven-seconds verdict=partly grade=strong} Interviewers decide in the first seven seconds
Early impressions do correlate with later ratings [@barrick2010], but ...
:::

::: receipts {source=kluger1996} The feedback paradox
**What they did.** ... **What they found.** ... **What it cannot tell you.** ...
:::

::: field {regions="US, UK, India"} Notice periods
...
:::

::: craft
Practitioner advice, labelled as such.
:::

::: craft {by=author} Why we think defaults beat scripts
Our argument, labelled as opinion.
:::

::: flashback {ref=ch01.sec.loop}
One or two sentences connecting back.
:::

::: coming {ref=ch16}
One or two sentences pointing forward.
:::

::: figure {#ch10.fig.trust src="ch10/trust.svg"}
Alt: A triangle with "ability", "benevolence" and "integrity" at its corners...

What to notice in this figure, in one or two sentences.
:::

::: rewind
- Five to eight bullets.
:::

::: further {ref=more.sec.managing}
One or two sentences: what this chapter left out, and what the appendix section offers.
:::
```

In the appendix only, each recommended resource is a card. Its label (Evidence-based, Theory or Practitioner view) comes from the source's `kind`; its body says what the resource is good for and who it suits:

```markdown
::: resource {source=dunlosky2013}
Good for anyone who studies for a living; readable without a psychology degree.
:::
```

Verdicts are `busted`, `partly` or `holds`; grades are `strong`, `moderate`, `weak` or `myth-or-unsupported`. Figure sizes: add `size=small` for a narrow figure or `size=wide` to let it spread on large screens.

## 4. Writing well in this book

- **Open with a scene** that puts the chapter's problem in front of a character. Use the beats assigned in DESIGN.md §5 and no others.
- **Give a reason to care before the content.** Then the idea, then the evidence, then what to do.
- **One idea per section.** Short sections, plain headings.
- **Say the important things more than once, differently**: in prose, in a figure, in a scene, in an exercise. Never the same sentence twice.
- **Be concrete.** Name the number, the study, the region, the mistake.
- **Be fair.** If the evidence is mixed, say so. If something is unfair, say who it is unfair to and source it. Never tell readers that nothing they do matters, and never pretend that everything is in their control.
- **Keep the cast on model.** Check facts against DESIGN.md §5. Characters can be wrong; the book cannot.

## 5. Adding a source

If the source you need is already in `research/part1/sources.yaml` or `research/part2/sources.yaml`, cite its key; do not copy it. Otherwise, open it, read it and add it to `book/sources/chNN.yaml`:

```yaml
smith2024:
  type: article
  authors: ['Smith, Jane', 'Okoye, Chidi']
  year: 2024
  title: The title as published
  container: Journal Name
  volume: '12'
  issue: '3'
  pages: 45-67
  doi: 10.1234/abcd.5678
  url: https://the-page-you-actually-opened
  url_checked: '2026-10-25'
  url_note: Abstract read on PubMed. (Say exactly what you read.)
  kind: evidence
  design: randomised experiment
  supports: >-
    What the source shows, as the book uses it, with the numbers you print.
  sample: Who and how many.
  grade: moderate
  caveats: Its limits.
```

- **Keys** are lowercase family name plus year, with a suffix if needed (`smith2024`, `smith2024-pay`); organisations use a short name (`bls-tenure2026`). Keys are permanent.
- **Required:** `type`, `authors`, `year`, `title`, `url`, `url_checked`, `grade`, `supports`. Use `doi` whenever one exists. `kind` is one of `evidence`, `review`, `theory`, `data`, `practitioner` or `law`. `flags` may list `commercial`, `self-interested`, `practitioner`, `not-peer-reviewed` or `coauthor-with-retractions`; `retracted` sources cannot be cited.
- The Part I registry's spellings (`venue`, `accessed`, `commercial: true`) are also accepted.
- The same key may exist in two registries only if it is the same work (same DOI, URL or title and year). The build tells you if it is not.
- Grade honestly, by what the source can support *as you use it* (DESIGN.md §9).

## 6. Adding a figure

1. Decide the one idea the figure teaches. Sketch it on paper first.
2. Make `book/figures/chNN/name.svg`, either by hand or with a script in `book/figures/_src/chNN_figures.py` using `tools/figkit.py`, which gives you the cast (`avatar`, `person`), hand-drawn lines and arrows (`Pen`), text helpers and `write_svg` (which adds the canonical style block). Run your script with `python3 book/figures/_src/chNN_figures.py`.
3. Follow DESIGN.md §8: a `viewBox` and `class="fig"` on the root, colours only through `figure.css` classes, meaningful labels at `t` (24) and secondary notes no smaller than `t-sm` (20), no raster images or scripts. If you hand-write a figure, run `python3 tools/build.py --sync-figure-style` to add the style block.
4. Put it in the chapter with a `::: figure` block, with an id, an `Alt:` paragraph that says what the figure shows and means, and a caption that says what to notice.
5. Look at it in both themes and at phone width.

## 7. Building and checking

```sh
python3 tools/build.py            # build docs/; fails on any error
python3 tools/build.py --check    # run every check, write nothing
python3 -m http.server -d docs 8000   # then open http://localhost:8000/
```

Python 3.11 or newer; nothing to install. The build fails, with the file and line, on:

- a cross-reference to an id that does not exist, or an id outside your chapter's namespace, or a duplicate id;
- a citation key that is in no registry, or a retracted or deprecated source;
- a figure without alt text or caption, a missing figure file, or an SVG that breaks the figure rules;
- placeholder text anywhere in the book (TODO, TK, TBD, FIXME, XXX, lorem);
- an unknown element, a missing required attribute, or malformed Markdown it cannot read.

It warns if a chapter has no Rewind. `docs/` is generated: never edit it by hand; rebuild and commit it with your change.

## 8. Before you open a pull request

- `python3 tools/build.py` prints `ok:`.
- You looked at the chapter in a browser in light and dark themes (the theme button cycles Auto, Light, Dark) and at a phone width of about 375 px, with no horizontal scrolling.
- You read every answer box and every Myth Check once more against its sources.
- The PR touches only the files you own (§1), plus `docs/`.
