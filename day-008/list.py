item1= [35, 12, 99, 68, 55, 87]
print(item1)
item2 = ['Python', 'Java', 'Go', 'Kotlin']
print(item2)
item3 = list(range(1, 10))
print(item3)

added = item1 + item2
print(added)

multiplied = ['hello']* 3
print(multiplied)

print(100 in [1, 2, 3, 100])
print('hello' in ['a', 'b', 'c'])

item3 = [1, 2, 3]
size = len(item3)
print(size) # -3

"""
negative number mean count back, start from -1 for the last element
"""
print(item3[0], item3[-size]) # 1, 1
item3[-1] = 100
print(item3) # [1, 2, 100]
print(item3[size - 1], item3[-1]) # 100 100

item3 = [1, 2, 3, 4, 5, 6]
print(item3[1:]) # [1, end]
print(item3[:1]) # [0, 1)
print(item3[1:5:2]) # [0, 1) step 2

itema = [1, 2, 3, 4]
itemb = list(range(1, 5))
print(itema == itemb) # true, compare each index

itemc = [3, 2, 1]
print(itema < itemc)
"""
list index out of range
"""
# print(itemc[3])

for index in range(len(itema)):
    print(itema[index])

for item in itema:
    print(item)


