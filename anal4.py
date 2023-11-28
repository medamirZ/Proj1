import pandas as pd
import numpy as np
import anal1
from collections import Counter

# getting Products's Groups
proudct_grp = anal1.data_df.groupby(by='Product')
usb_c_charging_cable = proudct_grp.get_group('USB-C Charging Cable')
lighting_charging_cable = proudct_grp.get_group('Lightning Charging Cable')
AAA_Batteries_4 = proudct_grp.get_group('AAA Batteries (4-pack)')
AA_Batteries_4 = proudct_grp.get_group('AA Batteries (4-pack)')
wired_headphones = proudct_grp.get_group('Wired Headphones')
apple_airpods = proudct_grp.get_group('Apple Airpods Headphones')
bose_sound_sport = proudct_grp.get_group('Bose SoundSport Headphones')
fhd_monitor_27 = proudct_grp.get_group('27in FHD Monitor')
iphone = proudct_grp.get_group('iPhone')
gaming_monitor_4k =  proudct_grp.get_group('27in 4K Gaming Monitor')
ultrawide_monitor_34 = proudct_grp.get_group('34in Ultrawide Monitor')
google_phone = proudct_grp.get_group('Google Phone')
flat_screen_tv = proudct_grp.get_group('Flatscreen TV')
mac_book = proudct_grp.get_group('Macbook Pro Laptop')
thinkpad = proudct_grp.get_group('ThinkPad Laptop')
monitor_20 = proudct_grp.get_group('20in Monitor')
vareebaad_phone = proudct_grp.get_group('Vareebadd Phone')
lg_washing_machine = proudct_grp.get_group('LG Washing Machine')
lg_dryer = proudct_grp.get_group('LG Dryer')



# Assuming anal1 is the instance of your analysis class and data_df is the DataFrame
# containing the 'Product' column.

product_groups_total = {
    'USB-C Charging Cable': '',
    'Lightning Charging Cable': '',
    'AAA Batteries (4-pack)': '',
    'AA Batteries (4-pack)': '',
    'Wired Headphones': '',
    'Apple Airpods Headphones': '',
    'Bose SoundSport Headphones': '',
    '27in FHD Monitor': '',
    'iPhone': '',
    '27in 4K Gaming Monitor': '',
    '34in Ultrawide Monitor': '',
    'Google Phone': '',
    'Flatscreen TV': '',
    'Macbook Pro Laptop': '',
    'ThinkPad Laptop': '',
    '20in Monitor': '',
    'Vareebadd Phone': '',
    'LG Washing Machine': '',
    'LG Dryer': ''
}


product_groups_total['USB-C Charging Cable'] = usb_c_charging_cable['Quantity Ordered'].value_counts().sum()
product_groups_total['Lightning Charging Cable'] = lighting_charging_cable['Quantity Ordered'].value_counts().sum()
product_groups_total['AAA Batteries (4-pack)'] = AAA_Batteries_4['Quantity Ordered'].value_counts().sum()
product_groups_total['AA Batteries (4-pack)'] = AA_Batteries_4['Quantity Ordered'].value_counts().sum()
product_groups_total['Wired Headphones'] = wired_headphones['Quantity Ordered'].value_counts().sum()
product_groups_total['Apple Airpods Headphones'] = apple_airpods['Quantity Ordered'].value_counts().sum()
product_groups_total['Bose SoundSport Headphones'] = bose_sound_sport['Quantity Ordered'].value_counts().sum()
product_groups_total['27in FHD Monitor'] = fhd_monitor_27['Quantity Ordered'].value_counts().sum()
product_groups_total['iPhone'] = iphone['Quantity Ordered'].value_counts().sum()
product_groups_total['27in 4K Gaming Monitor'] = gaming_monitor_4k['Quantity Ordered'].value_counts().sum()
product_groups_total['34in Ultrawide Monitor'] = ultrawide_monitor_34['Quantity Ordered'].value_counts().sum()
product_groups_total['Google Phone'] = google_phone['Quantity Ordered'].value_counts().sum()
product_groups_total['Flatscreen TV'] = flat_screen_tv['Quantity Ordered'].value_counts().sum()
product_groups_total['Macbook Pro Laptop'] = mac_book['Quantity Ordered'].value_counts().sum()
product_groups_total['ThinkPad Laptop'] = thinkpad['Quantity Ordered'].value_counts().sum()
product_groups_total['20in Monitor'] = monitor_20['Quantity Ordered'].value_counts().sum()
product_groups_total['Vareebadd Phone'] = vareebaad_phone['Quantity Ordered'].value_counts().sum()
product_groups_total['LG Washing Machine'] = lg_washing_machine['Quantity Ordered'].value_counts().sum()
product_groups_total['LG Dryer'] = lg_dryer['Quantity Ordered'].value_counts().sum()

Toserie = pd.Series(product_groups_total)
# print(Toserie)
# print(anal1.data_df['Product'].value_counts())

# imagine i did all that just to get same results between 
# pandas value counts and grouping data by products and multiplying it by quantity ordrer:| 

proudcct_grp = anal1.data_df.groupby(by='Product')['Quantity Ordered'].sum().sort_values(ascending=False)
print(proudcct_grp)

# well this works and it shows the real counts (Quantity Ordered * Product )

# Most Sold Products :  
# AAA Batteries (4-pack)        30986
# AA Batteries (4-pack)         27611
# USB-C Charging Cable          23931