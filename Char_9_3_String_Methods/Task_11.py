s = input()
count = 0
for i in range(int(len(s))):
    if s[i] == s[i].lower() and "a" <= s[i] <= "z":
        count += 1
print(count)