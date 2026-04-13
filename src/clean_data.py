import pandas as pd

# Load raw dataset
file_path = "data/Online Retail.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Convert InvoiceDate from text to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], format="%d/%m/%Y %H:%M")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Create cancellation flag
df["IsCancelled"] = df["InvoiceNo"].astype(str).str.startswith("C")

# Create sales-only dataset excluding cancelled rows
sales_df = df[df["IsCancelled"] == False].copy()

# Save outputs
full_output_path = "data/cleaned_online_retail.csv"
sales_output_path = "data/cleaned_online_retail_sales_only.csv"

df.to_csv(full_output_path, index=False)
sales_df.to_csv(sales_output_path, index=False)

print("Day 8 cleaning step completed.")
print(f"Full cleaned file saved to: {full_output_path}")
print(f"Sales-only cleaned file saved to: {sales_output_path}")

print("\nCancellation summary:")
print(df["IsCancelled"].value_counts())

print("\nRow counts:")
print(f"All rows: {len(df)}")
print(f"Sales-only rows: {len(sales_df)}")

print("\nFirst 10 rows of full cleaned data:")
print(df.head(10))