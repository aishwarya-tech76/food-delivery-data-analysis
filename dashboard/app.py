import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Food Delivery Analytics",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
<style>

/* ==============================
   MAIN PAGE
   ============================== */

.stApp {
    background: #f4f6fa;
}

.block-container {
    padding-top: 2.5rem !important;
    padding-bottom: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 1500px;
}

/* ==============================
   SIDEBAR
   ============================== */

[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263244;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

[data-testid="stSidebar"] label {
    color: #e5e7eb !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] .stCaption {
    color: #94a3b8 !important;
}

/* ==============================
   MAIN TITLE
   ============================== */

.dashboard-title {
    width: 100%;
    font-size: clamp(28px, 3vw, 38px);
    line-height: 1.2;
    font-weight: 800;
    color: #0f172a;
    margin-top: 0;
    margin-bottom: 7px;
    padding: 0;
    text-align: left;
    white-space: normal;
    overflow: visible;
}

.dashboard-subtitle {
    width: 100%;
    font-size: 14px;
    line-height: 1.6;
    color: #64748b;
    margin-top: 0;
    margin-bottom: 28px;
    padding: 0;
    white-space: normal;
    overflow: visible;
}

/* ==============================
   SECTION HEADINGS
   ============================== */

.section-heading {
    font-size: 22px;
    line-height: 1.4;
    font-weight: 800;
    color: #172033;
    margin-top: 27px;
    margin-bottom: 15px;
}

/* ==============================
   KPI CARDS
   ============================== */

[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px 18px !important;
    min-height: 142px;
    height: 142px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.07);
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
}

[data-testid="stMetricLabel"] {
    color: #64748b !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    line-height: 1.35 !important;
    white-space: nowrap !important;
}

[data-testid="stMetricValue"] {
    color: #0f172a !important;
    font-size: 27px !important;
    font-weight: 800 !important;
    line-height: 1.25 !important;
    white-space: nowrap !important;
    overflow: visible !important;
    letter-spacing: -0.3px;
}

/* ==============================
   CHART CARDS
   ============================== */

[data-testid="stPlotlyChart"] {
    background: #1f2937;
    border: 1px solid #293548;
    border-radius: 16px;
    padding: 4px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.14);
    overflow: hidden;
}

/* ==============================
   DATAFRAME
   ============================== */

[data-testid="stDataFrame"] {
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
}

/* ==============================
   INFO BOXES
   ============================== */

[data-testid="stAlert"] {
    border-radius: 14px;
}

/* ==============================
   FOOTER
   ============================== */

.footer-text {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 35px;
    margin-bottom: 10px;
}

/* ==============================
   RESPONSIVE
   ============================== */

