students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}

print(students.get(1002))
print(students.get(1005))
print(students.get(1005, {'name': 'unknow'}))

print(students.keys())
print(students.values())
print(students.items())

for key, value in students.items():
    print(key, '--->', value)

stu1 = students.pop(1002)
print(stu1)
print(len(students))
stu2 = students.pop(1005, {})
print(stu2)

print(len(students))
key, value = students.popitem()
print(key, value)

results = students.setdefault(1005, {'name': 'fangqihe', 'sex': True})
print(results)
print(students)

others = {
    1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
    1010: {'name': '王语嫣', 'sex': False, 'age': 19},
    1008: {'name': '钟灵', 'sex': False}
}
students.update(others)
print(students)

person = {'name': 'wangdachui', 'age': 25, 'sex': True}
del person['age']
print(person)
