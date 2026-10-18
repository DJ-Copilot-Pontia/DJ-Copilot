# Servicios

Coordinará los casos de uso y aplicará las reglas del dominio.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `track_service.py`: consultar canciones y análisis disponibles.
- `import_service.py`: detectar archivos nuevos o modificados y coordinar su procesamiento.
- `analysis_service.py`: analizar audio y actualizar sus representaciones.
- `recommendation_service.py`: recuperar candidatos, filtrar y construir la selección.
- `conversation_service.py`: interpretar peticiones, mantener contexto y explicar resultados.

## Relación con otras capas

Dependerá de contratos de repositorios e integraciones. dependencies.py proporcionará las implementaciones concretas.

## Ejemplo en DJ Copilot

El servicio de recomendaciones excluirá referencias y duplicados, comprobará el BPM y devolverá menos resultados si no hay suficientes candidatos válidos.
