# Análisis de comportamiento de la Bolsa de Valores

## Proyecto Integrador de Aprendizaje – Programación Básica  
**Maestra:** Perla Marviera  

**Integrantes del equipo:**  
- Ana María – Matrícula: 2190413  
- Alexander Flores – Matrícula: 2208864  

---

## 📌 Descripción del proyecto

Este proyecto obtiene datos financieros reales de la bolsa de valores utilizando la librería `yfinance` (Yahoo Finance).  
Los datos se limpian, se analizan estadísticamente y se visualizan mediante gráficas profesionales.  
Además, se genera un reporte en Excel con múltiples hojas que resume los hallazgos.

Nuestro objetivo es comparar el comportamiento de grandes empresas tecnológicas (Google, Apple, Microsoft, Amazon) para responder preguntas como:  
- ¿Cuál fue el año con mayor desplome en el periodo 2020-actualidad?  
- ¿La bolsa se ve afectada por la geopolítica o por la política del país de origen?

---

## 🔌 API utilizada

**`yfinance` – Yahoo Finance API**  
No requiere clave de acceso, es gratuita y muy estable.  
Documentación oficial: [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)

*¿Por qué cambiamos de SerpApi a yfinance?*  
Inicialmente intentamos usar SerpApi (Google Finance), pero tuvimos problemas de timeout y falta de datos reales. Con yfinance todo funciona de inmediato y los datos son confiables.

---

## 🛠️ Instalación y configuración

### Requisitos previos
- Python 3.8 o superior
- Conexión a Internet

### Pasos

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/AlexFlores8a/PIA_BJ_A.M._A.F.git
   cd PIA_BJ_A.M._A.F

2. Instalar dependencias

pip install yfinance matplotlib openpyxl

3. Ejecutar el flujo completo


python recopilar_datos.py   # Obtiene datos de múltiples empresas e históricos
python analysis.py          # Calcula estadísticas y guarda .txt
python visualizations.py    # Genera 4 gráficas en results/plots/
python datasheet.py         # Crea archivo Excel en results/excel/
python script2.py           # Ejecuta todo lo anterior de una vez
🧭 Ejemplos de uso
Consultar datos actuales de una empresa

python main.py GOOGL
Esto guarda los datos en data/clean/data_clean.json.

Generar estadísticas

python analysis.py
Resultados impresos en consola y guardados en results/estadisticas.txt.

Crear gráficas y Excel

python visualizations.py
python datasheet.py
Las gráficas se guardan en results/plots/ y el Excel en results/excel/.

📁 Estructura del repositorio (actual)
text
.
├── README.md
├── recopilar_datos.py        # Descarga datos multiempresa e históricos
├── analysis.py               # Estadísticas (media, mediana, moda, etc.)
├── visualizations.py         # Genera 4 gráficas (barras, pastel, línea, dispersión)
├── datasheet.py              # Crea Excel con 3 hojas
├── script2.py                # Orquestador que corre todo el análisis
├── main.py                   # Script 1 (consulta individual de un símbolo)
├── src/
│   ├── api_client.py         # Conexión a yfinance
│   ├── cleaner.py            # Limpieza y normalización
│   └── validators.py         # Validaciones básicas
├── data/
│   ├── raw/                  # Datos crudos (response.json)
│   └── clean/                # Datos limpios (data_clean.json, multi_clean.json, etc.)
├── results/
│   ├── estadisticas.txt
│   ├── plots/                # 4 gráficas en PNG
│   └── excel/                # reporte_final.xlsx
└── figures/                  (carpeta antigua, ya no se usa)

🧩 Explicación de cada script
Archivo	Función
recopilar_datos.py	Descarga datos actuales de GOOGL, AAPL, MSFT, AMZN y el histórico de GOOGL (30 días). Guarda en data/clean/.
analysis.py	Lee multi_clean.json, calcula media, mediana, moda, mínimo, máximo, rango y desviación estándar del cambio porcentual. Guarda resultados en results/estadisticas.txt.
visualizations.py	Genera 4 gráficas profesionales (barras, pastel, línea, dispersión) y las guarda en results/plots/.
datasheet.py	Crea un archivo Excel con tres hojas: Datos_limpios, Estadisticas y Frecuencias.
script2.py	Ejecuta analysis.py, visualizations.py y datasheet.py en secuencia.
main.py	Consulta un solo símbolo (ej. python main.py AAPL) y guarda datos limpios en data/clean/data_clean.json.


🎥 Video demo

Enlace al video de demostración (YouTube)
https://youtu.be/1czs-NIO52A?si=cFyya_RF0PB5Pu3I

El video muestra la ejecución de los scripts, las gráficas generadas y el contenido del Excel.


✨ Créditos del equipo
***Ana María – Responsable de la limpieza de datos, generación de gráficas y reporte Excel.

***Alexander Flores – Responsable de la conexión a la API, estadísticas y documentación.

Ambos participamos activamente en los commits y en la resolución de problemas.   