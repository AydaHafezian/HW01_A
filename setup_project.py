import os
from pathlib import Path

# 1. Create folders
folders = ["src/airbnb_ops", "data/raw", "data/processed", "reports", "tests"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")

# 2. Create raw CSV files (Mock data)
listings_csv = """listing_id,neighbourhood,price,minimum_nights,availability_365,number_of_reviews,host_name,host_id
1,Downtown,150,2,300,10,Alice,H1
2,Downtown,200,1,365,5,Bob,H2
3,Uptown,100,3,100,2,Charlie,H3
"""

segments_csv = """neighbourhood,tourism_segment,priority_level
Downtown,High,1
Uptown,Medium,2
"""

Path("data/raw/listings_sample.csv").write_text(listings_csv)
Path("data/raw/neighbourhood_segments.csv").write_text(segments_csv)

print("Created raw data files.")
