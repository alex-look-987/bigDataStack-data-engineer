# 08: pip install: usar herramientas de otros

## Crear y activar el venv — Windows vs Mac

```bash
# 1. Crea una carpeta para tu proyecto
mkdir mi-proyecto-datos
cd mi-proyecto-datos

# 2. Crea el entorno virtual
python3 -m venv .venv

# 3. Actívalo
source .venv/bin/activate

# 4. Tu prompt cambia:
# (.venv) usuario@mac mi-proyecto-datos %

# 5. Verifica que python apunta al venv
python --version
# Python 3.12.4

```

```bash
## ¿Qué es pip y cómo funciona?

pip install requests
pip install pandas

# (Dentro del venv, "pip" funciona igual en ambos sistemas)

# Instalar una versión específica
pip install requests==2.31.0

# Instalar versión mínima
pip install "requests>=2.28"

# Ver qué tienes instalado
pip list

# Ver detalles de un paquete
pip show requests
```

## requirements.txt: la receta de tu proyecto

```bash
# Generar requirements.txt con lo que tienes instalado
pip freeze > requirements.txt

# El archivo contiene algo como:
# requests==2.31.0
# pandas==2.1.4
# numpy==1.26.2

# Instalar todo desde requirements.txt (otro dev, otro PC)
pip install -r requirements.txt
```

## Librerías esenciales para trabajar con datos

### Las que vas a usar seguro, vayas por donde vayas:

- **pandas** — manipular datos en tablas (DataFrames). Es la librería central de todo profesional de datos.

- **requests** — pedir datos a una API por HTTP.

- **python-dotenv** — leer configuración desde un fichero .env, sin escribir contraseñas en el código.
  
### Si vas por análisis de datos:

- **matplotlib/seaborn** — hacer gráficos. Las verás en la sección de visualización.

- **openpyxl** — leer y escribir ficheros de Excel (.xlsx) desde Python. La necesitarás el día que te manden el informe en Excel.

- **jupyter** — trabajar en notebooks, que es donde se explora antes de escribir el script definitivo.

### Si vas por ingeniería de datos:

- **pytest** — escribir tests que comprueban que tu proceso sigue funcionando.

- **pyyaml** — leer y escribir ficheros YAML, el formato de configuración de casi todas las herramientas.

- **mypy** — avisar de errores de tipos antes de ejecutar.
Y una que le viene bien a todo el mundo: black — formatea tu código solo, siempre igual. Se acabó discutir dónde van los espacios.

## Tu primer script con librerías externas

```bash
# Instala python-dotenv (dentro de tu venv)
pip install python-dotenv


```