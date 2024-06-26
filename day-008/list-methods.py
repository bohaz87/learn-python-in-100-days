items = ['Python', 'Java', 'Go', 'Kotlin']

items.append('Swift')

print(items)

items.insert(2, 'SQL')
print(items)

items.remove('Java')
print(items)

items.pop(0)
print(items)
items.pop(len(items) - 1)
print(items)
items.pop(); # remove the last one
print('pop without index', items)

items.clear();
print(items)

items = ['Python', 'Java', 'Go', 'Kotlin']
del items[0]
print('del', items)

items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']
print(items.count('Python'))
print(items.count('Go'))
print(items.count('Swift'))

items = ['Python', 'Java', 'Go', 'Kotlin', 'Python']
items.sort()
print(items)

items.reverse()
print(items)
