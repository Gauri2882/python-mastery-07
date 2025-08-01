"""Project: Sales Report Analyzer"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    "Load sales data from a CSV file"
    try:
        data = pd.read_csv(file_path)
        print("data loaded successfully")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None
    
def clean_data(data):
    "clean and preprocess data"
    print("\nCleaning data...")

    # fill missing values
    data['Product_Category'] = data['Product_Category'].fillna("Unknown")
    data = data.dropna()

    # convert columns
    data['Date'] = pd.to_datetime(data['Date'])
    data['Sales_Amount'] = pd.to_numeric(data['Sales_Amount'], errors = 'coerce')

    # add new columns
    data['Year_Month'] = data['Date'].dt.to_period('M')
    if 'Quantity' in data.columns and 'Price' in data.columns:
        data['Revenue'] = data['Quantity'] * data['Price']
    
    print("Data cleaned successfully")
    return data

def analyze_data(data):
    "Analyze and display insights from the data"
    print("\n---- Sales Insights ----")

    # total sales by month
    monthly_sales = data.groupby('Year_Month')['Sales_Amount'].sum()
    print("\nMonth Sales: ")
    print(monthly_sales)

    # top 5 products by revenue
    if 'Revenue' in data.columns:
        top_products = data.groupby('Product Name')['Revenue'].sum().sort_values(ascending = False).head(5)
        print("\nTop 5 products by revenue:")
        print(top_products)

    # visualize monthly sales
    monthly_sales.plot(kind = 'bar', figsize = (10,6), color = 'skyblue')
    plt.title("Monthly sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation = 45)
    plt.show()

def main():
    print("Welcome to the sales report analyzer")

    # load data
    file_path = input("Emter the path to your sales CSV file:")
    data = load_data(file_path)
    if data is None:
        return
    
    # clean data
    data = clean_data(data)

    # analyze data
    analyze_data(data)

if __name__ == "__main__":
    main()