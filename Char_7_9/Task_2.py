n = int(input())
count = 0
for i in range(n):
    for j in range(i * 2 + 1):
        if j <= i:
            count += 1
        else:
            count -= 1
        print(count, end=' ')
    count = 0
    print()