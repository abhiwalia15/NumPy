import numpy as np
from scripts import *

qualities = [float(item[-1]) for item in wines[1:]]
print(sum(qualities) / len(qualities))

wines = np.array(wines[1:], dtype = np.float)
print(wines)
print(wines.shape)
