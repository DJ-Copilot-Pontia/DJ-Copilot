# Dominio

Contendrá las entidades y reglas del proyecto, independientes de FastAPI, SQLAlchemy y proveedores externos.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `track.py`: identidad y metadatos de una canción.
- `audio_analysis.py`: características musicales y versión del análisis.
- `import_job.py`: progreso y estados de importación.
- `recommendation.py`: criterios y candidatos seleccionados.
- `conversation.py`: contexto y mensajes.
- `enums.py`: estados y valores compartidos.

## Relación con otras capas

Los servicios trabajarán con estas entidades. Repositorios e integraciones convertirán los datos entre el dominio y sus formatos de almacenamiento o proveedor.

## Ejemplo en DJ Copilot

Una selección tendrá hasta diez canciones, sin duplicados y distintas de las referencias.
