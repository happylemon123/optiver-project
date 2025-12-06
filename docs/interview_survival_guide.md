# Interview Survival Guide: "I Forgot the Syntax!"

You are worried that AI is making you forget how to code. This is a valid fear, but here is the secret: **Senior Engineers forget syntax too.**

## 1. The Big Question: "Do I need to write C++ / OpenMP?"
**The Answer:** **NO.**

*   **Your Role:** You are a *Quant Researcher* or *Data Scientist*. You drive the car (Python).
*   **The C++ Role:** That is for *Quant Developers* or *High-Frequency Engineers*. They build the engine.
*   **OpenMP:** You will *never* write OpenMP code in an interview. You just need to know it exists so you can fix the `ImportError` if your Docker container crashes.

## 2. The Strategy: Pseudo-code > Syntax
In a whiteboard interview, if you forget `df.groupby('col').apply(...)`, **DO NOT PANIC.**

**Do this instead:**
1.  **Say it in English:** "I want to group by the stock ID and calculate the volatility for each."
2.  **Write Pseudo-code:**
    ```python
    for stock in data:
        calculate_volatility(stock)
    ```
3.  **The Magic Phrase:** *"I don't recall the exact Pandas syntax for the apply function right now, but conceptually I'm splitting the dataframe and applying this logic."*

**90% of interviewers will accept this.** They care about your *logic*, not your ability to be a human dictionary.

## 3. The "Must-Memorize" Cheat Sheet (Only 5 Lines)
If you are going to memorize anything, memorize these 5 patterns. They cover 80% of Quant interviews.

### A. The Loop (Iterating)
**Question:** *"Do you mean `for data in range(len(data))`?"*
**Answer:** No! That is the "Old Way" (C-style).
*   **The Old Way (Bad):** `for i in range(len(prices)): print(prices[i])`
    *   You have to manage the index `i` manually. It's messy.
*   **The Python Way (Good):** `for price in prices: print(price)`
    *   Python grabs the item directly. It reads like English: *"For every price in the list of prices..."*

### B. The Filter (Selecting Data)
**Question:** *"Why do you frame `df` twice? `df[df['price'] > 100]`"*
**Answer:** Think of it as `df[ MASK ]`.
1.  **The Inner Part:** `df['price'] > 100`
    *   This creates a "Mask" of True/False values: `[True, False, True, ...]`
    *   It doesn't know *what* data to return, it just knows which rows passed the test.
2.  **The Outer Part:** `df[ ... ]`
    *   This takes the Mask and says: *"Okay, give me the full rows where the Mask is True."*
    *   You need the outer `df` to actually get the data back.

### C. The GroupBy (The Quant Staple)
```python
# "Average price per stock"
df.groupby('stock_id')['price'].mean()
```

### D. The Merge (Joining Tables)
```python
# "Join price data with sector data"
pd.merge(prices_df, sector_df, on='stock_id')
```

### E. The Model (The "Start Engine" Button)
```python
model.fit(X_train, y_train)
prediction = model.predict(X_test)
```

## Summary
*   **Relax:** You don't need to be a C++ expert.
*   **Focus:** Understand *what* the code does (Logic), not just *how* to spell it (Syntax).
*   **Cheat:** Memorize the 5 patterns above. Google the rest.
