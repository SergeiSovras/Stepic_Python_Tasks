# объявление функции
def get_factors(num):
    array = []
    for i in range(1, num +1):
        if num % i == 0:
            array.append(i)
    return len(array)
# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))