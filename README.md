# Análisis de datos de amenazas de ciberseguridad

**Curso:** MCDI500 — Programación para la Ciencia de Datos  
**Integrantes:** Jennifer Nilo – Patricio Núñez  

## Descripción del Proyecto
Este proyecto busca optimizar el triaje y disminuir la fatiga de alertas en centros de operaciones de seguridad (SOC). Mediante el ecosistema científico de Python, se analiza un conjunto masivo de aproximadamente 6 millones de logs de red para aislar el ruido estadístico de los verdaderos indicadores de compromiso.

## Estructura del Repositorio
* `data/raw/`: Contiene el dataset original de logs de red (excluido del control de versiones por volumen).
* `data/processed/`: Directorio de destino para el dataset limpio, codificado y optimizado tras la Fase 2 (excluido del control de versiones).
* `notebooks/`: Aloja el código fuente y el flujo reproducible del análisis exploratorio inicial (`F1_Definicion.ipynb`).
* `F2/`: Directorio exclusivo para la Fase 2. Contiene el *notebook* ejecutable (`F2_Preprocesamiento.ipynb`) con el *pipeline* de limpieza exhaustiva y normalización.
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
* Enlace: [https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs/data](https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs/data)
* **IMPORTANTE:** El archivo descargado debe ser almacenado exclusivamente en el directorio `data/raw/`.

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

> **Nota técnica:** Cada decisión algorítmica y transformación de variables se encuentra estrictamente documentada y justificada en las celdas Markdown del propio *notebook*.