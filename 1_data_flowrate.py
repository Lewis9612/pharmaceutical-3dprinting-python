Drug_Name = input("Drug name: ")
Degradation_Temerature = float(input("Degradation Temperature of the drug (Celsius): "))
Nozzle_Temperature = float(input("Current nozzle Temperature (Celsius): "))
Extrusion_Multiplier = int(input("Extrussion multiplier (%): "))

temp_status = "Normal"
flow_status = "Stable"

if Nozzle_Temperature > Degradation_Temerature:
    temp_status = 'WARNING: DRUG DEGRADATION RISK'
elif Nozzle_Temperature < 170:
    temp_status = "CAUTION: RISK OF NOZZLE CLOGGING"

if Extrusion_Multiplier < 90 or Extrusion_Multiplier > 110:
    flow_status ="Flow rate unstable - check feeder gears"

print_status = {
    "Drug" : Drug_Name,
    "Temperature_status": temp_status,
    "Flow_rate": flow_status
}

print("\n--- SYSTEM STATUS DICTIONARY ---")
print(print_status)
