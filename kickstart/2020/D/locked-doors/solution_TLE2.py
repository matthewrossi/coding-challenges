# 1 to N rooms in a row
# N-1 locked doors connect the adjacent rooms
# each door has a unique difficulty level

# start room, goes to lower difficulty, if only one locked, opens it
# once a door is unlocked it remains so

# queries: K-th room she visits starting from S-th

import numpy as np

from collections import namedtuple

Entry = namedtuple("Entry", ["prev", "left", "right"])

def update_entry(entry, step):
    prev = entry.prev
    current = prev[-1]
    left = entry.left
    right = entry.right
    for _ in range(step):
        if left < 0 or (right != n - 1 and doors[left] > doors[right]):
            current = right + 2
            right += 1
        else:
            current = left + 1
            left -= 1
        prev.append(current)
    
    return Entry(prev, left, right)

t = int(input())
for test in range(1, t + 1):
    n, q = map(int, input().split())
    doors = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    # sort by starting position
    by_starting = np.argsort(queries, axis=0)

    answer = [-1] * q
    cache_start = -1
    cache = None
    for i, _ in by_starting:
        start, step = queries[i]
        if start != cache_start:
            entry = Entry([start], start - 2, start - 1)
            cache = update_entry(entry, step - 1)
            cache_start = start
        else:
            if step > len(cache.prev):
                cache = update_entry(cache, step - len(cache.prev))
        answer[i] = str(cache.prev[step - 1])

    print("Case #{}: {}".format(test, " ".join(answer)))
