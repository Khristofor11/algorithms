from random import random

N = 10
a = [0] * N
for i in range(N):
    a[i] = int(random() * 100)
    print(a[i], end=' ')
print()

mn = min(a)
mx = max(a)
imn = a.index(mn)
imx = a.index(mx)
print(f'a{[imn + 1]} = {mn}, a{[imx + 1]} = {mx} ')
a[imn], a[imx] = a[imx], a[imn]
for i in range(10):
    print(a[i], end=' ')
print()
