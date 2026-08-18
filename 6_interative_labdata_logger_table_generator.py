import pandas as pd

print("--- LAB DATA LOGGER ---")

collected_data = []

while True:
    batch_id = input("Batch ID: ")
    polymer_composition = input("Polymer Composition: ")
    print_temperature = float(input("Temperature: "))
    measured_hardness = float(input("Measured hardness (Newtons): "))

    data_entry = {
        "Batch ID": batch_id,
        "Polymer Composition": polymer_composition,
        "Print Temerature": print_temperature,
        "Measured hardness": measured_hardness
    }
    collected_data.append(data_entry)

    exit_switch = input("Do you want to add another batch ? (yes or no): ")
    if exit_switch == "no":
        break
    elif exit_switch == "yes":
        continue

df = pd.DataFrame(collected_data)

print("\n--- FINAL PHARMACEUTICAL DATA TABLE ---")
print(df)
