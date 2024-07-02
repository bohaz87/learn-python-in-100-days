import math

def ptp(data):
	return max(data) - min(data)

def arerage(data):
	return sum(data) / len(data)

def variance(data):
	x_bar = arerage(data)
	temp = [(num - x_bar) ** 2 for num in data]
	return sum(temp) / (len(temp) - 1)

def standard_deviation(data):
	return math.sqrt(variance(data))

def median(data):
	temp, size = sorted(data), len(data)
	if size % 2 != 0:
		return temp[size // 2]
	else:
		return arerage(temp[size // 2 - 1: size // 2 + 1])

