# Data Cleaning Notes

## Purpose

The purpose of the cleaning step is to turn the raw Online Retail transaction data into reporting-ready datasets that can support KPI analysis more reliably.

## Key Cleaning Rules

- Converted `InvoiceDate` into a proper datetime field.
- Standardised key text fields such as `InvoiceNo`, `StockCode`, `Description`, and `Country`.
- Converted `CustomerID` to numeric while allowing missing values.
- Removed rows missing essential fields needed for reporting: `InvoiceDate`, `Quantity`, or `UnitPrice`.
- Removed exact duplicate rows.
- Created a `Revenue` column as `Quantity * UnitPrice`.
- Flagged important data conditions including cancelled invoices, negative quantities, zero or negative prices, missing customer IDs, missing descriptions, and non-standard stock codes.
- Added reporting-ready date fields including `invoice_date`, `year`, `month`, and `year_month`.

## Output Datasets Created

- `data/master_flagged_retail.csv`: main cleaned dataset with flags and derived fields
- `data/sales_only_retail.csv`: sales-focused dataset excluding cancelled rows, non-positive quantity or price rows, and non-standard stock codes
- `data/customer_eligible_retail.csv`: subset of sales-only data where `CustomerID` is available
- `data/data_quality_summary.csv`: summary of row removals, flags, and revenue coverage

## Main Limitation

Customer-level analysis is limited by missing `CustomerID` values in the source data. This means customer KPIs only reflect the subset of transactions where a customer identifier is present.
