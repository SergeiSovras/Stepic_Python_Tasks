word = input()
n = 0
while word != 'КОНЕЦ' and word != 'конец':
    print(word)
    n += 1
    word = input()
print(n)