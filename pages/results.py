import streamlit as st
from utils.graphics import generate_plotly_chart

def show_results_page():
    st.markdown("<h1>Resultados del Test</h1>", unsafe_allow_html=True)

    # Datos de ejemplo
    data = {
        "Crecimiento proyectado": 75,
        "Demanda laboral": 54,
        "Automatización": 99,
        "Avance tecnológico": 14
    }

    # Usar columnas para mostrar gráficos y resultados
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Resumen General")
        st.write(f"Crecimiento proyectado de tu industria: **75%**")
        st.write(f"Demanda laboral actual: **54%**")
        st.write(f"Nivel de automatización: **99%**")
        st.write(f"Nivel de avance tecnológico: **14%**")

    with col2:
        st.markdown("<div class='plot-container'>", unsafe_allow_html=True)
        fig = generate_plotly_chart(data)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Botón para generar estadísticas
    if st.button("Generar Estadísticas"):
        st.write("Generando estadísticas...")

    # Botón para regresar al inicio
    if st.button("Volver al Inicio"):
        st.session_state.step = 0
