import streamlit as st
from pages import test, results

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
        
        /* Estilo para los títulos */
        h1, h2 {
            color: #467BE9 !important; /* Azul Scholarshine */
            font-weight: bold;
        }

        /* Estilo para los subtítulos */
        h3 {
            color: #FF5A72 !important; /* Rosa Pink Future */
        }

        /* Estilo para el texto general */
        p, label {
            color: #000000 !important; /* Texto en negro */
        }

        /* Estilo para los botones */
        .stButton button {
            background-color: #FF5A72; /* Fondo Rosa Pink Future */
            color: white;
            border-radius: 10px;
            font-weight: bold;
        }

        /* Barra de progreso */
        .stProgress .css-1f7rzyt {
            background-color: #467BE9 !important; /* Azul Scholarshine */
        }

        /* Fondo para los gráficos */
        .plot-container {
            background-color: #FDE192; /* Fondo Amarillo Shine */
            padding: 10px;
            border-radius: 10px;
        }

        </style>
    """, unsafe_allow_html=True)

    # Crear navegación entre páginas
    pages = {
        "Test de Exploración": test.show_test_page,
        "Resultados": results.show_results_page
    }

    # Menú de navegación
    st.sidebar.title("Navega por la app")
    page = st.sidebar.selectbox("Selecciona una página", list(pages.keys()))

    # Mostrar la página seleccionada
    pages[page]()

if __name__ == "__main__":
    main()
