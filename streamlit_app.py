import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Interior Price Trend Dashboard", layout="wide")

st.title("AI for Comparative Price Analysis in Interior Design")

# Load data
df = pd.read_csv("interior_design_prices.csv", parse_dates=["Date"])
future_summary = pd.read_csv("future_summary_next12m.csv")
eval_df = pd.read_csv("evaluation_summary.csv")

# Sidebar
st.sidebar.header("Controls")
category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)


# Historical Trend

st.subheader(f"Historical Price Trend: {category}")

cat_df = df[df["Category"] == category]

fig, ax = plt.subplots()
ax.plot(cat_df["Date"], cat_df["Price"], marker="o")
ax.set_xlabel("Date")
ax.set_ylabel("Price (INR)")
ax.set_title(f"{category} Price Trend")
st.pyplot(fig)


# Forecast Summary

st.subheader("Average Predicted Price (Next 12 Months)")
st.dataframe(future_summary)


# Evaluation Metrics

st.subheader("Model Evaluation Metrics (2024)")
st.dataframe(eval_df)


# Insights

st.subheader("Key Observations")
st.markdown("""
- Lighting and Flooring show the lowest forecasting error.
- Decor is more volatile, leading to slightly higher errors.
- Overall model performance is strong with low MAE and RMSE.
""")
