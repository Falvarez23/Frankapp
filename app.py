import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Aplicar estilo CSS para mejorar el diseño y darle un estilo de página web
    st.markdown(
        """
        <style>
        /* Fondo general */
        .main {
            background-color: #f1f5fd; /* Azul claro */
            font-family: 'Arial', sans-serif; /* Fuente clara y legible */
        }

        /* Título principal */
        h1 {
            color: #1F1F1F; /* Negro oscuro */
            font-size: 3em; /* Tamaño grande para el título */
            font-weight: 700; /* Negrita */
            text-align: center;
            margin-bottom: 0;
        }

        /* Subtítulo */
        h2 {
            color: #1F1F1F; /* Negro oscuro */
            font-size: 1.5em; /* Tamaño de subtítulo */
            font-weight: 500;
            text-align: center;
            margin-bottom: 20px;
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

        /* Imagen del producto */
        .product-image {
            text-align: center;
        }

        .product-image img {
            max-width: 400px;
            height: auto;
            margin-bottom: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Contenido de la página tipo web
    st.title("¡Gracias por tu compra!")
    st.subheader("Test de Exploración de Carreras Adquirido")

    # Imagen del producto (simulación)
    st.markdown('<div class="product-image"><img src="https://via.placeholder.com/400x300.png?text=Imagen+de+Test" alt="Test de Carreras"></div>', unsafe_allow_html=True)

    # Mensaje de bienvenida y explicativo
    st.markdown("""
    <p>
        ¡Gracias por adquirir nuestro <strong>Test de Exploración de Carreras</strong>! 
        Este test está diseñado para ayudarte a identificar tus intereses y habilidades, 
        guiándote hacia las carreras que más se ajustan a tu perfil.
        A continuación, haz clic en el botón para empezar tu test y descubrir las mejores opciones de carrera para ti.
    </p>
    """, unsafe_allow_html=True)

    # Botón grande de CTA (Call to Action) para comenzar el test
    if st.button("¡Comenzar Test!"):
        st.write("Aquí comenzarías el test... (esta función puede ser reemplazada por el formulario del test)")
        # Aquí podrías redirigir al formulario de test real o cargar el formulario si es parte de esta misma aplicación.
        # O cargar el formulario de preguntas que ya tienes en el código anterior.

if __name__ == "__main__":
    main()
