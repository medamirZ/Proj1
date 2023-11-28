import anal1
import pandas as pd
from matplotlib import pyplot as plt

# mean sale       185.61
mean = anal1.data_df['Total Sales'].mean()
filt_mean = anal1.data_df['Total Sales'] == mean

# median sale     14.95     Lightning Charging Cable
median = anal1.data_df['Total Sales'].median()
filt_median = anal1.data_df['Total Sales'] == median

# max sale        1700.0    Macbook Pro Laptop
max = anal1.data_df['Price Each'].max()
filt_max = anal1.data_df['Total Sales'] == max

# min sale        2.99  AAA Batteries (4-pack)
min = anal1.data_df['Total Sales'].min()
filt_min = anal1.data_df['Total Sales'] == min

print(anal1.data_df[filt_min]['Product'].value_counts())