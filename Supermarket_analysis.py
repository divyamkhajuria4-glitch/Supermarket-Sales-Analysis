# ==========================================
# SuperMarket Sales Analysis using NumPy
# ==========================================

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# Load Dataset
# ==========================================

supermarket = pd.read_csv("SuperMarket Analysis copy.csv")

print(supermarket.head())
print(supermarket.shape)
print(supermarket.columns)


# ==========================================
# Convert Important Columns to NumPy Arrays
# ==========================================

sales = supermarket["Sales"].to_numpy()
quantity = supermarket["Quantity"].to_numpy()
payment = supermarket["Payment"].to_numpy()
product_line = supermarket["Product line"].to_numpy()
gender = supermarket["Gender"].to_numpy()
rating = supermarket["Rating"].to_numpy()
customer_type = supermarket["Customer type"].to_numpy()

print(sales.shape)
print(quantity.shape)
print(payment.shape)
print(product_line.shape)
print(gender.shape)



# ==========================================
# Overall Sales Analysis
# ==========================================

print("\nOverall Sales Analysis")

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Median Sales:", np.median(sales))
print("Minimum Sales:", np.min(sales))
print("Maximum Sales:", np.max(sales))
print("Sales Standard Deviation:", np.std(sales))


# ==========================================
# Product Line Analysis
# ==========================================

unique_product_lines = np.unique(product_line)

print("\nProduct Line Analysis")

for product in unique_product_lines:

    mask = product_line == product

    total_sales = np.sum(sales[mask])
    average_sales = np.mean(sales[mask])
    total_quantity = np.sum(quantity[mask])

    print("\nProduct Line:", product)
    print("Total Sales:", total_sales)
    print("Average Sales:", average_sales)
    print("Total Quantity:", total_quantity)




# ==========================================
# Payment Method Analysis
# ==========================================

unique_payment = np.unique(payment)

print("\nPayment Method Analysis")

for method in unique_payment:

    mask = payment == method

    transaction_count = np.sum(mask)
    total_sales = np.sum(sales[mask])
    average_sales = np.mean(sales[mask])
    total_quantity = np.sum(quantity[mask])

    print("\nPayment Method:", method)
    print("Transactions:", transaction_count)
    print("Total Sales:", total_sales)
    print("Average Sales:", average_sales)
    print("Total Quantity:", total_quantity) 



# ==========================================
# Gender Analysis
# ==========================================

unique_gender = np.unique(gender)

print("\nGender Analysis")

for g in unique_gender:

    mask = gender == g

    total_sales = np.sum(sales[mask])
    average_sales = np.mean(sales[mask])
    total_quantity = np.sum(quantity[mask])

    print("\nGender:", g)
    print("Total Sales:", total_sales)
    print("Average Sales:", average_sales)
    print("Total Quantity:", total_quantity)



    # ==========================================
# Customer Type Analysis
# ==========================================

unique_customer_type = np.unique(customer_type)

print("\nCustomer Type Analysis")

for customer in unique_customer_type:

    mask = customer_type == customer

    total_sales = np.sum(sales[mask])
    average_sales = np.mean(sales[mask])
    total_quantity = np.sum(quantity[mask])

    print("\nCustomer Type:", customer)
    print("Total Sales:", total_sales)
    print("Average Sales:", average_sales)
    print("Total Quantity:", total_quantity)




    # ==========================================
# City Analysis
# ==========================================

city = supermarket["City"].to_numpy()
unique_city = np.unique(city)

print("\nCity Analysis")

for c in unique_city:

    mask = city == c

    total_sales = np.sum(sales[mask])
    average_sales = np.mean(sales[mask])
    total_quantity = np.sum(quantity[mask])

    print("\nCity:", c)
    print("Total Sales:", total_sales)
    print("Average Sales:", average_sales)
    print("Total Quantity:", total_quantity)




    # ==========================================
# Branch Analysis
# ==========================================

branch = supermarket["Branch"].to_numpy()
unique_branch = np.unique(branch)

print("\nBranch Analysis")

for b in unique_branch:

    mask = branch == b

    total_sales = np.sum(sales[mask])
    average_sales = np.mean(sales[mask])
    total_quantity = np.sum(quantity[mask])

    print("\nBranch:", b)
    print("Total Sales:", total_sales)
    print("Average Sales:", average_sales)
    print("Total Quantity:", total_quantity)



