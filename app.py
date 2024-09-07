import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Recomendador de Carrera - Resultados del Test")

# Pedir al usuario que cargue el archivo CSV del test
uploaded_file = st.file_uploader("Sube el archivo del test en formato CSV", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo cargado
    df_test = pd.read_csv(uploaded_file)
    st.write("Aquí están los datos del archivo:")
    st.write(df_test)
    
    # Aquí podrías incluir tu lógica para procesar los resultados del test y mostrar las recomendaciones
    # Ejemplo: Mostrar las 3 carreras recomendadas del test
    st.subheader("Carreras recomendadas")
    if 'Carrera 1 (más alta)' in df_test.columns:
        st.write(df_test['Carrera 1 (más alta)'])
    else:
        st.write("No se encontraron las columnas de carreras recomendadas.")
    
    # Agrega más código para calcular o mostrar otros datos relevantes
    # Por ejemplo, podrías agregar gráficos o tablas adicionales

else:
    st.write("Por favor, sube un archivo CSV para comenzar.")
