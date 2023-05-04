n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
for j in range(len(array)):
    print(array[j])
print()
for j in range(len(array)):
    print(pow(array[j], 2) + 2 * array[j] + 1)