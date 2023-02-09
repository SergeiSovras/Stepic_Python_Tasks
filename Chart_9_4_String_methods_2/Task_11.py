s = input()
num = '0123456789'
counter = 0
for i in range(int(len(s))):
    if num.count(s[i]) == 1:
        counter += 1
print(counter)