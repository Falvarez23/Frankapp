import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

# Cargar los datos del test
df_test = pd.read_csv('test_industria_con_nombres.csv')

# Crear gráfico de barras para las áreas de interés
areas_interes = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo', 
                 'Social-asistencial', 'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']
puntajes = df_test[areas_interes].mean()

st.markdown("<h3>Resultado del Test: Áreas de Interés</h3>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.barplot(x=areas_interes, y=puntajes, palette='Blues_d', ax=ax)
ax.set_title('Puntaje Promedio por Área de Interés')
ax.set_ylabel('Puntaje Promedio')
ax.set_xlabel('Áreas de Interés')
st.pyplot(fig)

st.markdown("<p>Este gráfico muestra las áreas de interés del estudiante según su test. Los puntajes reflejan las áreas donde el estudiante tiene mayor afinidad.</p>", unsafe_allow_html=True)


# Crear gráfico circular para las carreras recomendadas
carreras = ['Carrera 1 (más alta)', 'Carrera 2', 'Carrera 3']
puntajes_carreras = [df_test['Carrera 1 (más alta)'].count(), 
                     df_test['Carrera 2'].count(), 
                     df_test['Carrera 3'].count()]

st.markdown("<h3>Carreras Recomendadas</h3>", unsafe_allow_html=True)
fig2, ax2 = plt.subplots()
ax2.pie(puntajes_carreras, labels=carreras, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')  # Para que sea un círculo
st.pyplot(fig2)

st.markdown("<p>Las tres carreras recomendadas basadas en el perfil del estudiante se muestran en este gráfico circular.</p>", unsafe_allow_html=True)


# Datos de la industria para las 3 carreras
carreras_industria = ['Tecnología y Desarrollo de Software', 'Creatividad y Medios Digitales', 'Salud y Bienestar']
valores_industria = [116.2, 23.7, 20.4]  # Valores en miles de millones
proyeccion_crecimiento = [17.5, 13.2, 17.8]  # Proyecciones de crecimiento

st.markdown("<h3>Datos de la Industria para las Carreras Recomendadas</h3>", unsafe_allow_html=True)

# Gráfico 1: Proyección de crecimiento
fig3, ax3 = plt.subplots()
sns.barplot(x=carreras_industria, y=proyeccion_crecimiento, palette='Greens', ax=ax3)
ax3.set_title('Proyección de Crecimiento de Profesionales (%)')
ax3.set_xlabel('Carrera')
ax3.set_ylabel('Proyección de Crecimiento (%)')
st.pyplot(fig3)

# Gráfico 2: Valor de la Industria Global
fig4, ax4 = plt.subplots()
sns.barplot(x=carreras_industria, y=valores_industria, palette='Oranges', ax=ax4)
ax4.set_title('Valor de la Industria Global (Miles de Millones $)')
ax4.set_xlabel('Carrera')
ax4.set_ylabel('Valor de la Industria (Miles de Millones)')
st.pyplot(fig4)

st.markdown("<p>Estos gráficos muestran cómo las carreras recomendadas se complementan con la proyección de crecimiento en sus respectivas industrias y su valor global.</p>", unsafe_allow_html=True)

# Crear un gráfico adicional para mostrar cómo los datos varían por país
st.markdown("<h3>Comparativa de Carreras por País</h3>", unsafe_allow_html=True)

paises = ['EEUU', 'España', 'México', 'Argentina', 'Colombia']
carreras_por_pais = [20, 15, 25, 18, 22]  # Números de profesionales por país (ejemplo)

fig5, ax5 = plt.subplots()
sns.barplot(x=paises, y=carreras_por_pais, palette='Purples', ax=ax5)
ax5.set_title('Cantidad de Profesionales por País en Carreras Recomendadas')
ax5.set_xlabel('País')
ax5.set_ylabel('Número de Profesionales')
st.pyplot(fig5)

st.markdown("<p>Este gráfico muestra cómo varía la disponibilidad de profesionales en las carreras recomendadas según el país, lo que puede influir en las oportunidades del estudiante.</p>", unsafe_allow_html=True)

