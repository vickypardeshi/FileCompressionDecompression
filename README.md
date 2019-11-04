# FileCompressionDecompression

In this program we are using Huffman Technique coding to compress and decompress any txt file.

Follow following steps to compress & decompress the file :

	1.1) You need python3 environment
	1.2) On terminal, type python3 main.py
	1.3) use options from the menu and follow the further steps
	1.4) To check change in the size of the file use ls -lh command on the terminal
  
About the process of code for Compression:
1)Read text file
2)Make a Frequency table
3)From frequency table make MinHeap 
4)Take two minimum from Minheap and make Huffman tree
5)And append the root node to the MinHeap 
6)Continue the steps 4 & 5 till one element remaining in Minheap
7)Now from Huffman tree write code to each charcter
8)Write this code and frequency table in the file(in binary formate) and encode the file
9)After all this process we do the file compression

About the process of code for Decompression:
1)Read a compress file 
2)Firstly separate a frequency table and data from file
3)Using frequency table make a original file  
4)After all this process we do the file decompression
