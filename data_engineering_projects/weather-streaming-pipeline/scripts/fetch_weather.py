import requests
import pandas as pd
from datetime import datetime

API_KEY = 'your_api_key'
CITY = 'Jaipur'

url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(url)
data = response.json()

record = {
    'city': CITY,
    'temperature': data['main']['temp'],
    'humidity': data['main']['humidity'],
    'timestamp': datetime.now()
}

df = pd.DataFrame([record])
df.to_csv('data/weather_data.csv', mode='a', header=False, index=False)
print('Weather fetched')
