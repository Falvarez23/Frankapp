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

    # Intereses profesionales por persona
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

        # Gráfico de intereses
        st.subheader("Distribución de Intereses")
        fig, ax = plt.subplots()
        intereses.plot(kind='bar', ax=ax)
        ax.set_ylabel('Puntuación de Interés')
        ax.set_title('Intereses Profesionales')
        st.pyplot(fig)

    # Métricas adicionales
    if st.checkbox("Mostrar distribución salarial"):
        st.subheader("Distribución de Salarios")
        salary_columns = ['Salario_Junior', 'Salario_Intermedio', 'Salario_Senior']
        
        fig, ax = plt.subplots()
        data[salary_columns].plot(kind='box', ax=ax)
        ax.set_title('Distribución de Salarios (Junior, Intermedio, Senior)')
        ax.set_ylabel('Salario ($)')
        st.pyplot(fig)

    if st.checkbox("Mostrar tasa de rotación laboral"):
        st.subheader("Tasa de Rotación Laboral")
        fig, ax = plt.subplots()
        data['Tasa_Rotacion_Laboral'] = data['Tasa_Rotacion_Laboral'].str.rstrip('%').astype('float') / 100.0
        data.plot(kind='bar', x='Nombre', y='Tasa_Rotacion_Laboral', ax=ax)
        ax.set_title('Tasa de Rotación Laboral por Persona')
        ax.set_ylabel('Tasa de Rotación (%)')
        st.pyplot(fig)

    if st.checkbox("Mostrar crecimiento de vacantes"):
        st.subheader("Crecimiento de Vacantes")
        fig, ax = plt.subplots()
        data['Crecimiento_Vacantes'] = data['Crecimiento_Vacantes'].str.rstrip('%').astype('float') / 100.0
        data.plot(kind='bar', x='Nombre', y='Crecimiento_Vacantes', ax=ax)
        ax.set_title('Crecimiento de Vacantes por Persona')
        ax.set_ylabel('Crecimiento de Vacantes (%)')
        st.pyplot(fig)

    if st.checkbox("Mostrar tasa de automatización"):
        st.subheader("Tasa de Automatización")
        fig, ax = plt.subplots()
        data['Tasa_Automatizacion'] = data['Tasa_Automatizacion'].str.rstrip('%').astype('float') / 100.0
        data.plot(kind='bar', x='Nombre', y='Tasa_Automatizacion', ax=ax)
        ax.set_title('Tasa de Automatización por Persona')
        ax.set_ylabel('Tasa de Automatización (%)')
        st.pyplot(fig)

else:
    st.write("Por favor, sube un archivo CSV para continuar.")

