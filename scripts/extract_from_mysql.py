# scripts/extract_from_mysql.py

import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime

DB_PATH = Path("data/sqlite/clientes.db")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def extraer_desde_sqlite():
    try:
        conn = sqlite3.connect(DB_PATH)
        query = "SELECT * FROM clientes"
        df = pd.read_sql_query(query, conn)

        if df.empty:
            print("La tabla 'clientes' está vacía.")
            return

        df["fecha_extraccion"] = datetime.now().isoformat()

        salida = OUTPUT_DIR / "clientes_sqlite.csv"
        df.to_csv(salida, index=False)
        print(f"Datos extraídos desde SQLite correctamente: {salida}")
        conn.close()

    except Exception as e:
        print(f"Error al extraer desde la base de datos: {e}")

if __name__ == "__main__":
    extraer_desde_sqlite()
