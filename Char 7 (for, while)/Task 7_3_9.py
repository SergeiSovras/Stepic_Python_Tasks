n = int(input())
first = -1
second = -1
for i in range(1, n + 1):
    x = int(input())
    if x > first:
        second = first
        first = x
    elif x > second:
        second = x
print(first)
print(second)
