import numpy as np
#slicing a 2-D array
a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
a
a[:]
a[-1,0]

#looping a numpy array
#for row in a:
    #print(row)

#looping each element in array
#for cell in a.flat:
    #print(cell)
    
#stacking one array over second vertically
np.vstack((a,b))

#stacking one array over second horizontally
np.hstack((a,b))

#splitting a function horizontally and vertically
a=np.arange(30).reshape(2,15)
b=np.arange(30,60).reshape(2,15)
result=np.hsplit(a,5)
print(result[0])
result_1=np.vsplit(b,2)
print(result_1[0])

#boolean exp
c=(a>5)
c

#way of extracting all elements that are true by giving condition as index
a[c]
