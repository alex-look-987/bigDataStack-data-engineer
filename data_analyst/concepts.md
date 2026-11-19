# Data Analyst

## Cuándo conviene sustituir NTILE por rangos manuales con CASE WHEN?

**Respuesta:**
- Cuando el gasto está muyb sesgado y NTILE mezcla clientes distintos

**Concepto:**

TO BE COMPLETED

## En RFM, qué mide la R, F y la M?

**Respuesta:**
- Días desde la última compra, número de compras y dinero gastado

**Concepto: Recency, Frequency, Monetary**

Tres números por cliente

- Cuánto hace de la última compra
- Cuántas compras hizo 
- Cuánto dinero gastó

Los tres grupos salen de una tabla de compras con cliente, fecha e importe:
- un GROUP BY con MAX de la fecha: COUNT y SUM

## qué precio es un atributo de la dimensión de producto y no un hecho?

**Respuesta:**
- El precio de lista que el producto tiene en el catálogo

**Concepto:**

TO BE COMPLETED

## Una tabla tiene millones de filas, claves y columnas numéricoas, qué es?

**Respuesta:**
- Una tabla de hechos, donde se guardan los eventos con sus números

**Concepto: Tabla de hechos**

Registra eventos del negocio (ventas, clicks, envíos). Tiene métricas que se suman y claves que se apuntan a las dimensiones

- Las dimensiones son pequeñas y de texto descriptivo.
- Muchas filas, números y claves apuntan a un hecho

## 