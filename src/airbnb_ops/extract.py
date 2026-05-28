from pathlib import Path
import pandas as pd


def read_csv_checked(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected CSV at {path}, but it does not exist.")
    return pd.read_csv(path)