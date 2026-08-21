import requests
import json
from pathlib import Path
from datetime import datetime
import calendar


def download_nbp_eur(year: int = 2020):
    project_root = Path(__file__).resolve().parents[2]
    dir = project_root / "data" / "raw" / "nbp_eur"
    dir.mkdir(parents=True, exist_ok=True)

    current_date = datetime.now()

    if year == current_date.year:
        max_month = current_date.month
    else:
        max_month = 12

    for month in range(1, max_month + 1):
        last_day = calendar.monthrange(year, month)[1]

        if year == current_date.year and month == current_date.month:
            last_day = current_date.day

        start_date = f"{year}-{month:02d}-01"
        end_date = f"{year}-{month:02d}-{last_day:02d}"

        url = f"http://api.nbp.pl/api/exchangerates/rates/a/eur/{start_date}/{end_date}/?format=json"
        response = requests.get(url)

        if response.status_code == 200:
            file_name = f"nbp_eur_{year}_{month:02d}.json"
            file_path = dir / file_name

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(response.json(), file, indent=4)

            print(f"Succesfully downloaded {year}-{month:02d}-{last_day:02d} nbp_eur file")
        else:
            print(f"Error, cannot download nbp_eur file for {start_date} to {end_date}")


if __name__ == "__main__":
    download_nbp_eur(2021)
    download_nbp_eur(2022)
    download_nbp_eur(2023)
    download_nbp_eur(2024)
    download_nbp_eur(2025)
    download_nbp_eur(2026)
