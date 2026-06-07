# Análisis de datos de amenazas de ciberseguridad

**Curso:** MCDI500 — Programación para la Ciencia de Datos  
**Integrantes:** Jennifer Nilo – Patricio Núñez  

## Descripción del Proyecto
Este proyecto busca optimizar el triaje y disminuir la fatiga de alertas en centros de operaciones de seguridad (SOC). Mediante el ecosistema científico de Python, se analiza un conjunto masivo de aproximadamente 6 millones de logs de red para aislar el ruido estadístico de los verdaderos indicadores de compromiso.

## Estructura del Repositorio
* `data/raw/`: Contiene el dataset original (excluido del control de versiones por volumen).
* `notebooks/`: Aloja el código fuente y el flujo reproducible del análisis exploratorio (`F1_Definicion.ipynb`).
* `docs/`: Documentación técnica.
* `src/`: Scripts de funciones modulares.

## Instrucciones de Reproducción
Para ejecutar este proyecto garantizando los mismos resultados de entorno, sigue estos pasos en tu terminal:

1. **Clonar el repositorio:**
```bash
git clone https://github.com/pnunezcarreno/proyecto-grupo10-mcdi500.git
cd proyecto-grupo10-mcdi500
```

2. **Descargar el dataset con los logs de ciberseguridad:**
+ Enlace: https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs/data
+ **IMPORTANTE:** El dataset debe ser almacenado en el directorio **data/raw/**.

4. **Crear y activar el entorno virtual:**
```bash
python -m venv .venv
# En Windows: .venv\Scripts\activate
```

4. **Instalar las dependencias exactas:**
```bash
pip install -r requirements.txt
```

5. **Ejecutar Jupyter:**
```bash
jupyter notebook
```
