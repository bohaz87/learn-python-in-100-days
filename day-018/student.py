class Student:
	__slots__ = ('__name', '__age')

	def __init__(self, name, age) -> None:
		self.__name = name
		self.__age = age

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name or 'unknown'

	@property
	def age(self):
		return self.__age

	def study(self, course_name):
		print(f'{self.__name}正在学习{course_name}')

stu = Student('wangdachui', 20)
stu.study('Python程序设计')
# print(stu._Student__name)
# print(stu.__name)
print(stu.name)
print(stu.age)
stu.name = ''
print(stu.name)

stu.sex = 'Male'
print(stu.sex)