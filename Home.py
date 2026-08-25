import streamlit as st

from utils import load_dataset

from charts import (
    category_distribution,
    average_price_chart,
    historical_trend
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Price Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = load_dataset()

df["Date"] = df["Date"].astype("datetime64[ns]")

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.subheader("Filters")

# Category Filter
categories = ["All"] + sorted(df["Category"].dropna().unique())

category = st.sidebar.selectbox(
    "Select Category",
    categories
)

# Get subcategories based on category selection
if category == "All":
    available_subcategories = sorted(
        df["Sub_Category"].dropna().unique()
    )
else:
    available_subcategories = sorted(
        df.loc[
            df["Category"] == category,
            "Sub_Category"
        ].dropna().unique()
    )

subcategory = st.sidebar.selectbox(
    "Select Subcategory",
    ["All"] + available_subcategories
)

# Apply Filters
filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

if subcategory != "All":
    filtered_df = filtered_df[
        filtered_df["Sub_Category"] == subcategory
    ]

# --------------------------------------------------
# Dashboard Title
# --------------------------------------------------


st.image(
    "images/BLUE.png",
    width=300
)

st.subheader(
    "AI-Driven Price Intelligence & Forecasting System"
)

st.caption(
    "Comparative Price Forecasting of Interior Design Products using Prophet, ARIMA and GRU forecasting models."
)

st.divider()
# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📄 Total Records",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "📂 Categories",
        filtered_df["Category"].nunique()
    )

with col3:
    st.metric(
        "📁 Subcategories",
        filtered_df["Sub_Category"].nunique()
    )

with col4:
    st.metric(
        "🛋 Unique Products",
        filtered_df["Product_Name"].nunique()
    )

st.divider()

# --------------------------------------------------
# Dashboard Charts
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.plotly_chart(
        category_distribution(filtered_df),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        average_price_chart(filtered_df),
        use_container_width=True
    )

st.divider()

st.plotly_chart(
    historical_trend(filtered_df),
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Dataset Explorer
# --------------------------------------------------

st.subheader("📋 Dataset Explorer")

search = st.text_input(
    "Search Product Name"
)

display_df = filtered_df.copy()

if search:

    display_df = display_df[
        display_df["Product_Name"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.dataframe(
    display_df,
    use_container_width=True,
    height=400
)