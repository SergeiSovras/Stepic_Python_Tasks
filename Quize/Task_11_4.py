s = input()
array_1 = list(s)
array_2 = []
array_2 = s.split('-')
x = s.replace("-", "")
flag = 'NO'
if x.isdigit():
   if len(array_1) == 12:
       if len(list(array_2[0])) == 3 and len(list(array_2[1])) == 3 and len(list(array_2[2])) == 4:
           flag = 'YES'
   if len(array_1) == 14:
       if array_2[0] == '7' and len(list(array_2[1])) == 3 and len(list(array_2[2])) == 3 and len(list(array_2[3])) == 4:
           flag = 'YES'
print(flag)
