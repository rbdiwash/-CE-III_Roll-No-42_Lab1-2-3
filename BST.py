



class BST:

	def __init__(self):
		self._size = 0
		self.root = None

	class BSTNode:
		def __init__(self,key, value):
			self.key = key
			self.value = value
			self.left = None
			self.right = None

	def add(self,key,value):
		z=self.BSTNode(key,value)
		y=None
		x=self.root
		while (x!=None):
			y=x
			if(key<x.key):
				x=x.left
			else:
				x=x.right
		if(y==None) :
			self._root=z
		elif (z.key<y.key):
			y.left=z
		else:
			y.right= z
		self._size +=1


	def is_empty(self):
		if self._size == 0:
			return 1

	def size(self):
		return self._size

	def inorder_walk(self):
		nodes = []
		self._inorder_walk(self._root, nodes)
		return nodes
	def _inorder_walk(self,subtree,nodes)	:
		if subtree:
			self._inorder_walk(subtree.left,nodes)
			nodes.append(subtree.key)
			self._inorder_walk(subtree.right,nodes)

def preOrderTraverse(self):
		nodes = []
		self._preOrderTraverse(self._root, nodes)
		return nodes

	def _preOrderTraverse(self, subtree, nodes):
		if(subtree):
			nodes.append(subtree.key)
			self._preOrderTraverse(subtree.left, nodes)
			self._preOrderTraverse(subtree.right, nodes)

	def postOrderTraverse(self):
		nodes = []
		self._postOrderTraverse(self._root, nodes)
		return nodes

	def _postOrderTraverse(self, subtree, nodes):
		if(subtree):
			self._preOrderTraverse(subtree.left, nodes)
			self._preOrderTraverse(subtree.right, nodes)
			nodes.append(subtree.key)

	def searchForNode(self, key):
		found = []
		self._searchForNode(self._root, key, found)
		return found

	def _searchForNode(self, subtree, key, found):
		if(subtree):
			if(key == subtree.key):
				found.append(1)
			elif(key < subtree.key):
				self._searchForNode(subtree.left, key, found)
			elif(key > subtree.key):
				self._searchForNode(subtree.right, key, found)

	def searchSmallestKey(self):
		nodes = []
		self._searchSmallestKey(self._root, nodes)
		return nodes

	def _searchSmallestKey(self, subtree, nodes):
		if(subtree):
			if(subtree.left == None):
				nodes.append(subtree.key)
			self._searchSmallestKey(subtree.left, nodes)

	def searchLargestKey(self):
		nodes = []
		self._searchLargestKey(self._root, nodes)
		return nodes

	def _searchLargestKey(self, subtree, nodes):
		if(subtree):
			if(subtree.right == None):
				nodes.append(subtree.key)
self._findLargestKey(subtree.right, nodes)