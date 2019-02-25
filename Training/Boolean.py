# This file deals with boolean operations
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(my_house, your_house)
print(np.logical_and(my_house <18, my_house >19))
print(np.logical_and(my_house <18, your_house<14))
# help('%')
z = 4
if z % 2 == 0 : # % yields the remainder of the division
 print('Number is even') # must be indentation in order to run
elif z % 2 == 0 :
 print('Number is odd')
else :
 print('something else')
 print('another line')
print ('outside of the block, just the indentation marks end of the block')

import pandas as pd
cars = pd.read_csv('C:/Users/mike/source/Data/cars_csv.txt', index_col = 0)
cars_series = cars["cars_per_cap"] > 200

print(cars_series)

import os
print(os.getcwd())