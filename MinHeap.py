class MinHeap :	

	def minHeapify(self,root, size, heap) :
		leftChild = root*2+1
		rightChild = root*2+2
		smallestElement = root
		
		if(leftChild<size and heap[leftChild].frequency < heap[smallestElement].frequency):
			smallestElement=leftChild 
		
		if(rightChild<size and heap[rightChild].frequency < heap[smallestElement].frequency):
			smallestElement=rightChild
		
		if(smallestElement != root):
			heap[root],heap[smallestElement]=heap[smallestElement],heap[root]
			self.minHeapify(smallestElement, size, heap)
		
	def minHeap(self, heap) :
		size = len(heap)
		if size != 1 :
			for root in range(size//2-1,-1,-1) :
				self.minHeapify(root, size, heap)
			return (heap)
		else :
			return (heap)
