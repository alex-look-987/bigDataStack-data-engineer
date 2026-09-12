# Gitflow simplificado: el flujo que usan los equipos reales

### El flujo mínimo viable: main + feature branches
El flujo más simple que funciona profesionalmente tiene estas reglas:

01. main es sagrado: siempre funciona, siempre es deployable, nadie commitea directamente
02. Cada tarea = una feature branch: por pequeña que sea, trabaja en una branch
03. Nombres descriptivos: feature/, fix/, refactor/, docs/ + nombre claro
04. Push frecuente: sube tu branch a GitHub al menos una vez al día (backup + visibilidad)
05. PR obligatorio: todo cambio pasa por un Pull Request con al menos 1 revisión
06. Merge via PR: nunca git merge local para meter cosas en main — siempre vía GitHub
07. Borar branch después del merge: no acumules branches muertas

### Gitflow completo vs simplificado: cuándo complicarse
El Gitflow original de Vincent Driessen tiene más branches:

- main: código en producción
- develop: integración de features antes de release
- feature/*: funcionalidades nuevas (salen de develop)
- release/*: preparar una versión para producción
- hotfix/*: fixes urgentes en producción

**nota:** Regla del pragmatismo: si tu equipo tiene menos de 10 personas y no envía software con versiones a clientes externos, NO uses Gitflow completo. Es burocracia innecesaria. Main + feature branches + CI/CD es el estándar moderno para el 90% de equipos de tecnología.

### Commit messages: el arte ignorado

```bash
# Conventional Commits:
# tipo: descripción breve

git commit -m "feat: añadir validación de emails"
git commit -m "fix: manejar NULL en campo precio"
git commit -m "refactor: simplificar función de limpieza"
git commit -m "docs: documentar proceso de deploy"
git commit -m "test: añadir tests para módulo de exportación"
git commit -m "chore: actualizar dependencias"

# Tipos comunes:
# feat     = funcionalidad nueva
# fix      = corrección de bug
# refactor = cambio interno sin cambiar funcionalidad
# docs     = documentación
# test     = añadir o modificar tests
# chore    = tareas de mantenimiento
```

### .gitignore: lo que nunca debe subir a GitHub

```.gitignore
# .gitignore para proyectos de datos

# Entornos virtuales
venv/
.venv/
env/

# Variables de entorno (¡NUNCA subir credenciales!)
.env
.env.local
*.secret

# Datos (los datos no van en Git)
data/
*.csv
*.parquet
*.xlsx
!data/.gitkeep

# Python
__pycache__/
*.pyc
*.pyo
.pytest_cache/

# Notebooks
.ipynb_checkpoints/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```