n = input()
n = int(n.lstrip('#'))
array = []
for i in range(n):
    str = input()
    if '#' in str:
        str = str[:str.index('#')]
    array.append(str.rstrip())
print(*array, sep='\n')