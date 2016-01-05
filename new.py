import fileop


class Caeser(object):
	def __init__(self,shift):
		self.shift = shift


	def encrypt(self):
		data = fileop.FileOperator().file_read()
		for var in data:
			if var.isalpha():
				to_write = ord(var) + self.shift
				if(to_write > ord('z')):
					to_write=to_write-26
				to_file = chr(to_write)
				fileop.FileOperator().file_write(to_file)


new = Caeser(3)
new.encrypt()
