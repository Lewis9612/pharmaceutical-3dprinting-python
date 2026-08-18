import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Check if the mock dataset exists, if not, generate it automatically
filename = "tablet_weights.csv"
if not os.path.exists(filename):
    rng = np.random.default_rng(seed=42)
    # Generate 20 tablets with a mean of 150 mg and standard deviation of 8 mg
    mock_weights = rng.normal(loc=150, scale=8, size=20)
    df_mock = pd.DataFrame({"weight": mock_weights})
    df_mock.to_csv(filename, index=False)
    print(f"Generated new mock data and saved to {filename}")

# Load the weights
df = pd.read_csv(filename)

mean_weight = df["weight"].mean()
standard_deviation = df["weight"].std()
relative_standard_deviation = (standard_deviation / mean_weight) * 100

print(f"Mean weight (mg): {mean_weight:.2f}")
print(f"Standard deviation (mg): {standard_deviation:.2f}")
print(f"RSD (%): {relative_standard_deviation:.2f}")

# Define Warning (7.5%) and Action (15%) thresholds
warning_low, warning_high = mean_weight * 0.925, mean_weight * 1.075
action_low, action_high = mean_weight * 0.85, mean_weight * 1.15

warning_violations = 0
action_violations = 0

for data in df["weight"]:
    if data > warning_high or data < warning_low:
        warning_violations += 1
    if data > action_high or data < action_low:
        action_violations += 1

# Check Quality Control standards
if warning_violations <= 2 and action_violations == 0:
    print("QC Status: PASS")
else:
    print("QC Status: FAIL")

# Visualization
plt.figure(figsize=(10, 6))
plt.hist(df["weight"], bins=10, color='skyblue', edgecolor='black', alpha=0.7)

# Add vertical control limit lines
plt.axvline(mean_weight, color='blue', linestyle='solid', label='Mean')
plt.axvline(warning_low, color='orange', linestyle='dashed', label='Warning Limits (±7.5%)')
plt.axvline(warning_high, color='orange', linestyle='dashed')
plt.axvline(action_low, color='red', linestyle='dashed', label='Action Limits (±15%)')
plt.axvline(action_high, color='red', linestyle='dashed')

# Labels, Legend, and Saving
plt.title("Tablet Weight Distribution & Quality Control Limits")
plt.xlabel("Weight (mg)")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("weight_qc_plot.png")
print("Plot saved as weight_qc_plot.png")
plt.show()
