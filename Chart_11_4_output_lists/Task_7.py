n = int(input())
array = []
search_request = []

for i in range(n):
    array.append(input())
k = int(input())
for j in range(k):
    search_request.append(input())
for l in range(len(array)):
    o = 0
    for m in range(len(search_request)):
        if search_request[m].lower() in array[l].lower():
            o += 1
        if o == len(search_request):
            print(array[l])