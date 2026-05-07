-- KPI 1: Total Revenue
-- Purpose: Calculate total gross revenue from the sales_only_retail table

SELECT ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales_only_retail;


-- KPI 2: Total Orders
-- Purpose: Count distinct orders using InvoiceNo

SELECT COUNT(DISTINCT InvoiceNo) AS total_orders
FROM sales_only_retail;

-- KPI 3: Average Order Value
-- Purpose: Calculate average revenue per order

SELECT ROUND(SUM(Revenue) / COUNT(DISTINCT InvoiceNo), 2) AS average_order_value
FROM sales_only_retail;


-- KPI 4: Monthly Revenue Trend
-- Purpose: Show revenue by year-month for trend analysis

SELECT
    year_month,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM sales_only_retail
GROUP BY year_month
ORDER BY year_month;

-- KPI 5: Top Countries by Revenue
-- Purpose: Rank countries by total revenue

SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales_only_retail
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;

-- KPI 6: Top Products by Revenue
-- Purpose: Rank products by total revenue using StockCode and Description

SELECT
    StockCode,
    Description,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales_only_retail
GROUP BY StockCode, Description
ORDER BY total_revenue DESC
LIMIT 10;

-- KPI 7: Cancellation Count
-- Purpose: Count rows flagged as cancelled in the master dataset

SELECT COUNT(*) AS cancellation_count
FROM master_flagged_retail
WHERE is_cancelled = 1;


-- KPI 8: Cancellation Rate
-- Purpose: Measure the percentage of rows in the master dataset flagged as cancelled

SELECT ROUND(
    100.0 * SUM(CASE WHEN is_cancelled = 1 THEN 1 ELSE 0 END) / COUNT(*),
    2
) AS cancellation_rate_percent
FROM master_flagged_retail;
