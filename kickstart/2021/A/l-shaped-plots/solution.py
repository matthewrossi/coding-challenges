#!/usr/bin/env python3

UP, DOWN, LEFT, RIGHT = range(4)

def ls(l1, l2):
    long, short = (l1, l2) if l1 >= l2 else (l2, l1)
    return max(min(long // 2, short) - 1, 0) + max(short // 2 - 1, 0)

t = int(input())
for test in range(1, t + 1):
    r, c = map(int, input().split())
    m = [input().split() for _ in range(r)]

    dp = [[[0]*4 for _ in range(c + 2)] for _ in range(r + 2)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if m[i - 1][j - 1] == "1":
                dp[i][j][UP] = dp[i - 1][j][UP] + 1
                dp[i][j][LEFT] = dp[i][j - 1][LEFT] + 1
    for i in range(r, 0, -1):
        for j in range(c, 0, -1):
            if m[i - 1][j - 1] == "1":
                dp[i][j][DOWN] = dp[i + 1][j][DOWN] + 1
                dp[i][j][RIGHT] = dp[i][j + 1][RIGHT] + 1

    res = 0
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if m[i - 1][j - 1] == "1" and \
                    not (dp[i][j][UP] == dp[i][j][DOWN] == 1) and \
                    not (dp[i][j][LEFT] == dp[i][j][RIGHT] == 1):
                up, down, left, right = [dp[i][j][d] for d in [UP, DOWN, LEFT, RIGHT]]
                res += ls(up, left) + ls(up, right) + ls(down, left) + ls(down, right)

    print("Case #{}: {}".format(test, res))
