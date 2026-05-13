import json
import statistics as stats
from collections import Counter
import os

print("=== Avance 3: Estadísticas y tabla de frecuencias ===\n")

# 1. Cargar los datos limpios
ruta_limpios = "data/clean/data_clean.json"
if not os.path.exists(ruta_limpios):
    print(f"❌ Error: No se encuentra el archivo {ruta_limpios}")
    print("Ejecuta primero 'python main.py GOOGL' para generar datos limpios.")
    exit(1)

with open(ruta_limpios, "r", encoding="utf-8") as f:
    data = json.load(f)

# Verificar que los datos no estén vacíos
if not data:
    print("❌ El archivo de datos limpios está vacío.")
    exit(1)

# 2. Elegir una variable numérica (cambio_porcentaje)
#    Si es None, intentamos con precio_actual
valor_numerico = data.get("cambio_porcentaje")
nombre_variable = "cambio_porcentaje"
if valor_numerico is None:
    valor_numerico = data.get("precio_actual")
    nombre_variable = "precio_actual"
if valor_numerico is None:
    print("❌ No se encontró una variable numérica válida (cambio_porcentaje o precio_actual).")
    print("Datos disponibles:", list(data.keys()))
    exit(1)

# 3. Calcular estadísticas
#    Como solo tenemos un valor (una empresa), la media, mediana y moda son ese mismo valor.
#    Pero para el Avance 3 necesitamos una lista de valores. 
#    Como solo tenemos un registro, simularemos que tenemos varios símbolos.

lista_valores = [valor_numerico]  # si tuvieras múltiples, sería más grande

print(f"📊 Analizando variable: {nombre_variable}")
print(f"Valor obtenido: {valor_numerico}\n")

# Media
media = stats.mean(lista_valores)
# Mediana
mediana = stats.median(lista_valores)
# Moda (puede dar error si todos son únicos)
try:
    moda = stats.mode(lista_valores)
except stats.StatisticsError:
    moda = "No hay moda (todos los valores son únicos o lista vacía)"

# Desviación estándar (si hay más de 1 elemento, sino no)
if len(lista_valores) > 1:
    desviacion = stats.stdev(lista_valores)
else:
    desviacion = None

# Mostrar resultados
print("=== Resultados estadísticos ===")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")
if desviacion is not None:
    print(f"Desviación estándar: {desviacion:.2f}")
else:
    print("Desviación estándar: No se puede calcular con un solo dato.")

# 4. Tabla de frecuencias para variable categórica (exchange)
categoria = data.get("exchange", "N/A")
# Si quieres una tabla más interesante, podrías agrupar por rangos de precio, pero usaremos exchange
frecuencias = Counter([categoria])

print("\n=== Tabla de frecuencias (Exchange) ===")
for cat, count in frecuencias.items():
    print(f"{cat}: {count} vez/veces")

# 5. Guardar resultados en un archivo
os.makedirs("results", exist_ok=True)
ruta_resultados = "results/estadisticas.txt"

with open(ruta_resultados, "w", encoding="utf-8") as f:
    f.write("=== Avance 3 - Resultados estadísticos ===\n")
    f.write(f"Variable analizada: {nombre_variable}\n")
    f.write(f"Media: {media:.2f}\n")
    f.write(f"Mediana: {mediana:.2f}\n")
    f.write(f"Moda: {moda}\n")
    if desviacion:
        f.write(f"Desviación estándar: {desviacion:.2f}\n")
    f.write("\n=== Tabla de frecuencias (Exchange) ===\n")
    for cat, count in frecuencias.items():
        f.write(f"{cat}: {count}\n")

print(f"\n✅ Resultados guardados en {ruta_resultados}")