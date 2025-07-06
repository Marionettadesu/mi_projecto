import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Cuadro de Mandos: Análisis de Vehículos Usados')

# Casilla para el histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Construyendo un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer", title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para el gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión Precio vs Kilometraje')

if build_scatter:
    st.write('Construyendo un gráfico de dispersión: Precio vs Kilometraje')
    
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title='Precio vs Kilometraje',
                      labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig2, use_container_width=True)

# Botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title='Precio vs Kilometraje',
                      labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig2, use_container_width=True)