import pandas as pd
import pickle
from unidecode import unidecode

MODEL_FILE = "random_forest_regressor.pkl"

pd.set_option('future.no_silent_downcasting', True)

def get_districts(df_data):
    district = []
    for d in df_data["District"].unique():
        i = d.split("/São Paulo")
        district.append({"label": i[0], "value": d})

    # Ordena pelo label usando unidecode para normalização dos caracteres acentuados
    district_sorted = sorted(district, key=lambda x: unidecode(x["label"]))
    return district_sorted

def preprocess_df(df_data):
    df_filtered = df_data[df_data["Negotiation Type"] == "rent"].copy()
    df_filtered = df_filtered.drop(["New", "Negotiation Type", "Property Type"], axis=1)
    one_hot = pd.get_dummies(df_filtered["District"])
    df_filtered = df_filtered.join(one_hot)
    return df_filtered

def x_test_dataframe(df_data, user_data):
    user_data["Latitude"] = df_data[df_data["District"] == user_data["District"][0]]["Latitude"].median()
    user_data["Longitude"] = df_data[df_data["District"] == user_data["District"][0]]["Longitude"].median()

    df_schema = df_data.iloc[0:0]
    df_schema = df_schema.drop(["Price", "District"], axis=1)

    one_hot = pd.get_dummies(user_data["District"])
    df_dummie = user_data.drop(["District"], axis=1)
    df_dummie = df_dummie.join(one_hot)
    df_dummie = df_dummie.replace({False: 0, True: 1})

    x_test = pd.concat([df_schema, df_dummie])
    x_test = x_test.fillna(0)
    return x_test

def predict(df_data, user_data):
    try:
        with open(MODEL_FILE, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        return f"Error loading model: {str(e)}"

    x_test = x_test_dataframe(df_data, user_data)
    prediction = model.predict(x_test)[0]
    return prediction
