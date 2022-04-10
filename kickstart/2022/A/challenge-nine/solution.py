def sum_digits(num):
    sum = 0
    for c in num:
        sum += ord(c) - ord('0')
    return sum
    

nof_test = int(input())
for test in range(1, nof_test + 1):
    num = input()

    sum = sum_digits(num)
    for digit in range(10):
        if (sum + digit) % 9 == 0:
            break

    for pos, c in enumerate(num):
        if ord(c) - ord('0') > digit:
            break
    else:
        pos += 1
    pos += (digit == 0) # avoid leading zero

    print("Case #{}: {}".format(test, num[:pos] + str(digit) + num[pos:]))
