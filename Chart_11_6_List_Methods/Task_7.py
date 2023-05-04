s = input()
s = s.lower()
text = s.split()
count = 0
print('Общее количество артиклей: ', text.count('a') + text.count('an') + text.count('the') )