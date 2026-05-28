import pandas as pd


def validate_summary(summary: pd.DataFrame) -> None:
    if summary.empty:
        raise ValueError("Summary dataframe is empty.")

    required_cols = {"neighbourhood", "avg_price", "n_listings"}
    missing = required_cols - set(summary.columns)
    if missing:
        raise ValueError(f"Summary is missing expected columns: {missing}")