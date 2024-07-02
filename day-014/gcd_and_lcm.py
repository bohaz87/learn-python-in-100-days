def gcd_and_lcm(x: int, y: int):
	a, b = x, y
	while b % a != 0:
		a, b = b % a, a
	return a, x * y // a

print(gcd_and_lcm(3, 4))
print(gcd_and_lcm(2, 4))