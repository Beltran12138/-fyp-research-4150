# Section 6 — Pre-Launch Predictive Simulation

**COMM4150 FYP: Re-coding Trust | ZHAO Han (1155191400) | CUHK**

> *A multi-agent opinion dynamics simulation of the "Re-coding Trust" campaign, inspired by the MiroFish / OASIS (CAMEL-AI) framework.*

---

## Overview

This simulation models how 60 autonomous AI agents — calibrated against survey data (N=287) from Hong Kong crypto-engaged users aged 18–35 — respond to the campaign's three primary stimuli across three environmental scenarios. DeepSeek-V3 serves as the agent reasoning engine.

**Research question:** Will the "Re-coding Trust" campaign mechanics (RIB memorial wall, Dark Chapter Confession, "Still Here" counter-thread) generate the community dynamics they are designed to produce?

---

## Methodology

| Parameter | Value |
|---|---|
| Framework | OASIS (CAMEL-AI, 2026) — lightweight implementation |
| Reasoning engine | DeepSeek-V3 (`deepseek-chat`) |
| Agents | 60 (28 Cultural Natives + 32 Cautious Explorers) |
| Scenarios | 3 (Pessimistic / Base / Optimistic) |
| Simulation rounds | 3 (per scenario) |
| API calls | 18 total (2 agent types × 3 scenarios × 3 rounds) |
| Random seed | 4150 |
| Run date | 26 April 2026 |

### Agent Types

| Type | Count | Initial Stance | Degen Score | RAVE-affected |
|---|---|---|---|---|
| Cultural Native (Segment A) | 28 | −0.25 (±noise) | 0.82 | 18% |
| Cautious Explorer (Segment B) | 32 | +0.05 (±noise) | 0.41 | 12% |

### Stimulus Rounds

| Round | Stimulus |
|---|---|
| 1 | RIB Thread Launch + Hero Film (no paid promotion) |
| 2 | Dark Chapter Confession + Pizza Personas Quiz |
| 3 | "Still Here" Counter-Thread + Airdrop Countdown |

---

## Key Results (Base Scenario)

| Metric | Pessimistic | Base | Optimistic |
|---|---|---|---|
| RIB Submissions | 13,500 | 43,392 | 65,250 |
| /confess Unique | 20,270 | 62,522 | 100,140 |
| KYC Accounts | 7,982 | 10,001* | 10,001* |
| Trust-Engagement Gap (Δ) | 1.63 | 1.00 | 1.00 |
| "Boring" Association | 27.7% | 18.9% | 17.4% |

*Campaign objective cap (10,001) reached — capacity constraint, not demand constraint.

**Primary objective (Δ ≤ 1.75):** Met in Base and Pessimistic scenarios.

---

## Simulation Output

- **Raw results:** [`data/simulation/results.json`](../../data/simulation/results.json)
- **Summary table:** [`data/simulation/summary.txt`](../../data/simulation/summary.txt)

### Figures

| Figure | Description |
|---|---|
| [Fig 6.1](../../data/simulation/charts/fig6_1_stance_evolution.png) | Agent brand stance evolution by scenario (Round 0→3) |
| [Fig 6.2](../../data/simulation/charts/fig6_2_kpi_comparison.png) | Campaign KPI predictions by scenario |
| [Fig 6.3](../../data/simulation/charts/fig6_3_agent_radar.png) | Agent behaviour profile: Cultural Native vs Cautious Explorer (Base) |
| [Fig 6.4](../../data/simulation/charts/fig6_4_kyc_funnel.png) | KYC conversion probability across campaign rounds |

---

## Reproduction

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set DeepSeek API key
export DEEPSEEK_API_KEY=sk-xxxx      # macOS/Linux
set DEEPSEEK_API_KEY=sk-xxxx         # Windows

# 3. Run simulation (~3 minutes, ~HK$3 API cost)
python src/simulation/campaign_sim.py

# 4. Generate charts
python src/simulation/generate_charts.py
```

Output saved to `data/simulation/`.

---

## Four Key Findings

1. **RAVE topicality: 5× amplifier** — RIB submission probability: 0.15 (pessimistic, salience=0.2) vs 0.75 (base, salience=0.65) in Round 1.

2. **Confession mechanic: 3× engagement depth** — Cautious Explorer engagement_depth: 1 (Round 1, standard) → 3 (Round 2, /confess).

3. **"Still Here" at-peak timing validated** — Round 3 produced largest single-round attitude shift in all scenarios (base: +0.240 vs Round 2's +0.151).

4. **KYC is lagged funnel outcome** — Cautious Explorer KYC probability: 0.25 (R1) → 0.20 (R2) → 0.38 (R3). Community formation precedes conversion.

---

## Limitations

- 60 agents (vs. MiroFish's 1M) — population scaling uses linear projection
- DeepSeek-V3 roleplay ≠ true social network dynamics
- TG membership cap (10,000) reached in all scenarios — directional, not precise
- RAVE crash and all environmental conditions frozen at April 2026

---

## References

- CAMEL-AI. (2026). OASIS: Open Agent Social Interaction Simulations. https://github.com/camel-ai/oasis
- MiroFish. (2026). MiroFish: AI swarm intelligence prediction engine. https://mirofish.ink/
- Gao, C., et al. (2024). OASIS: Open agent social interaction simulations with one million agents. arXiv:2411.11581.

---

*Section 6 | ZHAO Han (1155191400) | CUHK COMM4150 | Supervisor: Prof. Donna Chu*
