# GENERADOR DE RESUMENES 
El objetivo principal de este proyecto es desarrollar y comparar distintos enfoques de resumen automático de textos en español, combinando métodos clásicos 
(extractivos) con modelos avanzados de lenguaje (abstractivos). Se busca analizar qué tipo de modelo genera resúmenes más fieles, coherentes y eficientes.

## Estructura del proyecto 🗃️

## Colab ▶
Notebooks desarrollados en Google Colab para experimentación y evaluación de modelos:
- abstractivo.ipynb: Entrenamiento del modelo T5-small con fine-tuning sobre el dataset MLSUM.
- comparativa_extractivo_abstractivo.ipynb: Métodos extractivos y comparativa entre los modelos
  
## Scraper 
Scripts en Python para obtener datos reales desde fuentes online
- scraping.py: Extracción de noticias recientes desde el diario La Razón.
- scraping_Gemini.py: Recolección de artículos científicos desde Wikipedia y procesamiento previo al resumen.


## Dataset 📑
Conjuntos de datos utilizados para entrenamiento y evaluación:
- noticias_10.csv: Noticias reales recopiladas mediante scraping de medios digitales.
- wikipedia_resumenes.tsv: Artículos técnicos de Wikipedia con sus respectivos resúmenes generados.

## Documentación 📄
Documentación asociada al proyecto:
- documentacion_final.pdf: Memoria detallada del proyecto con justificación, metodología, comparativa de modelos y análisis de resultados.
