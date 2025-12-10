import pandas as pd

# Load CSV
IEP_df = pd.read_csv("2025_formatted1.csv")

num_rows = IEP_df.shape[0]
print(f"Number of rows before cleaning: {num_rows}")

IEP_df_interpolated = IEP_df.interpolate()

IEP_df = IEP_df.dropna()

num_rows_new = IEP_df.shape[0]
print(f"Number of rows after cleaning: {num_rows_new}")


# Count columns
num_columns = len(IEP_df.columns)
print('Number of columns in IEP_df:', num_columns)