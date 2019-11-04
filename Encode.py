class Encode :
	def __init__(self, huffmanCodes, fileName) :
		self.huffmanCodes = huffmanCodes
		self.fileName = fileName
		self.encodedData = ""
		self.byteArray = None

	def convertFile(self) :
		data = open(self.fileName, "r").read()
		self.encodedData = ""
		for character in data :
			self.encodedData  = self.encodedData+self.huffmanCodes[character]
		return self.encodedData

	def padFile(self) :
		extra = 8 - len(self.encodedData)%8
		for iterator in range(extra) :
			self.encodedData = self.encodedData + "0"
		padding  = "{0:08b}".format(extra)
		self.encodedData = padding + self.encodedData
		return self.encodedData

	def convertToBits(self) :
		self.byteArray = bytearray()
		while(self.encodedData != "") :
			self.byteArray.append(int(self.encodedData[:8],2))
			self.encodedData = self.encodedData[8:]
		return (self.byteArray)

	def encode(self) :
		self.encodedData = self.convertFile()
		self.encodedData = self.padFile()
		self.byteArray = self.convertToBits()
		encodedFile = open(self.fileName+".bv","wb+")
		self.huffmanCodes = str(self.huffmanCodes).encode()
		encodedFile.write(self.huffmanCodes)
		encodedFile.write("\n".encode())
		encodedFile.write(bytes(self.byteArray))
		encodedFile.close()
