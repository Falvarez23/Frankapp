import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos del test y la industria
df_test = pd.read_csv('test_industria_con_nombres.csv')  # Asegúrate de usar la ruta correcta
df_industry = pd.read_csv('datos_industria.csv')  # Ruta de los datos de la industria

# Interfaz de usuario
st.title("Recomendador de Carrera - Resultados del Test")

# Selección del estudiante
nombre_estudiante = st.selectbox('Selecciona un estudiante', df_test['Nombre'])

# Obtener datos del estudiante seleccionado
datos_estudiante = df_test[df_test['Nombre'] == nombre_estudiante]

# Mostrar los datos del estudiante
st.subheader(f"Datos del estudiante: {nombre_estudiante}")
st.write(datos_estudiante)

# Mostrar las áreas de interés
areas_interes = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo', 
                 'Social-asistencial', 'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']

# Gráfica de las áreas de interés
puntajes_interes = datos_estudiante[areas_interes].T  # Transponer para graficar
st.subheader("Áreas de Interés")
st.bar_chart(puntajes_interes)

# Carrera recomendada
st.subheader("Carrera recomendada y datos de la industria")
carrera_recomendada = datos_estudiante['Carrera 1 (más alta)'].values[0]
st.write(f"Carrera recomendada: {carrera_recomendada}")

# Obtener los datos de la industria para la carrera recomendada
datos_industria = df_industry[df_industry['Carrera'] == carrera_recomendada]

st.write("Datos de la industria para la carrera recomendada:")
st.write(datos_industria)

# Visualizar el crecimiento proyectado y el valor de la industria
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='Carrera', y='Proyección de crecimiento profesionales', data=datos_industria, ax=ax)
plt.title('Proyección de Crecimiento de Profesionales en la Industria')
plt.xticks(rotation=45)
st.pyplot(fig)

# Visualizar el valor de la industria
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='Carrera', y='Valor de la industria Global', data=datos_industria, ax=ax)
plt.title('Valor Global de la Industria')
plt.xticks(rotation=45)
st.pyplot(fig)

# Mostrar el perfil completo del estudiante con la recomendación
st.subheader("Recomendación Final")
st.write(f"Basado en los intereses y habilidades, se recomienda la carrera de {carrera_recomendada}.\n"
         f"Esta carrera tiene una proyección de crecimiento del {datos_industria['Proyección de crecimiento profesionales'].values[0]}% y "
         f"un valor estimado de la industria de {datos_industria['Valor de la industria Global'].values[0]}.")
