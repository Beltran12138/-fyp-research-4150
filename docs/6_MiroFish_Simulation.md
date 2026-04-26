# Section 6 — Pre-Launch Predictive Simulation (MiroFish)
## COMM4150 FYP: Re-coding Trust | ZHAO Han (1155191400)

---

## 6.1 Rationale: Simulation as Pre-Launch Research

Campaign planning conventionally relies on historical analogues, survey-based concept testing, and expert judgement to forecast how a proposed strategy will perform in the market. Each method carries a structural limitation: historical analogues assume static environmental conditions; survey respondents self-report hypothetical behaviour rather than demonstrating actual social dynamics; expert judgement is subject to cognitive biases toward confirming the strategy already designed. For a campaign whose core mechanics — a community-built memorial wall, a confession-based Telegram community, a single "Still Here" counter-post — depend on emergent audience behaviour rather than controlled brand broadcasting, these conventional validation methods are insufficient. The campaign's success is contingent not on whether individual respondents say they would participate, but on whether a social system of sufficiently high density and emotional resonance can form within the target community.

To address this, a pre-launch predictive simulation was conducted using **MiroFish** as the methodological framework — a multi-agent swarm intelligence simulation engine launched in March 2026 that applies the OASIS (Open Agent Social Interaction Simulations) framework developed by CAMEL-AI (MiroFish, 2026; CAMEL-AI, 2026). MiroFish spawns thousands of autonomous AI agents, each assigned a unique personality profile, social history, initial stance, and peer network, then observes the emergent social dynamics — opinion shifts, coalition formation, viral diffusion — that arise when these agents interact across simulated social environments. Since its release, MiroFish has been applied to financial forecasting, PR crisis scenario planning, and policy reception testing.

Due to the closed nature of the full MiroFish platform at the time of research, the simulation was implemented as a purpose-built lightweight equivalent: a 60-agent Python model using DeepSeek-V3 (deepseek-chat) as the agent reasoning engine, calibrated against the same OASIS methodology principles — multi-agent opinion dynamics, structured round-based stimulus introduction, and population-scaled output projection. The simulation ran on 26 April 2026 (seed: 4150) and produced the results reported in this section. The source code is archived at `src/simulation/campaign_sim.py`; raw output at `data/simulation/results.json`.

The specific question being tested: will the "Re-coding Trust" campaign mechanics generate the community dynamics they are designed to produce — and under what environmental conditions does the campaign fail to reach its primary objectives?

---

## 6.2 Simulation Setup

### 6.2.1 Seed Material

The simulation was seeded with four document inputs, which informed agent persona calibration and scenario condition parameters:

| Input | Content | Purpose |
|---|---|---|
| Survey dataset summary | N=287, key findings from Section 2.2.4 | Calibrate agent attitude distributions (Trust M=5.27, Relatability M=2.75, platform usage, barrier profile) |
| Computational social listening output | Section 2.1 NLP results: pain point clusters, Pizza Day sentiment anomaly, KOL influence matrix | Seed agent vocabulary, friction patterns, and network topology |
| RaveDAO (RAVE) incident report | April 2026: 95% crash, $6B market cap wiped, ZachXBT investigation | Inject topical environmental condition active four weeks before Pizza Day |
| Campaign brief | Safe Punk positioning, RIB concept, Dark Chapter mechanic, airdrop structure | Define the stimulus agents would encounter |

### 6.2.2 Agent Persona Distribution

From the seed material, 60 simulation agents were constructed and scaled to a target population of 100,000 HK crypto-engaged users aged 18–35, distributed across the two target segments:

| Agent Type | Simulation Count | Population Equivalent | Behavioural Profile |
|---|---|---|---|
| Cultural Natives (Segment A) | 28 (47%) | 45,000 | High degen fluency; offshore platform preference; airdrop FOMO susceptibility; active CT quoters; initial Trust=5.2/7, Relatability=2.3/7 |
| Cautious Explorers (Segment B) | 32 (53%) | 55,000 | Financial-independence motivation; social proof dependence; KOL-influenced; event-conversion susceptible; initial Trust=5.4/7, Relatability=3.1/7 |
| RAVE-affected agents (cross-segment overlay) | 18% Cultural Native / 12% Cautious Explorer | ~9,900 | Recent financial loss from RAVE crash; elevated trauma salience; heightened RIB resonance (1.3× probability multiplier applied) |

### 6.2.3 Simulation Structure

Agents progressed through three sequential stimulus rounds representing the campaign's primary activation sequence, with each round evaluated by DeepSeek-V3 reasoning per agent type:

| Round | Stimulus | Campaign Phase |
|---|---|---|
| 1 | RIB Thread Launch + Hero Film (no paid promotion) | Phase 1 launch |
| 2 | Dark Chapter Confession Mechanic + Pizza Personas Quiz | Phase 1 community formation |
| 3 | "Still Here" Counter-Thread + Airdrop Countdown (10,001 scarcity mechanic) | Phase 1–2 transition |

