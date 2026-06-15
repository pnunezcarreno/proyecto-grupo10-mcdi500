import pandas as pd
import os

# Ajusta el nombre del archivo raw original según como lo tengas en tu equipo
ruta_raw_original = '../data/raw/cybersecurity_threat_detection_logs.csv' 
ruta_raw_muestra = '../data/raw/cybersecurity_threat_detection_logs_muestra_500k.csv'

print(f"Extrayendo muestra desde: {ruta_raw_original}...")

try:
    # Leemos solo las primeras 500.000 filas
    df_muestra_raw = pd.read_csv(ruta_raw_original, nrows=500000)
    
    # Guardamos el nuevo archivo crudo que sí subiremos a GitHub
    df_muestra_raw.to_csv(ruta_raw_muestra, index=False)
    
    print(f"¡Éxito! Muestra cruda de {len(df_muestra_raw):,} filas guardada en: {ruta_raw_muestra}")

except FileNotFoundError:
    print("Error: No se encontró el dataset raw original. Verifica la ruta.")