# Gitflow simplificado para equipos de analítica

### El flujo mínimo viable: main + feature branches
El flujo más simple que funciona profesionalmente tiene estas reglas:

01. main es sagrado: siempre funciona, siempre es deployable, nadie commitea directamente
02. Cada tarea = una feature branch: por pequeña que sea, trabaja en una branch
03. Nombres descriptivos: feature/, fix/, refactor/, docs/ + nombre claro
04. Push frecuente: sube tu branch a GitHub al menos una vez al día (backup + visibilidad)
05. PR obligatorio: todo cambio pasa por un Pull Request con al menos 1 revisión
06. Merge via PR: nunca git merge local para meter cosas en main — siempre vía GitHub
07. Borar branch después del merge: no acumules branches muertas

### Qué significa "main es la versión que funciona"

En la práctica, para un equipo de analistas esto significa:

- Las queries que alimentan dashboards están en main y funcionan
- Los scripts de informes periódicos leen de main
- El diccionario de métricas en main es la versión oficial
- Cualquier compañero puede clonar main y ejecutar los análisis sin que nada falle

### Gitflow completo vs simplificado: cuándo complicarse
El Gitflow original de Vincent Driessen tiene más branches:

- **main:** código en producción
- **develop:** integración de features antes de release
- **feature/** — funcionalidad nueva: un análisis, una query, un notebook
- **fix/** — corrección de algo que está mal: un cálculo erróneo, un duplicado, un filtro roto
- **docs/** — documentación: diccionario de métricas, README, comentarios en queries
- **refactor/** — reorganizar sin cambiar resultados: renombrar columnas, limpiar un notebook

```bash
# Analisis nuevos
feature/query-retencion-marketing
feature/cohortes-producto-q3
feature/segmentacion-clientes-rfm

# Correcciones
fix/informe-semanal-duplicados
fix/calculo-churn-sin-trials
fix/filtro-fecha-kpis-diarios

# Documentacion
docs/diccionario-metricas
docs/readme-estructura-repo
docs/comentarios-query-ingresos

# Reorganizacion
refactor/renombrar-columnas-legacy
refactor/separar-queries-por-area
```

**nota:** Regla del pragmatismo: si tu equipo tiene menos de 10 personas y no envía software con versiones a clientes externos, NO uses Gitflow completo. Es burocracia innecesaria. Main + feature branches + CI/CD es el estándar moderno para el 90% de equipos de tecnología.

### Commit messages: el arte ignorado

```bash
# Conventional Commits para analitica:

git commit -m "feat: query de retencion por cohorte mensual"
git commit -m "fix: corregir duplicados en informe semanal"
git commit -m "refactor: simplificar CTE de ingresos recurrentes"
git commit -m "docs: documentar metrica de churn en diccionario"
git commit -m "feat: anadir grafico de conversion al notebook"
git commit -m "fix: filtro de fecha excluia el ultimo dia del mes"

# Tipos comunes en analitica:
# feat     = analisis nuevo, query nueva, grafico nuevo
# fix      = correccion de calculo, filtro, duplicado
# refactor = reorganizar sin cambiar resultados
# docs     = documentacion, comentarios, diccionario
```

### .gitignore: lo que nunca debe subir a GitHub

```.gitignore
# .gitignore para un repo de analitica

# Variables de entorno (credenciales de bases de datos)
.env
.env.local

# Datos locales (no van en Git: pesan y cambian)
*.csv
*.xlsx
*.parquet
datos/*
!datos/.gitkeep

# Python
__pycache__/
*.pyc
.venv/
venv/

# Notebooks: los checkpoints son cache, no codigo
.ipynb_checkpoints/

# IDE y sistema
.vscode/
.idea/
.DS_Store
Thumbs.db
```

### El repo típico de un equipo de analítica

```bash
analitica-ecommerce/
  queries/                  # Queries SQL organizadas por area
    retencion/
      cohortes_mensual.sql
      churn_por_segmento.sql
    ingresos/
      ingresos_recurrentes.sql
      arpu_por_plan.sql
    marketing/
      atribucion_canal.sql
      cac_por_campana.sql
  informes/                 # Scripts que generan informes periodicos
    kpis_semanales.py
    informe_mensual.py
  notebooks/                # Analisis exploratorios
    exploracion_churn_q3.ipynb
    segmentacion_rfm.ipynb
  docs/                     # Documentacion del equipo
    diccionario_metricas.md
    guia_nuevos_analistas.md
  .gitignore
  README.md
```