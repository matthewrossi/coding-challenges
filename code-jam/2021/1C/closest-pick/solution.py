#!/usr/bin/env python3

import math

t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    tickets = list(map(int, input().split()))
    
    tickets.sort()
    # put tickets at extremes
    dp = [tickets[0] - 1, k - tickets[n - 1]]

    # look for improving chances
    max_gap = 0
    for i in range(n - 1):
        gap = tickets[i + 1] - tickets[i] - 1
        max_gap = max(max_gap, gap)
        winning = math.ceil(gap / 2)
        # subtitute it with the minimum of the two
        if dp[0] <= dp[1] and winning > dp[0]:
            dp[0] = winning
        elif dp[1] < dp[0] and winning > dp[1]:
            dp[1] = winning

    numerator = sum(dp) if sum(dp) > max_gap else max_gap
    print("Case #{}: {}".format(test, numerator / k))
