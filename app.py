import streamlit as st
import pandas as pd
import requests
import json

# Título de la App
st.title("Recomendador de Carreras")

# 1. Entrada del Estudiante (datos ficticios o cargados desde un archivo)
st.header("Datos del Estudiante")

# Cargar CSV para simular datos del test
uploaded_file = st.file_uploader("Sube el archivo con los datos del estudiante", type=["csv"])

if uploaded_file is not None:
    df_test = pd.read_csv(uploaded_file)
    st.write("Datos del archivo cargado:", df_test)

    # Selección del estudiante
    estudiantes = df_test['Nombre'].unique()
    selected_estudiante = st.selectbox("Selecciona un estudiante", estudiantes)

    # Mostrar los datos del estudiante seleccionado
    datos_estudiante = df_test[df_test['Nombre'] == selected_estudiante]
    st.write(f"Datos del estudiante: {selected_estudiante}", datos_estudiante)

    # Datos clave del test para el estudiante seleccionado
    areas_interes = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo',
                     'Social-asistencial', 'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']

    puntajes_interes = datos_estudiante[areas_interes].T  # Transpuesta para graficar

    # Visualización de los puntajes
    st.bar_chart(puntajes_interes)

    # 2. Llamada al modelo en Azure ML usando el endpoint (simulación)
    st.header("Recomendación basada en el modelo")

    if st.button("Obtener recomendación de carrera"):
        # Aquí llamas a la API del modelo en Azure
        api_url = "TU_ENDPOINT_DEL_MODELO"  # Cambia esto por el endpoint real de Azure
        api_key = "TU_API_KEY"  # Coloca aquí tu API key
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
        
        # Prepara los datos para enviarlos al modelo
        input_data = datos_estudiante.to_dict(orient="records")
        response = requests.post(api_url, headers=headers, json={"data": input_data})
        
        if response.status_code == 200:
            resultado = response.json()
            st.write("Carrera recomendada:", resultado['carrera'])
        else:
            st.write("Error en la llamada al modelo:", response.text)

    # 3. Datos de la industria
    st.header("Datos de la industria para la carrera recomendada")
    df_industria = pd.read_csv('ruta_a_datos_de_la_industria.csv')  # Cargar datos de la industria
    carrera_recomendada = datos_estudiante['Carrera 1 (más alta)'].values[0]
    datos_industria = df_industria[df_industria['Carrera'] == carrera_recomendada]
    st.write(f"Carrera recomendada: {carrera_recomendada}")
    st.write("Datos de la industria para la carrera recomendada:", datos_industria)

    # Visualización de la proyección de crecimiento
    st.bar_chart(datos_industria[['Proyección de crecimiento profesionales']])
