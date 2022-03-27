#!/usr/bin/env python3

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())
    divisors = list(map(int, input().split()))

    ids = [i for i in range(n)]
    ids = sorted(ids, key=lambda i: divisors[i])

    current = 0
    dividends = [None] * n
    for i in ids:
        divisor = divisors[i]
        if divisor > current:
            # solve current = x % divisor when possible
            dividends[i] = divisor + current
            current += 1
        else:
            # we can't get a different rest, so pick one
            dividends[i] = divisor

    print(" ".join(map(str, dividends)))
