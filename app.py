import streamlit as st
import requests

# Diccionario que relaciona preguntas con carreras (debes ajustar las relaciones)
carreras_dict = {
    "Tecnología y desarrollo de software": [1, 57, 38, 76, 19],
    "Ciencias de la salud": [22, 41, 60, 79],
    "Energías renovables": [23, 36, 42, 55, 80],
    # Añade las demás relaciones entre carreras y preguntas aquí
}

# Lista completa de las 95 preguntas
preguntas = [
    "¿Te sientes atraído por el campo de la robótica y la automatización?",
    "¿Te atrae la idea de utilizar herramientas digitales para expresar tu creatividad?",
    "¿Te entusiasma la idea de contribuir al desarrollo de videojuegos?",
    # Incluye todas las 95 preguntas completas aquí
    # ...
    "¿Te interesa investigar y desarrollar tecnologías innovadoras para el tratamiento y purificación del agua?",
]

# Función para calcular el puntaje de cada carrera
def calcular_carrera(puntajes_respuestas):
    puntajes_carrera = {}

    # Inicializar puntaje por carrera
    for carrera in carreras_dict:
        puntajes_carrera[carrera] = 0

    # Sumar los puntajes de cada carrera basado en las respuestas
    for carrera, preguntas_carrera in carreras_dict.items():
        for pregunta in preguntas_carrera:
            puntaje = puntajes_respuestas.get(pregunta, 0)
            puntajes_carrera[carrera] += puntaje

    # Seleccionar la carrera con el puntaje más alto
    carrera_recomendada = max(puntajes_carrera, key=puntajes_carrera.get)
    return carrera_recomendada, puntajes_carrera

# Interfaz de Streamlit
st.title("Recomendador de Carrera - Responde las Preguntas")

# Crear un diccionario para almacenar las respuestas del usuario
puntajes_respuestas_estudiante = {}

# Mostrar las preguntas y capturar las respuestas
for i, pregunta in enumerate(preguntas, start=1):
    respuesta = st.slider(f"Pregunta {i}: {pregunta}", 0, 10, 5)  # Respuesta en escala de 0 a 10
    puntajes_respuestas_estudiante[i] = respuesta

# Botón para calcular las puntuaciones y recomendar una carrera
if st.button("Calcular Carrera"):
    carrera_recomendada, puntajes_totales = calcular_carrera(puntajes_respuestas_estudiante)
    
    st.subheader(f"Carrera recomendada: {carrera_recomendada}")
    
    st.subheader("Puntajes por carrera:")
    for carrera, puntaje in puntajes_totales.items():
        st.write(f"{carrera}: {puntaje}")

# Función para enviar las respuestas al modelo de Azure
def enviar_datos_a_azure(puntajes_respuestas):
    # Configurar el endpoint y la API Key
    AZURE_ENDPOINT = "http://<tu-url-de-azure>/score"  # Reemplaza con tu URL del endpoint
    AZURE_API_KEY = "tu-api-key"  # Reemplaza con tu clave de API

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AZURE_API_KEY}"
    }

    # Prepara los datos para enviar a Azure
    data = {
        "Inputs": {
            "data": [puntajes_respuestas]  # Aquí envías los puntajes obtenidos
        }
    }

    response = requests.post(AZURE_ENDPOINT, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Botón para enviar los datos al modelo de Azure
if st.button("Enviar a Azure"):
    resultado = enviar_datos_a_azure(puntajes_respuestas_estudiante)
    if resultado:
        st.write("Resultado del modelo en Azure:")
        st.json(resultado)
