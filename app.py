import streamlit as st
import requests
import json

# Configurar el endpoint y la API Key
AZURE_ENDPOINT = "http://24b2f267-69fe-459b-a13e-d0942833b354.eastus2.azurecontainer.io/score"  # Reemplaza con tu URL del endpoint
AZURE_API_KEY = "g2KD6q7U7ibu5KIsZcmCYJwcYs2NLpLj"  # Reemplaza con tu clave de API

# Función para realizar la solicitud al modelo
def obtener_prediccion(datos_estudiante):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AZURE_API_KEY}"
    }

    response = requests.post(AZURE_ENDPOINT, headers=headers, json={"Inputs": {"input1": [datos_estudiante]}})
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Función para preparar los datos del estudiante
def preparar_datos_estudiante(estudiante):
    datos = {
        "Característica_1": estudiante.get('caracteristica_1', 0),
        "Característica_2": estudiante.get('caracteristica_2', 0),
        "Característica_3": estudiante.get('caracteristica_3', 0),
        # Agrega todas las características necesarias hasta las 33 que el modelo espera
        "Característica_4": estudiante.get('caracteristica_4', 0),
        "Característica_5": estudiante.get('caracteristica_5', 0),
        "Característica_6": estudiante.get('caracteristica_6', 0),
        "Característica_7": estudiante.get('caracteristica_7', 0),
        # Continúa hasta las que sean necesarias según tu modelo...
        # Añade más según los campos que necesites
    }
    return datos

# Interfaz de Streamlit
st.title("Recomendador de Carrera - Resultados del Test")

# Input de datos del estudiante (puedes ajustar esto según lo que desees pedir en el formulario)
nombre = st.text_input("Nombre del estudiante", "Frank Alvarez")
edad = st.slider("Edad", 16, 25, 21)
sexo = st.selectbox("Sexo", ["M", "F"])

# Otros inputs adicionales que necesites para las características
caracteristica_1 = st.number_input("Puntaje de característica 1", 0, 100)
caracteristica_2 = st.number_input("Puntaje de característica 2", 0, 100)
# Añade más inputs según las características que necesite tu modelo...

# Diccionario que recopila toda la información ingresada
estudiante_seleccionado = {
    "nombre": nombre,
    "edad": edad,
    "sexo": sexo,
    "caracteristica_1": caracteristica_1,
    "caracteristica_2": caracteristica_2,
    # Añade más características aquí según lo que necesite tu modelo
}

# Botón para obtener la predicción
if st.button("Obtener predicción"):
    # Prepara los datos para enviar al modelo
    datos_estudiante = preparar_datos_estudiante(estudiante_seleccionado)
    
    # Hacer la solicitud al modelo
    prediccion = obtener_prediccion(datos_estudiante)

    # Mostrar el resultado de la predicción
    if prediccion:
        st.write("Predicción del modelo:")
        st.json(prediccion)
