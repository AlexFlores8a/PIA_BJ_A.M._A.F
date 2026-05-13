def limpiar_datos_financieros(raw_data: dict) -> dict:
    if not raw_data:
        return {}
    return raw_data