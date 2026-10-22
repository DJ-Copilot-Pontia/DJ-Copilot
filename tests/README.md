# Pruebas

Organizará las comprobaciones del comportamiento del MVP cuando exista implementación.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `unit/`: reglas y casos de uso aislados.
- `integration/`: interacción entre API, persistencia e integraciones.
- `fixtures/`: datos de prueba controlados.

## Relación con otras capas

Las pruebas unitarias sustituirán herramientas externas por dobles. Las de integración comprobarán las fronteras entre componentes.

## Ejemplo en DJ Copilot

Se comprobarán filtros de BPM, exclusión de referencias, ausencia de duplicados, reutilización del análisis y fidelidad de las respuestas.
