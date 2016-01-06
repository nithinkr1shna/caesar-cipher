class Proces:
	def processEncrypt(self,data,shift):
		to_file = " "
		NUMBER_26 = ord('z')
		for var in data:
			if var.isalpha():
				to_write = ord(var) + shift
				if(to_write > NUMBER_26):
					to_write=to_write-26
				to_file +=chr(to_write)
		return to_file