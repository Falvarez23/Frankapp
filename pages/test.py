import streamlit as st
from pages import test, results

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Crear navegación simple entre páginas
    pages = {
        "Test de Exploración": test.show_test_page,
        "Resultados": results.show_results_page
    }

    # Menú de navegación
    page = st.sidebar.selectbox("Navega por la app", list(pages.keys()))

    # Mostrar la página seleccionada
    pages[page]()

if __name__ == "__main__":
    main()
