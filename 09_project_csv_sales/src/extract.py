import csv, json
from datetime import datetime
from collections import defaultdict

# ═══ EXTRACT: leer datos ═══════════════════════════════════════
def extract_sales(csv_route):
    """Lee el CSV y devuelve una lista de diccionarios (datos crudos)."""
    with open(csv_route, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        return list(reader)

