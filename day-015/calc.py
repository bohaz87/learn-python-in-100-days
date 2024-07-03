def calc(*args):
	result = 0
	for arg in args:
		if type(arg) in (int, float):
			result += arg
	return result

# Error: print(calc(a = 1, b = 2, c = 3))

"""
不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前，否则将会引发异常。
"""
def calc2(*args, **xxx,):
	result = 0
	for arg in args:
		if type(arg) in (int, float):
			result += arg
	for arg in xxx.values():
		if type(arg) in (int, float):
			result += arg
	return result

print(calc2())
print(calc2(1, 2, 3))
print(calc2(1, 2, 3, a = 1, b = 2, c = 3))
# Error	print(calc2(1, 2, 3, a = 1, b = 2, c = 3, 4, 5))