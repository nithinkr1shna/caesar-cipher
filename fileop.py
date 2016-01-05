class FileOperator(object):

	def file_write(self,content):
		file_w = open("out.txt",'a')
		file_w.write(content)

	def file_read(self):
		file_r= open("pg.txt",'r')
		return file_r.read()



