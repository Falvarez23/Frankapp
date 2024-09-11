import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np  # Asegúrate de importar numpy
from datetime import datetime
import plotly.io as pio
import io

# Configuración de la página
st.set_page_config(page_title="Generador de Gráficos Personalizado", layout="wide")

# Función para convertir HEX a RGBA con transparencia
def hex_to_rgba(hex_color, alpha=1.0):
    hex_color = hex_color.lstrip('#')
    return f'rgba({int(hex_color[0:2], 16)},{int(hex_color[2:4], 16)},{int(hex_color[4:6], 16)},{alpha})'

# Colores predefinidos
predefined_colors = [
    "#FF5C5C", "#5CCFFF", "#FFA500", "#90EE90", "#9370DB", "#FFD700"
]

# Lista de fuentes más utilizadas
font_options = [
    "Times New Roman", "Arial", "Helvetica", "Calibri", "Verdana", 
    "Tahoma", "Georgia", "Garamond", "Courier New", "Brush Script MT"
]

# Sidebar para la configuración del gráfico
st.sidebar.header("Configuración del Gráfico")

# Título del gráfico
chart_title = st.sidebar.text_input("Título del Gráfico", "Generador de Gráfico")

# Tipo de gráfico
chart_type = st.sidebar.selectbox("Tipo de Gráfico", ["Línea", "Área", "Dispersión", "Barras", "Donut"])

# Ingresar valores para los ejes
x_values = st.sidebar.text_area("Valores para X (separados por comas)", "2013,2014,2015,2016,2017,2018")
x = x_values.split(",")

# Selector de número de variables Y
num_y_vars = st.sidebar.number_input("Número de variables Y", min_value=1, max_value=100, value=1, step=1, key="num_y_vars")
y_values_list = []
y_names_list = []
for i in range(num_y_vars):
    if f"y_values_{i}" not in st.session_state:
        st.session_state[f"y_values_{i}"] = ','.join([str(np.random.randint(1, 25)) for _ in x])
    y_values = st.sidebar.text_area(f"Valores para Y-{i+1} (separados por comas)", st.session_state[f"y_values_{i}"], key=f"y_values_{i}")
    y_name = st.sidebar.text_input(f"Nombre de la Variable Y-{i+1}", f"Variable Y-{i+1}", key=f"y_name_{i}")
    y_values_list.append(y_values)
    y_names_list.append(y_name)

# Etiquetas personalizadas para los ejes
x_label = st.sidebar.text_input("Etiqueta para el eje X", "X")
y_label = st.sidebar.text_input("Etiqueta para el eje Y", "Y")

# Desplegable de opciones adicionales
with st.sidebar.expander("Opciones Adicionales"):
    graph_width = st.slider("Ancho del Gráfico", min_value=400, max_value=1200, value=1000, step=50)
    graph_height = st.slider("Alto del Gráfico", min_value=300, max_value=900, value=700, step=50)
    font_family = st.selectbox("Fuente del Gráfico", font_options, index=font_options.index("Times New Roman"))
    axis_font_size = st.slider("Tamaño de la Fuente de los Ejes", min_value=10, max_value=30, value=24, step=1)
    tick_font_size = st.slider("Tamaño de los Números de los Ejes", min_value=8, max_value=24, value=19, step=1)
    show_legend = st.checkbox("Mostrar Leyenda", value=True)
    
    # Configuración de la leyenda
    legend_font_family = st.selectbox("Fuente de la Leyenda", font_options, index=font_options.index("Arial"))
    legend_font_size = st.slider("Tamaño de la Fuente de la Leyenda", min_value=10, max_value=30, value=22, step=1)
    
    opacity = st.slider("Opacidad (%)", min_value=0, max_value=100, value=30, step=1) / 100
    border_width = st.slider("Grosor del Borde", min_value=0.0, max_value=3.0, value=1.5, step=0.1)
    border_opacity = st.slider("Opacidad del Borde (%)", min_value=0, max_value=100, value=60, step=1) / 100
    show_grid = st.checkbox("Activar rejilla", value=True)
    
    if chart_type == "Barras" and num_y_vars > 1:
        superposed_bars = st.checkbox("Superpuestas", value=True, key="superposed_bars")
    else:
        superposed_bars = False
    if chart_type == "Barras":
        horizontal_bars = st.checkbox("Invertidas", key="horizontal_bars")
    
    if chart_type == "Donut":
        hole_size = st.slider("Tamaño del agujero (%)", min_value=0, max_value=100, value=30, step=1) / 100
        show_values = st.checkbox("Mostrar valores en el gráfico", value=False)

# Opción para múltiples colores (siempre activada para Donut)
use_multiple_colors = st.sidebar.checkbox("Usar múltiples colores", value=True if chart_type == "Donut" or num_y_vars > 1 else False, key="use_multiple_colors")

# Seleccionar color(es) para el gráfico
selected_color = st.sidebar.color_picker("Color", "#24CBA0", key="single_color")

# Definir colores
if use_multiple_colors:
    num_colors = len(x)
    colors = [hex_to_rgba(st.sidebar.color_picker(f"Color {i+1}", predefined_colors[i % len(predefined_colors)], key=f"color_{i}"), alpha=opacity) for i in range(num_colors)]
else:
    color = hex_to_rgba(selected_color, alpha=opacity)
    colors = [color] * len(x)

# Procesar valores
y_values_lists = [[float(i) for i in y_values.split(",") if i.strip()] for y_values in y_values_list]

# Asegurar que todas las listas de Y tengan el mismo tamaño que X
for y_values in y_values_lists:
    while len(y_values) < len(x):
        y_values.append(0)
    while len(y_values) > len(x):
        y_values.pop()

