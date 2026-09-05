#%%
from pathlib import Path

# Crear archivos de ejemplo 
Path("logs").mkdir(parents=True, exist_ok=True)

for i in range(1, 4):
    with open(f"logs/server_{i}.txt", "w") as f:
        for j in range(i * 10):
            f.write(f"[INFO] Evento {j} del servidor {i}\n")

#%%

# sorted() fija el orden alfabético: glob() solo devuelve lo que encuntraa
archivos = sorted(Path("logs").glob("*.txt"))
print(f"Archivos encontrados: {len(archivos)}")

#%%

# Contar las líneas de cada uno

total_lineas = 0

for archivo in archivos:
    with open(archivo, "r") as f:
        lineas = len(f.readlines())
    print(f"  {archivo.name}: {lineas} líneas")
    total_lineas =+ lineas

print("")
print(f"Total de líneas en todos los logs: {total_lineas}")
# %%
