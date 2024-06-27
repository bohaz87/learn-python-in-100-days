# define a tumple with three items
t1 = (30, 10, 55)

t2 = ('bob', 40, True, 'shanghai')

print(type(t1), type(t2))

print(len(t1), len(t2))

print(t1[0], t1[-3])
print(t2[3], t2[-1])

for member in t2:
    print('member:', member)

print(100 in t1)
print(40 in t2)

t3 = t1 + t2
print('t3: ', t3)

print(t3[:3])

print(t1 == t3)
print(t1 >= t3)
print(t1 < (30, 11, 55))

"""
()表示空元组，但是如果元组中只有一个元素，
需要加上一个逗号，否则()就不是代表元组的字面量语法，
而是改变运算优先级的圆括号，所以('hello', )和(100, )才是一元组，
而('hello')和(100)只是字符串和整数
"""
a = ()
print(a, type(a))

b = ('hello')
print(b, type(b))

c = (100)
print(c, type(c))

d = ('hello',)
print(d, type(d))

e = (100,)
print(e, type(e))
