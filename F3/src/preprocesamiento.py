"""
Módulo de Preprocesamiento Orientado a Objetos para Logs de Ciberseguridad.
Aplica herencia, polimorfismo y encapsulamiento.
"""

from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 1. CLASE BASE ABSTRACTA (Herencia y Contrato)
class Transformador(ABC):
    """
    Clase Base Abstracta (Python Software Foundation, 2024).
    Define el contrato polimórfico (Patrón Strategy) para todas las etapas del pipeline.
    """
    @abstractmethod
    def aplicar(self, df):
        pass

# 2. SUBCLASES CONCRETAS (Polimorfismo)

class LimpiadorNulos(Transformador):
    """Limpia variables críticas y rellena metadatos."""
    def aplicar(self, df):
        df_limpio = df.dropna(subset=['timestamp', 'source_ip', 'dest_ip'])
        if 'user_agent' in df_limpio.columns:
            df_limpio['user_agent'] = df_limpio['user_agent'].fillna('Desconocido')
        if 'request_path' in df_limpio.columns:
            df_limpio['request_path'] = df_limpio['request_path'].fillna('/')
        return df_limpio

class FiltroIPs(Transformador):
    """Valida mediante Regex el formato IPv4 estricto."""
    def aplicar(self, df):
        regex_ipv4 = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        mask_src = df['source_ip'].astype(str).str.match(regex_ipv4)
        mask_dst = df['dest_ip'].astype(str).str.match(regex_ipv4)
        return df[mask_src & mask_dst].copy()

class TransformadorFechas(Transformador):
    """Convierte el timestamp a formato datetime64."""
    def aplicar(self, df):
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        return df.dropna(subset=['timestamp'])

class EscaladorMinMax(Transformador):
    """
    Aplica clipping (percentil 99) y escalamiento Min-Max al volumen de datos 
    utilizando scikit-learn (Pedregosa et al., 2011).
    """
    def aplicar(self, df):
        df_out = df.copy()
        if 'bytes_transferred' in df_out.columns:
            # 1. Clipping para tratar valores atípicos
            limite_sup = df_out['bytes_transferred'].quantile(0.99)
            df_out['bytes_transferred'] = np.where(
                df_out['bytes_transferred'] > limite_sup, limite_sup, df_out['bytes_transferred']
            )
            
            # 2. Escalamiento profesional con scikit-learn
            scaler = MinMaxScaler()
            # fit_transform espera un array 2D, por eso los dobles corchetes
            df_out['bytes_escalados'] = scaler.fit_transform(df_out[['bytes_transferred']])
            
        return df_out
        
class IngenieriaCaracteristicas(Transformador):
    """Convierte texto en matriz numérica (One-Hot y Label Encoding)."""
    def aplicar(self, df):
        df_feat = df.copy()
        
        # Extracción
        regex_privada = r'^(?:10\.|172\.(?:1[6-9]|2[0-9]|3[0-1])\.|192\.168\.)'
        df_feat['is_internal_source'] = df_feat['source_ip'].astype(str).str.contains(regex_privada).astype(int)
        herramientas = 'nmap|curl|python|wget|postman|nikto|sqlmap'
        df_feat['is_automated_ua'] = df_feat['user_agent'].astype(str).str.lower().str.contains(herramientas).astype(int)
        
        # Limpieza de texto
        df_feat = df_feat.drop(columns=['source_ip', 'dest_ip', 'user_agent', 'request_path', 'bytes_transferred'], errors='ignore')
        
        # Encoding
        columnas_nominales = [col for col in ['action', 'log_type', 'protocol'] if col in df_feat.columns]
        df_feat = pd.get_dummies(df_feat, columns=columnas_nominales, dtype=int)
        
        if 'threat_label' in df_feat.columns:
            mapa_amenazas = {'benign': 0, 'suspicious': 1, 'malicious': 2}
            df_feat['threat_label_encoded'] = df_feat['threat_label'].map(mapa_amenazas)
            df_feat = df_feat.drop(columns=['threat_label'])
            
        return df_feat

# 3. EL ORQUESTADOR (Encapsulamiento)
class PipelinePreprocesamiento:
    """Centraliza la ejecución secuencial protegiendo el estado interno."""
    def __init__(self, etapas):
        self.etapas = etapas
    
    def ejecutar(self, df):
        df_interno = df.copy() # Estado encapsulado
        for etapa in self.etapas:
            df_interno = etapa.aplicar(df_interno) # Ejecución polimórfica
        return df_interno