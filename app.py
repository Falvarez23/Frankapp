import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Formulario de Interés", page_icon=":memo:", layout="centered")

    # Aplicar estilo CSS
    st.markdown(
        """
        <style>
        .main {
            background-color: #FFFFFF; /* Fondo blanco */
            color: #333333; /* Texto gris oscuro para mejor contraste */
        }
        .stRadio label {
            color: #333333; /* Texto gris oscuro para las opciones de radio */
        }
        .stButton button {
            background-color: #007BFF; /* Botón azul */
            color: #FFFFFF; /* Texto blanco en el botón */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título
    st.title("Formulario de Interés")

    # Preguntas del formulario
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

    # Almacenar respuestas
    responses = {}

    st.header("Responde las siguientes preguntas:")

    # Iterar sobre las preguntas para crear los campos del formulario
    for i, question in enumerate(questions):
        response = st.radio(question, options, key=i)
        responses[question] = response
    
    # Botón para enviar el formulario
    if st.button("Enviar"):
        st.write("Respuestas recibidas:")
        for question, response in responses.items():
            st.write(f"{question}: {response}")

if __name__ == "__main__":
    main()
