# Метод s.count('ABC', 0, 8)) для поиска вхождения строки ABC в строку s начиная с 0 и заканчивая 7 символом включительно
s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ

# Метод startswith(<suffix>, <start>, <end>) определяет начинается ли исходная строка s подстрокой <suffix>
s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('baz'))

# Метод endswith(<suffix>, <start>, <end>) определяет оканчивается ли исходная строка s подстрокой <suffix>
s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))

#М етод find(<sub>, <start>, <end>) находит индекс первого вхождения подстроки <sub> в исходной строке s
s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))

# Метод rfind(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки s

# Метод index(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), за тем исключением, что он вызывает ошибку  ValueError: substring not found во время выполнения программы, если подстрока <sub> не найдена.
# Метод rindex(<sub>, <start>, <end>) идентичен методу index(<sub>, <start>, <end>), за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки s.

# Метод strip() возвращает копию строки s у которой удалены все пробелы стоящие в начале и конце строки
s = '     foo bar foo baz foo qux      '
print(s.strip())

# Метод lstrip() возвращает копию строки s у которой удалены все пробелы стоящие в начале строки.
# Метод rstrip() возвращает копию строки s у которой удалены все пробелы стоящие в конце строки.

# Метод replace(<old>, <new>, <count>) возвращает копию s со всеми вхождениями подстроки <old>, замененными на <new>, count - количество замен
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))