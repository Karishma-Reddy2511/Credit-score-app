# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample synthetic data
data = {
    'age': [25, 45, 35, 50, 23, 52, 36, 27, 48, 33],
    'income': [300000, 800000, 500000, 1000000, 250000, 1100000, 600000, 320000, 950000, 550000],
    'loan_amount': [100000, 200000, 150000, 300000, 50000, 250000, 175000, 80000, 230000, 160000],
    'credit_score': [650, 720, 680, 790, 600, 810, 700, 640, 750, 690],
    'employment_years': [2, 10, 5, 20, 1, 18, 6, 3, 15, 4],
    'eligible': ['yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes']
}

df = pd.DataFrame(data)

# Label encode
le = LabelEncoder()
df['eligible'] = le.fit_transform(df['eligible'])

# Split and scale
X = df.drop('eligible', axis=1)
y = df['eligible']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model & tools
pickle.dump(model, open("credit_model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))
pickle.dump(le, open("label_encoder.pkl", "wb"))

print("✅ Model, Scaler, and Label Encoder saved successfully!")
