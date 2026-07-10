# Switching cost vs prior specialisation — the record

Synthesis note, 10 July 2026. Combines the August 2024 ideas (the walk meeting
with Daniel, 9 Aug 2024, plus the RSOS rebuttal positions) with the July 2026
empirical campaign (gridBench goal-geometry notebooks 04, 09, 10), re-examines
the disjoint-subpolicies theorem from the Space-of-Goals supplementary
material, and states the switching cost mathematically, tied back to the exact
step where the published proof leans on an unstated assumption.

Sources: `cognitive-geom-paper/cognitive-geometry-sup-matl.tex`
(§ Triangle Inequality for Disjoint Subpolicies);
`cognitive-geom-paper/response-to-reviewers{,-2}.tex`;
`daily/2026-June/2026-06-11/transcript-polani-2024-08-09.md` (cleaned meeting
transcript); `workbench/topics/cognitive-geometry-kl-control` §7;
`gridBench/notebooks/goal-geometry/09-switching-cost-conjecture.py` and
`10-twist-prior-specialisation.py`. Feeds §5 (switching costs) and §6 of this
paper.

---

## 1. The August 2024 position

Assembled from the rebuttals (2022) and the 9 Aug 2024 meeting:

1. **The conjecture.** "When you create a switch, you are allowed to violate
   the triangle equality by a term determined by the switching cost" — and the
   switching cost is the **disambiguation cost**: zero if the two trajectory
   segments' supports do not overlap; otherwise the entropy of section
   membership (the 95/5 example), averaged over visitation. Round 1 put it as:
   the relaxation contribution "reflects the informational switching cost
   between the different segments."
2. **The theorem.** Supplementary material: the triangle inequality holds when
   the subpolicies are *essentially disjoint* — overlap presented as the entire
   source of breakage.
3. **The covering space.** "The discrete analogon of a covering space, where
   essentially different 'clones' of the underlying space are overlayed and are
   individually dealt with via different policies between which the agent
   switches at transition points." Operationalised in 2024 as clone-and-glue:
   two sheets, goal on the second, the switch state a zero-step link.
4. **The soup objection and the concession** (9 Aug 2024). K: the glued world
   computes decision information against the *joint* marginal, but the saving
   of a switch is that each section gets its *own* marginal. D: "where the
   switching cost really saves is that when the brain goes into a different
   memory state, it can use a different marginal."
5. **Conservation of misery.** The switch should not save information overall
   — abstraction reduces bandwidth, not total information; if the switching
   cost exactly reinstates the equality, we have a conservation law.
6. **Subgoals and landmarks.** Subgoals restrict the trajectory space
   (stochasticity makes this bite); funneling obstacles naturally allow
   subgoaling; future work: "landmark states form a natural segmentation of
   trajectories where switching policies is easy." Behavioural story: aiming
   off / handrailing. Open question: single policy (no maintenance cost) vs
   multiple policies (cheaper per segment) — the winner depends on the unknown
   C_switching.

## 2. Definitions

Cost-only MDP, goal g absorbing, rewards r ≤ 0. For a memoryless policy π and
a **state-independent reference distribution** q over actions, define

    F^{π,q}_g(s) = E^π_s [ Σ_{t<τ_g} ( −r_t + (1/β) log₂( π(a_t|s_t) / q(a_t) ) ) ].

The paper's free energy is the self-consistent (Blahut–Arimoto) object

    F_g(s) = F^{π_g, p̂_g}_g(s),   p̂_g(a) = Σ_s p_live(s) π_g(a|s),

with (π_g, p̂_g) the BA fixed point — the alternating minimisation of F^{π,q}
over π and q. Two standing facts:

- **(F1) Own marginal is optimal.** For fixed π, F^{π,q} is minimised over q at
  the visitation-weighted action marginal ρ_π (cross-entropy argmin). The
  formalism's p̂ uses the live distribution rather than the leg's
  visit-weighting; the two agree up to a small systematic noted in §6.
