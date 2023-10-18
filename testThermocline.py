# Bruce A. Maxwell
# Fall 2015
# CS 151S Project 3
# Updated by Caitrin Eaton on August 25, 2017, for Python3 compliance
#
# Test function for the thermocline function in the file thermocline.py
#
import thermocline
def clearfile(filename):
       """
       Clears the content of the specified file.
       """
       fp = open(filename, 'w')
       fp.close()

clearfile('thermocline_data.csv')
# computes densities for a set of temps and prints them out
def main():
    
    # some sample temperatures
    #temps = [24.47, 23.95, 24.41, 23.81, 19.92, 16.88, 14.06, 11.56, 9.82, 9.13, 8.82]
    #depths = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]

    # call the thermocline function
    #depth = thermocline.thermocline_depth( temps, depths )

    # print out the result
    #print("Thermocline depth {0:.2f}".format(depth))


   # these are the fields corresponding to the temperatures in order by depth
    # note they use 0-indexing
    fields = [10, 11, 16, 17, 15, 14, 13, 12]

    # these are the depth values for each temperature measurement
    depths = [ 1, 3, 5, 7, 9, 11, 13, 15 ]
 
    # open the data file and read past the header line
    fp = open('GoldieJuly2019.csv', 'r')
    line = fp.readline()

    # assign to day the value 0
    day = 0
    
    # for each line in the file
    for line in fp:
        # split the line on commas and assign it to words
        words = line.split(',')

        # if the time is about noon (12:03:00 PM)
        if '12:03:00 PM' in words[0]:
            # add one to the day variable
            day  += 1
            # assign to temps the empty list
            temps = []
            # loop over the number of items in depths (loop variable i)

            for i in range(len(depths)):
               # append to temps the result of casting words[ fields[i] ] to a float
               temps.append(float(words[fields[i]]))
            
	        # assign to thermo_depth the result of calling thermocline_depth with temps and depths as arguments
            thermo_depth = thermocline.thermocline_depth(temps, depths)
            # print (or save to a file) the day of the month and thermo_depth separated by a comma
            print(f"Day {day}: Thermocline Depth = {thermo_depth} meters")
            
            #print(str(day)+','+str(thermo_depth))
            hp = open('thermocline_data.csv','a')
            hp.write(str(day)+','+str(thermo_depth)+'\n')



    return

if __name__ == "__main__":
    main()