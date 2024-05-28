import dash
import dash_bootstrap_components as dbc
import pandas as pd
from src.data_processing.utils import *

data = pd.read_csv(r"data/sao-paulo-properties-april-2019.csv")
df_data = preprocess_df(data)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.config["suppress_callback_exceptions"] = True
app.scripts.config.serve_locally = True
server = app.server
