total = 0
for i in range(1, 101):
	total += i

print(f'{total = }')
print(sum(range(1, 101)))

i = 0
total = 0
while i < 101:
	total += i
	i += 1
print(f'{total = }')

"""
break
"""
i = 0
total = 0
while True:
	total += i
	i += 1
	if i > 100:
		break
print(f'{total = }')


"""
continue
"""
i = 0
total = 0
for i in range(1, 101):
	if i % 2 != 0:
		continue
	else:
		total += i
print(f'{total = }')