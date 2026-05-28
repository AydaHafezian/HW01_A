from dataclasses import dataclass
from pathlib import Path


@dataclass
class PipelineConfig:
    project_root: Path = Path(__file__).resolve().parents[2]

    raw_dir: Path = project_root / "data" / "raw"
    processed_dir: Path = project_root / "data" / "processed"
    reports_dir: Path = project_root / "reports"

    listings_file: str = "listings_sample.csv"
    segments_file: str = "neighbourhood_segments.csv"

    output_file: str = "airbnb_neighbourhood_summary.csv"
    report_file: str = "hw01_a_run_report.md"

    @property
    def listings_path(self) -> Path:
        return self.raw_dir / self.listings_file

    @property
    def segments_path(self) -> Path:
        return self.raw_dir / self.segments_file

    @property
    def output_path(self) -> Path:
        return self.processed_dir / self.output_file

    @property
    def report_path(self) -> Path:
        return self.reports_dir / self.report_file
