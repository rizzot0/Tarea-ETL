# scripts/extract_from_json.py

import pandas as pd
from pathlib import Path
from datetime import datetime

# Ruta del JSON de entrada y del CSV de salida
INPUT_FILE = Path("data/json/productos.json")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def extraer_desde_json():
    try:
        # Leer y normalizar JSON
        df = pd.read_json(INPUT_FILE)
        df = pd.json_normalize(df.to_dict(orient='records'))

        # Validación básica
        if df.empty:
            print("Advertencia: archivo JSON vacío.")
        
        # Agregar fecha de extracción
        df["fecha_extraccion"] = datetime.now().isoformat()

        # Guardar salida
        salida = OUTPUT_DIR / "productos_json.csv"
        df.to_csv(salida, index=False)
        print(f"Datos JSON procesados correctamente: {salida}")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {INPUT_FILE}")
    except Exception as e:
        print(f"Error al procesar JSON: {e}")

if __name__ == "__main__":
    extraer_desde_json()
