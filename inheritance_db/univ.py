class University():
	def getUnivDet(self):
		self.uname = input("University: ")
		self.ulocation = input("University location: ")

	def dispUnivDet(self):
		print(self.uname, self.ulocation)