import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# Título de la aplicación
st.title('Análisis de Evaluación Profesional')

# Cargar el archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Mostrar los primeros datos del archivo
    st.write("Primeros datos del archivo:")
    st.write(data.head())

    # Seleccionar una persona al azar
    if st.button("Seleccionar persona al azar para el análisis"):
        random_person = data.sample(1).iloc[0]
        
        # Obtener información de la persona
        nombre = random_person['Nombre']
        edad = random_person['Edad']
        genero = 'Masculino' if random_person['Sexo'] == 'M' else 'Femenino'

        # Mostrar la información de la persona
        st.subheader(f"Informe para: {nombre}")
        st.write(f"**Edad**: {edad} años")
        st.write(f"**Género**: {genero}")

        # Intereses
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

        # Mostrar los intereses
        for col in interest_columns:
            st.write(f"{col}: {intereses[col]}")

        # Recomendaciones
        st.subheader("Recomendaciones basadas en los intereses:")
        st.write("1. **Técnico-manual**: Carreras relacionadas con la ingeniería o trabajos técnicos especializados.")
        st.write("2. **Científico-investigador**: Investiga carreras en ciencia y tecnología.")
        st.write("3. **Artístico-creativo**: Explora profesiones en diseño o producción creativa.")
        st.write("4. **Social-asistencial**: Considera trabajos en asistencia social o psicología.")
        
        # Graficar los intereses
        st.subheader("Distribución de Intereses")
        fig, ax = plt.subplots()
        intereses.plot(kind='bar', ax=ax)
        ax.set_ylabel('Puntuación de Interés')
        ax.set_title('Intereses Profesionales')
        st.pyplot(fig)

else:
    st.write("Por favor, sube un archivo CSV para continuar.")
