import streamlit as st

def show_test_page():
    st.markdown("<h1>Test de Exploración de Carreras</h1>", unsafe_allow_html=True)

    # Preguntas del test
    questions = [
        "¿Te sientes atraído por el campo de la robótica y la automatización?",
        "¿Te atrae la idea de utilizar herramientas digitales para expresar tu creatividad?",
        "¿Te entusiasma la idea de contribuir al desarrollo de videojuegos y experiencias interactivas?",
        "¿Te apasiona la idea de mejorar la salud y el bienestar de las personas?",
        "¿Te sientes motivado/a por trabajar en organizaciones sin fines de lucro dedicadas a problemas sociales?",
        "¿Te apasiona la idea de crear tu propio negocio o trabajar en un entorno dinámico?",
        "¿Te llama la atención el mundo del comercio electrónico?",
        "¿Te apasiona la idea de contribuir a la educación de las personas?",
        "¿Te resulta sorprendente el mundo del marketing y la publicidad?",
        "¿Te apasiona la idea de trabajar en la creación y diseño de prendas de moda?"
    ]

    # Opciones de respuesta
    options = [
        "Bajo interés o potencial en la subárea.",
        "Interés o potencial moderado en la subárea.",
        "Alto interés o potencial en la subárea."
    ]

    if 'step' not in st.session_state:
        st.session_state.step = 0

    # Pantalla inicial
    if st.session_state.step == 0:
        st.write("Este test está diseñado para ayudarte a identificar tus intereses y habilidades.")
        if st.button("Comenzar Test"):
            st.session_state.step = 1

    # Preguntas del test con barra de progreso
    elif st.session_state.step > 0 and st.session_state.step <= len(questions):
        question_idx = st.session_state.step - 1
        st.markdown(f"<h2>Pregunta {st.session_state.step} de {len(questions)}</h2>", unsafe_allow_html=True)

        # Barra de progreso
        progress = (st.session_state.step - 1) / len(questions)
        st.progress(progress)

        # Pregunta actual
        st.write(questions[question_idx])
        st.radio("Selecciona una opción:", options, key=f"response_{question_idx}")

        if st.button("Siguiente"):
            st.session_state.step += 1

    # Mostrar el botón para ver resultados al finalizar
    elif st.session_state.step > len(questions):
        st.session_state.step = 0
        st.write("¡Has completado el test! Haz clic en el botón a continuación para ver tus resultados.")
        if st.button("Ver Resultados"):
            st.session_state.step = len(questions) + 1  # Avanzar a la página de resultados
