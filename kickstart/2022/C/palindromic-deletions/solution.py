#!/usr/bin/env python3
# Kudos to AwakeAnay for the solution
# https://codingcompetitions.withgoogle.com/kickstart/submissions/00000000008cb4d1/000000000065d150

import math

MAX_N = 405
MODULO = 10**9 + 7


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# Precompute binomials
binom = [[0] * (MAX_N) for _ in range(MAX_N)]
for i in range(MAX_N):
    binom[i][0] = binom[i][i] = 1
for i in range(MAX_N):
    for j in range(1, i):
        binom[i][j] = (binom[i-1][j] + binom[i-1][j-1]) % MODULO

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())
    s = input()
 
    # Find the number of palindromes of a given length
    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            dp[1][i][j] = max(0, j-i+1)
            dp[0][i][j] = 1

    for i in range(2, n + 1):
        for j in range(2, n + 1):
            for u in range(n - j + 1):
                v = u+j-1
                dp[i][u][v] = (dp[i][u+1][v] + dp[i][u][v-1] - dp[i][u+1][v-1] + MODULO) % MODULO
                if s[u] == s[v]:
                    dp[i][u][v] = (dp[i][u][v] + dp[i-2][u+1][v-1]) % MODULO

    ans = 0
    for i in range(n):
        ans += dp[i][0][n-1] * modinv(binom[n][i], MODULO)
        ans %= MODULO

    print("Case #{}: {}".format(test, ans))
