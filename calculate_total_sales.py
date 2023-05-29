# This script calculates the total
# sales for each category.

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="root123@", database="superstore"
)

cursor = connection.cursor()

query = """
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales_by_category
GROUP BY Category;
"""

cursor.execute(query)

results = cursor.fetchall()

# Store sales data in a list of tuples
sales_data = []
for row in results:
    category = row[0]
    total_sales = row[1]
    sales_data.append((category, total_sales))

# Close cursor and connection
cursor.close()
connection.close()

# Return the sales data
get_sales_data = sales_data
