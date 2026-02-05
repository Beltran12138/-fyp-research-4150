import sys
import os

# Add the current directory to path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from visualization.engine import VisualizationEngine

def run_pipeline():
    print("--- Starting HashKey Social Listening Pipeline ---")
    
    # In a real scenario, we would call collectors and analysis modules here
    # For this research phase, we generate visualizations based on research data
    
    print("[1/2] Initializing Visualization Engine...")
    # Go up one level to reach the outputs folder in root
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
    engine = VisualizationEngine(output_dir=output_path)
    
    print("[2/2] Generating Research Visualizations...")
    engine.generate_pain_points_wordcloud()
    engine.generate_sentiment_trend()
    engine.generate_influencer_matrix()
    
    print("\n[SUCCESS] Pipeline completed.")
    print(f"Visualizations updated in: {output_path}")

if __name__ == "__main__":
    run_pipeline()
