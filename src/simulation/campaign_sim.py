"""
MiroFish-Inspired Campaign Simulation — COMM4150 FYP: Re-coding Trust
======================================================================
Pre-launch predictive simulation for the "Re-coding Trust" / Safe Punk campaign.
Applies a lightweight multi-agent opinion dynamics model using DeepSeek-V3 as
the agent reasoning engine, inspired by the MiroFish / OASIS framework.

Methodology:
  - 60 agents distributed across 2 target segments + RAVE-affected overlay
  - 3 scenarios (Pessimistic / Base / Optimistic) × 3 simulation rounds
  - Each round: DeepSeek evaluates agent-type reactions to campaign stimuli
  - Output: opinion shift, engagement rates, predicted KPI ranges

Usage:
    export DEEPSEEK_API_KEY=sk-xxxx
    python src/simulation/campaign_sim.py

Output:
    data/simulation/results.json
    data/simulation/summary.txt

Section 6 | ZHAO Han (1155191400) | CUHK COMM4150
"""

import os
import json
import time
import random
import sys
from datetime import datetime
from openai import OpenAI

# ── Configuration ────────────────────────────────────────────────────────────

API_KEY    = os.getenv("DEEPSEEK_API_KEY", "")
BASE_URL   = "https://api.deepseek.com"
MODEL      = "deepseek-chat"
RANDOM_SEED = 4150  # reproducibility — matches survey seed

random.seed(RANDOM_SEED)

# ── Agent Type Definitions (calibrated from Section 2.2.4 survey data) ───────

AGENT_TYPES = {
    "cultural_native": {
        "count": 28,
        "description": (
            "Age 18-24 HK crypto user. Uses offshore exchanges (Binance/OKX). "
            "Primary driver: speculation and community. Holds BTC/ETH + memecoins. "
            "Telegram and Twitter-first. Degen identity core to self-concept. "
            "Associates HashKey with 'Reliable' AND 'Boring' simultaneously. "
            "Trust score for HashKey: 5.2/7. Relatability: 2.3/7. "
            "Top barrier to licensed exchange: Lack of degen culture (33.8%). "
            "Preferred incentive: exclusive airdrop (45.6%). "
            "Pizza Day awareness: 72.5%."
        ),
        "initial_stance": -0.25,   # slightly negative toward HashKey culturally
        "degen_score": 0.82,
        "rave_affected_share": 0.18,
    },
    "cautious_explorer": {
        "count": 32,
        "description": (
            "Age 22-30 HK crypto user. Uses offshore exchanges but less culturally "
            "committed. Primary driver: financial independence (45.3%). "
            "Holds BTC/ETH + stablecoins. Watches KOLs on YouTube and Telegram. "
            "Has explored HashKey KYC but not completed it. "
            "Associates HashKey with 'Reliable' and 'Safe'. Trust: 5.4/7. "
            "Relatability: 3.1/7. Relies on social proof before switching. "
            "Top barriers: complex KYC (27.5%), high fees (21.6%). "
            "Preferred incentive: airdrop + fee rebate combo. "
            "Pizza Day awareness: 63%."
        ),
        "initial_stance": 0.05,    # slightly positive but uncommitted
        "degen_score": 0.41,
        "rave_affected_share": 0.12,
    },
}

# ── Scenario Definitions ──────────────────────────────────────────────────────

SCENARIOS = {
    "pessimistic": {
        "label": "Pessimistic",
        "rib_seed_72h": 40,           # tombstones in first 72h
        "rave_salience": 0.2,         # RAVE crash memory fades fast (0–1)
        "kol_reach_multiplier": 0.6,
        "description": (
            "RaveDAO (RAVE) crash topicality fades within 1 week. "
            "RIB thread gets moderate CT engagement but low tombstone submissions. "
            "KOL activation underperforms. Telegram community grows slowly. "
            "No major crypto incident amplifies the graveyard narrative."
        ),
    },
    "base": {
        "label": "Base",
        "rib_seed_72h": 180,
        "rave_salience": 0.65,
        "kol_reach_multiplier": 1.0,
        "description": (
            "RaveDAO crash remains culturally salient for ~3 weeks post-launch. "
            "RIB thread achieves moderate CT spread; community actively submits tombstones. "
            "KOL partnerships perform as planned. Telegram community reaches target. "
            "Safe Punk concept resonates with Cultural Natives as predicted."
        ),
    },
    "optimistic": {
        "label": "Optimistic",
        "rib_seed_72h": 420,
        "rave_salience": 0.90,
        "kol_reach_multiplier": 1.45,
        "description": (
            "RAVE crash triggers sustained community anger for 5+ weeks. "
            "RIB thread goes viral on CT; multiple high-follower accounts amplify. "
            "KOL activation exceeds projections. Telegram community achieves viral threshold. "
            "Pizza Personas quiz spreads organically beyond crypto-native communities."
        ),
    },
}

