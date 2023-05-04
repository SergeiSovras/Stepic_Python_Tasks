numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
max = max(numbers)
min = min(numbers)
ind_max = numbers.index(max)
ind_min = numbers.index(min)
numbers[ind_max], numbers[ind_min] = numbers[ind_min], numbers[ind_max]
print(numbers)
