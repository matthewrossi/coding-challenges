t = int(input())
for test in range(1, t + 1):
    x, y, s = input().split()
    x = int(x)
    y = int(y)
    n = len(s)

    dp = [[float("+inf")] * 2 for _ in range(n + 1)]
    dp[0][0] = dp[0][1] = 0
    for i in range(1, n + 1):
        for c in range(2):
            if c == 0 and s[i-1] == 'J':   continue
            if c == 1 and s[i-1] == 'C':   continue
            for d in range(2):
                cost = 0
                if i > 1:
                    if d == 0 and c == 1: cost += x
                    if d == 1 and c == 0: cost += y
                dp[i][c] = min(dp[i][c], dp[i - 1][d] + cost)
    
    print("Case #{}: {}".format(test, min(dp[n][0], dp[n][1])))    
