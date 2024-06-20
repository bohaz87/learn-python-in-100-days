num = int(input('input a number: '))
is_prime = True
end = int(num ** 0.5)
for i in range(2, end + 1):
	if num % i == 0:
		is_prime = False
		break

if is_prime:
	print(f'{num} is prime')
else:
	print(f'{num} is not prime')