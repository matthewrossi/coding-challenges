import sys
from collections import defaultdict

t, n, q = map(int, input().split())
for test in range(t):
    indexes = list(range(1, n + 1))

    # insertion sort
    for i in range(1, n):
        # binary search where to put indexes[i]
        start = 1
        end = i
        while start < end:
            mid = (start + end) // 2
            # use query as a "less than" by using current minima
            print(indexes[0], indexes[i], indexes[mid], flush=True)
            median = int(input())
            # when current minima is the median, indexes[i] is the new minima
            if indexes[0] == median:
                start = 0
                break
            if indexes[mid] == median:
                start = mid + 1
            else:
                end = mid
        # move indexes[i] to position
        target = indexes[i]
        for j in range(i, start, -1):
            indexes[j] = indexes[j - 1]
        indexes[start] = target

    print(" ".join(map(str, indexes)), flush=True)
    input()
