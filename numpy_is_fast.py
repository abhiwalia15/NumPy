import numpy as np
import sys
import time

size=10000000

l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start=time.time()
#python list
result=[(x+y) for x, y in zip(l1,l2)]
timetaken= time.time() - start
print(str(timetaken)+"-python list")

start=time.time()
#numpy array
result= a1+ a2
timetaken= time.time()-start
print(str(timetaken)+"-numpy array")
