import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. SURFACE AREA FUNCTIONS
# ==========================================

def sa_solid_cylinder(radius_mm, height_mm):
    """Calculate surface area of a solid cylinder tablet."""
    r_m = radius_mm / 1000.0
    h_m = height_mm / 1000.0

    sa_m2 = 2 * np.pi * (r_m ** 2) + 2 * np.pi * r_m * h_m
    sa_mm2 = 2 * np.pi * (radius_mm ** 2) + 2 * np.pi * radius_mm * height_mm

    return sa_m2, sa_mm2


def sa_channelled_tablet(radius_mm, height_mm, n_channels, r_channel_mm):
    """Calculate surface area of a channelled tablet (Alhnan et al. 2018)."""
    face_area = 2 * (np.pi * (radius_mm ** 2) - n_channels * np.pi * (r_channel_mm ** 2))
    outer_side = 2 * np.pi * radius_mm * height_mm
    channel_walls = n_channels * (2 * np.pi * r_channel_mm * height_mm)

    sa_mm2 = face_area + outer_side + channel_walls
    sa_m2 = sa_mm2 / 1e6

    return sa_m2, sa_mm2


# ==========================================
# 2. NOYES-WHITNEY SIMULATION ENGINE
# ==========================================

def simulate_dissolution(sa_m2, drug_mass_mg=100.0, D=2e-8, t_max_hours=8.0):
    """Simulate % drug dissolved over time using Noyes-Whitney."""
    V_m3 = 0.9 / 1000.0        # 900 mL dissolution bath in m³
    Cs_mg_m3 = 500.0 * 1000.0  # 500 mg/L drug solubility converted to mg/m³
    h_d = 50e-6                # 50 µm diffusion layer thickness

    # Rate constant k (depends directly on surface area A!)
    k = (D * sa_m2) / (V_m3 * h_d)

    # Time steps from 0 to t_max_hours (in seconds for physics)
    time_seconds = np.linspace(0, t_max_hours * 3600, 500)
    time_hours = time_seconds / 3600.0

    # Noyes-Whitney concentration calculation
    concentration = Cs_mg_m3 * (1.0 - np.exp(-k * time_seconds))
    
    # Calculate mass dissolved (C * V)
    mass_dissolved_mg = concentration * V_m3
    
    # Cap mass dissolved at total drug mass
    mass_dissolved_mg = np.minimum(mass_dissolved_mg, drug_mass_mg)

    # Calculate percentage dissolved
    pct_dissolved = (mass_dissolved_mg / drug_mass_mg) * 100.0

    # Calculate T90 (time to 90% dissolved)
    idx_90 = np.where(pct_dissolved >= 90.0)[0]
    t90 = time_hours[idx_90[0]] if len(idx_90) > 0 else None

    return time_hours, pct_dissolved, t90


# ==========================================
# 3. PLOTTING & COMPARISON
# ==========================================

if __name__ == "__main__":
    # Tablet dimensions
    radius_mm = 5.0
    height_mm = 3.0

    # 1. Solid Tablet
    sa_solid_m2, solid_mm2 = sa_solid_cylinder(radius_mm, height_mm)
    t_solid, pct_solid, t90_solid = simulate_dissolution(sa_solid_m2)

    # 2. 2-Channel Tablet
    sa_chan2_m2, chan2_mm2 = sa_channelled_tablet(radius_mm, height_mm, n_channels=2, r_channel_mm=0.75)
    t_chan2, pct_chan2, t90_chan2 = simulate_dissolution(sa_chan2_m2)

    # 3. 6-Channel Tablet
    sa_chan6_m2, chan6_mm2 = sa_channelled_tablet(radius_mm, height_mm, n_channels=6, r_channel_mm=0.75)
    t_chan6, pct_chan6, t90_chan6 = simulate_dissolution(sa_chan6_m2)

    # Print Summary Table
    print("=" * 60)
    print("DISSOLUTION PREDICTOR SUMMARY TABLE")
    print("=" * 60)
    print(f"Solid Tablet:     SA = {solid_mm2:.1f} mm2  -->  T90 = {t90_solid:.2f} hours")
    print(f"2-Channel Tablet: SA = {chan2_mm2:.1f} mm2  -->  T90 = {t90_chan2:.2f} hours")
    print(f"6-Channel Tablet: SA = {chan6_mm2:.1f} mm2  -->  T90 = {t90_chan6:.2f} hours")
    print("=" * 60)

    # Create Plot
    plt.figure(figsize=(8, 5))

    plt.plot(t_solid, pct_solid, label=f'Solid Tablet (T90 = {t90_solid:.2f}h)', color='navy', linestyle='--')
    plt.plot(t_chan2, pct_chan2, label=f'2-Channel Tablet (T90 = {t90_chan2:.2f}h)', color='darkorange')
    plt.plot(t_chan6, pct_chan6, label=f'6-Channel Tablet (T90 = {t90_chan6:.2f}h)', color='crimson')

    # 90% threshold reference line
    plt.axhline(y=90, color='gray', linestyle=':', label='90% Target Threshold')

    plt.title('Dissolution Rate Comparison (Noyes-Whitney Model)', fontsize=12)
    plt.xlabel('Time (hours)', fontsize=10)
    plt.ylabel('Drug Dissolved (%)', fontsize=10)
    plt.ylim(0, 105)
    plt.xlim(0, 3)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # Save plot
    plt.savefig('my_dissolution_plot.png')
    print("\nPlot saved successfully as 'my_dissolution_plot.png'!")
