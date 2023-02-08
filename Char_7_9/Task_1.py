count = 1
n = int(input())
for i in range (n):
    for j in range(i+1):
        print(count, end=' ')
        count += 1
    print()