import pandas as pd 
import numpy as np

data = pd.read_csv('all_sales.csv')
data_df = pd.DataFrame(data)
# print(data['Quantity Ordered'].dtype)         int64
# print(data['Price Each'].dtype)               float64

# adding Total Sales Column
data_df['Total Sales'] = data_df['Price Each'] * data_df['Quantity Ordered']

filt1 = data_df['Month'] == 'February'
Months = ['January','February','March','April','May','June','July','August','September','October','November','December']
SumPerMonth = {}
filt = 'Month' == 'January'

for i in Months :
    filt = data_df['Month'] == i
    SumPerMonth[i] = data_df.loc[filt,'Total Sales'].sum()

SumPerMonth_Serie = pd.Series(SumPerMonth)
# print(SumPerMonth_Serie.max())          #Best Month : December with 4614149.48 




