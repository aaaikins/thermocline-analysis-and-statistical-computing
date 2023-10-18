
"""
Name of File: analyze.py
Date: 09/27/2023
Author's Name: Aikins Acheampong

Purpose: The purpose of this code is to analyze data from a CSV file, including calculating statistics.
"""

import sys 
import stats



def main(filename, column_id):

    # assign to fp the result of opening the file hurricanes.csv for reading
    fp = open(filename, 'r')
    # assign to line the first line of the data file
    line = fp.readline()
    # assign to headers the result of splitting the line using commas
    #headers = line.split(',')
    # print headers
    #print(headers)

    # assign to a list variable named data an empty list
    data = []
    # for all of the remaining lines in the file
    for line in fp:
        # assign to items the result of splitting the line using commas
        items = line.split(',')      
        # append the second item to data (which index?) items cast as a float
        data.append(float(items[column_id]))

    # close the data file
    fp.close()
    # print data
    #print(data)
    #print(stats.sum(data))
    print(f'mean of data = {stats.mean_data(data)}')
    #print(stats.min(data))
    #print(stats.max(data))
    #print(stats.variance(data))
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))



