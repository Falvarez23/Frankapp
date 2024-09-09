import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Gráfico de Puntajes de Carreras")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV con puntajes de carreras", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)

    # Asumimos que hay dos columnas en el archivo: 'Carrera' y 'Puntaje'
    st.write("Datos cargados:")
    st.dataframe(df)

    # Ordenar el dataframe por el puntaje de las carreras
    df_sorted = df.sort_values(by="Puntaje", ascending=False)

    # Seleccionar las 3 carreras con los puntajes más altos
    top_3_carreras = df_sorted.head(3)

    # Crear gráfico de barras de todas las carreras
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_sorted['Carrera'], df_sorted['Puntaje'], color='lightblue')

    # Destacar las 3 carreras con los puntajes más altos
    for i, row in top_3_carreras.iterrows():
        ax.bar(row['Carrera'], row['Puntaje'], color='orange')

    ax.set_xlabel("Carreras")
    ax.set_ylabel("Puntaje")
    ax.set_title("Puntajes de Carreras (con las 3 más altas destacadas)")
    plt.xticks(rotation=90)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    # Mostrar las 3 carreras con mayor puntaje
    st.write("Las 3 carreras con mayor puntaje son:")
    st.dataframe(top_3_carreras)
