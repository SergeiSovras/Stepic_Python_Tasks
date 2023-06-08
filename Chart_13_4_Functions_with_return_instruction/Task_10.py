# объявление функции
def find_all(target, symbol):
    array = []
    for i in range(len(target)):
        if target[i] == symbol:
            array.append(i)
    return array
# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))