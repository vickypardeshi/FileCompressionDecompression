import sys

class Frequency :
	def __init__(self, fileName) :
		self.fileName = fileName
	
	def readFile(self) :
		try :
			with open(self.fileName,"r") as fileDiscriptor :
				data = fileDiscriptor.read()
			return data
			fileDiscriptor.close()

		except OSError as exception :
			print("File Opening Error\n")
			sys.exit()

	def frequencyTable(self) :
		frequencyTable = {}
		data = self.readFile()
		for character in data :
			if not character in frequencyTable :
				frequencyTable[character] = 0
			frequencyTable[character] += 1
		return frequencyTable
