def is_prime(n: int):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

for n in range(0, 16):
	print(f'{n} is prime: {is_prime(n)}')