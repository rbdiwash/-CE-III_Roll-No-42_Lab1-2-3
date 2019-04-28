def insertionSort(alist):
    for i in range(1, len(alist)): 
        key = alist[i] 
        j = i-1
        while j >= 0 and key < alist[j]: 
                alist[j + 1] = alist[j] 
                j -= 1
        alist[j + 1] = key 

if __name__ == '__main__':
	A = [2, 6, 1, 3 , 0]
	insertionSort(A)
	print(A)
