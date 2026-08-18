import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_absolute_error, r2_score

# Check if the mock dataset exists, if not, generate it automatically
filename = "printing_data.csv"
if not os.path.exists(filename):
    rng = np.random.default_rng(seed=42)
    n_samples = 100
    infill = rng.uniform(10, 90, n_samples)      # 10% to 90% infill
    temp = rng.uniform(170, 230, n_samples)      # 170°C to 230°C temperature
    
    # Disintegration increases with higher infill and decreases with higher temperature
    noise = rng.normal(0, 30, n_samples)
    disintegration_time = 120 + (infill * 8) - ((temp - 170) * 1.5) + noise
    disintegration_time = np.clip(disintegration_time, 30, None) # Min 30 seconds
    
    df_mock = pd.DataFrame({
        "Infill_Percent": infill,
        "Print_Temp": temp,
        "Disintegration_Time_Sec": disintegration_time
    })
    df_mock.to_csv(filename, index=False)
    print("Dataset generated successfully.")

# Load data
df = pd.read_csv("printing_data.csv")

# Separate features (X) and target (y)
X = df[["Infill_Percent", "Print_Temp"]]
Y = df[["Disintegration_Time_Sec"]]

# Split data (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, Y_train.values.ravel())

# Evaluate model
prediction = model.predict(X_test)
mae = mean_absolute_error(Y_test, prediction)
r2 = r2_score(Y_test, prediction)

print(f"Mean absolute error: {mae:.2f} seconds")
print(f"R2 score: {r2:.2f}")

# User input prediction
user_target_infill = float(input("Target infill (%): "))
user_target_temp = float(input("Target Temperature (°C): "))

user_input = [[user_target_infill, user_target_temp]]
new_prediction = model.predict(user_input)
predicted_code = new_prediction[0]

print(f"\nPredicted Disintegration Time: {predicted_code:.2f} seconds")
print(f"Which is approximately: {predicted_code / 60:.2f} minutes")
