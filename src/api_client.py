import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def get_finance_data(symbol="GOOGL:NASDAQ", timeout=15):
    """
    Obtiene datos financieros de SerpApi para un símbolo dado.
    Retorna un dict con la respuesta JSON, o None si hay error.
    """
    API_KEY = os.getenv("SERPAPI_API_KEY")
    if not API_KEY:
        print("✗ Error: No se encontró la API key. Verifica tu archivo .env")
        return None

    params = {
        "engine": "google_finance",
        "q": symbol,
        "api_key": API_KEY
    }
    url = "https://serpapi.com/search"

    try:
        print(f"Conectando a SerpApi con símbolo: {symbol}")
        response = requests.get(url, params=params, timeout=timeout)
        print(f"Status code: {response.status_code}")

        if response.status_code == 200:
            print("¡Conexión exitosa!")
            return response.json()
        else:
            print(f"Advertencia: La API respondió con código {response.status_code}")
            return None
    except requests.exceptions.Timeout:
        print("✗ Error: Timeout - la API tardó demasiado.")
        return None
    except requests.exceptions.ConnectionError:
        print("✗ Error: No se pudo conectar. Verifica internet.")
        return None
    except Exception as e:
        print(f"✗ Error inesperado: {e}")
        return None