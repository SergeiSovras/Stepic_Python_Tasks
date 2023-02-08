s = input()
l = len(s)
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
for i in range(1, l):
    if i % 2 == 0:
        print(s[i], end='')
print()
for i in range(1, l):
    if i % 2 != 0:
        print(s[i], end='')
print()
print(s[::-1], end='')
print()
print(s[::-2], end='')
