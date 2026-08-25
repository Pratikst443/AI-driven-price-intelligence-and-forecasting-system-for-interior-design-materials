import streamlit as st

from utils import load_model_comparison

from charts import (
    mae_chart,
    rmse_chart
)

st.set_page_config(
    page_title="Model Comparison",
    page_icon="🤖",
    layout="wide"
)

model_df = load_model_comparison()

st.title("🤖 Model Comparison")

st.caption(
    "Compare the performance of Prophet, ARIMA, and GRU forecasting models."
)

#Best model card
best = model_df.loc[
    model_df["MAE"].idxmin()
]

st.success(
    f"""
🏆 Best Performing Model

**{best['Model']}**

MAE: {best['MAE']:.2f}

RMSE: {best['RMSE']:.2f}
"""
)

#Charts
left, right = st.columns(2)

with left:

    st.plotly_chart(
        mae_chart(model_df),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        rmse_chart(model_df),
        use_container_width=True
    )

#Comparison table
st.subheader("📋 Model Performance")

st.dataframe(
    model_df,
    use_container_width=True
)

#Key insights
st.subheader("💡 Key Insights")

st.markdown("""
- **Prophet** achieved the lowest MAE and RMSE, indicating the highest forecasting accuracy.
- **GRU** outperformed ARIMA but did not surpass Prophet.
- **ARIMA** produced the largest prediction errors among the three models.
- Overall, **Prophet** was selected as the preferred forecasting model for this project.
""")