- **(F2) Exact prior-swap identity.** For fixed π, swapping the reference is
  exactly a log-ratio expectation:

      F^{π,q}_g(s) − F^{π,q'}_g(s) = (1/β) Σ_x ν^π_s(x) Σ_a π(a|x) log₂( q'(a) / q(a) ),

  where ν^π_s(x) is the expected number of decisions taken at x en route.
  Writing n = Σ_x ν(x) (expected leg length) and ρ(a) = (1/n) Σ_x ν(x) π(a|x)
  (the leg's action marginal), the swap away from the own marginal costs

      Δ(q) := F^{π,q} − F^{π,ρ} = (n/β) · D_KL( ρ ‖ q ).      (†)

## 3. The theorem, re-read: what the proof actually assumes

**Original statement** (supplementary material, verbatim in substance):

> Let s ≠ g. If for all s′ the trajectories induced by π₁ (goal s′, from s)
> and π₂ (goal g, from s′) intersect only at s′ — S_{π₁(s)} ∩ S_{π₂(s′)} =
> {s′} — then F_g(s) ≤ F^{π₁}_{s′}(s) + F^{π₂}_g(s′).

**Proof shape**: assume the inequality fails; glue π̂ = π₁ on S₁\{s′}, π₂ on
S₂ (well-defined *because* the supports are disjoint); expand F^{π̂}_g(s) over
trajectories and split the sum into the two legs, recovering
F^{π₁}_{s′}(s) + F^{π₂}_g(s′) < F_g(s) — contradicting optimality of π_F.

**The unstated assumption.** In the expansion (eq. S-inequality_expansion) every
log term is written against a single marginal p̂(a) — the same symbol in the
leg-1 terms, the leg-2 terms, and the glued policy's free energy. The split of
the trajectory sum into the two named free energies is an identity **only if
all three quantities are referenced to one common prior**. But the theorem's
right-hand side is defined with each leg's *own* self-consistent marginal
(p̂₁ ≠ p̂₂ in general), and the left-hand side with the direct problem's p̂_g.
So the proof, as written, establishes:

> **Theorem A (what the 2022 proof proves).** If the supports are essentially
> disjoint *and all free energies are referenced to a common prior q*, then
> F^{q}_g(s) ≤ F^{π₁,q}_{s′}(s) + F^{π₂,q}_g(s′).

With per-leg marginals the marginalisation step silently drops the swap cost
(†) on each leg — and that dropped term is not small: it is, empirically, the
entire violation.

**Empirical confirmation that disjointness is not the load-bearing hypothesis**
(nb09): the *worst* triangle violations sit on triples whose segments barely
overlap (minimum overlap ≈ 0.01 expected shared visits, against a median of
1–2 for non-violating triples), and the gap is uncorrelated with every
state-level identification cost (|r| < 0.12). Overlap is not the source of the
breakage; the per-leg priors are.

## 4. The switching cost, mathematically — related back to the proof

Fix the failure at exactly the step it occurs. Repeat the glueing, but keep
the priors explicit. For **any** single reference q (using F_g ≤ F^{π̂,q} and
the disjoint-support decomposition of π̂'s trajectory measure):

    F_g(s) ≤ F^{π₁,q}_{s′}(s) + F^{π₂,q}_g(s′)
           = F_{s′}(s) + F_g(s′) + Δ₁(q) + Δ₂(q),

with Δᵢ(q) = (nᵢ/β)·D_KL(ρᵢ‖q) from (†) (up to the live-vs-visit slack of F1).
Minimising the correction over the free choice of q:

    gap(s, s′, g) ≤ min_q [ Δ₁(q) + Δ₂(q) ]
                  = ((n₁+n₂)/β) · JS_w( ρ₁, ρ₂ ),     w = n₁/(n₁+n₂),   (‡)

since the weighted sum of KLs is minimised by the mixture
q* = w ρ₁ + (1−w) ρ₂, yielding the weighted Jensen–Shannon divergence. This is
the switching cost:

> **C_switch = (expected total leg length / β) × the weighted Jensen–Shannon
> divergence between the two legs' action marginals.**

Properties, each answering a 2024 position:

- **It vanishes iff ρ₁ = ρ₂** — marginal agreement, *not* support
  disjointness. This is Daniel's own concession made precise: the switch's
  saving (and hence the violation it licenses) is the per-section marginal.
- **JS_w(ρ₁,ρ₂) = I(M; A)** where M ∼ Bernoulli(w) is *which leg* and A the
  action drawn from that leg's marginal: the mutual information between the
  section variable and the action. The switching cost is the part of "which
  section am I in" that is *visible in the actions*.
- **I(M; A) ≤ H(M) = H_b(w)** — Daniel's disambiguation entropy is the exact
  upper envelope of the true term. His 2024 conjecture named the right object
  at the wrong granularity: the entropy cap lives at the action-marginal level
  (per leg), not at the per-state membership level. The state-level forms
  (visit-weighted H_b of membership; per-state policy JS) are the ones nb09
  tested and refuted — they are the joint-marginal/clone-and-glue accounting,
  i.e. exactly what the soup objection said would fail.
- **The §7 bound is the one-sided instance.** Our implementation uses a
  uniform live distribution, so p̂ is goal-indexed and choosing q = p̂_g makes
  Δ₂ = 0 exactly (the direct solve is its own fixed point). Then (‡) reduces to

      gap ≤ Δ₁(p̂_g) = (1/β) Σ_x ν₁(x) E_{π₁(·|x)}[ log₂( p̂₁(a)/p̂_g(a) ) ]
                     ≈ (n₁/β) · D_KL( p̂₁ ‖ p̂_g ),

  which is the workbench §7 C_switch and notebook 10's PS_est. The measured
  prior-specialisation credit PS = F^{p̂_g-reprice}₁ − F₁ satisfies PS ≤ Δ₁
  (re-optimising the policy under the foreign prior can only help), so the
  chain is gap ≤ PS ≤ Δ₁(p̂_g) ≤ (‡'s symmetric form at q = p̂_g).

**Relation back to the proof, in one sentence:** the published proof is correct
for a common prior and needs disjointness only to make the glued policy
well-defined; restoring the per-leg priors adds exactly the Δ terms, whose
q-minimised value (‡) is the switching cost — so the "relaxed triangle
inequality with C_switching" the paper conjectured in Future Work is (‡), with
C_switching a *marginal-level* Jensen–Shannon quantity, not a state-level
disambiguation entropy.

**The overlap term, demoted.** Without disjointness the glueing needs the
memory bit M — the covering space of the 2024 discussion. Whatever overlap
adds beyond (‡) is a genuine identification cost, but empirically it is below
resolution: repricing leg 1 alone (no overlap term at all) already restores
the inequality on every triple tested (§6). Overlap moved from "the entire
source of the breakage" to a second-order correction not yet distinguishable
from zero.

## 5. What the experiments established (nb04, 09, 10)

- **nb04**: flat worlds have zero violating triples at every β; walled worlds
  violate (four_rooms ~1% of triples, 1-in-6 ordered pairs have a profitable
  midpoint); the gap grows as β falls (max 1.14 / 3.43 / 11.05 at β = 3/1/0.3);
  the GA exemplar twist *amplifies* violations 2.4× while lowering mean cost.
- **nb09**: no state-level switching-cost model restores the inequality
  (one-off misses the tail; per-decision membership entropy covers 17–88%;
  per-state policy JS 3–32%); repricing leg 1 under the direct marginal
  collapses **every** violation to solver noise across ~178k triples
  (four_rooms β ∈ {0.3,1,3}, ring corridor β = 1). The violation *is* prior
  specialisation.
- **nb10 + cohort**: five GA run-bests (coverages 0.85, 0.82, 0.40, 0.47,
  0.38) plus Cartesian, all at β = 1 (exemplar also at 0.3 and 3):
  - shared-prior survivors above solver noise: **0 in every condition** —
    the common-prior quasimetric is frame-independent;
  - PS_est (= Δ₁(p̂_g)) upper-bounds measured PS on **100.0%** of triples in
    every frame, r = 0.93–0.96 (twists), 0.995 (Cartesian);
  - the twists' amplified violations ride *more divergent* per-goal marginals
    (median pairwise KL 1.24–4.44 bits vs Cartesian 0.79 — most divergent for
    the low-coverage, fragmented twists). Violation *rate* and marginal
    divergence measure different things: amplification tracks coverage (the
    saturated twists, 0.85/0.82, violate on 3.3%/2.7% of triples; the
    fragmented ones sit near Cartesian at 1.2–1.8%) — a strong coherent flow
    makes two-leg routes profitable *often*, divergent vocabularies make each
    one *large*;
  - PS concentrates off the habit flow: on-flow leg pairs (both goals'
    marginals > 0.5 on the dominant label) carry median PS 0.6–1.9
    bits-equivalent vs 6.1–15.9 off-flow (4–8× separation in all five twists),
    with corr(marginal KL, PS) = 0.89–0.93. The home-cycle flow is a
    **marginal-compatibility class**.
- **Precision check** (Cartesian β = 1, θ tightened 1e-5 → 1e-8/1e-9): max
  shared-prior residual 5.3e-4 bits against gaps of order 1–11 bits — four
  orders of magnitude — with zero triples above 1e-3. The residual is
  dominated by the marginal-extraction systematic (the fixed-point deviation,
  4.2e-4, did not shrink with θ), not by convergence, so whether a genuine
  stochasticity correction exists below ~1e-3 bits is open. In deterministic
  dynamics the common-prior inequality is exact by path concatenation; the
  stochastic case (transition expectation inside the exponent — risk-sensitive,
  not LMDP) still wants a proof.

## 6. August 2024 vs July 2026, idea by idea

| August 2024 | July 2026 status |
|---|---|
| Violation = switching cost in disguise | Half right. Violation = **prior-specialisation credit** (the marginal-level part of the switching cost); the state-level disambiguation part is second-order, below solver noise. |
| No overlap → no cost → triangle holds | **Wrong as stated**: worst violations sit on near-disjoint legs. Correct vanishing condition: **ρ₁ = ρ₂** (marginal agreement). |
| Disambiguation entropy H(M\|S), per step | Upper envelope only: the true term is I(M;A) = JS_w(ρ₁,ρ₂) ≤ H_b(w). Right intuition, wrong granularity — and the per-state versions fail empirically. |
| Clone-and-glue two sheets | Correct as a memory formalism; fails with the joint marginal — exactly the soup objection. nb09's refuted state-level costs are the joint-marginal accounting, empirically vindicating the 2024 objection. |
| Different marginal per memory state (the concession) | **The mechanism.** Validated: repricing one leg's marginal explains 100% of the violation, in both frames, five twists. |
| Conservation of misery (switch can't save information overall) | Quantified: gap/credit is near 1 at β ≥ 1 (median PS share 1.07 Cartesian, 1.16–1.48 twists) — nearly a conservation law — but the credit overshoots at β = 0.3 (share ≈ 2) and in twisted frames. The matching lower bound is still open; the tightness numbers now exist. |
| Landmarks = where switching is easy; funneling → natural subgoals | Refined: landmarks are **marginal-agreement states** (nb05: doorways have zero switch rate — basins flow through); the flow itself is a marginal-compatibility class (nb10). Funneling creates marginal-incompatible legs on either side, which is where the profitable subgoals live. |
| Brains change the cognitive geometry of space | The twist experiment realises it: evolution reshapes the marginal-compatibility classes (pairwise KL 0.79 → 1.24–4.44), cheapening the mean route while *adding* profitable segmentation off-flow. The "perfect twist / switching cost on steroids" sketch from the walk is notebooks 04+10. |
| Options / cost of adding a meta-level | Concrete and computable: the meta-level costs (n/β)·JS between the options' action marginals — zero for options that share a vocabulary, priced by (‡) otherwise. |

## 7. Adjusted statements (proposed for §5 / any RSOS follow-up)

- **Theorem A (repair of the published theorem).** Common prior q + essentially
  disjoint supports ⟹ F^{q}_g(s) ≤ F^{π₁,q}_{s′}(s) + F^{π₂,q}_g(s′). (The
  2022 proof, with its implicit assumption made explicit. Disjointness is used
  only for well-definedness of the glued policy.)
- **Proposition B (conjectured; empirically exact to < 1e-3 bits).** With a
  common prior, the free energy is a quasimetric *without any disjointness
  condition*: exact for deterministic dynamics by path concatenation;
  stochastic case open below the current numerical floor.
- **Corollary C (the corrected relaxed inequality — the Future-Work programme
  resolved).** With per-leg self-consistent marginals,
  F_g(s) ≤ F_{s′}(s) + F_g(s′) + C_switch, with
  C_switch = ((n₁+n₂)/β)·JS_w(ρ₁, ρ₂) (‡), one-sided form Δ₁(p̂_g) validated on
  ~350k triples across six σ-frames: 100% coverage, r ≈ 0.93–0.995, zero
  violations of the bound.

**Do we need to adjust the theorem? Yes, in three ways:** (i) make the common
prior explicit in the hypotheses — it, not disjointness, is load-bearing;
(ii) drop (or demote to "conjecturally unnecessary") the disjointness
condition in the common-prior form; (iii) replace the Future-Work
"C_switching as disambiguation cost" with the marginal-level (‡) — the
disambiguation entropy survives only as the upper envelope H_b(w) of the true
mutual-information term.
