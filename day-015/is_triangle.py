def is_triangle(a, b, c):
	return a + b > c and b + c > a and c + a > b

print(is_triangle(1, 2, 3,))
print(is_triangle(a = 1, b = 2, c = 3))
print(is_triangle(c = 3, a = 1, b = 2))

def is_triangle2(*, a, b, c):
	return is_triangle(a, b, c)

# Error: print(is_triangle2(1, 2, 3))
print(is_triangle2(a = 1, b = 2, c = 3))
