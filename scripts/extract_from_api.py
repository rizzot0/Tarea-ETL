# scripts/extract_from_api.py

import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

# Ruta de salida
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def extraer_usuarios_api():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return

    datos = response.json()

    # Normalizar datos JSON anidados
    df = pd.json_normalize(datos)

    # Agregar metadatos de extracción
    df["fecha_extraccion"] = datetime.now().isoformat()

    # Guardar como CSV
    archivo_salida = OUTPUT_DIR / "usuarios_api.csv"
    df.to_csv(archivo_salida, index=False)

    print(f"Datos extraídos y guardados en {archivo_salida}")

if __name__ == "__main__":
    extraer_usuarios_api()
