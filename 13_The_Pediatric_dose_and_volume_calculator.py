print("--- PEDIATRIC DOSE & VOLUME CALCULATOR ---")

Patient_name = input("Patient name: ")
Patient_weight = float(input("Patient weight (kg): "))
adult_dose = 100

pediatric_dose = (Patient_weight / 70)* adult_dose

required_infill = (pediatric_dose/adult_dose)*100

if required_infill < 10:
    print("Warning: Dosage too low for standard FDM printing. Recommend liquid compunding instead.")
else:
    print(f"Patient: {Patient_name}; Dose: {pediatric_dose:.2f}; Infill: {required_infill}")
