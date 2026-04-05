# Import pandas library for data handling
import pandas as pd

# Load the dataset (latin1 encoding is used to avoid text errors)
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Display first 5 rows of the dataset
print(df.head())

#ANALYSIS 1: Top 5 profitable products
# Group data by Product Name, sum Profit, sort descending, show top 5
print(df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head())

#ANALYSIS 2: Discount vs Profit (IMPORTANT - Discount Trap)
# Group by Sub-Category and calculate average Discount and Profit
print(df.groupby("Sub-Category")[["Discount","Profit"]].mean().sort_values(by="Profit", ascending=False))


#Same as above but not printed (can remove or keep for practice)
df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head()

#ANALYSIS 3: Total Sales by Region
df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

#ANALYSIS 4: Total Profit by Region
df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

#ANALYSIS 5: Region Sales vs Profit (IMPORTANT)
# Helps find regions with high sales but low profit
region_data = df.groupby("Region")[["Sales","Profit"]].sum()
print(region_data.sort_values(by="Sales", ascending=False))

#VISUALIZATION: Discount vs Profit Scatter Plot
# Shows relationship between discount and profit
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x="Discount", y="Profit", data=df)
plt.show()


#DATA CLEANING: Check missing values
print(df.isnull().sum())


#DATA CLEANING: Check duplicate rows
print(df.duplicated().sum())


#FEATURE ENGINEERING: Convert Order Date to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create new column 'Month' from Order Date
df["Month"] = df["Order Date"].dt.to_period("M")


#ANALYSIS 6: Monthly Sales Trend
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

# Plot monthly sales trend
monthly_sales.plot()
plt.show()


#FEATURE ENGINEERING: Profit Margin
# Profit Margin = Profit / Sales
df["Profit Margin"] = df["Profit"] / df["Sales"]

# Analyze profit margin by sub-category
df.groupby("Sub-Category")["Profit Margin"].mean().sort_values()


#ANALYSIS 7: Total Profit by Sub-Category
category_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values()
print(category_profit)


#ANALYSIS 8: Sales by Customer Segment
segment_sales = df.groupby("Segment")["Sales"].sum()
print(segment_sales)


#SAVE CLEANED DATASET for Power BI
df.to_csv("clean_superstore.csv", index=False)