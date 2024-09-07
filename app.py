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
        "Característica_4": estudiante.get('caracteristica_4', 0),
        "Característica_5": estudiante.get('caracteristica_5', 0),
        "Característica_6": estudiante.get('caracteristica_6', 0),
        "Característica_7": estudiante.get('caracteristica_7', 0),
        "Característica_8": estudiante.get('caracteristica_8', 0),
        "Característica_9": estudiante.get('caracteristica_9', 0),
        "Característica_10": estudiante.get('caracteristica_10', 0),
        "Característica_11": estudiante.get('caracteristica_11', 0),
        "Característica_12": estudiante.get('caracteristica_12', 0),
        "Característica_13": estudiante.get('caracteristica_13', 0),
        "Característica_14": estudiante.get('caracteristica_14', 0),
        "Característica_15": estudiante.get('caracteristica_15', 0),
        "Característica_16": estudiante.get('caracteristica_16', 0),
        "Característica_17": estudiante.get('caracteristica_17', 0),
        "Característica_18": estudiante.get('caracteristica_18', 0),
        "Característica_19": estudiante.get('caracteristica_19', 0),
        "Característica_20": estudiante.get('caracteristica_20', 0),
        "Característica_21": estudiante.get('caracteristica_21', 0),
        "Característica_22": estudiante.get('caracteristica_22', 0),
        "Característica_23": estudiante.get('caracteristica_23', 0),
        "Característica_24": estudiante.get('caracteristica_24', 0),
        "Característica_25": estudiante.get('caracteristica_25', 0),
        "Característica_26": estudiante.get('caracteristica_26', 0),
        "Característica_27": estudiante.get('caracteristica_27', 0),
        "Característica_28": estudiante.get('caracteristica_28', 0),
        "Característica_29": estudiante.get('caracteristica_29', 0),
        "Característica_30": estudiante.get('caracteristica_30', 0),
        "Característica_31": estudiante.get('caracteristica_31', 0),
        "Característica_32": estudiante.get('caracteristica_32', 0),
        "Característica_33": estudiante.get('caracteristica_33', 0)
    }
    return datos

# Interfaz de Streamlit
st.title("Recomendador de Carrera - Resultados del Test")

# Input de datos del estudiante
nombre = st.text_input("Nombre del estudiante", "Frank Alvarez")
edad = st.slider("Edad", 16, 25, 21)
sexo = st.selectbox("Sexo", ["M", "F"])

# Inputs para todas las características del estudiante
caracteristica_1 = st.number_input("Puntaje de característica 1", 0, 100)
caracteristica_2 = st.number_input("Puntaje de característica 2", 0, 100)
caracteristica_3 = st.number_input("Puntaje de característica 3", 0, 100)
caracteristica_4 = st.number_input("Puntaje de característica 4", 0, 100)
caracteristica_5 = st.number_input("Puntaje de característica 5", 0, 100)
caracteristica_6 = st.number_input("Puntaje de característica 6", 0, 100)
caracteristica_7 = st.number_input("Puntaje de característica 7", 0, 100)
caracteristica_8 = st.number_input("Puntaje de característica 8", 0, 100)
caracteristica_9 = st.number_input("Puntaje de característica 9", 0, 100)
caracteristica_10 = st.number_input("Puntaje de característica 10", 0, 100)
caracteristica_11 = st.number_input("Puntaje de característica 11", 0, 100)
caracteristica_12 = st.number_input("Puntaje de característica 12", 0, 100)
caracteristica_13 = st.number_input("Puntaje de característica 13", 0, 100)
caracteristica_14 = st.number_input("Puntaje de característica 14", 0, 100)
caracteristica_15 = st.number_input("Puntaje de característica 15", 0, 100)
caracteristica_16 = st.number_input("Puntaje de característica 16", 0, 100)
caracteristica_17 = st.number_input("Puntaje de característica 17", 0, 100)
caracteristica_18 = st.number_input("Puntaje de característica 18", 0, 100)
caracteristica_19 = st.number_input("Puntaje de característica 19", 0, 100)
caracteristica_20 = st.number_input("Puntaje de característica 20", 0, 100)
caracteristica_21 = st.number_input("Puntaje de característica 21", 0, 100)
caracteristica_22 = st.number_input("Puntaje de característica 22", 0, 100)
caracteristica_23 = st.number_input("Puntaje de característica 23", 0, 100)
caracteristica_24 = st.number_input("Puntaje de característica 24", 0, 100)
caracteristica_25 = st.number_input("Puntaje de característica 25", 0, 100)
caracteristica_26 = st.number_input("Puntaje de característica 26", 0, 100)
caracteristica_27 = st.number_input("Puntaje de característica 27", 0, 100)
caracteristica_28 = st.number_input("Puntaje de característica 28", 0, 100)
caracteristica_29 = st.number_input("Puntaje de característica 29", 0, 100)
caracteristica_30 = st.number_input("Puntaje de característica 30", 0, 100)
caracteristica_31 = st.number_input("Puntaje de característica 31", 0, 100)
caracteristica_32 = st.number_input("Puntaje de característica 32", 0, 100)
caracteristica_33 = st.number_input("Puntaje de característica 33", 0, 100)

# Diccionario que recopila toda la información ingresada
estudiante_seleccionado = {
    "nombre": nombre,
    "edad": edad,
    "sexo": sexo,
    "caracteristica_1": caracteristica_1,
    "caracteristica_2": caracteristica_2,
    "caracteristica_3": caracteristica_3,
    "caracteristica_4": caracteristica_4,
    "caracteristica_5": caracteristica_5,
    "caracteristica_6": caracteristica_6,
    "caracteristica_7": caracteristica_7,
    "caracteristica_8": caracteristica_8,
    "caracteristica_9": caracteristica_9,
    "caracteristica_10": caracteristica_10,
    "caracteristica_11": caracteristica_11,
    "caracteristica_12": caracteristica_12,
    "caracteristica_13": caracteristica_13,
    "caracteristica_14": caracteristica_14,
    "caracteristica_15": caracteristica_15,
    "caracteristica_16": caracteristica_16,
    "caracteristica_17": caracteristica_17,
    "caracteristica_18": caracteristica_18,
    "caracteristica_19": caracteristica_19,
    "caracteristica_20": caracteristica_20,
    "caracteristica_21": caracteristica_21,
    "caracteristica_22": caracteristica_22,
    "caracteristica_23": caracteristica_23,
    "caracteristica_24": caracteristica_24,
    "caracteristica_25": caracteristica_25,
    "caracteristica_26": caracteristica_26,
    "caracteristica_27": caracteristica_27,
    "caracteristica_28": caracteristica_28,
    "caracteristica_29": caracteristica_29,
    "caracteristica_30": caracteristica_30,
    "caracteristica_31": caracteristica_31,
    "caracteristica_32": caracteristica_32,
    "caracteristica_33": caracteristica_33
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
