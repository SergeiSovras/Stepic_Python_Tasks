n = int(input())
array = []
for i in range(n):
    s = input()
    if s not in array:
        array.append(s)
for j in range(len(array)):
    print(array[j])