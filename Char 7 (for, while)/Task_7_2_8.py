m, n = int(input()), int(input())
if m < n:
    for i in range(m, n+1):
        if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
            print(i)
else:
    for i in range(m, n-1, -1):
        if i % 2 == 0:
            print(i)