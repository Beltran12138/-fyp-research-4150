import re
import pandas as pd
import jieba
import os
import time
from textblob import TextBlob
from snownlp import SnowNLP

# Chinese character detection pattern
_CJK_RE = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')

def _compute_sentiment(text: str) -> float:
    """
    Compute sentiment polarity for a single post.

    - Chinese text  → SnowNLP.sentiments, rescaled to [-1, +1]
    - English text  → TextBlob.sentiment.polarity  (already [-1, +1])

    Returns a float in [-1.0, 1.0].
    """
    text = str(text).strip()
    if not text:
        return 0.0

    if _CJK_RE.search(text):
        # SnowNLP returns [0, 1]; rescale to [-1, +1]
        score = SnowNLP(text).sentiments
        return round(score * 2 - 1, 4)
    else:
        return round(TextBlob(text).sentiment.polarity, 4)


class DataProcessor:
    def __init__(self, raw_path, processed_path):
        self.raw_path = raw_path
        self.processed_path = processed_path
        if not os.path.exists(self.processed_path):
            os.makedirs(self.processed_path)

    def process_sentiment(self):
        print(f"Reading raw data from {self.raw_path}...")
        df = pd.read_csv(self.raw_path)

        print("Initializing NLP pipeline (TextBlob for English / SnowNLP for Chinese)...")

        # Compute sentiment directly from post content
        df['analyzed_sentiment'] = df['content'].apply(_compute_sentiment)

        all_text = " ".join(df['content'].tolist())
        words = jieba.lcut(all_text)
        stop = {'HashKey', 'the', 'and', 'for', 'is', 'to', 'of', 'a', 'in', 'on'}
        filtered_words = [w for w in words if len(w) > 1 and w not in stop]

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