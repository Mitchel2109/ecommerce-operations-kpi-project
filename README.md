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
- SQL
- GitHub

## Project Structure

- `data/`
- `docs/`
- `reports/`
- `sql/`
- `src/`

## Current Progress

The data cleaning stage is complete and has been validated.

The cleaning pipeline currently:
- loads the raw Online Retail dataset
- standardises key fields
- converts `InvoiceDate` into a usable datetime field
- creates a `Revenue` column
- removes unusable rows and exact duplicates
- creates business and data-quality flags
- creates reporting-ready time fields
- produces separate cleaned outputs for different analysis purposes

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

## Next Steps

The next stage of the project is to:
- load the cleaned data into SQL
- write KPI queries
- generate reporting outputs
- summarise findings in a short business-style report