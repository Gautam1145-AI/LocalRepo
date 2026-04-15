import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/cleaned_sales.csv')
engine = create_engine('sqlite:///sales.db')
df.to_sql('sales', engine, if_exists='replace', index=False)
print('Loaded to database')
