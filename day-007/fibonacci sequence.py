count = 1
a = 0
b = 1
while count <= 20:
    print(f'{count}:\t{b}')
    a, b = b, a + b
    count += 1
