import re

def validar_simbolo_accion(symbol: str) -> bool:
    """
    Valida que el símbolo tenga el formato: letras mayúsculas, opcionalmente dos puntos y más letras.
    Ejemplos válidos: GOOGL, GOOGL:NASDAQ, MSFT, AMZN, AAPL.
    """
    patron = r"^[A-Z]+(:[A-Z]+)?$"
    return bool(re.match(patron, symbol))

def validar_precio(valor) -> bool:
    """
    Verifica que un valor pueda convertirse a float (número positivo o negativo).
    """
    try:
        float(valor)
        return True
    except (ValueError, TypeError):
        return False

def validar_porcentaje(valor) -> bool:
    """
    Verifica que un porcentaje (como string " +1.23%") sea convertible a float (quitando el % y signo).
    """
    if not isinstance(valor, str):
        return False
    # Eliminar signos +/-, espacios y el símbolo %
    limpio = valor.strip().replace('%', '').replace('+', '').replace(',', '')
    try:
        float(limpio)
        return True
    except ValueError:
        return False