# File: Dockerfile (no extension)
FROM python:3.12-slim

WORKDIR /app

# Primero copiamos SOLO requiriments.txt (truco de cache)
COPY requiriments.txt .

RUN pip install --no-cache-dir -r requiriments.txt

# Luego copiamos el código
COPY app.py .

CMD ["python", "app.py"]