import pandas as pd

df = pd.read_csv("data/student_performance.csv")

print(df.head())
X = df.drop(
    ['StudentID', 'FinalExamScore'],
    axis=1
)

y = df['FinalExamScore']

print("Features Shape:", X.shape)
print("Target Shape:", y.shape)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Trained Successfully!")
predictions = model.predict(X_test)

print(predictions[:5])
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

r2 = r2_score(
    y_test,
    predictions
)

print("\nModel Evaluation")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)
import joblib

joblib.dump(model, "student_model.pkl")

print("Model saved successfully!")
