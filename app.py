import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo de datos
df = pd.read_csv('test_industria_con_nombres.csv')

# Mostrar los primeros datos
st.title("Recomendador de Carrera - Resultados del Test")
st.write("Datos del archivo (test_industria_con_nombres.csv):")
st.write(df.head())

# Seleccionar una carrera recomendada
st.subheader("Carrera recomendada y datos de la industria")
carrera_recomendada = df.iloc[0]['Carrera 1 (más alta)']
st.write(f"Carrera recomendada: {carrera_recomendada}")

# Filtrar los datos de la industria para esa carrera
datos_industria = df[df['Carrera 1 (más alta)'] == carrera_recomendada]
st.write("Datos de la industria para la carrera recomendada:")
st.write(datos_industria[['Proyeccion_Crecimiento_Industria', 'Valor_Industria_Global', 'Salario_Junior', 'Salario_Intermedio', 'Salario_Senior']])

# Gráfico de barras: Proyección de crecimiento de profesionales
st.subheader("Proyección de crecimiento de profesionales por carrera")
plt.figure(figsize=(10, 5))
sns.barplot(x='Carrera 1 (más alta)', y='Proyección de crecimiento profesionales', data=df)
plt.title('Proyección de Crecimiento Profesionales')
plt.xticks(rotation=45)
st.pyplot(plt)

# Gráfico de líneas: Comparación de salarios
st.subheader("Comparación de Salarios (Junior, Intermedio, Senior)")
plt.figure(figsize=(10, 5))
sns.lineplot(data=df[['Salario_Junior', 'Salario_Intermedio', 'Salario_Senior']])
plt.title('Evolución de los Salarios')
plt.xlabel('Tipo de Salario')
plt.ylabel('Valor en USD')
st.pyplot(plt)

# Gráfico de pastel: Distribución de industrias por países
st.subheader("Distribución de la industria por países")
plt.figure(figsize=(8, 8))
df['País'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3')
plt.title('Distribución de la Industria por Países')
st.pyplot(plt)