@media (max-width: 900px) {

    .block-container {
        padding-top: 1.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .dashboard-title {
        font-size: 28px;
    }

    [data-testid="stMetric"] {
        min-height: 130px;
        height: auto;
    }

    [data-testid="stMetricValue"] {
        font-size: 25px !important;
    }
}

</style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# PROJECT PATH
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "food_delivery.csv"

# =========================================================
# LOAD DATA
# =========================================================

try:

    df = pd.read_csv(DATA_PATH)

except Exception as e:

    st.error("❌ food_delivery.csv could not be loaded.")
    st.error(str(e))
    st.stop()

# =========================================================
# DATA CLEANING
# =========================================================

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

numeric_columns = [
    "Quantity",
    "Price",
    "Total_Amount",
    "Delivery_Time_Min",
    "Rating"
]

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

df = df.dropna(
    subset=[
        "Order_ID",
        "Order_Date",
        "Total_Amount"
    ]
).copy()

# =========================================================
# DATE FEATURES
# =========================================================

df["Month_Number"] = df["Order_Date"].dt.month

df["Month"] = df["Order_Date"].dt.strftime("%b")

df["Day_Name"] = df["Order_Date"].dt.day_name()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎛️ Dashboard Filters")

st.sidebar.caption(
    "Customize your analysis"
)

# ---------------------------------------------------------
# CITY
# ---------------------------------------------------------

city_list = sorted(
    df["City"].dropna().unique()
)

selected_city = st.sidebar.multiselect(
    "📍 City",
    city_list,
    default=city_list
)

# ---------------------------------------------------------
# CATEGORY
# ---------------------------------------------------------

category_list = sorted(
    df["Category"].dropna().unique()
)

selected_category = st.sidebar.multiselect(
    "🍕 Category",
    category_list,
    default=category_list
)

# ---------------------------------------------------------
# PAYMENT
# ---------------------------------------------------------

payment_list = sorted(
    df["Payment_Mode"].dropna().unique()
)

selected_payment = st.sidebar.multiselect(
    "💳 Payment Mode",
    payment_list,
    default=payment_list
)

# ---------------------------------------------------------
# ORDER STATUS
# ---------------------------------------------------------

status_list = sorted(
    df["Order_Status"].dropna().unique()
)

selected_status = st.sidebar.multiselect(
    "📦 Order Status",
    status_list,
    default=status_list
)

# =========================================================
# FILTER DATA
# =========================================================

filtered_df = df[
    df["City"].isin(selected_city)
    &
    df["Category"].isin(selected_category)
    &
    df["Payment_Mode"].isin(selected_payment)
    &
    df["Order_Status"].isin(selected_status)
].copy()

if filtered_df.empty:

    st.warning(
        "⚠️ No data available for the selected filters."
    )

    st.stop()

# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    """
    <div class="dashboard-title">
        🍔 Food Delivery Analytics Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="dashboard-subtitle">
        Sales Performance • Customer Behaviour • Restaurant Analysis •
        Payment Insights • Delivery Performance
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# KPI CALCULATIONS
# =========================================================

total_orders = len(filtered_df)

gross_order_value = filtered_df[
    "Total_Amount"
].sum()

total_quantity = filtered_df[
    "Quantity"
].sum()

average_order_value = filtered_df[
    "Total_Amount"
].mean()

cancelled_orders = (
    filtered_df["Order_Status"] == "Cancelled"
).sum()

cancellation_rate = (
    cancelled_orders /
    total_orders *
    100
)

delivered_df = filtered_df[
    filtered_df["Order_Status"] == "Delivered"
]

delivered_orders = len(
    delivered_df
)

delivered_revenue = delivered_df[
    "Total_Amount"
].sum()

average_delivery_time = delivered_df[
    "Delivery_Time_Min"
].mean()

average_rating = filtered_df[
    "Rating"
].mean()

# =========================================================
# BUSINESS OVERVIEW
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        📊 Business Overview
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# KPI ROW 1
# =========================================================

kpi1, kpi2, kpi3 = st.columns(
    3,
    gap="medium"
)

with kpi1:

    st.metric(
        label="📦 Total Orders",
        value=f"{total_orders:,}"
    )

with kpi2:

    st.metric(
        label="💰 Gross Order Value",
        value=f"₹{gross_order_value:,.0f}"
    )

with kpi3:

    st.metric(
        label="🚚 Delivered Revenue",
        value=f"₹{delivered_revenue:,.0f}"
    )

# =========================================================
# KPI ROW 2
# =========================================================

kpi4, kpi5, kpi6 = st.columns(
    3,
    gap="medium"
)

with kpi4:

    st.metric(
        label="🛒 Quantity Sold",
        value=f"{total_quantity:,}"
    )

with kpi5:

    st.metric(
        label="❌ Cancellation Rate",
        value=f"{cancellation_rate:.1f}%"
    )

with kpi6:

    if pd.notna(average_rating):

        st.metric(
            label="⭐ Average Rating",
            value=f"{average_rating:.2f} / 5"
        )

    else:

        st.metric(
            label="⭐ Average Rating",
            value="N/A"
        )

# =========================================================
# SALES ANALYSIS
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        💰 Sales Analysis
    </div>
    """,
    unsafe_allow_html=True
)

sales_col1, sales_col2 = st.columns(
    2,
    gap="medium"
)

# =========================================================
# CATEGORY SALES
# =========================================================

with sales_col1:

    category_sales = (
        filtered_df
        .groupby("Category")["Total_Amount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    fig_category = px.bar(
        category_sales,
        x="Category",
        y="Total_Amount",
        title="Sales by Category",
        text_auto=".2s"
    )

    fig_category.update_traces(
        marker_color="#6366F1",
        hovertemplate=
        "<b>%{x}</b><br>"
        "Sales: ₹%{y:,.0f}"
        "<extra></extra>"
    )

    fig_category.update_layout(
        height=400,
        margin=dict(
            l=45,
            r=20,
            t=70,
            b=50
        ),
        paper_bgcolor="#1f2937",
        plot_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        xaxis=dict(
            color="#d1d5db",
            showgrid=False
        ),
        yaxis=dict(
            color="#d1d5db",
            gridcolor="#374151"
        )
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# =========================================================
# MONTHLY SALES
# =========================================================

with sales_col2:

    monthly_sales = (
        filtered_df
        .groupby(
            [
                "Month_Number",
                "Month"
            ]
        )["Total_Amount"]
        .sum()
        .reset_index()
        .sort_values(
            "Month_Number"
        )
    )

    fig_month = px.line(
        monthly_sales,
        x="Month",
        y="Total_Amount",
        title="Monthly Sales Trend",
        markers=True
    )

    fig_month.update_traces(
        line=dict(
            color="#06B6D4",
            width=4
        ),
        marker=dict(
            size=9
        ),
        hovertemplate=
        "<b>%{x}</b><br>"
        "Sales: ₹%{y:,.0f}"
        "<extra></extra>"
    )

    fig_month.update_layout(
        height=400,
        margin=dict(
            l=45,
            r=20,
            t=70,
            b=50
        ),
        paper_bgcolor="#1f2937",
        plot_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        xaxis=dict(
            color="#d1d5db",
            showgrid=False
        ),
        yaxis=dict(
            color="#d1d5db",
            gridcolor="#374151"
        )
    )

    st.plotly_chart(
        fig_month,
        use_container_width=True
    )

# =========================================================
# PAYMENT & ORDER STATUS
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        💳 Payment & Order Analysis
    </div>
    """,
    unsafe_allow_html=True
)

