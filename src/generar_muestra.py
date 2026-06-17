import pandas as pd
import os

# Ajustar numero de muestras a extraer
numero_muestras = 500000

# Ajusta el nombre del archivo raw original según como lo tengas en tu equipo
ruta_raw_original = '../data/raw/cybersecurity_threat_detection_logs.csv' 
ruta_raw_muestra = f'../data/raw/cybersecurity_threat_detection_logs_muestra_{numero_muestras}.csv'

print(f"Extrayendo muestra desde: {ruta_raw_original}...")

try:
    # Leemos solo las primeras {numero_muestras} del dataset raw original para crear la muestra
    df_muestra_raw = pd.read_csv(ruta_raw_original, nrows=numero_muestras)
    
    # Guardamos el nuevo archivo crudo que sí subiremos a GitHub
    df_muestra_raw.to_csv(ruta_raw_muestra, index=False)
    
    print(f"¡Éxito! Muestra cruda de {len(df_muestra_raw):,} filas guardada en: {ruta_raw_muestra}")

except FileNotFoundError:
    print("Error: No se encontró el dataset raw original. Verifica la ruta.")