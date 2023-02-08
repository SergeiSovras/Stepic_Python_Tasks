price = int(input())
n = 0

while price // 25 != 0:
    price = price - 25
    n += 1

while price // 10 != 0:
    price = price - 10
    n += 1

while price // 5 != 0:
    price = price - 5
    n += 1

while price // 1 != 0:
    price = price - 1
    n += 1
print(n)