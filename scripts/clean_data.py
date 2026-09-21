import pandas as pd

# Read raw dataset
input_file = "data/raw/RS_Session_255_AU_1231.1.csv"

df = pd.read_csv(input_file)

# Remove SI. No.
df = df.drop(columns=["SI. No."])

# Convert wide format to long format
df_clean = df.melt(
    id_vars=["District"],
    var_name="Financial_Year",
    value_name="Expenditure_Crore"
)

# Clean Financial Year names
df_clean["Financial_Year"] = (
    df_clean["Financial_Year"]
    .str.extract(r"(FY \d{4}-\d{2})")[0]
    .str.replace("FY ", "", regex=False)
)

# Convert expenditure to numeric
df_clean["Expenditure_Crore"] = pd.to_numeric(
    df_clean["Expenditure_Crore"],
    errors="coerce"
)

# Sort data
df_clean = df_clean.sort_values(
    ["District", "Financial_Year"]
)

# Save processed dataset
output_file = "data/processed/mgnrega_expenditure_clean.csv"

df_clean.to_csv(output_file, index=False)

print("Data cleaning completed successfully!")
print(f"Rows: {len(df_clean)}")
print(f"Columns: {len(df_clean.columns)}")
print("\nFirst 10 rows:")
print(df_clean.head(10))
