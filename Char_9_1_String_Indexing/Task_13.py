s = input()
l = len(s)
counter = 0
for i in range(l - 1):
    if s[i] == s[i+1]:
        counter += 1
print(counter)