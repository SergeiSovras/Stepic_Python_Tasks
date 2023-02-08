s = input()
voice = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
unvoice = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
count_v = 0
count_uv = 0
for c in s:
    if c in voice:
        count_v += 1
    elif c in unvoice:
        count_uv += 1
print('Количество гласных букв равно ', count_v)
print('Количество согласных букв равно ', count_uv)