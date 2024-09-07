import streamlit as st
import requests
import json

# Configurar el endpoint y la API Key
AZURE_ENDPOINT = "http://24b2f267-69fe-459b-a13e-d0942833b354.eastus2.azurecontainer.io/score"
AZURE_API_KEY = "g2KD6q7U7ibu5KIsZcmCYJwcYs2NLpLj"

# Función para realizar la solicitud al modelo
def obtener_prediccion(datos_estudiante):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AZURE_API_KEY}"
    }

    # El modelo espera que los datos estén dentro del campo "Inputs"
    body = {
        "Inputs": {
            "data": [datos_estudiante]  # Asegúrate de que los datos van en formato de lista
        }
    }

    response = requests.post(AZURE_ENDPOINT, headers=headers, json=body)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Interfaz de Streamlit
st.title("Recomendador de Carrera - Resultados del Test")

# Obtener datos del estudiante mediante input en Streamlit
nombre = st.text_input("Nombre del estudiante", value="Juan Pérez")
edad = st.slider("Edad", 16, 25, 20)  # Edad entre 16 y 25 años
sexo = st.selectbox("Sexo", ["M", "F"])

# Preparar los datos para el envío
datos_estudiante = {
    "Nombre": nombre,
    "Edad": edad,
    "Sexo": sexo
}

# Hacer la solicitud al modelo cuando el usuario presiona el botón
if st.button("Obtener predicción"):
    prediccion = obtener_prediccion(datos_estudiante)
    if prediccion:
        st.write("Predicción del modelo:")
        st.json(prediccion)
