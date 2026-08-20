# pharmaceutical-3dprinting-python
Python toolkit for pharmaceutical 3D printing (FDM/HME): Noyes-Whitney drug dissolution kinetic simulator, scikit-learn ML disintegration predictor, real-time sensor QC, and pediatric dosing tools.

# Computational Pharmaceutics & 3D Printing Toolkit

A collection of Python scripts, kinetic simulation engines, and machine learning models for pharmaceutical 3D printing (FDM/HME), formulation optimization, and quality control. Developed as part of self-directed research bridging clinical pharmacy with digital manufacturing.

---

## Overview of Modules

### 1. Dissolution Kinetic Simulator (`dissolution_predictor.py`)
- **Physics Engine**: Implements the Noyes-Whitney equation to simulate percentage drug dissolved over time in a 900 mL dissolution bath ($V = 0.9\text{ L}$, $C_s = 500\text{ mg/L}$).
- **Surface Area Models**: Mathematical surface area equations comparing standard solid cylindrical tablets against multi-channelled tablet architectures (based on geometry models from Alhnan et al. 2018).
- **Output**: Generates time-series dissolution curves (`my_dissolution_plot.png`) illustrating how surface-area-to-volume ratio controls drug release rates.

$$\frac{dC}{dt} = \frac{D \cdot A}{V \cdot h} (C_s - C)$$

---

### 2. Machine Learning Quality Control & Disintegration Predictor (`predict_disintegration.py`, `11_Smart_Manufacturing_Classifier.py`)
- **Disintegration Prediction**: Uses `scikit-learn` Random Forest Regressor to predict tablet disintegration time based on formulation composition, infill percentage, and printing temperature.
- **Extrusion Failure Classification**: Classifies print batches into quality outcomes (crumbling failure, optimal pass, thermal degradation) using Random Forest classifiers and K-Means clustering on nozzle temperature, print speed, and infill metrics.

---

### 3. Process Monitoring & Quality Control (`5_autonomous_quality_control_loop.py`, `3_real_time_sensor_stream_simulation.py`)
- **Real-Time Extrusion Monitoring**: Simulates continuous temperature sensor streams to detect thermal deviations outside target bounds (165°C to 195°C).
- **Layer Height Quality Control**: Automated feedback loop evaluating layer thickness deviations and calculating necessary print speed adjustments to correct over- or under-extrusion.

---

### 4. Lab Utilities & Dosage Calculators (`0_dose_calculator.py`, `hme_logger.py`, `weight_qc.py`)
- **Pediatric Dose Calculator**: Calculates required filament mass and printed volume based on patient weight and API-to-polymer potency ratios.
- **Hot-Melt Extrusion Logger**: Interactive CLI logger recording formulation batches, carrier polymers, API loading, and extrusion parameters into structured pandas DataFrames.
- **Weight QC Simulator**: Statistical evaluation of tablet weight uniformity using normal distributions and standard deviation limits ($150\text{ mg} \pm 8\text{ mg}$).

---

## Technology Stack

- **Language**: Python 3.10+
- **Data & Math**: NumPy, Pandas
- **Machine Learning**: Scikit-Learn (RandomForestRegressor, RandomForestClassifier, KMeans, LinearRegression)
- **Visualization**: Matplotlib
- **CAD Integration**: FreeCAD, Nomad Sculpt, Bambu Studio

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Lewis9612/pharmaceutical-3dprinting-python.git
   cd pharmaceutical-3dprinting-python
   ```

2. Install dependencies:
   ```bash
   pip install numpy pandas scikit-learn matplotlib
   ```

3. Run the dissolution simulator:
   ```bash
   python my_dissolution_predictor/dissolution_predictor.py
   ```

4. Run the disintegration predictor:
   ```bash
   python predict_disintegration.py
   ```

---

## Author

**Yin Ki Luk, MPharm**  
UK-Registered Community Pharmacist | Self-Taught Developer & Maker
