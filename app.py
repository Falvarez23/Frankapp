import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Contenedor principal
    container = st.container()
    
    with container:
        # Título del test
        st.title("Test de Exploración de Carreras")
        
        # Introducción al test
        st.write("""
        ¡Gracias por adquirir nuestro Test de Exploración de Carreras!
        Este test está diseñado para ayudarte a identificar tus intereses y habilidades,
        guiándote hacia las carreras que más se ajustan a tu perfil.
        """)

        # Pantalla de bienvenida
        if 'step' not in st.session_state:
            st.session_state.step = 0

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

        # Pantalla inicial
        if st.session_state.step == 0:
            st.subheader("¡Bienvenido!")
            st.write("""
            Este test está diseñado para explorar tus intereses en varias áreas profesionales.
            Haz clic en el botón de abajo para comenzar el test.
            """)
            if st.button("Comenzar Test"):
                st.session_state.step = 1

        # Preguntas del test
        elif st.session_state.step <= len(questions):
            question_idx = st.session_state.step - 1
            st.subheader(f"Pregunta {st.session_state.step} de {len(questions)}")
            st.write(questions[question_idx])
            response = st.radio("Selecciona una opción:", options, key=f"response_{question_idx}")

            if st.button("Siguiente"):
                st.session_state.step += 1

        # Resultados del test
        else:
            st.subheader("¡Resultados del Test!")
            st.write("Gracias por completar el test. Estos son tus resultados:")
            
            # Aquí puedes incluir el cálculo de resultados según las respuestas
            st.write("**Tus respuestas han sido registradas con éxito.**")

            # Botón para reiniciar el test
            if st.button("Volver al inicio"):
                st.session_state.step = 0

if __name__ == "__main__":
    main()
