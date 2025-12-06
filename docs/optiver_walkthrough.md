# What Just Happened? (The Optiver Pipeline)

You just ran a professional "Quantitative Research Pipeline." Here is the breakdown of the black box.

## 1. The "Clean Kitchen" (Docker)
*   **What happened:** Your computer built a "virtual computer" (Container) inside itself.
*   **Why:** This virtual computer has Python 3.9, LightGBM, and all the math libraries installed perfectly. It ensures that if you send this code to a hedge fund, it runs *exactly* the same way.

## 2. The "Prep Work" (Feature Engineering)
*   **The Input:** The 3GB file `train.csv` (stock prices).
*   **The Action:** We needed to calculate things like "Volatility" and "Imbalance" for 200 stocks.
*   **The "Flex":** Instead of doing Stock A -> Stock B -> Stock C (which takes forever), we used **Parallel Computing**. We used all your CPU cores to process Stock A, B, C, and D *at the same time*.
*   **The Result:** `train_engineered.csv` (A new table with your smart features added).

## 3. The "Learning" (Model Training)
*   **The Action:** We fed the `train_engineered.csv` into **LightGBM**.
*   **The Math:** LightGBM looked at the data and said: *"Hey, when 'Imbalance' is high, the price usually goes down."* It wrote these rules down.
*   **The Result:** `model.txt`. This text file contains thousands of "If/Then" rules. This *is* the AI.

## 4. The Proof
You now have a file called `model.txt`. You can send this file to anyone, and they can use it to predict stock prices without knowing how you trained it.

---
### Summary for Interviews
*"I built a reproducible pipeline using **Docker**. It ingests raw tick data, calculates features like Realized Volatility in **parallel** using `joblib`, and trains a **LightGBM** model to predict price movements."*
