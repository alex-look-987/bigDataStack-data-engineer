# GitHub: tu código en la nube

### Paso 3: Conectar tu repo local con GitHub (git remote)

```bash
# Conectar tu repo local con GitHub
# Sustituye TU-USUARIO por tu nombre de usuario de GitHub
git remote add origin https://github.com/TU-USUARIO/mi-proyecto.git

# Verificar que se añadió
git remote -v
# origin  https://github.com/TU-USUARIO/mi-proyecto.git (fetch)
# origin  https://github.com/TU-USUARIO/mi-proyecto.git (push)
```

### Autenticación: PAT vs SSHv

Tienes dos opciones para autenticarte con GitHub. La que recomendamos para empezar: instala la GitHub CLI y ejecuta gh auth login. Se abre el navegador, te identificas, y ya está. Los otros dos caminos (PAT y SSH) funcionan, pero son más pasos:

- **Personal Access Token (PAT):** generas un token en GitHub y lo usas como contraseña. Más fácil de configurar. Ideal para empezar.

- **SSH Keys:** generas un par de claves en tu máquina y subes la pública a GitHub. Más seguro a largo plazo. No tienes que poner token cada vez.

```bash
# Opción recomendada para empezar: GitHub CLI (gh)
# Instalar GitHub CLI:
winget install --id GitHub.cli

# Autenticarse (abre el navegador):
gh auth login
# Selecciona: GitHub.com → HTTPS → Yes → Login with browser
# ¡Listo! Ya no te pedirá token nunca más.
```

### git pull: traer cambios de GitHub a tu máquina

```bash
# Descargar los últimos cambios de GitHub
git pull

# Es equivalente a: git fetch + git merge
# fetch = "descarga los cambios pero no los apliques"
# merge = "aplica los cambios descargados"
# pull = "haz ambas cosas de una vez"
```

### Leer git status después del primer push: ahead y behind

```bash
# Las cinco cosas que te puede decir:

git status -sb

## main...origin/main                       # estás igual que GitHub
## main...origin/main [ahead 2]             # tienes 2 commits que aún no has subido  -> git push
## main...origin/main [behind 3]            # el equipo subió 3 que tú no tienes      -> git pull
## main...origin/main [ahead 1, behind 3]   # las dos cosas a la vez
## feature/exportar-json                    # sin "...origin/": esta rama sólo está en tu ordenador
```

```bash
# Ver en qué rama estás
# <- git branch --show-current
```