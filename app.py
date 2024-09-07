import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Recomendador de Carrera - Resultados del Test y Datos de la Industria")

# Leer el archivo test_industria_con_nombres.csv directamente
uploaded_file = st.file_uploader("Sube el archivo test_industria_con_nombres.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Mostrar los datos del archivo
    st.write("### Datos del archivo (test_industria_con_nombres.csv):")
    st.write(df)
    
    # Suponiendo que hay una columna 'Carrera 1 (más alta)' en el archivo
    st.subheader("Carrera recomendada y datos de la industria")
    
    carrera_recomendada = df['Carrera 1 (más alta)'].iloc[0]  # Tomamos la primera carrera recomendada
    st.write(f"Carrera recomendada: {carrera_recomendada}")
    
    # Filtrar los datos para la carrera recomendada
    datos_industria_carrera = df[df['Carrera 1 (más alta)'] == carrera_recomendada]
    
    if not datos_industria_carrera.empty:
        # Mostrar los datos filtrados
        st.write("Datos de la industria para la carrera recomendada:")
        st.write(datos_industria_carrera)

        # Gráfico de barras para comparar proyección de crecimiento y valor de la industria
        st.subheader("Comparación de Crecimiento y Valor de la Industria")
        fig, ax = plt.subplots()
        
        # Datos para el gráfico (proyección de crecimiento y valor de la industria)
        ax.bar(['Proyección de Crecimiento'], datos_industria_carrera['Proyección de crecimiento profesionales'].values, label='Proyección de Crecimiento (%)')
        ax.bar(['Valor de la Industria'], datos_industria_carrera['Valor de la industria Global'].values, label='Valor de la Industria (Billion USD)')
        
        ax.set_ylabel('Valores')
        ax.set_title(f"Datos de la Industria para {carrera_recomendada}")
        ax.legend()

        # Mostrar gráfico en Streamlit
        st.pyplot(fig)

        # Comparación de otras métricas, si es necesario
        st.subheader("Otras métricas relevantes:")
        st.write(f"Proyección de crecimiento de la industria: {datos_industria_carrera['Proyección de crecimiento profesionales'].values[0]}%")
        st.write(f"Valor global de la industria en 2026: ${datos_industria_carrera['Valor de la industria Global'].values[0]} billion")
    
    else:
        st.write("No se encontraron datos de la industria para la carrera recomendada.")
else:
    st.write("Por favor, sube el archivo test_industria_con_nombres.csv.")
