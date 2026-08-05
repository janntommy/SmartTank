import requests
from pathlib import Path
from datetime import datetime

def download_fuel():
    url = "https://ec.europa.eu/energy/observatory/reports/History_Prices_with_taxes.xlsx"
    response = requests.get(url)

    if response.status_code == 200:
        dir = Path(__file__).parent.parent.parent / "data" / "raw" / "fuel"
        dir.mkdir(parents=True, exist_ok=True)

        today = datetime.now().strftime('%Y-%m-%d')
        file_name = f"fuel_raw_{today.replace("-","_")}.xlsx"
        file_path = dir / file_name

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print("Successfully downloaded fuel file")
        return str(file_path)
    else:
        return None

if __name__ == "__main__":
    download_fuel()