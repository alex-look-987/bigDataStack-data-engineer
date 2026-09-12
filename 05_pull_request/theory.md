# Pull Requests: pedir revisión antes de mergear

### Anatomía de un Pull Request

Un PR en GitHub tiene estas partes:

- Título: resumen de una línea de qué hace el cambio (como un commit message)
- Descripción: contexto detallado — qué, por qué, cómo probarlo, qué impacto tiene
- Diff (archivos cambiados): vista línea por línea de lo que añadiste, modificaste o borraste
- Comentarios: conversación entre autor y revisores, tanto generales como en líneas específicas
- Checks: tests automáticos, linting, builds que se ejecutan al crear el PR
- Reviewers: personas asignadas para revisar el código
- Labels: etiquetas como "bug", "feature", "breaking-change"

### Crear tu primer Pull Request

El flujo es: 

1. trabajas en tu branch local
2. la subes a GitHub con git push
3. creas el PR desde la web de GitHub (o con GitHub CLI).

Vamos paso a paso:

```bash
# 1. Asegúrate de que tu branch está subida a GitHub
git switch feature/exportar-json
git push -u origin feature/exportar-json

# 2. Crear el PR desde la terminal (con GitHub CLI)
#    Primero escribe la descripción en un fichero:
#    (puedes hacerlo en VS Code, que es más cómodo)
#
#    descripcion.md:
#    ## Qué hace
#    - Añade exportar.py con función para exportar datos a JSON
#    - Soporta exportar con indentación configurable
#
#    ## Cómo probarlo
#    python exportar.py --input datos.csv --output resultado.json
#
#    ## Notas
#    Primera iteración. Falta manejo de errores.

gh pr create --title "feat: módulo de exportación a JSON" --body-file descripcion.md

# GitHub te da el URL del PR creado.
# También puedes crearlo desde github.com: verás un banner
# "Compare & pull request" después de hacer push.
```

### Cómo escribir una buena descripción de PR

```md
# [ERROR] MAL - No dice nada
# Título: "updates"
# Descripción: "fixed stuff"

# [OK] BIEN - El revisor entiende todo en 30 segundos
# Título: "fix: manejar valores NULL en campo dirección"
# Descripción:
# ## Problema
# El pipeline crashea cuando el campo "direccion" es NULL
# en la tabla clientes_raw. Afecta a ~200 registros/día.
#
# ## Solución
# Añadido .fillna("Sin dirección") antes de la transformación.
# Los registros sin dirección ahora se procesan con valor por defecto.
#
# ## Testing
# - Añadido test con fixture que incluye NULLs
# - Verificado con datos de producción del lunes (tenía 47 NULLs)
#
# ## Impacto
# Cero registros descartados. Pipeline no crashea.
```

### Mergear un PR: las tres opciones

- Merge commit (por defecto): crea un commit de merge con dos padres. El historial muestra claramente que hubo una branch. Ideal para equipos que quieren ver la historia completa.
- Squash and merge: aplasta todos los commits de la branch en UNO solo y lo pone en main. Historial más limpio, pero pierdes los commits intermedios. Ideal para PRs con muchos commits "wip" o "fix typo".
- Rebase and merge: reescribe los commits de tu branch como si hubieran sido hechos directamente en main. Historial lineal, sin merge commits. Más avanzado — evítalo al principio.
  
### Buenas prácticas de code review

El code review es una habilidad social tanto como técnica. He visto equipos donde el review se convierte en una guerra de egos, y equipos donde es la herramienta más valiosa de aprendizaje. La diferencia está en la actitud:

- Como AUTOR: no te lo tomes personal. Los comentarios son sobre el código, no sobre ti. Responde a cada comentario, incluso si es para decir "hecho" o "buena idea, lo cambio".
- Como REVISOR: sé específico y constructivo. No "esto está mal" → sí "esto podría fallar si el input es vacío, ¿consideraste ese caso?". Sugiere alternativas, no solo señales problemas.
- Mantén los PRs pequeños. Un PR de 2000 líneas no lo revisa nadie bien. Ideal: 100-400 líneas. Si tu cambio es grande, divídelo en PRs secuenciales.
- Responde rápido. Un PR que espera revisión 3 días bloquea al autor. Intenta revisar en menos de 24h.
- Usa comentarios de "nit" (nitpick) para cosas menores que no bloquean el merge: estilo, nombres, sugerencias opcionales.

### Branch protection rules: automatizar la disciplina

GitHub permite configurar "Branch protection rules" para main. Estas reglas automatizan las buenas prácticas para que nadie pueda saltárselas — ni siquiera el jefe:

- Require pull request reviews: nadie puede mergear sin al menos 1 aprobación
- Require status checks to pass: los tests automáticos deben pasar antes del merge
- Require up-to-date branch: tu branch debe tener los últimos cambios de main
- Do not allow bypassing: ni siquiera los admins pueden saltarse las reglas

Configurar branch protection rules es de las primeras cosas que hago en un proyecto nuevo. Es como poner un candado en la puerta de producción: solo entras si tienes la llave (PR aprobado + tests pasando).