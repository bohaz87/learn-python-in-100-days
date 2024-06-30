sentence = input('type some words:')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1

for key, value in counter.items():
    print(f'{key} appeared {value} times')

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

stocks = {key: value for key, value in stocks.items() if value > 100}
print(stocks)
