import pandas as pd
import numpy as np
import anal1

# create city column
anal1.data_df['City'] = anal1.data_df['Purchase Address'].str.split(',').apply(lambda x: x[1][1:])

# grouping by city
cityGrp = anal1.data_df.groupby(by='City')
san_francisco = cityGrp.get_group(name='San Francisco')
Los_Angeles = cityGrp.get_group(name='Los Angeles')
New_york_city = cityGrp.get_group(name='New York City')
Boston = cityGrp.get_group(name='Boston')
Atlanta = cityGrp.get_group(name='Atlanta')
Dallas = cityGrp.get_group(name='Dallas')
Seattle = cityGrp.get_group(name='Seattle')
Portland = cityGrp.get_group(name='Portland')
Austin = cityGrp.get_group(name='Austin')

sumProduct = {}
# Getting City Groups
sumProduct['San Francisco'] =  san_francisco[['City','Product']].value_counts().sum()
sumProduct['Los Angeles'] =  Los_Angeles[['City','Product']].value_counts().sum()
sumProduct['New York City'] =  New_york_city[['City','Product']].value_counts().sum()
sumProduct['Boston'] =  Boston[['City','Product']].value_counts().sum()
sumProduct['Atlanta'] =  Atlanta[['City','Product']].value_counts().sum()
sumProduct['Dallas'] =  Dallas[['City','Product']].value_counts().sum()
sumProduct['Seattle'] =  Seattle[['City','Product']].value_counts().sum()
sumProduct['Portland'] =  Portland[['City','Product']].value_counts().sum()
sumProduct['Austin'] =  Austin[['City','Product']].value_counts().sum()

sumProductDf = pd.Series(sumProduct)
print(sumProductDf)             #Best City : San Francisco with : 44662