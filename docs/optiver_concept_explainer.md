# The "No-Jargon" Explainer

You asked excellent questions. The terminology is confusing because it borrows words from other fields. Let's translate them.

## 1. Docker Questions
**Q: "Why is it an image? What does it do with a picture?"**
*   **Analogy:** Think of a **Video Game Save File** or a **System Backup**.
*   **Explanation:** It is *not* a picture (jpeg/png). In computing, an "Image" means a "frozen snapshot of a hard drive."
*   **Why we use it:** We created a "snapshot" of a computer that has Python and LightGBM installed. When you run `docker run`, you are "loading that save file" so you can play the game (run the code) immediately without installing anything.

**Q: "Why is there a C++ package (`libgomp1`)?"**
*   **Analogy:** **Premium Fuel** for a sports car.
*   **Explanation:** Python is easy to write, but slow. LightGBM is fast because it's actually written in C++ (a hard, fast language).
*   **The Catch:** For LightGBM to run, it needs a specific C++ helper tool called `libgomp1` (OpenMP) to handle the speed. We installed it so LightGBM doesn't crash.

**Q: "Why keep the pipeline start when this computer on?"**
*   **Clarification:** This instruction (`CMD`) is for the *Virtual Computer* (Container), not your laptop.
*   **Translation:** "As soon as this Virtual Computer wakes up, automatically run the script." It ensures you don't have to type `python main.py` yourself every time.

## 2. Python Questions (`delayed`)
**Q: "Why use `delayed`?"**
*   **Analogy:** **Meal Prep**.
*   **Explanation:**
    *   Normally, when Python sees `calculate_features()`, it runs it *now*.
    *   `delayed(calculate_features)` tells Python: "Don't cook this meal yet. Just put the ingredients in a Tupperware box."
    *   **Why:** We make 200 Tupperware boxes (one for each stock). Then, we hand them to 8 different chefs (CPU cores) to cook them all at the same time.

## 3. The Dataset (The "Quant" Logic)
**Q: "What are these 2 sets of columns?"**
This dataset is special because it's about the **Closing Auction** (the last 10 minutes of the day).

### Set A: The Normal Market (The "Now")
*   **`bid_price` / `ask_price`:**
    *   **Bid:** The highest price someone is willing to **buy** right now.
    *   **Ask:** The lowest price someone is willing to **sell** right now.
    *   **Imbalance Ratio:** If there are 1,000 people wanting to buy (Bid Size) and only 10 people wanting to sell (Ask Size), the price is about to go UP. That's the "Imbalance."

### Set B: The Auction Market (The "Future")
*   **`far_price` / `near_price`:**
    *   These are hypothetical prices calculated by the NASDAQ computer.
    *   **Translation:** "If the market closed *right this second*, what would the price be?"
    *   Quants watch these to see where the price is "drifting" before the final bell rings.
