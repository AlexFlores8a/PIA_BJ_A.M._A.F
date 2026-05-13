import requests
import json
import os
import sys
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()
API_KEY = os.getenv("SERPAPI_API_KEY")
print(f"DEBUG: API_KEY encontrada = {API_KEY[:5]}..." if API_KEY else "DEBUG: No se encontró API_KEY")

print("=== Avance 2 - Script 1 con API key (preparación) ===\n")

# Obtener la API key desde la variable de entorno
API_KEY = os.getenv("SERPAPI_API_KEY")

if not API_KEY:
    print("✗ Error: No se encontró la API key. Asegúrate de tener el archivo .env con SERPAPI_API_KEY=tu_clave")
    sys.exit(1)

# Parámetros de la consulta a SerpApi
params = {
    "engine": "google_finance",
    "q": "GOOGL:NASDAQ",      # Puedes cambiar por MSFT:NASDAQ, AMZN:NASDAQ, etc.
    "api_key": API_KEY
}

url = "https://serpapi.com/search"

try:
    print(f"Conectando a SerpApi con parámetros: {params['q']}")
    response = requests.get(url, params=params, timeout=15)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        print("¡Conexión exitosa! Recibiendo datos reales.")
    else:
        print(f"Advertencia: La API respondió con código {response.status_code}. Puede haber un problema con la key o la consulta.\n")

    # Crear carpeta data/raw si no existe
    os.makedirs("data/raw", exist_ok=True)

    # Guardar la respuesta (JSON) en data/raw/response.json
    try:
        data = response.json()
    except json.JSONDecodeError:
        data = {"error": "La respuesta no es un JSON válido", "texto": response.text}

    with open("data/raw/response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✓ Archivo guardado en data/raw/response.json")
    print("Ahora los datos son reales (o un error detallado de SerpApi)")

except requests.exceptions.Timeout:
    print("✗ Error: La API tardó demasiado en responder (timeout).")
    sys.exit(1)
except requests.exceptions.ConnectionError:
    print("✗ Error: No se pudo conectar a la API. Verifica tu conexión a internet.")
    sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"✗ Error inesperado en la petición: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error general: {e}")
    sys.exit(1)