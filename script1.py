import requests
import json
import os
import sys

print("=== Avance 1: Script 1 v0 - Conexión a API y guardado crudo ===\n")

url = "https://serpapi.com/search?engine=google_finance&q=GOOGL:NASDAQ"

try:
    print(f"Conectando a: {url}")
    response = requests.get(url, timeout=10)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        print("¡Conexión exitosa!")
    else:
        print(f"Advertencia: La API respondió con código {response.status_code}. Continuamos guardando la respuesta de error.\n")

    os.makedirs("data/raw", exist_ok=True)

    try:
        data = response.json()
    except json.JSONDecodeError:
        data = {"error": "La respuesta no es un JSON válido", "texto": response.text}

    with open("data/raw/response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✓ Archivo guardado en data/raw/response.json")

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