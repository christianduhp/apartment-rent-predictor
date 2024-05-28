from dash import dcc, html
import dash_bootstrap_components as dbc

from app import *
from src.data_processing.utils import get_districts

controllers = dbc.Row(
    [
        html.Img(
            id="logo",
            src=app.get_asset_url("logo.png"),
            style={"width": "40%"},
        ),
        html.H3(
            "Previsão de Preços de Aluguel de Apartamentos",
            style={"margin-top": "30px"},
        ),
        html.P(
            """ Utilize a plataforma para praver com precisão o valor do aluguel de apartamentos na cidade de São Paulo com Machine Learning """
        ),
        html.H4(
            "Distrito",
            style={"margin-top": "50px", "margin-bottom": "25px"},
        ),
        dcc.Dropdown(
            id="district-dropdown",
            options=get_districts(df_data),
            value=0,
            placeholder="Selecione um distrito",
        ),
        html.H4(
            "Área (m²)",
            style={"margin-top": "50px", "margin-bottom": "25px"},
        ),
        dcc.Slider(id="slider-square-size", min=0, max=1000, value=0),
        html.H4(
            "Dormitórios",
            style={"margin-top": "50px", "margin-bottom": "25px"},
        ),
        dcc.Slider(id="slider-rooms", min=0, max=10, step=1),
        html.H4(
            "Banheiros",
            style={"margin-top": "50px", "margin-bottom": "25px"},
        ),
        dcc.Slider(id="slider-toilets", min=0, max=10, step=1),
        html.H4(
            "Suítes",
            style={"margin-top": "50px", "margin-bottom": "25px"},
        ),
        dcc.Slider(id="slider-suites", min=0, max=6, step=1, value=0),
        html.H4(
            "Vagas de Estacionamento",
            style={"margin-top": "50px", "margin-bottom": "25px"},
        ),
        dcc.Slider(id="slider-parking", min=0, max=5, step=1, value=0),
        html.H4(
            "Disposto a pagar por condomínio",
            style={"margin-top": "50px", "margin-bottom": "25px"},
        ),
        dcc.Slider(id="slider-condo", min=0, max=8000),
        html.H4("Elevador", style={"margin-top": "50px", "margin-bottom": "25px"}),
        dcc.Dropdown(
            id="option-elevator",
            options=[
                {"label": "Sim", "value": "1"},
                {"label": "Não", "value": "0"},
            ],
            value="1",
            clearable=False,
        ),
        html.H4("Mobiliado", style={"margin-top": "50px", "margin-bottom": "25px"}),
        dcc.Dropdown(
            id="option-furnished",
            options=[
                {"label": "Sim", "value": "1"},
                {"label": "Não", "value": "0"},
            ],
            value="1",
            clearable=False,
        ),
        html.H4("Piscina", style={"margin-top": "50px", "margin-bottom": "25px"}),
        dcc.Dropdown(
            id="option-swimming-pool",
            options=[
                {"label": "Sim", "value": "1"},
                {"label": "Não", "value": "0"},
            ],
            value="1",
            clearable=False,
        ),
    ],
    style={"justify-content": "center", "margin": "1em"},
)
