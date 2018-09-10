import csv

#delimiter tells to split the character after semi-colon , not after comas.
with open('winequality-red.csv','r') as f:
	wines = list(csv.reader(f, delimiter=';'))

#print(wines[:])





