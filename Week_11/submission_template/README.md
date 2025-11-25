# Week 11 - Docker Lab Submission

This project demonstrates basic Docker usage for data science applications.

## What This Project Does

This project contains:
1. **app.py** - A simple Python script that prints messages
2. **analyze.py** - A data analysis script that reads a CSV file and calculates statistics
3. **Dockerfile** - Instructions for building a Docker image
4. **docker-compose.yml** - Configuration for running Jupyter Notebook

## Prerequisites

- Docker Desktop installed and running
- Verify with: `docker --version`

## How to Build

Build the Docker image:
```bash
docker build -t data-analyzer .
```

## How to Run

Run the data analysis:
```bash
docker run data-analyzer
```

Run with volume mount (to use your own data):
```bash
docker run -v $(pwd)/data:/app/data data-analyzer
```

Run Jupyter Notebook:
```bash
docker-compose up
```
Then open the URL shown in the terminal (usually http://localhost:8888)

## Project Structure

```
.
├── app.py              # Simple Python script
├── analyze.py          # Data analysis script
├── data/
│   └── scores.csv      # Sample data file
├── Dockerfile          # Docker image definition
├── requirements.txt    # Python dependencies
├── docker-compose.yml  # Docker Compose configuration
└── README.md          # This file
```

## Common Commands

```bash
# Build image
docker build -t data-analyzer .

# Run container
docker run data-analyzer

# List images
docker images

# List containers
docker ps -a

# Stop container
docker stop <container_id>

# Remove container
docker rm <container_id>

# Start Jupyter
docker-compose up
```

## Issues Encountered

(Describe any problems you faced and how you solved them)

Example:
- **Issue**: Port 8888 already in use
- **Solution**: Changed port in docker-compose.yml to 8889:8888
