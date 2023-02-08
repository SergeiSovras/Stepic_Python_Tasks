s = input()
count_1 = 0
count_2 = 0
for c in s:
    if c == '+':
        count_1 += 1
    elif c == '*':
        count_2 += 1
print('Символ + встречается', count_1, 'раз')
print('Символ * встречается', count_2, 'раз')