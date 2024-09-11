import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Definir el estado inicial de la aplicación
    if 'step' not in st.session_state:
        st.session_state.step = 0  # Etapa del test (pantalla inicial = 0)

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

    # Pantalla inicial (pantalla de bienvenida)
    if st.session_state.step == 0:
        st.title("¡Gracias por tu compra!")
        st.subheader("Test de Exploración de Carreras Adquirido")

        st.markdown("""
        <p style='text-align: center; font-size: 1.2em;'>
            ¡Gracias por adquirir nuestro <strong>Test de Exploración de Carreras</strong>! 
            Haz clic en el botón de abajo para comenzar el test y descubrir tus mejores opciones de carrera.
        </p>
        """, unsafe_allow_html=True)

        # Botón para comenzar el test
        if st.button("¡Comenzar Test!"):
            st.session_state.step = 1  # Avanzar al test

    # Pantalla del test con barra de progreso
    elif st.session_state.step > 0 and st.session_state.step <= len(questions):
        st.title("Test de Exploración de Carreras")

        # Barra de progreso
        progress = (st.session_state.step - 1) / len(questions)
        st.progress(progress)

        # Mostrar la pregunta actual
        question_idx = st.session_state.step - 1
        st.write(f"Pregunta {st.session_state.step} de {len(questions)}")
        st.write(questions[question_idx])

        # Recoger la respuesta
        response = st.radio("Elige tu respuesta:", options, key=question_idx)

        # Botón para ir a la siguiente pregunta
        if st.button("Siguiente"):
            st.session_state.step += 1

    # Pantalla final después de completar el test
    elif st.session_state.step > len(questions):
        st.title("¡Test completado!")
        st.markdown("""
        <p style='text-align: center; font-size: 1.2em;'>
            ¡Gracias por completar el Test de Exploración de Carreras! Pronto recibirás los resultados que te guiarán hacia las mejores opciones de carrera.
        </p>
        """, unsafe_allow_html=True)

        # Reiniciar el test
        if st.button("Volver al inicio"):
            st.session_state.step = 0  # Volver a la pantalla de bienvenida

if __name__ == "__main__":
    main()
