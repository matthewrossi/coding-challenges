#!/usr/bin/env python3

import heapq

t = int(input())
for test in range(1, t + 1):
    r, c = map(int, input().split())
    house = [list(map(int, input().split())) for _ in range(r)]

    done = [[False] * c for _ in range(r)]

    cells = [None] * (r * c)
    for i in range(r):
        for j in range(c):
            cells[i * c + j] = (-house[i][j], i, j)
    heapq.heapify(cells)

    additions = 0
    while cells:
        neg, i, j = heapq.heappop(cells)
        peak = -neg

        if done[i][j]:
            continue

        offsets = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for i_offset, j_offset in offsets:
            i_curr = i + i_offset
            j_curr = j + j_offset

            if i_curr < 0 or i_curr >= r or j_curr < 0 or j_curr >= c:
                continue

            if peak > house[i_curr][j_curr] + 1:
                additions += peak - house[i_curr][j_curr] - 1
                house[i_curr][j_curr] = peak - 1
                heapq.heappush(cells, (-house[i_curr][j_curr], i_curr, j_curr))
        
        done[i][j] = True

    print("Case #{}: {}".format(test, additions))
