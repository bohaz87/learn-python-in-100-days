import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))

print(sys.getsizeof(a), sys.getsizeof(b))

print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))

# tuple to list
info = ('bob', 175, True, 'shanghai')
print(list(info))

# list to tuple
fruits = ['apple', 'banana', 'orange']
print(tuple(fruits))
