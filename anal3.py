import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import anal1

y_axis = anal1.data_df['Order Date'].str.split(' ')[0:].apply(lambda x :x[1][0:2]).value_counts()
serie = pd.DataFrame(y_axis)
x_axis = serie.index
serie = serie.rename(columns={'count':'Count'})
y = serie
print(serie['Count'])
# Order Date
# 19    12886       Top Hours
# 12    12573
# 11    12392
# 18    12263
# 20    12218        
# 13    12115       


plt.plot(x_axis,serie['Count'])
plt.xlabel('Hours')
plt.ylabel('Bought Products')
plt.title('Behavior of Bought Products per hour ')


plt.show()
