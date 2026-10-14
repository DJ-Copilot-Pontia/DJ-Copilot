# DJ Copilot 🎧

![DJ Copilot: robot con auriculares y mesa de mezclas](assets/dj-copilot.png)

**Asistente de inteligencia artificial para explorar y preseleccionar música mediante lenguaje natural.**

DJ Copilot es un proyecto académico desarrollado en equipo en el marco del **proyecto Júpiter de Pontia**. Nuestro objetivo es construir y evaluar un prototipo que ayude a un DJ a encontrar canciones de su colección musical a partir de temas de referencia y peticiones expresadas con sus propias palabras.

> «Propón cinco canciones parecidas a estos dos temas, entre 120 y 124 BPM».

## Por qué lo hacemos

Preparar una sesión requiere escuchar, revisar y comparar muchas canciones. Cuando la biblioteca crece, localizar los temas que encajan con el estilo del DJ y la intención de la sesión consume cada vez más tiempo.

Los filtros habituales —artista, género, año o BPM— son útiles, pero no representan por completo una petición como «algo parecido a este tema, con más energía». Además, los metadatos pueden estar incompletos y el etiquetado manual exige dedicación.

Queremos facilitar esa exploración combinando análisis automático de audio, búsqueda por similitud e interacción conversacional. **La selección final seguirá siendo del DJ.**

## Qué vamos a construir

Una aplicación que permita incorporar una colección local, analizar sus canciones y recuperar candidatos adecuados para una consulta. La solución combinará tres componentes:

| Componente | Función prevista |
| --- | --- |
| Análisis de audio | Extraer características, etiquetas y representaciones de las canciones mediante herramientas y modelos preentrenados. |
| Recuperación musical | Buscar temas similares a las referencias y aplicar restricciones comprobables, como un rango de BPM. |
| Asistente conversacional | Interpretar la petición, pedir aclaraciones y explicar los resultados usando la información del catálogo. |

Las canciones de referencia representarán inicialmente las preferencias del usuario. Evaluaremos hasta qué punto las características del audio permiten también buscar por energía, emoción o contexto.

## Alcance inicial del MVP

Partiremos de una aplicación para **un único usuario y una colección local de 50–100 canciones**, ajustando el volumen tras las primeras pruebas. La propuesta de trabajo plantea un foco inicial en música electrónica.

El prototipo permitirá:

1. Incorporar canciones locales y almacenar su análisis para reutilizarlo.
2. Seleccionar uno o varios temas de referencia.
3. Formular una petición indicando referencias, número de resultados y un rango opcional de BPM.
4. Obtener hasta diez canciones del catálogo, sin duplicados y distintas de las referencias.
5. Consultar una explicación basada en los datos disponibles.
6. Ajustar las referencias o los criterios mediante conversación.

Si una consulta no puede resolverse con la información disponible, el asistente explicará la limitación o solicitará una aclaración.

### Líneas por validar

Exploraremos peticiones como «más energético», «más tranquilo» o «con un perfil emocional parecido». Su incorporación dependerá de que las pruebas permitan relacionarlas de forma razonable con las características obtenidas del audio.

La personalización mediante valoraciones del usuario y el aprendizaje por transferencia se estudiarán como posibles ampliaciones. La exploración de catálogos externos tampoco forma parte del alcance local inicial.

## Enfoque técnico previsto

El flujo propuesto es:

```text
Colección local → Análisis de audio → Catálogo e índice de búsqueda
                                              ↓
Petición + referencias → Interpretación → Recuperación y filtros
                                              ↓
                             Propuesta explicada → Ajustes del DJ
```

Evaluaremos **Essentia** como herramienta candidata para el análisis musical, así como el uso de embeddings y una base de datos vectorial para recuperar canciones por similitud. Integraremos un modelo de lenguaje para la interacción y la elaboración de respuestas fundamentadas en los resultados recuperados.

El punto de partida será utilizar modelos preentrenados. Las herramientas, modelos, almacenamiento e interfaz definitivos se elegirán después de comprobar su viabilidad sobre una muestra pequeña. El entrenamiento desde cero queda fuera de la propuesta inicial.

## Plan de trabajo

| Fase | Resultado esperado |
| --- | --- |
| Definición | Problema, usuarios, propuesta de valor, requisitos y criterios de aceptación. |
| Viabilidad | Pruebas de análisis de audio y recuperación sobre una muestra, con estimación de recursos y costes. |
| Diseño | Flujo funcional, arquitectura, tratamiento de datos y decisiones técnicas documentadas. |
| Implementación | Análisis del catálogo, búsqueda musical e integración del asistente. |
| Validación | Pruebas funcionales, evaluación de recomendaciones y análisis de rendimiento y costes. |
| Entrega académica | Memoria, resultados, limitaciones, contribuciones del equipo y evidencias para el proyecto Júpiter. |

La documentación abordará también control de versiones, pruebas, despliegue, configuración, gestión de secretos y trazabilidad, según las necesidades de la solución elegida.

## Cómo evaluaremos el prototipo

Comprobaremos:

- **Cumplimiento funcional:** resultados presentes en el catálogo, cantidad solicitada cuando existan candidatos suficientes, ausencia de duplicados y cumplimiento de los filtros admitidos.
- **Fidelidad de las respuestas:** explicaciones apoyadas en información disponible, sin inventar canciones ni atributos.
- **Utilidad para el DJ:** valoración de la pertinencia de las recomendaciones y de la interacción conversacional.
- **Viabilidad técnica y económica:** tiempos de análisis y consulta, consumo de recursos, errores y costes de operación.

Los resultados, los criterios de aceptación definitivos y las limitaciones se documentarán durante el desarrollo.

## Proyecto Júpiter de Pontia

Este repositorio reunirá el código y la documentación de **DJ Copilot como trabajo del proyecto Júpiter de Pontia**. La memoria explicará las decisiones, el proceso de desarrollo y la contribución de cada integrante.

Se prevé incluir un **anexo de cumplimiento académico** que relacione los requisitos del proyecto Júpiter con sus evidencias: documentación, implementación, pruebas y resultados.

## Estado y documentación

Este README describe la propuesta y el trabajo previsto; no acredita funcionalidades ya implementadas. Las instrucciones de instalación y ejecución se añadirán cuando se haya definido la tecnología y exista una primera versión ejecutable.

Documentos de referencia del equipo, sujetos a sus permisos de acceso:

- [Planteamiento](https://docs.google.com/document/d/1BbC1g_K7YxbnP2iYkAJucAUy8AZWLGfI4RxgVkznYcQ/edit).
- [Propuesta de índice](https://docs.google.com/document/d/17XoxDB2rRBFuJF-XM9wHfXjLIcmjquAtkQzrLFy6szk/edit).

## Datos y licencias

Las decisiones sobre datos, privacidad, licencias de modelos y propiedad intelectual formarán parte del diseño. El repositorio no incluirá archivos musicales ni credenciales. La licencia del código está pendiente de definición por el equipo.
