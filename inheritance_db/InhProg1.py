class C1:
	def getA(self):
		self.a=10


class C2(C1):
    def getB(self):
        self.b=20

    def operate(self):
        self.c=self.a+self.b
        print("sum({},{})={}".format(self.a,self.b,self.c))


o2=C2()
print(o2.__dict__)
o2.getB()
print(o2.__dict__)
o2.getA()
print(o2.__dict__)
o2.operate()
print(o2.__dict__)

class Parent:
	def parentprop(self):
		self.pp=float(input("Enter Parent Property:"))
		return self.pp
class Child(Parent):
	def childprop(self):
		self.cp=float(input("Enter Child Property:"))
		return self.cp
	def totprop(self):
		pp1=self.parentprop()
		cp1=self.childprop()
		totprop=pp1+cp1
		print("="*50)
		print("Parent Property:{}".format(pp1))
		print("Child Property:{}".format(cp1))
		print("Total Property of child:{}".format(totprop))
		print("="*50)

#main programs
co=Child()
co.totprop()