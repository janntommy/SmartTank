from pathlib import Path
import pandas as pd
import json


def transform_nbp_eur():
    root = Path(__file__).resolve().parents[2]
    raw_dir = root / "data" / "raw" / "nbp_eur"
    transformed_dir = root / "data" / "transformed" / "nbp_eur_t"

    transformed_dir.mkdir(parents=True, exist_ok=True)

    all_files = []

    for file_path in sorted(raw_dir.glob("nbp_eur_*.json")):
        with open(file_path, 'r') as file:
            data = json.load(file)
            all_files.extend(data['rates'])

    if not all_files:
        return None

    original_df = pd.DataFrame(all_files)
    df = original_df[["effectiveDate", "mid"]]
    df.columns = ["date", "eur_to_pln_rate"]
    df["date"] = pd.to_datetime(df["date"])


    output_dir = transformed_dir / "nbp_eur_t.csv"
    df.to_csv(output_dir, index=False)

    # print(df.head(10))

if __name__ == "__main__":
    transform_nbp_eur()