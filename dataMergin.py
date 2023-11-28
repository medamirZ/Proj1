import pandas as pd
import numpy as np

jan = pd.read_csv('Sales_January_2019.csv')
feb = pd.read_csv('Sales_February_2019.csv')
mar = pd.read_csv('Sales_March_2019.csv')
apr = pd.read_csv('Sales_April_2019.csv')
may = pd.read_csv('Sales_May_2019.csv')
jun = pd.read_csv('Sales_June_2019.csv')
jul = pd.read_csv('Sales_July_2019.csv')
aug = pd.read_csv('Sales_August_2019.csv')
sep = pd.read_csv('Sales_september_2019.csv')
oct = pd.read_csv('Sales_October_2019.csv')
nov = pd.read_csv('Sales_November_2019.csv')
dec = pd.read_csv('Sales_December_2019.csv')

# adding Month Column
jan['Month'] = 'January'
feb['Month'] = 'February'
mar['Month'] = 'March'
apr['Month'] = 'April'
may['Month'] = 'May'
jun['Month'] = 'June'
jul['Month'] = 'July'
aug['Month'] = 'August'
sep['Month'] = 'September'
oct['Month'] = 'October'
nov['Month'] = 'November'
dec['Month'] = 'December'

# save & write to csv 
jan.to_csv('Sales_January_2019.csv',index=False)
feb.to_csv('Sales_February_2019.csv',index=False)
mar.to_csv('Sales_March_2019.csv',index=False)
apr.to_csv('Sales_April_2019.csv',index=False)
may.to_csv('Sales_May_2019.csv',index=False)
jun.to_csv('Sales_June_2019.csv',index=False)
jul.to_csv('Sales_July_2019.csv',index=False)
aug.to_csv('Sales_August_2019.csv',index=False)
sep.to_csv('Sales_september_2019.csv',index=False)
oct.to_csv('Sales_October_2019.csv',index=False)
nov.to_csv('Sales_November_2019.csv',index=False)
dec.to_csv('Sales_December_2019.csv',index=False)


