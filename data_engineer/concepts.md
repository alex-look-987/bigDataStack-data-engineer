# Data Engineer

## Un executor se cae y pierde sus particiones, cómo las recupera Spark?

**Respuesta:**
- Repite las transformaciones registradas sobre esas particiones

**Concepto: Linaje (lineage)**

El registro de las transformaciones que originaron cada conjunto de datos. Spark lo recorre para recalcular solo lo perdido, sin guardar copias

- Spark no replica los datos: guarda la receta para rehacerlos
- Por eso puede tolerar fallos sin pagar el coste de triplicar el almacenamiento

## Por qué Spark es mucho más rápido que MapReduce en pipelines de varios pasos?

**Respuesta:**
- Encadena los pasos en memoria en vez de pasar por disco entre cada uno

**Concepto: Datos intermedios en memoria**

1. MapReduce guarda en disco el resultado de cada paso.
2. Spark encadena en memoria los pasos que no reordenan datos:
    - El shuffle escribe a disco local, y también se vuelca lo que no cabe en memoria

- MapReduce escribría y leía disco entre cada fase.
- Spark encadena en memoria lo que no necesita reordenar
- El shufgle sí escribe a disco, y cache() guarda lo que reutiliza

## Quieres parar el laboratorio sin perder los datos de los volúmenes, qué haces?

**Respuesta:**
- Ejecutas docker compose down, sin la opción -v

**Concepto:**

TO BE COMPLETED

## Pasas una ruta local a spark.read.csv en un clúster, qué debe cumplirse?

**Respuesta:**
- La ruta debe verse igual desde el driver y desde cada nodo con tasks

**Concepto: Rutas en un clúster**

1. Los executors abren el fichero en sus nodos
2. Una ruta local debe verse igual desde el drive y desde cada nodo donde se ejecuten tasks

- Si el fichero no está en el worker, el fallo aparece más tarde dentro de tasks
- Por eso se monta el mismo volumen en todos los servicios
  
## Llamas a count() y luego a show() sobre el mismo pipeline sin cache, qué pasa?

**Respuesta:**
- Cada acción recalcula todo el pipeline desde el orgen

**Concepto: cache()**

1. Marca un DataFrame para guardarlo en memoria (y en disco si no cabe) tras su primera acción
2. Sin él, cada acción recalcula la cadena de transformaciones desde el origen

- Un DataFrame guarda la receta, no los datos.
- Con dos o más acciones sobre el mismo resultado, cache() evita pagar el cálculo varias veces


## Qué riesgo tiene llamar a collect() sobre un DataFrame de miles de millones de filas?

**Respuesta:**
- Trae todas las filas al driver y peude agotar su memoria

**Concepto: collect()**

1. Acción que trae todas las filas al driver, que es una sola máquina
2. Con un DataFrame grande se queda sin memoria, como el problema original de Pandas

- Los datos estaban repartidos para no caber en una máquina
  - collect() los junta en una
- Para ver una muestra basta con:
  - show() o take()
  
## Encadenas filter, select y groupBy sobre un DataFrame, cuándo trabaja Spark?

**Respuesta:**
- Cuando una acción como count o write pide el resultado

**Concepto: Evaluación perezosa**

1. Las transformaciones solo se anotan en u nada
    - se calcula hasta que una acción (count, show, write) pide un resultado
  
- Hasta la acción solo se construye el plan
- Verlo completo permite a Spark optimizarlo antes de gastar tiempo del cálculo

## Cruzaz millones de ventas con una table de 200 países, qué te conviene?

**Respuesta:**
- un broadcast de la tabla pequeña, sin mover la de ventas

**Concepto: Broadcast join**

Spark envía la tabla pequeña completa a cada nodo, que la cruza localmente con su parte de la grande. Así la tabla grande no se mueve por la red

- Se difunde la tabla que cabe en memoria.
- Hacerlo con la de ventas, enorme, agotaría la memoria de los executors

