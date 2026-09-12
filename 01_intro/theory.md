# Instalar Git y hacer tu primer commit 

## Theory

### Configuración inicial (una sola vez)

```bash
# Funciona igual en ambos sistemas:
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Para que los repos nuevos usen "main" (como GitHub):
git config --global init.defaultBranch main

# Verificar la configuración:
git config --global --list
# Debería mostrar tu nombre, email y defaultBranch
```

### Los 3 conceptos clave de Git

Git tiene una filosofía que necesitas entender antes de escribir comandos. Piensa en ello como preparar un paquete para enviar por correo:

01. **Working directory (tu escritorio):** es tu carpeta de proyecto. Los archivos que editas, creas o borras. Es tu zona de trabajo normal.
02. **Staging area (la caja de envío):** cuando decides qué cambios quieres guardar, los "metes en la caja" con git add. No todo lo que cambias tiene que ir en el mismo envío.
03. **Repository (la oficina de correos):** cuando haces git commit, sellas la caja y la envías al historial. Ese punto queda guardado para siempre. Puedes volver a él cuando quieras.

### git commit: crear un punto de guardado

```bash
# Ver el historial:
git log --oneline
# Resultado: a1b2c3d Primer commit: añadir README con título del proyecto
```

## Practice

- Usa "git status --short" para ver qué sigue vigilado y "git check-ignore -v <fichero>" para ver qué regla ignora cada cosa.

```bash
#Usa "git status --short" para ver qué sigue vigilado 
git status --short

# "git check-ignore -v <fichero>" para ver qué regla ignora cada cosa.
git check-ignore -v <fichero>
```

- git ls-files muestra lo que Git sigue de verdad. El .gitignore solo frena lo que aún NO sigue; para lo ya commiteado hace falta "git rm --cached <fichero>". Es el error que le pasa a todo el mundo la primera vez con un secreto.

```bash
# Míralo: git ls-files enseña lo que Git SIGUE. El .env está ahí (se commiteó).
git ls-files
```

```bash
# 3. Sácalo del seguimiento SIN borrarlo del disco:
git rm --cached .env
```
