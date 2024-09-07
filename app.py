import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title("Recomendador de Carrera - Resultados del Test")

# Cargar el archivo CSV
df = pd.read_csv('test_industria_con_nombres.csv')

# Mostrar una selección de estudiantes
nombre_seleccionado = st.selectbox('Selecciona un estudiante', df['Nombre'])

# Filtrar datos del estudiante seleccionado
datos_estudiante = df[df['Nombre'] == nombre_seleccionado]

# Mostrar los datos del estudiante
if not datos_estudiante.empty:
    st.subheader(f"Datos del estudiante: {nombre_seleccionado}")
    st.write(datos_estudiante)

    # Mostrar gráficamente las áreas de interés del estudiante
    areas_interes = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo',
                     'Social-asistencial', 'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']

    puntajes_interes = datos_estudiante[areas_interes].T  # Transpuesta para graficar
    puntajes_interes.columns = ['Puntaje']

    st.subheader("Áreas de Interés")
    st.bar_chart(puntajes_interes)

    # Mostrar la carrera recomendada
    carrera_recomendada = datos_estudiante['Carrera 1 (más alta)'].values[0]
    st.subheader(f"Carrera recomendada: {carrera_recomendada}")

    # Filtrar datos de la industria para la carrera recomendada
    datos_industria = df[df['Carrera 1 (más alta)'] == carrera_recomendada]

    if not datos_industria.empty:
        st.subheader(f"Datos de la industria para {carrera_recomendada}")
        st.write(datos_industria[['Valor de la industria Global', 'Proyección de crecimiento profesionales']])

        # Graficar la proyección de crecimiento y el valor de la industria
        fig, ax1 = plt.subplots(figsize=(8, 4))

        # Gráfico de barra para proyección de crecimiento
        sns.barplot(x=datos_industria['Carrera 1 (más alta)'], y=datos_industria['Proyección de crecimiento profesionales'], ax=ax1, color='lightblue')
        ax1.set_ylabel('Proyección de crecimiento (%)')

        # Gráfico de línea para valor de la industria
        ax2 = ax1.twinx()
        sns.lineplot(x=datos_industria['Carrera 1 (más alta)'], y=datos_industria['Valor de la industria Global'].str.replace('[\$,]', '', regex=True).astype(float), ax=ax2, color='orange')
        ax2.set_ylabel('Valor de la industria Global ($ billones)')

        plt.title(f"Proyección y Valor de la Industria para {carrera_recomendada}")
        st.pyplot(fig)

    else:
        st.error(f"No se encontraron datos de la industria para {carrera_recomendada}")

else:
    st.error(f"No se encontraron datos para {nombre_seleccionado}")
