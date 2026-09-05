# List and Dictionaries

### Operaciones esenciales con listas

```python

precios = [299.99, 49.99, 899.00, 129.50, 1499.00]


# Buscar
print(precios.index(899.00))
```

### Diccionarios: datos con nombre

```python

# Un registro de venta como diccionario
venta = {
    "id": "VNT-2024-001",
    "fecha": "2024-01-15",
    "cliente": "María García",
    "producto": "Monitor 4K",
    "cantidad": 2,
    "precio_unitario": 349.99,
    "impuesto": 0.21,
}

# Acceso seguro con .get() (no explota si la clave no existe)
descuento = venta.get("descuento", 0) # 0 si no existe
```

### Lista de diccionarios: tus futuros DataFrames

```python

# Una "tabla" de ventas como lista de diccionarios
ventas = [
    {"fecha": "2024-01-15", "producto": "Laptop", "importe": 1299.00},
    {"fecha": "2024-01-15", "producto": "Monitor", "importe": 349.99},
    {"fecha": "2024-01-16", "producto": "Teclado", "importe": 79.99},
    {"fecha": "2024-01-16", "producto": "Laptop", "importe": 1299.00},
    {"fecha": "2024-01-17", "producto": "Ratón", "importe": 29.99},
]

# Filtrar: ventas de más de 100 euros
grandes = [v for v in ventas if ventas['importe']>100]

# Transformar: extraer solo importes
importes = [v['importe'] for v in ventas]

# Agrupar: ventas por producto
from collections import Counter

productos_vendidos = [v['producto'] for v in ventas]
conteo = Counter(productos_vendidos)
```

