import pandas as pd
import os

while True:
    id = input("ID:")
    polymer_carrier = input("Carrier: ")
    Api_name = input("API Name: ")
    while True:
        try:
            Mass_of_Polymer = float(input("Mass of Polymer (g): "))
            if Mass_of_Polymer < 0:
                print("Mass cannot be negative. Please try again")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            Mass_of_API_Added = float(input("Mass of API added (g): "))
            if Mass_of_API_Added < 0:
                print("Mass cannot be negative. Please try again")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:  
            Extrusion_Temperature = float(input("Extrusion Temperature (°C): "))
            if Extrusion_Temperature < 100 or Extrusion_Temperature > 250:
                print("The temperature can be invalid.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    Total_mass = Mass_of_API_Added + Mass_of_Polymer
    drug_loading_percentage = (Mass_of_API_Added / Total_mass) * 100 

    new_data = {
        "ID" : id,
        "Polymer Carrier" : polymer_carrier,
        "API Name" : Api_name,
        "Mass of polymer (g)" : Mass_of_Polymer,
        "Mass of API (g)" : Mass_of_API_Added,
        "Extrusion Temperature": Extrusion_Temperature,
        "Total Mass (g)": Total_mass,
        "Drug loading %": drug_loading_percentage
    }
    
    filename = "filament_log.csv"
    file_exists = os.path.exists(filename)
    df = pd.DataFrame([new_data])
    df.to_csv(filename, mode='a', index=False, header=not file_exists)

    next_batch = input("Do you want to log another Batch? (y/n):")   
    if next_batch.lower() != "y":
        break
