import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("📊 Retail Sales Analytics Dashboard")
st.markdown("Interactive dashboard summarizing key findings from the Superstore dataset analysis.")

st.header("Data Visualization")

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

st.header("Predictive Modeling")

tab1, tab2 = st.tabs(["Classification: Profitability", "Regression: Sales Prediction"])

with tab1:
    st.subheader("Model Comparison - Predicting Profitability")
    model_results = pd.DataFrame({
        'Model': ['Logistic Regression', 'KNN', 'Random Forest', 'Decision Tree'],
        'Accuracy': [0.942, 0.9375, 0.936, 0.930],
        'AUC': [0.98, 0.94, 0.97, 0.93]
    })
    st.dataframe(model_results)
    
    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(data=model_results, x='Model', y='AUC', hue='Model', palette='viridis', legend=False, ax=ax)
    ax.set_title('AUC Score by Model')
    ax.set_ylim(0.8, 1.0)
    st.pyplot(fig)
    
    st.markdown("**Best model:** Logistic Regression (94.2% accuracy, 0.98 AUC)")

with tab2:
    st.subheader("Model Comparison - Predicting Sales Amount")
    reg_results = pd.DataFrame({
        'Model': ['Linear Regression', 'Decision Tree', 'Random Forest', 'Gradient Boosting', 'XGBoost', 'SVR', 'KNN'],
        'R2': [0.1863, 0.0920, 0.1963, 0.2233, 0.1717, -0.0098, 0.1049],
        'RMSE': [693.28, 732.36, 689.02, 677.35, 699.48, 772.34, 727.16]
    })
    st.dataframe(reg_results)
    
    fig, ax = plt.subplots(figsize=(9,4))
    sns.barplot(data=reg_results, x='Model', y='R2', hue='Model', palette='coolwarm', legend=False, ax=ax)
    ax.set_title('R² Score by Model')
    plt.xticks(rotation=30)
    st.pyplot(fig)
    
    st.markdown("**Best model:** Gradient Boosting (R² = 0.2233) — though overall R² is modest, suggesting Sales is hard to predict from these features alone.")

st.header("Exploratory Data Analysis")

fig, ax = plt.subplots(figsize=(7,5))
corr_matrix = df[['Sales', 'Profit', 'Discount', 'Quantity']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)

st.markdown("""
**Key relationships:** Sales-Profit correlation is 0.48 (moderate positive); 
Discount-Profit is -0.22 (moderate negative) — heavier discounting tends to erode profit.
""")

subcat_profit = df.groupby('Sub-Category')['Profit'].mean().sort_values(ascending=False).round(2)
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Top 5 Sub-Categories by Profit**")
    st.dataframe(subcat_profit.head(5))
with col2:
    st.markdown("**Bottom 5 Sub-Categories by Profit**")
    st.dataframe(subcat_profit.tail(5))
# Mean vs Median comparison chart
category_stats = df.groupby('Category')[['Profit']].agg(['mean', 'median']).round(2)
category_stats.columns = ['Mean Profit', 'Median Profit']

fig, ax = plt.subplots(figsize=(8,5))
category_stats.plot(kind='bar', ax=ax, color=['#4C72B0', '#DD8452'])
ax.set_title('Mean vs Median Profit by Category')
ax.set_ylabel('Profit')
plt.xticks(rotation=0)
st.pyplot(fig)

st.markdown("""
**Notice the gap:** mean profit is consistently higher than median profit across 
every category — a sign that a small number of large orders are pulling the 
average up, while most individual orders earn less than the mean suggests.
""")

# Skewness distributions
fig, axes = plt.subplots(1, 2, figsize=(12,4))
sns.histplot(df['Sales'], bins=40, color='steelblue', kde=True, ax=axes[0])
axes[0].set_title(f"Sales Distribution (Skewness: {df['Sales'].skew():.2f})")
sns.histplot(df['Profit'], bins=40, color='darkorange', kde=True, ax=axes[1])
axes[1].set_title(f"Profit Distribution (Skewness: {df['Profit'].skew():.2f})")
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
**Both distributions are heavily right-skewed** — most orders cluster near small 
values, with a handful of large orders stretching the tail far to the right. This 
is consistent with the modest R² scores seen in the regression modeling tab above.
""")

st.markdown("*See the Discount vs Profit relationship in the Predictive Modeling section above — this stage's correlation analysis (-0.22) confirms that visual pattern numerically.*")

