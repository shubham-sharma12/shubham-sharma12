from univ import University
class College(University):
	def getColgDet(self):
		self.cname = input("College: ")
		self.clocation = input("College location: ")

	def dispColgDet(self):
		print(self.cname, self.clocation)