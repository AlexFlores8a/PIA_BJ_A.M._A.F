import json
import statistics as stats
from collections import Counter
import os

def main():
    # Cargar datos multi empresa
    with open("data/clean/multi_clean.json", "r") as f:
        multi = json.load(f)

    # Crear carpeta results si no existe
    os.makedirs("results", exist_ok=True)

    cambios = [item["cambio_porcentaje"] for item in multi if item["cambio_porcentaje"] is not None]

    if cambios:
        media = stats.mean(cambios)
        mediana = stats.median(cambios)
        try:
            moda = stats.mode(cambios)
        except stats.StatisticsError:
            moda = "No hay moda única (todos distintos)"
        minimo = min(cambios)
        maximo = max(cambios)
        rango_val = maximo - minimo
        desviacion = stats.stdev(cambios) if len(cambios) > 1 else 0

        print("\n--- Estadísticas del cambio porcentual ---")
        print(f"Media: {media:.2f}%")
        print(f"Mediana: {mediana:.2f}%")
        print(f"Moda: {moda}")
        print(f"Mínimo: {minimo:.2f}%")
        print(f"Máximo: {maximo:.2f}%")
        print(f"Rango: {rango_val:.2f}%")
        print(f"Desviación estándar: {desviacion:.2f}%")
    else:
        print("No hay datos de cambio porcentual disponibles.")

    # Guardar resultados en archivo de texto
    with open("results/estadisticas.txt", "w") as f:
        f.write("=== Resultados de Estadísticas ===\n")
        if cambios:
            f.write(f"Media: {media:.2f}%\n")
            f.write(f"Mediana: {mediana:.2f}%\n")
            f.write(f"Moda: {moda}\n")
            f.write(f"Mínimo: {minimo:.2f}%\n")
            f.write(f"Máximo: {maximo:.2f}%\n")
            f.write(f"Rango: {rango_val:.2f}%\n")
            f.write(f"Desviación estándar: {desviacion:.2f}%\n")
        else:
            f.write("No hay datos suficientes.\n")
    print("\n✓ Resultados guardados en results/estadisticas.txt")

if __name__ == "__main__":
    main()