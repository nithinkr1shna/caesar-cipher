import fileop

class Caeser(object):
	def __init__(self,shift):
		self.shift = shift

	def __processEncrypt(self,data,shift):
		to_file=self.__AlphaCheck_and_Encryptor(data,shift)
		return to_file

	def __AlphaCheck_and_Encryptor(self,data,shift):
		to_file =" "
		for var in data:
			if var.isalpha():
				to_file += self.__Encryptor(shift,var)
		return to_file

	def __Encryptor(self,shift,var):
		to_write = ord(var) + shift
		to_write = self.__total_alph_count_check(to_write)
		to_file1 =chr(to_write)
		return to_file1

	def __total_alph_count_check(self,to_write):
		TOTAL_ALPHABET_COUNT= ord('z')
		if(to_write > TOTAL_ALPHABET_COUNT):
			to_write=to_write-26
			return to_write
		else:
			return to_write

	def encrypt(self):
		data = fileop.FileOperator().file_read()
		to_file = self.__processEncrypt(data,self.shift)
		fileop.FileOperator().file_write(to_file)


new = Caeser(3)
new.encrypt()
