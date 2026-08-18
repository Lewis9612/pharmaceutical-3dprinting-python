import math
import matplotlib.pyplot as plt

# Tablet Properties
a_radius = 5
a_height = 5
b_outer_radius = 5
b_inner_radius = 2
b_height = 5
density = 0.2

# Calculate Initial Properties
a_volume = math.pi * (a_radius**2) * a_height
a_surface_area = 2 * math.pi * (a_radius**2) + 2 * math.pi * a_radius * a_height
a_initial_drug_mass = a_volume * density

b_volume = math.pi * (b_outer_radius**2 - b_inner_radius**2) * b_height
b_surface_area = 2 * math.pi * (b_outer_radius**2 - b_inner_radius**2) + 2 * math.pi * b_outer_radius * b_height + 2 * math.pi * b_inner_radius * b_height
b_initial_drug_mass = b_volume * density

# Constants
D = 0.01  # mm2/s
Cs = 0.5 / 1000  # mg/mm3 (converted 0.5 mg/mL to mg/mm3 by dividing by 1000)
h = 0.1   # mm
Vmedium = 900 * 1000  # 900 mL converted to mm3
total_time = 7200     # seconds
dt = 1

def get_dissolution_profile(initial_area, initial_mass):
    mdissolved = 0
    dissolve_percentage = []
    time_at_90 = None
    
    for t in range(0, total_time, dt):
        current_concentration = mdissolved / Vmedium
        remaining_mass = max(0, initial_mass - mdissolved)
        current_area = initial_area * (remaining_mass / initial_mass)**(2/3)
        
        # Noyes-Whitney
        dm = ((D * current_area * (Cs - current_concentration)) / h) * dt
        mdissolved = min(initial_mass, mdissolved + dm)
        
        pct = (mdissolved / initial_mass) * 100
        dissolve_percentage.append(pct)
        
        # Track 90% threshold
        if pct >= 90 and time_at_90 is None:
            time_at_90 = t / 60
            
    return dissolve_percentage, time_at_90

# Run Simulations
profile_A, time_90_A = get_dissolution_profile(a_surface_area, a_initial_drug_mass)
profile_B, time_90_B = get_dissolution_profile(b_surface_area, b_initial_drug_mass)

# Output Results
if time_90_A is not None:
    print(f"Tablet A (Solid) reaches 90% dissolution at: {time_90_A:.1f} minutes")
else:
    print("Tablet A (Solid) did not reach 90% dissolution within 2 hours.")

if time_90_B is not None:
    print(f"Tablet B (Hollow) reaches 90% dissolution at: {time_90_B:.1f} minutes")
else:
    print("Tablet B (Hollow) did not reach 90% dissolution within 2 hours.")

# Visualization
time_minutes = [t/60 for t in range(0, total_time, dt)]
plt.figure(figsize=(10, 6))
plt.plot(time_minutes, profile_A, label="Tablet A (Solid)")
plt.plot(time_minutes, profile_B, label="Tablet B (Hollow)")
plt.xlabel("Time (minutes)")
plt.ylabel("% Dissolved")
plt.title("Noyes-Whitney Dissolution Comparison")
plt.legend()
plt.grid(True)
plt.savefig("dissolution_profile.png")
plt.show()
