a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

aa = a
bb = b
cc = c

sum1 = 0
while aa > 0:
    a1 = aa % 10
    aa = aa // 10
    sum1 += a1
sum2 = 0
while bb > 0:
    b1 = bb % 10
    bb = bb // 10
    sum2 += b1
sum3 = 0
while cc > 0:
    c1 = cc % 10
    cc = cc // 10
    sum3 += c1

if sum1 > sum2:
    if sum1 > sum3:
        print(f'Введенное число {a}, сумма цифр = {sum1}')
    else:
        print(f'Введенное число {c}, сумма цифр = {sum3}')
else:
    if sum3 > sum2:
        print(f'Введенное число {c}, сумма цифр = {sum3}')
    else:
        print(f'Введенное число {b}, сумма цифр = {sum2}')
