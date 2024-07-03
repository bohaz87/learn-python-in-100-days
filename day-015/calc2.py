def calc(*args, init_value, op, **kwargs):
	result = init_value
	for value in args:
		result = op(result, value)
	for value in kwargs.values():
		result = op(result, value)
	return result

def add(a, b):
	return a + b

def mul(a, b):
	return a * b

print(calc(1, 2, 3, init_value=0, op=add, x = 4, y = 5))
print(calc(1, 2, 3, x = 4, y = 5, init_value=0, op=mul))

from operator import add as add2
print(calc(1, 2, 3, init_value=0, op=add2, x = 4, y = 5))
