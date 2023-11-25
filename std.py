'''
Question:
compute the standard deviation off the numpy array
input: arr=[20,2,7,1,34]
'''
import numpy as np
arr = np.array([20, 2, 7, 1, 34])

#'np.std(arr)' is used to calculate the standard deviation of the given numpy array.
std_deviation = np.std(arr)

#printing the result
print("Standard Deviation:", std_deviation)

#Output
#Standard Deviation: 12.576167937809991
