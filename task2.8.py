a = int(input("Сколько будет чисел? "))
b = int(input("Какую цифру считать? "))
count = 0
for i in range(1, a + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == b:
            count += 1
        m = m // 10

print(f'Цифра {b} встетилась {count} раз')
