import pandas as pd
import numpy as np
from joblib import Parallel, delayed
import os
import time

def calculate_features(stock_df):
    """
    Calculates features for a single stock.
    Designed to be run in parallel.
    """
    # 1. Imbalance Features
    stock_df['imbalance_ratio'] = stock_df['imbalance_size'] / stock_df['matched_size']
    
    # 2. Price Spreads
    stock_df['price_spread'] = stock_df['ask_price'] - stock_df['bid_price']
    stock_df['market_urgency'] = stock_df['price_spread'] * stock_df['imbalance_buy_sell_flag']
    
    # 3. Depth Pressure
    stock_df['depth_pressure'] = (stock_df['ask_size'] - stock_df['bid_size']) / (stock_df['ask_size'] + stock_df['bid_size'])
    
    # 4. Volatility (Realized Volatility of WAP)
    # We need to sort by time first
    stock_df = stock_df.sort_values('seconds_in_bucket')
    stock_df['log_return'] = np.log(stock_df['wap']).diff()
    stock_df['realized_volatility'] = stock_df['log_return'].rolling(window=10).std()
    
    return stock_df.fillna(0)

def main():
    print("Loading data...")
    try:
        df = pd.read_csv("data/train.csv")
    except FileNotFoundError:
        print("Error: data/train.csv not found. Run generate_dummy_data.py first.")
        return

    print(f"Data loaded: {df.shape}")
    
    start_time = time.time()
    
    # PARALLEL EXECUTION
    # Group by stock_id and process each group in a separate core
    print("Starting parallel feature engineering...")
    results = Parallel(n_jobs=-1, verbose=1)(
        delayed(calculate_features)(group) for _, group in df.groupby('stock_id')
    )
    
    # Combine results back into one DataFrame
    full_df = pd.concat(results)
    
    end_time = time.time()
    print(f"Feature engineering completed in {end_time - start_time:.2f} seconds")
    
    output_path = "data/train_engineered.csv"
    full_df.to_csv(output_path, index=False)
    print(f"Saved engineered data to {output_path}")

if __name__ == "__main__":
    main()
