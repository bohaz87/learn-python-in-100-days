set1 = set()
set1.add(33)
set1.add(55)
set1.update(({1, 10, 100, 1000}))
print(set1)

set1.discard(100)
set1.discard(99)
print(set1)

if 10 in set1:
    set1.remove(10)
print(set1)

print(set1.pop())
set1.clear()
print(set1)

set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
