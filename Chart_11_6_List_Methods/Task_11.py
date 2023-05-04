array = []
array = input().split()
result = [int(item) for item in array]
# print(result)
result.sort()
print(result)
result.sort(reverse = True)
print(result)