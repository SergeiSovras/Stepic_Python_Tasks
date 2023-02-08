a, b = int(input()), int(input())
sum_f, sum_1, x = 0, 0, 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_1 = sum_1 + j
    if sum_1 > sum_f:
        sum_f = sum_1
        x = i
    if sum_1 == sum_f and i > x:
        sum_f = sum_1
        x = i
    sum_1 = 0
print(x, sum_f)