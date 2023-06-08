def draw_triangle(fill, base):
    for i in range(base + 1):
        for j in range(i):
            if i + j <= base:
                print(fill, end='')
        print()
fill = input()
base = int(input())
draw_triangle(fill, base)