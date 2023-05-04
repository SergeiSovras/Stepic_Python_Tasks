n = int(input())
array = []
s = ''
for i in range(n):
    array.append(input())
k = int(input())
for j in range(n):
    if len(array[j]) >= k:
        s = s + array[j][k-1]
print(s)