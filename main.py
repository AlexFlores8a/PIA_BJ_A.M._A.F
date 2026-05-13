import sys
import os
import json
from src.api_client import get_finance_data
from src.validators import validar_simbolo_accion
from src.cleaner import limpiar_datos_financieros

def main():
    # 1. Parámetro por CLI (sys.argv)
    if len(sys.argv) > 1:
        symbol = sys.argv[1]
    else:
        symbol = "GOOGL:NASDAQ"
        print(f"Usando símbolo por defecto: {symbol}")

    # 2. Validar el símbolo con regex
    if not validar_simbolo_accion(symbol):
        print(f"✗ Error: El símbolo '{symbol}' no tiene un formato válido (ejemplo: GOOGL, MSFT:NASDAQ)")
        sys.exit(1)
    else:
        print(f"✓ Símbolo '{symbol}' validado correctamente.")

    print("\n=== Avance 2 - Script 1 final (con limpieza) ===\n")

    # 3. Obtener datos de la API (usando api_client)
    data = get_finance_data(symbol)
    if not data:
        print("No se pudo obtener datos. Terminando.")
        sys.exit(1)

    # 4. Guardar raw (opcional, ya se guarda en api_client? pero lo dejamos)
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("✓ Datos crudos guardados en data/raw/response.json")

    # 5. Limpiar datos usando cleaner
    clean_data = limpiar_datos_financieros(data)

    # 6. Validar algunos campos limpios
    if not clean_data.get("precio_actual") and not clean_data.get("precio_anterior"):
        print("⚠️ Advertencia: No se encontraron precios en la respuesta de la API.")

    # 7. Guardar datos limpios
    os.makedirs("data/clean", exist_ok=True)
    with open("data/clean/data_clean.json", "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=4)
    print("✓ Datos limpios guardados en data/clean/data_clean.json")
    print("\n--- Muestra del dato limpio ---")
    print(json.dumps(clean_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()