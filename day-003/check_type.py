a = 100
b = 123.45
c = 'hello, world'
d = True

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'str'>
print(type(d)) # <class 'bool'>

"""
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串（在可能的情况下）转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码方式。
chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。
"""
print(float(a))
print(int(b))
print(int('123'))
# 'hello world' could not convert to int
# print(int(c))

print(int('123', base=16)) # '123' is 16 based, result will be 10 based
print(int('100', base=2)) # 100 is 2 based, result will be 4
print(chr(100)) # 'd'
print(ord('d')) # 100
print(int('1', base=10))
print(int('100', base=10))