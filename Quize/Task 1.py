print('Enter the year')
year = int(input())
if year % 10 == 0 and (year // 10) % 10 == 0:
    print('yes')
else:
    print('no')