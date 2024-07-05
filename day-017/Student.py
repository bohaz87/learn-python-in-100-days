class Student:
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

	def study(self, course_name):
		print(f'{self.name} is studying {course_name}')

	def play(self):
		print(f'{self.name} is playing')
	
	def __repr__(self) -> str:
		return f'{self.name}: {self.age}'

stu1 = Student('luohao', 40)
stu2 = Student('wangdachui', 15)
print(stu1)
print(stu2)

print(hex(id(stu1)), hex(id(stu2)))

Student.study(stu1, 'Python Course')
stu1.study('Java Course')

Student.play(stu2)
stu2.play()