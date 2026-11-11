# Data Analysis with NumPy and Pandas

# 1) NumPy array operations

# 1.1) Import the necessary libraries
import numpy as np
import pandas as pd

# 1.2) Create a NumPy array named "temperatures_w1"
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

# 1.3) Display shape, data type, and size
print("Shape:", temperatures_w1.shape)
print("Dtype:", temperatures_w1.dtype)
print("Size:", temperatures_w1.size)

# 1.4) Convert temperatures into Fahrenheit
temperatures_w1_f = (temperatures_w1 * 9 / 5) + 32

# 1.5) Calculate max, min, and mean temperatures
print("Max:", temperatures_w1.max())
print("Min:", temperatures_w1.min())
print("Mean:", temperatures_w1.mean())

# 1.6) Extract first three, last two, and middle three values
print("First 3:", temperatures_w1[:3])
print("Last 2:", temperatures_w1[-2:])
print("Middle 3:", temperatures_w1[2:5])

# 1.7) Create a 2D NumPy array named "temperatures"
temperatures = np.array(
    [
        [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
        [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1],
    ]
)

# 1.8) Display shape, data type, and size of the 2D array
print("2D Shape:", temperatures.shape)
print("2D Dtype:", temperatures.dtype)
print("2D Size:", temperatures.size)

# 1.9) Slicing operations on 2D array
print("Row 0:", temperatures[0])
print("Row 1:", temperatures[1])
print("Row 0, last 2:", temperatures[0, -2:])
print("Row 1, last 2:", temperatures[1, -2:])


# 2) Create a Pandas Series

# 2.1) Create a Pandas Series named "marks"
marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=["Rank1", "Rank2", "Rank3", "Rank4", "Rank5"],
    name="Marks",
)

# 2.2) Display the full "marks" Series
print(marks)

# 2.3) Display the first three elements of the "marks" Series
print(marks.iloc[:3])  

# 2.4) Display all elements of the "marks" Series shows all elements
print(marks)

# 2.5) Display elements greater than 90
print(marks[marks > 90])

# 2.6) Add 100 to the first element of the "marks" Series
marks.loc["Rank1"] = 100

# 2.7) Drop the last element of the "marks" Series
marks = marks.drop("Rank5")

# 2.8) Create a new Series named "cgpa" by dividing "marks" by 10
cgpa = marks / 10
print(cgpa)


# 3) Create a Pandas DataFrame

# 3.1) Create a Pandas DataFrame named "transactions"
transactions = pd.DataFrame({
    "TransactionID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "ProductCategory": [
        "Electronics",
        "Clothing",
        "Electronics",
        "Furniture",
        "Clothing",
        "Electronics",
        "Furniture",
        "Clothing",
        "Furniture",
        "Electronics",
    ],
    "Region": [
        "North",
        "South",
        "North",
        "East",
        "West",
        "North",
        "East",
        "West",
        "South",
        "North",
    ],
    "Amount": [200, 150, 300, 450, 200, 250, 300, 180, 350, 400],
})

# 3.2) Display first five rows of the DataFrame
print(transactions.head())

# 3.3) Display shape, column names, and data types
print("Shape:", transactions.shape)
print("Columns:", transactions.columns.tolist())
print("Data Types:\n", transactions.dtypes)

# 3.4) Display "ProductCategory" and "Amount" columns
print(transactions[["ProductCategory", "Amount"]])

# 3.5) Display last three columns of the DataFrame
print(transactions.iloc[:, -3:])

# 3.6) Filter Region == "North" and Amount > 200
print(
    transactions[
        (transactions["Region"] == "North") & (transactions["Amount"] > 200)
    ]
)

# 3.7) Display frequency counts of "ProductCategory" Included descriptive output print statement
print(transactions["ProductCategory"].value_counts())

# 3.8) Display unique values in "Region"
print(transactions["Region"].unique())

# 3.9) Mean "Amount" for each "Region"
print(transactions.groupby("Region")["Amount"].mean())

# 3.10) Update "Amount" for TransactionID 102 to 165
transactions.loc[transactions["TransactionID"] == 102, "Amount"] = 165

# 3.11) Add "Discount" column (10% of Amount)
transactions["Discount"] = transactions["Amount"] * 0.10

# 3.12) Remove transaction with TransactionID 109
transactions = transactions[transactions["TransactionID"] != 109].copy()

# 3.13) Drop the "Discount" column
transactions = transactions.drop(columns=["Discount"])