payment_col1, payment_col2 = st.columns(
    2,
    gap="medium"
)

# =========================================================
# PAYMENT MODE
# =========================================================

with payment_col1:

    payment_data = (
        filtered_df[
            "Payment_Mode"
        ]
        .value_counts()
        .reset_index()
    )

    payment_data.columns = [
        "Payment_Mode",
        "Orders"
    ]

    fig_payment = px.pie(
        payment_data,
        names="Payment_Mode",
        values="Orders",
        title="Payment Mode Preference",
        hole=0.55
    )

    fig_payment.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_payment.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        ),
        paper_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        legend=dict(
            font=dict(
                color="white"
            )
        )
    )

    st.plotly_chart(
        fig_payment,
        use_container_width=True
    )

# =========================================================
# ORDER STATUS
# =========================================================

with payment_col2:

    status_data = (
        filtered_df[
            "Order_Status"
        ]
        .value_counts()
        .reset_index()
    )

    status_data.columns = [
        "Order_Status",
        "Orders"
    ]

    fig_status = px.pie(
        status_data,
        names="Order_Status",
        values="Orders",
        title="Order Status Distribution",
        hole=0.55
    )

    fig_status.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_status.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        ),
        paper_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        legend=dict(
            font=dict(
                color="white"
            )
        )
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

