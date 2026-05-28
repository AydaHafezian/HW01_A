from pathlib import Path

# 1. pii.py
pii_code = """import pandas as pd
import hashlib

def handle_pii(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "host_name" in df.columns: 
        df = df.drop(columns=["host_name"])
    if "host_id" in df.columns:
        df["host_key"] = df["host_id"].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())
        df = df.drop(columns=["host_id"])
    return df
"""
Path("src/airbnb_ops/pii.py").write_text(pii_code)

# 2. transform.py
transform_code = """import pandas as pd

def build_neighbourhood_summary(listings: pd.DataFrame, segments: pd.DataFrame) -> pd.DataFrame:
    summary = listings.groupby("neighbourhood").agg(
        num_listings=("listing_id", "count"),
        avg_price=("price", "mean")
    ).reset_index()
    summary = summary.merge(segments, on="neighbourhood", how="left")
    return summary
"""
Path("src/airbnb_ops/transform.py").write_text(transform_code)

print("Created pii.py and transform.py successfully.")
