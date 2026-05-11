# PIA_PytonMexican
#Analisis del comportamiento de la Bolsa de Valores con Google Finance API 

#Presentación 
Proyecto Integrador de Aprendizaje de la materia de Programación Basica con la Maestra Perla Marviera

## Integrantes del equipo
- Ana María – Matrícula: 2190413
- Alexander Flores – Matrícula: 

## Descripción 
El proyecto utiliza la API de Google Finance a traves de SerpApi para obtener datos y comparativa sobre el comportamiento financiero de la bolsa de Valores. Los datos que se recopilaran se almacenan en formato JSON y servira como base para su análisis 

## Objetivo 
Buscar, analizar y comparar aquellas empresas que tuvieron mas alzas, aquellas que tuvieron mas bajas a partir del 2020 hasta la actualidad.


## API elegida
SerpApi – Google Finance API  
- Documentación oficial: [https://serpapi.com/google-finance-api](https://serpapi.com/google-finance-api)

## Elegimos esta API porque nos permite acceder a datos financieros reales de la bolsa de valores en formato JSON estructurado. Es adecuada para nuestro proyecto, ya que necesitamos comparar el comportamiento de acciones tecnológicas (GOOGL, MSFT, AMZN) y responder preguntas sobre tendencias del mercado.

## Pregunta de investigación
-¿Cual fue el año con el desplome mas bajo en ese periodo?
-¿La bolsa son afectadas por la Geopolitica o por la Politica de su país de origen?

## Tecnologías utilizadas
-Python 
-SerApi(API de Google Finance)
-Solicitudes

## Estructura del repositorio
README.m
request_test.py
data/
raw/
response.json

## Funcionamiento
El programa esta conectado a una API de Google Finance, obtiene los datos y los guarda en un archivo JSON para después analizarlos.


