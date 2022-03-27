#!/usr/bin/env python3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


nof_tests = int(input())
for test in range(nof_tests):
    x, k = map(int, input().split())

    min_lcm, max_lcm = float("+inf"), float("-inf")
    for i in range(x, x * k):
        for j in range(i + 1, x * k + 1):
            lcm = i * j // gcd(i, j)
            min_lcm = min(min_lcm, lcm)
            max_lcm = max(max_lcm, lcm)
    print(min_lcm, max_lcm)