import pandas as pd

# Load CSV
IEP_df = pd.read_csv("2025_formatted1.csv")


IEP_df_dropped = IEP_df.drop(IEP_df.columns[[40, 41, 42]], axis = 1)

IEP_df_numeric = IEP_df_dropped.select_dtypes(include='number')

num_columns_numeric = len(IEP_df_numeric.columns)
print(f'number of numeric columns: {num_columns_numeric}')

IEP_df_interpolated = IEP_df_numeric.interpolate()

# IEP_df_final = pd.concat([IEP_df_interpolated, IEP_df_dropped.select_dtypes(exclude='number')],axis=1)

IEP_df_interpolated.to_csv("IEP_df_interpolated.csv")