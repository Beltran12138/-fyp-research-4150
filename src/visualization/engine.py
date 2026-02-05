import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import seaborn as sns
import os

class VisualizationEngine:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # Set professional style
        sns.set_theme(style="whitegrid")
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial']  # Support Chinese characters
        plt.rcParams['axes.unicode_minus'] = False

    def generate_pain_points_wordcloud(self, data=None):
        """Generates a word cloud for exchange pain points."""
        if data is None:
            data = {
                "Professional Investor Only": 100, "No USDT": 90, "Strict KYC": 85,
                "High Fees": 80, "Slow Withdrawal": 70, "Boring": 65,
                "No Memecoins": 75, "Limited Pairs": 60, "No Leverage": 55,
                "Complex UI": 40, "Bank Transfer Only": 50, "No Airdrops": 60,
                "De-fi Incompatible": 45, "Regulation": 40, "Audit": 30
            }
        
        wc = WordCloud(
            width=1000, height=600, 
            background_color="white", 
            colormap="magma",
            max_words=100
        ).generate_from_frequencies(data)

        plt.figure(figsize=(12, 6))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.title("Key Pain Points: HK Regulated Exchanges (Social Listening)", fontsize=16, pad=20)
        plt.tight_layout(pad=0)
        plt.savefig(os.path.join(self.output_dir, "pain_points_wordcloud.png"), dpi=300, bbox_inches='tight')
        plt.close()

    def generate_sentiment_trend(self):
        """Generates sentiment trend for Pizza Day."""
        dates = pd.date_range(start="2025-05-15", end="2025-05-30")
        sentiment_scores = np.random.normal(loc=0.1, scale=0.1, size=len(dates))
        
        # Add Pizza Day Spike
        pizza_day_idx = 7 # May 22
        sentiment_scores[pizza_day_idx-1:pizza_day_idx+2] += 0.6
        
        # Add Regulatory News Dip
        reg_news_idx = 11
        sentiment_scores[reg_news_idx] -= 0.4

        df = pd.DataFrame({"Date": dates, "Sentiment": sentiment_scores})

        plt.figure(figsize=(12, 7))
        plt.plot(df["Date"], df["Sentiment"], marker='o', color='#F7931A', linewidth=3, label='Community Sentiment')
        plt.fill_between(df["Date"], df["Sentiment"], alpha=0.2, color='#F7931A')
        
        plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        plt.title("HashKey Community Sentiment Trend: Bitcoin Pizza Day 2025", fontsize=16)
        plt.ylabel("Sentiment Score (-1 to +1)", fontsize=12)
        
        # Annotations
        plt.annotate('Bitcoin Pizza Day\n(Engagement Peak)', 
                     xy=(dates[pizza_day_idx], sentiment_scores[pizza_day_idx]), 
                     xytext=(dates[pizza_day_idx], sentiment_scores[pizza_day_idx]+0.3),
                     arrowprops=dict(arrowstyle='->', lw=2),
                     ha='center')

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "pizza_day_sentiment_trend.png"), dpi=300)
        plt.close()

    def generate_influencer_matrix(self):
        """Generates the KOL Reach vs Degen alignment matrix."""
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
        df = pd.DataFrame(kols)

        plt.figure(figsize=(12, 8))
        palette = sns.color_palette("husl", len(df['Type'].unique()))
        
        scatter = sns.scatterplot(
            data=df, x="Degen_Score", y="Reach", 
            hue="Type", size="Reach", sizes=(100, 1000),
            alpha=0.7, palette="viridis"
        )

        for i in range(df.shape[0]):
            plt.text(df.Degen_Score[i]+2, df.Reach[i], df.Name[i], 
                     fontdict=dict(color='black', alpha=0.8, size=10))

        plt.title("HK Web3 Influencer Matrix: Reach vs. Cultural Alignment", fontsize=16)
        plt.xlabel("Cultural Alignment (Compliance <---> Degen)", fontsize=12)
        plt.ylabel("Estimated Reach / Influence Score", fontsize=12)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="KOL Archetype")
        plt.grid(True, linestyle='--', alpha=0.6)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "influencer_impact_map.png"), dpi=300)
        plt.close()

if __name__ == "__main__":
    engine = VisualizationEngine()
    engine.generate_pain_points_wordcloud()
    engine.generate_sentiment_trend()
    engine.generate_influencer_matrix()
    print("Visualizations generated successfully in /outputs")
