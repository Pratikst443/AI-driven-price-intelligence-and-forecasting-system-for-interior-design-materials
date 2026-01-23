import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Interior Design Market Trends",
    layout="wide"
)

# -------------------------------------------------
# Global CSS (background, sidebar, buttons)
# -------------------------------------------------
st.markdown("""
<style>

/* App background */
[data-testid="stAppViewContainer"] {
    background-color: #f6f3ec;
    color: #545454;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #789c83;
}
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Buttons */
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

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Title (HTML for full color control)
# -------------------------------------------------
st.markdown(
    "<h1 style='color:#789c83;'>AI for Comparative Price Analysis in Interior Design</h1>",
    unsafe_allow_html=True
)

# -------------------------------------------------
# Load data
# -------------------------------------------------
df = pd.read_csv("interior_design_prices.csv", parse_dates=["Date"])
future_summary = pd.read_csv("future_summary_next12m.csv")
eval_df = pd.read_csv("evaluation_summary.csv")

# -------------------------------------------------
# Sidebar controls
# -------------------------------------------------
st.sidebar.header("Controls")
category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

# -------------------------------------------------
# Historical Trend Plot
# -------------------------------------------------
cat_df = df[df["Category"] == category]

st.markdown(
    f"<h2 style='color:#789c83;'>Historical Price Trend: {category}</h2>",
    unsafe_allow_html=True
)

fig, ax = plt.subplots()
ax.plot(
    cat_df["Date"],
    cat_df["Price"],
    marker="o",
    color="#789c83"
)
ax.set_xlabel("Date")
ax.set_ylabel("Price (INR)")
ax.set_title(f"{category} Price Trend", color="#545454")
st.pyplot(fig)

# -------------------------------------------------
# Two-column layout: Evaluation + Forecast summary
# -------------------------------------------------
col1, col2 = st.columns(2)

# ---------- Evaluation Metrics Table ----------
with col1:
    st.markdown(
        "<h2 style='color:#789c83;'>Model Evaluation Metrics (2024)</h2>",
        unsafe_allow_html=True
    )

    styled_eval = (
        eval_df.style
        .set_properties(**{
            "background-color": "#f6f3ec",
            "color": "#545454",
            "border-color": "#789c83"
        })
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#789c83"),
                    ("color", "white"),
                    ("font-weight", "bold")
                ]
            }
        ])
    )

    st.dataframe(styled_eval, use_container_width=True)

# ---------- Forecast Summary Table ----------
with col2:
    st.markdown(
        "<h2 style='color:#789c83;'>Avg Predicted Price (Next 12 Months)</h2>",
        unsafe_allow_html=True
    )

    styled_future = (
        future_summary.style
        .set_properties(**{
            "background-color": "#f6f3ec",
            "color": "#545454",
            "border-color": "#789c83"
        })
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#789c83"),
                    ("color", "white"),
                    ("font-weight", "bold")
                ]
            }
        ])
    )

    st.dataframe(styled_future, use_container_width=True)

# -------------------------------------------------
# Insights Section
# -------------------------------------------------
st.markdown(
    "<h2 style='color:#789c83;'>Key Observations</h2>",
    unsafe_allow_html=True
)

st.markdown("""
<ul>
<li>Lighting and Flooring show the lowest forecasting error, making them highly predictable.</li>
<li>Decor is more volatile, resulting in relatively higher error values.</li>
<li>Overall model performance is strong with low MAE and RMSE across categories.</li>
</ul>
""", unsafe_allow_html=True)
