n = int(input())
s = input()
for i in range(int(len(s))):
    if ord(s[i]) - n < 97:
        print(chr(ord(s[i]) - n + 26), end='')
    else:
        print(chr(ord(s[i]) - n), end='')