oper = ''
while oper != 0:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    oper = input('Введите операцию' " '+', '-', '/', '*', '0' ")
    if y == 0:
        print("Делить на ноль нельзя.")
    else:
        if oper == '+':
            summ = x + y
            print(f'Сумма чисел = {summ}')
        elif oper == '-':
            razn = x - y
            print(f'Разница чисел = {razn}')
        elif oper == '/':
            delen = x / y
            print(f'Деление чисел = {delen}')
        elif oper == '*':
            proizv = x * y
            print(f'Произведение чисел = {proizv}')
        elif oper == '0':
            print('До скорых встреч!')
            break
        else:
            print('Ошибка. Введите другой символ.')
