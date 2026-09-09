import csv

# ═══ EXTRACT: leer datos ═══════════════════════════════════════
def extraer_ventas(ruta_csv):
    """Lee el CSV y devuelve una lista de diccionarios (datos crudos)."""
    with open(ruta_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        return list(reader)

