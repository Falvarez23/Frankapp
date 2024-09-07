

import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Recomendador de Carrera - Resultados del Test')

# Cargar los datos del test y de la industria (aquí ajusta la ruta de tus archivos CSV)
df_test = pd.read_csv('ruta_a_tu_archivo_test.csv')
df_industry = pd.read_csv('ruta_a_tu_archivo_industria.csv')

# Mostrar los primeros registros del test
st.subheader('Datos del Test:')
st.write(df_test.head())  # Muestra las primeras filas de los datos del test

# Mostrar los primeros registros de la industria
st.subheader('Datos de la Industria:')
st.write(df_industry.head())  # Muestra las primeras filas de los datos de la industria

# Unir los datos del test con los datos de la industria
df_combined = pd.merge(df_test, df_industry, left_on='Carrera 1 (más alta)', right_on='Carrera', how='inner')

# Mostrar los datos combinados
st.subheader('Datos Combinados (Test + Industria):')
st.write(df_combined.head())  # Muestra las primeras filas de los datos combinados

# Simular una recomendación de carrera para un estudiante
st.subheader('Carrera Recomendadas para el Estudiante')
for index, row in df_combined.iterrows():
    st.write(f"Estudiante: {row['Nombre']} | Carrera recomendada: {row['Carrera']} - {row['Valor de la industria']}")


