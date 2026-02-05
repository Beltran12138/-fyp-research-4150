import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_mock_data():
    platforms = ['Twitter', 'LIHKG', 'Telegram']
    
    positive_contents = [
        "HashKey's UI is so clean, finally a licensed exchange that feels premium! #HashKey",
        "Just finished my KYC on HashKey. Super fast and professional. Secure trading is the way.",
        "Excited for Bitcoin Pizza Day 2026! Can't wait to see what HashKey has planned.",
        "The safest place to hold BTC in HK. Compliance matters after FTX. #HKWeb3",
        "HashKey's fiat on-ramp is a lifesaver. Direct bank transfer is so much better than C2C.",
        "HK's regulatory framework is leading the way. HashKey is the gold standard."
    ]
    
    negative_contents = [
        "Why is HashKey so boring? No memecoins, no leverage... just plain tokens. #Degen",
        "Strict KYC is such a pain. I miss the offshore days. #HashKey #Crypto",
        "Withdrawal took longer than expected. Still better than nothing I guess.",
        "The 'Professional Investor' requirement is so elitist. What about retail? #HKWeb3",
        "High fees on licensed exchanges compared to DEXs. Why bother?",
        "No USDT pairs? This is so restrictive for active traders."
    ]
    
    neutral_contents = [
        "Checking out the new HashKey update. #HKWeb3 #Crypto",
        "Bitcoin Pizza Day is coming. May 22 is a big day for crypto history.",
        "SFC's new guidelines on VATP are out. Interesting developments.",
        "Anyone using HashKey for institutional custody? Looking for reviews.",
        "Bitcoin price holding steady at $100k. #BTC",
        "HashKey vs OSL - which one has better liquidity?"
    ]

    data = []
    start_date = datetime(2025, 5, 1)
    
    for i in range(500):
        platform = random.choice(platforms)
        timestamp = start_date + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
        
        roll = random.random()
        if roll < 0.4:
            content = random.choice(positive_contents)
            sentiment_val = random.uniform(0.1, 0.8)
        elif roll < 0.7:
            content = random.choice(neutral_contents)
            sentiment_val = random.uniform(-0.1, 0.1)
        else:
            content = random.choice(negative_contents)
            sentiment_val = random.uniform(-0.8, -0.1)
            
        data.append({
            'id': f'raw_{i:04d}',
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'platform': platform,
            'user': f'crypto_user_{random.randint(100, 999)}',
            'content': content,
            'simulated_sentiment': round(sentiment_val, 2)
        })
        
    df = pd.DataFrame(data)
    # Correct relative path
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data', 'raw')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, 'social_feed_archived.csv')
    df.to_csv(output_path, index=False)
    print(f"Mock raw data generated: 500 rows saved to {output_path}")

if __name__ == "__main__":
    generate_mock_data()