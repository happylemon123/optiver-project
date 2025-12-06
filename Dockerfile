FROM python:3.9-slim

WORKDIR /app

# Install system dependencies (OpenMP is needed for LightGBM)
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/

# Default command: Generate dummy data, engineer features, then train
CMD ["bash", "-c", "python src/generate_dummy_data.py && python src/feature_engineering.py && python src/train.py"]
