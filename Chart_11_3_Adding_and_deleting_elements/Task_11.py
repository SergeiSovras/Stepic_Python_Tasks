n = int(input())
array = []
new_array = []
for i in range(n):
    s = int(input())
    if i % 2 == 0:
        array.append(s)
print(array)