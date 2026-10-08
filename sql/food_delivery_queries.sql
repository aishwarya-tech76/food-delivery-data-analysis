-- 1. Total Number of Orders

SELECT COUNT(*) AS total_orders
FROM food_delivery;


-- 2. Total Gross Order Value

SELECT SUM(Total_Amount) AS total_revenue
FROM food_delivery;


-- 3. Total Quantity Sold

SELECT SUM(Quantity) AS total_quantity_sold
FROM food_delivery;


-- 4. Average Order Value

SELECT AVG(Total_Amount) AS average_order_value
FROM food_delivery;



-- 5. Category-wise Sales

SELECT
    Category,
    SUM(Total_Amount) AS total_sales
FROM food_delivery
GROUP BY Category
ORDER BY total_sales DESC;



-- 6. Top 5 Food Items by Sales

SELECT
    Item,
    SUM(Total_Amount) AS total_sales
FROM food_delivery
GROUP BY Item
ORDER BY total_sales DESC
LIMIT 5;



-- 7. Payment Mode Preference

SELECT
    Payment_Mode,
    COUNT(*) AS total_orders
FROM food_delivery
GROUP BY Payment_Mode
ORDER BY total_orders DESC;


-- 8. City-wise Orders

SELECT
    City,
    COUNT(*) AS total_orders
FROM food_delivery
GROUP BY City
ORDER BY total_orders DESC;


-- 9. Monthly Sales

SELECT
    EXTRACT(MONTH FROM Order_Date) AS month_number,
    SUM(Total_Amount) AS total_sales
FROM food_delivery
GROUP BY EXTRACT(MONTH FROM Order_Date)
ORDER BY month_number;



-- 10. Order Status Distribution

SELECT
    Order_Status,
    COUNT(*) AS total_orders
FROM food_delivery
GROUP BY Order_Status
ORDER BY total_orders DESC;



-- 11. Cancellation Rate

SELECT
    COUNT(CASE WHEN Order_Status = 'Cancelled' THEN 1 END) * 100.0
    / COUNT(*) AS cancellation_rate
FROM food_delivery;



-- 12. Average Delivery Time

SELECT
    AVG(Delivery_Time_Min) AS average_delivery_time
FROM food_delivery
WHERE Order_Status = 'Delivered';



-- 13. Average Customer Rating

SELECT
    AVG(Rating) AS average_rating
FROM food_delivery
WHERE Rating IS NOT NULL;



-- 14. Top 5 Customers by Purchase Value

SELECT
    Customer_ID,
    Customer_Name,
    SUM(Total_Amount) AS total_purchase_value
FROM food_delivery
GROUP BY Customer_ID, Customer_Name
ORDER BY total_purchase_value DESC
LIMIT 5;



-- 15. Top 10 Restaurants by Sales

SELECT
    Restaurant,
    SUM(Total_Amount) AS total_sales
FROM food_delivery
GROUP BY Restaurant
ORDER BY total_sales DESC
LIMIT 10;