Three scenario conditions were run, varying two key input variables: **RIB community uptake rate** (tombstones submitted in the first 72 hours) and **RAVE topicality coefficient** (the degree to which the RaveDAO crash remained salient in agent memory).

---

## 6.3 Scenario Predictions

The following outputs were generated by the simulation (run: 26 April 2026, seed: 4150, model: deepseek-chat):

| Metric | Pessimistic | Base | Optimistic |
|---|---|---|---|
| *Inputs* | | | |
| RIB tombstones (first 72h) | 40 | 180 | 420 |
| RAVE topicality window | 1 week | 3 weeks | 5+ weeks |
| *Predicted Outputs* | | | |
| @HashKey0xU members by May 22 | 10,000‡ | 10,000‡ | 10,000‡ |
| Total RIB community submissions | 13,500 | 43,392 | 65,250 |
| /confess unique submissions | 20,270 | 62,522 | 100,140 |
| KYC-completed airdrop accounts | 7,982 | 10,001* | 10,001* |
| Trust-Engagement Gap (Δ), Jul 2026 | 1.63 | 1.00 | 1.00 |
| "Boring" word association, Jul 2026 | 27.7% | 18.9% | 17.4% |

*Airdrop cap of 10,001 reached in Base and Optimistic; capacity constraint, not demand constraint.

‡Telegram community channel membership demand exceeded the simulation ceiling (10,000) in all three scenarios. The discriminating metric between scenarios is therefore confession submissions and KYC conversion rate, not channel membership. Even in the Pessimistic scenario, underlying TG join demand among agents exceeded the ceiling, suggesting the 5,000-member objective (Section 4.4.4) is achievable across all scenario conditions.

**Fig 6.1** plots the mean agent stance trajectory across all four time points (Initial → Round 3) for each scenario. **Fig 6.2** visualises the six KPI predictions side-by-side. Both figures are generated directly from `data/simulation/results.json`; source code at `src/simulation/generate_charts.py`.

The Base scenario — defined as the most probable given current environmental conditions — predicts that the primary campaign objective (Gap Δ ≤ 1.75) falls within achievable range under both Base and Pessimistic conditions. The Pessimistic scenario produces Gap Δ = 1.63, which meets the primary objective but misses the "Boring" association target of <25% (27.7% predicted). The Base scenario produces Gap Δ = 1.00 and Boring = 18.9%, exceeding all primary targets. KYC conversion distinguishes scenarios most sharply: 7,982 accounts (Pessimistic) versus the 10,001 cap (Base/Optimistic).

---

## 6.4 Key Findings and Campaign Design Implications

The simulation produced four findings derived from observed agent behaviour across rounds and scenarios:

**Finding 1 — RAVE topicality is a 5× amplifier for Phase 1 seeding.**

Under Pessimistic conditions (RAVE salience = 0.2), Cultural Native agents' RIB submission probability in Round 1 was 0.15 and initial stance change was −0.05 (net negative — the campaign's early stimulus produced mild resistance, not engagement, without RAVE's emotional context). Under Base conditions (salience = 0.65), the same agents showed rib_submission_probability = 0.75 and stance_change = +0.15 in Round 1 — a 5.0× differential in submission intent attributable entirely to RAVE topicality. At population scale, this differential produces 13,500 (Pessimistic) versus 43,392 (Base) total RIB submissions — a 3.2× gap. The decision to launch the RIB thread in early February 2026, before the RAVE crash memory fades, is therefore not a preference but a structural launch-timing constraint.

**Fig 6.3** (radar chart) shows the cumulative engagement profile of both agent types in the Base scenario across all five behavioural dimensions. The near-identical area covered by both segments indicates that under Base conditions, campaign mechanics successfully bridge the cultural gap between Cultural Natives and Cautious Explorers.

**Finding 2 — Confession mechanic produces 3.0× engagement depth over standard community onboarding.**

In the Pessimistic scenario (weakest campaign conditions), Cautious Explorer agents showed engagement_depth = 1 in Round 1 (standard RIB launch) and engagement_depth = 3 in Round 2 (Dark Chapter Confession + Persona Quiz) — a 3.0× increase. Under Base conditions, the confession round sustained engagement_depth = 4 for Cultural Natives and 3 for Cautious Explorers; the post-Round 2 agent snapshot shows TG community membership rising from 75.0% to 96.7% of agents — a 29-percentage-point gain driven by the confession mechanic rather than broadcast outreach. Agents with RAVE-affected memory profiles (rave_boost = 1.3×) showed the highest engagement persistence. This finding validates the Dark Chapter Confession mechanic (Section 5.6) as the campaign's primary community formation engine: emotional resonance, not informational content, produces the depth of engagement that converts passive followers into active community members.

**Finding 3 — "Still Here" counter-thread timing: Round 3 produced the largest single-round attitude shift across all scenarios.**

Across all three scenario conditions, Round 3 (Still Here counter-thread + airdrop countdown) consistently produced the largest single-round stance movement:

| Scenario | Round 2 stance Δ | Round 3 stance Δ | Ratio |
|---|---|---|---|
| Pessimistic | +0.080 | +0.141 | 1.76× |
| Base | +0.151 | +0.240 | 1.59× |
| Optimistic | +0.177 | +0.288 | 1.63× |

