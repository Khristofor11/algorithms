a = [8, 3, 15, 6, 4, 2]
b = []
for i, item in enumerate(a):
    if a[i] % 2 == 0:
        b.append(i)
print(a)
print('Индексы четных элементов: ', b)
