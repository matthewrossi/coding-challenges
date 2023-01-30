#!/usr/bin/env python3

def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end and string[start] == string[end]:
        start += 1
        end -= 1

    return start >= end

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    a = int(input())

    res = 0
    for num in range(1, int(a**0.5) + 1):
        if a % num == 0:
            res += is_palindrome(str(num))
            other = a // num
            if other != num:
                res += is_palindrome(str(other))

    print("Case #{}: {}".format(test, res))
