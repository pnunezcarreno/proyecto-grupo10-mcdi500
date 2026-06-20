# Análisis de datos de amenazas de ciberseguridad

**Curso:** MCDI500 — Programación para la Ciencia de Datos  
**Integrantes:** Jennifer Nilo – Patricio Núñez  

## Descripción del Proyecto
Este proyecto busca optimizar el triaje y disminuir la fatiga de alertas en centros de operaciones de seguridad (SOC). Mediante el ecosistema científico de Python, se analiza un conjunto masivo de aproximadamente 6 millones de logs de red para aislar el ruido estadístico de los verdaderos indicadores de compromiso.

## Estructura del Repositorio
* `data/raw/`: Contiene una muestra del dataset original de logs de red (excluido del control de versiones por volumen).
* `data/processed/`: Directorio de destino para el dataset limpio, codificado y optimizado tras la Fase 2 (excluido del control de versiones).
* `notebooks/`: Aloja el código fuente y el flujo reproducible del análisis exploratorio inicial (`F1_Definicion.ipynb`).
* `F2/`: Directorio exclusivo para la Fase 2. Contiene el *notebook* ejecutable (`F2_Preprocesamiento.ipynb`) con el *pipeline* de limpieza exhaustiva y normalización.
* `F3/`: Directorio exclusivo para la Fase 3. Contiene el *notebook* ejecutable (`F3_Algoritmos.ipynb`) con el *pipeline* de diseño algoritmico y medición de complejidad.
* `F4/`: Directorio exclusivo para la Fase 4. Contiene el *notebook* ejecutable (`F4_Visualizacion.ipynb`) con el *pipeline* que concentra lo visto en F1 (Definición), F2 (Limpieza y transformación), F3 (Diseño algoritmico y POO), finalizando en la F4 dedicado a la comunicación e interpretación visual de resultados.
* `docs/`: Documentación técnica y reportes formales.
* `src/`: Scripts de funciones modulares.

## Instrucciones de Reproducción
Para ejecutar este proyecto garantizando los mismos resultados de entorno, sigue estos pasos en tu terminal:

### 1. Clonar el repositorio:
```bash
git clone https://github.com/pnunezcarreno/proyecto-grupo10-mcdi500.git
cd proyecto-grupo10-mcdi500
```

### 2. Descargar el dataset crudo:
* Dentro de el directorio  `data/raw/` está presente una muestra del dataset original con 500.000 registros, el cual servirá para probar el funcionamiento de los notebooks.

**Recomendación:** Para analizar en profundidad este caso, se recomienda descargar el dataset original:

* Enlace dataset original: [https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs/data](https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs/data)
* **IMPORTANTE:** El archivo descargado debe ser almacenado exclusivamente en el directorio `data/raw/`.

* Alternativa: Se dispone de script de descarga del dataset crudo desde repositorio de Google Drive y lo almacena directamente en el directorio `data/raw/`. El script se encuentra en `src/dataset_raw_downloader.py`
* **IMPORTANTE:** Para ejecutar el script `src/dataset_raw_downloader.py` es necesario instalar previamente la libreria `gdown`:
```bash
pip install gdown
```

* Opcional: Tambien se dispone de script que genera una muestra a partir del dataset original en `data/raw/`. El script se encuentra en `src/generar_muestra.py`
* **IMPORTANTE:** Dentro del script hay una variable llamada `numero_muestras` la cual controla cuantos registros se extraeran del dataset crudo.

### 3. Crear y activar el entorno virtual:
```bash
python -m venv .venv
# En Windows: .venv\Scripts\activate
```

### 4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución de la Fase 1 (Definición)
1. Con el entorno virtual activado, inicia Jupyter Notebook.
2. Abre el archivo ubicado en la ruta `notebook/F1_Definicion.ipynb`.
3. Ejecuta el *notebook* de forma secuencial (o utilizando `Restart Kernel and Run All Cells`).

## Ejecución de la Fase 2 (Preprocesamiento)
1. Con el entorno virtual activado, inicia Jupyter Notebook.
2. Abre el archivo ubicado en la ruta `F2/F2_Preprocesamiento.ipynb`.
3. Ejecuta el *notebook* de forma secuencial (o utilizando `Restart Kernel and Run All Cells`).
4. El *pipeline* automatizado leerá los logs desde `data/raw/`, aplicará la depuración modular (tratamiento de nulos, escalamiento Min-Max, codificación *One-Hot* y *Label Encoding*) y exportará el *dataset* puramente numérico hacia `data/processed/`.

## Ejecución de la Fase 3  (Diseño Algorítmico y Complejidad)
1. Con el entorno virtual activado, inicia Jupyter Notebook.
2. Abre el archivo ubicado en la ruta `F3/Algoritmos.ipynb`.
3. Ejecuta el *notebook* Fase 3 de forma secuencial (o utilizando `Restart Kernel and Run All Cells`).
4. El notebook orquestador `F3_Algoritmos.ipynb` consume el dataset procesado desde `data/processed/`, realizando una transformación estructural a listas nativas de Python para ejecutar y comparar el rendimiento de algoritmos de ordenamiento (iterativo $O(n^2)$ vs. recursivo $O(n \log n)$) mediante la clase AnalizadorAlertas definida en `F3/src/motor_analisis.py`.


## Ejecución de la Fase 3  (Diseño algorítmico, Complejidad y Programación Orientada a Objetos)
1. Con el entorno virtual activado, inicia Jupyter Notebook.
2. Abre el archivo ubicado en la ruta `F3/F3_Algoritmos-POO.ipynb`.
3. Ejecuta el *notebook* Fase 3 de forma secuencial (o utilizando `Restart Kernel and Run All Cells`).
4. El notebook orquestador `F3/F3_Algoritmos-POO.ipynb` consume el dataset crudo o la muestra desde `data/raw/`, ejecutando los pasos de la Fase 2 (tratamiento de nulos, escalamiento Min-Max, codificación *One-Hot* y *Label Encoding*) bajo el paradigma de la Programacion Orientada a Objetos mediante las clases definidas en `F3/src/preprocesamiento.py`, para ejecutar y comparar el rendimiento de algoritmos de ordenamiento (iterativo $O(n^2)$ vs. recursivo $O(n \log n)$) mediante la clase AnalizadorAlertas definida en `F3/src/motor_analisis.py`.

## Ejecución de la Fase 4  (Visualización y comunicación de resultados)
1. Con el entorno virtual activado, inicia Jupyter Notebook.
2. Abre el archivo ubicado en la ruta `F4/F4_Visualizacion.ipynb`.
3. Ejecuta el *notebook* Fase 4 de forma secuencial (o utilizando `Restart Kernel and Run All Cells`).
4. El notebook orquestador `F4/F4_Visualizacion.ipynb` consume el dataset crudo o la muestra desde `data/raw/`, ejecutando los pasos de la Fase 2 (tratamiento de nulos, escalamiento Min-Max, codificación One-Hot y Label Encoding) bajo el paradigma de la Programación Orientada a Objetos mediante las clases definidas en `F4/src/preprocesamiento.py`, y evalúa el rendimiento algorítmico mediante la clase AnalizadorAlertas (`F4/src/motor_analisis.py`), culminando con la generación de visualizaciones analíticas en `matplotlib` para interpretar la complejidad asintótica y los patrones tácticos de las amenazas.

   
> **Nota técnica:** Cada decisión algorítmica y transformación de variables se encuentra estrictamente documentada y justificada en las celdas Markdown del propio *notebook*.