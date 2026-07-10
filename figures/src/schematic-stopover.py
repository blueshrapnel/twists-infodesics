# Schematic for section 5: why a stopover can beat the direct route.
# Pure illustration (marked as such) -- the quantitative claims live in
# F-switching-cost-decomposition.png.  Renders F-stopover-schematic.png.
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Wedge

MOVE_COLS = ["#4477aa", "#ee7733", "#88ccee", "#aa3377"]
MOVE_NAMES = ["north", "east", "south", "west"]
ROUTE_COL = "#444444"


def pie(ax, xy, fracs, r=0.13):
    start = 90.0
    for f, c in zip(fracs, MOVE_COLS):
        ax.add_patch(Wedge(xy, r, start - 360 * f, start, fc=c, ec="white",
                           lw=0.8, zorder=6))
        start -= 360.0 * f


def route(ax, pts, lw=2.4, ls="-"):
    for p, q in zip(pts[:-1], pts[1:]):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>",
                                     mutation_scale=15, lw=lw,
                                     color=ROUTE_COL, linestyle=ls,
                                     shrinkA=7, shrinkB=7, zorder=4))


def nodes(ax, A, B, C, waypoint_dxy=(-78, -2)):
    for xy, name, dxy in ((A, "start", (-2, -16)), (B, "waypoint", waypoint_dxy),
                          (C, "goal", (2, 10))):
        ax.plot(*xy, "o", ms=9, color="black", zorder=7)
        ax.annotate(name, xy, textcoords="offset points", xytext=dxy,
                    fontsize=10)


fig, axes = plt.subplots(1, 3, figsize=(12.8, 4.3), dpi=150,
                         gridspec_kw=dict(width_ratios=[1.1, 1.1, 0.9]))
A, B, C = (0.16, 0.16), (0.78, 0.30), (0.94, 0.92)

# ---- panel 1: direct route, one mix of moves --------------------------
ax = axes[0]
ax.set_xlim(0, 1.30); ax.set_ylim(0, 1.10); ax.set_aspect("equal")
ax.axis("off")
nodes(ax, A, B, C, waypoint_dxy=(8, -14))
route(ax, [A, (0.48, 0.22), B, (0.90, 0.60), C])
pie(ax, (0.28, 0.86), [0.33, 0.42, 0.11, 0.14])
ax.annotate("one mix of moves\nfor the whole journey", (0.28, 0.86),
            textcoords="offset points", xytext=(0, -46), ha="center",
            fontsize=9)
ax.set_title("direct: one habitual mix", fontsize=11)

# ---- panel 2: stopover, each leg its own mix --------------------------
ax = axes[1]
ax.set_xlim(0, 1.30); ax.set_ylim(0, 1.10); ax.set_aspect("equal")
ax.axis("off")
nodes(ax, A, B, C, waypoint_dxy=(8, -14))
route(ax, [A, (0.48, 0.22), B])
route(ax, [B, (0.90, 0.60), C], ls=(0, (5, 2)))
pie(ax, (0.30, 0.52), [0.08, 0.80, 0.05, 0.07])
ax.annotate("leg 1: mostly east", (0.30, 0.52), textcoords="offset points",
            xytext=(0, -32), ha="center", fontsize=9)
pie(ax, (0.40, 0.88), [0.76, 0.10, 0.07, 0.07])
ax.annotate("leg 2: mostly north", (0.40, 0.88), textcoords="offset points",
            xytext=(0, -32), ha="center", fontsize=9)
ax.set_title("stopover: each leg its own mix", fontsize=11)

# ---- panel 3: the ledger ----------------------------------------------
ax = axes[2]
direct, leg1, leg2 = 10.0, 4.2, 3.4
credit = direct - leg1 - leg2
ax.bar(0, direct, width=0.5, color=ROUTE_COL)
ax.bar(1, leg1, width=0.5, color="#b8cbe4", edgecolor=ROUTE_COL, lw=0.8)
ax.bar(1, leg2, width=0.5, bottom=leg1, color="#f5cfae",
       edgecolor=ROUTE_COL, lw=0.8)
ax.bar(1, credit, width=0.5, bottom=leg1 + leg2, color="white",
       edgecolor="#cc3311", hatch="//", lw=1.4)
ax.text(0, direct + 0.25, "direct\ncost", ha="center", fontsize=9)
ax.text(1, leg1 / 2, "leg 1", ha="center", va="center", fontsize=9)
ax.text(1, leg1 + leg2 / 2, "leg 2", ha="center", va="center", fontsize=9)
ax.annotate("the discount =\nvalue of changing\nvocabulary at the waypoint",
            (1.28, leg1 + leg2 + credit / 2), fontsize=8.5, color="#cc3311",
            va="center", ha="left")
ax.set_xlim(-0.55, 3.0)
ax.set_ylim(0, 11.8)
ax.set_xticks([0, 1], ["direct", "stopover"])
ax.set_ylabel("total cost of the journey:\nsteps + decisions (free energy)",
              fontsize=9)
ax.set_yticks([])
ax.set_title("the ledger (schematic)", fontsize=11)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)

handles = [Rectangle((0, 0), 1, 1, color=c) for c in MOVE_COLS]
fig.legend(handles, MOVE_NAMES, loc="lower center", ncol=4, fontsize=8.5,
           frameon=False, bbox_to_anchor=(0.40, 0.0), title="moves",
           title_fontsize=8.5)
fig.suptitle("Why a stopover can beat the direct route: not the switch — "
             "the change of habitual vocabulary", fontsize=12)
fig.tight_layout(rect=(0, 0.06, 1, 1))
out = Path(__file__).resolve().parents[1] / "F-stopover-schematic.png"
fig.savefig(out, dpi=150, bbox_inches="tight")
print(f"wrote {out}")
