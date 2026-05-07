from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

SALES_CSV_PATH = PROJECT_ROOT / "data" / "sales_only_retail.csv"
MASTER_CSV_PATH = PROJECT_ROOT / "data" / "master_flagged_retail.csv"
DB_PATH = PROJECT_ROOT / "data" / "ecommerce_kpis.db"

SALES_TABLE = "sales_only_retail"
MASTER_TABLE = "master_flagged_retail"


def load_table(csv_path, table_name, conn):
    df = pd.read_csv(csv_path)

    df.to_sql(table_name, conn, if_exists="replace", index=False)

    sqlite_count = conn.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    ).fetchone()[0]

    csv_count = len(df)

    print(f"{table_name} CSV rows: {csv_count}")
    print(f"{table_name} SQLite rows: {sqlite_count}")

    if csv_count == sqlite_count:
        print(f"{table_name} row count check passed.")
    else:
        raise ValueError(f"{table_name} row count check failed.")

    print()


def main():
    with sqlite3.connect(DB_PATH) as conn:
        load_table(SALES_CSV_PATH, SALES_TABLE, conn)
        load_table(MASTER_CSV_PATH, MASTER_TABLE, conn)


if __name__ == "__main__":
    main()