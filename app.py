import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("📊 Retail Sales Analytics Dashboard")
st.markdown("Interactive dashboard summarizing Week 1 findings from the Superstore dataset.")

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sidebar filter
category_filter = st.sidebar.multiselect(
    "Filter by Category", options=df['Category'].unique(), default=df['Category'].unique()
)
df_filtered = df[df['Category'].isin(category_filter)]

# Layout: 2 columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    fig, ax = plt.subplots()
    sns.barplot(data=df_filtered, x='Category', y='Sales', estimator=sum, hue='Category', palette='viridis', legend=False, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Sales by Region")
    fig, ax = plt.subplots()
    sns.barplot(data=df_filtered, x='Region', y='Sales', estimator=sum, hue='Region', palette='coolwarm', legend=False, ax=ax)
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Profit Distribution")
    fig, ax = plt.subplots()
    sns.histplot(data=df_filtered, x='Profit', bins=40, color='darkorange', kde=True, ax=ax)
    st.pyplot(fig)

with col4:
    st.subheader("Discount vs Profit")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df_filtered, x='Discount', y='Profit', hue='Category', alpha=0.6, ax=ax)
    ax.axhline(0, color='red', linestyle='--')
    st.pyplot(fig)

st.subheader("Monthly Sales Trend over Time")
monthly_sales = df_filtered.groupby(df_filtered['Order Date'].dt.to_period('M'))['Sales'].sum()
fig, ax = plt.subplots(figsize=(12,4))
monthly_sales.plot(color='crimson', linewidth=2, marker='o', ax=ax)
ax.set_ylabel("Sales")
st.pyplot(fig)

st.subheader("Key Insights")
st.markdown("""
- **Technology leads in total sales**, crossing 800,000.
- **West region leads** in sales; **South region trails** behind.
- **Discount is a major driver of losses** — higher discounts correlate strongly with negative profit, especially in Technology.
- **Sales show seasonality** with year-end peaks and overall growth from 2015 to 2017.
""")
