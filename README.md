# Proyecto ETL - Extracción de Múltiples Fuentes

Este proyecto implementa el proceso de **extracción de datos (Extract)** de un flujo ETL completo. La tarea consistía en:

> **Implementar la extracción de datos desde al menos cinco fuentes diferentes (de distinto tipo) hacia un repositorio en BD.**
> Las cinco fuentes deben estar relacionadas en el contexto de la BD.

---

##  Estructura del Proyecto

```
ETL/
├── data/
│   ├── csv/
│   ├── json/
│   ├── excel/
│   ├── sqlite/
│   └── repositorio_final.db
├── outputs/
│   └── *.csv  ← Archivos extraídos desde cada fuente
├── scripts/
│   ├── extract_from_api.py
│   ├── extract_from_csv.py
│   ├── extract_from_json.py
│   ├── extract_from_excel.py
│   ├── extract_from_mysql.py (usa SQLite)
│   └── load_to_database.py
└── README.md
```

---

##  Fuentes de Datos Utilizadas

| Fuente         | Tipo              | Script                      | Archivo generado                   |
|----------------|-------------------|------------------------------|-------------------------------------|
| API pública    | API REST          | `extract_from_api.py`        | `usuarios_api.csv`                 |
| CSV local      | Archivo plano     | `extract_from_csv.py`        | `clientes_csv_limpio.csv`          |
| JSON estruct.  | Archivo anidado   | `extract_from_json.py`       | `productos_json.csv`               |
| Excel          | Archivo `.xlsx`   | `extract_from_excel.py`      | `ventas_excel.csv`                 |
| SQLite         | Base de datos     | `extract_from_mysql.py`      | `clientes_sqlite.csv`              |

---

## Comandos para ejecutar los scripts

Asegúrate de estar ubicado en la carpeta del proyecto. Ejecuta cada script en este orden:

```bash
# 1. Extracción desde API
py scripts/extract_from_api.py

# 2. Extracción desde archivo CSV
py scripts/extract_from_csv.py

# 3. Extracción desde archivo JSON
py scripts/extract_from_json.py

# 4. Extracción desde archivo Excel
py scripts/extract_from_excel.py

# 5. Extracción desde base de datos SQLite
py scripts/extract_from_mysql.py

# 6. Carga final a base de datos unificada
py scripts/load_to_database.py
```

---

## Requisitos

- Python 3.10 o superior
- Librerías:
  - `pandas`
  - `requests`
  - `openpyxl`

Instalación recomendada:

```bash
pip install pandas requests openpyxl
```

---

##  Resultado

Se genera una base de datos con 5 tablas (una por fuente), lo que permite integrar información desde distintos orígenes en un solo repositorio consultable.

