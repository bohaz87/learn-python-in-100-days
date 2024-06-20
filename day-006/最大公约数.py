a = int(input('input a: '))
b = int(input('input b: '))
max = 1
for i in range(a, 0, -1):
	if a % i == 0 and b % i == 0:
		if max < i:
			max = i
			break
			
print(f'最大公约数是{max = }')