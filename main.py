import sys
import os
import json
from src.api_client import get_finance_data
from src.cleaner import limpiar_datos_financieros

def main():
    if len(sys.argv) > 1:
        symbol = sys.argv[1]
    else:
        symbol = "GOOGL"
        print(f"Usando símbolo por defecto: {symbol}")

    # Validación simple
    if not symbol.isalnum():
        print("Error: símbolo inválido (solo letras y números)")
        sys.exit(1)

    print("\n=== Obteniendo datos financieros ===\n")
    data = get_finance_data(symbol)
    if not data:
        print("No se pudieron obtener datos. Verifica el símbolo o internet.")
        sys.exit(1)

    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("✓ Datos crudos guardados en data/raw/response.json")

    clean_data = limpiar_datos_financieros(data)
    os.makedirs("data/clean", exist_ok=True)
    with open("data/clean/data_clean.json", "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=4)
    print("✓ Datos limpios guardados en data/clean/data_clean.json")
    print("\n--- Muestra del dato limpio ---")
    print(json.dumps(clean_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()