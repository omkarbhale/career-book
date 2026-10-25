# Three Games, One You

*A field guide to landing the job, being yourself at work, and making the work count.*

Working life is three different games. In the **snapshot game**, strangers judge a short, edited trailer of you: a résumé, a few conversations, an afternoon of interviews. In the **long game**, colleagues watch the whole film, every day, for years. In the **career game**, the film gets reviewed, in cycles, and the review decides what you do next. The skills differ, so this book teaches all three:

- **Part I, The Snapshot Game**: deciding whether to switch, how hiring works from the other side of the table, turning your experience into evidence, résumés and profiles, referrals and weak ties, interviews, work samples, offers, negotiation and leaving well.
- **Part II, The Long Game**: first-principles conduct at work: trust and reputation, starting a new job, reliability, writing and feedback, the professionalism dial, office friendships, conflict and politics, and staying yourself under pressure.
- **Part III, The Career Game**: being good at the work and having it count: performance reviews, promotion cases, choosing what to get good at, the fork between expert and manager, and the career over decades, which loops back to Part I.

The thread through all three is one person. Learn the snapshot game without shame, play the long game without a mask, make the work count honestly, and keep the trailer a true cut of the film. A closing appendix, *Left Out, on Purpose*, says what the book deliberately does not cover and where to go instead.

The book follows Dev, a software tester trying to become a developer, and a small cast through all three games. It is written in a conversational, picture-rich style inspired by learner-centred technical books, and **every factual claim is sourced and graded** (strong, moderate, weak, or myth-or-unsupported), with practitioner advice and the author's opinions labelled as such.

## Read it

**https://omkarbhale.github.io/career-book/**

The site is the `docs/` folder on `main`, so it goes live once GitHub Pages is set to serve that folder (Settings → Pages → Deploy from a branch → `main`, `/docs`). You can also open `docs/index.html` straight from a clone, or build and preview it yourself (below).

Start with *How to Use This Book*; it takes five minutes and suggests shorter routes if you are in a hurry.

## Status

**Complete.** Every page is written, fact-checked and edited:

| Part | Contents |
| --- | --- |
| Front matter | *How to Use This Book* and *Meet the Cast* |
| Part I, The Snapshot Game | Chapters 1 to 9 |
| Part II, The Long Game | Chapters 10 to 17 |
| Part III, The Career Game | Chapters 18 to 22 |
| Back matter | the epilogue, *The Loop*; the appendix *Left Out, on Purpose*; and a generated reference list |

About 145,000 words, including boxes and exercises, with original SVG figures throughout and 460 cited sources, each graded. The evidence bases are `research/part1/` (getting a job, 102 sources), `research/part2/` (conduct at work, 212) and `research/part3/` (the career game, 104), plus sources the writers added in `book/sources/`. The fact-check logs are public in `checks/part1.md`, `checks/part2.md` and `checks/part3.md`. `DESIGN.md` records the design, the cast and the story as written.

Found a mistake, a broken link or a better source? Open an issue. The claim policy in `DESIGN.md` §9 is the standard every change is held to.

## Build it

You need Python 3.11 or newer. There is nothing to install and the build makes no network requests.

```sh
python3 tools/build.py            # build the site into docs/
python3 tools/build.py --check    # run all checks without writing
python3 -m http.server -d docs 8000   # preview at http://localhost:8000/
```

The build fails if any cross-reference, citation key, figure or alt text is missing, if a figure breaks the colour rules, or if placeholder text remains. The same sources always produce the same `docs/`.

## Repository layout

| Path | What it is |
| --- | --- |
| `book/book.toml` | the book's spine: metadata, reading order, chapter summaries, cast |
| `book/front/`, `book/chapters/`, `book/back/` | the text, in Book Markdown (see `WRITING-GUIDE.md`) |
| `book/figures/` | standalone SVG figures; `figure.css` is their shared style; `_src/` holds the scripts that draw them |
| `book/sources/` | sources added by the book's writers (the research registries live in `research/`) |
| `book/theme/` | the site stylesheet and icon |
| `research/` | evidence bases for each part, and the style research note |
| `tools/build.py`, `tools/bookkit/` | the build (Python standard library only) |
| `tools/figkit.py` | optional helpers for drawing figures and the cast |
| `docs/` | the generated site (do not edit by hand) |

## Contributing

Start with `DESIGN.md`, then `WRITING-GUIDE.md`, then read Chapter 1 as the model. Each chapter writer owns their chapter's files, figures and sources, so chapters can be written in parallel without conflicts.

## Licence

The book and its code are released under the MIT License; see [`LICENSE`](LICENSE). Characters and companies in the book are fictional.

## Credits

Written with AI assistance under the direction of the repository's owner, Omkar Bhale, who set the brief and its scope. The research, drafting, figures, fact-checking and editing were done by AI agents working to that brief. Every source the book cites was opened and checked during the work, and the fact-check logs are public in [`checks/`](checks/), so you can see what was verified, what was changed and what was left out.

The style owes a debt to the learner-centred approach Kathy Sierra and Bert Bates brought to technical books, and to Richard Mayer's research on learning from words and pictures. This book is not affiliated with any publisher or series; all of its words and pictures are original.
