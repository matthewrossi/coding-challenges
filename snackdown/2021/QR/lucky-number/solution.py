#!/usr/bin/env python3

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    digits = list(map(int, input().split()))
    seven = False
    for digit in digits:
        if digit == 7:
            seven = True
    print("YES" if seven else "NO")
