import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import os

def main():
    print("Loading engineered data...")
    try:
        df = pd.read_csv("data/train_engineered.csv")
    except FileNotFoundError:
        print("Error: data/train_engineered.csv not found.")
        return

    # Drop non-feature columns
    drop_cols = ['target', 'date_id', 'row_id'] # row_id might not exist in dummy data
    features = [c for c in df.columns if c not in drop_cols]
    
    X = df[features]
    y = df['target']
    
    # Split Data (Time Series Split)
    # CRITICAL FIX: We must split by TIME, not randomly.
    # We train on the first 80% of days, and test on the last 20%.
    split_date = int(df['date_id'].max() * 0.8)
    
    train_data = df[df['date_id'] < split_date]
    val_data = df[df['date_id'] >= split_date]
    
    X_train = train_data[features]
    y_train = train_data['target']
    X_val = val_data[features]
    y_val = val_data['target']
    
    print(f"Training LightGBM model on {X_train.shape[0]} rows...")
    
    params = {
        'objective': 'regression',
        'metric': 'mae',
        'boosting_type': 'gbdt',
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.9
    }
    
    train_data = lgb.Dataset(X_train, label=y_train)
    val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)
    
    model = lgb.train(
        params,
        train_data,
        num_boost_round=100,
        valid_sets=[val_data],
        callbacks=[lgb.early_stopping(stopping_rounds=10), lgb.log_evaluation(10)]
    )
    
    # Save Model
    model.save_model('model.txt')
    print("Model saved to model.txt")
    
    # Feature Importance
    importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importance()
    }).sort_values('importance', ascending=False)
    
    print("\nTop 5 Features:")
    print(importance.head(5))

if __name__ == "__main__":
    main()