The simulation's reasoning for the Cautious Explorer agent in Round 3 (Base): *"The agent's high trust in HashKey's reliability and the scarcity-driven airdrop incentive outweigh KYC complexity concerns, but social proof from the RIB wave and KOL partnerships is needed to push them past the barrier."* This reasoning encodes the at-peak reveal logic: the memorial wall's accumulated emotional investment creates the credibility context that makes the "Still Here" statement most resonant. The finding confirms the strategic decision to withhold the counter-post until peak organic RIB engagement rather than launching it simultaneously with the thread.

**Fig 6.4** plots KYC conversion probability across rounds for both agent types and all three scenarios. Note: in the Pessimistic scenario, Cautious Explorer KYC probability dips slightly in Round 3 (0.15 → 0.10) before recovering — indicating that under low-RAVE-salience conditions the "Still Here" + airdrop stimulus alone is insufficient to overcome fee and KYC complexity barriers without the social proof built in Round 2. This finding strengthens the case for community formation preceding conversion.

**Finding 4 — KYC conversion is a lagged funnel outcome, not a launch-phase metric.**

KYC conversion probability followed a consistent upward trajectory through the three rounds, peaking in Round 3 when the airdrop scarcity mechanic activated:

| Agent type | Round 1 KYC probability | Round 2 KYC probability | Round 3 KYC probability |
|---|---|---|---|
| Cultural Native (Base) | 0.10 | 0.20 | 0.25 |
| Cautious Explorer (Base) | 0.25 | 0.20 | **0.38** (peak) |

The Cautious Explorer KYC peak at Round 3 (+0.38) — the highest of any agent-type/round combination — was driven by the "10,001 slices" scarcity mechanic working in conjunction with accumulated community social proof from Rounds 1–2. This validates the three-stage funnel design: community formation (Rounds 1–2) must precede conversion mechanics (Round 3) to maximise KYC yield. A campaign that launched the airdrop CTA in Round 1 — before community belonging was established — would produce sub-0.10 KYC conversion against agents who had not yet formed attachment to the memorial wall community.

---

## 6.5 Simulation Limitations

Three structural constraints bound this simulation's predictive power:

**Agent calibration accuracy.** Agent personas are generated from the survey dataset (N=287) and social listening output (Section 2.1). The survey employs purposive sampling and is not population-representative; agent distributions therefore reflect the demographic profile of the sample, not the full HK crypto community. Scenarios may over-represent 18–24 Cultural Natives relative to the actual population.

**Population scaling methodology.** The simulation treats a target population of 100,000 HK crypto-engaged users as uniformly reachable through the campaign's channels. This overestimates organic reach penetration: real-world frictions — content discovery, scroll-past behaviour, network concentration effects — would reduce absolute counts while preserving the ratio relationships between scenarios. The Telegram membership ceiling (10,000) was reached in all scenarios due to high underlying join propensities in the agent model; this should be read as directional (the membership objective is achievable across all conditions) rather than as a precise forecast.

**Environmental unpredictability.** The simulation encodes known environmental conditions as of April 2026 (RAVE crash, BTC price trajectory, SFC licensing landscape). Any material market event between simulation date and campaign launch (May 22) not encoded in the seed material falls outside the model's prediction boundary. The simulation is a plan validation tool, not a real-time forecast.

Despite these constraints, the simulation's primary contribution is scenario architecture: the identification of the mechanisms most sensitive to variation (RAVE topicality decay rate, /confess engagement depth, "Still Here" reveal timing) and the quantification of which design decisions are load-bearing versus peripheral. Findings 1 and 3 — RAVE-dependent launch timing and the at-peak counter-post reveal — represent structural commitments with high simulation confidence that have been incorporated into the campaign architecture as non-negotiable timing constraints. Finding 4 validates that the campaign's three-stage funnel sequence is correct: community before KYC, not KYC at launch.

---

*Sources: CAMEL-AI. (2026). OASIS: Open agent social interaction simulations. https://github.com/camel-ai/oasis; MiroFish. (2026). MiroFish: AI swarm intelligence prediction engine. https://mirofish.ink/; Agent Native. (2026, March). MiroFish: Swarm-intelligence with 1M agents that can predict everything. Medium. https://agentnativedev.medium.com/mirofish-swarm-intelligence-with-1m-agents-that-can-predict-everything-114296323663; Beitroot. (2026). MiroFish: Open source AI simulation engine for prediction and forecasting. https://www.beitroot.co/blog/mirofish-open-source-swarm-intelligence-engine; Campaign simulation source: src/simulation/campaign_sim.py (run: 26 April 2026, seed 4150, model: deepseek-chat); Raw output: data/simulation/results.json; Section 2.1 (computational social listening); Section 2.2.4 (survey data); Section 4.4 (campaign objectives); Section 5.6 (social content series).*

*Section 6 | ZHAO Han (1155191400) | CUHK COMM4150 | Supervisor: Prof. Donna Chu*
