import pandas as pd
import numpy as np
import os

def generate_dummy_data(output_path="data/train.csv", n_rows=10000):
    print(f"Generating {n_rows} rows of dummy data...")
    
    # Optiver competition columns
    columns = [
        "stock_id", "date_id", "seconds_in_bucket",
        "imbalance_size", "imbalance_buy_sell_flag",
        "reference_price", "matched_size",
        "far_price", "near_price",
        "bid_price", "bid_size",
        "ask_price", "ask_size",
        "wap", "target"
    ]
    
    data = {
        "stock_id": np.random.randint(0, 200, n_rows),
        "date_id": np.random.randint(0, 480, n_rows),
        "seconds_in_bucket": np.random.choice(range(0, 550, 10), n_rows),
        "imbalance_size": np.random.rand(n_rows) * 1000000,
        "imbalance_buy_sell_flag": np.random.choice([-1, 0, 1], n_rows),
        "reference_price": np.random.normal(1.0, 0.01, n_rows),
        "matched_size": np.random.rand(n_rows) * 500000,
        "far_price": np.random.normal(1.0, 0.02, n_rows),
        "near_price": np.random.normal(1.0, 0.015, n_rows),
        "bid_price": np.random.normal(0.999, 0.001, n_rows),
        "bid_size": np.random.randint(100, 10000, n_rows),
        "ask_price": np.random.normal(1.001, 0.001, n_rows),
        "ask_size": np.random.randint(100, 10000, n_rows),
        "wap": np.random.normal(1.0, 0.005, n_rows),
        "target": np.random.normal(0, 1, n_rows)
    }
    
    df = pd.DataFrame(data)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"Saved dummy data to {output_path}")

if __name__ == "__main__":
    generate_dummy_data()
