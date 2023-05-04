n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
max = max(array)
min = min(array)
for j in range(len(array)):
    if (array[j] == max):
        id_max = j
del array[id_max]
for j in range(len(array)):
    if (array[j] == min):
        id_min = j
del array[id_min]
for k in range(len(array)):
    print(array[k])