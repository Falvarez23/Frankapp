import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Visualización de archivo Excel")

# Cargar el archivo Excel
uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo Excel
    df = pd.read_excel(uploaded_file)

    # Mostrar el contenido del archivo
    st.dataframe(df)

    # Botón para descargar el archivo si lo deseas
    st.download_button(
        label="Descargar archivo Excel",
        data=uploaded_file,
        file_name="archivo_descargado.xlsx"
    )
