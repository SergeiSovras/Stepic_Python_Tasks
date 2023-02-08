for a in range(1, 151):
    for b in range(a + 1 , 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                for e in range(d + 1, 151):
                    if pow(a,5) + pow(b,5) + pow(c,5) + pow(d,5) == pow(e,5):
                        print(a+b+c+d)
                        break
