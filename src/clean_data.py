import pandas as pd
import re

# -----------------------------
# File paths
# -----------------------------
RAW_FILE = "data/Online Retail.csv"
MASTER_OUTPUT = "data/master_flagged_retail.csv"
SALES_OUTPUT = "data/sales_only_retail.csv"
CUSTOMER_OUTPUT = "data/customer_eligible_retail.csv"
DQ_SUMMARY_OUTPUT = "data/data_quality_summary.csv"

# -----------------------------
# Load raw data
# -----------------------------
df = pd.read_csv(RAW_FILE, encoding="ISO-8859-1")

print("Raw dataset loaded.")
print(f"Initial rows: {len(df):,}")
print(f"Initial columns: {df.shape[1]}")
print()

# -----------------------------
# Standardise column types
# -----------------------------
df["InvoiceNo"] = df["InvoiceNo"].astype(str).str.strip()
df["StockCode"] = df["StockCode"].astype(str).str.strip()
df["Description"] = df["Description"].astype("string").str.strip()
df["Country"] = df["Country"].astype(str).str.strip()

# CustomerID should stay nullable
df["CustomerID"] = pd.to_numeric(df["CustomerID"], errors="coerce")

# Convert date safely using the dataset's known format
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], format="%d/%m/%Y %H:%M", errors="coerce"
)

# -----------------------------
# Remove only rows that are truly unusable
# -----------------------------
initial_rows = len(df)

invalid_date_rows = df["InvoiceDate"].isna().sum()
missing_quantity_rows = df["Quantity"].isna().sum()
missing_unitprice_rows = df["UnitPrice"].isna().sum()

df = df.dropna(subset=["InvoiceDate", "Quantity", "UnitPrice"]).copy()

rows_after_required_drops = len(df)

# -----------------------------
# Remove exact duplicates
# -----------------------------
duplicate_rows = df.duplicated().sum()
df = df.drop_duplicates().copy()

rows_after_dedup = len(df)

# -----------------------------
# Create revenue before filtering into subsets
# -----------------------------
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# -----------------------------
# Create flags
# -----------------------------
df["is_cancelled"] = df["InvoiceNo"].str.startswith("C")
df["is_negative_qty"] = df["Quantity"] < 0
df["is_zero_or_negative_price"] = df["UnitPrice"] <= 0
df["is_missing_customer_id"] = df["CustomerID"].isna()
df["is_missing_description"] = (
    df["Description"].isna() | (df["Description"].str.strip() == "")
)

# -----------------------------
# Classify stock code type
# Simple rule:
# standard_product = digits only
# non_standard = anything else
# -----------------------------
def classify_stockcode(stockcode: str) -> str:
    if pd.isna(stockcode):
        return "unknown"
    stockcode = str(stockcode).strip()
    if re.fullmatch(r"\d+", stockcode):
        return "standard_product"
    return "non_standard"


df["stockcode_type"] = df["StockCode"].apply(classify_stockcode)

# -----------------------------
# Add time dimensions
# -----------------------------
df["invoice_date"] = df["InvoiceDate"].dt.date
df["year"] = df["InvoiceDate"].dt.year
df["month"] = df["InvoiceDate"].dt.month
df["year_month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
df["weekday"] = df["InvoiceDate"].dt.day_name()

# -----------------------------
# Save master dataset
# -----------------------------
df.to_csv(MASTER_OUTPUT, index=False)

# -----------------------------
# Build sales-only dataset
# Gross paid sales logic
# -----------------------------
sales_df = df[
    (~df["is_cancelled"])
    & (df["Quantity"] > 0)
    & (df["UnitPrice"] > 0)
    & (df["stockcode_type"] == "standard_product")
].copy()

sales_df.to_csv(SALES_OUTPUT, index=False)

# -----------------------------
# Build customer-eligible dataset
# -----------------------------
customer_df = sales_df[~sales_df["is_missing_customer_id"]].copy()
customer_df.to_csv(CUSTOMER_OUTPUT, index=False)

# -----------------------------
# Data quality summary
# -----------------------------
summary_rows = [
    {"metric": "initial_rows", "value": initial_rows},
    {"metric": "invalid_date_rows_removed", "value": int(invalid_date_rows)},
    {"metric": "missing_quantity_rows_removed", "value": int(missing_quantity_rows)},
    {"metric": "missing_unitprice_rows_removed", "value": int(missing_unitprice_rows)},
    {"metric": "exact_duplicate_rows_removed", "value": int(duplicate_rows)},
    {"metric": "master_rows_final", "value": len(df)},
    {"metric": "cancelled_rows_in_master", "value": int(df["is_cancelled"].sum())},
    {"metric": "negative_quantity_rows_in_master", "value": int(df["is_negative_qty"].sum())},
    {
        "metric": "zero_or_negative_price_rows_in_master",
        "value": int(df["is_zero_or_negative_price"].sum()),
    },
    {
        "metric": "missing_customer_id_rows_in_master",
        "value": int(df["is_missing_customer_id"].sum()),
    },
    {
        "metric": "missing_description_rows_in_master",
        "value": int(df["is_missing_description"].sum()),
    },
    {
        "metric": "non_standard_stockcode_rows_in_master",
        "value": int((df["stockcode_type"] == "non_standard").sum()),
    },
    {"metric": "sales_only_rows", "value": len(sales_df)},
    {"metric": "customer_eligible_rows", "value": len(customer_df)},
    {"metric": "sales_only_revenue", "value": round(sales_df["Revenue"].sum(), 2)},
    {
        "metric": "customer_eligible_revenue",
        "value": round(customer_df["Revenue"].sum(), 2),
    },
]

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(DQ_SUMMARY_OUTPUT, index=False)

# -----------------------------
# Customer coverage metrics
# -----------------------------
sales_revenue = sales_df["Revenue"].sum()
customer_revenue = customer_df["Revenue"].sum()
customer_revenue_coverage = (
    (customer_revenue / sales_revenue * 100) if sales_revenue != 0 else 0
)

# -----------------------------
# Terminal output
# -----------------------------
print("Cleaning pipeline complete.")
print()
print("Files created:")
print(f"- {MASTER_OUTPUT}")
print(f"- {SALES_OUTPUT}")
print(f"- {CUSTOMER_OUTPUT}")
print(f"- {DQ_SUMMARY_OUTPUT}")
print()
print("Row counts:")
print(f"Master dataset rows: {len(df):,}")
print(f"Sales-only rows: {len(sales_df):,}")
print(f"Customer-eligible rows: {len(customer_df):,}")
print()
print("Revenue summary:")
print(f"Sales-only revenue: GBP {sales_revenue:,.2f}")
print(f"Customer-eligible revenue: GBP {customer_revenue:,.2f}")
print(f"Customer revenue coverage: {customer_revenue_coverage:.2f}%")
