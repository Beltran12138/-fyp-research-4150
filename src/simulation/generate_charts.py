"""
Section 6 — Simulation Visualizations
Re-coding Trust | COMM4150 FYP | ZHAO Han (1155191400)

Generates 4 publication-quality figures from data/simulation/results.json.
Output: data/simulation/charts/fig6_1_*.png ... fig6_4_*.png

Usage:
    python src/simulation/generate_charts.py
"""

import json
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.gridspec as gridspec

matplotlib.rcParams['font.family'] = 'DejaVu Sans'
matplotlib.rcParams['axes.spines.top'] = False
matplotlib.rcParams['axes.spines.right'] = False

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
DATA_PATH = os.path.join(BASE_DIR, 'data', 'simulation', 'results.json')
OUT_DIR   = os.path.join(BASE_DIR, 'data', 'simulation', 'charts')
os.makedirs(OUT_DIR, exist_ok=True)

# ── Color palette (Safe Punk brand + accessible) ──────────────────────────────
C_PESSIMISTIC = '#6C757D'   # grey
C_BASE        = '#FF6B35'   # orange
C_OPTIMISTIC  = '#00D4FF'   # cyan
C_NATIVE      = '#FF2D78'   # pink
C_EXPLORER    = '#7B2FBE'   # purple
C_TARGET      = '#28A745'   # green (target line)
BG            = '#FAFAFA'
GRID          = '#E9ECEF'

# ── Load data ─────────────────────────────────────────────────────────────────
with open(DATA_PATH, encoding='utf-8') as f:
    data = json.load(f)

scenarios   = ['pessimistic', 'base', 'optimistic']
labels      = ['Pessimistic', 'Base', 'Optimistic']
colors      = [C_PESSIMISTIC, C_BASE, C_OPTIMISTIC]

# ─────────────────────────────────────────────────────────────────────────────
# Fig 6.1 — Agent Stance Evolution Across Rounds
# ─────────────────────────────────────────────────────────────────────────────
def fig_6_1():
    fig, ax = plt.subplots(figsize=(9, 5.5), facecolor=BG)
    ax.set_facecolor(BG)

    # initial mean stance: weighted avg of initial_stance params
    # 28 cultural_native (-0.25) + 32 cautious_explorer (0.05) = (28*-0.25+32*0.05)/60
    initial_mean = (28 * -0.25 + 32 * 0.05) / 60  # ≈ -0.09

    round_labels = ['Initial\n(Pre-launch)', 'Round 1\nRIB Launch\n+ Hero Film',
                    'Round 2\nConfession\n+ Persona Quiz',
                    'Round 3\nStill Here\n+ Countdown']
    x = [0, 1, 2, 3]

    for sc, label, color in zip(scenarios, labels, colors):
        rl = data[sc]['round_logs']
        stances = [initial_mean] + [r['agent_snapshot']['mean_stance'] for r in rl]
        ax.plot(x, stances, color=color, linewidth=2.5, marker='o',
                markersize=8, label=label, zorder=3)
        ax.fill_between(x, stances, initial_mean, alpha=0.07, color=color)

    # Target line (Gap Δ ≤ 1.75 requires stance > ~0.18)
    # stance_target = (2.52 - 1.75) / 4.2 + initial ≈ 0.09 (where gap formula inverts)
    ax.axhline(y=0.0, color='#ADB5BD', linewidth=0.8, linestyle='--', alpha=0.7)
    ax.axhline(y=0.183, color=C_TARGET, linewidth=1.2, linestyle=':', alpha=0.85,
               label='Min. stance for Δ ≤ 1.75')

    # Round boundary shading
    for xi in [0.5, 1.5, 2.5]:
        ax.axvline(xi, color=GRID, linewidth=0.8, zorder=1)

    ax.set_xticks(x)
    ax.set_xticklabels(round_labels, fontsize=9)
    ax.set_ylabel('Mean Agent Stance\n(−1 = hostile → +1 = advocate)', fontsize=10)
    ax.set_ylim(-0.25, 0.80)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
    ax.set_title('Fig 6.1 — Agent Brand Stance Evolution by Scenario',
                 fontsize=12, fontweight='bold', pad=12, loc='left')
    ax.legend(fontsize=9, framealpha=0.9, loc='upper left')
    ax.set_facecolor(BG)
    ax.yaxis.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'fig6_1_stance_evolution.png')
    plt.savefig(out, dpi=180, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'  Saved: {out}')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 6.2 — KPI Predictions: Three Scenarios
