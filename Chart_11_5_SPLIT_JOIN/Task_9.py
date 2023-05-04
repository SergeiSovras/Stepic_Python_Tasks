s = input()
count = 0
array = s.split(' ')
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            count += 1
print(count)