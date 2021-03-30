import sys
from collections import defaultdict

t, n, q = map(int, input().split())
for test in range(t):
    # extremes
    extremes = [1, 2]
    for item in range(3, n + 1):
        extremes.append(item)
        print(*extremes, flush=True)
        median = int(input())
        extremes.remove(median)

    minimum, maximum = extremes

    indexes = list(range(1, n + 1))
    indexes[0], indexes[minimum - 1] =  indexes[minimum - 1], indexes[0]
    indexes[-1], indexes[maximum - 1] = indexes[maximum - 1], indexes[-1]

    # insertion sort
    for i in range(1, n - 1):
        # binary search where to put indexes[i]
        start = 1
        end = i
        while start < end:
            mid = (start + end) // 2
            # use query as a "less than" by fixing minimum
            print(minimum, indexes[i], indexes[mid], flush=True)
            smaller = int(input())
            if indexes[mid] == smaller:
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
