def fac(n):
	if n in (0, 1):
		return 1
	return n * fac(n - 1)

print(fac(3))