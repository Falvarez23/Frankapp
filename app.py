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

    response = requests.post(AZURE_ENDPOINT, headers=headers, json=datos_estudiante)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Función para preparar los datos del estudiante
def preparar_datos_estudiante(estudiante):
    datos = {
        "Nombre": estudiante['nombre'],
        "Edad": estudiante['edad'],
        "Sexo": estudiante['sexo'],
        # Agrega más campos necesarios
    }
    return datos

# Interfaz de Streamlit
st.title("Recomendador de Carrera - Resultados del Test")

# Datos del estudiante (esto lo puedes cambiar según cómo obtienes los datos en tu app)
estudiante_seleccionado = {
    "nombre": "Juan Pérez",
    "edad": 20,
    "sexo": "M",
    # Agrega más datos según tu app
}

# Prepara los datos para enviar al modelo
datos_estudiante = preparar_datos_estudiante(estudiante_seleccionado)

# Hacer la solicitud al modelo
prediccion = obtener_prediccion(datos_estudiante)

# Mostrar el resultado de la predicción
if prediccion:
    st.write("Predicción del modelo:")
    st.json(prediccion)