# Crear un DataFrame
data = pd.DataFrame({"X": x})
for idx, y_set in enumerate(y_values_lists):
    data[y_names_list[idx]] = y_set

# Configuración común para todos los gráficos
common_layout = dict(
    xaxis_title=x_label,
    yaxis_title=y_label,
    plot_bgcolor="white",
    hovermode="x unified",
    width=graph_width,
    height=graph_height,
    margin=dict(l=80, r=40, t=100, b=60),  # Ajustar los márgenes para separar el texto de los ejes
    xaxis=dict(showgrid=show_grid, zeroline=True, gridcolor='rgba(211,211,211,0.5)', zerolinecolor='rgba(128,128,128,0.5)', autorange=True,
               tickfont=dict(size=tick_font_size), title_font=dict(size=axis_font_size)),
    yaxis=dict(showgrid=show_grid, zeroline=True, gridcolor='rgba(211,211,211,0.5)', zerolinecolor='rgba(128,128,128,0.5)', autorange=True,
               tickfont=dict(size=tick_font_size), title_font=dict(size=axis_font_size)),
    font=dict(family=font_family, size=axis_font_size, color="#374151"),
    showlegend=show_legend,
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02,
        font=dict(family=legend_font_family, size=legend_font_size)
    )
)

# Generar el gráfico basado en el tipo seleccionado
if chart_type == "Línea":
    fig = px.line(data, x="X", y=y_names_list, line_shape="spline")
    fig.update_traces(hovertemplate='<b>%{y}</b>', line=dict(width=border_width))  # Aplicar el grosor del borde a línea
    if use_multiple_colors:
        for i, name in enumerate(y_names_list):
            fig.update_traces(selector=dict(name=name), line_color=colors[i % len(colors)])
    else:
        fig.update_traces(line_color=color)

elif chart_type == "Área":
    fig = px.area(data, x="X", y=y_names_list, line_shape="spline")
    fig.update_traces(hovertemplate='<b>%{y}</b>', line=dict(width=border_width), fillcolor=color)
    if use_multiple_colors:
        for i, name in enumerate(y_names_list):
            fig.update_traces(selector=dict(name=name), line_color=colors[i % len(colors)], fillcolor=colors[i % len(colors)])
    else:
        fig.update_traces(line_color=color, fillcolor=color)

elif chart_type == "Dispersión":
    fig = px.scatter(data, x="X", y=y_names_list)
    fig.update_traces(hovertemplate='<b>%{y}</b>', marker=dict(size=10, line=dict(width=border_width, color=hex_to_rgba('#000000', border_opacity))))
    if use_multiple_colors:
        for i, name in enumerate(y_names_list):
            fig.update_traces(selector=dict(name=name), marker_color=colors[i % len(colors)], marker_line_color=colors[i % len(colors)])
    else:
        fig.update_traces(marker_color=color, marker_line_color=color)

elif chart_type == "Barras":
    if horizontal_bars:
        fig = px.bar(data, x=y_names_list, y="X", orientation='h', barmode='overlay' if superposed_bars else 'group')
    else:
        fig = px.bar(data, x="X", y=y_names_list, barmode='overlay' if superposed_bars else 'group')
    fig.update_traces(hovertemplate='<b>%{y}</b>', marker=dict(line=dict(width=border_width, color=hex_to_rgba('#000000', border_opacity))))
    if use_multiple_colors:
        for i, trace in enumerate(fig.data):
            trace.update(marker_color=colors[i % len(colors)])
    else:
        fig.update_traces(marker_color=color)
    fig.update_layout(bargap=0.2)

elif chart_type == "Donut":
    # Generar solo un gráfico Donut y asegurarse de que no haya duplicados
    fig = px.pie(data, values=y_values_lists[0], names="X", hole=hole_size, color_discrete_sequence=colors[:len(x)])
    
    if show_values:
        fig.update_traces(hovertemplate='<b>%{label}</b>: %{value} (%{percent})', textinfo='percent+label')
    else:
        fig.update_traces(hovertemplate='<b>%{label}</b>', textinfo='none')  # Ocultar valores y etiquetas

    fig.update_traces(marker=dict(colors=colors[:len(x)]))  # Aplicar múltiples colores

    fig.update_layout(
        title=dict(
            text=f"{chart_title}",
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(
                family=font_family,
                size=axis_font_size,
                color="#374151"
            )
        ),
        **common_layout
    )
    st.plotly_chart(fig)

# Añadir anotación para el título
if chart_type != "Donut":
    fig.update_layout(
        title=dict(
            text=f"{chart_title}",
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(
                family=font_family,
                size=axis_font_size,
                color="#374151"
        )
    ),
    legend_title_text=''  # Eliminar el texto del título de la leyenda
)

# Aplicar configuración común
fig.update_layout(**common_layout)

# Aplicar múltiples colores si se seleccionó la opción
if use_multiple_colors and chart_type != "Donut":
    for i, trace in enumerate(fig.data):
        trace.update(marker_color=colors[i % len(colors)])

# Mostrar el gráfico
st.plotly_chart(fig)

# Descargar gráfico con mayor resolución usando los valores personalizados
export_as_png = st.button("Descargar gráfico en alta calidad")

if export_as_png:
    img_bytes = pio.to_image(fig, format="png", width=graph_width, height=graph_height, scale=6)
    st.download_button(label="Descargar imagen", data=img_bytes, file_name="grafico_personalizado.png", mime="image/png")

# Forzar el autoescale
fig.update_layout(xaxis_autorange=True, yaxis_autorange=True)

# Información adicional
st.write("")
