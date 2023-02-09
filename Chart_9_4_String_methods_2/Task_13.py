s = input()
max_number = 0
max_s = ''
for i in range(int(len(s))):
    if s.count(s[i]) >= max_number:
        max_number = s.count(s[i])
        max_s = s[i]
print(max_s)