import fileop
import process

class Caeser(object):
	def __init__(self,shift):
		self.shift = shift

	def encrypt(self):
		data = fileop.FileOperator().file_read()
		to_file = process.Proces().processEncrypt(data,self.shift)
		fileop.FileOperator().file_write(to_file)


new = Caeser(3)
new.encrypt()
