import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv


def load_to_db():
    load_dotenv()

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    root = Path(__file__).resolve().parents[2]
    fuel_data = root / "data" / "transformed" / "fuel_t" / "eu_oil_bulletin_t.csv"
    nbp_eur_data = root / "data" / "transformed" / "nbp_eur_t" / "nbp_eur_2026_t.csv"

    connection = None
    cur = None

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        cur = connection.cursor()

        if not nbp_eur_data.exists():
            print("NBP_EUR_DATA file not found.")
        else:
            with open(nbp_eur_data, "r") as file:
                cur.copy_expert("COPY nbp_eur FROM STDIN WITH CSV HEADER", file)
            print("Successfully inserted nbp_eur_2026_t.csv into database")


        if not fuel_data.exists():
            print("FUEL DATA file not found.")
        else:
            with open(fuel_data, "r") as file:
                cur.copy_expert("COPY fuel FROM STDIN WITH CSV HEADER", file)
            print("Successfully eu_oil_bulletin_t.csv into database")



        connection.commit()

    except Exception as e:
        print(f"ERROR DURING INSERTING DATA: {e}")
        if connection:
            connection.rollback()

    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    load_to_db()