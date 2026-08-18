from sklearn.linear_model import LinearRegression 
import pandas as pd

# Features: [Infill %, Print Temp]
training_features = [
    [20, 180],
    [50, 190],
    [80, 200],
    [20, 210],
    [50, 180]
]
# Target: Disintegration Time in Minutes
observed_disintegration_times = [10.5, 42.0, 115.0, 22.5, 31.0]

model = LinearRegression()
model.fit(training_features, observed_disintegration_times)

print("--- AI MODEL TRAINED SUCCESSFULLY ---")
user_infill = float(input("Enter target print infill percentage (%): "))
user_temp = float(input("Enter target print temperature (C): "))



untested_test_case = [[user_infill, user_temp]]
predicted = model.predict(untested_test_case)

print(f"\nPredicted distegration time: {predicted[0]:.2f} minutes")
