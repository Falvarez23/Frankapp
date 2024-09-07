import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos del archivo CSV
df_test = pd.read_csv('test_industria_con_nombres.csv')

# Mostrar los primeros registros del archivo para referencia
st.markdown("<h3 style='color: green;'>Datos del archivo (test_industria_con_nombres.csv):</h3>", unsafe_allow_html=True)
st.dataframe(df_test.head())

# Selección de carrera recomendada
carrera_recomendada = df_test['Carrera 1 (más alta)'].iloc[0]
st.markdown(f"<h3 style='color: red;'>Carrera recomendada: {carrera_recomendada}</h3>", unsafe_allow_html=True)

# Filtrar los datos de la industria según la carrera recomendada
datos_industria = df_test[df_test['Carrera 1 (más alta)'] == carrera_recomendada]

# Verificar si las columnas existen y no tienen valores nulos
if 'Proyección de crecimiento profesionales' in datos_industria.columns and datos_industria['Proyección de crecimiento profesionales'].notnull().all():
    # Gráfico de crecimiento de la industria
    st.markdown("<h4 style='color: orange;'>Proyección de Crecimiento (%)</h4>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.barplot(x='Carrera 1 (más alta)', y='Proyección de crecimiento profesionales', data=datos_industria, ax=ax)
    ax.set_title('Proyección de Crecimiento de Profesionales por Carrera', fontsize=14)
    ax.set_xlabel('Carrera')
    ax.set_ylabel('Proyección de Crecimiento (%)')
    st.pyplot(fig)
else:
    st.error("Error: La columna 'Proyección de crecimiento profesionales' no contiene datos válidos.")

# Verificar si la columna de 'Valor de la industria Global' existe y no tiene valores nulos
if 'Valor de la industria Global' in datos_industria.columns and datos_industria['Valor de la industria Global'].notnull().all():
    # Gráfico de valor de la industria global
    st.markdown("<h4 style='color: teal;'>Valor de la Industria Global ($)</h4>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots()
    sns.barplot(x='Carrera 1 (más alta)', y='Valor de la industria Global', data=datos_industria, ax=ax2)
    ax2.set_title('Valor de la Industria Global', fontsize=14)
    ax2.set_xlabel('Carrera')
    ax2.set_ylabel('Valor en Miles de Millones')
    st.pyplot(fig2)
else:
    st.error("Error: La columna 'Valor de la industria Global' no contiene datos válidos.")

# Pie chart - Distribución de los campos en puntajes (Habilidades y Destrezas)
habilidades = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo', 'Social-asistencial', 
               'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']

# Verificar que las columnas de habilidades existan
if all(habilidad in df_test.columns for habilidad in habilidades):
    puntajes = [df_test[habilidad].mean() for habilidad in habilidades]

    st.markdown("<h4 style='color: brown;'>Distribución de Habilidades y Destrezas</h4>", unsafe_allow_html=True)
    fig3, ax3 = plt.subplots()
    ax3.pie(puntajes, labels=habilidades, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(habilidades)))
    ax3.axis('equal')  # Para que el gráfico sea un círculo perfecto
    st.pyplot(fig3)
else:
    st.error("Error: Algunas columnas de habilidades no están disponibles.")

# Footer
st.markdown("<h5 style='text-align: center; color: grey;'>Desarrollado por tu equipo</h5>", unsafe_allow_html=True)
