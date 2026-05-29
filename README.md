# HW01_A — Dockerized Airbnb Neighbourhood Summary Pipeline

This project is a Dockerized Python package for processing Airbnb listings data and producing a neighbourhood-level summary report.

## Project Overview

The pipeline:
1. Reads raw Airbnb listings and neighbourhood segment data
2. Handles sensitive information by hashing `host_id` and removing `host_name`
3. Aggregates listings by neighbourhood
4. Validates the resulting summary
5. Writes a processed CSV file and a short Markdown run report

## Package Name

The Python package/module used by the project is:

- `airbnb_ops`

The Docker image runs the package entrypoint with:
```bash
python -m airbnb_ops.cli
HW01_A/
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── run_pipeline.py
├── run_pipeline_offline.py
├── dvc.yaml
├── data/
│   ├── raw/
│   └── processed/
├── reports/
└── src/
└── airbnb_ops/
├── cli.py
├── config.py
├── extract.py
├── pii.py
├── transform.py
└── validate.py

Input Files
The offline pipeline uses the following input files:

data/raw/listings_sample.csv
data/raw/neighbourhood_segments.csv
Output Files
The pipeline produces:

data/processed/airbnb_neighbourhood_summary.csv
reports/hw01_a_run_report.md
Pipeline Steps
1. PII Handling
The pipeline anonymizes the dataset by:

hashing host_id into host_key
dropping host_name
2. Transformation
The data is then grouped by neighbourhood and summarized with:

avg_price
n_listings
The summary is also merged with neighbourhood segment information.

3. Validation
The output is validated to ensure that:

it is not empty
it contains the required columns
4. Reporting
A simple Markdown report is generated with:

the number of output rows
the output file path
Docker Usage
Build the Docker image:

bash
docker build -t hw01_a .
Run the container:

bash
docker run --rm hw01_a
Local Usage
If you want to run the offline pipeline without Docker:

bash
python run_pipeline_offline.py
CLI
The project includes a Typer-based CLI under airbnb_ops.cli.

The Dockerfile shows that the app is intended to be started with:

bash
python -m airbnb_ops.cli
Notes
The project is designed to be reproducible through Docker.
A local .venv directory should not be included in the final submission.
The offline pipeline is useful for running and testing the workflow without depending on external services.
Expected Result
After a successful run, you should see:

a processed CSV in data/processed/
a Markdown report in reports/
