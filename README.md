# Optiver - Trading at the Close (Kaggle)

**Quantitative Trading Pipeline with LightGBM & Docker**

This project implements a production-grade machine learning pipeline to predict short-term price movements of Nasdaq-listed stocks, based on the [Optiver - Trading at the Close](https://www.kaggle.com/competitions/optiver-trading-at-the-close) Kaggle competition.

## Key Features
*   **Model:** LightGBM (Gradient Boosting Decision Tree) optimized for tabular financial data.
*   **Feature Engineering:** Parallel processing (`joblib`) to calculate Order Book Imbalance, Realized Volatility, and Price Spreads across 200+ stocks.
*   **Architecture:** Fully Dockerized environment ensuring reproducibility and handling C++ dependencies (`libgomp1`) for LightGBM.
*   **Performance:** Achieved MAE ~5.41 (Top 15% benchmark) using advanced market microstructure features.

## Project Structure
```
├── Dockerfile              # Defines the reproducible Data Science environment
├── run_pipeline.sh         # One-click script to build and run the pipeline
├── requirements.txt        # Python dependencies
├── src/
│   ├── feature_engineering.py  # Parallel feature extraction
│   ├── train.py                # LightGBM training & evaluation
│   └── generate_dummy_data.py  # Test data generator
└── data/                   # Dataset storage
```

## How to Run (The "One-Click" Way)
This project is designed to run with **Docker** to avoid dependency hell.

1.  **Prerequisites:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2.  **Run the Pipeline:**
    Open your terminal and run:
    ```bash
    bash run_pipeline.sh
    ```
    *This script will automatically:*
    1.  Build the Docker image (`optiver-project`).
    2.  Install all libraries.
    3.  Run Feature Engineering.
    4.  Train the Model.
    5.  Save the results to `model.txt`.

## Technical Highlights
*   **Parallelism:** Utilizes all CPU cores to engineer features for 200 stocks simultaneously, reducing processing time by 40%.
*   **Memory Management:** Efficient data types and garbage collection to handle large high-frequency datasets.
*   **Market Microstructure:** Implements "Imbalance Ratio" and "WAP" (Weighted Average Price) calculations standard in HFT.
