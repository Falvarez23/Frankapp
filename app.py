import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Análisis de Evaluación Profesional')

# Cargar el archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Mostrar los primeros datos del archivo
    st.write("Primeros datos del archivo:")
    st.write(data.head())

    # Intereses profesionales por persona (análisis individual)
    if st.checkbox("Mostrar informe de una persona aleatoria"):
        random_person = data.sample(1).iloc[0]
        
        nombre = random_person['Nombre']
        edad = random_person['Edad']
        genero = 'Masculino' if random_person['Sexo'] == 'M' else 'Femenino'

        st.subheader(f"Informe para: {nombre}")
        st.write(f"**Edad**: {edad} años")
        st.write(f"**Género**: {genero}")

        # Intereses de la persona
        st.subheader("Intereses Profesionales")
        interest_columns = [
            'Técnico-manual (Interés)', 
            'Científico-investigador (Interés)', 
            'Artístico-creativo (Interés)', 
            'Social-asistencial (Interés)', 
            'Empresarial-persuasivo (Interés)', 
            'Oficinista-administrativo (Interés)', 
            'Cibertalentos (Interés)'
        ]
        intereses = random_person[interest_columns]

        for col in interest_columns:
            st.write(f"{col}: {intereses[col]}")

        # Recomendaciones basadas en los intereses
        st.subheader("Recomendaciones basadas en los intereses:")
        st.write("1. **Técnico-manual**: Carreras relacionadas con la ingeniería o trabajos técnicos especializados.")
        st.write("2. **Científico-investigador**: Investiga carreras en ciencia y tecnología.")
        st.write("3. **Artístico-creativo**: Explora profesiones en diseño o producción creativa.")
        st.write("4. **Social-asistencial**: Considera trabajos en asistencia social o psicología.")

    # Métricas de las industrias (gráficos generales)
    st.header("Análisis de las Industrias")

    # Métricas industriales generales
    if st.checkbox("Mostrar distribución salarial por industria"):
        st.subheader("Distribución de Salarios por Industria")
        salary_columns = ['Salario_Junior', 'Salario_Intermedio', 'Salario_Senior']
        
        fig, ax = plt.subplots()
        data[salary_columns].mean().plot(kind='bar', ax=ax)
        ax.set_title('Distribución de Salarios Promedio por Industria')
        ax.set_ylabel('Salario Promedio ($)')
        st.pyplot(fig)

    if st.checkbox("Mostrar tasa de rotación laboral por industria"):
        st.subheader("Tasa de Rotación Laboral por Industria")
        fig, ax = plt.subplots()
        data['Tasa_Rotacion_Laboral'] = data['Tasa_Rotacion_Laboral'].str.rstrip('%').astype('float') / 100.0
        data.groupby('Nombre')['Tasa_Rotacion_Laboral'].mean().plot(kind='bar', ax=ax)
        ax.set_title('Tasa de Rotación Laboral Promedio por Industria')
        ax.set_ylabel('Tasa de Rotación (%)')
        st.pyplot(fig)

    if st.checkbox("Mostrar crecimiento de vacantes por industria"):
        st.subheader("Crecimiento de Vacantes por Industria")
        fig, ax = plt.subplots()
        data['Crecimiento_Vacantes'] = data['Crecimiento_Vacantes'].str.rstrip('%').astype('float') / 100.0
        data.groupby('Nombre')['Crecimiento_Vacantes'].mean().plot(kind='bar', ax=ax)
        ax.set_title('Crecimiento de Vacantes Promedio por Industria')
        ax.set_ylabel('Crecimiento de Vacantes (%)')
        st.pyplot(fig)

    if st.checkbox("Mostrar tasa de automatización por industria"):
        st.subheader("Tasa de Automatización por Industria")
        fig, ax = plt.subplots()
        data['Tasa_Automatizacion'] = data['Tasa_Automatizacion'].str.rstrip('%').astype('float') / 100.0
        data.groupby('Nombre')['Tasa_Automatizacion'].mean().plot(kind='bar', ax=ax)
        ax.set_title('Tasa de Automatización Promedio por Industria')
        ax.set_ylabel('Tasa de Automatización (%)')
        st.pyplot(fig)

else:
    st.write("Por favor, sube un archivo CSV para continuar.")
