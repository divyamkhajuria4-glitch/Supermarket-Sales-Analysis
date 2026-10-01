
# ==========================================
# SuperMarket Sales Analysis - Visualizations
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# Load Dataset
# ==========================================

supermarket = pd.read_csv("SuperMarket Analysis copy.csv")


# ==========================================
# Convert Columns to NumPy Arrays
# ==========================================

sales = supermarket["Sales"].to_numpy()
payment = supermarket["Payment"].to_numpy()
product_line = supermarket["Product line"].to_numpy()
gender = supermarket["Gender"].to_numpy()
customer_type = supermarket["Customer type"].to_numpy()
city = supermarket["City"].to_numpy()
rating = supermarket["Rating"].to_numpy()


# ==========================================
# 1. Product Line-wise Total Sales
# ==========================================

unique_product_lines = np.unique(product_line)
product_sales = []

for product in unique_product_lines:

    mask = product_line == product
    total_sales = np.sum(sales[mask])

    product_sales.append(total_sales)


plt.figure()
plt.bar(unique_product_lines, product_sales)

plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.title("Product Line-wise Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 2. Payment Method-wise Total Sales
# ==========================================

unique_payment = np.unique(payment)
payment_sales = []

for method in unique_payment:

    mask = payment == method
    total_sales = np.sum(sales[mask])

    payment_sales.append(total_sales)


plt.figure()
plt.bar(unique_payment, payment_sales)

plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.title("Payment Method-wise Total Sales")

plt.tight_layout()
plt.show()


# ==========================================
# 3. Gender-wise Total Sales
# ==========================================

unique_gender = np.unique(gender)
gender_sales = []

for g in unique_gender:

    mask = gender == g
    total_sales = np.sum(sales[mask])

    gender_sales.append(total_sales)


plt.figure()
plt.bar(unique_gender, gender_sales)

plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.title("Gender-wise Total Sales")

plt.tight_layout()
plt.show()


# ==========================================
# 4. Customer Type-wise Total Sales
# ==========================================

unique_customer_type = np.unique(customer_type)
customer_sales = []

for customer in unique_customer_type:

    mask = customer_type == customer
    total_sales = np.sum(sales[mask])

    customer_sales.append(total_sales)


plt.figure()
plt.bar(unique_customer_type, customer_sales)

plt.xlabel("Customer Type")
plt.ylabel("Total Sales")
plt.title("Customer Type-wise Total Sales")

plt.tight_layout()
plt.show()


# ==========================================
# 5. City-wise Total Sales
# ==========================================

unique_city = np.unique(city)
city_sales = []

for c in unique_city:

    mask = city == c
    total_sales = np.sum(sales[mask])

    city_sales.append(total_sales)


plt.figure()
plt.bar(unique_city, city_sales)

plt.xlabel("City")
plt.ylabel("Total Sales")
plt.title("City-wise Total Sales")

plt.tight_layout()
plt.show()


# ==========================================
# 6. Rating Distribution
# ==========================================

rating_values, rating_counts = np.unique(
    rating,
    return_counts=True
)


plt.figure()
plt.bar(rating_values, rating_counts)

plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Rating Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# 7. Sales Distribution
# ==========================================

plt.figure()
plt.hist(sales, bins=10)

plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# Completed
# ==========================================

print("\nAll visualizations completed successfully!")


