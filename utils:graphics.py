import plotly.graph_objects as go

def generate_plotly_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    fig = go.Figure([go.Bar(x=labels, y=values, marker_color='lightskyblue')])
    fig.update_layout(
        title="Indicadores de la Industria",
        xaxis_title="Aspectos",
        yaxis_title="Porcentaje"
    )
    return fig
