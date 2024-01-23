import mysql.connector
from college import College
class Student(College):
	def getStudDet(self):
		self.sno = int(input('Student Number: '))
		self.sname = input('Student name: ')
		self.slocation = input('Student location: ')
		self.getColgDet()

	def dispStudDet(self):
		self.dispUnivDet()
		self.dispColgDet()
		print(self.sno, self.sname, self.slocation)

	def storeStudCollUnivData(self):
		try:
			con = mysql.connector.connect(
				host='localhost',
				user='root',
				password='krishna',
				database='store_db'
				)
			cur = con.cursor()
			tcq = "insert into university values(%d, '%s','%s','%s','%s','%s')"
			cur.execute(tcq %(self.sno, self.sname, self.cname, self.clocation, self.uname, self.ulocation))
			print('success connect')
			con.commit()
			print("{} Student Record Inserted Sucessfully".format(cur.rowcount))
		except mysql.connector.DatabaseError as e:
			print('not connect', e)
