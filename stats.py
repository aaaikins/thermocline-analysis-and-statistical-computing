"""
Name of File: stats.py
Date: 09/27/2023
Author's Name: Aikins Acheampong

Purpose: The purpose of this code is to provide functions for performing basic statistical calculations, such as finding the sum, mean, minimum, maximum, and variance of a given set of numbers.  
"""


def sum(numbers):
    """
    Calculate the sum of a list of numbers.
    """
    total = 0.0
    for number in numbers:
        total += number
    
    return total

def mean_data(data):
    """
    Calculate the mean (average) of a list of data.
    """
    mean = sum(data)/len(data)
    return mean 

def min(data):
    """
    Find the minimum value in a list of data.
    """
    min_data = data[0]
    for item in data:
        if item < min_data:
            min_data = item
    return min_data

def max(data):
    """
    Find the maximum value in a list of data.
    """
    max_data = data[0]
    for item in data:
        if item > max_data:
            max_data = item 
    return max_data

def variance(data):
    """
    Calculate the variance of a list of data.
    """
    if len(data) <= 1:
        return None
    mean = mean_data(data)
    total_squared_diff = 0
    for item in data:
        mean_diff = (item - mean)**2
        total_squared_diff += mean_diff
    variance = total_squared_diff/ (len(data) - 1)
    return variance

def median_data(data):
    """
    Calculate the median (middle value) of a list of data.
    """
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

def mode_data(data):
    """
    Find the mode(s) (most frequent value(s)) in a list of data.
    """
    from collections import Counter
    counts = Counter(data)
    max_freq = max(counts.values())
    modes = [val for val, freq in counts.items() if freq == max_freq]
    return modes

def standard_deviation(data):
    """
    Calculate the standard deviation of a list of data.
    """
    mean_val = mean_data(data)
    n = len(data)
    sum_squared_diff = sum((x - mean_val)**2 for x in data)
    variance = sum_squared_diff / (n - 1)
    return variance**0.5

def skewness(data):
    """
    Calculate the skewness of a list of data.
    """
    mean_val = mean_data(data)
    n = len(data)
    sum_cubed_diff = sum((x - mean_val)**3 for x in data)
    sum_squared_diff = sum((x - mean_val)**2 for x in data)
    skew = (sum_cubed_diff / n) / (sum_squared_diff / (n - 1))**(3/2)
    return skew

def kurtosis(data):
    """
    Calculate the kurtosis of a list of data.
    """
    mean_val = mean_data(data)
    n = len(data)
    sum_fourth_diff = sum((x - mean_val)**4 for x in data)
    sum_squared_diff = sum((x - mean_val)**2 for x in data)
    kurt = (sum_fourth_diff / n) / (sum_squared_diff / (n - 1))**2 - 3
    return kurt

def data_range(data):
    """
    Calculate the range of a list of data.
    """
    return max(data) - min(data)

def test():
    """
    Test function to verify the correctness of the implemented statistics functions.
    """
    data = list(range(2, 51, 2))
    #print(data)
    total_sum = sum(data)
    print(f'Sum of data = {total_sum}')  
    mean_num = mean_data(data)
    print(f'mean of data = {mean_num}')
    min_data = min(data)
    print(f'min of data = {min_data}')
    max_data = max(data)
    print(f'max of data = {max_data}')
    variance_data = variance(data)
    print(f'Variance of data = {variance_data}')

if __name__ == "__main__":
    test()
