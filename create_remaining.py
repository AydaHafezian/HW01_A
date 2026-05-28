from pathlib import Path

# 3. validate.py
validate_code = """import pandas as pd

def validate_data(df: pd.DataFrame):
    required_columns = ["neighbourhood", "price", "listing_id"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    
    if (df["price"] < 0).any():
        raise ValueError("Found negative prices in data.")
    
    print("Validation successful!")
"""
Path("src/airbnb_ops/validate.py").write_text(validate_code)

# 4. cli.py
cli_code = """import typer
from pathlib import Path
from airbnb_ops.extract import read_csv_checked
from airbnb_ops.pii import handle_pii
from airbnb_ops.transform import build_neighbourhood_summary
from airbnb_ops.validate import validate_data

app = typer.Typer()

@app.command()
def process(listings: Path, segments: Path):
    df = read_csv_checked(listings)
    df = handle_pii(df)
    validate_data(df)
    
    segments_df = read_csv_checked(segments)
    result = build_neighbourhood_summary(df, segments_df)
    
    print(result.head())
    print("Pipeline finished successfully.")

if __name__ == "__main__":
    app()
"""
Path("src/airbnb_ops/cli.py").write_text(cli_code)

print("Created validate.py and cli.py successfully.")