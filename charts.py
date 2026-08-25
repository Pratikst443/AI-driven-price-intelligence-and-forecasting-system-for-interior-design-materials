import plotly.express as px

CATEGORY_COLORS = {
    "Furniture": "#7DB7E8",
    "Lighting": "#156FC5",
    "Flooring": "#F6A2A7",
    "Decor": "#FF2B2B"
}

def category_distribution(df):

    category_count = (
        df.groupby("Category")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        category_count,
        names="Category",
        values="Count",
        hole=0.55,
        color="Category",
        color_discrete_map=CATEGORY_COLORS,
        title="Category Distribution"
    )

    fig.update_layout(height=450)

    # Keep category color when only one category exists
    if len(category_count) == 1:

        category = category_count.iloc[0]["Category"]

        fig.update_traces(
            marker=dict(
                colors=[CATEGORY_COLORS[category]]
            )
        )

    return fig


def average_price_chart(df):

    avg_price = (
        df.groupby("Category")["Price"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        avg_price,
        x="Category",
        y="Price",
        color="Category",
        color_discrete_map=CATEGORY_COLORS,
        title="Average Price by Category"
    )

    fig.update_layout(
        height=450,
        showlegend=False
    )

    # Keep category color when only one category exists
    if len(avg_price) == 1:

        category = avg_price.iloc[0]["Category"]

        fig.update_traces(
            marker_color=CATEGORY_COLORS[category]
        )

    return fig

def historical_trend(df):

    import plotly.express as px

    trend = (
        df.groupby(["Date", "Category"])["Price"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="Date",
        y="Price",
        color="Category",
        color_discrete_map=CATEGORY_COLORS,
        markers=True,
        title="Historical Average Price Trend"
    )

    fig.update_layout(
        height=550,
        xaxis_title="Date",
        yaxis_title="Average Price (₹)"
    )

    return fig


#CAGR chart
def cagr_chart(growth_df):

    fig = px.bar(
        growth_df,
        x="Category",
        y="CAGR",
        color="Category",
        color_discrete_map=CATEGORY_COLORS,
        title="Compound Annual Growth Rate (CAGR)"
    )

    fig.update_layout(
        height=500,
        showlegend=False,
        xaxis_title="Category",
        yaxis_title="CAGR"
    )

    return fig

#Volatility chart
def volatility_chart(summary):

    fig = px.bar(
        summary,
        x="Category",
        y="Volatility",
        color="Category",
        color_discrete_map=CATEGORY_COLORS,
        title="Category Price Volatility"
    )

    fig.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Category",
        yaxis_title="Volatility"
    )

    return fig

#Average Monthly return
def monthly_return_chart(summary):

    fig = px.bar(
        summary,
        x="Category",
        y="Avg_Monthly_Return",
        color="Category",
        color_discrete_map=CATEGORY_COLORS,
        title="Average Monthly Return"
    )

    fig.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Category",
        yaxis_title="Average Monthly Return"
    )

    return fig

#Forecast chart function
def forecast_chart(forecast, category):

    fig = px.line(
        forecast,
        x="ds",
        y="yhat",
        title="Forecasted Price Trend"
    )

    # Forecast Line Color
    fig.update_traces(
        line=dict(
            color=CATEGORY_COLORS[category],
            width=4
        )
    )

    # Upper Confidence
    fig.add_scatter(
        x=forecast["ds"],
        y=forecast["yhat_upper"],
        mode="lines",
        line=dict(width=0),
        showlegend=False
    )

    # Lower Confidence
    fig.add_scatter(
        x=forecast["ds"],
        y=forecast["yhat_lower"],
        mode="lines",
        fill="tonexty",
        line=dict(width=0),
        fillcolor="rgba(120,120,120,0.15)",
        name="Confidence Interval"
    )

    fig.update_layout(
        height=550,
        xaxis_title="Date",
        yaxis_title="Predicted Price (₹)"
    )

    return fig

#MAE comparison
def mae_chart(model_df):

    fig = px.bar(
        model_df,
        x="Model",
        y="MAE",
        color="Model",
        title="Mean Absolute Error (MAE)"
    )

    fig.update_layout(
        height=450,
        showlegend=False
    )

    return fig

#RMSE comparison
def rmse_chart(model_df):

    fig = px.bar(
        model_df,
        x="Model",
        y="RMSE",
        color="Model",
        title="Root Mean Squared Error (RMSE)"
    )

    fig.update_layout(
        height=450,
        showlegend=False
    )

    return fig

