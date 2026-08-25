import streamlit as st
from utils import load_dataset

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

df = load_dataset()

st.title("📊 Dataset Explorer")

st.markdown(
    """
    Explore the Interior Design Price Dataset.
    """
)

#summary cards
st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Rows", len(df))

with c2:
    st.metric("Categories", df["Category"].nunique())

with c3:
    st.metric("Subcategories", df["Sub_Category"].nunique())

with c4:
    st.metric("Sources", df["Source"].nunique())




# -----------------------------
# Filters
# -----------------------------

st.sidebar.header("Filters")

# Category
category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].dropna().unique())
)

# Dynamic Subcategory
if category == "All":
    subcategories = sorted(
        df["Sub_Category"].dropna().unique()
    )
else:
    subcategories = sorted(
        df.loc[
            df["Category"] == category,
            "Sub_Category"
        ].dropna().unique()
    )

subcategory = st.sidebar.selectbox(
    "Sub Category",
    ["All"] + subcategories
)

# Source
source = st.sidebar.selectbox(
    "Source",
    ["All"] + sorted(df["Source"].dropna().unique())
)

# Price Range
price_range = st.sidebar.slider(
    "Price Range (₹)",
    int(df["Price"].min()),
    int(df["Price"].max()),
    (
        int(df["Price"].min()),
        int(df["Price"].max())
    )
)

# Apply Filters
filtered = df.copy()

if category != "All":
    filtered = filtered[
        filtered["Category"] == category
    ]

if subcategory != "All":
    filtered = filtered[
        filtered["Sub_Category"] == subcategory
    ]

if source != "All":
    filtered = filtered[
        filtered["Source"] == source
    ]

filtered = filtered[
    filtered["Price"].between(
        price_range[0],
        price_range[1]
    )
]

#dataset search
st.subheader("🔍 Search")

search = st.text_input(
    "Search Product, Category or Subcategory"
)

if search:

    filtered = filtered[
        filtered["Product_Name"]
        .str.contains(search, case=False, na=False)
        |
        filtered["Category"]
        .str.contains(search, case=False, na=False)
        |
        filtered["Sub_Category"]
        .str.contains(search, case=False, na=False)
    ]

#Dataset statistics
st.subheader("📈 Dataset Statistics")

stats = filtered["Price"].describe()

a,b,c,d,e = st.columns(5)


a.metric(
    "Average",
    f"₹{stats['mean']:,.0f}"
)

b.metric(
    "Median",
    f"₹{filtered['Price'].median():,.0f}"
)

c.metric(
    "Minimum",
    f"₹{stats['min']:,.0f}"
)

d.metric(
    "Maximum",
    f"₹{stats['max']:,.0f}"
)

e.metric(
    "Std Dev",
    f"₹{stats['std']:,.0f}"
)

st.divider()

#display dataset
st.dataframe(
    filtered,
    use_container_width=True,
    height=600
)

