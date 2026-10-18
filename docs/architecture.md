# Arquitectura propuesta de DJ Copilot

## Estado y alcance

Este documento describe una arquitectura prevista, no una implementación. El repositorio contiene un esqueleto de carpetas con README explicativos; todavía no hay API ejecutable, endpoints, adaptadores ni pruebas implementadas.

La propuesta se basa en el README del proyecto, el esquema `propuesta.excalidraw` situado en la carpeta superior y la organización de `task-manager-api`. El MVP contempla un único usuario, una colección local inicial de 50–100 canciones y recomendaciones de hasta diez temas. El frontend, los catálogos externos, la personalización por valoraciones y la autenticación multiusuario quedan fuera del esqueleto inicial.

## Organización

```text
DJ-Copilot/
├── api/
│   ├── routers/
│   ├── schemas/
│   ├── domain/
│   ├── services/
│   ├── repositories/
│   ├── integrations/
│   ├── db/
│   └── core/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/
└── assets/
```

Cada carpeta contiene un README con su responsabilidad, componentes previstos, relaciones y un ejemplo. No se crean archivos Python vacíos: los nombres previstos se describen en esos documentos.

## Capas y dependencias

El recorrido habitual será cliente → router → servicio → repositorio o integración. Los schemas validarán las entradas y definirán las respuestas HTTP. El dominio contendrá entidades y reglas independientes de frameworks y proveedores.

Como en `task-manager-api`, los servicios dependerán de contratos de repositorio y `dependencies.py` proporcionará implementaciones concretas. Se añade una capa de integraciones para las herramientas musicales y de IA. Los contratos de estas herramientas vivirán en `integrations/interfaces.py`; los de persistencia en `repositories/interfaces.py`.

| Carpeta | Responsabilidad |
| --- | --- |
| `api/routers/` | Transporte HTTP y delegación a servicios. |
| `api/schemas/` | Validación y serialización de la API. |
| `api/domain/` | Entidades y reglas del proyecto. |
| `api/services/` | Coordinación de casos de uso. |
| `api/repositories/` | Contratos e implementaciones de persistencia. |
| `api/integrations/` | Adaptadores de metadatos, audio, índice vectorial y lenguaje. |
| `api/db/` | Tablas, conexiones y sesiones. |
| `api/core/` | Configuración, errores y registros. |

## Flujo de incorporación y análisis

```text
Carpeta musical configurada
    → Detectar canciones nuevas o modificadas
    → Leer metadatos
    → Analizar audio
    → Guardar catálogo y análisis
    → Actualizar índice vectorial
    → Marcar canción como disponible para búsqueda
```

La importación se solicitará explícitamente. No se presupone un monitor permanente de archivos. Se propone identificar cambios mediante una huella del archivo y registrar la versión del analizador y de los modelos, para reutilizar análisis válidos y recalcular cuando corresponda.

El catálogo relacional será la fuente de verdad sobre canciones, análisis y estados. Cada vector se asociará al identificador de canción y a la versión de representación correspondiente. Si falla la indexación, se conservará un estado pendiente o fallido para permitir su reintento; la canción no se considerará lista para búsqueda hasta completar ese paso.

El análisis se ejecutará fuera de la petición HTTP y tendrá un identificador de trabajo consultable. Para el MVP se propone un ejecutor local. El mecanismo de ejecución, la recuperación tras reinicios y los reintentos deberán concretarse antes de implementarlo; una cola externa no es un requisito inicial.

## Flujo de recomendación y conversación

```text
Petición + referencias + contexto
    → Interpretar criterios estructurados
    → Validar criterios y referencias
    → Recuperar candidatos por similitud
    → Aplicar filtros y exclusiones
    → Seleccionar resultados válidos
    → Generar explicación basada en sus datos
```

La búsqueda estructurada podrá utilizarse sin el modelo de lenguaje. El servicio de recomendaciones garantizará el máximo de diez resultados, la ausencia de duplicados, la exclusión de referencias y los filtros admitidos, como el rango de BPM. Si faltan candidatos válidos, devolverá los disponibles y explicará la limitación. Una canción sin BPM conocido no podrá satisfacer un filtro obligatorio de BPM.

El modelo de lenguaje interpretará solicitudes y explicará resultados; no decidirá por sí solo el cumplimiento de las restricciones. Ante criterios ambiguos o no respaldados por el análisis, solicitará una aclaración o informará de la limitación. El contexto de conversación conservará referencias y criterios para permitir ajustes sucesivos.

## Datos principales

- **Canción:** identificador, localización del archivo, huella y metadatos disponibles.
- **Análisis:** características, puntuaciones de etiquetas, modelos y versiones utilizadas, fecha y estado.
- **Representación vectorial:** identificador de canción, tipo de representación y versión. La dimensión se determinará por el modelo o perfil elegido.
- **Importación:** estado, progreso y errores por archivo.
- **Recomendación:** criterios, candidatos seleccionados y evidencias disponibles para explicar la selección.
- **Conversación:** mensajes y contexto de búsqueda.

Los embeddings de audio y los perfiles de etiquetas son representaciones diferentes. El perfil de 56 etiquetas más valencia y activación es una hipótesis por evaluar; no se asumirá que todos los modelos producen un vector único de 58 dimensiones.

## Endpoints previstos

| Método y ruta | Función |
| --- | --- |
| `GET /health` | Estado de la API. |
| `POST /imports` | Solicitar importación desde la carpeta configurada. |
| `GET /imports/{job_id}` | Consultar progreso y errores. |
| `GET /tracks` | Consultar y filtrar el catálogo. |
| `GET /tracks/{track_id}` | Consultar una canción y su análisis disponible. |
| `POST /recommendations` | Buscar con referencias y criterios explícitos. |
| `POST /conversations` | Crear una conversación. |
| `POST /conversations/{conversation_id}/messages` | Enviar una petición o ajustar la selección. |

Son contratos propuestos, todavía sin implementar. La importación respondería con `202 Accepted` y un identificador de trabajo. Los esquemas concretos, paginación y respuestas de error se definirán al implementar la API.

## Tecnologías y decisiones pendientes

Se propone Python con FastAPI, Pydantic y SQLAlchemy para mantener continuidad con `task-manager-api`. SQLite es una opción inicial para el catálogo local, pendiente de validar. Essentia es el candidato de análisis descrito en el README.

Quedan por evaluar la tecnología vectorial, la métrica de similitud, la combinación de varias referencias, las representaciones y ponderaciones, los modelos musicales, el proveedor de lenguaje y los recursos necesarios para ejecutar los análisis. Las consultas por energía o emoción dependerán de esa evaluación.

Cuando exista implementación se añadirán los archivos de dependencias, configuración de ejemplo y, si resulta útil, Docker y Compose. No forman parte de este esqueleto documental.

## Configuración, datos y validación

La carpeta musical, las rutas de almacenamiento y las credenciales se configurarán fuera del código. No se incorporarán canciones, secretos, bases de datos generadas ni pesos de modelos al repositorio.

Las pruebas futuras cubrirán reglas de selección, filtros, importación incremental, fallos parciales y colaboración entre capas. La evaluación del prototipo medirá además la pertinencia para el DJ, la fidelidad de las explicaciones, tiempos de procesamiento y costes, conforme al README principal.

## Diagrama

Consulta el [archivo editable de Excalidraw](architecture.excalidraw) o su [vista previa SVG](../assets/architecture.svg). El mapa muestra las capas, la importación y el flujo de recomendaciones.
