items = []
for x in range(0, 10):
    items.append(x)
print(items)

items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)

items1 = [x for x in range(0, 10)]
print(items1)

items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)

item3 = [x + y for x in 'ABC' for y in '12']
print(item3)

