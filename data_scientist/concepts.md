# Data Scientist Concepts

## Para qué sirve RotatingFilenHandler en un proceso que corre sin parar?

**Respuesta:**
- Parte el log en archivos al llegar a un tamaño máximo

**Concepto: Rotación de logs**

Cuando el archivo de log llega a cierto tamaño o antigüedad, se archiva y se empieza uno nuevo, para que no crezca sin fin

- Sin rotación, un proceso que corre 24/7 puede acabar llenando el disco
- Fija maxBytes y backupCount: con su valor por defecto, 0, nunca rota.

## Ha salido cara cinco veces seguidas. Qué probabilidad tiene cara la próxima vez?

**Respuesta:** 
- El mismo 50% de siempre: la moneda no tiene memoria

**Concepto: Sucesos independientes**

Dos sucesos son independientes si saber que ha pasado uno no cambia la probabilidad del otro. Creer lo contrario es la falacia del jugador

- Cada tirada es independiente de las anteriores
- En datos de negocio, sin embargo, casi nada es independiente:
  - la compra de ayer sí afecta a la de hoy

## Si lo que buscas es raro, por qué un detector 'fiable' da todo falsas alarmas?

**Respuesta:**
- Los sanos son tantos que sus pocos errores superan a los aciertos

**Concepto: Tasa base**

Cada cuánto ocurre de verdad lo que se intenta detectar. Sin ella, un porcentaje de acierto no se puede interpretar

- Un 5% de error sobre 99,900 sanos son casi 5,000 falsas alarmas, que tapan a los 99 aciertos
- La prueba no es mala:
  - lo raro es lo que busca

## 5 de 1,000 productos generan el 60% de la facturación, cómo lo resumes?

**Respuesta:**
- Por tramos: qué parte del total genera el top de productos

**Concepto: Ley de potencias**

Distribución donde unos pocos casos concentran casi todo el total. No hay un caso típico; se habla de tramos y de concentración

- En una ley de potencias no hay nada "en el medio": hay muchísimos productos pequeños y un puñado gigante
- Lo informativo es la concentración

## El histograma de sesiones tiene un pico de 4 minutos y otro en 45, qué indica?

**Respuesta:**
- Dos grupos mezclados: hay que segmentarlos antes de promediar

**Concepto: Distribución bimodal**

Una distribución con dos picos. Suele ser señal de dos poblaciones distintas mezcladas, y se trata segmentando antes de promediar

- Una media de 23 minutos no describe a nadie
- Calcula y presenta cada grupo por separado, por ejemplo gratuitos y de pago