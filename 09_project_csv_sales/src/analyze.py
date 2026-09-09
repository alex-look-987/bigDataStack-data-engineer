# ═══ ANALYZE: generar métricas ═════════════════════════════════
from collections import defaultdict
from datetime import datetime


def generar_resumen(ventas_limpias):
    """Genera el resumen ejecutivo a partir de datos limpios."""

    if not ventas_limpias:
        return {"error": "No hay datos válidos"}

    # métricas generales
    total_facturado = sum(v['total'] for v in ventas_limpias)
    num_transacciones = len(ventas_limpias)
    ticked_medio = total_facturado / num_transacciones

    # por categoría
    por_categoria = defaultdict(lambda: {"total":0, "transacciones": 0})
    for v in ventas_limpias:
        cat = v['categoria']
        por_categoria[cat]["total"] += v["total"]
        por_categoria[cat]["transacciones"] += 1

    # top productos
    productos_total = defaultdict(float)
    for v in ventas_limpias:
        productos_total[v["produto"]] += v["total"]

    top_productos = sorted(productos_total.items(), key=lambda x: x[1], reverse=True)[:3]

    # clientes únicos
    clientes = set(v['cliente'] for v in ventas_limpias)

    return {
        "fecha_reporte": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total_facturado": round(total_facturado, 2),
        "num_transacciones": num_transacciones,
        "ticket_medio": ticked_medio,
        "clientes_unicos": len(clientes),
        "por_categoria": dict(por_categoria),
        "top_3_productos": [
            {"producto": p, "total": round(t, 2)} for p, t in top_productos
        ],
    }