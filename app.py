import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Definimos las preguntas por área
preguntas = {
    "Tecnología y Desarrollo de Software": [
        "¿Te sientes atraído por el campo de la robótica y la automatización?",
        "¿Te interesa explorar el potencial de la IA y el aprendizaje automático?",
        "¿Te gusta trabajar con herramientas para reparar dispositivos tecnológicos?",
        "¿Te gustaría participar en el desarrollo de software para análisis de datos científicos?",
        "¿Te preocupa la seguridad informática y proteger los sistemas de ataques cibernéticos?"
    ],
    "Creatividad y Medios Digitales": [
        "¿Te atrae la idea de utilizar herramientas digitales para expresar tu creatividad?",
        "¿Te emociona trabajar en proyectos que integren arte, diseño y tecnología?",
        "¿Te consideras una persona con habilidades de comunicación visual y narrativa?",
        "¿Te preocupa el impacto social de las tecnologías digitales?",
        "¿Disfrutas de analizar las tendencias del mercado digital?"
    ]
}

# Opciones de respuesta y los valores que corresponden a cada una
opciones_respuesta = {
    "Nunca": 0,
    "A veces": 1,
    "Siempre": 2
}

# Descripciones breves de cada subárea
descripciones_subarea = {
    "Tecnología y Desarrollo de Software": "Técnico-manual: Habilidad para trabajar con herramientas y maquinaria, resolver problemas prácticos y realizar tareas manuales.",
    "Creatividad y Medios Digitales": "Artístico-creativo: Capacidad para expresarse a través de diferentes medios artísticos como la música, la pintura, la escritura o la danza."
}

# Función para calcular el puntaje y la interpretación
def calcular_puntaje_area(respuestas):
    puntaje_total = sum(respuestas)
    if 2 <= puntaje_total <= 5:
        interpretacion = "Bajo interés o potencial"
    elif 6 <= puntaje_total <= 8:
        interpretacion = "Interés o potencial moderado"
    elif 9 <= puntaje_total <= 10:
        interpretacion = "Alto interés o potencial"
    else:
        interpretacion = "Sin interés"
    return puntaje_total, interpretacion

# Gráfico de radar
def radar_chart(labels, values, title):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='purple', alpha=0.25)
    ax.plot(angles, values, color='purple', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title(title, size=15, color='purple', y=1.1)
    st.pyplot(fig)

# Gráfico de barras apiladas
def barra_apilada_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['#66b3ff','#99ff99','#ffcc99'])
    ax.set_xlabel("Áreas")
    ax.set_ylabel("Puntajes")
    ax.set_title(title)
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

# Gráfico de líneas
def line_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.plot(labels, values, marker='o', linestyle='-', color='purple')
    ax.set_xlabel("Áreas")
    ax.set_ylabel("Puntajes")
    ax.set_title(title)
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

# Gráfico de tarta
def pie_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Purples(np.linspace(0.5, 1, len(values))))
    ax.set_title(title)
    st.pyplot(fig)

# Histograma
def histograma_chart(values, title):
    fig, ax = plt.subplots()
    ax.hist(values, bins=[0, 2, 5, 8, 10], color='purple', alpha=0.7, rwidth=0.85)
    ax.set_xlabel("Rangos de Puntajes")
    ax.set_ylabel("Frecuencia")
    ax.set_title(title)
    st.pyplot(fig)

# Gráfico de barras horizontales
def barras_horizontales(labels, values, title):
    fig, ax = plt.subplots()
    ax.barh(labels, values, color='purple')
    ax.set_xlabel("Puntajes")
    ax.set_title(title)
    st.pyplot(fig)

# Título del test
st.title("Test de Intereses y Potenciales")

# Inicializamos un diccionario para almacenar las respuestas del usuario
respuestas_usuario = {}

# Iteramos por cada área y mostramos las preguntas con opciones de respuesta
for area, preguntas_area in preguntas.items():
    st.header(f"Área: {area}")
    respuestas = []
    for pregunta in preguntas_area:
        respuesta = st.radio(pregunta, list(opciones_respuesta.keys()))
        respuestas.append(opciones_respuesta[respuesta])
    respuestas_usuario[area] = respuestas

# Botón para calcular los resultados
if st.button("Calcular Resultados"):
    st.subheader("Resultados del Test")
    puntajes = {}
    for area, respuestas_area in respuestas_usuario.items():
        puntaje, interpretacion = calcular_puntaje_area(respuestas_area)
        descripcion = descripciones_subarea.get(area, "Descripción no disponible")
        st.write(f"Área: {area}")
        st.write(f"Descripción: {descripcion}")
        st.write(f"Puntaje total: {puntaje}")
        st.write(f"Interpretación: {interpretacion}")
        st.write("---")
        puntajes[area] = puntaje

    # Crear gráficos con los puntajes calculados
    labels = list(puntajes.keys())
    values = list(puntajes.values())
    
    # Gráfico de radar
    radar_chart(labels, values, "Gráfico de Radar - Puntajes por Área")
    
    # Gráfico de barras apiladas
    barra_apilada_chart(labels, values, "Gráfico de Barras Apiladas - Puntajes por Área")
    
    # Gráfico de líneas
    line_chart(labels, values, "Gráfico de Líneas - Puntajes por Área")
    
    # Gráfico de tarta
    pie_chart(labels, values, "Gráfico de Tarta - Puntajes por Área")
    
    # Histograma
    histograma_chart(values, "Histograma de Puntajes")
    
    # Gráfico de barras horizontales
    barras_horizontales(labels, values, "Gráfico de Barras Horizontales - Puntajes por Área")
