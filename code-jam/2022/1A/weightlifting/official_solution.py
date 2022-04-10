# Test Set 1: OK
# Test Set 2: Time Limit Exceeded

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_exe, nof_weights = map(int, input().split())
    weigths_per_exe = [list(map(int, input().split())) for _ in range(nof_exe)]

    # Compute common sets of weights
    C = [[0] * nof_exe for _ in range(nof_exe)]
    for l in range(nof_exe):
        cs = list(weigths_per_exe[l])
        for r in range(l, nof_exe):
            for w in range(nof_weights):
                cs[w] = min(cs[w], weigths_per_exe[r][w])
                C[l][r] += cs[w]
    
    dp = [[float("+inf")] * nof_exe for _ in range(nof_exe)]
    for i in range(nof_exe):
        dp[i][i] = 0
    for size in range(1, nof_exe):
        for l in range(nof_exe - size):
            r = l + size
            for x in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][x] + 2 * (C[l][x] - C[l][r]) + dp[x + 1][r] + 2 * (C[x + 1][r] - C[l][r]))

    print("Case #{}: {}".format(test, dp[0][nof_exe - 1] + 2 * C[0][nof_exe - 1]))