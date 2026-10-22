# Routers

Definirá los endpoints y conectará HTTP con los servicios.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `health.py`: estado de la API.
- `tracks.py`: consulta del catálogo.
- `imports.py`: inicio y seguimiento de importaciones.
- `recommendations.py`: búsqueda estructurada.
- `conversations.py`: creación de conversaciones y envío de mensajes.

## Relación con otras capas

Utilizará schemas para entradas y respuestas, y dependencies para obtener servicios. Las reglas musicales y el acceso a datos pertenecerán a otras capas.

## Ejemplo en DJ Copilot

POST /recommendations recibirá referencias, cantidad y un rango opcional de BPM.