# ==========================================
# Rating Analysis
# ==========================================

print("\nRating Analysis")

print("Average Rating:", np.mean(rating))
print("Median Rating:", np.median(rating))
print("Minimum Rating:", np.min(rating))
print("Maximum Rating:", np.max(rating))
print("Rating Standard Deviation:", np.std(rating))


# Rating Categories

high_rating = rating >= 8
medium_rating = (rating >= 5) & (rating < 8)
low_rating = rating < 5

print("\nRating Categories")

print("Ratings >= 8:", np.sum(high_rating))
print("Ratings 5 to <8:", np.sum(medium_rating))
print("Ratings < 5:", np.sum(low_rating))





# ==========================================
# Key Insights
# ==========================================

print("\n==========================================")
print("KEY INSIGHTS")
print("==========================================")


# ------------------------------------------
# Highest and Lowest Sales Product Line
# ------------------------------------------

product_sales = []

for product in unique_product_lines:

    mask = product_line == product
    total_sales = np.sum(sales[mask])

    product_sales.append(total_sales)


highest_product_index = np.argmax(product_sales)
lowest_product_index = np.argmin(product_sales)

print(
    "Highest Sales Product Line:",
    unique_product_lines[highest_product_index]
)

print(
    "Lowest Sales Product Line:",
    unique_product_lines[lowest_product_index]
)


# ------------------------------------------
# Highest Sales Payment Method
# ------------------------------------------

payment_sales = []

for method in unique_payment:

    mask = payment == method
    total_sales = np.sum(sales[mask])

    payment_sales.append(total_sales)


highest_payment_index = np.argmax(payment_sales)

print(
    "Highest Sales Payment Method:",
    unique_payment[highest_payment_index]
)


# ------------------------------------------
# Most Used Payment Method
# ------------------------------------------

payment_counts = []

for method in unique_payment:

    mask = payment == method
    count = np.sum(mask)

    payment_counts.append(count)


most_used_payment_index = np.argmax(payment_counts)

print(
    "Most Used Payment Method:",
    unique_payment[most_used_payment_index]
)


# ------------------------------------------
# Highest Sales Gender
# ------------------------------------------

gender_sales = []

for g in unique_gender:

    mask = gender == g
    total_sales = np.sum(sales[mask])

    gender_sales.append(total_sales)


highest_gender_index = np.argmax(gender_sales)

print(
    "Highest Sales Gender:",
    unique_gender[highest_gender_index]
)


# ------------------------------------------
# Highest Sales Customer Type
# ------------------------------------------

customer_sales = []

for customer in unique_customer_type:

    mask = customer_type == customer
    total_sales = np.sum(sales[mask])

    customer_sales.append(total_sales)


highest_customer_index = np.argmax(customer_sales)

print(
    "Highest Sales Customer Type:",
    unique_customer_type[highest_customer_index]
)


# ------------------------------------------
# Highest Sales City
# ------------------------------------------

city_sales = []

for c in unique_city:

    mask = city == c
    total_sales = np.sum(sales[mask])

    city_sales.append(total_sales)


highest_city_index = np.argmax(city_sales)

print(
    "Highest Sales City:",
    unique_city[highest_city_index]
)


# ------------------------------------------
# Highest Sales Branch
# ------------------------------------------

branch_sales = []

for b in unique_branch:

    mask = branch == b
    total_sales = np.sum(sales[mask])

    branch_sales.append(total_sales)


highest_branch_index = np.argmax(branch_sales)

print(
    "Highest Sales Branch:",
    unique_branch[highest_branch_index]
)


# ------------------------------------------
# Rating Insights
# ------------------------------------------

print(
    "Average Customer Rating:",
    np.mean(rating)
)

print(
    "Highest Customer Rating:",
    np.max(rating)
)

print(
    "Lowest Customer Rating:",
    np.min(rating)
)


# ------------------------------------------
# Most Common Product Line
# ------------------------------------------

product_counts = []

for product in unique_product_lines:

    mask = product_line == product
    count = np.sum(mask)

    product_counts.append(count)


most_common_product_index = np.argmax(product_counts)

print(
    "Most Common Product Line:",
    unique_product_lines[most_common_product_index]
)


print("==========================================")
