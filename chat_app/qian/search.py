class search(object):

	def _int_ (self):
		self.str_name = ""

	def convertToName(self, str):
		str = str.upper()
		str = str.strip()
		if (str[0:10] == 'FIND NAME:'):
			self.str_name = str[10:]
			self.str_name = self.str_name.strip()
			return self.str_name
		else:
			return 'Please input target name with \'Find Name:\''


a = search()
print a.convertToName("fInd naMe: Qian Zhang")
