# Habit cycles are infodesics

Paper 2 of the twists line: the theoretical reading of the habit
structures that `twists-home-vectors` (paper 1) characterises
empirically.  Seeded from `docs/habit-cycles-as-infodesics.md`, which
remains the argument-of-record until the sections outgrow it.

## Thesis

A repeated-label flow is a **pure infodesic** (a route followable with no
state information); the asymmetric homing mode is a **cost infodesic
segmented at informationally salient waypoints** (doorways), where the
free-energy triangle inequality fails and policy switching becomes
advantageous; **curvature**, concentrated at walls, is the knob that
decides whether the desics coincide (total saturation) or split
(segmentation into home + escape vocabulary).

## Source assets (referenced by TODO tags in main.tex)

| tag | asset |
|---|---|
| `[NB:policy-switching]` | `gridFour/notebooks/decision-information/policy-switching.ipynb` — triangle inequality fails across goal policies (concluded) |
| `[NB:infodesics]` | `gridFour/notebooks/geometry-paper/infodesics/*` — per-triple case studies |
| `[GB:01-03]` | `gridBench/notebooks/goal-geometry/01..03` — drift, corner law, switching-cost matrix, log-domain fixed-reference solver |
| `[S51]` | `gridFour/notebooks/attractor-fingerprint-probe/51-*` — policy-view machinery (segmented routes, label roles) |
| `[RN:salient]` | `twists-home-vectors/research-notes.md` — doorway salience ρ = −0.76 with mean free energy |
| `[CG]` | `cognitive-geom-paper/cognitive-geometry.tex` §Infodesics — definitions |

## Build

`latexmk -lualatex main.tex` (or `./build.sh`).  Includes are vendored
(copied from `twists-home-vectors` at skeleton time, paper-style `\code`
without highlight); `refs.bib` likewise starts as a copy — prune once the
citation set stabilises.
