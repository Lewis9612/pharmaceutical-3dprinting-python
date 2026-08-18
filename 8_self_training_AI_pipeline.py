from sklearn.linear_model import LinearRegression
import pandas as pd

print("--- AUTONOMOUS QUALITY CONTROL ---")

collected_data = []

while True:
    infill_percentage = float(input("Infill percentage: "))
    print_temperature = float(input("Print temperature: "))
    disintegration_time = float(input("Disintegration time: "))
    data = {
        "Infill Percentage": infill_percentage,
        "Print Temerature": print_temperature,
        "Disintegration Time": disintegration_time
    }
    collected_data.append(data)
    next_entry = input("Another entry? (yes / no): ")
    if next_entry == "no":
        break
    elif next_entry == "yes":
        continue

df = pd.DataFrame(collected_data)

X = df[["Infill Percentage", "Print Temerature"]]
Y = df[["Disintegration Time"]]

model = LinearRegression()

model.fit(X, Y) 

new_infill = float(input("Enter target print infill percentage (%): "))
new_temp = float(input("Enter target print temperature (C): "))

untested_test_case = [[new_infill, new_temp]]
predicted = model.predict(untested_test_case)

print(f"The predicted disintegration time: {predicted[0][0]:.2f} minute")
