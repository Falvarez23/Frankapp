import streamlit as st
import matplotlib.pyplot as plt

def main():
    # Configuración de la página
    st.set_page_config(page_title="Test de Exploración de Carreras", page_icon=":memo:", layout="centered")

    # Función para generar gráficos de ejemplo
    def generar_grafico(titulo, datos, etiquetas):
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.bar(etiquetas, datos, color='#1E90FF')
        ax.set_title(titulo, fontsize=14)
        ax.set_ylabel("Porcentaje")
        return fig

    # Preguntas del test
    questions = [
        "¿Te sientes atraído por el campo de la robótica y la automatización?",
        "¿Te atrae la idea de utilizar herramientas digitales para expresar tu creatividad?",
        # Añade más preguntas aquí...
    ]

    # Opciones de respuesta
    options = [
        "Bajo interés o potencial en la subárea.",
        "Interés o potencial moderado en la subárea.",
        "Alto interés o potencial en la subárea."
    ]

    # Estado inicial
    if 'step' not in st.session_state:
        st.session_state.step = 0

    # Pantalla inicial (bienvenida)
    if st.session_state.step == 0:
        st.title("¡Gracias por tu compra!")
        st.subheader("Test de Exploración de Carreras Adquirido")
        st.write("Este test está diseñado para ayudarte a identificar tus intereses y habilidades.")
        if st.button("Comenzar Test"):
            st.session_state.step = 1

    # Pantalla de preguntas
    elif st.session_state.step > 0 and st.session_state.step <= len(questions):
        question_idx = st.session_state.step - 1
        st.title(f"Pregunta {st.session_state.step} de {len(questions)}")
        st.write(questions[question_idx])
        response = st.radio("Elige tu respuesta:", options, key=f"response_{question_idx}")

        if st.button("Siguiente"):
            st.session_state.step += 1

    # Pantalla final con resultados y gráficos
    else:
        st.title("¡Resultados del Test!")
        st.write("Estos son tus resultados:")

        # Datos de ejemplo para gráficos
        datos_crecimiento = [75, 82, 54, 99, 14]
        etiquetas_crecimiento = ["Crec. Industria", "Crec. Profesionales", "Demanda", "Automatización", "Tecnología"]

        # Usamos columnas para colocar el gráfico y el texto uno junto al otro
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Resumen General")
            st.write("**Crecimiento proyectado de tu industria**: 75%")
            st.write("**Crecimiento proyectado de profesionales en tu industria**: 82%")
            st.write("**Demanda laboral actual**: 54%")
            st.write("**Nivel de automatización en tu industria**: 99%")
            st.write("**Nivel de avance tecnológico en tu industria**: 14%")

        with col2:
            # Generar gráfico de barras
            fig = generar_grafico("Indicadores de la Industria", datos_crecimiento, etiquetas_crecimiento)
            st.pyplot(fig)

        # Comparativa por áreas con gráfico
        st.subheader("Detalles por Áreas")
        st.write("**Crecimiento Profesional**")
        st.write("Tu proyección está por encima del promedio del sector en tu país, que es del 70%.")
        st.write("**Demanda Laboral**")
        st.write("La demanda en tu industria está en un nivel promedio.")

        # Añadir gráfico de crecimiento proyectado en otra columna
        col3, col4 = st.columns(2)

        with col3:
            st.write("**Tasa de Automatización**")
            st.write("La automatización es extremadamente alta en tu sector.")

        with col4:
            # Generar gráfico de barras
            fig2 = generar_grafico("Automatización vs Tecnología", [99, 14], ["Automatización", "Tecnología"])
            st.pyplot(fig2)

        # Botón para volver al inicio
        if st.button("Volver al inicio"):
            st.session_state.step = 0

if __name__ == "__main__":
    main()
