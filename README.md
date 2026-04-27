# Re-coding Trust — Computational Research Engine
> CUHK COMM4150 FYP · 2025–2026  
> Quantifying Hong Kong's crypto "Trust Paradox": why users trust HashKey Exchange but won't use it.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Research: CUHK](https://img.shields.io/badge/Research-CUHK-maroon.svg)](https://www.cuhk.edu.hk/)
[![Campaign Deliverables](https://img.shields.io/badge/Campaign-hkx-orange)](https://github.com/Beltran12138/hkx)

**Key Finding:** HashKey users score asset security trust at **M=5.27/7** — yet brand relatability at **M=2.75/7**. The Δ=2.52 gap is statistically significant (t(286) = 24.41, p < .001). This repo measures that gap and informs the [campaign strategy →](https://github.com/Beltran12138/hkx)

---

## Campaign Deliverables

> 🍕 [Pizza Personas Quiz](https://beltran12138.github.io/hkx/quiz/) &nbsp;·&nbsp; 🪦 [Rest in Blockchain Memorial](https://beltran12138.github.io/hkx/rib/) &nbsp;·&nbsp; 📦 [hkx CLI](https://github.com/Beltran12138/hkx)

---

## Research Architecture: 3-Layer Method

| Layer | Method | Scale |
|-------|--------|-------|
| **§2.1** Computational Social Listening | NLP pipeline — TextBlob (EN) + SnowNLP (ZH) | 5,000+ interactions across Twitter/X, LIHKG, Telegram |
| **§2.2** Primary Quantitative Survey | Google Forms, purposive + snowball sampling | N=287 valid responses (18–35, HK-resident) |
| **§2.3** Competitive Benchmark | LBank internal user research (Apr 2025) | N=1,751 |
| **§6** Pre-Launch Simulation | DeepSeek-V3 agent-based scenario model | 3 scenarios × 2 agent types |

---

## Key Findings

### The Trust Paradox — Quantified (§2.2)
*Trust (M=5.27) vs. Relatability (M=2.75): Δ=2.52, t(286)=24.41, p<.001*
![Trust Paradox](outputs/survey_trust_paradox.png)

### Pain Point Mapping (§2.1.1)
*"Lack of Degen Culture" is the #1 barrier to licensed exchange adoption (33.8%), outranking KYC complexity (27.5%) and high fees (21.6%).*
![Pain Points Word Cloud](outputs/pain_points_wordcloud.png)

### Pizza Day Sentiment Anomaly (§2.1.1)
*May 22 is the single highest positive sentiment engagement anomaly in the HK Web3 calendar.*
![Sentiment Trend](outputs/pizza_day_sentiment_trend.png)

### KOL Matrix (§2.1.1)
*Mapping influencer reach against cultural alignment (Compliance ↔ Degen) to identify "Translator" voices.*
![Influencer Map](outputs/influencer_impact_map.png)

### Exchange Usage (§2.2.4)
*64.5% primarily use offshore platforms (Binance/OKX/Bybit); only 15.7% use licensed exchanges.*
![Platform Usage](outputs/survey_platform_usage.png)

### Exchange Selection Factors (§2.2.4)
*Regulatory compliance ranked last (M=3.16/5); UX ranked first (M=4.21/5). Compliance is a hygiene factor, not a pull factor.*
![Factor Ranking](outputs/survey_factor_ranking.png)

### Main Adoption Barriers (§2.2.4)
*Cultural mismatch outranks structural friction.*
![Friction Points](outputs/survey_friction_points.png)

### Bitcoin Pizza Day Awareness (§2.2.4)
*66.2% combined awareness; 67.1% among the 18–24 primary cohort.*
![Pizza Day Awareness](outputs/survey_pizza_day_awareness.png)

### Preferred Campaign Incentive (§2.2.4)
*Token airdrops (45.6%) dominate as the conversion trigger — validating the campaign's on-chain mechanics.*
![Incentive Preference](outputs/survey_incentive_preference.png)

### HashKey Word Association (§2.2.4)
*"Reliable" (48.1%) and "Safe" (46.7%) co-occur with "Boring" (39.4%) — the Trust Paradox in one chart.*
![Word Association](outputs/survey_word_association.png)

---

## Project Structure

```
.
├── data/
│   ├── raw/
│   │   ├── social_feeds/           # Archived social feeds (500+ records)
│   │   └── survey_raw_responses.csv
│   ├── processed/                  # NLP-analyzed sentiment datasets
│   └── simulation/
│       ├── results.json            # §6 pre-launch simulation output (seed: 4150)
│       └── charts/                 # Fig 6.1–6.4 (generated)
├── docs/                           # Academic methodology documentation
├── outputs/                        # All generated charts (10 files)
└── src/
    ├── collectors/                 # Data ingestion pipelines
    ├── analysis/                   # NLP processor
    ├── visualization/
    │   ├── engine.py               # Social listening charts
    │   └── survey_charts.py        # Survey charts (7 outputs)
    ├── simulation/
    │   ├── campaign_sim.py         # DeepSeek-V3 agent simulation
    │   └── generate_charts.py      # Fig 6.1–6.4 generator
    └── main.py                     # Pipeline orchestrator
```

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.9+ |
| NLP | TextBlob (EN), SnowNLP (ZH), Jieba |
| Analytics | Pandas, NumPy, SciPy |
| Visualization | Matplotlib, Seaborn, WordCloud |
| Simulation | DeepSeek-V3 API (deepseek-chat) |

---

## Run

```bash
pip install -r requirements.txt

# Generate all survey charts (10 outputs)
python src/visualization/survey_charts.py

# Run full social listening pipeline
python src/main.py

# Re-run simulation and regenerate Figs 6.1–6.4
python src/simulation/campaign_sim.py
python src/simulation/generate_charts.py
```

---

*ZHAO Han · CUHK COMM4150 Final Year Project · 2025–2026*  
*Campaign deliverables → [github.com/Beltran12138/hkx](https://github.com/Beltran12138/hkx)*
