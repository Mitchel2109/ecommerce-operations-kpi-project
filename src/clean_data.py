import pandas as pd

# Load raw dataset
file_path = "data/Online Retail.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Convert InvoiceDate from text to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], format="%d/%m/%Y %H:%M")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Save first cleaned version
output_path = "data/cleaned_online_retail.csv"
df.to_csv(output_path, index=False)

print("Cleaning step completed.")
print(f"Cleaned file saved to: {output_path}")
print("\nUpdated data types:")
print(df.dtypes)

print("\nFirst 10 rows of cleaned data:")
print(df.head(10))