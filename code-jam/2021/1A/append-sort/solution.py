#!/usr/bin/env python3

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    x = list(map(int, input().split()))

    total = 0
    for i in range(n - 1):
        if x[i + 1] <= x[i]:
            # identify how many digits to add
            to_add = 1
            while x[i + 1] * 10**to_add < x[i] and x[i + 1] * 10**to_add + 10**to_add - 1 <= x[i]:
                to_add += 1
            total += to_add
            # update with mininum value greater than x[i]
            baseline = x[i + 1] * 10**to_add
            x[i + 1] = baseline if baseline > x[i] else x[i] + 1

    print("Case #{}: {}".format(test, total))
