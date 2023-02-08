n = int(input())
last_digit = n % 10
count_3 = 0
count_ld = 0
count_chet = 0
count_more_5 = 0
mult_more7 = 1
count_0_5 = 0
while n > 0:
    if n % 10 == 3:
        count_3 += 1
    if n % 10 == last_digit:
        count_ld += 1
    if n % 2 == 0:
        count_chet += 1
    if n % 10 > 5:
        count_more_5 += n % 10
    if n % 10 > 7:
        mult_more7 *= n % 10
    if n % 10 == 0 or n % 10 == 5:
        count_0_5 += 1
    n = n // 10
print(count_3)
print(count_ld)
print(count_chet)
print(count_more_5)
print(mult_more7)
print(count_0_5)