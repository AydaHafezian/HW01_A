from pathlib import Path
import hashlib

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"

LISTINGS_PATH = RAW_DIR / "listings_sample.csv"
SEGMENTS_PATH = RAW_DIR / "neighbourhood_segments.csv"

OUTPUT_PATH = PROCESSED_DIR / "airbnb_neighbourhood_summary.csv"
REPORT_PATH = REPORTS_DIR / "hw01_a_run_report.md"


def read_csv_checked(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected CSV at {path}, but it does not exist.")
    return pd.read_csv(path)


def handle_pii(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "host_id" in df.columns:
        df["host_key"] = (
            df["host_id"]
            .astype("string")
            .apply(
                lambda x: hashlib.sha256(x.encode("utf-8")).hexdigest()
                if x is not None
                else None
            )
        )

    if "host_name" in df.columns:
        df = df.drop(columns=["host_name"])

    return df


def build_neighbourhood_summary(listings: pd.DataFrame,
                                segments: pd.DataFrame) -> pd.DataFrame:
    listings_grouped = (
        listings
        .groupby("neighbourhood", as_index=False)
        .agg(
            avg_price=("price", "mean"),
            n_listings=("id", "count"),
        )
    )

    merged = listings_grouped.merge(
        segments,
        on="neighbourhood",
        how="left",
        validate="one_to_one",
    )

    return merged


def validate_summary(summary: pd.DataFrame) -> None:
    if summary.empty:
        raise ValueError("Summary dataframe is empty.")

    required_cols = {"neighbourhood", "avg_price", "n_listings"}
    missing = required_cols - set(summary.columns)
    if missing:
        raise ValueError(f"Summary is missing expected columns: {missing}")


def main() -> None:
    # اطمینان از وجود پوشه‌ها
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # 1) خواندن داده خام
    listings = read_csv_checked(LISTINGS_PATH)
    segments = read_csv_checked(SEGMENTS_PATH)

    # 2) PII
    listings = handle_pii(listings)

    # 3) ترنسفورم
    summary = build_neighbourhood_summary(listings, segments)

    # 4) اعتبارسنجی
    validate_summary(summary)

    # 5) ذخیره CSV خروجی
    summary.to_csv(OUTPUT_PATH, index=False)

    # 6) ساخت گزارش
    report_lines = [
        "# HW01-A run report",
        "",
        f"- Output rows: {len(summary)}",
        f"- Output path: {OUTPUT_PATH}",
    ]
    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Pipeline finished. Output: {OUTPUT_PATH}")
    print(f"Report: {REPORT_PATH}")


if __name__ == "__main__":
    main()
