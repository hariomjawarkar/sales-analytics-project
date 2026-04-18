import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('../data/sales_data.csv')

# Show first rows
print(df.head())

# Data Cleaning
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Total Sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()

# Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Visualization - Category Sales
plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../dashboard/category_sales.png')
plt.show()

# Visualization - Top Products
plt.figure()
top_products.plot(kind='bar')
plt.title("Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('../dashboard/top_products.png')
plt.show()
