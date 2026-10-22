# API de DJ Copilot

Reunirá la aplicación HTTP en Python con FastAPI y sus capas internas.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `main.py`: creación de la aplicación y registro de routers.
- `dependencies.py`: construcción e inyección de servicios, repositorios e integraciones.
- `exception_handlers.py`: traducción de errores de aplicación a respuestas HTTP.

## Relación con otras capas

La petición entra por routers, se valida con schemas y se resuelve mediante servicios. El dominio define las entidades y reglas; los repositorios e integraciones dan acceso a almacenamiento y herramientas externas.

## Ejemplo en DJ Copilot

Una petición de recomendaciones llegará al router y se delegará en el servicio de recomendaciones.
