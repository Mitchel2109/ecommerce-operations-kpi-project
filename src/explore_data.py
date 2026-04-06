import pandas as pd

file_path = "data/Online Retail.csv"

df = pd.read_csv(file_path, encoding="ISO-8859-1")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nFirst 10 rows:")
print(df.head(10))