import dash_bootstrap_components as dbc
from dash import html
from app import app

info_prediction = dbc.Row(
    [
        html.Div(
            [],
            style={"margin-top": "2em"},
            id="info-prediction",
        )
    ]
)

# Seção de explicação sobre a previsão de preços
explanation_section = html.Div(
    [
        html.Div(
            [
                html.Img(
                    id="img-logo",
                    src=app.get_asset_url("logo.png"),
                    style={"width": "20%", "marginRight": "2em"},
                ),
                html.Div(
                    [
                        html.H3(
                            "Como Funciona a Previsão de Preços",
                            style={"textAlign": "center", "margin-bottom": "1em"},
                        ),
                        html.P(
                            "Nosso sistema utiliza um modelo sofisticado de aprendizado de máquina chamado RandomForestRegressor para oferecer estimativas precisas do preço de aluguel de apartamentos. Este modelo analisa uma variedade de características dos imóveis, incluindo tamanho, número de quartos, banheiros, presença de elevador, mobília e piscina, entre outros. Ao preencher esses detalhes específicos do apartamento, nosso sistema é capaz de calcular uma estimativa personalizada do preço de aluguel. O RandomForestRegressor é uma técnica avançada que lida com a complexidade dos dados por trás das cortinas, permitindo que você se concentre apenas na inserção das informações necessárias. Quanto mais informações você fornecer, mais precisa será a estimativa resultante, garantindo uma experiência personalizada e confiável. Então, sinta-se à vontade para preencher todos os detalhes disponíveis para obter a estimativa mais precisa possível.",
                            style={
                                "textAlign": "justify",
                                "lineHeight": "1.6",
                                "flex": "1",
                            },
                        ),
                    ]
                ),
            ],
            id="explanation_section",
            style={"display": "flex", "alignItems": "center"},
        ),
    ],
    style={
        "padding": "2em",
    },
)


def create_prediction_display(prediction):
    return html.Div(
        [
            html.H4(
                "Estimativa de Preço", style={"textAlign": "center", "color": "#085092"}
            ),
            html.P(
                prediction,
                style={"textAlign": "center", "fontSize": "24px"},
            ),
        ],
        style={"justify-content": "center"},
    )
