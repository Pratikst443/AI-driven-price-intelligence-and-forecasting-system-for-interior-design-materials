import os
import pandas as pd

DATA_FOLDER = "data"

def load_dataset():
    return pd.read_csv(os.path.join(DATA_FOLDER, "interior_design_prices.csv"))

def load_growth_summary():
    return pd.read_csv(os.path.join(DATA_FOLDER, "growth_summary.csv"))

def load_model_comparison():
    return pd.read_csv(os.path.join(DATA_FOLDER, "model_comparison.csv"))

def load_prophet_evaluation():
    return pd.read_csv(os.path.join(DATA_FOLDER, "prophet_evaluation.csv"))

def load_arima_evaluation():
    return pd.read_csv(os.path.join(DATA_FOLDER, "arima_evaluation.csv"))

def load_future_summary():
    return pd.read_csv(os.path.join(DATA_FOLDER, "future_summary_next12m.csv"))

def load_forecast(subcategory):

    filename = f"forecast_{subcategory}.csv"

    path = os.path.join(
        DATA_FOLDER,
        "forecast",
        filename
    )

    return pd.read_csv(path)