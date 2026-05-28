import pandas as pd


def build_neighbourhood_summary(listings: pd.DataFrame,
                                segments: pd.DataFrame) -> pd.DataFrame:
    # فرض: listings شامل ستون‌های neighbourhood و price
    # و segments شامل ستون‌های neighbourhood و segment است.

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