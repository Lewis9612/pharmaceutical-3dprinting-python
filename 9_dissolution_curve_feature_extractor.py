time_points = [5, 10, 15, 30]
release_profile = [12.5, 35.0, 68.0, 98.5]

previous_time = 0
previous_release = 0.0

# This loops using index numbers: 0, 1, 2, 3
for i in range(len(time_points)):
    current_time = time_points[i]
    current_release = release_profile[i]
    
    # 1. Calculate the incremental release amount here...
    # interval_release = ...
    interval_release = current_release - previous_release
    # 2. Print your statement
    print(f"From {previous_time} to {current_time} mins: {interval_release}% released")
    
    # 3. UPDATE your tracking variables for the next loop run
    previous_time = interval_release
    # previous_release = interval_release
