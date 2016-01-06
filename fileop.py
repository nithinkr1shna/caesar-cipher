class FileOperator(object):

	def file_write(self,content):
		file_w = open('out.txt','a')
		file_w.write(content)
		file_w.close()

	def file_read(self):
		file_r= open('pg.txt','r')
		file_content = file_r.read()
		file_r.close()
		return file_content


