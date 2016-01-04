class Caeser(object):
	
	def encrypt(self,content,shifts):
		
		file_output = open('out.txt','w')
		for var in content:
			if var.isalpha():
				to_write = ord(var) + shifts
				if(to_write > ord('z')):
					to_write=to_write-26
				to_file = chr(to_write)											       
				file_output.write(to_file)

shifts =  int(raw_input('enter the number of shifts to perform'))
file =open('pg.txt','r')
content=file.read()
c= Caeser();
c.encrypt(content,shifts)
