from pathlib import Path

import typer
import pandas as pd

from .config import PipelineConfig
from .extract import read_csv_checked
from .pii import handle_pii
from .transform import build_neighbourhood_summary
from .validate import validate_summary


app = typer.Typer(help="Airbnb ops CLI")


@app.command("run")
def run() -> None:
    """
    Run the full Airbnb pipeline:
    - read raw data
    - handle PII
    - build neighbourhood summary
    - validate
    - save CSV + report
    """
    config = PipelineConfig()

    # ensure directories exist
    config.processed_dir.mkdir(parents=True, exist_ok=True)
    config.reports_dir.mkdir(parents=True, exist_ok=True)

    # 1) read raw data
    listings = read_csv_checked(config.listings_path)
    segments = read_csv_checked(config.segments_path)

    # 2) handle PII
    listings = handle_pii(listings)

    # 3) transform
    summary = build_neighbourhood_summary(listings, segments)

    # 4) validate
    validate_summary(summary)

    # 5) save output CSV
    output_path: Path = config.output_path
    summary.to_csv(output_path, index=False)

    # 6) build and save report
    report_lines = [
        "# HW01-A run report",
        "",
        f"- Output rows: {len(summary)}",
        f"- Output path: {output_path}",
    ]
    report_text = "\n".join(report_lines)

    config.report_path.write_text(report_text, encoding="utf-8")

    typer.echo(f"Pipeline finished. Output: {output_path}")
    typer.echo(f"Report: {config.report_path}")


if __name__ == "__main__":
    app()