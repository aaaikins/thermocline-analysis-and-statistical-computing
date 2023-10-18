"""
Name of File: thermocline.py
Date: 09/27/2023
Author's Name: Aikins Acheampong

Purpose: The purpose of this code is to calculate the density of a fluid based on its temperature and depth, and to find the depth at which the steepest change in density occurs (known as the thermocline depth).
"""


def density(temps):
    densities = []
    for temp in temps:
        rho = 1000 * (1 - (temp + 288.9414) * (temp - 3.9863)**2 / (508929.2*(temp + 68.12963)))
        densities.append(rho)
    return densities

def thermocline_depth( temps, depths ):
	# assign to rhos the result of calling the density function with temps as the argument
    rhos = density(temps)
	# create an empty list named drho_dz
    drho_dz = []
	# loop for one less than the length of rhos
    for i in range(len(rhos)-1):
        # append to drho_dz  the quantity rhos[i+1] minus rhos[i] divided by the quantity depths[i+1] minus depths[i]
        drho_dz.append((rhos[i+1]-rhos[i])/(depths[i+1] - depths[i]))
        # sanity check (optional): print out temps[i], rhos[i], and drho_dz[i] for visual inspection
	# assign to max_drho_dz the value -1.0
    max_drho_dz = -1.0
	# assign the maxindex the value -1
    maxindex = -1
	# loop for the length of drho_dz (loop variable i)
    for i in range(len(drho_dz)):
    	# if drho_dz[i] is greater than max_drho_dz
        if drho_dz[i] > max_drho_dz:
             # assign to max_drho_dz the value drho_dz[i]
            max_drho_dz = drho_dz[i] 
            # assign to maxindex the value i
            maxindex = i
    # assign to thermoDepth the average of depths[maxindex] and depths[maxindex+1]
    thermoDepth = (depths[maxindex] + depths[maxindex +1])/2
    return thermoDepth