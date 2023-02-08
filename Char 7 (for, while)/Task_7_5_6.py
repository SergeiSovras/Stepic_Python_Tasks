a = int(input())
greatest = 0
smalest = 9
while a != 0:
    if a % 10 > greatest:
        greatest = a % 10
    if a % 10 < smalest:
        smalest = a % 10
    a = a // 10
print(greatest, smalest)