import sys
from collections import defaultdict

t, n, q = map(int, input().split())
for test in range(t):
    medians = defaultdict(list)
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                print(i, j, k, flush=True)
                medians[int(input())].append((i, j, k))

    indexes = [None] * n

    i = 0
    extremes = [i for i in range(1, n + 1) if i not in medians]

    while i < n // 2:
        # place extremes
        if i > 0:
            print(indexes[0], *extremes, flush=True)
            median = int(input())
            if median != extremes[0]:
                extremes.reverse()
        indexes[i], indexes[n - i - 1] = extremes
        i += 1

        # remove triplets related to current extremes
        to_delete = set()
        for extreme in extremes:
            for median, triplets in medians.items():
                for pos in range(len(triplets) - 1, -1, -1):
                    if extreme in triplets[pos]:
                        del triplets[pos]
                # keep track of empty list of triplets
                if not triplets:
                    to_delete.add(median)

        # delete empty list of triplets
        for median in to_delete:
            del medians[median]

        # empty list of triplets are the new extremes
        extremes = list(to_delete)

    print(" ".join(map(str, indexes)), flush=True)
    input()
