n = int(input())
array = []
s = ''
for i in range(n):
    array.append(input())
k = int(input())
for j in range(n):
    new_array = []
    new_array.extend(array[j])
    if len(new_array) >= k:
        s = s + new_array[k-1]
print(s)