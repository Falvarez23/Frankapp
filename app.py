import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Estilo CSS personalizado
    st.markdown("""
        <style>
        /* Fondo general de la página */
        .main {
            background-color: #F9F7F4; /* Blanco neutro */
        }
        
        /* Cambiar color del texto y asegurarse de que no sea blanco */
        h1, h2, h3, h4, p, label {
            color: #000000 !important; /* Negro forzado */
        }

        /* Estilo para los botones */
        .stButton button {
            background-color: #FF5A72; /* Rosa Pink Future */
            color: white;
            border-radius: 10px;
        }

        /* Barra de progreso */
        .stProgress .css-1f7rzyt {
            background-color: #467BE9 !important; /* Azul Scholarshine */
        }

        /* Fondo de los gráficos */
        .plot-container {
            background-color: #FDE192; /* Fondo amarillo suave */
            padding: 10px;
            border-radius: 10px;
        }

        </style>
    """, unsafe_allow_html=True)

    # Mostrar contenido de ejemplo
    st.markdown("<h1>Test de Exploración de Carreras</h1>", unsafe_allow_html=True)
    st.write("Este es un ejemplo de texto que debería aparecer en negro.")
    
    if st.button("Botón de prueba"):
        st.write("Botón presionado.")

if __name__ == "__main__":
    main()
