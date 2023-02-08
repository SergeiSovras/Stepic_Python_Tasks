n = int(input())
x_1 = 1
x_2 = 0
x = 0
for i in range(1, n + 1):
    if i == 1:
        x = 1
    else:
        x = x_1 + x_2
        x_2 = x_1
        x_1 = x
    print(x)
