import pandas as pd

collected_data = []

while True:
    formulation_id = input("Batch_ID: ")
    target_api_weight = float(input("Target API Weight(mg): "))
    required_polymer = target_api_weight / 0.25
    data = {
        "ID": formulation_id,
        "Target api weight": target_api_weight,
        "Required polymer": required_polymer
    } 
    collected_data.append(data)

    total_mass = required_polymer + target_api_weight

    if total_mass > 500:
        print(f"{formulation_id} Status: REJECTED - Total mass exceed swallowing threshold.")
    else:
        print(f"{formulation_id} Status: APPROVED - Safe for clinical production.`")

    exit_switch = input("next batch? (y or n): ")
    if exit_switch == "n":
        break
    else:
        continue

df = pd.DataFrame(collected_data)

print(df)
