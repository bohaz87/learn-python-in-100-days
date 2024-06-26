scores = [[0] * 3] * 5
print(scores)

scores[0][0] = 95
print(scores)
# [[95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0]]

scores = [[0] * 3 for _ in range(5)]
scores[0][0] = 95
print(scores)


