print("--- 3D Printed Pediatric Dose Calculator ---")

patient_weight = float(input("Enter patient weight (kg): "))
target_dose_mg_per_kg = float(input("Enter target dose (mg/kg): "))

filament_potency = float(input("Enter filament potency (mg of drug per 1g of filament): "))

total_required_dose = patient_weight * target_dose_mg_per_kg

required_filament_grams = total_required_dose / filament_potency

infill_percentage = int(input("Enter desired infill percentage (%): "))

if infill_percentage < 30:
    release_profile = "Immediate release"
elif 30 <= infill_percentage <= 70:
    release_profile = "Sustained release"
else:
    release_profile = "Extended release" 

print("\n==============================")
print("     MANUFACTURING SUMMARY    ")
print("==============================")
print(f"Patient Weight: {patient_weight} kg")
print(f"Total Required Drug Dose: {total_required_dose:.2f} mg")
print(f"Required Filament Material to Print: {required_filament_grams:.4f} grams")
print(f"The desired infill percentage: {infill_percentage}%")
print(f"Predicted Release Profile: {release_profile}")
print("==============================")
