import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df_test = pd.read_csv('test_industria_con_nombres.csv')

# Mostrar los nombres de las columnas para verificar
st.write("Columnas en el archivo:", df_test.columns)

# Seleccionar un estudiante
if 'Nombre' in df_test.columns:
    estudiantes = df_test['Nombre'].unique()
    opcion_estudiante = st.selectbox('Selecciona un estudiante', estudiantes)
    
    # Filtrar datos del estudiante seleccionado
    datos_estudiante = df_test[df_test['Nombre'] == opcion_estudiante].iloc[0]
    
    # Mostrar los datos básicos del estudiante
    st.subheader(f"Datos del estudiante: {opcion_estudiante}")
    st.write(f"Edad: {datos_estudiante['Edad']}")
    st.write(f"Sexo: {datos_estudiante['Sexo']}")

    # Áreas de interés (asegúrate de que los nombres sean correctos)
    areas_interes = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo', 
                     'Social-asistencial', 'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']

    # Verificar si esas columnas están presentes
    for area in areas_interes:
        if area not in df_test.columns:
            st.write(f"Columna '{area}' no encontrada en el archivo CSV")
        else:
            # Mostrar los puntajes de las áreas de interés
            puntajes_interes = datos_estudiante[areas_interes].T  # Transpuesta para graficar
            puntajes_interes.columns = ['Puntaje']
            st.subheader("Áreas de Interés")
            st.bar_chart(puntajes_interes)

    # Mostrar la carrera recomendada
    if 'Carrera 1 (más alta)' in df_test.columns:
        st.subheader("Carrera recomendada y datos de la industria")
        st.write(f"Carrera recomendada: {datos_estudiante['Carrera 1 (más alta)']}")
        
        # Filtrar datos de la industria relacionados con la carrera recomendada
        df_industria = df_test[df_test['Carrera 1 (más alta)'] == datos_estudiante['Carrera 1 (más alta)']]
        
        # Graficar los datos de la industria relacionados con la carrera recomendada
        if not df_industria.empty:
            st.subheader("Datos de la industria para la carrera recomendada:")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x='Carrera 1 (más alta)', y='Proyección de crecimiento profesionales', data=df_industria, ax=ax)
            plt.title('Proyección de crecimiento de la carrera en la industria')
            st.pyplot(fig)
        else:
            st.write("No se encontraron datos de la industria para la carrera recomendada.")
    else:
        st.write("Columna 'Carrera 1 (más alta)' no encontrada en el archivo CSV.")
else:
    st.write("Columna 'Nombre' no encontrada en el archivo CSV.")
