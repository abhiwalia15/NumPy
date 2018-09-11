import numpy as np
import csv

#delimiter tells to split the character after semi-colon , not after comas.
with open('winequality-red.csv','r') as f:
	wines = list(csv.reader(f, delimiter=';'))
	
wine = np.genfromtxt("winequality-white.csv", delimiter=";", skip_header=1)	
all_wines = np.vstack((wines,wine))

print(all_wines.shape)
