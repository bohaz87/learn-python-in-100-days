def calc(*args, init_value = 0, op = lambda x, y: x + y, **kwargs):
	result = init_value
	for v in args:
		result = op(result, v)
	for v in kwargs.values():
		result = op(result, v)
	return result

print(calc(1, 2, 3, x = 4, y = 5))
print(calc(1, 2, 3, x = 4, y = 5, op=lambda a,b: a * b, init_value=1))

import operator, functools
fac = lambda n: functools.reduce(operator.mul, range(1, n + 1), 1)
print(fac(5))

is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
print(is_prime(23))