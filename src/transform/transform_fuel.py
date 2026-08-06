import pandas as pd
from pathlib import Path

def transform_fuel():
    root = Path(__file__).resolve().parents[2]
    raw_dir = root / "data" / "raw" / "fuel"
    transformed_dir = root / "data" / "transformed" / "fuel_t"

    transformed_dir.mkdir(parents=True, exist_ok=True)

    input_file = raw_dir / "eu_oil_bulletin.csv"

    df = pd.read_csv(input_file)
    df["date"] = pd.to_datetime(df["date"])

    output_file = transformed_dir / "eu_oil_bulletin_t.csv"
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    transform_fuel()