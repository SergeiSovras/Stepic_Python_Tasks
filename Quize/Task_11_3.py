s = input()
sum = 0
array_1 = s.split()
for i in array_1:
    sum += int(i)
print(*array_1, sep = '+', end = '')
print('=', sum, sep = '')