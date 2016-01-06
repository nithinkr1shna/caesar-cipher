class Proces:
	def processEncrypt(self,data,shift):
		to_file = ""
		for var in data:
			if var.isalpha():
				to_write = ord(var) + shift
				if(to_write > ord('z')):
					to_write=to_write-26
				to_file =to_file+ chr(to_write)
		return to_file