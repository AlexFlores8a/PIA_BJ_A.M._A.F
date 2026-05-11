import requests
import json
import os

print("--- Avance 0: Prueba de conexión a API ---")

url = "https://serpapi.com/search?engine=google_finance&q=GOOGL:NASDAQ"

try:
    print(f"Conectando a: {url}")
    response = requests.get(url)
    print(f"Status code: {response.status_code}")

    # Crear carpeta data/raw (relativa a la raíz)
    os.makedirs("data/raw", exist_ok=True)

    # Intentar convertir respuesta a JSON
    try:
        data = response.json()
    except json.JSONDecodeError:
        data = {"error": "La respuesta no es JSON válido", "texto": response.text}

    # Guardar el archivo en data/raw/response.json
    with open("data/raw/response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Archivo guardado en data/raw/response.json")

except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")
