m = int(input('input m: '))
n = int(input('input n: '))

def factorial(n):
	result = 1
	for n in range(1, n + 1):
		result *= n
	return result

print(factorial(m) // factorial(n) // factorial(m - n))