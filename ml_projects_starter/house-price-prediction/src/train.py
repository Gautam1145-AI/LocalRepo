import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib, os

df = pd.read_csv('data/housing.csv').dropna()
df = pd.get_dummies(df, drop_first=True)

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("Saved model")
