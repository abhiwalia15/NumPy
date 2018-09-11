import numpy as np

a_1 = np.array( 
    [
        [2,3,2],
        [5,6,4]
    ])

a_2 = np.array(
    [
        [2,3,5]
    ])


#sum of column
a_1.sum(axis=0)
#sum of row
a_1.sum(axis=1)
#mean along column
a_1.mean(axis=0)
#mean along row
a_1.mean(axis=1)
#standard deviation
a_2.std()
#used to comvert array into 1-D array
a_1.ravel()
