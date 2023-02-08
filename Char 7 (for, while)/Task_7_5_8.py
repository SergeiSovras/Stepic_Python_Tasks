a = int(input())
x = a % 10
n = 0
while a != 0:
    if a % 10 != x:
        n += 1
    x = a % 10
    a = a // 10
if n == 0:
    print('Same')
else:
    print('Different')