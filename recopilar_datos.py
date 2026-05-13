import yfinance as yf
import json
import os
from datetime import datetime, timedelta

def get_company_data(symbol):
    """Obtiene datos actuales de una empresa (precio, cambio, volumen, etc.)"""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        hist = ticker.history(period="2d")
        if hist.empty:
            print(f"  No hay datos históricos para {symbol}")
            return None
        ultimo = hist.iloc[-1]
        precio_actual = float(ultimo["Close"])
        if len(hist) >= 2:
            anterior = hist.iloc[-2]["Close"]
            cambio = precio_actual - anterior
            cambio_porcentaje = (cambio / anterior) * 100
            precio_anterior = float(anterior)
        else:
            precio_anterior = None
            cambio = None
            cambio_porcentaje = None
        return {
            "simbolo": symbol,
            "nombre": info.get("longName", symbol),
            "exchange": info.get("exchange", "N/A"),
            "precio_actual": precio_actual,
            "precio_anterior": precio_anterior,
            "cambio": cambio,
            "cambio_porcentaje": cambio_porcentaje,
            "min_dia": float(ultimo["Low"]),
            "max_dia": float(ultimo["High"]),
            "volumen": int(ultimo["Volume"]),
            "fecha_consulta": str(ultimo.name.date())
        }
    except Exception as e:
        print(f"  Error con {symbol}: {e}")
        return None

def get_historical_data(symbol, days=30):
    """Obtiene precios de cierre de los últimos 'days' días"""
    ticker = yf.Ticker(symbol)
    end = datetime.now()
    start = end - timedelta(days=days)
    hist = ticker.history(start=start, end=end)
    if hist.empty:
        return []
    result = []
    for date, row in hist.iterrows():
        result.append({
            "fecha": str(date.date()),
            "precio_cierre": float(row["Close"])
        })
    return result

def main():
    # 1. Datos de múltiples empresas
    simbolos = ["GOOGL", "AAPL", "MSFT", "AMZN"]
    datos_multi = []
    for sym in simbolos:
        print(f"Recopilando {sym}...")
        data = get_company_data(sym)
        if data:
            datos_multi.append(data)
    # Guardar en data/clean/multi_clean.json
    os.makedirs("data/clean", exist_ok=True)
    with open("data/clean/multi_clean.json", "w", encoding="utf-8") as f:
        json.dump(datos_multi, f, indent=4, ensure_ascii=False)
    print("\n✓ multi_clean.json guardado en data/clean/")

    # 2. Datos históricos de GOOGL (30 días)
    print("\nObteniendo datos históricos de GOOGL...")
    historico = get_historical_data("GOOGL", days=30)
    with open("data/clean/historico_GOOGL.json", "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4)
    print("✓ historico_GOOGL.json guardado en data/clean/")

if __name__ == "__main__":
    main()