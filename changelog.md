Registro de Cambios (Changelog)
===============================

# Análisis de datos de amenazas de ciberseguridad

**Curso:** MCDI500 — Programación para la Ciencia de Datos
**Integrantes:** Jennifer Nilo – Patricio Núñez

### V4
##### Fase 4 - Semana 3 - Junio 2026
* **`20-06 Commit: 963518a`** Se crea `changelog.md` en la raíz del directorio que muestra la trazabilidad de los cambios implementados durante el proyecto.
* **`20-06 Commit: f74a4ce`** Se actualiza README.md con las instrucciones para la reproducibilidad de la Fase 4.
* **`19-06 Commit: 0a8f404`** Uso de escalas logarítmicas en las visualizaciones para resolver el problema de la dispersión de datos. Esto permite observar simultáneamente el inmenso volumen del tráfico normal y los eventos críticos de exfiltración, evitando que estos últimos pasen desapercibidos.
* **`19-06 Commit: 2cb1643`** Integración de la librería `matplotlib` para crear visualizaciones que explican de forma clara la velocidad de los algoritmos y los patrones de tráfico, facilitando la toma de decisiones.
* **`19-06 Commit: 0df5070`** Se crea el notebook `F4/F4_Visualizacion.ipynb` para la Fase 4.

### V3
##### Fase 3 - Semana 2 - Junio 2026
* **`17-06 Commit: 1d4c360`** Se actualiza README.md con las instrucciones para la reproducibilidad de la Fase 3.
* **`17-06 Commit: f9115e6`** Implementación de la librería `scikit-learn` para la normalización de datos, sustituyendo el cálculo matemático manual. Esto permite "aprender" y guardar los mínimos y máximos de la muestra original, previniendo la contaminación de información (*Data Leakage*) al momento de evaluar datos nuevos.
* **`17-06 Commit: cdbb95b`** Actualización de las dependencias del ecosistema científico instalando `scikit-learn` y `matplotlib`.
* **`17-06 Commit: 3732bb1`** Se crea el notebook `F3/F3_Algoritmos-POO.ipynb` para la continuación de la Fase 3.
* **`16-06 Commit: b208c20`** Adición de *script* `dataset_raw_downloader.py` en el directorio `/src` para automatizar la descarga del *dataset* masivo original desde un repositorio alternativo.
* **`15-06 Commit: 44f75df`** Incorporación de una muestra del *dataset* con 500.000 registros para garantizar la reproducibilidad y pruebas de código.
* **`15-06 Commit: 6e56ba8`** Adición de *script* `generar_muestra.py` en el directorio `/src` que permite la creación de muestras personalizadas.
* **`15-06 Commit: a1be702`** Modificación y guardado del archivo `requirements.txt` a codificación UTF-8 para corregir los problemas de lectura cruzada entre distintos sistemas operativos.
* **`14-06 Commit: 9d84f7f`** Reestructuración del código del proyecto utilizando el paradigma de Programación Orientada a Objetos (POO) para mejorar su organización, modularidad y escalabilidad.
* **`14-06 Commit: ca18e31`** Implementación del Patrón *Strategy* utilizando Clases (ej. `EscaladorMinMax`, `FiltroIPs`) para lograr alta cohesión y bajo acoplamiento.
* **`14-06 Commit: 933a636`** Implementación de comparación de los algoritmos iterativo $O(n^2)$ y recursivo (*Merge Sort* $O(n \log n)$) para demostrar cuál de los dos es el más apto para el contexto de análisis de eventos de ciberseguridad.
* **`14-06 Commit: 9d22879`** Se crea el notebook `F3/F3_Algoritmos.ipynb` para la Fase 3.

### V2
##### Fase 2 - Semana 1 - Junio 2026
* **`09-06 Commit: 8542497`** Se actualiza README.md con las instrucciones para la reproducibilidad de la Fase 2.
* **`09-06 Commit: a342651`** Se crea el notebook `F2/F2_Preprocesamiento.ipynb` para la Fase 2.
* **`09-06 Commit: a342651`** Reemplazo de valores faltantes (NA) con etiquetas por defecto (como "Desconocido"). Esto previno la pérdida masiva de registros incompletos y mantuvo el volumen de datos necesario para el análisis.
* **`09-06 Commit: a342651`** Implementación de *One-Hot Encoding* sobre variables categóricas, dejando la matriz en un formato puramente numérico apto para procesamiento.

### V1
##### Fase 1 - Semana 1 - Junio 2026
* **`08-06 Commit: 9407969`** Se crea el notebook `notebook/F1_Definicion.ipynb` para la Fase 1.
* **`07-06 Commit: 0c27a3b`** Se crea README.md con las instrucciones iniciales para la creación del entorno.
* **`07-06 Commit: f566902`** Configuración inicial del ecosistema científico basado en la instalación de `jupyter`, `numpy` y `pandas`.
* **`07-06 Commit: f566902`** Establecimiento de un entorno virtual (`venv`) aislado y control de versiones inicial mediante `git`.
* **`07-06 Commit: f566902`** Declaración de las primeras dependencias en el archivo `requirements.txt` para asegurar las condiciones de reproducibilidad.