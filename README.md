# COMM4150 FYP: Re-coding Trust
> **Computational Social Listening Dashboard for HashKey Exchange**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Research: CUHK](https://img.shields.io/badge/Research-CUHK-maroon.svg)](https://www.cuhk.edu.hk/)

## 📌 Project Overview
This repository contains the computational research component of the **"Re-coding Trust"** PR campaign for **HashKey Exchange** (Bitcoin Pizza Day 2026). 

The project addresses the **"Trust Paradox"**: While HashKey has secured institutional trust through compliance, it faces a "culture gap" with Hong Kong's crypto-native youth. We use NLP and social listening to bridge this gap by encoding "Institutional Safety" into "Degen Culture."

---

## 📂 Project Structure
```text
.
├── config/             # Configuration templates & API keys
├── data/               # Raw and processed social data (LIHKG, X, TG)
├── docs/               # Academic research papers & methodology
│   ├── 2.1_Secondary_Research.md
│   ├── 2.1.1_Computational_Social_Listening.md
│   └── 2.1.1_Visualizations_Output.md
├── outputs/            # Generated charts and word clouds
├── src/                # Python source code
│   ├── collectors/     # Data collection scripts (X API, Telethon)
│   ├── analysis/       # NLP, Sentiment Analysis, LDA Topic Modeling
│   ├── visualization/  # Matplotlib/Seaborn visualization engine
│   └── main.py         # Pipeline entry point
├── requirements.txt    # Project dependencies
└── README.md           # You are here
```

---

## 📊 Key Research Insights

### 1. The Pain Point Map
*What are local users actually complaining about regarding licensed exchanges?*
![Pain Points Word Cloud](outputs/pain_points_wordcloud.png)

### 2. The "Pizza Day" Opportunity
*Sentiment analysis showing the "Compliance vs. Culture" engagement gap during global Web3 holidays.*
![Sentiment Trend](outputs/pizza_day_sentiment_trend.png)

### 3. The Influencer Matrix
*Mapping "Institutional Trust" vs. "Degen Culture" among HK Web3 Opinion Leaders.*
![Influencer Map](outputs/influencer_impact_map.png)

---

## 🛠 Tech Stack
* **Language:** Python 3.9+
* **NLP:** `TextBlob`, `SnowNLP`, `Jieba` (Chinese Segmentation)
* **Visualization:** `Matplotlib`, `Seaborn`, `WordCloud`
* **Data Sources:** Twitter/X API, LIHKG (Scraped), Telegram (Telethon)

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Beltran12138/-fyp-research-4150.git
   cd -fyp-research-4150
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the visualization engine**
   ```bash
   python src/main.py
   ```

---

## 📝 Research Excerpts
- **[Secondary Research Report](docs/2.1_Secondary_Research.md)**: Analysis of HK's Web3 policy landscape and the "Trust Paradox."
- **[Methodology](docs/2.1.1_Computational_Social_Listening.md)**: Technical breakdown of the NLP pipeline and data sources.

---
*Developed by ZHAO Han (1155191400) | CUHK COMM4150 Final Year Project*
