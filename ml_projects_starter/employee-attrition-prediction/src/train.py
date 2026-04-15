import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib, os

df = pd.read_csv('data/employee_attrition.csv').dropna()

for col in df.select_dtypes(include='object').columns:
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop('Attrition', axis=1)
y = df['Attrition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("Saved model")
