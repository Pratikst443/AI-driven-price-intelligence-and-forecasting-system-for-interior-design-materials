import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Interior Design Market Trends", 
    layout="wide"
)


st.markdown("""
<style>

/* -----------------------
   GLOBAL BACKGROUND
------------------------*/
[data-testid="stAppViewContainer"] {
    background-color: #f6f3ec;
    color: #545454;
}

/* -----------------------
   SIDEBAR
------------------------*/
[data-testid="stSidebar"] {
    background-color: #789c83;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* -----------------------
   TEXT & HEADINGS
------------------------*/
html, body, p, li, span {
    color: #545454 !important;
}

/* Disable Streamlit heading colors */
h1, h2, h3 {
    all: unset;
}

/* -----------------------
   BUTTONS
------------------------*/
div.stButton > button {
    background-color: #789c83;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.4em 1em;
}

div.stButton > button:hover {
    background-color: #6f8f78;
}

/* -----------------------
   DATAFRAME
------------------------*/
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<h1 style="color:#789c83; font-weight:700;">
AI for Comparative Price Analysis in Interior Design
</h1>
""", unsafe_allow_html=True)



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

st.markdown(
    f"<h2 style='color:#789c83;'>Historical Price Trend: {category}</h2>",
    unsafe_allow_html=True
)

fig, ax = plt.subplots()
ax.plot(cat_df["Date"], cat_df["Price"], marker="o", color="#789c83")
ax.set_xlabel("Date")
ax.set_ylabel("Price (INR)")
ax.set_title(f"{category} Price Trend", color="#545454")
st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Historical Trend")
    st.pyplot(fig)

with col2:
    st.subheader("Evaluation Metrics")
    st.dataframe(eval_df)

# Forecast Summary

st.subheader("Average Predicted Price (Next 12 Months)")
st.markdown(
    f"<h2 style='color:#789c83;'>Average Predicted Price (Next 12 Months): {category}</h2>",
    unsafe_allow_html=True
)
st.dataframe(future_summary)


# Evaluation Metrics

st.markdown(
    f"<h2 style='color:#789c83;'>model Evaluation Metrics: {category}</h2>",
    unsafe_allow_html=True
)
st.dataframe(eval_df)


# Insights

st.markdown(
    f"<h2 style='color:#789c83;'>Key Observations: {category}</h2>",
    unsafe_allow_html=True
)
st.markdown(""")
- Lighting and Flooring show the lowest forecasting error.
- Decor is more volatile, leading to slightly higher errors.
- Overall model performance is strong with low MAE and RMSE.
""")
