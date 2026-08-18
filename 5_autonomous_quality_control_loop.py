layer_height_log = [0.20, 0.21, 0.25, 0.28, 0.22, 0.20, 0.15]

for height in layer_height_log:
    deviation = height - 0.2
    if deviation == 0:
        print("Layer optimal. No action required.")
    elif deviation > 0:
        speed_adjustment = -(deviation * 100)
        print(f"Over-extrusion detected (Deviation: {deviation:.3f}mm). AI Action: Reduce print speed by {speed_adjustment:.3f}%")
    else:
        speed_adjustment = -(deviation * 100)
        print(f"Under-extrusion detected (Deviation: {deviation:.3f}mm). AI Action: Increase print speed by {speed_adjustment:.3f}%")
