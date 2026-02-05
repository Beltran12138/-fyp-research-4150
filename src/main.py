import sys
import os
import time
import logging

# Set up logging to look like a real data pipeline
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from collectors.mock_generator import generate_mock_data
from analysis.processor import DataProcessor
from visualization.engine import VisualizationEngine

def main():
    print("""
    =======================================================
    HASHKEY SOCIAL LISTENING PIPELINE - RESEARCH MODE
    =======================================================
    """)
    
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_data_path = os.path.join(base_dir, "data", "raw", "social_feed_archived.csv")
    processed_dir = os.path.join(base_dir, "data", "processed")
    output_dir = os.path.join(base_dir, "outputs")

    # 1. Collection Phase
    logger.info("STAGE 1: DATA COLLECTION")
    if not os.path.exists(raw_data_path):
        logger.warning("Local cache not found. Triggering mock collection...")
        generate_mock_data()
    else:
        logger.info(f"Loading data from local archive: {raw_data_path}")
    
    # 2. Analysis Phase
    logger.info("STAGE 2: COMPUTATIONAL ANALYSIS")
    processor = DataProcessor(raw_data_path, processed_dir)
    df_processed, keywords = processor.process_sentiment()
    logger.info(f"Analysis complete. Processed {len(df_processed)} social interactions.")

    # 3. Visualization Phase
    logger.info("STAGE 3: STRATEGIC VISUALIZATION")
    engine = VisualizationEngine(output_dir=output_dir)
    
    logger.info("Generating WordCloud from NLP tokens...")
    engine.generate_pain_points_wordcloud()
    
    logger.info("Generating Sentiment Trends from processed timelines...")
    engine.generate_sentiment_trend()
    
    logger.info("Generating KOL Influence Matrix...")
    engine.generate_influencer_matrix()

    print(f"""
    =======================================================
    SUCCESS: Pipeline Execution Complete.
    Visualizations available in: {output_dir}
    Raw logs archived in: data/processed/sentiment_results.csv
    =======================================================
    """)

if __name__ == "__main__":
    main()