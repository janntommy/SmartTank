from src.download.download_nbp_eur import download_nbp_eur
from src.sql_py.convert_to_pln import convert_eur_to_pln
from src.sql_py.execute_sql_setup import execute_sql_setup
from src.sql_py.load_to_db import load_to_db
from src.transform.transform_fuel import transform_fuel
from src.transform.transform_nbp_eur import transform_nbp_eur


def run_smarttank():
    try:
        print("Starting SmartTank...")

        print("\n1. DOWNLOADING NBP_EUR DATA...")
        download_nbp_eur()

        print("\n2. TRANSFORMING FUEL DATA...")
        transform_fuel()

        print("\n3. TRANSFORMING NBP_EUR DATA...")
        transform_nbp_eur()

        print("\n4. CREATING AND LOADING DATABASE...")
        execute_sql_setup()

        print("\n5. LOADING DATA INTO DATABASE...")
        load_to_db()

        print("\n6. CONVERTING EUR TO PLN VALUE...")
        convert_eur_to_pln()

        print("\nSMARTTANK COMPLETE!")

    except Exception as e:
        print(f"ERROR DURING RUNNING MAIN PROGRAMME: {e}")

if __name__ == "__main__":
    run_smarttank()