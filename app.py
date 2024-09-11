import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Estilo CSS actualizado para modernizar el diseño y darle más espacio
    st.markdown(
        """
        <style>
        /* Fondo general */
        .main {
            background-color: #f1f5fd; /* Azul claro */
            font-family: 'Arial', sans-serif; /* Fuente clara y legible */
        }

        /* Estilo para el contenedor centrado */
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 50px 30px;
            background-color: #ffffff; /* Fondo blanco para el contenido */
            border-radius: 10px; /* Bordes redondeados */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra sutil */
        }

        /* Título principal */
        h1 {
            color: #1F1F1F; /* Negro oscuro */
            font-size: 2.5em; /* Tamaño grande para el título */
            font-weight: 700; /* Negrita */
            text-align: center;
            margin-bottom: 20px; /* Espaciado inferior */
        }

        /* Subtítulo ajustado */
        h2 {
            color: #ff7f50 !important; /* Color coral más visible */
            font-size: 1.5em; /* Tamaño mayor para el subtítulo */
            font-weight: 400;
            text-align: center;
            margin-top: 0; /* Quitar margen superior */
            margin-bottom: 30px; /* Aumentar espaciado inferior */
        }

        /* Texto descriptivo */
        p {
            font-size: 1.2em; /* Tamaño del texto para instrucciones */
            color: #333333; /* Gris oscuro */
            text-align: center;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto 40px; /* Centrado y con espaciado inferior */
        }

        /* Botón de CTA (Call to Action) */
        .stButton button {
            background-color: #3366FF; /* Botón azul fuerte */
            color: #FFFFFF !important; /* Texto blanco */
            font-size: 1.5em; /* Texto grande */
            padding: 15px 30px; /* Botón grande */
            border-radius: 5px; /* Bordes redondeados */
            border: none; /* Sin borde */
            transition: background-color 0.3s ease; /* Animación suave */
        }

        /* Hover en el botón */
        .stButton button:hover {
            background-color: #2850b8; /* Botón más oscuro al pasar el mouse */
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

        </style>
        """,
        unsafe_allow_html=True
    )

    # Contenido principal centrado y con más espacio
    st.markdown("<div class='container'>", unsafe_allow_html=True)

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
        <p>
            ¡Gracias por adquirir nuestro <strong>Test de Exploración de Carreras</strong>! 
            Este test está diseñado para ayudarte a identificar tus intereses y habilidades, 
            guiándote hacia las carreras que más se ajustan a tu perfil.
            A continuación, haz clic en el botón para empezar tu test y descubrir las mejores opciones de carrera para ti.
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
        st.title("¡Resultados del Test!")
        st.write("**Nombre del usuario**: Juan Pérez")
        
        # Resumen general
        st.subheader("Resumen General")
        st.write("Crecimiento proyectado de tu industria: **75%**")
        st.write("Crecimiento proyectado de profesionales en tu industria: **82%**")
        st.write("Demanda laboral actual: **54%**")
        st.write("Nivel de automatización en tu industria: **99%**")
        st.write("Nivel de avance tecnológico en tu industria: **14%**")

        # Detalles por áreas
        st.subheader("Detalles por áreas")

        st.write("**Crecimiento Profesional**")
        st.write("Crecimiento proyectado: **82%**")
        st.write("Comparativa: Tu proyección está por encima del promedio del sector en tu país, que es del 70%.")
        st.write("Recomendación: Con esta alta proyección de crecimiento, te sugerimos centrarte en el desarrollo de habilidades tecnológicas avanzadas para mantenerte competitivo en un entorno de alta automatización.")

        st.write("**Demanda Laboral**")
        st.write("Demanda actual: **54%**")
        st.write("Comparativa: La demanda en tu industria está en un nivel promedio. Esto significa que hay oportunidades, pero es importante diferenciarse de la competencia.")
        st.write("Recomendación: Refuerza tus habilidades técnicas a través de certificaciones o especializaciones para aumentar tu atractivo ante posibles empleadores.")

        st.write("**Tasa de Automatización**")
        st.write("Tasa de automatización: **99%**")
        st.write("Comentario: La automatización es extremadamente alta en tu sector. Esto sugiere que las tareas rutinarias están siendo reemplazadas por tecnologías.")
        st.write("Recomendación: Enfócate en desarrollar habilidades que complementen las tecnologías, como la creatividad, el liderazgo y la gestión de proyectos tecnológicos.")

        st.write("**Tasa de Avance Tecnológico**")
        st.write("Tasa de avance tecnológico: **14%**")
        st.write("Comentario: Aunque tu industria tiene un alto nivel de automatización, el avance tecnológico está todavía en etapas tempranas.")
        st.write("Recomendación: Aprovecha este periodo para convertirte en un líder en la adopción de nuevas tecnologías, buscando formación en áreas emergentes como inteligencia artificial o blockchain.")

        # Comparativa de Crecimiento por Industria
        st.subheader("Comparativa de Crecimiento por Industria")
        st.write("A continuación te mostramos cómo te comparas con otros profesionales en tu industria en relación con el crecimiento laboral proyectado:")

        # Botón para ver recomendaciones personalizadas
        if st.button("Ver recomendaciones personalizadas"):
            st.subheader("Recomendaciones Personalizadas")
            st.write("""
            - **Desarrollo de Habilidades Avanzadas**: Te sugerimos inscribirte en nuestro curso de "Gestión de Proyectos Tecnológicos" para mejorar tu perfil ante los empleadores y aprovechar el alto crecimiento proyectado.
            - **Aprovechar la Automatización**: Con el alto nivel de automatización en tu industria, es recomendable que desarrolles habilidades de programación y análisis de datos para trabajar junto con las tecnologías emergentes.
            - **Networking**: Aprovecha el crecimiento moderado en demanda laboral para ampliar tu red de contactos en la industria. Participa en conferencias o eventos relacionados con el desarrollo tecnológico y automatización.
            """)

        # Botón para volver al inicio
        if st.button("Volver al inicio"):
            st.session_state.step = 0  # Volver a la pantalla de bienvenida

    # Cerrar contenedor
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
