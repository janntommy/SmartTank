import requests
import json
from pathlib import Path
from datetime import datetime, timedelta

def download_nbp_eur(days: int = 90):
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    url = f"http://api.nbp.pl/api/exchangerates/rates/a/eur/{start_date}/{end_date}/?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        script_dir = Path(__file__).parent.resolve()
        dir = script_dir.parent.parent / "data" / "raw" / "nbp_eur"
        dir.mkdir(parents=True, exist_ok=True)

        file_path = dir / f"nbp_eur_raw_{end_date.replace("-", "_")}.json"

        if file_path.exists():
            print("Nbp_eur file already exists")
        else:
            with open(file_path, 'w') as file:
                json.dump(response.json(), file, indent=4)

            print("Successfully downloaded nbp_eur file")
        return file_path

    else:
        return None

if __name__ == "__main__":
    download_nbp_eur()