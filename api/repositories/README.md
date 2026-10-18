# Repositorios

Encapsulará la persistencia del catálogo, los análisis y el estado de la aplicación.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `interfaces.py`: contratos de persistencia.
- `track_repository.py`: canciones y huellas de archivos.
- `analysis_repository.py`: características y versiones de análisis.
- `import_job_repository.py`: progreso y errores.
- `conversation_repository.py`: conversaciones y mensajes.

## Relación con otras capas

Los servicios dependerán de los contratos. Las implementaciones utilizarán db/ y convertirán modelos persistidos en entidades de dominio. El índice vectorial se encapsulará en integrations/.

## Ejemplo en DJ Copilot

El repositorio permitirá localizar una canción por su identificador y recuperar el análisis vigente.
