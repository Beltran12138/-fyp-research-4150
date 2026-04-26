"""
Section 2.3 Comparative Benchmark Charts
LBank vs HashKey — Re-coding Trust FYP
ZHAO Han (1155191400) | COMM4150

Charts generated:
    1. benchmark_brand_matrix.png       — Positioning scatter (trust vs cultural resonance)
    2. benchmark_motivation_compare.png — Side-by-side selection drivers (horizontal bars)
    3. benchmark_discovery_overlap.png  — Channel overlap grouped bar
    4. benchmark_user_profile_compare.png — Investment scale + platform tenure
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../../outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Color palette ──────────────────────────────────────────────────────────────
HK_BLUE   = "#1A3A5C"   # HashKey
HK_GOLD   = "#C9A84C"   # HashKey accent
LB_YELLOW = "#F5C800"   # LBank brand yellow
LB_BLACK  = "#1A1A1A"   # LBank text
GRAY      = "#E8E8E8"
WHITE     = "#FFFFFF"

FONT_FAMILY = "DejaVu Sans"
plt.rcParams.update({
    "font.family": FONT_FAMILY,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


# ── Chart 1: Brand Positioning Scatter ────────────────────────────────────────
def chart_brand_matrix():
    fig, ax = plt.subplots(figsize=(9, 7))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)

    # Exchanges: (trust score, cultural resonance score, label, color, size)
    # Trust: HashKey=5.27/7→75%, LBank inferred low ~35%, Binance ~55%, Bybit ~52%
    # Cultural resonance: HashKey=2.75/7→39%, LBank high ~82%, Binance ~65%, Bybit ~68%
    exchanges = [
        (75, 39,  "HashKey",   HK_BLUE,   220),
        (35, 82,  "LBank",     LB_YELLOW, 220),
        (62, 65,  "Binance",   "#F0B90B", 140),
        (50, 68,  "Bybit",     "#F7A600", 120),
        (47, 70,  "MEXC",      "#2354E6", 110),
        (46, 72,  "Bitget",    "#1DA2FF", 110),
        (44, 58,  "KuCoin",    "#00A3E0", 100),
        (30, 80,  "DEX",       "#9B59B6", 90),
    ]

    for (x, y, label, color, size) in exchanges:
        ax.scatter(x, y, color=color, s=size, zorder=5, edgecolors=LB_BLACK, linewidths=0.8)
        offset_x = 2 if label not in ["HashKey", "LBank"] else 0
        offset_y = -6 if label == "HashKey" else (5 if label == "LBank" else 3)
        ha = "left" if label not in ["HashKey"] else "center"
        ax.annotate(label, (x, y), xytext=(x + offset_x, y + offset_y),
                    fontsize=9, fontweight="bold" if label in ["HashKey", "LBank"] else "normal",
                    color=LB_BLACK, ha=ha)

    # "Safe Punk" zone star
    ax.scatter(73, 78, marker="*", color="#E74C3C", s=400, zorder=6)
    ax.annotate("\"Safe Punk\"\nOpportunity Zone", (73, 78),
                xytext=(55, 88), fontsize=8.5, color="#E74C3C",
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#E74C3C", lw=1.2))

    # Quadrant shading
    ax.axvline(x=52, color=GRAY, lw=1, linestyle="--", zorder=1)
    ax.axhline(y=60, color=GRAY, lw=1, linestyle="--", zorder=1)
    ax.text(15, 85, "High Culture\nLow Trust\n(Offshore Degen)", fontsize=7.5, color="#888",
            ha="center", style="italic")
    ax.text(80, 85, "High Culture\nHigh Trust\n(Target Zone)", fontsize=7.5, color="#E74C3C",
            ha="center", style="italic", fontweight="bold")
    ax.text(15, 35, "Low Culture\nLow Trust\n(Niche / Unknown)", fontsize=7.5, color="#888",
            ha="center", style="italic")
    ax.text(80, 35, "Low Culture\nHigh Trust\n(Institutional / Boring)", fontsize=7.5, color="#888",
            ha="center", style="italic")

    ax.set_xlim(0, 100)
    ax.set_ylim(20, 100)
    ax.set_xlabel("Institutional Trust Score  (higher = more trusted)", fontsize=10, color=LB_BLACK)
    ax.set_ylabel("Cultural Resonance Score  (higher = more relatable)", fontsize=10, color=LB_BLACK)
    ax.set_title("Figure 2.3-A: Exchange Brand Positioning Matrix\nTrust vs. Cultural Resonance",
                 fontsize=12, fontweight="bold", color=LB_BLACK, pad=14)

    note = ("Sources: HashKey trust/relatability — Section 2.2.1 survey (N=287, HK).\n"
            "LBank cultural resonance — LBank User Research Report, Apr 2025 (N=1,751).\n"
            "Other exchanges estimated from Section 2.2.1 qualitative data.")
    fig.text(0.5, 0.01, note, ha="center", fontsize=7, color="#999", style="italic")

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    out = os.path.join(OUTPUT_DIR, "benchmark_brand_matrix.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")


# ── Chart 2: Selection Driver Comparison ──────────────────────────────────────
def chart_motivation_compare():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.patch.set_facecolor(WHITE)
    fig.suptitle("Figure 2.3-B: Primary Selection Drivers — LBank vs. HashKey HK Market",
                 fontsize=12, fontweight="bold", color=LB_BLACK, y=1.01)

    # LBank data (% of N=1,797)
    lbank_labels = [
        "Meme speed &\nliquidity",
        "Wide crypto\nselection",
        "Incentives /\nrewards",
        "Lower fees",
        "User-friendly\ninterface",
        "Security",
    ]
    lbank_vals = [37.79, 24.87, 12.02, 10.91, 6.62, 4.79]

    # HashKey HK (mean score 1-5, rescaled to %)
    hk_labels = [
        "UX Quality",
        "Fee Structure",
        "Asset Variety",
        "Community\nVibe",
        "Regulatory\nCompliance",
    ]
    hk_vals = [84.2, 81.8, 77.6, 68.6, 63.2]   # (score-1)/(5-1)*100

    for ax, labels, vals, color, title, xlabel in [
        (axes[0], lbank_labels, lbank_vals, LB_YELLOW,
         "LBank  (Why users chose, N=1,797)", "% of respondents"),
        (axes[1], hk_labels, hk_vals, HK_BLUE,
         "HashKey HK  (Factor importance rank, N=287)", "Importance score rescaled (%)"),
    ]:
        ax.set_facecolor(WHITE)
        bars = ax.barh(labels[::-1], vals[::-1], color=color,
                       edgecolor=LB_BLACK, linewidth=0.6, height=0.6)
        for bar, val in zip(bars, vals[::-1]):
            ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2,
                    f"{val:.1f}{'%' if '%' in xlabel else ''}", va="center", fontsize=8.5)
        ax.set_title(title, fontsize=9.5, fontweight="bold", color=LB_BLACK, pad=8)
        ax.set_xlabel(xlabel, fontsize=8.5)
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)
        ax.set_xlim(0, max(vals) * 1.25)

    note = "Sources: LBank User Research Report Apr 2025 (N=1,797); Section 2.2.1 Survey (N=287, HK, Feb–Mar 2026)."
    fig.text(0.5, -0.02, note, ha="center", fontsize=7, color="#999", style="italic")
    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, "benchmark_motivation_compare.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")


# ── Chart 3: Discovery Channel Overlap ────────────────────────────────────────
def chart_discovery_overlap():
    channels = ["Telegram", "Twitter / X", "Friend\nReferral", "Official\nAdvertising", "Internet\nSearch"]
    # LBank (% of N=1,797, SM breakdown inferred)
    lbank_pct = [23.7, 35.6, 30.85, 39.81, 29.40]
    # HashKey HK target (% using platform, Section 2.2.1)
    hk_pct    = [72.1, 67.9, None, None, None]   # only measured for social + not others
    hk_plot   = [72.1, 67.9, 0, 0, 0]  # fill 0 for unmeasured

    x = np.arange(len(channels))
    w = 0.38

    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)

    b1 = ax.bar(x - w/2, lbank_pct, w, color=LB_YELLOW, edgecolor=LB_BLACK, lw=0.6, label="LBank (global, N=1,797)")
    b2 = ax.bar(x + w/2, hk_plot,   w, color=HK_BLUE,   edgecolor=LB_BLACK, lw=0.6, label="HashKey HK target (N=287)")

    for bar, val in zip(b1, lbank_pct):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f"{val:.1f}%", ha="center", va="bottom", fontsize=8)
    for bar, val, orig in zip(b2, hk_plot, hk_pct):
        if orig is not None:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                    f"{orig:.1f}%", ha="center", va="bottom", fontsize=8, color=WHITE,
                    fontweight="bold")
        else:
            ax.text(bar.get_x() + bar.get_width()/2, 2,
                    "N/M", ha="center", va="bottom", fontsize=7.5, color="#AAA", style="italic")

    ax.set_xticks(x)
    ax.set_xticklabels(channels, fontsize=9.5)
    ax.set_ylabel("% of respondents", fontsize=9.5)
    ax.set_title("Figure 2.3-C: Discovery Channel Overlap — LBank vs. HashKey HK Audience\n"
                 "(Same platforms, different messages)", fontsize=11, fontweight="bold",
                 color=LB_BLACK, pad=10)
    ax.set_ylim(0, 90)
    ax.legend(fontsize=9, framealpha=0)

    # Annotation
    ax.annotate("Both audiences live here\n→ channel parity, not channel gap",
                xy=(0.5, 70), fontsize=8.5, color="#E74C3C", ha="center",
                arrowprops=None, style="italic")
    ax.axvspan(-0.5, 1.5, alpha=0.06, color="#E74C3C", zorder=0)

    note = ("LBank SM breakdown: X 56.74% + TG 37.69% of total SM respondents (62.81%), inferred absolute %.\n"
            "HashKey HK: platform usage % from Section 2.2.1 media habits question. Official advertising & search not measured.\n"
            "N/M = not measured in HK survey.")
    fig.text(0.5, -0.04, note, ha="center", fontsize=7, color="#999", style="italic")

    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, "benchmark_discovery_overlap.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")


# ── Chart 4: User Profile Comparison (Investment + Tenure) ────────────────────
def chart_user_profile():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor(WHITE)
    fig.suptitle("Figure 2.3-D: User Profile Comparison — LBank Global vs. HashKey HK Target",
                 fontsize=11, fontweight="bold", color=LB_BLACK, y=1.02)

    # Investment scale
    inv_labels = ["<$1K/mo", "$1K–$2K", "$2K–$5K", "$5K–$10K", ">$10K"]
    lbank_inv  = [42.49, 27.59, 8.01, 12.47, 9.43]

    # HK survey: we captured experience years, not monthly investment
    # Use experience as proxy: 1-3 years = most common (43.2%), infer similar conservative pattern
    # We'll note this gap and show experience data instead
    hk_exp_labels = ["< 6 mo", "6mo–1yr", "1–3 yr", "3–5 yr", "> 5 yr"]
    hk_exp_vals   = [8.4, 12.5, 43.2, 24.6, 11.3]  # Section 2.2.1 inferred from 58.2% 18-24 / 43.2% 1-3yr

    # Left: Investment scale — LBank
    ax = axes[0]
    ax.set_facecolor(WHITE)
    bars = ax.bar(inv_labels, lbank_inv, color=LB_YELLOW, edgecolor=LB_BLACK, lw=0.6, width=0.6)
    for bar, val in zip(bars, lbank_inv):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f"{val:.1f}%", ha="center", va="bottom", fontsize=8.5)
    ax.set_title("LBank: Monthly Investment Distribution\n(N=1,972)", fontsize=9.5, fontweight="bold",
                 color=LB_BLACK)
    ax.set_ylabel("% of respondents")
    ax.set_ylim(0, 55)
    ax.tick_params(axis="x", labelsize=8.5)
    # Annotate conservative majority
    ax.annotate("70% invest\nunder $2K/mo", xy=(1, 27.59), xytext=(2.5, 40),
                fontsize=8, color="#E74C3C", arrowprops=dict(arrowstyle="->", color="#E74C3C"),
                fontweight="bold")
    ax.axvspan(-0.5, 1.5, alpha=0.1, color=LB_YELLOW, zorder=0)

    # Right: Platform tenure — LBank vs HK experience (side by side)
    ax2 = axes[1]
    ax2.set_facecolor(WHITE)
    tenure_labels = ["< 1 mo", "1–3 mo", "3–6 mo", "6–12 mo", "> 1 yr"]
    lbank_tenure  = [20.81, 13.36, 9.91, 13.63, 42.26]
    # HK data: % in each experience cohort mapped to comparable tenure brackets (proxy)
    # Not directly comparable; we'll plot LBank only and note HK's 15.7% licensed usage
    x = np.arange(len(tenure_labels))
    bars2 = ax2.bar(x, lbank_tenure, color=LB_YELLOW, edgecolor=LB_BLACK, lw=0.6, width=0.55)
    for bar, val in zip(bars2, lbank_tenure):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{val:.1f}%", ha="center", va="bottom", fontsize=8.5)
    ax2.set_xticks(x)
    ax2.set_xticklabels(tenure_labels, fontsize=8.5)
    ax2.set_title("LBank: Platform Retention by Tenure\n(N=1,797)  ← cf. HashKey: only 15.7% HK users on licensed exch.",
                  fontsize=9, fontweight="bold", color=LB_BLACK)
    ax2.set_ylabel("% of respondents")
    ax2.set_ylim(0, 55)
    ax2.annotate("42.26% retained\nbeyond 1 year\n(cultural stickiness)",
                 xy=(4, 42.26), xytext=(2.3, 48),
                 fontsize=8, color="#E74C3C",
                 arrowprops=dict(arrowstyle="->", color="#E74C3C"),
                 fontweight="bold")

    note = ("Sources: LBank User Research Report, Apr 2025 (N=1,751–1,972).\n"
            "HashKey HK comparison point: Section 2.2.1 survey — 15.7% HK respondents use licensed exchanges (N=287).")
    fig.text(0.5, -0.04, note, ha="center", fontsize=7, color="#999", style="italic")

    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, "benchmark_user_profile_compare.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")


if __name__ == "__main__":
    print("Generating Section 2.3 benchmark charts...")
    chart_brand_matrix()
    chart_motivation_compare()
    chart_discovery_overlap()
    chart_user_profile()
    print("Done. All 4 charts saved to outputs/")
