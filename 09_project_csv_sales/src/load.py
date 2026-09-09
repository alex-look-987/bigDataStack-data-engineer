# ═══ LOAD: escribir resultados ═════════════════════════════════
import json


def guardar_resultados(resumen, errores, ruta_salida, ruta_errores):
    """Escribe el resumen y los errores en archivos JSON"""

    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=2, ensure_ascii=False)

        if errores:
            with open(ruta_errores, "w", encoding="utf-8") as f:
                json.dump(errores, f, indent=2, ensure_ascii=False)

