from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import os
import numpy as np

fig = go.Figure()
fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")

map = dbc.Row([dcc.Graph(id="map-graph", figure=fig)], style={"height": "85vh"})


def create_map_figure(df_data, df_intermediate):
    mean_lat_ = df_intermediate["Latitude"].median()
    mean_long_ = df_intermediate["Longitude"].median()
    
    px.set_mapbox_access_token(os.environ.get("DEFAULT_PUBLIC_TOKEN"))

    map_fig = px.scatter_mapbox(
        df_intermediate,
        lat="Latitude",
        lon="Longitude",
        color="Price",
        size="Size",
        size_max=20,
        zoom=10,
        opacity=0.4,
    )

    color_scale = create_color_scale(df_data)
    map_fig.update_coloraxes(colorscale=color_scale)

    map_fig.update_layout(
        mapbox=dict(center=go.layout.mapbox.Center(lat=mean_lat_, lon=mean_long_)),
        template="plotly_dark",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=go.layout.Margin(l=10, r=10, t=10, b=10),
    )

    return map_fig


# Função para criar a escala de cores
def create_color_scale(df_data):
    color_scale = px.colors.sequential.GnBu
    df_quantiles = (
        df_data["Price"].quantile(np.linspace(0, 1, len(color_scale))).to_frame()
    )
    df_quantiles = (
        round(
            (df_quantiles - df_quantiles.min())
            / (df_quantiles.max() - df_quantiles.min())
            * 10000
        )
        / 10000
    )
    df_quantiles.iloc[-1] = 1
    df_quantiles["colors"] = color_scale
    df_quantiles.set_index("Price", inplace=True)
    color_scale = [[i, j] for i, j in df_quantiles["colors"].items()]
    return color_scale
