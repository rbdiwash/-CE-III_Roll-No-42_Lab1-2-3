from insertionsort import insertionSort
import random
from time import time
import matplotlib.pyplot as plt

n = 10000
i = 0
timeArray = []
sizeArray = []

#for worst case reverse sorted
#for best case sorted

for i in range(n, n * 11, n):
	sizeArray.append(i)
	randomvalues = random.sample(range(i),i)
	starttime = time()
	# randomvalues.sort() #best case
	insertionSort(randomvalues)
	endtime = time()
	totaltime = endtime - starttime
	timeArray.append(totaltime)
	print(totaltime, "for size", i)

def getTimeArray():
	return timeArray

def getSizeArray():
	return sizeArray

if __name__ == '__main__':
	fig, ax = plt.subplots(1,1)
	ax.plot(sizeArray, timeArray)
	plt.show()
