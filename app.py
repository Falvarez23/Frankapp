import streamlit as st
import matplotlib.pyplot as plt

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Definir la paleta de colores directamente en el código (sin CSS)
    color_azul = "#1E90FF"
    color_verde = "#32CD32"
    color_rojo = "#FF4500"
    color_fondo = "#F0F0F0"

    # Función para generar gráficos
    def generar_grafico(titulo, datos, etiquetas, color_barra):
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.bar(etiquetas, datos, color=color_barra)
        ax.set_title(titulo, fontsize=14)
        ax.set_ylabel("Porcentaje")
        return fig

    # Datos de ejemplo
    datos_crecimiento = [75, 82, 54, 99, 14]
    etiquetas_crecimiento = ["Crec. Industria", "Crec. Profesionales", "Demanda", "Automatización", "Tecnología"]

    # Estado inicial
    if 'step' not in st.session_state:
        st.session_state.step = 0

    # Pantalla inicial (bienvenida)
    if st.session_state.step == 0:
        st.markdown(f"<h1 style='color:{color_azul}; text-align:center;'>¡Gracias por tu compra!</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color:{color_azul}; text-align:center;'>Test de Exploración de Carreras Adquirido</h2>", unsafe_allow_html=True)
        st.write("Este test está diseñado para ayudarte a identificar tus intereses y habilidades.")
        if st.button("Comenzar Test", key="start_test"):
            st.session_state.step = 1

    # Preguntas del test
    elif st.session_state.step > 0 and st.session_state.step <= len(datos_crecimiento):
        st.markdown(f"<h2 style='color:{color_azul};'>Test de Exploración de Carreras</h2>", unsafe_allow_html=True)
        progress = (st.session_state.step - 1) / len(datos_crecimiento)
        st.progress(progress)
        
        question_idx = st.session_state.step - 1
        st.write(f"Pregunta {st.session_state.step} de {len(datos_crecimiento)}")
        st.write("Elige tu respuesta:")
        options = ["Bajo interés", "Interés moderado", "Alto interés"]
        response = st.radio("Selecciona una opción:", options, key=f"response_{question_idx}")

        if st.button("Siguiente", key=f"next_{question_idx}"):
            st.session_state.step += 1

    # Pantalla de resultados
    else:
        st.markdown(f"<h1 style='color:{color_azul};'>¡Resultados del Test!</h1>", unsafe_allow_html=True)
        st.write("Estos son tus resultados:")

        # Mostrar resultados y gráficos
        col1, col2 = st.columns([1, 1])

        # Mostrar resultados a la izquierda
        with col1:
            st.subheader("Resumen General")
            st.write(f"Crecimiento proyectado de tu industria: **75%**")
            st.write(f"Crecimiento proyectado de profesionales: **82%**")
            st.write(f"Demanda laboral actual: **54%**")
            st.write(f"Nivel de automatización: **99%**")
            st.write(f"Nivel de avance tecnológico: **14%**")

        # Mostrar gráfico a la derecha
        with col2:
            fig = generar_grafico("Indicadores de la Industria", datos_crecimiento, etiquetas_crecimiento, color_azul)
            st.pyplot(fig)

        # Segunda fila para mostrar otros detalles y gráficos
        col3, col4 = st.columns([1, 1])

        with col3:
            st.subheader("Crecimiento Profesional")
            st.write("Tu proyección está por encima del promedio del sector en tu país (70%).")

        with col4:
            # Gráfico comparativo
            fig2 = generar_grafico("Automatización vs Tecnología", [99, 14], ["Automatización", "Tecnología"], color_verde)
            st.pyplot(fig2)

        # Botón para reiniciar
        if st.button("Volver al inicio", key="restart"):
            st.session_state.step = 0

if __name__ == "__main__":
    main()
