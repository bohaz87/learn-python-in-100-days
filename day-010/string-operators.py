s1 = 'hello, world'
s2 = '你好，世界'
print(s1, s2)

# cross multi line string
s3 = '''
hello,
world!
'''
# end mean do NOT change line, replace '\n' to ''
print(s3, end='')

s1 = '\'hello, world!\''
print(s1)
s2 = '\\hello, world!\\'
print(s2)

s1 = '\time up \now'
print('s1:', s1)
# use r'' to set raw string
s2 = r'\time up \now'
print('s2:', s2)

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
