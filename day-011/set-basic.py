from re import S


set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print(len(set1))

set2 = set('hello')
print(set2)

set3 = set([1, 2, 3, 3, 2, 1])
print(set3)

set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set4)

for elem in set4:
    print(elem)

set1 = {11, 12, 13, 14, 15}
print(10 in set1)
print(15 in set1)
set2 = {'Python', 'Java', 'Go', 'Swift'}
print('Ruby' in set2)
print('Java' in set2)

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
print(set1 & set2)
print(set1.intersection((set2)))

print(set1 | set2)
print(set1.union((set2)))

print(set1 - set2)
print(set1.difference(set2))

# 对称差
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1|set2) - (set1 & set2))


set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
print(set1)
set3 = {3, 6, 9}
set1 &= set3
print(set1)

set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = set2

print(set1 < set2, set1 <= set2)
print(set2 < set3, set2 <= set3)
print(set1.issubset(set2))

print(set2.issuperset(set1))
print(set2 > set1)

