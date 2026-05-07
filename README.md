# E-commerce Operations KPI Project

## Project Overview

This project uses the Online Retail dataset to build a practical KPI reporting pipeline for entry-level and junior analyst, reporting, BI, and operations-analytics roles.

The aim is to take raw retail transaction data and turn it into clean, reporting-ready datasets that can support KPI analysis for revenue, orders, cancellations, customer coverage, and product or country performance.

## Business Goal

Turn raw online retail transaction data into a reliable KPI reporting workflow for sales, orders, cancellations, customer coverage, and product/country performance.

## Problem Statement

The raw dataset is not ready for decision-making because it contains missing values, cancellations, duplicate records, inconsistent product entries, invalid transaction values, and dates stored as text.

This project cleans and structures the data so that core business KPIs can be analysed more reliably.

## Tools Used

- Python
- pandas
- matplotlib
- SQLite
- SQL
- Git and GitHub

## Project Structure

- `data/`
- `docs/`
- `reports/`
- `sql/`
- `src/`

## Current Progress

The core KPI reporting pipeline is complete.

The project now:
- loads and cleans the raw Online Retail dataset
- creates reporting-ready sales and customer analysis outputs
- loads the cleaned sales dataset into SQLite
- calculates key business KPIs using SQL
- generates chart outputs for monthly revenue and country-level revenue
- summarises the main findings in a final business report

## Current Output Files

The cleaning script generates these files locally:

- `data/master_flagged_retail.csv`
- `data/sales_only_retail.csv`
- `data/customer_eligible_retail.csv`
- `data/data_quality_summary.csv`

These generated CSV files are not committed to GitHub because data outputs are excluded in `.gitignore`.

## Cleaning Notes

A short explanation of the cleaning rules used in the project is available in:

- `reports/data_cleaning_notes.md`

## Key KPIs

- Total Revenue
- Total Orders
- Average Order Value
- Cancellation Count
- Cancellation Rate
- Monthly Revenue Trend
- Top Products by Revenue
- Top Countries by Revenue
- Active Customer Count
- Revenue per Customer

## Current Limitation

Customer-level analysis is limited by missing `CustomerID` values in the source data, so customer KPIs only cover the identifiable subset of transactions rather than the full dataset.

## Reporting Outputs

The project includes two simple chart outputs created with Python, pandas, and matplotlib:

- `reports/charts/monthly_revenue_trend.png`
- `reports/charts/top_countries_by_revenue.png`

The monthly revenue trend chart shows how revenue changes over time and highlights the strongest trading month in the dataset.

The top countries chart shows revenue by country and highlights the concentration of revenue in the United Kingdom.

A final business summary is available in:

- `reports/final_summary.md`

## Next Steps

Potential future improvements include:
- export SQL KPI outputs into dedicated reporting tables or CSV files
- add automated validation checks for key KPI totals
- build a simple dashboard using the validated KPI outputs
- compare UK and non-UK revenue performance in more detail
