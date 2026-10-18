# Integraciones

Aislará el acceso a herramientas de audio, metadatos, búsqueda vectorial y modelos de lenguaje.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `interfaces.py`: contratos de las herramientas.
- `metadata_reader.py`: lectura de etiquetas y propiedades del archivo.
- `audio_analyzer.py`: adaptación del analizador de audio, con Essentia como candidato.
- `vector_index.py`: indexación y recuperación por similitud.
- `language_model.py`: interpretación de peticiones y generación de explicaciones.

## Relación con otras capas

Los servicios consumirán contratos y dependencies.py seleccionará las implementaciones. Los formatos y errores específicos de cada proveedor se adaptarán aquí.

## Ejemplo en DJ Copilot

El analizador devolverá características con su versión de modelo. El modelo de lenguaje recibirá candidatos y datos verificables para explicar la selección. Las tecnologías definitivas siguen pendientes de evaluación.