# ── Campaign Stimuli (per round) ──────────────────────────────────────────────

STIMULI = [
    {
        "round": 1,
        "name": "RIB Launch + Hero Film",
        "description": (
            "HashKey launches the Rest in Blockchain memorial wall on X/Twitter. "
            "Tweet: 'We're building a memorial wall. Reply with any crypto exchange, "
            "protocol, or fund that no longer exists. We'll add the tombstone.' "
            "Hero Film (60s graveyard–survival essay, Still DRE BGM) published simultaneously. "
            "RIB microsite live. Laszlo Bot deployed. No paid promotion."
        ),
    },
    {
        "round": 2,
        "name": "Dark Chapter Confession + Persona Quiz",
        "description": (
            "Telegram @HashKey0xU channel launches with Dark Chapter Confession mechanic. "
            "Users DM @hsk_laszlobot with /confess to share darkest crypto moment. "
            "Pizza Personas quiz live. SBTI-style sharing mechanic. "
            "RIB wall has accumulated 200+ community tombstones at this point. "
            "14-day countdown begins on X/Twitter with daily provocations."
        ),
    },
    {
        "round": 3,
        "name": "Still Here Counter-Thread + Pizza Day Countdown",
        "description": (
            "At peak RIB engagement, @HashKeyExchange drops single counter-reply: "
            "'Still here. SFC Type 1 + Type 7. HashKey Exchange, 2018–'. "
            "D-7 to D-0 countdown posts. Airdrop scarcity mechanic activated: "
            "'10,001 slices. After that: it's history.' "
            "Physical event (Central HK, May 22) promoted via OOH and TG channel."
        ),
    },
]

# ── DeepSeek API Client ───────────────────────────────────────────────────────

def get_client():
    if not API_KEY:
        print("ERROR: Set DEEPSEEK_API_KEY environment variable.")
        sys.exit(1)
    return OpenAI(api_key=API_KEY, base_url=BASE_URL)

# ── Core Simulation: Agent-Type Reaction Evaluation ──────────────────────────

