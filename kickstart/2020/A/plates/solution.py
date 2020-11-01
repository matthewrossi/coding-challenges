t = int(input())
for test in range(1, t + 1):
    n, k, p = map(int, input().split())
    cums = []
    for _ in range(n):
        beauty = list(map(int, input().split()))
        cum = [0] * (k + 1)
        for i in range(k):
            cum[i + 1] = cum[i] + beauty[i]
        cums.append(cum)

    dp = [[0] * (p + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(p + 1):
            for x in range(min(j, k) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + cums[i - 1][x])

    print("CASE #{}: {}".format(test, dp[n][p]))
