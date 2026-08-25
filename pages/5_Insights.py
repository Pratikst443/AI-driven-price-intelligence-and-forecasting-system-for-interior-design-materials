import streamlit as st

from utils import (
    load_growth_summary,
    load_model_comparison,
    load_future_summary
)

st.set_page_config(
    page_title="AI Insights",
    page_icon="💡",
    layout="wide"
)

growth = load_growth_summary()
models = load_model_comparison()
future = load_future_summary()

st.title("💡 AI Insights")

st.caption(
    "AI-generated insights based on historical trends and forecasting results."
)

#Key insights card
highest_growth = growth.loc[
    growth["CAGR"].idxmax()
]

most_volatile = growth.loc[
    growth["Volatility"].idxmax()
]

best_model = models.loc[
    models["MAE"].idxmin()
]

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Highest CAGR",
        highest_growth["Category"]
    )

with c2:
    st.metric(
        "Most Volatile",
        most_volatile["Category"]
    )

with c3:
    st.metric(
        "Best Forecast Model",
        best_model["Model"]
    )

#Business insights
st.subheader("Growth Insights")

st.markdown(f"""
- **{highest_growth['Category']}** recorded the highest long-term growth (CAGR).
- **{most_volatile['Category']}** experienced the greatest price fluctuations.
- Historical trends indicate different growth patterns across categories, helping identify areas with stronger market potential.
""")

#Forecast insights
st.subheader("Forecast Insights")

st.markdown("""
- Forecasts indicate a continued upward trend in prices for several interior design products.
- Confidence intervals suggest varying levels of prediction certainty across products.
- Forecasting can support inventory planning, budgeting, and procurement decisions.
""")

#Model insights
st.subheader("Model Insights")

st.markdown(f"""
- **{best_model['Model']}** achieved the lowest MAE and RMSE.
- Lower prediction errors indicate better forecasting accuracy.
- This model is recommended for future price prediction tasks in this project.
""")

#Recommandations
st.subheader("Business Recommendations")

st.success("""
• Prioritize inventory for high-growth categories.

• Monitor volatile categories more frequently.

• Use forecast results for procurement planning.

• Update forecasting models periodically with new pricing data.

• Adopt AI-assisted decision making to improve pricing strategy.
""")