import random

answer = random.randrange(1, 101)
count = 0
while True:
	count += 1
	num = int(input('input a number: '))
	if num > answer:
		print('大了')
	elif num < answer:
		print('小了')
	else:
		print(f'猜对了, {count = }')
		break