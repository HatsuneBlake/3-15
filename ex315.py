class ErrorRecorder(Exception):
	data = 'err_log.txt'
	def __init__(self,line,file):
		self.line = line
		self.file = file
	def recorder(self):
		log = open(self.data,'a')
		log.write('Error at: %s %r\n'%(self.file,self.line))
		log.close()
		
class FileError(ErrorRecorder):pass

if __name__ == '__main__':
	try:
		raise FileError(2,'t.txt')
	except ErrorRecorder as info:
		info.recorder()
	finally:
		with open('err_log.txt') as info:
			print info.read()