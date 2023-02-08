a1, a2, a3 = int(input()), int(input()), int(input())
if a1 != max(a1, a2, a3) and a1 != min(a1, a2, a3):
    print(max(a1, a2, a3))
    print(a1)
    print(min(a1, a2, a3))
elif a2 != max(a1, a2, a3) and a2 != min(a1, a2, a3):
    print(max(a1, a2, a3))
    print(a2)
    print(min(a1, a2, a3))
else:
    print(max(a1, a2, a3))
    print(a3)
    print(min(a1, a2, a3))