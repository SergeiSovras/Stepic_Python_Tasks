n = int(input())
array = []
new_array = []
for i in range(n):
    array.append(int(input()))
for j in range(1, n):
    new_array.append(array[j-1] + array[j])
print(new_array)