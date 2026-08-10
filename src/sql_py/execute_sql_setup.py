import os
from pathlib import Path
import psycopg2
from dotenv import load_dotenv


def execute_sql_setup():
    load_dotenv()

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    root = Path(__file__).resolve().parents[2]
    sql_create_db_file = root / "sql" / "create_db.sql"
    sql_create_tables_file = root / "sql" / "create_tables.sql"

    try:
        with open(sql_create_db_file, 'r') as file:
            sql_create_db = file.read()

        conn_create_db = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn_create_db.autocommit = True
        cur_create_db = conn_create_db.cursor()

        cur_create_db.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}';")
        if not cur_create_db.fetchone():
            cur_create_db.execute(sql_create_db)
            print(f"Successfully created database: {DB_NAME}")
        else:
            print(f"Database {DB_NAME} is already existing.")

    except Exception as e:
        print(f"ERROR DURING CREATING DATABASE: {e}")
        return

    finally:
        if 'cur_create_db' in locals() and cur_create_db:
            cur_create_db.close()

        if 'conn_create_db' in locals() and conn_create_db:
            conn_create_db.close()





    try:
        with open(sql_create_tables_file, 'r') as file:
            sql_create_tables = file.read()

        conn_target = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur_target = conn_target.cursor()
        cur_target.execute(sql_create_tables)
        conn_target.commit()

        print("Successfully created table: nbp_eur.")
        print("Successfully created table: fuel.")

    except Exception as e:
        print(f"ERROR DURING CREATING TABLES: {e}")

        if conn_target:
            conn_target.rollback()

    finally:
        if 'cur_target' in locals() and cur_target:
            cur_target.close()
        if 'conn_target' in locals() and conn_target:
            conn_target.close()


if __name__ == "__main__":
    execute_sql_setup()