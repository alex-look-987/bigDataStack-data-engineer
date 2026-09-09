import os
from src.generate_data import generar_ventas, ventas
from src.analyze import generar_resumen
from src.extract import extraer_ventas
from src.load import guardar_resultado
from src.transform import transformar_ventas

CSV_PATH = "09_project_csv_sales/data/"

# ═══ MAIN: orquestar el pipeline ══════════════════════════════
def main():
    """Punto de entrada del pipeline."""
    print("=" * 50)
    print("  PIPELINE DE VENTAS DIARIAS")
    print("=" * 50)
    
    # Configuración
    folder_rooth = "09_project_csv_sales/data/"
    ruta_entrada = f"{folder_rooth}ventas_dia.csv"
    ruta_salida = f"{folder_rooth}resumen_dia.json"
    ruta_errores = f"{folder_rooth}errores_dia.json"

    # Create data
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    generar_ventas(ventas)
    
    # 1. EXTRACT
    print("\n[1/4] Extrayendo datos...")
    ventas_raw = extraer_ventas(ruta_entrada)
    print(f"      Leídos: {len(ventas_raw)} registros")
    
    # 2. TRANSFORM
    print("[2/4] Limpiando y transformando...")
    ventas_limpias, errores = transformar_ventas(ventas_raw)
    tasa_exito = len(ventas_limpias) / len(ventas_raw) * 100
    print(f"      Válidos: {len(ventas_limpias)} ({tasa_exito:.0f}%)")
    print(f"      Errores: {len(errores)}")
    
    # 3. ANALYZE
    print("[3/4] Generando resumen ejecutivo...")
    resumen = generar_resumen(ventas_limpias)
    print(f"      Total facturado: {resumen['total_facturado']}€")
    
    # 4. LOAD
    print("[4/4] Guardando resultados...")
    guardar_resultado(resumen, errores, ruta_salida, ruta_errores)
    print(f"      Resumen: {ruta_salida}")
    if errores:
        print(f"      Errores: {ruta_errores}")
    
    # Reporte final
    print("\n" + "=" * 50)
    print("  RESUMEN EJECUTIVO")
    print("=" * 50)
    print(f"  Facturación total: {resumen['total_facturado']}€")
    print(f"  Ticket medio:      {resumen['ticket_medio']}€")
    print(f"  Transacciones:     {resumen['num_transacciones']}")
    print(f"  Clientes únicos:   {resumen['clientes_unicos']}")
    print(f"\n  Top 3 productos:")
    for item in resumen["top_3_productos"]:
        print(f"    • {item['producto']}: {item['total']}€")
    print("=" * 50)


if __name__ == "__main__":
    main()