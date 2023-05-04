n = int(input())
array = []
for i in range(n):
    array.append(input())
search_request = input()
for j in range(len(array)):
    if search_request.lower() in array[j].lower():
        print(array[j])