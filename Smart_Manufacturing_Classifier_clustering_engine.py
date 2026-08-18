from sklearn.ensemble import RandomForestClassifier

X_train = [
    [20, 170, 10], #crunbling failure = 0
    [50, 190, 15], #perfect pass = 1
    [80, 230, 20], #burning degradation = 2
    [20, 165, 12], #Crumbling failure
    [60, 195, 15], #perfect pass
    [90, 240, 25] #burning degradation
]
y_train = [0, 1, 2, 0, 1, 2]

model = RandomForestClassifier(n_estimators=10, random_state=42)

model.fit(X_train, y_train)
infill = float(input("Infill: "))
temperature = float(input("Temperature: "))
speed = float(input("Speed: "))

test_case = [[infill, temperature, speed]]
prediction = model.predict(test_case)
predicted_code = prediction[0]

print("\n--- AI REASONING OUTPUT ---")
if predicted_code == 0:
    print("AI Prediction: CRUMBLING FAILURE. The print temperature is too low for the polymer mesh to fuse.")
elif predicted_code == 1:
    print("AI Prediction: PERFECT PASS! Optimal print settings achieved for this formulation.")
elif predicted_code == 2:
    print("AI Prediction: THERMAL DEGRADATION. Temperature too high; active pharmaceutical ingredient is burning.")
