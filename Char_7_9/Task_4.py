n = int(input())
counter = 0
for j in range(1, n + 1):
    for i in range(1, n + 1):
        if j % i == 0:
            counter += 1
    print(j,'+'*counter, sep ='')
    counter = 0