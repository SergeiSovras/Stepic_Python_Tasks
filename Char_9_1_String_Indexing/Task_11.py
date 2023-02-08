s = input()
test_string = '0123456789'
count = 0
for c in s:
    if c in test_string:
        count += 1
if count > 0:
    print('Цифра')
else:
    print('Цифр нет')