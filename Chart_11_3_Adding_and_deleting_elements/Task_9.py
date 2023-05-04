n = int(input())
array = []
for i in range(1, n + 1):
    if (n % i) == 0:
        array.append(i)
print(array)