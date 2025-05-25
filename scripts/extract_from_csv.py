# scripts/extract_from_csv.py

import pandas as pd
from pathlib import Path
from datetime import datetime

# Rutas
INPUT_FILE = Path("data/csv/clientes.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def extraer_desde_csv():
    try:
        # Leer CSV
        df = pd.read_csv(INPUT_FILE)

        # Validaciones mínimas
        if df.isnull().values.any():
            print("Advertencia: el archivo contiene valores nulos.")

        # Agregar fecha de extracción
        df["fecha_extraccion"] = datetime.now().isoformat()

        # Guardar en outputs
        salida = OUTPUT_DIR / "clientes_csv_limpio.csv"
        df.to_csv(salida, index=False)
        print(f"Datos CSV procesados correctamente: {salida}")

    except FileNotFoundError:
        print(f"Archivo no encontrado: {INPUT_FILE}")
    except Exception as e:
        print(f"Error al procesar CSV: {e}")

if __name__ == "__main__":
    extraer_desde_csv()
