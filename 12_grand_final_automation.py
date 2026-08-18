import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

# Features: [Infill %, Temp °C]
raw_data = [
    [10, 170], [15, 175], [20, 165], # Clearly Group A
    [80, 230], [85, 240], [90, 235]  # Clearly Group B
]

cluster_model = KMeans(n_clusters=2, random_state=42)
labels = cluster_model.fit_predict(raw_data)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(raw_data, labels)

infill = float(input("Infill (%): "))
temperature = float(input("Temperature: "))

test_case = [[infill, temperature]]
prediction = model.predict(test_case)
predicted_code = prediction[0]

print(f"\n[AI Decision] This new configuration belongs to Cluster Group: {predicted_code}")
