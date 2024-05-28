from dash import Input, Output
import dash_bootstrap_components as dbc
from babel.numbers import format_currency
from dotenv import load_dotenv

# import from folders
from app import *
from src.components._map import *
from src.components._prediction import *
from src.components._controllers import *
from src.components._footer import *
from src.data_processing.utils import predict

load_dotenv()

# =========  Layout  =========== #
app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col([controllers], md=3),
                dbc.Col([info_prediction, map, explanation_section], md=9),
            ]
        ),
        dbc.Row(dbc.Col([footer], width={"size": 12}), className="mt-4"),
    ],
    fluid=True,
)


# ======= Callbacks ======== #
@app.callback(
    [Output("map-graph", "figure"), Output("info-prediction", "children")],
    [
        Input("district-dropdown", "value"),
        Input("slider-square-size", "value"),
        Input("slider-rooms", "value"),
        Input("slider-toilets", "value"),
        Input("slider-suites", "value"),
        Input("slider-parking", "value"),
        Input("slider-condo", "value"),
        Input("option-elevator", "value"),
        Input("option-furnished", "value"),
        Input("option-swimming-pool", "value"),
    ],
)
def filter_data_and_predict(
    district,
    square_size,
    rooms,
    toilets,
    suites,
    parking,
    condo,
    elevator,
    furnished,
    swimming_pool,
):

    if district is None:
        df_intermediate = df_data.copy()
        prediction = "Selecione um distrito para começar"
    else:
        df_intermediate = df_data[df_data["District"] == district]
        size_limit = (
            square_size
            if square_size > df_intermediate["Size"].min()
            else df_intermediate["Size"].max()
        )
        df_intermediate = df_intermediate[df_intermediate["Size"] <= size_limit]

        df_user_selected = pd.DataFrame(
            {
                "District": [district],
                "Size": [square_size],
                "Rooms": [rooms],
                "Toilets": [toilets],
                "Suites": [suites],
                "Parking": [parking],
                "Condo": [condo],
                "Elevator": [elevator],
                "Furnished": [furnished],
                "Swimming Pool": [swimming_pool],
            }
        )

        prediction = predict(df_data, df_user_selected)
        prediction = f"O valor estimado do aluguel é: {format_currency(prediction, 'BRL', locale='pt_BR')}"

    map_fig = create_map_figure(df_data, df_intermediate)

    prediction_display = create_prediction_display(prediction)
    return map_fig, prediction_display


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8080)
