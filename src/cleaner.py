def limpiar_datos_financieros(raw_data: dict) -> dict:
    """
    Extrae los campos clave del JSON de SerpApi y los normaliza.
    Retorna un diccionario limpio con tipos correctos.
    """
    clean = {}

    # 1. Información general del instrumento
    if "organic_results" in raw_data and len(raw_data["organic_results"]) > 0:
        # A veces los datos principales están en "organic_results"[0]
        fin = raw_data["organic_results"][0].get("finance", {})
    else:
        # Si no, intentamos con "finance" directamente (estructura alternativa)
        fin = raw_data.get("finance", {})

    # 2. Extraer símbolo y nombre
    clean["simbolo"] = fin.get("ticker", "N/A")
    clean["nombre"] = fin.get("name", "N/A")
    clean["exchange"] = fin.get("exchange", "N/A")

    # 3. Precios
    precio_actual = fin.get("regular_market_price")
    clean["precio_actual"] = float(precio_actual) if precio_actual else None

    precio_anterior = fin.get("previous_close")
    clean["precio_anterior"] = float(precio_anterior) if precio_anterior else None

    # 4. Cambio y porcentaje
    cambio = fin.get("regular_market_change")
    clean["cambio"] = float(cambio) if cambio else None

    cambio_porcentaje = fin.get("regular_market_change_percent")
    if cambio_porcentaje and isinstance(cambio_porcentaje, str):
        # Eliminar '%' y convertir
        clean["cambio_porcentaje"] = float(cambio_porcentaje.replace('%', ''))
    else:
        clean["cambio_porcentaje"] = None

    # 5. Rango del día (máx/mín)
    dia_rango = fin.get("regular_market_day_range")
    if dia_rango and isinstance(dia_rango, str) and " - " in dia_rango:
        partes = dia_rango.split(" - ")
        try:
            clean["min_dia"] = float(partes[0])
            clean["max_dia"] = float(partes[1])
        except:
            clean["min_dia"] = clean["max_dia"] = None
    else:
        clean["min_dia"] = clean["max_dia"] = None

    # 6. Volumen (si existe)
    volumen = fin.get("regular_market_volume")
    clean["volumen"] = int(volumen) if volumen else None

    # 7. Timestamp (fecha de la consulta)
    clean["fecha_consulta"] = raw_data.get("search_metadata", {}).get("created_at", "N/A")

    return clean