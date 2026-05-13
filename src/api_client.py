import yfinance as yf

def get_finance_data(symbol="GOOGL"):
    try:
        print(f"Conectando a Yahoo Finance con símbolo: {symbol}")
        ticker = yf.Ticker(symbol)
        info = ticker.info
        hist = ticker.history(period="2d")
        if hist.empty:
            print("No hay datos históricos")
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
        data = {
            "simbolo": symbol.upper(),
            "nombre": info.get("longName", "N/A"),
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
        print("¡Datos obtenidos correctamente!")
        return data
    except Exception as e:
        print(f"Error en yfinance: {e}")
        return None
