import json
import matplotlib.pyplot as plt
import os

def main():
    # Cargar datos multi empresa
    with open("data/clean/multi_clean.json", "r") as f:
        multi = json.load(f)

    # Cargar datos históricos de GOOGL
    with open("data/clean/historico_GOOGL.json", "r") as f:
        historico = json.load(f)

    # Crear carpeta para gráficas (según checklist de la profe)
    os.makedirs("results/plots", exist_ok=True)

    # ------------------------------------------------------------
    # 1. Gráfica de barras: Precio actual por empresa
    # ------------------------------------------------------------
    simbolos = [item["simbolo"] for item in multi]
    precios = [item["precio_actual"] for item in multi]

    plt.figure(figsize=(8, 5))
    plt.bar(simbolos, precios, color=['blue', 'green', 'red', 'orange'])
    plt.title("Comparación de Precio Actual por Empresa", fontsize=14)
    plt.xlabel("Empresa", fontsize=12)
    plt.ylabel("Precio (USD)", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.savefig("results/plots/barras_precios.png", dpi=150)
    plt.close()
    print("✓ Gráfica 1: results/plots/barras_precios.png")

    # ------------------------------------------------------------
    # 2. Gráfica de pastel: Distribución de precios actuales
    # ------------------------------------------------------------
    precios_pastel = [item["precio_actual"] for item in multi]
    etiquetas = [item["simbolo"] for item in multi]

    plt.figure(figsize=(7, 7))
    plt.pie(precios_pastel, labels=etiquetas, autopct="%1.1f%%",
            colors=['gold', 'lightblue', 'lightgreen', 'pink'])
    plt.title("Distribución del Precio Actual por Empresa", fontsize=14)
    plt.savefig("results/plots/pastel_precios.png", dpi=150)
    plt.close()
    print("✓ Gráfica 2: results/plots/pastel_precios.png")

    # ------------------------------------------------------------
    # 3. Gráfica de línea: Evolución del precio de GOOGL (30 días)
    # ------------------------------------------------------------
    fechas = [item["fecha"] for item in historico]
    precios_hist = [item["precio_cierre"] for item in historico]

    plt.figure(figsize=(10, 5))
    plt.plot(fechas, precios_hist, marker='o', linestyle='-', color='purple')
    plt.title("Evolución del Precio de GOOGL (últimos 30 días)", fontsize=14)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Precio de Cierre (USD)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("results/plots/linea_historico.png", dpi=150)
    plt.close()
    print("✓ Gráfica 3: results/plots/linea_historico.png")

    # ------------------------------------------------------------
    # 4. Gráfica de dispersión: Cambio porcentual vs Volumen
    # ------------------------------------------------------------
    # Filtrar valores None
    cambios_vol = []
    volumenes = []
    for item in multi:
        if item.get("cambio_porcentaje") is not None:
            cambios_vol.append(item["cambio_porcentaje"])
            volumenes.append(item["volumen"])

    if len(cambios_vol) == len(volumenes) and len(cambios_vol) > 0:
        plt.figure(figsize=(8, 6))
        plt.scatter(cambios_vol, volumenes, color='teal', alpha=0.7)
        plt.title("Relación entre Cambio Porcentual y Volumen", fontsize=14)
        plt.xlabel("Cambio Porcentual (%)", fontsize=12)
        plt.ylabel("Volumen (USD)", fontsize=12)
        # Formatear eje Y para mostrar en millones
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))
        plt.grid(True, alpha=0.3)
        plt.savefig("results/plots/dispersion_volumen.png", dpi=150)
        plt.close()
        print("✓ Gráfica 4: results/plots/dispersion_volumen.png")
    else:
        print("⚠️ No hay suficientes datos para la gráfica de dispersión.")

    print("\n✅ 4 gráficas generadas en 'results/plots/'")

if __name__ == "__main__":
    main()
