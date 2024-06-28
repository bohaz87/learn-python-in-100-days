s1 = 'hello' + ' ' +  'world'
print(s1)

s2 = '!' * 3
print(s2)

s1 += s2
print(s1)

s1 *= 2
print(s1)

s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2, s1 < s2)
print(s2 == 'hello world')
print(s2 == 'Hello world')
print(s2 != 'Hello world')

s3 = '中文'
print(ord(s3[0]), ord(s3[1]))
s4 = '王大锤'
print(ord(s4[0]), ord(s4[2]), ord(s4[2]))
print(s3 > s4, s3 <= s4)

s1 = 'hello world'
s2 = 'hello world'
s3 = s2
print(s1 == s2, s2 == s3)

# is will compare by ref
"""
字符串驻留机制：

在Python中，某些情况下会对字符串进行驻留优化，以节省内存和提高速度。对于较短的字符串和常用字符串（如标识符、数字等），Python会自动进行驻留。但对于较长的字符串，驻留行为是不确定的。
在你的情况下，'hello world' 这个字符串被驻留了，所以 s1 和 s2 实际上引用了相同的内存地址。这导致 s1 is s2 为 True。
"""
print('s1 is s2: ', s1 is s2, 's2 is s3:', s2 is s3)
print(id(s1), id(s2), id(s3))

# in operactor
s1 = 'hello, world'
print('wo' in s1)
s2 = 'goodbye'
print(s2 in s1)

# len operactor
s = 'hello, world'
print(len(s))
print(len('goodbye, world'))

"""
字符串是不可变类型，所以不能通过索引运算修改字符串中的字符。
"""
s = 'abcd123456'
N = len(s)
print(s[0], s[-N])
print(s[N - 1], s[-1])

s = '0123456789'
print(s[2:5])
print(s[-7:-4])
print(s[2:])
print(s[-7:])

print(s[2::2])
print(s[-7::2])

s1 = 'hello'
for index in range(len(s1)):
    print(s1[index])

for ch in s1:
    print(ch)
