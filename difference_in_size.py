import numpy as np
import sys 
import time

#list made in python
l = range(1000)
#find size of that list
print(sys.getsizeof(1)*len(l))



#numpy array
array = np.arange(1000)
print(array.size*array.itemsize)
