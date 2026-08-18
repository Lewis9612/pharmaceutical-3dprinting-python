batches = [
    {"id": "B01", "temp": 185, "speed": 30},
    {"id": "B02", "temp": 210, "speed": 40},
    {"id": "B03", "temp": 175, "speed": 25},
    {"id": "B04", "temp": 160, "speed": 35}
]

pass_count = 0
for batch in batches:
    
    if 170 < batch["temp"] < 200 and batch["speed"] <= 35:
        print(f"{batch["id"]} PASS: Batch is stable.")
        pass_count += 1
    else:
        print(f"{batch['id']} FAIL: Out of specification.")
    
print(pass_count)
