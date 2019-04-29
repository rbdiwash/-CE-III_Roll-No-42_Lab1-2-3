def LinearSearch (elements, searchParameter):
	i = 0
	while True:
		if searchParameter == elements[i]: 
										   
			index = i
			break
		i = i + 1
	return index

def BinarySearch(elements , searchParameter):
	maxi = len(elements) - 1
	mini = 0
	i = int((maxi + mini)/2)

	while searchParameter != elements[i]: 
										  
		if elements[i] < searchParameter:
			mini = i
		else:
			maxi = i
		i = int((maxi + mini)/2)
return i
