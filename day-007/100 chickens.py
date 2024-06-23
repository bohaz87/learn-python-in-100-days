"""
公鸡5元一只，母鸡3元一只，小鸡1元三只，
用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
a = 0
b = 0
c = 0
for a in range(0, 21):
    for b in range(0, 34):
        c = 100 - a - b
        if c % 3 != 0:
            continue
        if a * 5 + b * 3 + c / 3 == 100:
            print(a, b, c)
