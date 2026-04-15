import pandas as pd

df = pd.read_csv('data/extracted_sales.csv')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['order_date'] = pd.to_datetime(df['order_date'])
df.to_csv('data/cleaned_sales.csv', index=False)
print('Transformation complete')
