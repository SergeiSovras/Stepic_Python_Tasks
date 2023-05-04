array_1 = input().split()
array_2 = input().split()
array_3 = []
for i in range(len(array_1)):
    array_3.append(int(array_1[i]) + int(array_2[i]))
print(*array_3, sep = '\n')