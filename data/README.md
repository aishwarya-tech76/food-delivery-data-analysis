# 🍔 Food Delivery Data Analysis

## 📌 Project Overview

This project analyzes food delivery order data to understand customer behavior, sales performance, food preferences, payment methods, delivery performance, and order trends.

An interactive dashboard has been developed using Python and Streamlit to visualize important business insights.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze overall food delivery sales performance
- Identify top-selling food categories and items
- Understand customer ordering behavior
- Analyze preferred payment methods
- Study delivery time and order status
- Identify sales trends over time
- Analyze customer ratings
- Create an interactive dashboard for business insights

---

## 📊 Dataset Description

The dataset contains food delivery order information.

### Important Columns

| Column | Description |
|---|---|
| Order_ID | Unique order identification |
| Order_Date | Date of the order |
| Customer_ID | Unique customer identification |
| Customer_Name | Customer name |
| City | Customer/order city |
| Restaurant | Restaurant name |
| Category | Food category |
| Item | Food item |
| Quantity | Quantity ordered |
| Price | Price per item |
| Total_Amount | Total order amount |
| Payment_Mode | Payment method |
| Delivery_Time_Min | Delivery time in minutes |
| Order_Status | Order status |
| Rating | Customer rating |

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Streamlit
- Plotly
- Matplotlib
- VS Code
- CSV Dataset

---

## 🔄 Data Analysis Process

### 1. Data Collection
The food delivery dataset was collected in CSV format.

### 2. Data Cleaning
The dataset was checked for:

- Missing values
- Incorrect data types
- Duplicate records
- Date formatting
- Invalid values

### 3. Exploratory Data Analysis

The following areas were analyzed:

- Total sales
- Total orders
- Total quantity
- Average order value
- Category performance
- Item performance
- Payment mode
- City-wise performance
- Delivery time
- Order status
- Customer ratings
- Monthly trends

### 4. Dashboard Development

An interactive Streamlit dashboard was created to display:

- Key Performance Indicators
- Sales trends
- Category analysis
- Payment analysis
- Order status
- Delivery performance
- Customer/order data
- Interactive filters

---

## 📈 Key Business Questions

1. What is the total revenue generated?
2. How many orders were placed?
3. Which food category generates the highest sales?
4. Which food items are most popular?
5. Which payment mode is most preferred?
6. Which city has the highest number of orders?
7. What is the average delivery time?
8. What percentage of orders are cancelled?
9. What is the average customer rating?
10. How does sales performance change over time?

---

## 💡 Business Insights

## 💡 Business Insights

Based on the analysis of 1,000 food delivery orders, the following insights were identified:

- Total revenue generated was **₹6,17,576**.
- A total of **1,000 orders** were recorded.
- The total quantity of food items sold was **2,533**.
- The average order value was approximately **₹617.58**.
- **Pizza** was the highest revenue-generating category with sales of **₹1,35,183**.
- **Paneer Pizza** was the top-selling item by sales with revenue of **₹44,264**.
- **UPI** was the most preferred payment method with **351 orders**.
- **Nagpur** recorded the highest number of orders with **215 orders**.
- The average delivery time was approximately **42 minutes**.
- The overall order cancellation rate was **23.8%**.
- The average customer rating was approximately **4.01 out of 5**.
- **September** recorded the highest monthly sales with revenue of **₹63,446**.

### Business Recommendations

Based on these findings:

- The business can promote high-performing **Pizza** products.
- **Paneer Pizza** can be given more promotional focus because of its strong sales performance.
- UPI payment support should continue to be prioritized.
- Delivery operations can be improved to reduce the average delivery time.
- The company should investigate the reasons behind the **23.8% cancellation rate**.
- Customer feedback and ratings can be analyzed further to improve service quality.
---

## 📊 Dashboard

The project includes an interactive Streamlit dashboard where users can filter and analyze food delivery data.

Users can explore the data using different filters and visualizations.

---

## 🚀 How to Run the Project

### Step 1: Open the project

Open the project folder in VS Code.

### Step 2: Activate virtual environment

```powershell
.\venv\Scripts\Activate.ps1