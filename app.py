import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos del archivo CSV
df_test = pd.read_csv('test_industria_con_nombres.csv')

# Mostrar los nombres de las columnas para verificar
st.write("Columnas del DataFrame:")
st.write(df_test.columns)

# Selección del estudiante
nombre_seleccionado = st.selectbox('Selecciona un estudiante', df_test['Nombre'])

# Filtrar los datos del estudiante seleccionado
datos_estudiante = df_test[df_test['Nombre'] == nombre_seleccionado]

# Verificar si hay datos para el estudiante seleccionado
if not datos_estudiante.empty:
    st.write(f"Datos del estudiante: {nombre_seleccionado}")

    # Definir las columnas de interés (asegúrate de que estas columnas existan en el CSV)
    areas_interes = [
        'Técnico-manual', 
        'Científico-investigador', 
        'Artístico-creativo', 
        'Social-asistencial', 
        'Empresarial-persuasivo', 
        'Oficinista-administrativo', 
        'Cibertalentos'
    ]

    # Verificar si las columnas existen en los datos
    if all(col in df_test.columns for col in areas_interes):
        # Calcular los puntajes promedio de las áreas de interés
        puntajes_interes = datos_estudiante[areas_interes].mean()

        # Mostrar los puntajes de las áreas de interés
        st.write("Áreas de Interés y Puntajes:")
        st.write(puntajes_interes)

        # Crear un gráfico de barras con los puntajes
        plt.figure(figsize=(10, 5))
        sns.barplot(x=puntajes_interes.index, y=puntajes_interes.values, palette='coolwarm')
        plt.title(f"Áreas de Interés de {nombre_seleccionado}")
        plt.ylabel('Puntaje')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    else:
        st.error("Las columnas de áreas de interés no existen en el archivo CSV.")
else:
    st.error("No se encontraron datos para el estudiante seleccionado.")

# Datos de la industria para la carrera recomendada
if 'Carrera 1 (más alta)' in df_test.columns:
    carrera_recomendada = datos_estudiante['Carrera 1 (más alta)'].values[0]
    st.write(f"Carrera recomendada: {carrera_recomendada}")

    # Filtrar los datos de la industria para la carrera recomendada
    datos_industria = df_test[df_test['Carrera 1 (más alta)'] == carrera_recomendada]

    if not datos_industria.empty:
        st.write(f"Datos de la industria para la carrera recomendada ({carrera_recomendada}):")
        st.write(datos_industria[['Proyección de crecimiento profesionales', 'Valor de la industria Global']])

        # Crear gráfico de proyección de crecimiento
        plt.figure(figsize=(10, 5))
        sns.barplot(x='Carrera 1 (más alta)', y='Proyección de crecimiento profesionales', data=datos_industria, palette='coolwarm')
        plt.title(f"Proyección de crecimiento profesionales para {carrera_recomendada}")
        plt.ylabel('Proyección de crecimiento (%)')
        st.pyplot(plt)
    else:
        st.error("No se encontraron datos de la industria para la carrera recomendada.")
else:
    st.error("La columna 'Carrera 1 (más alta)' no existe en el archivo CSV.")
