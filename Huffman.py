from MinHeap import MinHeap
from Frequency import Frequency

class Node :
	def __init__(self, character, frequency) :
		self.character = character
		self.frequency = frequency
		self.left = None
		self.right = None

class Huffman :
	def __init__(self, frequencyTable) :
		self.frequencyTable = frequencyTable
		self.heap = []
		self.huffmanCodes = {}

	def inorder(self, root) :
		if root :
			self.inorder(root.left)
			print(root.frequency)
			self.inorder(root.right)

	def minHeapList (self) :
		for key in self.frequencyTable :
			node = Node(key, self.frequencyTable[key])
			self.heap.append(node)
		return (self.heap)

	def generateHuffmanCodes(self, root, code) :
		if root == None:
			return
		
		if root.character != None :
			self.huffmanCodes[root.character] = code
			return

		self.generateHuffmanCodes(root.left, code+"0")
		self.generateHuffmanCodes(root.right, code+"1")

	def generateHuffmanTree(self) :
		self.heap = self.minHeapList()
		
		minHeapObject = MinHeap()
		self.heap = minHeapObject.minHeap(self.heap)
		
		while (len(self.heap) > 1) :
			left = self.heap.pop(0)
			self.heap = minHeapObject.minHeap(self.heap)

			right = self.heap.pop(0)
			self.heap = minHeapObject.minHeap(self.heap)
			
			root = Node(None, left.frequency+right.frequency)
			root.left = left
			root.right = right
	
			self.heap.append(root)
			self.heap = minHeapObject.minHeap(self.heap)
		
		return root	
		
	def huffman(self) :
		root = self.generateHuffmanTree()
		self.generateHuffmanCodes(root, "")
		return self.huffmanCodes
