"""
Name of File: Extension2.py
Date: 09/27/2023
Author's Name: Aikins Acheampong

Purpose: 
This code defines a function, `compare_time_periods`, which reads temperature data from a file, extracts statistics and calculates the thermocline depth for a specified time period.
"""
import stats
import thermocline
def compare_time_periods(start_time, end_time):
    # Read data from the file
    file = open('GoldieJuly2019.csv', 'r')
    line = file.readline()
     
    depths = [ 1, 3, 5, 7, 9, 11, 13, 15 ]
    # Initialize lists to store temperature
    temps = []

    # Initialize variables to track if we are in the relevant time period
    in_time_period = False

    for line in file:
        words = line.split(',')
        date_time = words[0]
        # Check if the line contains the start time
        if start_time == date_time:
            in_time_period = True
            continue  # Skip the line with the timestamp

        # Check if the line contains the end time
        if end_time == date_time:
            in_time_period = False
            break  # Stop reading the file

        # If we're in the relevant time period, process the data
        if in_time_period:
            temp = float(words[4])
            depth = float(words[2])
            temps.append(temp)
            depths.append(depth)

    # Calculate thermocline depth for the time period
    thermo_depth = thermocline.thermocline_depth(temps, depths)

    # Compute statistics for the temperature data
    mean_temp = stats.mean_data(temps)
    min_temp = stats.min(temps)
    max_temp = stats.max(temps)
    variance_temp = stats.variance(temps)
    std_dev_temp = variance_temp ** 0.5

    # Print the statistics
    print(f"Statistics for {start_time} to {end_time}:")
    print("Mean Temperature:", mean_temp)
    print("Min Temperature:", min_temp)
    print("Max Temperature:", max_temp)
    print("Variance of Temperature:", variance_temp)
    print("Standard Deviation of Temperature:", std_dev_temp)

    # Print the thermocline depth
    print(f"Thermocline Depth: {thermo_depth}m")

# Test function
compare_time_periods('07/01/2019 12:03:00 AM', '07/01/2019 11:48:00 PM')
