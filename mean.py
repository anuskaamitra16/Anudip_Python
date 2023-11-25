'''
Question:

how to find mean of every numpy array in the given list? 
input: 
list=[ 
np.array([3,2,8,9]), 
np.array([4,12,34,25,78]), 
np.array([23,12,67])
]
'''

import numpy as np

list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

'''
create a variable to store the mean value using 'np.mean(arr)'
to calculate the mean of each numpy array in the list
means = [np.mean(arr) for arr in list]
'''

#printing the mean result
print("Means:", means)

#output
'''
Means: [5.5, 30.6, 34.0]
'''
