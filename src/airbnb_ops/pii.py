import hashlib
import pandas as pd


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