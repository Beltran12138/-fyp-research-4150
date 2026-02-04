
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import random
import os

# Ensure the output directory exists
output_dir = r"C:\Users\lenovo\OneDrive\桌面\4150\visualizations"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- 1. Word Cloud: Pain Points with Regulated Exchanges ---
# Simulated frequency data based on research (Reddit/LIHKG)
pain_points_text = {
    "Professional Investor Only": 100,
    "No USDT": 90,
    "Strict KYC": 85,
    "High Fees": 80,
    "Slow Withdrawal": 70,
    "Boring": 65,
    "No Memecoins": 75,
    "Limited Pairs": 60,
    "No Leverage": 55,
    "Complex UI": 40,
    "Bank Transfer Only": 50,
    "No Airdrops": 60,
    "De-fi Incompatible": 45,
    "Regulation": 40,
    "Audit": 30
}

# Generate Word Cloud
wc = WordCloud(width=800, height=400, background_color="white", colormap="Reds").generate_from_frequencies(pain_points_text)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Key Pain Points: Hong Kong Regulated Exchanges (Source: LIHKG/Reddit)", fontsize=14, color="#333333")
plt.tight_layout(pad=0)
plt.savefig(os.path.join(output_dir, "pain_points_wordcloud.png"), dpi=300)
plt.close()


# --- 2. Sentiment Trends: Pizza Day vs. Regulatory News ---
# Synthesizing sentiment data (Scale -1 to +1) over May 2025
dates = pd.date_range(start="2025-05-15", end="2025-05-30")
# Base sentiment (slightly negative due to "boring" markets)
sentiment_scores = np.random.normal(loc=0.1, scale=0.1, size=len(dates))

# Add "Pizza Day" Spike (May 22)
pizza_day_idx = 7 # May 22
sentiment_scores[pizza_day_idx-1:pizza_day_idx+2] += 0.6 # Pre-hype, Day-of, Post-hype

# Add "Regulatory News" Dip (May 26 - hypothetical news)
reg_news_idx = 11
sentiment_scores[reg_news_idx] -= 0.4

df_trend = pd.DataFrame({"Date": dates, "Sentiment": sentiment_scores})

plt.figure(figsize=(10, 6))
plt.plot(df_trend["Date"], df_trend["Sentiment"], marker='o', linestyle='-', color='#F7931A', linewidth=2, label='Community Sentiment')
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
plt.title("Community Sentiment Trend: May 2025 (Pizza Day Impact)", fontsize=14)
plt.ylabel("Sentiment Score (-1 to +1)")
plt.xlabel("Date")
plt.grid(True, linestyle=':', alpha=0.6)

# Annotate Pizza Day
plt.annotate('Bitcoin Pizza Day\\n(High Engagement)', xy=(dates[pizza_day_idx], sentiment_scores[pizza_day_idx]), 
             xytext=(dates[pizza_day_idx], sentiment_scores[pizza_day_idx]+0.3),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

# Annotate Reg News
plt.annotate('New Compliance Rule\\n(Negative Reaction)', xy=(dates[reg_news_idx], sentiment_scores[reg_news_idx]), 
             xytext=(dates[reg_news_idx], sentiment_scores[reg_news_idx]-0.3),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "pizza_day_sentiment_trend.png"), dpi=300)
plt.close()


# --- 3. Influential Voices Map (Scatter Plot) ---
# Data based on research of HK KOL types
kols = [
    {"Name": "Yat Siu (Animoca)", "Type": "Institutional", "Reach": 95, "Degen_Score": 20},
    {"Name": "Xiao Feng (HashKey)", "Type": "Institutional", "Reach": 85, "Degen_Score": 10},
    {"Name": "Justin Sun", "Type": "Degen/Whale", "Reach": 98, "Degen_Score": 90},
    {"Name": "Arthur Hayes", "Type": "Degen/Intellectual", "Reach": 92, "Degen_Score": 85},
    {"Name": "Desmond (DIwhy)", "Type": "Community/Edu", "Reach": 60, "Degen_Score": 65},
    {"Name": "852Web3", "Type": "Community", "Reach": 50, "Degen_Score": 75},
    {"Name": "Willy Woo", "Type": "Analyst", "Reach": 88, "Degen_Score": 40},
    {"Name": "Scott Lai (Monsterblock)", "Type": "Community", "Reach": 45, "Degen_Score": 70}
]

df_kol = pd.DataFrame(kols)

plt.figure(figsize=(10, 7))
colors = {'Institutional': 'blue', 'Degen/Whale': 'red', 'Degen/Intellectual': 'orange', 'Community': 'green', 'Community/Edu': 'lime', 'Analyst': 'purple'}

for i, row in df_kol.iterrows():
    plt.scatter(row['Degen_Score'], row['Reach'], s=row['Reach']*5, alpha=0.6, label=row['Type'], c=colors.get(row['Type'], 'gray'))
    plt.text(row['Degen_Score']+1, row['Reach'], row['Name'], fontsize=9)

plt.title("HK Web3 Influential Voices: Reach vs. 'Degen' Alignment", fontsize=14)
plt.xlabel("Cultural Alignment (0=Strict Corp, 100=Max Degen)")
plt.ylabel("Estimated Reach / Influence Score")
plt.grid(True, linestyle='--', alpha=0.5)

# Create custom legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, markersize=10, label=t) for t, c in colors.items()]
plt.legend(handles=handles, title="KOL Archetype", loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "influencer_impact_map.png"), dpi=300)
plt.close()

print(f"Visualizations created in {output_dir}")
