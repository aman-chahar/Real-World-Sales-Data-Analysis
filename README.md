# Exploratory data analysis of Sales dataset
This project aims to analyze sales data from a real-world dataset. It performs various data cleaning, manipulation, and analysis tasks to gain insights into the sales performance, customer behavior, and product popularity. The analysis is performed using Python and the pandas library. The key questions addressed in this project are:

The project begins by importing the necessary libraries, pandas, and os.

Read the 12 CSV files and concatinate them into a single file,then read data from a "all_data.csv" file and displays the first few rows to provide an overview of the data (186822, 6).
### Task 1: Clean up the data
This section focuses on data cleaning tasks such as removing rows with missing values, filtering out irrelevant data, and converting column data types for further analysis. 
### Task 2: Add Month Column
adds a "Month" column to the dataset for grouping sales data by month.
### Task 3: Add a sales column
A "Sales" column is added to the dataset to calculate the total sales for each order.
### Task 4: Add a city column
Creates a "City" column by extracting city and state information from the purchase address.
### Question 1: What was the best month for sales? How much was earned that month?
Groupby the sales data by month, created bar chart using Matplotlib.

Insights:- Heighest sales recorded in December, Total Sales for december month crossed 4.5 million USD.
### Question 2: What City has the highest number of Sales ?
Groupby the sales data by city, created bar chart using Matplotlib.

Insights:- San Francisco (CA) has the heighest sales.
### Question 3: What time should we display advertisements to maximize likelihood of customer's buying product ?
Convert the "Order date" to time using datetime. and Groupby the number of order by "Hour".

Insights:- We should display advertisements Between 11am to 12 noon and between 6 to 7 PM to maximize likelihood of customer's buying product
### Question 4: What products are most often sold together ?
Filtering the rows with duplicate 'Order ID'(indicating that multiple products were ordered together in the same order) values, a new column 'Grouped' is created in the DataFrame. This column contain the names of products that were ordered together in the same order.

The Top 10 most common orders are as follows:

[(('iPhone', 'Lightning Charging Cable'), 1005),
 (('Google Phone', 'USB-C Charging Cable'), 987),
 (('iPhone', 'Wired Headphones'), 447),
 (('Google Phone', 'Wired Headphones'), 414),
 (('Vareebadd Phone', 'USB-C Charging Cable'), 361),
 (('iPhone', 'Apple Airpods Headphones'), 360),
 (('Google Phone', 'Bose SoundSport Headphones'), 220),
 (('USB-C Charging Cable', 'Wired Headphones'), 160),
 (('Vareebadd Phone', 'Wired Headphones'), 143),
 (('Lightning Charging Cable', 'Wired Headphones'), 92)]
 ### Question 5: What product sold the most ? Why do you think it sold the most ?
 Groupby the products with the mean of product price. And created a bar chart of products with their mean price and number of quantity prdered.
  
  Insights:- Batteries have the heighest sales and their prics is low.
 
  Macbook pro laptop have low sales as its price is too high.
 
  As I can see, the items with less price have high sales and vice-versa.

### Conclusion
The project provides valuable insights into sales data, helping businesses make informed decisions about their products and marketing strategies.
 
