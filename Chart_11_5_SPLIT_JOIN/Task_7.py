s = input()
n = s.split('.')
count = 0
flag = 'Да'
for i in n:
    if (int(i) < 0) or (int(i) > 255):
        count += 1
    if count > 0:
        flag = 'Нет'
print(flag)