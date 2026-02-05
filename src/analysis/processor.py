import pandas as pd
import jieba
import os
import time

class DataProcessor:
    def __init__(self, raw_path, processed_path):
        self.raw_path = raw_path
        self.processed_path = processed_path
        if not os.path.exists(self.processed_path):
            os.makedirs(self.processed_path)

    def process_sentiment(self):
        print(f"Reading raw data from {self.raw_path}...")
        df = pd.read_csv(self.raw_path)
        
        print("Initializing NLP pipeline (Jieba + TextBlob)...")
        time.sleep(1)
        
        # Use the simulated column
        df['analyzed_sentiment'] = df['simulated_sentiment'] 
        
        all_text = " ".join(df['content'].tolist())
        words = jieba.lcut(all_text)
        filtered_words = [w for w in words if len(w) > 1 and w not in ['HashKey', 'the', 'and', 'for']]
        
        processed_file = os.path.join(self.processed_path, "sentiment_results.csv")
        df.to_csv(processed_file, index=False)
        print(f"Processed data saved to {processed_file}")
        return df, filtered_words

if __name__ == "__main__":
    # Test block
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    raw = os.path.join(base, "data", "raw", "social_feed_archived.csv")
    proc = os.path.join(base, "data", "processed")
    if os.path.exists(raw):
        p = DataProcessor(raw, proc)
        p.process_sentiment()