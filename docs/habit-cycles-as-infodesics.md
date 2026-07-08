# Habit cycles as infodesics

Interpretation note for the twists-home-vectors work: the habit-cycle / home-vector
structures this paper characterises *are* infodesics in the Space-of-Goals sense.
Paper 1 (this folder) reports the structures empirically (saturation typology,
cycle-escape decomposition); this note records the infodesic reading, which is
Paper 2 / thesis territory but explains *why* the structures are what they are.

Infodesics are NOT one of the "resurrected strands" (path-integral control,
empirical decision information, diffusion — stalled threads being revived). They
are the live, central object of the cognitive-geometry programme, continuous from
the Space of Goals paper (2022) through the current sphere / geodesic–loxodrome /
curvature work — never set aside. This note connects the paper's empirical habit
structures to that live object.

Sources: infodesic definitions in `cognitive-geom-paper/cognitive-geometry.tex`
(§Infodesics, ll. ~867–940); cycle-escape results in `main.tex` §Mechanism and the
5 June cohort analysis; the geodesic/loxodrome/curvature thread in
`~/Dropbox/phd/daily/2026-June/2026-06-10/note.tex`. Vault concept note:
`atlas/concepts/habit-cycles-as-infodesics.md`.

## A single-label flow is a pure infodesic

A **pure infodesic** is a sequence visitable with *no state information* — action
selection independent of state, decision information I_D → 0, "following the same
direction with as little cognitive correction as possible" (optimal open-loop policy).

A **single-label flow** is exactly that: press one label in every state. The label
is state-independent (I_D ≈ 0), even though the twist makes the *physical* direction
vary cell to cell. This is the "single-label flows are informationally free"
observation made precise: single-label flow = constant-label = open-loop = pure
infodesic = loxodrome = directional desic.

- **Home vector** = the direction field of a pure infodesic — the open-loop "point
  home" bearing (Mallot Ch 5.2 path-integration primitive = the loxodrome / constant
  bearing).
- **Habit cycle** = the attractor the pure infodesic drains into — the recurrent home
  set the open-loop single-label policy reaches; in infodesic terms, the *goal* of
  the pure infodesic.

The cycle is the infodesic's terminus, the home vector its flow, and the *habit* is
the whole pure-infodesic object (flow + limit set).

## The asymmetric mode is a cost infodesic, segmented at waypoints

A **cost infodesic** is a free-energy-optimal route where the free-energy triangle
inequality holds with equality; subsegments carry *different* policies; and when the
triangle equality is enforced, "policy switching and a collection of informationally
salient midpoints emerges via the segmentation of behaviour."

That is exactly the cycle-escape three-role decomposition reported in this paper:

| Cycle-escape role (this paper) | Infodesic reading |
|---|---|
| Home label (drains to home cycle) | one pure-infodesic leg |
| Directed-escape label (exits to opposite room) | the policy *switch* to a second pure-infodesic leg |
| Doorway between regions | informationally salient midpoint / subgoal where switching emerges |
| Cycle-respecting silenced label | the deficient / trivial part of the infodesic |

So the asymmetric habit = a cost infodesic chopped into single-label (pure-infodesic)
legs joined at doorway waypoints by policy switches. Mallot's place-graph (places
linked by labelled routes) is this segmentation. It is the same mechanism as the
ε-infodesic gap going negative "when it becomes advantageous to use multiple
policies".

## Curvature and β explain the bimodality

- **Open envs** (wrap_grid; zero curvature): pure infodesic = value geodesic = cost
  infodesic coincide → one constant-direction label is also shortest → total
  saturation, four clean home vectors, no switching. The habit *is* the geodesic.
- **Walled envs** (four_rooms, x_wall; curvature concentrated at walls/doorways): the
  desics split, the cost infodesic goes deficient / non-contiguous → no single
  direction reaches the goal optimally → the route segments → the home +
  directed-escape structure. The deficiency *is* the need for the escape-waypoint
  label.

So the saturation bimodality this paper documents (total saturation vs
asymmetric-saturation-with-escape) is the discrete face of the loxodrome-vs-segmented-
infodesic story, with **curvature** the shared knob — a twist is a global action
labelling on a possibly non-flat space, its holonomy = curvature = the I_D cost the
geometry forces. Because the GA optimises free energy at β = 1, the habit solutions
sit toward the low-I_D / loxodromic end of the loxodrome↔geodesic interpolation:
habits are the cheap, far-predictable extreme of the infodesic family.

## Where it lands

- **Paper 1 (this folder):** stays structural — the saturation typology and
  cycle-escape decomposition as reported. At most one discussion sentence flagging
  that the home label is an informationally-free single-label flow (a pure infodesic)
  and the directed-escape label is a policy switch.
- **Paper 2 / thesis Ch 4–5:** the full bridge — home vectors and habit cycles as the
  direction-fields and attractors of pure infodesics; the asymmetric habit as a
  segmented cost infodesic; curvature as the knob unifying the discrete habit results
  with the continuous sphere/manifold infodesic work. This is the hinge that turns
  "habits have geometry" from a slogan into the infodesic claim.
