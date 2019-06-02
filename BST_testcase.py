import unittest
from BST import BST


class BSTTestCase(unittest.TestCase):

	def test_bstTest(self):
		bst = BST()

		#Test add and size
		bst.add(10, "A value")
		self.assertEqual(bst.size(), 1)

		bst.add(5, "A value")
		self.assertEqual(bst.size(), 2)

		bst.add(30,"A value")
		self.assertEqual(bst.size(), 3)

		#Test inorder_Walk
		self.assertListEqual(bst.inorder_walk(),[5,10,30])

		bst.add(15, "value")
		self.assertListEqual(bst.inorder_walk(),[5,10,15,30])


if __name__ == "__main__":
	unittest.main()