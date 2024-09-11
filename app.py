import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Formulario de Interés", page_icon=":memo:", layout="centered")

    # Aplicar estilo CSS para mejorar el diseño general y la experiencia de usuario
    st.markdown(
        """
        <style>
        /* Fondo de la página */
        .main {
            background-color: #f1f5fd; /* Azul claro */
        }

        /* Título principal */
        h1 {
            color: #1F1F1F; /* Negro oscuro */
            font-size: 3em; /* Tamaño de fuente grande para el título */
            font-weight: 700; /* Negrita */
            margin-bottom: 20px; /* Espaciado inferior */
            text-align: center;
        }

        /* Subtítulo */
        h2 {
            color: #1F1F1F; /* Negro oscuro */
            font-size: 1.5em; /* Tamaño de subtítulo */
            font-weight: 500;
            margin-bottom: 30px; /* Espaciado inferior */
        }

        /* Preguntas del formulario */
        .stRadio label {
            font-size: 1.1em; /* Tamaño del texto de las preguntas */
            color: #333333; /* Gris oscuro */
            font-weight: 500; /* Seminegrita para mejor legibilidad */
            margin-bottom: 15px; /* Espaciado entre preguntas */
        }

        /* Opciones de radio */
        .stRadio div {
            font-size: 1em; /* Tamaño de las opciones de respuesta */
            color: #333333; /* Gris oscuro */
        }

        /* Botones */
        .stButton button {
            background-color: #3366FF; /* Azul fuerte */
            color: #FFFFFF !important; /* Texto blanco */
            font-size: 1.2em; /* Tamaño del texto de los botones */
            padding: 10px 20px; /* Espaciado dentro del botón */
            border-radius: 5px; /* Bordes redondeados */
            border: none; /* Sin borde */
            transition: background-color 0.3s ease; /* Animación suave al pasar el mouse */
        }
        .stButton button:hover {
            background-color: #2850b8; /* Color más oscuro al pasar el mouse */
        }
        
        /* Texto recibido (después de enviar respuestas) */
        .stMarkdown {
            font-size: 1.1em;
            color: #333333;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Título y subtítulo del formulario
    st.title("Formulario de Interés")
    st.header("Responde las siguientes preguntas:")

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
