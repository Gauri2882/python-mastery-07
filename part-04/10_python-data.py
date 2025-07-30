""" Loading and exploring sales data """

import pandas as pd
import matplotlib.pyplot as plt

# load sales data
data = pd.read_csv("part-04/sales_data.csv")
print(f"\nfew rows:\n {data.head()}")

# summary of dataset
print(f"\nsummary of dataset:")
data.info()

# statistical summary
print(f"\nstatistical summary:\n{data.describe()}")

# check for missing values
print(f"\nmissing values:\n{data.isnull().sum()}")

# fill missing values
data["Product_Category"] = data['Product_Category'].fillna("Unknown")

# drop rows with missing values
data = data.dropna()

# convert data column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# convert data column to numeric format
data['Sales_Amount'] = pd.to_numeric(data['Sales_Amount'], errors = 'coerce')

# feature engineering : adding new field based on existing data
data['Year_Month'] = data['Date'].dt.to_period('M')

# add a revenue column 
data['Revenue'] = data['Quantity'] * data['Price']


# total sales by month
monthly_sales = data.groupby('Year_Month')['Sales_Amount'].sum()
print(f"\nMonthly sales:\n{monthly_sales}")

# top products 
top_products = data.groupby('Product Name')['Revenue'].sum().sort_values(ascending= False).head(5)
print(f"\nTop 5 products sold:\n{top_products}")

# plot monthly sales
monthly_sales.plot(kind = "bar", figsize= (10, 6), color = "skyblue")
plt.title("Monthly sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation = 45)
plt.show()

