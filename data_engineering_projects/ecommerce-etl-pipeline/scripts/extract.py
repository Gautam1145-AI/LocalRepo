import pandas as pd

df = pd.read_csv('data/sales.csv')
print(df.head())
df.to_csv('data/extracted_sales.csv', index=False)
print('Extraction complete')
