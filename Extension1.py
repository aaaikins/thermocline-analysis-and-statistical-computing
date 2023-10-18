"""
Name of File: Extension1.py
Date: 09/27/2023
Author's Name: Aikins Acheampong

Purpose:  This script compares thermocline depths at specified times in a temperature data file and outputs the results to a separate file.


"""



import thermocline

def clearfile(filename):
    """
    Clears the content of the specified file.
    """
    fp = open(filename, 'w')
    fp.close()

def compare_times(temperature_file, output_file, target_times):
    """
    Compare thermocline depths at specified times.
    """
    clearfile(output_file)

    # These are the fields corresponding to the temperatures in order by depth
    fields = [10, 11, 16, 17, 15, 14, 13, 12]

    # These are the depth values for each temperature measurement
    depths = [1, 3, 5, 7, 9, 11, 13, 15]

    # Open the data file and read past the header line
    with open(temperature_file, 'r') as fp:
        line = fp.readline()
        day = 0
        
        for line in fp:
            words = line.split(',')
            time = words[0]

            if any(target_time in time for target_time in target_times):
                day += 1
                temps = [float(words[fields[i]]) for i in range(len(depths))]
                thermo_depth = thermocline.thermocline_depth(temps, depths)

                print(f"Day {day}, Time {time}: Thermocline Depth = {thermo_depth} meters")
                with open(output_file, 'a') as hp:
                    hp.write(f"Day {day}, Time {time}: {thermo_depth} meters\n")

if __name__ == "__main__":
    temperature_file = 'GoldieJuly2019.csv'
    output_file = 'thermocline_comparison.csv'
    target_times = ['12:03:00 PM', '2:03:00 PM']  # Add more times as needed

    compare_times(temperature_file, output_file, target_times)
