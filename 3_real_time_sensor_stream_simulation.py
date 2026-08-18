sensor_stream = [180, 182, 185, 215, 178, 179]

temperature_history = []

for temp in sensor_stream:
    temperature_history.append(temp)
    average_temp = sum(temperature_history) / len(temperature_history)
    print(f"Temperature history: {temperature_history}")
    print(f"Average temperature: {average_temp}")
    if temp < 165 or temp > 195:
        print("Anomaly detected! Adjusting process parameters...")
