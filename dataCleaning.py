import pandas as pd
import numpy as np

data = pd.read_csv('all_sales.csv')
data_df = pd.DataFrame(data)
filt = data_df.isna().any(axis=1)
data_df[filt].dropna(how='all')
print(data_df)


