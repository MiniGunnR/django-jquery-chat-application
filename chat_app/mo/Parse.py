class Parse(object):
	def __init__(self):
		self.mode=[0,0,0]
		
	def outputString(self,inputstring):
		if not isinstance(inputstring,str):
			raise Exception("Format error")
		inputstring = inputstring.lower()
		if inputstring.find("facebook")>=0:
			self.mode[0] = 1
			inputstring=inputstring.replace("facebook","")
		if inputstring.find("twitter")>=0:
			self.mode[1] = 1
			inputstring=inputstring.replace("twitter","")
		if inputstring.find("instagram")>=0:
			self.mode[2] = 1
			inputstring=inputstring.replace("instagram","")

		outputString = inputstring.strip()
		return (self.mode,outputString)

test = Parse()
print test.outputString("hello world facebook twitter")
