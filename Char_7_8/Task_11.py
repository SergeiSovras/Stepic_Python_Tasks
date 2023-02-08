count = 0
for i in range(1, 14):
    for j in range(1, 13):
        for k in range(1, 12):
            if 28 * i + 30 * j + 31 * k == 365:
                count += 1
                print(i , j , k)