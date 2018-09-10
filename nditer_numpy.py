import numpy as np

#iterate each item in an array row wise
a = np.arange(12).reshape(3,4)
b = np.arange(12,24).reshape(3,4)

for x in np.nditer(a, order='C'):
    print(x)

#iterate each item in an array column wise
for x in np.nditer(a, order='F'):
    print(x)
    
#iterating 2 arrays at same time.
for x,y in np.nditer([a,b]):
    print(x, y)
