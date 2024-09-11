import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

def main():
    # Colores de la paleta
    azul_scholarshine = "#467BE9"
    amarillo_shine = "#FDE192"
    pink_future = "#FF5A72"
    blanco_neutro = "#F9F7F4"
    negro = "#000000"

    # Contenedor de estilo en línea para asegurar que los colores se apliquen correctamente
    st.markdown(
        f"""
        <style>
        /* Fondo general */
        .main {{
            background-color: {blanco_neutro};
            font-family: 'Arial', sans-serif;
        }}

        /* Título en Azul Scholarshine */
        h1 {{
            color: {azul_scholarshine};
        }}

        /* Subtítulo en Azul Scholarshine */
        h2 {{
            color: {azul_scholarshine};
        }}

        /* Fondo de las secciones en Amarillo Shine */
        .section {{
            background-color: {amarillo_shine};
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }}

        /* Botón de acción en Pink Future */
        .stButton button {{
            background-color: {pink_future};
            color: white;
            font-size: 1.2em;
            padding: 10px 20px;
            border-radius: 5px;
        }}

        /* Resaltar valores importantes en Pink Future */
        .highlight {{
            color: {pink_future};
            font-weight: bold;
        }}
        </style>
        """, unsafe_allow_html=True
    )

    # Preguntas del test
    questions = [
        "¿Te sientes atraído por el campo de la robótica y la automatización, y cómo estas tecnologías pueden aplicarse en contextos científicos y de investigación?",
        "¿Te atrae la idea de utilizar herramientas digitales para expresar tu creatividad y generar contenido multimedia innovador?",
        "¿Te entusiasma la idea de contribuir al desarrollo de videojuegos y experiencias interactivas mediante la creación de arte digital, diseño de personajes o entornos virtuales?",
        "¿Te apasiona la idea de mejorar la salud y el bienestar de las personas a través de diferentes intervenciones y estrategias?",
        "¿Te sientes motivado/a por la posibilidad de trabajar en organizaciones sin fines de lucro dedicadas a abordar problemas sociales, como la pobreza, la falta de vivienda o la educación desigual?",
        "¿Te apasiona la idea de crear tu propio negocio o trabajar en un entorno dinámico y cambiante?",
        "¿Te llama la atención el mundo del comercio electrónico y te interesa trabajar en el desarrollo de tiendas online o plataformas de venta digital?",
        "¿Te apasiona la idea de contribuir a la educación de las personas y mejorar sus vidas a través de la enseñanza y el aprendizaje?",
        "¿Te resulta sorprendente el mundo del marketing y la publicidad, y te interesa desarrollar estrategias creativas para comunicar mensajes a diferentes audiencias?",
        "¿Te apasiona la idea de trabajar en la creación y diseño de prendas de moda, experimentando con materiales, texturas y formas para desarrollar colecciones innovadoras y vanguardistas?"
    ]

    # Opciones de respuesta
    options = [
        "Bajo interés o potencial en la subárea.",
        "Interés o potencial moderado en la subárea.",
        "Alto interés o potencial en la subárea."
    ]

    # Estado inicial
    if 'step' not in st.session_state:
        st.session_state.step = 0

    # Pantalla inicial
    if st.session_state.step == 0:
        st.title("¡Gracias por tu compra!")
        st.subheader("Test de Exploración de Carreras Adquirido")
        st.write("Este test está diseñado para ayudarte a identificar tus intereses y habilidades.")
        st.write("Haz clic en el botón de abajo para comenzar.")

        if st.button("Comenzar Test"):
            st.session_state.step = 1

    # Pantalla de preguntas
    elif st.session_state.step <= len(questions):
        question_idx = st.session_state.step - 1
        st.title("Test de Exploración de Carreras")
        st.subheader(f"Pregunta {st.session_state.step} de {len(questions)}")
        st.write(questions[question_idx])
        response = st.radio("Elige tu respuesta:", options, key=f"response_{question_idx}")

        if st.button("Siguiente"):
            st.session_state.step += 1

    # Pantalla de resultados
    else:
        st.title("¡Resultados del Test!")
        st.write("Estos son tus resultados:")

        # Resultados en una sección con el fondo amarillo y texto destacado en rosa
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(f"**Crecimiento proyectado de tu industria**: <span class='highlight'>75%</span>", unsafe_allow_html=True)
        st.write(f"**Demanda laboral actual**: <span class='highlight'>54%</span>", unsafe_allow_html=True)
        st.write(f"**Nivel de automatización en tu industria**: <span class='highlight'>99%</span>", unsafe_allow_html=True)
        st.write(f"**Nivel de avance tecnológico en tu industria**: <span class='highlight'>14%</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Botón para volver al inicio
        if st.button("Volver al inicio"):
            st.session_state.step = 0

if __name__ == "__main__":
    main()