# ─────────────────────────────────────────────────────────────────────────────
def fig_6_2():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5), facecolor=BG)
    fig.suptitle('Fig 6.2 — Campaign KPI Predictions by Scenario',
                 fontsize=12, fontweight='bold', x=0.02, ha='left', y=1.01)

    # Left panel: count metrics
    ax1 = axes[0]
    ax1.set_facecolor(BG)
    metrics_count = {
        'RIB Submissions': [13500, 43392, 65250],
        '/confess Unique': [20270, 62522, 100140],
        'KYC Accounts':    [7982,  10001, 10001],
        'TG Members':      [10000, 10000, 10000],
    }
    x = np.arange(len(metrics_count))
    width = 0.25
    for i, (sc, label, color) in enumerate(zip(scenarios, labels, colors)):
        vals = [v[i] for v in metrics_count.values()]
        bars = ax1.bar(x + i*width, vals, width, label=label, color=color,
                       alpha=0.88, zorder=3, edgecolor='white', linewidth=0.5)
        for bar in bars:
            h = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, h + 500,
                     f'{h:,.0f}', ha='center', va='bottom', fontsize=6.5, color='#495057')

    # Campaign targets
    target_vals = [None, None, 10001, 5000]
    for xi, tv in zip(x, target_vals):
        if tv:
            ax1.hlines(tv, xi - 0.1, xi + 3*width + 0.1,
                       colors=C_TARGET, linewidths=1.5, linestyles='dashed', zorder=4)

    ax1.set_xticks(x + width)
    ax1.set_xticklabels(metrics_count.keys(), fontsize=9)
    ax1.set_ylabel('Count', fontsize=10)
    ax1.set_title('Community & Conversion Metrics', fontsize=10, pad=8)
    ax1.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda v, _: f'{int(v):,}'))
    ax1.legend(fontsize=9, framealpha=0.9)
    ax1.yaxis.grid(True, color=GRID, linewidth=0.6)
    ax1.set_axisbelow(True)

    # Right panel: brand health metrics
    ax2 = axes[1]
    ax2.set_facecolor(BG)

    gap_vals    = [1.63, 1.00, 1.00]
    boring_vals = [27.7, 18.9, 17.4]

    ax2_twin = ax2.twinx()
    xb = np.arange(3)
    b1 = ax2.bar(xb - 0.18, gap_vals, 0.35, label='Trust-Engagement Gap (Δ)',
                 color=colors, alpha=0.88, zorder=3, edgecolor='white')
    b2 = ax2_twin.bar(xb + 0.18, boring_vals, 0.35,
                      label='"Boring" Association (%)',
                      color=colors, alpha=0.45, hatch='//', zorder=3, edgecolor='white')

    # Target lines
    ax2.axhline(1.75, color=C_TARGET, linewidth=1.5, linestyle='dashed',
                label='Gap target (≤1.75)')
    ax2_twin.axhline(25.0, color='#FFC107', linewidth=1.5, linestyle='dashed',
                     label='"Boring" target (<25%)')

    for bar, v in zip(b1, gap_vals):
        ax2.text(bar.get_x() + bar.get_width()/2, v + 0.03,
                 f'Δ{v:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    for bar, v in zip(b2, boring_vals):
        ax2_twin.text(bar.get_x() + bar.get_width()/2, v + 0.3,
                      f'{v}%', ha='center', va='bottom', fontsize=9)

    ax2.set_xticks(xb)
    ax2.set_xticklabels(labels, fontsize=9)
    ax2.set_ylabel('Trust-Engagement Gap (Δ)', fontsize=10, color='#333')
    ax2_twin.set_ylabel('"Boring" Word Association (%)', fontsize=10, color='#555')
    ax2.set_ylim(0, 3.2)
    ax2_twin.set_ylim(0, 45)
    ax2.set_title('Brand Health Metrics (Jul 2026 Prediction)', fontsize=10, pad=8)
    ax2.yaxis.grid(True, color=GRID, linewidth=0.6)
    ax2.set_axisbelow(True)

    lines1, lbls1 = ax2.get_legend_handles_labels()
    lines2, lbls2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, lbls1 + lbls2, fontsize=8, framealpha=0.9, loc='upper right')

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'fig6_2_kpi_comparison.png')
    plt.savefig(out, dpi=180, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'  Saved: {out}')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 6.3 — Agent Behaviour Radar: Cultural Native vs Cautious Explorer (Base)
