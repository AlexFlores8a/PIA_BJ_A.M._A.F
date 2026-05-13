import json
import statistics as stats
from collections import Counter
import os

# Cargar datos limpios
try:
    with open("data/clean/data_clean.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: No se encuentra data/clean/data_clean.json. Ejecuta primero python main.py GOOGL")
    exit(1)

# Extraer variable numérica (porcentaje de cambio)
valores = []
if data.get("cambio_porcentaje") is not None:
    valores = [data["cambio_porcentaje"]]
else:
    print("No hay datos de cambio_porcentaje en el JSON limpio.")

# Calcular estadísticas
if valores:
    media = stats.mean(valores)
    mediana = stats.median(valores)
    try:
        moda = stats.mode(valores)
    except stats.StatisticsError:
        moda = "No hay moda única (todos los valores son distintos o lista muy pequeña)"
    print(f"\n--- Estadísticas del cambio porcentual ---")
    print(f"Media: {media:.2f}%")
    print(f"Mediana: {mediana:.2f}%")
    print(f"Moda: {moda}")
else:
    print("\nNo hay suficientes datos numéricos para estadísticas.")

# Tabla de frecuencias (por exchange)
exchange = data.get("exchange", "N/A")
frecuencia = Counter([exchange])
print(f"\n--- Tabla de frecuencias (exchange) ---")
for cat, count in frecuencia.items():
    print(f"{cat}: {count}")

# Guardar resultados en results/estadisticas.txt
os.makedirs("results", exist_ok=True)
with open("results/estadisticas.txt", "w") as f:
    f.write("=== Avance 3 - Estadísticas ===\n")
    f.write(f"Media del cambio porcentual: {media:.2f}%\n" if valores else "Media: No disponible\n")
    f.write(f"Mediana del cambio porcentual: {mediana:.2f}%\n" if valores else "Mediana: No disponible\n")
    f.write(f"Moda: {moda}\n")
    f.write("\nTabla de frecuencias (exchange):\n")
    for cat, count in frecuencia.items():
        f.write(f"{cat}: {count}\n")

print("\n✓ Resultados guardados en results/estadisticas.txt")
