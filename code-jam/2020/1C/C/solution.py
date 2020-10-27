tests = int(input())
for test in range(1, tests + 1):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[None] * d for _ in range(n)] # dp[n][d] = (dimensione, tagli)

    size, cuts = 0, 1

    for i in range(n):
        # sectors up to i
        for j in range(d):
            # we want j cuts
            for k in range(j):
                # iter on prev sizes
                curr_size = dp[i - 1][k][size]
                cuts = int(a[i] / curr_size)


                if dp[i - 1][j][cuts] > dp[i - 1][k][cuts] + :

            dp[i][j] = dp[i - 1][j]

    # counts = [0] * n
    # for i in range(n):
    #     for j in range(i, n):
    #         counts[i] += int(a[j] / a[i])
    

    print("Case #{}: {}".format(test, counts))
