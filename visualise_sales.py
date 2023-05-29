import matplotlib.pyplot as plt

# Import the sales data from calculate_total_sales.py
from calculate_total_sales import get_sales_data

# Get the sales data
sales_data = get_sales_data

# Extract the categories and total sales from the sales data
categories = [item[0] for item in sales_data]
total_sales = [item[1] for item in sales_data]

# Create a bar chart to visualize the sales by category
plt.bar(categories, total_sales)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales by Category")
plt.xticks(rotation=45)

# Display the chart
plt.show()
