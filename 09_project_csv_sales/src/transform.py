

# ═══ TRANSFORM: limpiar y calcular ═════════════════════════════
def transformar_ventas(ventas_raw: list[dict]):
    """Limpia datos sucios y calcula totales. Devuelve (limpias, errores)."""

    limpias = []
    errores = []

    for i, venta in enumerate(ventas_raw):
        try:
            # validar producto no vacío
            if not (venta.get("producto", "")).strip():
                raise ValueError("Producto vacío")

            # convertir cantidad (default 1 si vacío)
            cantidad_raw = venta.get("cantidad", "").strip()
            cantidad = int(cantidad_raw) if cantidad_raw else 1

            # convertir precio
            precio = float(venta['precio_unitario'])

            # calcular total
            total = cantidad * precio

            # registro limpio
            limpias.append({
                "fecha": venta["fecha"],
                "producto": venta["producto"].strip(),
                "categoria": venta["categoria"].strip(),
                "cantidad": cantidad,
                "precio_unitario": precio,
                "total": round(total, 2),
                "cliente": venta["cliente"].strip(),
            })
        except (ValueError, TypeError) as e:
            errores.append({
                "fila": i + 2, # +2 por header y 0-index
                "error": str(e),
                "datos": dict(venta),
            })

    return limpias, errores