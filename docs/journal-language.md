# Journal language — the translation table

Working glossary for the multidisciplinary rewrite (started 10 Jul 2026 with
§5). Rule of the exercise: **more intuitive without softening** — every plain
phrase must be *exactly* the formal object, so a technical reader can invert
the translation and a general reader never has to. Each entry: formal term →
plain phrase (used in prose/figures) → what makes it exact.

| Formal | Plain | Why it is exact |
|---|---|---|
| action marginal / prior $\hat p$, $\rho$ | **habitual mix of moves** / **(habit-)vocabulary** | it *is* the route's overall move distribution, state-blind; "habitual actions" is Daniel's own gloss in the 2024 transcript |
| decision information $\mathcal{I}_D$ | **decisions** (as a costed quantity); "deviations from the habitual mix are what cost decisions" | $\mathcal{I}_D$ is exactly the accumulated KL from the marginal |
| free energy $\mathcal{F}$ | **total cost of the journey: steps + decisions** | $\mathcal{F} = -V + \mathcal{I}_D/\beta$, no residue |
| triangle-inequality violation | **a stopover that beats the direct route** (two-leg air fare undercutting the direct flight) | violation literally means $D[A,B]+D[B,C] < D[A,C]$ |
| the gap | **the (stopover) discount** | gap = direct − segmented cost |
| prior specialisation (PS) | **what a leg saves by using its own vocabulary instead of the journey's** / **the vocabulary credit** | PS = reprice of the leg under the other marginal, an exact identity (eq. prior-swap) |
| $C_{\text{switch}} = \frac{n}{\beta}\mathrm{JS}_w(\rho_1,\rho_2)$ | **the value of changing vocabulary at the waypoint** | the q-minimised sum of the legs' reprices, closed form |
| $I(M;A)$ | **the part of "which leg am I on" that is visible in the actions** | mutual information between section variable and action |
| $H_b(w)$ bound | **at most a coin-flip's worth per expected step** | binary entropy of the leg-length split |
| disambiguation cost (2022 conjecture) | **the cost of remembering which leg you are on** | per-decision membership-entropy reading, refuted as the source of the discount |
| quasimetric | **a distance table where out and back can differ** | asymmetry is the only dropped axiom (plus the here-relevant triangle property named separately) |
| policy support overlap | **the two legs sharing ground** | visitation supports intersecting |
| marginal-compatibility class | **goals that share a vocabulary** | pairwise marginal KL ≈ 0 within the class |
| twist / $\sigma$ | (context) **relabelling of the controls per place** — paper already defines; avoid "sigma" in prose | |
| pure infodesic / single-label flow | **a route you can follow without looking** (press the same control everywhere) | $\mathcal{I}_D \to 0$, state-blind |
| home cycle / attractor | **where the habit takes you if you never look** | limit set of the single-label flow |
| coverage | **how much of the world one habit reaches** | largest-basin fraction of a label |
| $\beta$ (parsimony) | **the decision budget** (small $\beta$ = decisions expensive) | Lagrange weight on $\mathcal{I}_D$; careful: "budget" loosely — keep $\beta$ symbol alongside |
| triangle violation on flat worlds (nb11/nb12) | **the labelling manufactures stopover discounts on a world with no walls** | Cartesian torus: zero violations, identical vocabularies by symmetry |

## Status of the pass

- **Done (10 Jul)**: §5 plain-language spine (air-fare paragraph), stopover
  schematic (`F-stopover-schematic.png`, source `figures/src/`), glosses in
  "Reading the closed form", captions of the decomposition and twist-PS
  figures rewritten in ledger language.
- **Next candidates**, in rough order of jargon density:
  1. §2 background — one plain sentence per desic kind; the fare line can be
     forward-referenced from the triangle-inequality paragraph.
  2. §4 figures (`F-triangle-violation`, `F-segmentation-switch-points`,
     `F-triangle-twist-vs-cartesian`): axis labels still notebook-grade
     ("gap = direct − segmented cost (positive = violation)" → "stopover
     discount (bits)"); doorway-flank story is already plain.
  3. §3 pure-infodesic prose — "a route you can follow without looking" as
     the lead sentence.
  4. Theorem/Proposition/Corollary statements stay formal (they must), but
     each can take a one-line plain paraphrase *after* the environment.
  5. Abstract & intro, once the section language settles.

## House rules

- Plain phrase first *or* formal first is decided per sentence by which
  reader hits it first; but every formal object gets its plain gloss at
  first use and the pairing stays fixed for the whole paper.
- Never replace a number or weaken a quantifier in translation ("every
  ordered triple tested", not "routes tend to").
- Analogies must be structurally exact (air fare = triangle violation), not
  merely evocative; if an analogy needs a caveat, drop the analogy.
