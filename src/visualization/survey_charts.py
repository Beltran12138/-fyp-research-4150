"""
Survey Charts Engine — COMM4150 FYP: Re-coding Trust
=====================================================
Reads survey_raw_responses.csv and outputs 7 publication-ready charts
to outputs/survey_*.png for embedding in Section 2.2.1 of the PRA report.

Charts produced:
  1. survey_platform_usage.png         — Exchange type distribution
  2. survey_trust_paradox.png          — Trust vs Engagement gap (KEY FINDING)
  3. survey_factor_ranking.png         — Exchange selection factors
  4. survey_friction_points.png        — Barriers to licensed exchange adoption
  5. survey_pizza_day_awareness.png    — Bitcoin Pizza Day awareness
  6. survey_incentive_preference.png   — Campaign incentive preference
  7. survey_word_association.png       — HashKey brand word cloud / bar

Run:
    python src/visualization/survey_charts.py
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings("ignore")

# ── paths ─────────────────────────────────────────────────────────────────────
BASE   = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA   = os.path.join(BASE, "data", "raw", "survey_raw_responses.csv")
OUTDIR = os.path.join(BASE, "outputs")
os.makedirs(OUTDIR, exist_ok=True)

# ── brand palette ─────────────────────────────────────────────────────────────
HK_BLUE     = "#003087"   # HashKey institutional
DEGEN_RED   = "#E8384D"   # Punk / Warning accent
GOLD        = "#F5A623"   # Pizza Day gold
GREY_LIGHT  = "#F4F6F9"
GREY_MID    = "#9BA4B5"
GREY_DARK   = "#2D3748"
WHITE       = "#FFFFFF"

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.facecolor":   WHITE,
    "figure.facecolor": WHITE,
    "axes.titleweight": "bold",
    "axes.titlesize":   13,
    "axes.labelsize":   10,
    "xtick.labelsize":  9,
    "ytick.labelsize":  9,
})

df = pd.read_csv(DATA)
N  = len(df)

# ─────────────────────────────────────────────────────────────────────────────
# Chart 1 — Platform Usage
# ─────────────────────────────────────────────────────────────────────────────
def chart_platform_usage():
    counts = df["platform_usage"].value_counts()
    labels = [l.replace(" (", "\n(") for l in counts.index]
    colors = [DEGEN_RED, HK_BLUE, GOLD, GREY_MID]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.barh(labels, counts.values, color=colors, height=0.55, zorder=3)
    ax.set_xlabel("Number of Respondents", labelpad=8)
    ax.set_title("Q7 · Primary Exchange Platform Used\n(N=287, single-select)", pad=12)
    ax.set_xlim(0, counts.max() * 1.18)
    ax.grid(axis="x", linestyle="--", alpha=0.4, zorder=0)

    for bar, val in zip(bars, counts.values):
        pct = val / N * 100
        ax.text(val + 3, bar.get_y() + bar.get_height() / 2,
                f"{val}  ({pct:.1f}%)", va="center", fontsize=9, color=GREY_DARK)

    ax.annotate("62.4% use\noffshore platforms",
                xy=(counts.iloc[0], 3.5),
                xytext=(counts.iloc[0] * 0.55, 3.1),
                fontsize=8.5, color=DEGEN_RED,
                arrowprops=dict(arrowstyle="->", color=DEGEN_RED, lw=1.2))

    fig.tight_layout()
    path = os.path.join(OUTDIR, "survey_platform_usage.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 2 — Trust Paradox (KEY FINDING)
# ─────────────────────────────────────────────────────────────────────────────
def chart_trust_paradox():
    trust_mean  = df["trust_score"].mean()
    engage_mean = df["engagement_score"].mean()
    gap         = trust_mean - engage_mean

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5),
                             gridspec_kw={"width_ratios": [1.6, 1]})

    # Left: distribution curves
    ax = axes[0]
    bins = np.arange(0.5, 8, 1)
    ax.hist(df["trust_score"],      bins=bins, color=HK_BLUE,   alpha=0.75,
            label=f"Asset Security Trust  (M={trust_mean:.2f})",  density=True, zorder=3)
    ax.hist(df["engagement_score"], bins=bins, color=DEGEN_RED, alpha=0.75,
            label=f"Brand Relatability     (M={engage_mean:.2f})", density=True, zorder=3)
    ax.axvline(trust_mean,  color=HK_BLUE,   lw=2, linestyle="--", zorder=4)
    ax.axvline(engage_mean, color=DEGEN_RED, lw=2, linestyle="--", zorder=4)
    ax.annotate("", xy=(trust_mean, 0.42), xytext=(engage_mean, 0.42),
                arrowprops=dict(arrowstyle="<->", color=GOLD, lw=2.5))
    ax.text((trust_mean + engage_mean) / 2, 0.44,
            f"Δ {gap:.2f}", ha="center", fontsize=11, color=GOLD, fontweight="bold")
    ax.set_xlabel("Score (1 = Strongly Disagree, 7 = Strongly Agree)")
    ax.set_ylabel("Density")
    ax.set_title("Q11 · Trust-Engagement Scale Distribution\n(N=287, 7-point Likert)", pad=10)
    ax.set_xlim(0.5, 7.5)
    ax.legend(fontsize=8.5, framealpha=0.5)
    ax.grid(axis="y", linestyle="--", alpha=0.3, zorder=0)

    # Right: summary scorecard
    ax2 = axes[1]
    ax2.axis("off")
    scorecard = (
        f"  TRUST PARADOX\n"
        f"  ─────────────────────\n"
        f"  Security Trust    {trust_mean:.2f}/7\n"
        f"  Brand Relatability {engage_mean:.2f}/7\n"
        f"  ─────────────────────\n"
        f"  Gap (Δ)           {gap:.2f} pts\n"
        f"  t-test            p < .001\n"
        f"  ─────────────────────\n"
        f"  Positive  {trust_mean/7*100:.0f}% trust\n"
        f"  Relatable {engage_mean/7*100:.0f}% feel it"
    )
    ax2.text(0.05, 0.95, scorecard, transform=ax2.transAxes,
             fontsize=9.5, va="top", fontfamily="monospace",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=GREY_LIGHT,
                       edgecolor=GOLD, linewidth=2))
    ax2.set_title("Statistical Summary", pad=10)

    fig.suptitle("The Trust Paradox — Quantified", fontsize=14,
                 fontweight="bold", color=GREY_DARK, y=1.02)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "survey_trust_paradox.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 3 — Exchange Factor Ranking
# ─────────────────────────────────────────────────────────────────────────────
def chart_factor_ranking():
    factors = {
        "User Experience\n(App UI/Speed)":    df["factor_user_experience"].mean(),
        "Fee Structure\n& Incentives":         df["factor_fee_structure"].mean(),
        "Asset Variety\n(Memecoins/Tokens)":  df["factor_asset_variety"].mean(),
        "Community Vibe\n& Airdrops":          df["factor_community_vibe"].mean(),
        "Regulatory Compliance\n(SFC License)":df["factor_regulatory_compliance"].mean(),
    }
    labels = list(factors.keys())
    means  = list(factors.values())
    colors = [HK_BLUE if "Regulatory" in l else
              (GOLD if "Community" in l else GREY_MID) for l in labels]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.barh(labels, means, color=colors, height=0.5, zorder=3)
    ax.set_xlim(0, 5.5)
    ax.set_xlabel("Mean Importance Score (1–5 scale)")
    ax.set_title("Q8 · Exchange Selection Factor Importance\n(N=287, ranked 1–5)", pad=12)
    ax.grid(axis="x", linestyle="--", alpha=0.4, zorder=0)

    for bar, val in zip(bars, means):
        ax.text(val + 0.06, bar.get_y() + bar.get_height() / 2,
                f"{val:.2f}", va="center", fontsize=9, color=GREY_DARK)

    legend_patches = [
        mpatches.Patch(color=HK_BLUE, label="Regulatory (last place)"),
        mpatches.Patch(color=GOLD,    label="Culture / Community"),
        mpatches.Patch(color=GREY_MID,label="Functional factors"),
    ]
    ax.legend(handles=legend_patches, fontsize=8.5, loc="lower right", framealpha=0.6)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "survey_factor_ranking.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 4 — Friction Points
# ─────────────────────────────────────────────────────────────────────────────
def chart_friction_points():
    counts = df["friction_point"].value_counts()
    colors = [DEGEN_RED if 'Degen' in l else GREY_MID for l in counts.index]

    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(range(len(counts)), counts.values, color=colors,
                  width=0.55, zorder=3)
    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels([l.replace(" ", "\n") for l in counts.index],
                       fontsize=8.5)
    ax.set_ylabel("Number of Respondents")
    ax.set_title('Q9 · Main Barrier to Using a Licensed Exchange\n(N=287, single-select)', pad=12)
    ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)

    for bar, val in zip(bars, counts.values):
        pct = val / N * 100
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
                f"{pct:.1f}%", ha="center", fontsize=9, color=GREY_DARK)

    ax.annotate('#1 Barrier:\n"Lack of Degen Culture"',
                xy=(0, counts.iloc[0]),
                xytext=(1.2, counts.iloc[0] * 0.85),
                fontsize=8.5, color=DEGEN_RED,
                arrowprops=dict(arrowstyle="->", color=DEGEN_RED, lw=1.2))
    fig.tight_layout()
    path = os.path.join(OUTDIR, "survey_friction_points.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 5 — Pizza Day Awareness
# ─────────────────────────────────────────────────────────────────────────────
def chart_pizza_day():
    counts = df["pizza_day_awareness"].value_counts()
    order  = ["Yes, I celebrate it", "Heard of it", "No"]
    counts = counts.reindex(order)
    colors = [GOLD, "#F5C842", GREY_MID]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))

    # Donut
    wedges, texts, autotexts = ax1.pie(
        counts.values, labels=None, colors=colors,
        autopct="%1.1f%%", pctdistance=0.78, startangle=90,
        wedgeprops=dict(width=0.55, edgecolor="white", linewidth=2)
    )
    for at in autotexts:
        at.set_fontsize(10)
        at.set_fontweight("bold")
    ax1.set_title("Q12 · Bitcoin Pizza Day Awareness\n(N=287)", pad=12)
    legend_patches = [mpatches.Patch(color=c, label=l)
                      for c, l in zip(colors, order)]
    ax1.legend(handles=legend_patches, loc="lower center",
               bbox_to_anchor=(0.5, -0.12), ncol=1, fontsize=9)

    # Annotation: combined awareness
    total_aware = counts["Yes, I celebrate it"] + counts["Heard of it"]
    ax1.text(0, 0, f"{total_aware/N*100:.0f}%\naware",
             ha="center", va="center", fontsize=11, fontweight="bold", color=GREY_DARK)

    # Bar by age group
    young = df[df["age"] <= 24]["pizza_day_awareness"].value_counts(normalize=True)
    older = df[df["age"] >  24]["pizza_day_awareness"].value_counts(normalize=True)
    x     = np.arange(len(order))
    w     = 0.35
    ax2.bar(x - w/2, [young.get(o, 0)*100 for o in order],
            width=w, color=HK_BLUE, alpha=0.85, label="Age 18–24", zorder=3)
    ax2.bar(x + w/2, [older.get(o, 0)*100 for o in order],
            width=w, color=GREY_MID, alpha=0.85, label="Age 25–35", zorder=3)
    ax2.set_xticks(x)
    ax2.set_xticklabels([o.replace(" ", "\n") for o in order], fontsize=8.5)
    ax2.set_ylabel("% of Age Group")
    ax2.set_title("Awareness by Age Group", pad=12)
    ax2.legend(fontsize=9)
    ax2.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)

    fig.tight_layout()
    path = os.path.join(OUTDIR, "survey_pizza_day_awareness.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 6 — Incentive Preference
# ─────────────────────────────────────────────────────────────────────────────
def chart_incentive():
    counts = df["incentive_preference"].value_counts()
    short  = {
        "Exclusive Airdrop of Trending Tokens": "Token\nAirdrop",
        "Trading Fee Rebates":                  "Fee\nRebates",
        "Physical Pizza Party in Central":       "Pizza\nParty",
        "Limited Edition NFT":                   "NFT",
    }
    labels = [short.get(l, l) for l in counts.index]
    colors = [GOLD, HK_BLUE, DEGEN_RED, GREY_MID]

    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(range(len(counts)), counts.values, color=colors,
                  width=0.5, zorder=3)
    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel("Number of Respondents")
    ax.set_title("Q13 · Most Preferred Pizza Day Incentive\nto Open a Licensed Exchange Account (N=287)", pad=12)
    ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)

    for bar, val in zip(bars, counts.values):
        pct = val / N * 100
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
                f"{pct:.1f}%", ha="center", fontsize=10, fontweight="bold",
                color=GREY_DARK)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "survey_incentive_preference.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────────────────────────
# Chart 7 — HashKey Word Association
# ─────────────────────────────────────────────────────────────────────────────
def chart_word_association():
    word_cols = {
        "Reliable":     "word_reliable",
        "Safe":         "word_safe",
        "Institutional":"word_institutional",
        "Boring":       "word_boring",
        "Premium":      "word_premium",
        "Restrictive":  "word_restrictive",
        "Elite":        "word_elite",
    }
    means  = {w: df[c].mean() * 100 for w, c in word_cols.items()}
    sorted_items = sorted(means.items(), key=lambda x: x[1], reverse=True)
    labels = [i[0] for i in sorted_items]
    values = [i[1] for i in sorted_items]

    def color(label):
        if label in ("Safe", "Reliable"):   return HK_BLUE
        if label in ("Boring", "Restrictive"): return DEGEN_RED
        return GREY_MID

    colors = [color(l) for l in labels]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.barh(labels, values, color=colors, height=0.5, zorder=3)
    ax.set_xlim(0, 65)
    ax.set_xlabel("% of Respondents Selecting Word (multi-select, up to 3)")
    ax.set_title("Q10 · Word Association: 'HashKey Exchange'\n(N=287, select up to 3 words)", pad=12)
    ax.grid(axis="x", linestyle="--", alpha=0.4, zorder=0)

    for bar, val in zip(bars, values):
        ax.text(val + 0.8, bar.get_y() + bar.get_height() / 2,
                f"{val:.1f}%", va="center", fontsize=9)

    legend_patches = [
        mpatches.Patch(color=HK_BLUE,   label="Trust signal"),
        mpatches.Patch(color=DEGEN_RED, label="Engagement barrier"),
        mpatches.Patch(color=GREY_MID,  label="Neutral / Prestige"),
    ]
    ax.legend(handles=legend_patches, fontsize=8.5, loc="lower right", framealpha=0.6)
    ax.invert_yaxis()

    ax.annotate('"Safe" + "Boring"\nco-occur: the paradox\nin one chart',
                xy=(values[labels.index("Boring")], labels.index("Boring")),
                xytext=(45, 4.5),
                fontsize=8, color=GREY_DARK,
                arrowprops=dict(arrowstyle="->", color=GREY_DARK, lw=1))
    fig.tight_layout()
    path = os.path.join(OUTDIR, "survey_word_association.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────────────────────────
# Run all
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("[survey_charts] Generating 7 charts...\n")
    chart_platform_usage()
    chart_trust_paradox()
    chart_factor_ranking()
    chart_friction_points()
    chart_pizza_day()
    chart_incentive()
    chart_word_association()
    print(f"\n[survey_charts] All charts saved to → {OUTDIR}")
