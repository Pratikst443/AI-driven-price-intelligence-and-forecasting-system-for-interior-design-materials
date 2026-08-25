import streamlit as st

from utils import (
    load_dataset,
    load_growth_summary
)

from charts import (
    historical_trend,
    cagr_chart,
    volatility_chart,
    monthly_return_chart
)
st.set_page_config(
    page_title="Historical Analysis",
    page_icon="📈",
    layout="wide"
)

df = load_dataset()
summary = load_growth_summary()

st.title("📈 Historical Analysis")

st.markdown("""
Analyze historical price trends and category-wise performance.
""")

st.info("""
This page summarizes historical pricing behaviour across interior design categories,
including long-term growth (CAGR), price variability (Volatility), and average monthly returns.
""")

#Category filter
category = st.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].unique())
)

filtered_df = df.copy()

if category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

    summary = summary[
        summary["Category"] == category
    ]

#Historical trend
st.plotly_chart(
    historical_trend(filtered_df),
    use_container_width=True
)


# Growth & Stability

left, right = st.columns(2)

with left:

    st.plotly_chart(
        cagr_chart(summary),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        volatility_chart(summary),
        use_container_width=True
    )

st.plotly_chart(
    monthly_return_chart(summary),
    use_container_width=True
)

#Growth summary table
st.subheader("📋 Growth Summary")

st.dataframe(
    summary,
    use_container_width=True
)