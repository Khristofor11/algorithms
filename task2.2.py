n = int(input('Введите любое число: '))
even = odd = 0
while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print(f"четных - {even}, нечетных - {odd}")
