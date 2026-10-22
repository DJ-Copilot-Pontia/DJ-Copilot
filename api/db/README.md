# Base de datos

Definirá los modelos de almacenamiento relacional y el ciclo de vida de conexiones y sesiones.

## Estado

Esta carpeta forma parte del esqueleto documental. Los componentes descritos son previstos; todavía no están implementados.

## Contenido previsto

- `models.py`: tablas de canciones, análisis, importaciones y conversaciones.
- `session.py`: motor de base de datos y sesiones.

## Relación con otras capas

Los repositorios utilizarán esta capa. Las entidades del dominio permanecerán separadas de los modelos de SQLAlchemy.

## Ejemplo en DJ Copilot

Se propone SQLite con SQLAlchemy como punto de partida local. El catálogo conservará identificadores y versiones que permitan relacionarlo con el índice vectorial; la decisión queda por validar.
