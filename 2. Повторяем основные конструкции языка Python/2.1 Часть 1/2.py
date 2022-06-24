res = float(input()) / float(input()) ** 2

if 18.5 <= res <= 25:
    print('Оптимальная масса')
elif res > 25:
    print('Избыточная масса')
else:
    print('Недостаточная масса')
