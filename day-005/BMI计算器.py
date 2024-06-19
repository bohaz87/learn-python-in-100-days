"""
BMI计算器
"""
height = float(input('Height(cm): '))
weight = float(input('Weight(kg): '))

bmi = weight / (height /100) ** 2

print(f'{bmi = :.1f}')

if 18.5 <= bmi < 24:
	print('你的身材真棒!')
elif bmi > 30:
	print('你的身材真胖!')
else:
	print('你的身材不够标准')