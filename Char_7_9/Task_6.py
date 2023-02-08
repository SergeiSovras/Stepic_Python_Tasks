n = int(input())
fac, sum, = 1, 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        fac = fac * j
    sum = sum + fac
    fac = 1
print(sum)

n = int(input())
sum_1 = 1
m = 1
while i <= n:
    m = m * i
    sum_1 = sum_1 + m
    i = i + 1
print(sum)
