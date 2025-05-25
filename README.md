# Proyecto ETL - Extracción de Múltiples Fuentes

Este proyecto implementa el proceso de **extracción de datos (Extract)** de un flujo ETL completo. La tarea consistía en:

> **Implementar la extracción de datos desde al menos cinco fuentes diferentes (de distinto tipo) hacia un repositorio en BD.**
> Las cinco fuentes deben estar relacionadas en el contexto de la BD.

---

## 📁 Estructura del Proyecto

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

## 📌 Fuentes de Datos Utilizadas

| Fuente         | Tipo              | Script                      | Archivo generado                   |
|----------------|-------------------|------------------------------|-------------------------------------|
| API pública    | API REST          | `extract_from_api.py`        | `usuarios_api.csv`                 |
| CSV local      | Archivo plano     | `extract_from_csv.py`        | `clientes_csv_limpio.csv`          |
| JSON estruct.  | Archivo anidado   | `extract_from_json.py`       | `productos_json.csv`               |
| Excel          | Archivo `.xlsx`   | `extract_from_excel.py`      | `ventas_excel.csv`                 |
| SQLite         | Base de datos     | `extract_from_mysql.py`      | `clientes_sqlite.csv`              |

---

## 🏁 Carga Final

Todos los archivos `.csv` generados son integrados en una base de datos central (`repositorio_final.db`) mediante el script:

```bash
py scripts/load_to_database.py
```

---

## ✅ Requisitos

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

## ✨ Resultado

Se genera una base de datos con 5 tablas (una por fuente), lo que permite integrar información desde distintos orígenes en un solo repositorio consultable.

