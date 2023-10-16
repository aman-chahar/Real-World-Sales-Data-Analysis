# Exploratory data analysis of Sales dataset
This project aims to analyze sales data from a real-world dataset. It performs various data cleaning, manipulation, and analysis tasks to gain insights into the sales performance, customer behavior, and product popularity. The analysis is performed using Python and the pandas library. The key questions addressed in this project are:

The project begins by importing the necessary libraries, pandas, and os.
Read the 12 CSV files and concatinate them into a single file,then read data from a "all_data.csv" file and displays the first few rows to provide an overview of the data (186822, 6).
## Task 1: Clean up the data
This section focuses on data cleaning tasks such as removing rows with missing values, filtering out irrelevant data, and converting column data types for further analysis (186305 entries).
#   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Order ID          185950 non-null  object 
 1   Product           185950 non-null  object 
 2   Quantity Ordered  185950 non-null  int64  
 3   Price Each        185950 non-null  float64
 4   Order Date        185950 non-null  object 
 5   Purchase Address  185950 non-null  object
 
## Task 2: Add Month Column
adds a "Month" column to the dataset for grouping sales data by month.
## Task 3: Add a sales column
A "Sales" column is added to the dataset to calculate the total sales for each order.
## Task 4: Add a city column
Creates a "City" column by extracting city and state information from the purchase address.
## Question 1: What was the best month for sales? How much was earned that month?
The project calculates and visualizes monthly sales to identify the best month for sales.