# ─────────────────────────────────────────────────────────────────────────────
def fig_6_3():
    categories = ['RIB Submission', '/confess', 'TG Joined', 'UGC Shared', 'KYC Completed']
    N = len(categories)

    native_vals   = [0.9643, 0.8929, 1.0000, 0.7857, 0.5000]
    explorer_vals = [0.9063, 0.8125, 1.0000, 0.7813, 0.5938]

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    native_vals   += native_vals[:1]
    explorer_vals += explorer_vals[:1]

    fig, ax = plt.subplots(figsize=(7, 6.5), subplot_kw=dict(polar=True), facecolor=BG)
    ax.set_facecolor(BG)

    ax.plot(angles, native_vals,   color=C_NATIVE,   linewidth=2.2, linestyle='solid', label='Cultural Native (Seg. A)')
    ax.fill(angles, native_vals,   color=C_NATIVE,   alpha=0.18)
    ax.plot(angles, explorer_vals, color=C_EXPLORER, linewidth=2.2, linestyle='solid', label='Cautious Explorer (Seg. B)')
    ax.fill(angles, explorer_vals, color=C_EXPLORER, alpha=0.18)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, fontweight='bold')
    ax.set_ylim(0, 1.05)
    ax.set_yticks([0.25, 0.50, 0.75, 1.00])
    ax.set_yticklabels(['25%', '50%', '75%', '100%'], fontsize=8, color='#6C757D')
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)

    ax.set_title('Fig 6.3 — Agent Behaviour Profile: Base Scenario\n'
                 'Cumulative engagement rates by end of simulation (N=60 agents)',
                 fontsize=11, fontweight='bold', pad=20)
    ax.legend(loc='lower right', bbox_to_anchor=(1.28, -0.08), fontsize=10, framealpha=0.9)

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'fig6_3_agent_radar.png')
    plt.savefig(out, dpi=180, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'  Saved: {out}')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 6.4 — KYC Conversion Probability Through Campaign Funnel
# ─────────────────────────────────────────────────────────────────────────────
def fig_6_4():
    """
    Shows how KYC conversion probability rises through the 3 rounds
    for both agent types, across all 3 scenarios.
    Validates Finding 4: KYC is a lagged funnel outcome.
    """
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), facecolor=BG,
                             sharey=True)
    fig.suptitle('Fig 6.4 — KYC Conversion Probability Across Campaign Rounds\n'
                 'Finding 4: Community formation (Rounds 1–2) precedes conversion (Round 3)',
                 fontsize=11, fontweight='bold', x=0.02, ha='left')

    round_x = [1, 2, 3]
    round_labels = ['R1\nRIB Launch\n+ Film', 'R2\nConfession\n+ Quiz', 'R3\nStill Here\n+ Countdown']

    agent_keys  = ['cultural_native',   'cautious_explorer']
    agent_names = ['Cultural Native (Segment A)', 'Cautious Explorer (Segment B)']
    agent_colors= [C_NATIVE, C_EXPLORER]

    for ax, akey, aname, acol in zip(axes, agent_keys, agent_names, agent_colors):
        ax.set_facecolor(BG)
        for sc, slabel, scolor in zip(scenarios, labels, colors):
            rl = data[sc]['round_logs']
            kyc_probs = [r['reactions'][akey]['kyc_conversion_probability'] for r in rl]
            ls = '-' if sc == 'base' else ('--' if sc == 'optimistic' else ':')
            lw = 2.5 if sc == 'base' else 1.8
            ax.plot(round_x, kyc_probs, color=scolor, linewidth=lw,
                    linestyle=ls, marker='D', markersize=7,
                    label=slabel, zorder=3)
            for xi, yv in zip(round_x, kyc_probs):
                ax.annotate(f'{yv:.0%}', (xi, yv),
                            textcoords='offset points', xytext=(0, 8),
                            ha='center', fontsize=8, color=scolor)

        ax.set_xticks(round_x)
        ax.set_xticklabels(round_labels, fontsize=9)
        ax.set_ylabel('KYC Conversion Probability', fontsize=10)
        ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(xmax=1.0))
        ax.set_ylim(0, 0.55)
        ax.set_title(aname, fontsize=10, fontweight='bold', pad=8)
        ax.legend(fontsize=9, framealpha=0.9)
        ax.yaxis.grid(True, color=GRID, linewidth=0.6)
        ax.set_axisbelow(True)

        # Shade R3 as conversion phase
        ax.axvspan(2.5, 3.5, alpha=0.06, color=C_TARGET, zorder=0, label='_nolegend_')
        ax.text(3, 0.02, 'Conversion\nphase', ha='center', fontsize=7.5,
                color=C_TARGET, style='italic')

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'fig6_4_kyc_funnel.png')
    plt.savefig(out, dpi=180, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f'  Saved: {out}')


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Generating Section 6 figures...')
    fig_6_1()
    fig_6_2()
    fig_6_3()
    fig_6_4()
    print(f'\nAll figures saved to: {OUT_DIR}')
    print('Figures: fig6_1_stance_evolution.png  fig6_2_kpi_comparison.png')
    print('         fig6_3_agent_radar.png        fig6_4_kyc_funnel.png')
