import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Encabezado de la aplicación
st.header('Gráficos sobre el odómetro y el precio de los vehículos')
st.write('Explora la distribución del odómetro y la relación entre el odómetro y el precio.')

# Leer los datos del archivo CSV
car_data = pd.read_csv('./data/vehicles_us.csv')

# Casilla para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del odómetro(millas)')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para las columnas odómetro y precio')
    fig = px.scatter(car_data, x='odometer', y='price', title='Odómetro vs precio')
    st.plotly_chart(fig, use_container_width=True)