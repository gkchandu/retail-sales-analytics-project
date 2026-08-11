# Retail Sales Analytics Pipeline

🔗 **Live Dashboard:** [View Interactive Dashboard](https://retail-sales-analytics-project-dashboard.streamlit.app)

An end-to-end data science project analyzing retail sales data — from data cleaning and visualization to predictive modeling and business insights.

## 📊 Dataset
**Superstore Dataset** ([Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final))
Contains order-level retail data including sales, profit, discount, category, region, and order dates (2014-2017).

## 🎯 Project Goals
This project follows a full data science pipeline across four phases:
1. **Data Cleaning & Visualization** — clean the dataset and uncover initial patterns
2. **Predictive Modeling** — build and evaluate ML models on the cleaned data
3. **Exploratory Data Analysis** — deeper statistical analysis and correlation study
4. **Real-World Application** — apply the full pipeline to derive business recommendations

## 🛠️ Tools & Libraries
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Google Colab
- Streamlit *(for interactive dashboards)*

## 📁 Project Structure
```
retail-sales-analytics-project/
├── 01_Data_Cleaning_and_Visualization.ipynb
├── 02_Predictive_Modeling.ipynb
├── 03_Exploratory_Data_Analysis.ipynb
├── 04_Real_World_Application.ipynb
├── app.py                          # Streamlit dashboard
├── requirements.txt                # Dashboard dependencies
├── Sample - Superstore.csv         # Dataset
└── README.md
```

## 1: Data Cleaning & Visualization

**What was done:**
- Checked and confirmed no missing values or duplicate rows in the dataset
- Fixed data types (converted Order Date, Ship Date to datetime)
- Identified profit outliers using boxplot analysis
- Built visualizations: Sales by Category, Sales by Region, Profit distribution, Monthly sales trend, Discount vs Profit

**Key Findings:**
- Technology leads total sales (800,000+), followed closely by Furniture and Office Supplies
- West region leads in sales (700,000+); South region trails behind (under 400,000)
- Sales show strong year-end seasonality with overall growth from 2015 to 2017 (peak: 2017 at 118,447)
- Higher discounts are strongly linked to losses — orders with 70-80% discount are almost always unprofitable, especially in the Technology category

## 2: Predictive Modeling

**What was done:**
- **Task 1 (Classification):** Predicted whether an order is Profitable (Yes/No) using Logistic Regression, Decision Tree, Random Forest, and KNN
- **Task 2 (Regression):** Predicted actual Sales amount using Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost, SVR, and KNN

**Key Findings:**
- **Task 1:** Logistic Regression performed best (94.2% accuracy, 0.98 AUC), followed closely by Random Forest (0.97 AUC). The dataset is imbalanced (80.6% profitable orders), making AUC a more reliable metric than accuracy alone.
- **Task 2:** Gradient Boosting performed best (R² = 0.2233), though all models showed modest R² scores overall — suggesting Sales amount is difficult to predict precisely from order-level features alone (Discount, Category, Region, etc.) without additional data like unit pricing or historical demand.
- A log-transform experiment on Task 2's target improved SVR and KNN specifically, but slightly reduced performance for tree-based models — an interesting example of how preprocessing choices affect different model types differently.

**Why both tasks:** Classification tells us *whether* an order is profitable; regression tells us *how much* it's worth. Together, they give a more complete picture than either alone.

## 3: Exploratory Data Analysis

**What was done:**
- Calculated statistical summaries, correlation matrices, and skewness for key numeric variables
- Compared mean vs median Profit/Sales across Categories and Regions
- Built a Category × Region pivot table for Sales
- Identified top and bottom performing Sub-Categories by average profit

**Key Findings:**
- Sales and Profit are both extremely right-skewed (skewness of 12.97 and 7.56 
respectively), confirming a small number of large orders drive most of the variation
- Mean profit is consistently 2-3x higher than median profit across every category and region, showing outliers distort simple averages
- **Copiers** is an extreme outlier, averaging ~15x more profit than the next best Sub-Category, while **Tables** loses money on average (-55.57)
- Discount's relationship with Profit is non-linear — profit holds steady up to ~20% discount, then drops sharply beyond 50%

## 4: Real-World Business Case Study

**What was done:**
- Framed a real business question: where should the company focus to improve 
overall profitability?
- Analyzed profitability by Customer Segment, simulated the impact of capping 
discounts at different thresholds, built a Sub-Category action list, and created 
an inventory planning framework (velocity x margin)
- Applied the **profitability classification model** (built during the predictive modeling stage) to hypothetical new orders to 
demonstrate real-time business use

**Key Findings:**
- Capping discounts at **40%** would have avoided an estimated **99,558** in 
losses across **933** orders
- **Tables, Bookcases, and Supplies** consistently lose money and are candidates 
for pricing review; **Binders** sells in high volume but at a negative margin
- **Copiers** is a high-value, low-turnover product — 15x more profitable than 
the next-best Sub-Category, but shouldn't be bulk-stocked
- **Home Office** segment has the highest margin (14.3%) despite the lowest 
discount rate — segment-specific discount strategy may outperform a uniform policy

**Full business case study, including executive summary and recommendations, is 
available in the notebook.**

## 👤 Author
*[G K Chandrakala]* 
