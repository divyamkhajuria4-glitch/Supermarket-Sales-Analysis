# SuperMarket Sales Analysis using NumPy

## 📌 Project Overview

This project analyzes supermarket sales data using **NumPy** to understand sales performance, customer behavior, payment methods, product lines, cities, branches, and customer ratings.

The main goal of this project is to practice **NumPy, data analysis, Boolean masking, aggregation, and data visualization** on a real-world dataset.

---

## 🎯 Objective

The objective of this project is to:

* Analyze overall sales performance
* Analyze sales by product line
* Compare different payment methods
* Analyze sales by gender
* Compare Member and Normal customers
* Analyze sales across different cities
* Analyze branch-wise sales
* Study customer rating distribution
* Create meaningful visualizations

---

## 🛠️ Technologies Used

* **Python**
* **NumPy** — Data analysis and numerical calculations
* **Pandas** — Reading the CSV dataset
* **Matplotlib** — Data visualization

---

## 📂 Project Structure

```text
Supermarket-Sales_Analysis/
│
├── SuperMarket Analysis copy.csv
├── Supermarket_analysis.py
├── visualizations.py
├── README.md
└── .venv/
```

---

## 📊 Dataset

The dataset contains **1,000 supermarket transactions**.

Important columns include:

* Invoice ID
* Branch
* City
* Customer type
* Gender
* Product line
* Unit price
* Quantity
* Tax 5%
* Sales
* Date
* Time
* Payment
* COGS
* Gross income
* Rating

---

## 🔎 Analysis Performed

### 1. Overall Sales Analysis

Calculated:

* Total Sales
* Average Sales
* Median Sales
* Minimum Sales
* Maximum Sales
* Standard Deviation

### 2. Product Line Analysis

For each product line, calculated:

* Total Sales
* Average Sales
* Total Quantity Sold

### 3. Payment Method Analysis

Analyzed:

* Number of transactions
* Total Sales
* Average Sales
* Total Quantity Sold

Payment methods include:

* Cash
* Credit Card
* Ewallet

### 4. Gender Analysis

Compared:

* Total Sales
* Average Sales
* Total Quantity Sold

between male and female customers.

### 5. Customer Type Analysis

Compared:

* Member customers
* Normal customers

using:

* Total Sales
* Average Sales
* Total Quantity Sold

### 6. City Analysis

Analyzed:

* Total Sales
* Average Sales
* Total Quantity Sold

for each city.

### 7. Branch Analysis

Analyzed branch-wise:

* Total Sales
* Average Sales
* Total Quantity Sold

### 8. Rating Analysis

Calculated:

* Average Rating
* Median Rating
* Minimum Rating
* Maximum Rating
* Rating Standard Deviation

Ratings were also divided into:

* High Rating: `>= 8`
* Medium Rating: `5 to < 8`
* Low Rating: `< 5`

---

## 📈 Visualizations

The project includes the following visualizations:

1. Product Line-wise Total Sales
2. Payment Method-wise Total Sales
3. Gender-wise Total Sales
4. Customer Type-wise Total Sales
5. City-wise Total Sales
6. Rating Distribution
7. Sales Distribution

All visualizations were created using **Matplotlib**.

---

## 🧠 NumPy Concepts Practiced

This project helped practice several important NumPy concepts:

* NumPy Arrays
* `shape`
* `size`
* `ndim`
* `np.sum()`
* `np.mean()`
* `np.median()`
* `np.min()`
* `np.max()`
* `np.std()`
* Boolean Masking
* Conditional Filtering
* `np.where()`
* `np.unique()`
* `return_counts`
* Sorting
* Array Slicing
* Broadcasting
* Axis-based Aggregation
* `np.argmax()`
* `np.argmin()`

---

## 💡 Key Skills Demonstrated

Through this project, I practiced:

* Data loading
* Data cleaning basics
* NumPy-based data analysis
* Boolean masking
* Conditional analysis
* Statistical analysis
* Category-wise analysis
* Data aggregation
* Data visualization
* Python loops and logic building

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd Supermarket-Sales_Analysis
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Run the analysis

```bash
python Supermarket_analysis.py
```

### 5. Run the visualizations

```bash
python visualizations.py
```

---

## 🚫 Libraries Not Used

To keep the project focused on NumPy practice:

* No Seaborn
* No Scikit-learn
* No SciPy
* No Pandas `groupby()`
* No Pandas `pivot_table()`
* No Pandas `describe()`
* No Pandas `value_counts()`

NumPy was used for the main numerical analysis.

---

## 📚 Learning Purpose

This is a **learning and portfolio project** created to strengthen Python and NumPy skills through practical data analysis.

The project focuses on understanding the logic behind data analysis rather than relying on high-level Pandas functions.

---

## 👨‍💻 Author

**Divyam Khajuria**

B.Tech Computer Science Graduate
Aspiring AI Engineer

---

## ⭐ Future Improvements

Possible future improvements include:

* Adding more advanced visualizations
* Creating an interactive dashboard
* Adding automated insights
* Improving project documentation
* Extending the analysis with machine learning in a separate project

