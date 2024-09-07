import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos desde GitHub (asegúrate de que el archivo esté correctamente en el repo)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/TuNombreDeUsuarioGitHub/streamlit-app/main/test_industria_con_nombres.csv"
    return pd.read_csv(url)

df_test = load_data()

# Seleccionar el nombre del estudiante para mostrar resultados
st.title("Recomendador de Carrera - Resultados del Test")
nombre_seleccionado = st.selectbox("Selecciona un estudiante", df_test['Nombre'])

# Filtrar los datos para el estudiante seleccionado
datos_estudiante = df_test[df_test['Nombre'] == nombre_seleccionado]

# Mostrar los datos principales del estudiante
st.subheader(f"Datos del estudiante: {nombre_seleccionado}")
st.write(datos_estudiante[['Edad', 'Sexo', 'Carrera 1 (más alta)']])

# Gráfico de barras para mostrar los intereses del estudiante
areas_interes = ['Técnico-manual', 'Científico-investigador', 'Artístico-creativo',
                 'Social-asistencial', 'Empresarial-persuasivo', 'Oficinista-administrativo', 'Cibertalentos']

st.subheader("Áreas de Interés")
puntajes_interes = datos_estudiante[areas_interes].mean()

plt.figure(figsize=(10, 5))
sns.barplot(x=puntajes_interes.index, y=puntajes_interes.values, palette='coolwarm')
plt.title(f"Áreas de Interés de {nombre_seleccionado}")
plt.ylabel('Puntaje')
plt.xticks(rotation=45)
st.pyplot(plt)

# Mostrar la carrera recomendada con los datos de la industria
st.subheader("Carrera Recomendada y Datos de la Industria")
carrera_recomendada = datos_estudiante['Carrera 1 (más alta)'].values[0]
st.write(f"Carrera recomendada: **{carrera_recomendada}**")

# Simular datos de la industria para la carrera recomendada
datos_industria = {
    'Carrera': ['Tecnología y Desarrollo de Software', 'Creatividad y Medios Digitales'],
    'Proyección de crecimiento profesionales': [11, 9],
    'Salario promedio (USD)': [116200, 97000],
    'Tasa de graduación (%)': [85, 78]
}

df_industria = pd.DataFrame(datos_industria)
datos_industria_carrera = df_industria[df_industria['Carrera'] == carrera_recomendada]

if not datos_industria_carrera.empty:
    st.write("Datos de la industria para la carrera recomendada:")
    st.write(datos_industria_carrera)
    
    # Gráfico para visualizar los datos de la industria
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    sns.barplot(x='Carrera', y='Proyección de crecimiento profesionales', data=datos_industria_carrera, ax=ax[0])
    ax[0].set_title("Proyección de Crecimiento (%)")

    sns.barplot(x='Carrera', y='Salario promedio (USD)', data=datos_industria_carrera, ax=ax[1])
    ax[1].set_title("Salario Promedio")

    st.pyplot(fig)
else:
    st.write("No se encontraron datos de la industria para esta carrera.")
