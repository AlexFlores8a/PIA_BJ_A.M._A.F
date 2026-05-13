# Análisis del comportamiento de la Bolsa de Valores (con yfinance)

## Presentación
Proyecto Integrador de Aprendizaje de la materia de Programación Básica con la Maestra Perla Marviera.

## Integrantes del equipo
- Ana María – Matrícula: 2190413
- Alexander Flores – Matrícula: 2208864

## Descripción
El proyecto obtiene datos financieros reales de la bolsa de valores utilizando la librería **yfinance** (Yahoo Finance). Los datos se almacenan en formato JSON y sirven como base para análisis estadístico, visualización y generación de reportes.

## Objetivo
Buscar, analizar y comparar aquellas empresas que tuvieron más alzas y más bajas a partir del 2020 hasta la actualidad.

## API / Librería utilizada
**yfinance** (Yahoo Finance) – API gratuita sin necesidad de clave.  
Documentación: [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)

### Justificación del cambio
Inicialmente se consideró SerpApi, pero presentaba problemas de timeout y falta de datos. Se migró a yfinance porque es gratuita, no requiere API key, es confiable y devuelve datos financieros reales (precios, volumen, etc.) de forma inmediata.

## Preguntas de investigación
- ¿Cuál fue el año con el desplome más bajo en el periodo 2020-actualidad?
- ¿La bolsa es afectada por la geopolítica o por la política de su país de origen?

## Tecnologías utilizadas
- Python
- yfinance (Yahoo Finance)
- requests (solo para respaldo)
- statistics, collections
- matplotlib (para gráficas – próximo avance)
- openpyxl (para Excel – entrega final)

## Estructura del repositorio (actualizada)
/
├── README.md
├── main.py # Orquestador principal (conexión y limpieza)
├── estadisticas.py # Script para Avance 3 (estadísticas)
├── src/
│ ├── api_client.py # Conexión a yfinance
│ ├── cleaner.py # Limpieza (ahora simplificada)
│ ├── validators.py # Validaciones (no se usa actualmente)
│ └── utils.py # Utilidades (opcional)
├── data/
│ ├── raw/ # Datos crudos (response.json)
│ └── clean/ # Datos limpios (data_clean.json)
├── results/ # Resultados de estadísticas
└── figures/ # Próximamente gráficas

## Funcionamiento general
El programa se conecta a Yahoo Finance mediante yfinance, obtiene datos de un símbolo (por ejemplo, GOOGL, AAPL, MSFT), los limpia y guarda en `data/clean/data_clean.json`. Luego, `estadisticas.py` calcula media, mediana, moda y una tabla de frecuencias, guardando los resultados en `results/estadisticas.txt`.

---

## Avance 1 – Script 1 v0 (histórico)

> **Nota:** Este avance se realizó inicialmente con SerpApi. Actualmente el proyecto usa yfinance.

### Cómo se ejecutaba originalmente
```bash
python script1.pyº