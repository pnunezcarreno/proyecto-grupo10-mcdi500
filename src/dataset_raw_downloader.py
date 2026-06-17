import gdown

# El ID se extrae del enlace para compartir de Google Drive
file_id = '1YdX8srW1O2_yiTaBAjcoyV009mKnNVSe'
url = f'https://drive.google.com/uc?id={file_id}'
output = '../data/raw/cybersecurity_threat_detection_logs.csv'

print("Iniciando descarga desde Google Drive...")
gdown.download(url, output, quiet=False)
print("¡Descarga completada!")