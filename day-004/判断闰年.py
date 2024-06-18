year = int(input('input year: '))
is_leap = year % 4 == 0 and year % 1000 != 0 or year % 400 == 0
print(f'{is_leap = }')