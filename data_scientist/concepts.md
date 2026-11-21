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

## Qué consigue activar 'branch protection rules en main'?

**Respuesta:**
- Que no se fusione nada sin cumplir lo exigido, como una revisión

**Concepto: Branch protection rules**

Reglas de GitHub que se aplica a una rama:
- Exigir revisiones
- Test en verde
- Rama actualizada antes de permitir el merge

Convierte el acuerdo del equipo en una regla técnica:
- no depende de que cada persona se acuerde de pedir revisión

## Qué es un Pull Request?

**Respuesta:**
- Una petición para que revisen tu rama antes de fusionarla

**Concepto: Pull Request (PR)**

Una petición para que tu rama entre en otra, con un espacio para ver los cambios, comentarlos y aprobarlos antes de fusionar

El PR es el punto donde el equipo: 
- ve los cambios
- deja comentarios 
- y las pruebas automáticas se ejecutan antes de tocar main

## Qué hace "Squash and merge" al fusionar un PR?

**Respuesta:**
- Mete todos los commits de la rama en main como un único commit

**Concepto: Squash and merge (aplastar y fusionar)**

Aplasta todos los commits de la rama en uno solo y lo añade a main.

El historial queda limpio, pero se pierden los commits intermedios

- Los commits intermedios no pasan main
- Por eso git branch -d suele negarse a borrar la rama (dice que no está del todo fusionada) y hay que usar -D

## Cuándo no puede Git fusionar dos cambios por si solo?

**Respuesta:**
- Cuando dos ramas modifican la misma zona de un mismo archivo

**Concepto: Conflicto de merge**

Ocurre cuando dos ramas cambian la misma zona de un archivo y Git no sabe cuál versión conservar. Hace falta que una persona decida.

- Git une solo los cambios de un mismo archivo si caen en sitios separados
- El choque es de zona, no de archivo

## En un archivo en conflicto, qué hay entre <<<<<<<< y =======?

**Respuesta:**
- La versión de la rama en la que estás, la que recibe el merge

**Concepto: Marcas de conflicto**

1. Git escribe ambas versiones en el archivo
  - Arriba, la de tu rama actual
  - Abajo, la entrante
2. Se resuelve dejando el texto final y borrando las marcas

- Debajo de ====== está la versión entrante.
- Antes de commitear no debe quedar ninguna marca:
  - sería basura dentro del código

## En pleno conflicto no sabes qué hacer, cómo vuelves al estado anterior?

**Respuesta:**
- Ejecutas git merge --abort y todo queda como antes

**Concepto: git merge --abort**

1. Cancela un merge en curso y deja la rama como estaba antes de empezarlo.
2. Se puede intentar de nuevo cuandp se hable con la otra persona

- Abortar no pierde nada:
  - el merge no se completó
- Commitear con marcas dejaría el conflicto sin resolver dentro del historial

## Reorganizas código sin cambiar lo que hace, qué pprefijo de commit usas?

**Respuesta:**
- refactor: reordenar el código sin cambiar lo que hace

**Concepto: Conventional Commits**

Convención para mensajes de commit: un prefijo (feat, fix, docs, refactor) dice qué tipo de cambio es, seguida de una descripción breve

- Fix: corrige errores
- Feat: añade funcionalidades
- Un prefijo claro permite buscar en el historial qué se hizo y por qué

## Qué flujo de ramas basta a un equipo pequeño sin releases con versiones?

**Respuesta:**
- Main y una rama por tarea, que entra por Pull Request

**Concepto: Main + feature branches**

**Flujo mínimo:**
1. Main siempre funciona
2. Cada tarea va en su rama y entra por Pull Request
3. Gitflow completo añade: develop, release, hotfix

Las ramas extras del Gitflow complete solo compensan si hay versiones empaquetadas o alguien que las prueba antes de publicarlas. Si no, es burocracia

## En una plantilla con un sueldo altísimo, qué pasa con el sueldo medio?

**Respuesta:**
- Queda por encima de lo que cobra la mayoría de la plantilla entera

**Concepto: Media aritmética**

1. La suma de todos los valores dividida entre cuántos hay
2. ES sensible a los valores extremos, que la arrastran hacia su lado

- Un valor muy alto tira de la media hacia arriba, y la mediana ni se mueve
- Por eso la mayoría puede cobrar menos que el sueldo medio

## Qué medida responde a "Cuál es el plan más contratado"?

**Respuesta:**
- La moda: el valor que aparece más veces en los datos

**Concepto: Moda**

1. El valoe que más se repite
2. Es la medida natural con categorías, como planes o colores, donde no se pueden promediar

- Con categorías no se puede promediar
- Lo que sí se puede hacer es contar, y el más contado es la moda
- El recuento total no distingue entre planes

## En un bloxplot, hasta dónde llega el bigote superior?

**Respuesta:**
- Al dato más alto dentro de 1,5 veces el IQR desde la caja

**Concepto: Boxplot (caja y bigotes)**

1. Gráfico con la caja de Q1 a Q3 y la mediana dentro
2. Los bigotes llegan al dato más extremo dentro de 1,5 veces el IQR; el resto son puntos

- Lo que queda más allá del bigote se dibuja como punto suelto:
  - Es un posible valor atípico
- El bigote no tiene por qué llegar al máximo

## Entra un sueldo altísimo, qué medida de dispersión apenas se mueve?

**Respuesta:**
- El rango intercuartílico, porque solo mira el 50% central

**Concepto: Rango intercuartílico (IQR)**

1. La distancia entre el primer y el tercer cuartil:
- el ancho del 50% de los datos.
2. Ignora el 25% de cada extremo

- El rango y la desviación típica usan los extremos y se disparan
- El IQR solo mira dónde empieza y acaba la caja centra