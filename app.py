import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Estilos personalizados con CSS
st.markdown("""
    <style>
    /* Fondo de la página */
    .main {
        background-color: #F5F7FA;
    }

    /* Estilo de títulos */
    h1, h2, h3 {
        color: #22223B;
        font-family: 'Helvetica', sans-serif;
    }

    /* Estilo para el botón "Adquirir Test" */
    .stButton button:first-child {
        background-color: #4B9AE3;
        color: white;
        border-radius: 10px;
        border: 2px solid #4B9AE3;
        padding: 10px 20px;
        font-size: 16px;
        margin-right: 10px;
    }

    /* Estilo para el botón "Ver Resultado" */
    .stButton button:last-child {
        background-color: white;
        color: #4B9AE3;
        border: 2px solid #4B9AE3;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        margin-right: 10px;
    }

    /* Fondo de los contenedores */
    .stContainer {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Mensaje de introducción
def mostrar_introduccion():
    st.title("¡Sueña en grande, logra tus metas!")
    st.write("""
        ### ¡Descubre tu camino hacia el éxito con **Mentess™** nuestro test de exploración de carreras! 

        En **ScholarShine**, creemos que cada estudiante tiene un potencial único que merece ser explorado. 
        Nuestra prueba te ayudará a identificar tus **intereses**, **habilidades** y **atributos**, guiándote hacia carreras que se ajusten perfectamente a tu perfil.

        Con resultados claros y detallados, estarás un paso más cerca de tomar decisiones informadas sobre tu futuro académico y profesional.

        ¡Comienza ahora con nuestro test de exploración de carreras y descubre tu futuro!
    """)

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

# Función para crear un gráfico de radar
def radar_chart(labels, values, title):
    num_vars = len(labels)

    # Configurar el ángulo para los ejes de la gráfica
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # La gráfica necesita que las coordenadas estén cerradas, así que añadimos el primer valor al final
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='purple', alpha=0.25)
    ax.plot(angles, values, color='purple', linewidth=2)

    # Añadir etiquetas a cada eje
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Añadir título
    ax.set_title(title, size=15, color='purple', y=1.1)

    # Mostrar la gráfica
    st.pyplot(fig)

# Función para crear un gráfico de barras
def bar_chart(labels, values, title):
    if len(labels) != len(values):
        st.error("Error: Las etiquetas y los valores no tienen la misma longitud.")
        return

    fig, ax = plt.subplots()
    ax.bar(labels, values, color='#4B9AE3')
    ax.set_xlabel("Áreas")
    ax.set_ylabel("Puntajes")
    ax.set_title(title)
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

# Función para graficar una red neuronal simple
def neural_network_chart():
    fig, ax = plt.subplots(figsize=(6, 6))

    # Coordenadas para las capas de la red
    layers = [3, 5, 2]  # Ejemplo de red con 3 neuronas de entrada, 5 en la oculta y 2 de salida
    x_spacing = np.linspace(0, 1, len(layers))

    for i, layer in enumerate(layers):
        y_spacing = np.linspace(0, 1, layer)
        ax.scatter([x_spacing[i]] * layer, y_spacing, s=100)

        # Dibujar conexiones entre las capas
        if i > 0:
            for prev_y in np.linspace(0, 1, layers[i-1]):
                for curr_y in y_spacing:
                    ax.plot([x_spacing[i-1], x_spacing[i]], [prev_y, curr_y], 'k-', lw=0.5)

    ax.set_title("Visualización de Red Neuronal")
    ax.axis('off')
    st.pyplot(fig)

# Mostrar introducción si no se ha iniciado el test
if 'test_iniciado' not in st.session_state:
    st.session_state['test_iniciado'] = False
    mostrar_introduccion()

# Botón para iniciar el test
if st.session_state['test_iniciado'] == False and st.button("Iniciar Test"):
    st.session_state['test_iniciado'] = True
    st.experimental_rerun()

# Si el test se ha iniciado, mostrar las preguntas
if st.session_state['test_iniciado']:
    st.title("Test de Exploración de Carreras")
    
    # Inicializamos un diccionario para almacenar las respuestas del usuario
    respuestas_usuario = {}

    # Iteramos por cada área y mostramos las preguntas con opciones de respuesta
    for area, preguntas_area in preguntas.items():
        st.header(f"Área: {area}")
        respuestas = []
        for pregunta in preguntas_area:
            respuesta = st.radio(pregunta, list(opciones_respuesta.keys()))
            # Almacena el valor numérico de la respuesta seleccionada
            respuestas.append(opciones_respuesta[respuesta])
        respuestas_usuario[area] = respuestas

    # Botón para calcular los resultados
    if st.button("Ver Resultados"):
        st.subheader("Resultados del Test")
        puntajes = {}
        for area, respuestas_area in respuestas_usuario.items():
            puntaje, interpretacion = calcular_puntaje_area(respuestas_area)
            descripcion = descripciones_subarea.get(area, "Descripción no disponible")
            st.write(f"Área: {area}")
            st.write(f"Descripción: {descripcion}")
            st.write(f"Puntaje total: {puntaje}")
            st.write(f"
