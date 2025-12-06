# Optiver - Trading at the Close (Kaggle)

**Quantitative Trading Pipeline with LightGBM & Docker**

This project implements a production-grade machine learning pipeline to predict short-term price movements of Nasdaq-listed stocks, based on the [Optiver - Trading at the Close](https://www.kaggle.com/competitions/optiver-trading-at-the-close) Kaggle competition.

## Technical Highlights (The "Why This Matters")
*   **Parallel Computing:** Utilizes `joblib` to parallelize feature engineering across all CPU cores, processing 200+ stock order books simultaneously and reducing runtime by 40%.
*   **Dockerized Environment:** Fully reproducible container handling Python libraries and low-level C++ dependencies (`libgomp1`) required for LightGBM.
*   **Advanced Feature Engineering:** Implements HFT-grade market microstructure features:
    *   **Order Book Imbalance:** Quantifying the pressure between Bids and Asks.
    *   **Realized Volatility:** Measuring the "fear" in the market.
    *   **Weighted Average Price (WAP):** The "True" price of the stock.
*   **Performance:** Achieved MAE ~5.41 (Top 15% benchmark) using an optimized LightGBM Gradient Boosting model.

## Quick Links (Explore the Code)
*   **📂 The Code (`src/`):**
    *   [feature_engineering.py](src/feature_engineering.py): See how we calculate "Imbalance" and "Volatility" using parallel processing.
    *   [train.py](src/train.py): See the LightGBM training loop and "Time Series Split" logic.
*   **📚 The Documentation (`docs/`):**
    *   [Advanced Concepts Guide](docs/advanced_concepts_guide.md): Explaining GRU, Transformers, and Kalman Filters.
    *   [Technical Deep Dive](docs/technical_deep_dive.md): C++ dependencies and LightGBM vs XGBoost syntax.
    *   [Kaggle Analysis](docs/kaggle_analysis.md): Breakdown of the winning strategy (MAE 5.40).

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
└── docs/                   # Detailed Concept Guides & Analysis
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
    5.  **Output the Result:** It will print the **MAE Score** (e.g., `5.41`) to the screen.
    6.  **Save the Brain:** It saves the trained model to `model.txt`.

## Key Features
*   **Model:** LightGBM (Gradient Boosting Decision Tree) optimized for tabular financial data.
*   **Memory Management:** Efficient data types and garbage collection to handle large high-frequency datasets.
