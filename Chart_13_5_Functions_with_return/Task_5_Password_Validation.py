# объявление функции
def is_password_good(password):
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    if len(password) >= 8:
        for a in password:
            if a.isupper():
                counter_1 = 1
            if a.islower():
                counter_2 = 1
            if a.isdigit():
                counter_3 = 1
    if counter_1 * counter_2 * counter_3 == 1:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))