# Branch

## [03] Tres branches en paralelo


El repositorio multi-branch ya está inicializado con un commit inicial en main, y la primera rama (feature/validar-emails, con su commit) ya está hecha como modelo. Crea las otras dos ramas con un commit cada una, fusiona las tres en main (usa --no-edit) y borra las tres.

Comandos a probar:

Así se hizo la primera (de referencia):

```bash
git switch -c feature/validar-emails
git commit --allow-empty -m "trabajo en feature/validar-emails"
git switch main
```

- Branch 2: fix/formato-fechas
  -  <- las tres líneas: switch -c, commit --allow-empty, switch main

- Branch 3: feature/exportar-csv
    - Fusionar las tres en main, una por una (usa --no-edit)

```bash
git merge ... --no-edit
# <- (--no-edit acepta el mensaje automático sin abrir el editor)
```

### Solución

cd multi-branch

**Branch 2**
  - git switch -c fix/formato-fechas
  - git commit --allow-empty -m "trabajo en fix/formato-fechas"
  - git switch main

**Branch 3**
  - git switch -c feature/exportar-csv
  - git commit --allow-empty -m "trabajo en feature/exportar-csv"
  - git switch main

**Fusionar las tres**
  - git merge feature/validar-emails
  - git merge fix/formato-fechas --no-edit
  - git merge feature/exportar-csv --no-edit

**Borrar las tres**
  - git branch -d feature/validar-emails
  - git branch -d fix/formato-fechas
  - git branch -d feature/exportar-csv

**Comprobar:**
  - git branch

*** main**
  - git log --oneline

**(6 commits: 3 de trabajo, 2 merges y el inicial)**

### Explicación

Seis commits: tres de trabajo, dos merges y el inicial.

- **¿Por qué dos Merge branch y no tres?** Porque el primer merge (validar-emails) es fast-forward: main no tenía nada nuevo, solo avanza su puntero. Los otros dos sí crean merge commit porque main ya ha avanzado. En el panel de la derecha lo ves: la primera fusión no añade nodo, las otras dos sí dibujan un commit con dos padres.

- --no-edit acepta el mensaje automático sin abrir el editor (vim). Sin él, Git abre vim y te quedas encallado si no sabes que se sale con Esc y :wq.

- --allow-empty permite commitear sin haber cambiado ningún fichero: es para practicar el flujo sin distraerse con el contenido.