# =========================================================
# TOP PERFORMERS
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        🏆 Top Performers
    </div>
    """,
    unsafe_allow_html=True
)

top_col1, top_col2 = st.columns(
    2,
    gap="medium"
)

# =========================================================
# TOP RESTAURANTS
# =========================================================

with top_col1:

    restaurant_sales = (
        filtered_df
        .groupby(
            "Restaurant"
        )["Total_Amount"]
        .sum()
        .sort_values()
        .tail(5)
        .reset_index()
    )

    fig_restaurant = px.bar(
        restaurant_sales,
        x="Total_Amount",
        y="Restaurant",
        orientation="h",
        title="Top 5 Restaurants by Sales",
        text_auto=".2s"
    )

    fig_restaurant.update_traces(
        marker_color="#F59E0B"
    )

    fig_restaurant.update_layout(
        height=400,
        margin=dict(
            l=45,
            r=20,
            t=70,
            b=45
        ),
        paper_bgcolor="#1f2937",
        plot_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        xaxis=dict(
            color="#d1d5db",
            gridcolor="#374151"
        ),
        yaxis=dict(
            color="#d1d5db",
            showgrid=False
        )
    )

    st.plotly_chart(
        fig_restaurant,
        use_container_width=True
    )

# =========================================================
# TOP ITEMS
# =========================================================

with top_col2:

    item_sales = (
        filtered_df
        .groupby(
            "Item"
        )["Total_Amount"]
        .sum()
        .sort_values()
        .tail(5)
        .reset_index()
    )

    fig_items = px.bar(
        item_sales,
        x="Total_Amount",
        y="Item",
        orientation="h",
        title="Top 5 Food Items by Sales",
        text_auto=".2s"
    )

    fig_items.update_traces(
        marker_color="#10B981"
    )

    fig_items.update_layout(
        height=400,
        margin=dict(
            l=45,
            r=20,
            t=70,
            b=45
        ),
        paper_bgcolor="#1f2937",
        plot_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        xaxis=dict(
            color="#d1d5db",
            gridcolor="#374151"
        ),
        yaxis=dict(
            color="#d1d5db",
            showgrid=False
        )
    )

    st.plotly_chart(
        fig_items,
        use_container_width=True
    )

# =========================================================
# CITY & DAY ANALYSIS
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        📍 Location & Time Analysis
    </div>
    """,
    unsafe_allow_html=True
)

location_col1, location_col2 = st.columns(
    2,
    gap="medium"
)

# =========================================================
# CITY SALES
# =========================================================

with location_col1:

    city_sales = (
        filtered_df
        .groupby(
            "City"
        )["Total_Amount"]
        .sum()
        .sort_values()
        .reset_index()
    )

    fig_city = px.bar(
        city_sales,
        x="Total_Amount",
        y="City",
        orientation="h",
        title="Sales by City",
        text_auto=".2s"
    )

    fig_city.update_traces(
        marker_color="#8B5CF6"
    )

    fig_city.update_layout(
        height=400,
        margin=dict(
            l=45,
            r=20,
            t=70,
            b=45
        ),
        paper_bgcolor="#1f2937",
        plot_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        xaxis=dict(
            color="#d1d5db",
            gridcolor="#374151"
        ),
        yaxis=dict(
            color="#d1d5db",
            showgrid=False
        )
    )

    st.plotly_chart(
        fig_city,
        use_container_width=True
    )

# =========================================================
# DAY OF WEEK
# =========================================================

with location_col2:

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    day_sales = (
        filtered_df
        .groupby(
            "Day_Name"
        )["Total_Amount"]
        .sum()
        .reindex(
            day_order
        )
        .reset_index()
    )

    fig_day = px.bar(
        day_sales,
        x="Day_Name",
        y="Total_Amount",
        title="Sales by Day of Week",
        text_auto=".2s"
    )

    fig_day.update_traces(
        marker_color="#EC4899"
    )

    fig_day.update_layout(
        height=400,
        margin=dict(
            l=45,
            r=20,
            t=70,
            b=50
        ),
        paper_bgcolor="#1f2937",
        plot_bgcolor="#1f2937",
        font=dict(
            color="white"
        ),
        title_font=dict(
            color="white",
            size=18
        ),
        xaxis=dict(
            color="#d1d5db",
            showgrid=False
        ),
        yaxis=dict(
            color="#d1d5db",
            gridcolor="#374151"
        )
    )

    st.plotly_chart(
        fig_day,
        use_container_width=True
    )

