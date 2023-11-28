import pandas as pd

# Assuming your DataFrame is named 'df' and contains columns 'Product' and 'Quantity Ordered'
# Example DataFrame
data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'B', 'A', 'B'],
    'Quantity Ordered': [19, 1, 3, 2, 1, 4, 2, 3, 1, 2]
}

df = pd.DataFrame(data)

# Group by 'Product' and sum the 'Quantity Ordered' for each product
most_sold_products = df.groupby('Product')['Quantity Ordered'].sum()

# Display the result
print(most_sold_products)
