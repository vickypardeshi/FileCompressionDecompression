import ast

class Decode :
	def __init__(self, fileName) :
		self.fileName = fileName
		self.frequencyTable = None
		self.data = ""
		self.bitString = ""
		self.extractedData=""

	def readFile(self) :
		fileDiscriptor = open(self.fileName, "rb")
		self.frequencyTable = fileDiscriptor.readline().decode().rstrip()
		self.frequencyTable = ast.literal_eval(self.frequencyTable)
		self.data = fileDiscriptor.readline()

	def removePadding(self) :
		padding = -int(self.bitString[:8],2)
		self.bitString = self.bitString[8:padding]

	def extractDataAsBits(self) :
		for character in self.data :
			characterAsBit = bin(character)[2:].rjust(8,'0')
			self.bitString = self.bitString + characterAsBit
	
	def writeData(self) :
		self.fileName = self.fileName.split('.')
		fileName = self.fileName[0]+"_new."+self.fileName[1]
		fd = open(fileName,"w+")
		fd.write(self.extractedData)

	def decodeBitString(self) :
		code = ''
		for bit in self.bitString :
			code=code+bit	
			for key, value in self.frequencyTable.items():
				if code == value :
					self.extractedData = self.extractedData + key
					code = ""
					break

	def decode(self) :
		self.readFile()
		self.extractDataAsBits()
		self.removePadding()
		self.decodeBitString()	
		self.writeData()
