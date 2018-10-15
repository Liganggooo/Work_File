class SchoolMember():
	def __init__(self,name,age):
		self.name = name 
		self.age = age
		print('initialized school member: {}'.format(self.name))
	def tell(self):
		print('name:"{}",age:"{}"'.format(self.name,self.age),end='')
		
class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print('initialized Teacher:{}'.format(self.name))
	def tell(self):
		SchoolMember.tell(self)
		print('salary:"{:d}"'.format(self.salary))
		
class Student(SchoolMember):
	def __init__(self,name ,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print('initialized Student:{}'.format(self.name))
	def tell(self):
		SchoolMember.tell(self)
		print('marks:"{:d}"'.format(self.marks))

t = Teacher('Mr.lee',22,10000)
s = Student('xiaoli',20,90)
print()
members = [t,s]
for member in members:
	member.tell()
		
	