# =========================================================
# DELIVERY PERFORMANCE
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        🚚 Delivery Performance
    </div>
    """,
    unsafe_allow_html=True
)

delivery_col1, delivery_col2, delivery_col3, delivery_col4 = st.columns(
    4,
    gap="medium"
)

with delivery_col1:

    st.metric(
        "📦 Delivered Orders",
        f"{delivered_orders:,}"
    )

with delivery_col2:

    st.metric(
        "❌ Cancelled Orders",
        f"{cancelled_orders:,}"
    )

with delivery_col3:

    if pd.notna(average_delivery_time):

        st.metric(
            "⏱️ Avg Delivery Time",
            f"{average_delivery_time:.1f} min"
        )

    else:

        st.metric(
            "⏱️ Avg Delivery Time",
            "N/A"
        )

with delivery_col4:

    st.metric(
        "💵 Average Order Value",
        f"₹{average_order_value:,.0f}"
    )

# =========================================================
# TOP CUSTOMERS
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        👥 Top 5 Customers
    </div>
    """,
    unsafe_allow_html=True
)

top_customers = (
    filtered_df
    .groupby(
        [
            "Customer_ID",
            "Customer_Name"
        ]
    )["Total_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(5)
    .reset_index()
)

top_customers.columns = [
    "Customer ID",
    "Customer Name",
    "Purchase Value"
]

top_customers["Purchase Value"] = (
    top_customers[
        "Purchase Value"
    ]
    .apply(
        lambda x:
        f"₹{x:,.2f}"
    )
)

st.dataframe(
    top_customers,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# BUSINESS INSIGHTS
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        💡 Business Insights
    </div>
    """,
    unsafe_allow_html=True
)

insight_col1, insight_col2 = st.columns(
    2,
    gap="medium"
)

# ---------------------------------------------------------
# TOP CATEGORY
# ---------------------------------------------------------

top_category_data = (
    filtered_df
    .groupby(
        "Category"
    )["Total_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)

top_category = top_category_data.index[0]

top_category_sales = top_category_data.iloc[0]

# ---------------------------------------------------------
# TOP ITEM
# ---------------------------------------------------------

top_item_data = (
    filtered_df
    .groupby(
        "Item"
    )["Total_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)

top_item = top_item_data.index[0]

# ---------------------------------------------------------
# TOP CITY
# ---------------------------------------------------------

top_city_data = (
    filtered_df
    .groupby(
        "City"
    )["Total_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)

top_city = top_city_data.index[0]

# ---------------------------------------------------------
# PAYMENT
# ---------------------------------------------------------

top_payment = (
    filtered_df[
        "Payment_Mode"
    ]
    .value_counts()
    .index[0]
)

# ---------------------------------------------------------
# INSIGHTS DISPLAY
# ---------------------------------------------------------

with insight_col1:

    st.info(
        f"🍕 **Top Category:** "
        f"{top_category} — "
        f"₹{top_category_sales:,.0f}"
    )

    st.info(
        f"🔥 **Top Food Item:** "
        f"{top_item}"
    )

    st.info(
        f"📍 **Top City by Sales:** "
        f"{top_city}"
    )

with insight_col2:

    st.info(
        f"💳 **Most Used Payment Mode:** "
        f"{top_payment}"
    )

    st.info(
        f"📦 **Total Orders:** "
        f"{total_orders:,}"
    )

    st.warning(
        f"⚠️ **Cancellation Rate:** "
        f"{cancellation_rate:.1f}%"
    )

# =========================================================
# DATA PREVIEW
# =========================================================

st.markdown(
    """
    <div class="section-heading">
        📋 Dataset Preview
    </div>
    """,
    unsafe_allow_html=True
)

st.dataframe(
    filtered_df.head(100),
    use_container_width=True,
    hide_index=True,
    height=320
)

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer-text">
        🍔 Food Delivery Analytics Dashboard
        • Python • Pandas • Plotly • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)