person1 = {'wangdachui', 55, 60, 'No. 8 North huake Road', '13122334455', '13812345678'}
print(person1)
xinhua = {
        'a': 'shanjiaoxia',
        'b': 'dao, wanglaitongxindeidfang; fangmian, diqu',
        'c': 'gancaodebieming',
        'd': 'abcdef'
        }
print(xinhua)

person = {
        'name': 'wangdachui',
        'age': 55,
        'weight': 60,
        'office': '62',
        'home': '8',
        'tel': '13812345678',
        'econtact': '13812345678'
        }
print(person)

person = dict(name='wangdachui', age=55, weight=60, home='No. 8')
print(person)

items1 = dict(zip('ABCDE', '12345'))
print((items1))
item2 = dict(zip('ABCDE', range(1, 10)))
print((item2))

item3 = {x: x ** 3 for x in range(1, 6)}
print((item3))

print(len(item3))
for key in item3:
    print(key)


person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
print('name' in person, 'tel' in person)
if 'age' in person:
    print(person['age'])

person['tel'] = '13812345678'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print('name' in person, 'tel' in person)

print(len(person))

for key in person:
    print(f'{key}: {person[key]}')


