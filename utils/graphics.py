import plotly.graph_objects as go

def generate_plotly_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    fig = go.Figure([go.Bar(x=labels, y=values, marker_color='#467BE9')])
    fig.update_layout(
        title="Indicadores de la Industria",
        xaxis_title="Aspectos",
        yaxis_title="Porcentaje",
        plot_bgcolor="#FDE192",  # Fondo amarillo suave
        font=dict(color="#000000")  # Texto en negro
    )
    return fig
