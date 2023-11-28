import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import dataMergin

# connect to DB
url = 'mysql+mysqlconnector://root:amirouche1602@localhost:3306/sales_2019'
engine = create_engine(url)
conn = engine.connect()
dataMergin.jan.to_sql(name='january',con=conn,index=False,if_exists='replace')
dataMergin.feb.to_sql(name='february',con=conn,index=False,if_exists='replace')
dataMergin.mar.to_sql(name='march',con=conn,index=False,if_exists='replace')
dataMergin.apr.to_sql(name='april',con=conn,index=False,if_exists='replace')
dataMergin.may.to_sql(name='may',con=conn,index=False,if_exists='replace')
dataMergin.jun.to_sql(name='june',con=conn,index=False,if_exists='replace')
dataMergin.jul.to_sql(name='july',con=conn,index=False,if_exists='replace')
dataMergin.aug.to_sql(name='august',con=conn,index=False,if_exists='replace')
dataMergin.sep.to_sql(name='september',con=conn,index=False,if_exists='replace')
dataMergin.oct.to_sql(name='october',con=conn,index=False,if_exists='replace')
dataMergin.nov.to_sql(name='november',con=conn,index=False,if_exists='replace')
dataMergin.dec.to_sql(name='december',con=conn,index=False,if_exists='replace')

