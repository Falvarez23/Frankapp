import streamlit as st

def show_test_page():
    st.title("Test de Exploración de Carreras")

    # Preguntas del test
    questions = [
        "¿Te sientes atraído por el campo de la robótica y la automatización?",
        "¿Te atrae la idea de utilizar herramientas digitales para expresar tu creatividad?",
        # Añade más preguntas aquí...
    ]

    # Opciones de respuesta
    options = ["Bajo interés", "Interés moderado", "Alto interés"]

    if 'step' not in st.session_state:
        st.session_state.step = 0

    # Pantalla inicial
    if st.session_state.step == 0:
        st.write("Este test está diseñado para ayudarte a identificar tus intereses y habilidades.")
        if st.button("Comenzar Test"):
            st.session_state.step = 1

    # Pantalla de preguntas
    elif st.session_state.step > 0 and st.session_state.step <= len(questions):
        question_idx = st.session_state.step - 1
        st.write(f"Pregunta {st.session_state.step} de {len(questions)}")
        st.radio("Selecciona una opción:", options, key=f"response_{question_idx}")

        if st.button("Siguiente"):
            st.session_state.step += 1
    else:
        st.session_state.step = 0
        st.write("Gracias por completar el test.")
