# Real-World Quant: "How does this actually work?"

You asked: *"If training takes 1 hour, how do we trade the 10-minute close?"*

This is the most common confusion for beginners. The answer lies in separating **School** (Training) from **Work** (Inference).

## 1. The Time Paradox: Training vs. Inference

### Phase A: Training (The "School")
*   **When:** Overnight (e.g., 2:00 AM - 6:00 AM).
*   **Time Taken:** Hours or Days.
*   **Action:** The computer looks at the last 5 years of data and learns the rules.
*   **Output:** The `model.txt` file (The "Brain").

### Phase B: Inference (The "Work")
*   **When:** During the 10-minute Close (3:50 PM - 4:00 PM).
*   **Time Taken:** **Microseconds.**
*   **Action:** The `model.txt` is loaded into memory.
    *   *Market:* "Price is 100."
    *   *Model:* "Buy!" (Takes 0.0001 seconds).
*   **The Key:** We do **NOT** train the model during the close. We just *use* it.

## 2. "How long is the model used for?" (Model Decay)
Models are like fresh fruit. They rot.

*   **Alpha Decay:** The market changes. A strategy that worked in 2023 might fail in 2024 because other traders figured it out.
*   **Retraining Cycle:**
    *   **High Frequency:** Retrained every night (using yesterday's new data).
    *   **Mid Frequency:** Retrained every weekend.
    *   **Low Frequency:** Retrained monthly.

## 3. The Role War: Researcher vs. Developer
You asked: *"Doesn't the Quant Developer do the engineering?"*

Traditionally, Yes. But the lines are blurring.

### The "Old School" Workflow (2010)
1.  **Researcher (You):** Writes messy Python code in a Jupyter Notebook. Finds a strategy.
2.  **Handoff:** You email the notebook to the Developer.
3.  **Developer:** Rewrites the whole thing in C++ for production.
4.  **Problem:** This takes weeks. By the time it's rewritten, the market has changed.

### The "Modern" Workflow (2025)
1.  **Researcher (You):** Writes **clean** Python code (using Docker/Parallelism).
2.  **Handoff:** The Developer takes your Docker container and deploys it *directly*.
3.  **Why you need Engineering skills:** If your Python code is slow garbage, the Developer rejects it. If you build it with Docker and Parallelism (like we did), you get hired because you save them time.

## Summary
*   **Training** is slow (Offline). **Inference** is fast (Online).
*   Models are retrained **daily** or **weekly**.
*   **Researchers** who know **Engineering** (Docker/Git) are the most valuable people in the industry because they bridge the gap.
