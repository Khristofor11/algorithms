from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = 0
while i < N:
    if arr[i] < 0 and index == 0:
        index = i
    elif 0 > arr[i] > arr[index]:
        index = i
    i += 1

print(index, ':', arr[index])
