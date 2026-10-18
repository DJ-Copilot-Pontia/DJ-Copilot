# Schemas

Definirá los contratos de entrada y salida de la API mediante Pydantic.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `track.py`: respuestas del catálogo y análisis.
- `import_job.py`: solicitud y progreso de importación.
- `recommendation.py`: referencias, filtros y resultados.
- `conversation.py`: mensajes y respuestas del asistente.

## Relación con otras capas

Los routers los usarán para validar y serializar datos. Se distinguirán de las entidades de dominio y de los modelos de base de datos.

## Ejemplo en DJ Copilot

Una solicitud validará que la cantidad esté entre 1 y 10 y que el BPM mínimo no supere al máximo.
