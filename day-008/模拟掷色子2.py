import random

counters = [0] * 6

for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1 

for index in range(0, 6):
    print(f'{index + 1}点出现了{counters[index]}次')
