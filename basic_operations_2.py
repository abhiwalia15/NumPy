import numpy as np
#remember all these functions are not going to change the original array

#initiliaze all rows and columns with 0 and pass shape as attribute.
np.zeros((3,3))

#initiliaze all rows and columns with 10 and pass shape as attribute.
np.ones((3,3))

#range function
np.arange(878,900)

#including no.s linearlly b/w 2 nos
np.linspace(1,5,5)

#how to reshape the array.
a=np.array([[1,2,4],[1,4,3]]) #2-d array
a.shape
a.reshape(3,2)

#convert 2-D to 1-D array
a.ravel()

#to find max
a.max()

#to find the min no. of array
a.min()

#to find sum
a.sum()

#to find sum of rows
a.sum(axis=1)

#to find sumof columns
a.sum(axis=0)

#to find squareroot
np.sqrt(a)

#to find standard deviation
a.std() 

#to find matrix multiplication
a=np.array([[1,2],[1,3]]) #2-d array
b=np.array([[1,2],[6,7]]) #2-d array
a.dot(b)
