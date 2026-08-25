import streamlit as st

from utils import (
    load_dataset,
    load_forecast
)

from charts import forecast_chart

st.set_page_config(
    page_title="Forecasting",
    page_icon="🔮",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------

df = load_dataset()


# -----------------------------
# Title
# -----------------------------

st.title("🔮 Forecasting")

st.caption(
    "Explore future price forecasts for interior design products."
)

# -----------------------------
# Filters
# -----------------------------

category = st.selectbox(
    "Category",
    sorted(df["Category"].unique())
)

subcategories = sorted(
    df.loc[
        df["Category"] == category,
        "Sub_Category"
    ]
    .dropna()
    .astype(str)
    .unique()
)

subcategory = st.selectbox(
    "Sub Category",
    subcategories
)

# -----------------------------
# Load Forecast
# -----------------------------

forecast = load_forecast(subcategory)
forecast = forecast[
    forecast["ds"] >= "2026-01-01"
]

# -----------------------------
# Forecast Chart
# -----------------------------

st.plotly_chart(
    forecast_chart(
    forecast,
    category
    ),
    use_container_width=True
)

# -----------------------------
# Forecast Summary
# -----------------------------

st.subheader("📊 Forecast Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Forecast Period",
        f"{len(forecast)} Months"
    )

with c2:
    st.metric(
        "Average Forecast",
        f"₹{forecast['yhat'].mean():,.0f}"
    )

with c3:
    st.metric(
        "Highest Forecast",
        f"₹{forecast['yhat'].max():,.0f}"
    )

with c4:
    st.metric(
        "Lowest Forecast",
        f"₹{forecast['yhat'].min():,.0f}"
    )

# -----------------------------
# Forecast Table
# -----------------------------

forecast_display = forecast.rename(
    columns={
        "ds": "Date",
        "yhat": "Predicted Price",
        "yhat_lower": "Lower Estimate",
        "yhat_upper": "Upper Estimate"
    }
)

st.subheader("📋 Forecast Data")

st.dataframe(
    forecast_display,
    use_container_width=True
)