formulations = [
    {"id": "F_Alpha", "api_mg": 100, "polymer_mg": 400, "disintegrant_mg": 50},
    {"id": "F_Beta",  "api_mg": 150, "polymer_mg": 300, "disintegrant_mg": 45},
    {"id": "F_Gamma", "api_mg": 80,  "polymer_mg": 600, "disintegrant_mg": 30}
]

for formulation in formulations:
    ratio = formulation["api_mg"] / formulation["polymer_mg"]
    if 0.22 <= ratio <= 0.45:
        print(f"{formulation["id"]} Ratio : {ratio:.3f} -> PASS: Blend uniform.")
    elif ratio < 0.22:
        print(f"{formulation["id"]} Ratio : {ratio:.3f} -> FAIL: Sub-potent blend (Too much polymer).")
    elif ratio > 0.45:
        print(f"{formulation["id"]} Ratio : {ratio:.3f} -> FAIL: Hyper-potent blend (Risk of toxicity).")
