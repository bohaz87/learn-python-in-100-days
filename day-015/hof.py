def is_even(num):
	return num % 2 == 0

def square(num):
	return num ** 2

list1 = [35, 12, 8, 99, 60, 52]
list2 = list(filter(is_even, list1))
print(list2)
list2 = list(map(square, list2))
print(list2)

list2 = [n ** 2 for n in list1 if n % 2 == 0]
print(list2)

"""
如果作为参数或者返回值的函数本身非常简单，一行代码就能够完成，那么我们可以使用Lambda函数来表示
"""
list2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, list1)))
print(list2)