import unittest
from insertionsort import insertionSort

class SortTestCase(unittest.TestCase):
	def testInsertionSort(self):
		data = [2, 1, 6, 4, 0]
		sorteddata =  [0, 1, 2, 4, 6]
		insertionSort(data)
		self.assertListEqual(data, sorteddata)

if __name__ == '__main__':
	unittest.main()
