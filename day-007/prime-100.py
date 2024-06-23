for n in range(1, 101):
	is_prime = True
	for x in range(2, int(n ** 0.5 + 1)):
		if n % x == 0:
			is_prime = False
			break

	if is_prime:
		print(f'{n} is prime')