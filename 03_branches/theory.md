```# Branches (02-03)

### git switch: moverse entre universos

```bash
# ATAJO: crear y moverte en un solo paso
git switch -c feature/otra-cosa
```

### Borrar branches: limpiar después de fusionar
$$  $$

```bash
# Borrar una branch que ya fusionaste
git branch -d feature/agregar-iva

# -d = delete seguro (solo si ya fusionaste)
# -D = delete forzado (borra aunque no esté fusionada — cuidado)
```

### git log --graph: visualizar el árbol de branches

```bash
# Ver el historial como un gráfico
git log --oneline --graph --all

# Salida de ejemplo, después de que un compañero fusionara lo suyo en main
# mientras tú trabajabas en tu branch:
#
# *   4bac115 Merge branch 'feature/exportar-csv'
# |\
# | * 06943c9 feat: exportar el informe a CSV        <- tu trabajo, en tu branch
# * | c7dde41 fix: corregir el formato de las fechas <- lo que entró en main mientras tanto
# |/
# * dc932ee feat: calcular el total con IVA          <- de aquí salieron las dos
# * f58ea3d commit inicial
#
# Las dos columnas son los dos caminos. Se separan en dc932ee y se vuelven a
# juntar arriba, en el merge commit. Eso es exactamente lo que dibuja el |\ y el |/.
```