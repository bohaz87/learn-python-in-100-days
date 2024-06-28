s1 = 'hello, world'

print(s1.capitalize())
print(s1.title())
print(s1.upper())

s2 = 'GOODBYE'
print(s2.lower())

s = 'hello, world'
print(s.find('or')) # 8
print(s.find('xxit')) # -1
print(s.index('or'))
# print(s.index('xxit'))

s = 'hello good world'
print(s.find('o')) # 4
print(s.find('o', 5)) # 7
print(s.rfind('o')) # 12

s1 = 'hello, world'
print(s1.startswith('He'))
print(s1.startswith('hel'))
print(s1.endswith('!'))

s2 = 'abcd123456'
print(s2.isdigit())
print(s2.isalpha())
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s2.isalnum())

s = 'hello, world'
print(s.center(20, '*'))
print(s.rjust(20, '~'))
print(s.ljust(20, '~'))
print('33'.zfill(5))
print('-33'.zfill(5))

a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')


s = '   username@example.com  \t\r\n'
# strip方法获得字符串修剪左右两侧空格之后的字符串
print(s.strip())

s = 'hello, world'
print(s.replace('o', '@'))
print(s.replace('o', '@', 1))

s = 'I love you'
words = s.split()
print(words, type(words))
print('#'.join(words))

s = 'I#love#you#so#much'
words = s.split('#')
print(words)
words = s.split('#', 3)
print(words)

a = '中文'
b = a.encode('utf-8')
c = a.encode('gbk')
print(f'{b = }, {c = }')


