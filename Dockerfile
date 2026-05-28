FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml requirements.txt ./
COPY pkg ./pkg

RUN pip install --no-index --find-links=/app/pkg typer click rich shellingham

RUN pip install --no-cache-dir pandas typer rich

COPY src ./src
COPY data/raw ./data/raw
COPY dvc.yaml ./
COPY run_pipeline.py run_pipeline_offline.py ./
COPY reports ./reports

RUN pip install --no-cache-dir .

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

CMD ["airbnb-ops", "run"]





