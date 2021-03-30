import math

def reverse(arr, start, end):
    for i in range(math.ceil((end - start) / 2)):
        arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    cost = 0
    for i in range(n - 1):
        j = min(range(i, n), key=lambda x: arr[x])
        reverse(arr, i, j)
        cost += j - i + 1

    print("Case #{}: {}".format(test, cost))
