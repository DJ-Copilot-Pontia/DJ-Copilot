# Configuración y soporte común

Reunirá la configuración transversal necesaria para la aplicación.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `config.py`: variables de entorno y rutas configuradas.
- `exceptions.py`: errores de aplicación.
- `logging.py`: configuración de registros.

## Relación con otras capas

La aplicación y sus adaptadores leerán la configuración desde aquí. exception_handlers.py convertirá los errores esperados a respuestas HTTP.

## Ejemplo en DJ Copilot

La carpeta musical y las credenciales del proveedor de lenguaje se configurarán mediante entorno. Las credenciales y archivos musicales no se incluirán en el repositorio.
