# Mi Proyecto
# Cuadro de Mandos - Análisis de Vehículos Usados

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit**, diseñada para explorar y analizar un conjunto de datos de anuncios de venta de coches en Estados Unidos.

## Descripción

La aplicación permite al usuario visualizar gráficas interactivas que facilitan el análisis exploratorio del conjunto de datos `vehicles_us.csv`. Las principales funcionalidades incluyen:

- Un **histograma** de la distribución del kilometraje (odómetro) de los vehículos.  
- Un **gráfico de dispersión** que muestra la relación entre el kilometraje y el precio de los coches.  
- Interactividad mediante **casillas de verificación**, para mostrar u ocultar cada gráfica dinámicamente.

## Cómo usar

1. Asegúrate de tener un entorno virtual configurado e instala las dependencias:
pip install -r requirements.txt

2. Inicia la aplicación Streamlit desde la raíz del proyecto:
streamlit run app.py

3. Accede a la app desde tu navegador para explorar los gráficos interactivos.