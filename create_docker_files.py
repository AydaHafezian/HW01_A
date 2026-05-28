from pathlib import Path

# 1. .dockerignore
dockerignore = """
.venv
.git
.dvc
__pycache__
*.pyc
data/raw/
"""
Path(".dockerignore").write_text(dockerignore, encoding="utf-8")

# 2. Dockerfile
dockerfile = """FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml requirements.txt ./

RUN pip install --no-cache-dir .

COPY src/ ./src/

ENTRYPOINT ["airbnb-ops"]
"""
Path("Dockerfile").write_text(dockerfile, encoding="utf-8")

# 3. docker-compose.yml
docker_compose = """services:
  pipeline:
    build: .
    volumes:
      - ./data:/app/data
    command: ["process", "--listings", "data/raw/listings_sample.csv", "--segments", "data/raw/neighbourhood_segments.csv"]
"""
Path("docker-compose.yml").write_text(docker_compose, encoding="utf-8")

print("Docker files created successfully using utf-8 encoding.")