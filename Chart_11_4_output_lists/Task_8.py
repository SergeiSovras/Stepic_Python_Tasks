n = int(input())
array_neg = []
array_zer = []
array_pos = []
fin_array = []
for i in range(n):
    s = int(input())
    if s < 0:
        array_neg.append(s)
    elif s == 0:
        array_zer.append(s)
    else:
        array_pos.append(s)
fin_array = array_neg + array_zer + array_pos
print(*fin_array, sep='\n')