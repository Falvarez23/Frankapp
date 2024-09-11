import streamlit as st

def show_test_page():
    st.markdown(
        """
        <style>
        /* Estilo general para el texto */
        h1, h2, h3, h4, p, label {
            color: #000000 !important; /* Cambiar el color del texto a negro */
        }

        /* Forzar color negro en botones de texto */
        .stButton button {
            color: #FFFFFF !important; /* Cambia el color del texto en el botón */
            background-color: #FF5A72; /* Fondo rosa */
        }

        /* Si hay algún texto específico que sigue siendo blanco */
        .stMarkdown p {
            color: #000000 !important; /* Texto en negro */
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("<h1 style='color:#467BE9; text-align:center;'>Test de Exploración de Carreras</h1>", unsafe_allow_html=True)

    st.write("Este es un ejemplo de texto que debería aparecer en negro.")
    
    st.button("Botón de prueba")
