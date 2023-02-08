count = 0

for i in range(1, 11):
    for j in range(1, 21):
        for k in range(1, 200):
            if 10 * i + 5 * j + 0.5 * k == 100 and i + j + k == 100:
                count += 1
                print(i , j , k)