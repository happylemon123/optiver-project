#!/bin/bash

# 1. Build the Docker image
echo "Building Docker image..."
docker build -t optiver-pipeline .

# 2. Run the container
echo "Running pipeline..."
# We mount the local directory to /app so we can see the output files (model.txt, data/)
docker run --rm -v $(pwd):/app optiver-pipeline
