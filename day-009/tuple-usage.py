# pack
a = 1, 10, 100
print(a, type(a))

i, j, k = a
print(i, j, k)


a = 1, 10, 100, 1000
i, j, *k = a
print(f'{i = }, {j = }, {k = }')
print(f'type k = {type(k)}')

i, *j, k = a
print(f'{i = }, {j = }, {k = }')

*i, j, k = a
print(f'{i = }, {j = }, {k = }')

*i, j = a
print(f'{i = }, {j = }')

a, b, *c = range(1, 10)
print(a, b, c)

a, b, c = [1, 10, 100]
print(a, b, c)

a, *b, c = 'hello'
print(a, b, c)

print(f'{a = }, {b = }')
a, b = b, a
print(f'{a = }, {b = }')
