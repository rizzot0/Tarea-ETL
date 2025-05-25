# scripts/extract_from_excel.py

import pandas as pd
from pathlib import Path
from datetime import datetime

# Rutas
INPUT_FILE = Path("data/excel/ventas.xlsx")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def extraer_desde_excel():
    try:
        df = pd.read_excel(INPUT_FILE)

        if df.empty:
            print("Archivo Excel vacío.")
            return

        # Agregar fecha de extracción
        df["fecha_extraccion"] = datetime.now().isoformat()

        # Guardar en CSV
        salida = OUTPUT_DIR / "ventas_excel.csv"
        df.to_csv(salida, index=False)
        print(f"Datos Excel procesados correctamente: {salida}")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {INPUT_FILE}")
    except Exception as e:
        print(f"Error al procesar Excel: {e}")

if __name__ == "__main__":
    extraer_desde_excel()
