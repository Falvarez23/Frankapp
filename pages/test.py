import streamlit as st

def show_test_page():
    st.markdown("<h1 style='color:#467BE9; text-align:center;'>Test de Exploración de Carreras</h1>", unsafe_allow_html=True)

    # Preguntas del test
    questions = [
        "¿Te sientes atraído por el campo de la robótica y la automatización?",
        "¿Te atrae la idea de utilizar herramientas digitales para expresar tu creatividad?",
    ]

    # Opciones de respuesta
    options = ["Bajo interés", "Interés moderado", "Alto interés"]

    if 'step' not in st.session_state:
        st.session_state.step = 0

    # Pantalla inicial
    if st.session_state.step == 0:
        st.write("Este test está diseñado para ayudarte a identificar tus intereses y habilidades.")
        if st.button("Comenzar Test", key="start_test"):
            st.session_state.step = 1

    # Preguntas del test
    elif st.session_state.step > 0 and st.session_state.step <= len(questions):
        question_idx = st.session_state.step - 1
        st.markdown(f"<h2 style='color:#467BE9;'>Pregunta {st.session_state.step} de {len(questions)}</h2>", unsafe_allow_html=True)
        st.write(questions[question_idx])
        st.radio("Selecciona una opción:", options, key=f"response_{question_idx}")

        if st.button("Siguiente", key=f"next_{question_idx}"):
            st.session_state.step += 1

    else:
        st.session_state.step = 0
        st.write("Gracias por completar el test.")
