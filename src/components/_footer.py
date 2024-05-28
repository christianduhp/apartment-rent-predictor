import dash
import dash_bootstrap_components as dbc
from dash import html
import datetime

year = datetime.datetime.today().year

github = "https://github.com/christianduhp"
footer = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                html.P(
                    [
                        html.A(
                            f"{year} © Christian Oliveira",
                            href=github,
                            className="text-decoration-none text-white",
                        ),
                    ],
                    className="text-center",
                ),
                width={"size": 12},
            )
        ]
    ),
    className="mt-4",
    fluid=True,
    style={
        "width": "100%",
        "background-color": "#1E1E1E",
        "padding": "20px",
    },
)
