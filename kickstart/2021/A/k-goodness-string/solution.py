#!/usr/bin/env python3

t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    s = input()

    goodness = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            goodness += 1

    print("Case #{}: {}".format(test, abs(k - goodness)))
