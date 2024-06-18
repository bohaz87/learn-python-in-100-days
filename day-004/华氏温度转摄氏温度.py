f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏温度 = %1.f摄氏度' % (f, c))
print(f'{f: .2f} = {c: .3f}')