#!/usr/bin/env python3

# # time: O(N^2), space: O(N^2*D)
# def solve(i, j, k):
#     if i > j:
#         return 0
#     if(dp[i][j][k] != -1):
#         return dp[i][j][k]
    
#     # Current state
#     currentVal_i = (dials[i] - k + d) % d
#     currentVal_j = (dials[j] - k + d) % d
#     # Convert index i to 0
#     currentOps = min(currentVal_i, d - currentVal_i)
#     val_1 = currentOps + solve(i + 1, j, (k + currentVal_i) % d)
#     # Convert index j to 0
#     currentOps = min(currentVal_j, d - currentVal_j)
#     val_2 = currentOps + solve(i, j - 1, (k + currentVal_j) % d)

#     dp[i][j][k] = min(val_1, val_2)
#     return dp[i][j][k]

# time: O(N^2), space: O(N^2)
def solve(start, end, side):
    if start > end:
        return 0
    if dp[start][end][side] != -1:
        return dp[start][end][side]
    
    k = 0
    if not side:    # left
        if start > 0:
            k = dials[start - 1]
    else:           # right
        if end < n - 1:
            k = dials[end + 1]
  
    # Move according to the left dial
    curr_dial_start = (dials[start] - k + d) % d
    curr_operations = min(curr_dial_start, d - curr_dial_start)
    moves_start = curr_operations + solve(start + 1, end, 0)
   
    # Move according to the right dial
    curr_dial_end = (dials[end] - k + d) % d
    curr_operations = min(curr_dial_end, d - curr_dial_end)
    moves_end = curr_operations + solve(start, end - 1, 1)

    # Select the one with the least moves
    dp[start][end][side] = min(moves_start, moves_end)

    return dp[start][end][side]


nof_test = int(input())
for test in range(1, nof_test + 1):
    n, d = map(int, input().split())
    dials = list(map(int, input().split()))

    # dp = [[[-1] * d for _ in range(n)] for _ in range(n)]
    dp = [[[-1] * 2 for _ in range(n)] for _ in range(n)]
    print("Case #{}: {}".format(test, solve(0, n - 1, 0)))
