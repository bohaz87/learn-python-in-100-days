a = int(input('input a: '))
b = int(input('input b: '))
while b % a != 0:
	a, b = b % a, a
			
print(f'最大公约数是{a = }')