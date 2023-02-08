x = int(input())
a = x
sum = 0
mult = 1
n = 0
while a != 0:
    sum += a % 10
    mult *= a % 10
    n += 1
    a = a // 10
print(sum)
print(n)
print(mult)
print(sum / n)
print(x // pow(10, n - 1))
print((x // pow(10, n - 1)) + (x % 10))