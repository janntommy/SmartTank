import requests
import json
from pathlib import Path
from datetime import datetime
import calendar


def download_nbp_eur(year: int = 2026):
    project_root = Path(__file__).resolve().parents[2]
    dir = project_root / "data" / "raw" / "nbp_eur"
    dir.mkdir(parents=True, exist_ok=True)

    current_month = datetime.now().month

    for month in range(1, current_month + 1):
        last_day = calendar.monthrange(year, month)[1]

        if month == current_month:
            last_day = datetime.now().day

        start_date = f"{year}-{month:02d}-01"
        end_date = f"{year}-{month:02d}-{last_day:02d}"

        url = f"http://api.nbp.pl/api/exchangerates/rates/a/eur/{start_date}/{end_date}/?format=json"
        response = requests.get(url)

        if response.status_code == 200:
            file_name = f"nbp_eur_{year}_{month:02d}.json"
            file_path = dir / file_name

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(response.json(), file, indent=4)

            print(f"Succesfully downloaded 2026-{month:02d}-{last_day:02d} nbp_eur file")
        else:
            print("Error, cannot download nbp_eur file")
if __name__ == "__main__":
    download_nbp_eur()
