# scripts/load_to_database.py

import sqlite3
import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path("outputs")
DB_FINAL = Path("data/dbFinal.db")
DB_FINAL.parent.mkdir(exist_ok=True)

# Definimos qué archivos cargar y sus nombres de tabla
archivos_tablas = {
    "usuarios_api.csv": "usuarios_api",
    "clientes_csv_limpio.csv": "clientes_csv",
    "productos_json.csv": "productos_json",
    "ventas_excel.csv": "ventas_excel",
    "clientes_sqlite.csv": "clientes_sqlite"
}

def cargar_csv_en_bd():
    conn = sqlite3.connect(DB_FINAL)
    for archivo, tabla in archivos_tablas.items():
        ruta = OUTPUT_DIR / archivo
        if ruta.exists():
            print(f"Cargando {archivo} en tabla {tabla}...")
            df = pd.read_csv(ruta)
            df.to_sql(tabla, conn, if_exists="replace", index=False)
        else:
            print(f"Archivo no encontrado: {ruta}")
    conn.close()
    print(f"\nBase de datos final creada: {DB_FINAL}")

if __name__ == "__main__":
    cargar_csv_en_bd()