def evaluate_agent_reaction(client, agent_type_name, agent_type, scenario, stimulus):
    """
    Single DeepSeek call: evaluate how this agent type reacts to the stimulus
    under the given scenario conditions. Returns structured reaction metrics.
    """

    prompt = f"""You are simulating a Hong Kong crypto community member's reaction
to a marketing campaign stimulus. Respond ONLY with a valid JSON object.

AGENT PROFILE:
{agent_type['description']}

SCENARIO CONTEXT:
{scenario['description']}
RAVE crash salience level: {scenario['rave_salience']} (0=forgotten, 1=top of mind)
RIB tombstone submissions so far: {scenario['rib_seed_72h']}

CAMPAIGN STIMULUS THIS ROUND:
{stimulus['description']}

Evaluate this agent's reaction. Return ONLY this JSON structure with no markdown:
{{
  "rib_submission_probability": <float 0-1, probability this agent submits a tombstone>,
  "confession_probability": <float 0-1, probability this agent uses /confess on Telegram>,
  "tg_join_probability": <float 0-1, probability this agent joins @HashKey0xU>,
  "ugc_share_probability": <float 0-1, probability this agent shares Persona quiz screenshot>,
  "kyc_conversion_probability": <float 0-1, probability this agent completes KYC on HashKey>,
  "stance_change": <float -0.3 to +0.5, change in attitude toward HashKey brand>,
  "engagement_depth": <int 1-5, how deeply this agent engages with the content>,
  "reasoning": "<one sentence explaining the dominant factor driving this agent's reaction>"
}}"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=300,
        )
        raw = response.choices[0].message.content.strip()
        # strip markdown code fences if present
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        return json.loads(raw)
    except Exception as e:
        print(f"  API error ({agent_type_name}, round {stimulus['round']}): {e}")
        return None

# ── Simulation Runner ─────────────────────────────────────────────────────────

def run_scenario(client, scenario_name, scenario):
    print(f"\n{'='*60}")
    print(f"  SCENARIO: {scenario['label'].upper()}")
    print(f"{'='*60}")

    # initialise per-agent state
    agents = []
    for atype_name, atype in AGENT_TYPES.items():
        for i in range(atype["count"]):
            is_rave = random.random() < atype["rave_affected_share"]
            agents.append({
                "id": f"{atype_name}_{i}",
                "type": atype_name,
                "stance": atype["initial_stance"] + random.gauss(0, 0.08),
                "rave_affected": is_rave,
                "rib_submitted": False,
                "confessed": False,
                "tg_joined": False,
                "ugc_shared": False,
                "kyc_completed": False,
                "engagement_total": 0,
            })

    round_logs = []

    for stimulus in STIMULI:
        print(f"\n  Round {stimulus['round']}: {stimulus['name']}")
        round_reactions = {}

        for atype_name in AGENT_TYPES:
            print(f"    Evaluating {atype_name}...", end=" ", flush=True)
            reaction = evaluate_agent_reaction(
                client,
                atype_name,
                AGENT_TYPES[atype_name],
                scenario,
                stimulus
            )
            if reaction:
                round_reactions[atype_name] = reaction
                print(f"stance_change={reaction['stance_change']:+.3f}  "
                      f"rib_p={reaction['rib_submission_probability']:.2f}  "
                      f"kyc_p={reaction['kyc_conversion_probability']:.2f}")
                print(f"      → {reaction['reasoning']}")
            else:
                print("FAILED — using fallback values")
                round_reactions[atype_name] = {
                    "rib_submission_probability": 0.05,
                    "confession_probability": 0.04,
                    "tg_join_probability": 0.06,
                    "ugc_share_probability": 0.08,
                    "kyc_conversion_probability": 0.03,
                    "stance_change": 0.0,
                    "engagement_depth": 1,
                    "reasoning": "fallback"
                }

            time.sleep(0.5)  # rate limiting

        # apply reactions to individual agents with noise
        for agent in agents:
            r = round_reactions[agent["type"]]
            noise = lambda: random.gauss(0, 0.05)
            rave_boost = 1.3 if agent["rave_affected"] else 1.0

            if not agent["rib_submitted"] and random.random() < min(1.0, r["rib_submission_probability"] * rave_boost + noise()):
                agent["rib_submitted"] = True
            if not agent["confessed"] and random.random() < min(1.0, r["confession_probability"] * rave_boost + noise()):
                agent["confessed"] = True
            if not agent["tg_joined"] and random.random() < min(1.0, r["tg_join_probability"] + noise()):
                agent["tg_joined"] = True
            if not agent["ugc_shared"] and random.random() < min(1.0, r["ugc_share_probability"] + noise()):
                agent["ugc_shared"] = True
            if not agent["kyc_completed"] and random.random() < min(1.0, r["kyc_conversion_probability"] + noise()):
                agent["kyc_completed"] = True

            stance_delta = r["stance_change"] * rave_boost + random.gauss(0, 0.04)
            agent["stance"] = max(-1.0, min(1.0, agent["stance"] + stance_delta))
            agent["engagement_total"] += r["engagement_depth"]

        round_logs.append({
            "round": stimulus["round"],
            "stimulus": stimulus["name"],
            "reactions": round_reactions,
            "agent_snapshot": {
                "mean_stance": sum(a["stance"] for a in agents) / len(agents),
                "rib_submitted_pct": sum(1 for a in agents if a["rib_submitted"]) / len(agents),
                "tg_joined_pct": sum(1 for a in agents if a["tg_joined"]) / len(agents),
                "kyc_pct": sum(1 for a in agents if a["kyc_completed"]) / len(agents),
            }
        })

    # ── Scale to real-world population ───────────────────────────────────────
    # Estimated HK crypto-engaged 18-35 population: 100,000
    # Cultural Natives: 45% = 45,000 | Cautious Explorers: 55% = 55,000
    POP_TOTAL      = 100_000
    POP_NATIVE     = 45_000
    POP_EXPLORER   = 55_000

    final_rates = {
        atype: {
            metric: sum(a[metric.replace("_pct", "_submitted") if "rib" in metric
                       else metric.replace("_pct", "_joined") if "tg" in metric
                       else metric.replace("_pct", "_completed") if "kyc" in metric
                       else metric.replace("_pct", "_shared") if "ugc" in metric
                       else "confessed"] for a in agents if a["type"] == atype) / AGENT_TYPES[atype]["count"]
            for metric in ["rib_submitted", "confessed", "tg_joined", "ugc_shared", "kyc_completed"]
        }
        for atype in AGENT_TYPES
    }

    tg_members = min(
        10_000,
        int((final_rates["cultural_native"]["tg_joined"] * POP_NATIVE +
             final_rates["cautious_explorer"]["tg_joined"] * POP_EXPLORER)
            * scenario["kol_reach_multiplier"])
    )
    rib_submissions = int(
        final_rates["cultural_native"]["rib_submitted"] * POP_NATIVE * scenario["kol_reach_multiplier"]
    )
    confess_submissions = int(
        (final_rates["cultural_native"]["confessed"] * POP_NATIVE +
         final_rates["cautious_explorer"]["confessed"] * POP_EXPLORER * 0.5)
        * scenario["kol_reach_multiplier"]
    )
    kyc_accounts = min(
        10_001,
        int((final_rates["cultural_native"]["kyc_completed"] * POP_NATIVE +
             final_rates["cautious_explorer"]["kyc_completed"] * POP_EXPLORER)
            * scenario["kol_reach_multiplier"])
    )

    # gap Δ: baseline 2.52; stance change scaled to 7-pt gap reduction
    mean_stance_change = (
        sum(a["stance"] - AGENT_TYPES[a["type"]]["initial_stance"] for a in agents)
        / len(agents)
    )
    predicted_gap = max(1.0, 2.52 - (mean_stance_change * 4.2))

    # boring association: baseline 39.4%
    positive_agents = sum(1 for a in agents if a["stance"] > 0.1) / len(agents)
    boring_predicted = max(0.10, 0.394 - (positive_agents * 0.22))

    predicted_metrics = {
        "tg_members_by_may22":       tg_members,
        "rib_total_submissions":      rib_submissions,
        "confess_unique_submissions": confess_submissions,
        "kyc_airdrop_accounts":       kyc_accounts,
        "trust_engagement_gap_jul":   round(predicted_gap, 2),
        "boring_association_jul":     f"{boring_predicted:.1%}",
        "mean_stance_final":          round(sum(a["stance"] for a in agents) / len(agents), 4),
        "mean_stance_change":         round(mean_stance_change, 4),
        "pct_positive_stance":        f"{positive_agents:.1%}",
    }

    print(f"\n  ── PREDICTED METRICS ({scenario['label']}) ──")
    for k, v in predicted_metrics.items():
        print(f"    {k:<40} {v}")

    return {
        "scenario": scenario_name,
        "label": scenario["label"],
        "round_logs": round_logs,
        "final_rates_sample": final_rates,
        "predicted_metrics": predicted_metrics,
        "agent_count": len(agents),
        "timestamp": datetime.now().isoformat(),
    }

# ── Entry Point ───────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  Re-coding Trust — Campaign Simulation (Section 6)")
    print("  COMM4150 FYP | ZHAO Han (1155191400)")
    print(f"  Model: {MODEL} | Agents: 60 | Scenarios: 3")
    print("=" * 60)

    client = get_client()
    all_results = {}

    for scenario_name, scenario in SCENARIOS.items():
        result = run_scenario(client, scenario_name, scenario)
        all_results[scenario_name] = result

    # ── Save results ──────────────────────────────────────────────────────────
    out_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "data", "simulation"
    )
    os.makedirs(out_dir, exist_ok=True)

    json_path = os.path.join(out_dir, "results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Full results saved → {json_path}")

    # ── Summary table ─────────────────────────────────────────────────────────
    summary_lines = [
        "=" * 72,
        "SECTION 6 — SIMULATION SUMMARY TABLE",
        "Re-coding Trust | ZHAO Han (1155191400) | COMM4150 FYP",
        "=" * 72,
        f"{'Metric':<42} {'Pessimistic':>10} {'Base':>10} {'Optimistic':>10}",
        "-" * 72,
    ]
    metrics_display = [
        ("TG members by May 22",           "tg_members_by_may22"),
        ("RIB community submissions",       "rib_total_submissions"),
        ("/confess unique submissions",     "confess_unique_submissions"),
        ("KYC airdrop accounts",            "kyc_airdrop_accounts"),
        ("Trust-Engagement Gap Δ (Jul)",    "trust_engagement_gap_jul"),
        ("'Boring' association (Jul)",      "boring_association_jul"),
    ]
    for label, key in metrics_display:
        vals = [str(all_results[s]["predicted_metrics"][key]) for s in SCENARIOS]
        summary_lines.append(f"{label:<42} {vals[0]:>10} {vals[1]:>10} {vals[2]:>10}")

    summary_lines += [
        "-" * 72,
        f"Simulation seed: {RANDOM_SEED} | Model: {MODEL}",
        f"Run timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 72,
    ]
    summary = "\n".join(summary_lines)
    print("\n" + summary)

    summary_path = os.path.join(out_dir, "summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"✓ Summary saved → {summary_path}")


if __name__ == "__main__":
    main()
