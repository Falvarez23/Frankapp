import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título y subtítulos con estilo
st.markdown("<h1 style='text-align: center; color: blue;'>Recomendador de Carrera - Resultados del Test</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Carrera recomendada y datos de la industria</h2>", unsafe_allow_html=True)

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

# Mostrar los datos de la industria
st.markdown("<h4 style='color: purple;'>Datos de la industria para la carrera recomendada:</h4>", unsafe_allow_html=True)
st.dataframe(datos_industria)

# Crear gráficos de los datos de la industria
st.markdown("<h3 style='color: navy;'>Gráficos de la industria</h3>", unsafe_allow_html=True)

# Gráfico de crecimiento de la industria
st.markdown("<h4 style='color: orange;'>Proyección de Crecimiento (%)</h4>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.barplot(x='Carrera 1 (más alta)', y='Proyección de crecimiento profesionales', data=datos_industria, ax=ax)
ax.set_title('Proyección de Crecimiento de Profesionales por Carrera', fontsize=14)
ax.set_xlabel('Carrera')
ax.set_ylabel('Proyección de Crecimiento (%)')
st.pyplot(fig)

# Gráfico de valor de la industria global
st.markdown("<h4 style='color: teal;'>Valor de la Industria Global ($)</h4>", unsafe_allow_html=True)
fig2, ax2 = plt.subplots()
sns.barplot(x='Carrera 1 (más alta)', y='Valor de la industria Global', data=datos_industria, ax=ax2)
ax2.set_title('Valor de la Industria Global', fontsize=14)
ax2.set_xlabel('Carrera')
ax2.set_ylabel('Valor en Miles de Millones')
st.pyplot(fig2)

# Pie chart - Distribución de los campos en puntajes (Habilidades y Destrezas)
st.markdown("<h4 style='color: brown;'>Distribución de Habilidades y Destrezas</h4>", unsafe_allow_html=True)
habilidades = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo', 'Social-asistencial', 
               'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']
puntajes = [df_test[habilidad].mean() for habilidad in habilidades]

fig3, ax3 = plt.subplots()
ax3.pie(puntajes, labels=habilidades, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(habilidades)))
ax3.axis('equal')  # Para que el gráfico sea un círculo perfecto
st.pyplot(fig3)

# Footer
st.markdown("<h5 style='text-align: center; color: grey;'>Desarrollado por tu equipo</h5>", unsafe_allow_html=True)
