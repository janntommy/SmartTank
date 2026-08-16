import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv


def convert_eur_to_pln():
    load_dotenv()

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    root = Path(__file__).resolve().parents[2]
    sql_view_file = root / "sql" / "views" / "convert_fuel_price_to_pln.sql"

    try:
        with open(sql_view_file, "r") as file:
            sql_file = file.read()

        conn_viewpln = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        conn_viewpln.autocommit = True
        cur_viewpln = conn_viewpln.cursor()

        cur_viewpln.execute(sql_file)
        print("Successfully created view fuel_pln.")

    except Exception as e:
        print(f"ERROR DURING CREATING VIEW: {e}")
    finally:
        if cur_viewpln:
            cur_viewpln.close()
        if conn_viewpln:
            conn_viewpln.close()

if __name__ == "__main__":
    convert_eur_to_pln()