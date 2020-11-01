from heapq import *
from math import floor

tests = int(input())
for test in range(1, tests + 1):
    n, k = map(int, input().split())
    minutes = list(map(int, input().split()))
    diff = [None] * (n - 1)
    for i in range(n - 1):
        diff[i] = (-(minutes[i + 1] - minutes[i]), 1)
    heapify(diff)
    for i in range(k):
        minute, count = heappop(diff)
        if minute == 1:
            print("Case #{}: {}".format(test, 1))
            break
        heappush(diff, (minute * count / (count + 1), count + 1))
    else:
        minute, _ = heappop(diff)
        print("Case #{}: {}".format(test, -floor(minute)))
