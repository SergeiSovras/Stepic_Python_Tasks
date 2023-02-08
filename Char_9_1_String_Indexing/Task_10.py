s = int(input())
sum_dig = 0
while s > 0:
    sum_dig += s % 10
    s = s // 10
print(sum_dig)