Registro de Cambios (Changelog)
===============================

# Análisis de datos de amenazas de ciberseguridad

**Curso:** MCDI500 — Programación para la Ciencia de Datos  
**Integrantes:** Jennifer Nilo – Patricio Núñez

### V4 Semana 3 - Junio 2026
* Implementación de la capa de visualización.
* Integración de la librería `matplotlib` para crear visualizaciones que explican de forma clara la velocidad de los algoritmos y los patrones de tráfico, facilitando la toma de decisiones.
* Uso de escalas logarítmicas en las visualizaciones para resolver el problema de la dispersión de datos. Esto permite observar simultáneamente el inmenso volumen del tráfico normal y los eventos críticos de exfiltración, evitando que estos últimos pasen desapercibidos.

### V3 Semana 2 - Junio 2026
* Reestructuración del código del proyecto utilizando el paradigma de Programación Orientada a Objetos (POO) para mejorar su organización, modularidad y escalabilidad.
* Implementación del Patrón *Strategy* utilizando Clases (ej. `EscaladorMinMax`, `FiltroIPs`) para lograr alta cohesión y bajo acoplamiento.
* Implementación de comparación de los de algoritmos iterativo $O(n^2)$ y recursivo (*Merge Sort* $`O(n \log n)`$) para demostrar cuál de los dos es el más apto para el contexto de analisis de eventos de ciberseguridad.
* Incorporación de una muestra del *dataset* con 500.000 registros para garantizar la reproducibilidad y pruebas de código.
* Adición de *scripts* utilitarios en el directorio `/src` para automatizar la descarga del *dataset* masivo original desde un repositorio alternativo y permitir la creación de muestras personalizadas.
* Actualización de las dependencias del ecosistema científico instalando `scikit-learn` y `matplotlib`.
* Modificación y guardado del archivo `requirements.txt` a codificación UTF-8 para corregir los problemas de lectura cruzada entre distintos sistemas operativos.
* Implementación de la librería `scikit-learn` para la normalización de datos, sustituyendo el cálculo matemático manual. Esto permite "aprender" y guardar los mínimos y máximos de la muestra original, previniendo la contaminación de información (*Data Leakage*) al momento de evaluar datos nuevos.

### V2 Semana 1 - Junio 2026
* Estandarización de formatos de direcciones IPv4 utilizando expresiones regulares (Regex).
* Reemplazo de valores faltantes (NA) con etiquetas por defecto (como "Desconocido"). Esto previno la pérdida masiva de registros incompletos y mantuvo el volumen de datos necesario para el análisis.
* Implementación de *One-Hot Encoding* sobre variables categóricas, dejando la matriz en un formato puramente numérico apto para procesamiento.

### V1 Semana 1 - Junio 2026
* Configuración inicial del ecosistema científico basado en la instalación de `jupyter`, `numpy` y `pandas`.
* Establecimiento de un entorno virtual (`venv`) aislado y control de versiones inicial mediante `git`.
* Declaración de las primeras dependencias de en el archivo `requirements.txt` para asegurar las condiciones de reproducibilidad.