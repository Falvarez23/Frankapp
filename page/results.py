import streamlit as st
from utils.graphics import generate_plotly_chart

def show_results_page():
    st.title("Resultados del Test")
    st.write("Resumen de tus respuestas")

    # Gráficos de resultados
    data = {
        "Crecimiento proyectado": 75,
        "Demanda laboral": 54,
        "Automatización": 99,
        "Avance tecnológico": 14
    }

    st.plotly_chart(generate_plotly_chart(data), use_container_width=True)
