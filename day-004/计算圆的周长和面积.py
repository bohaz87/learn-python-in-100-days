import math
radius = float(input('input radius: '))
PI = math.pi
print(PI)
perimeter = 2 * PI * radius
area = PI * radius * radius

print('perimeter: %.2f' % perimeter)
print('area: %.2f' % area)

print(f'perimeter: {perimeter: .2f}')
print(f'area: {area: .2f}')