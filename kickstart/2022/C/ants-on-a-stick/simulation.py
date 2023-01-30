#!/usr/bin/env python3

POSITION = 0
DIRECTION = 1
INDEX = 2

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n, l = map(int, input().split())

    ants = []
    for i in range(n):
        p, d = map(int, input().split())
        ants.append([p, d, i + 1])

    ants.sort()

    # simulation
    solution = []

    start = 0
    end = n - 1
    while start <= end:
        # moving
        for i in range(start, end + 1):
            p, d, _ = ants[i]
            ants[i][POSITION] = p + (-1 if not d else 1)
        
        # falling
        falling = []
        if ants[start][POSITION] == 0:
            falling.append(ants[start][INDEX])
            start += 1
        if ants[end][POSITION] == l:
            falling.append(ants[end][INDEX])
            end -= 1
        falling.sort()
        solution.extend(falling)
        
        # bouncing
        for i in range(start, end):
            p, d, _ = ants[i]
            p1, d1, _ = ants[i + 1]
            # same direction => no bouncing
            if d == d1:
                continue
            # different direction => may bounce
            if p >= p1:
                # change directions
                ants[i][DIRECTION] = 0
                ants[i + 1][DIRECTION] = 1
                # change positions
                if p > p1:
                    ants[i][POSITION] -= 1
                    ants[i + 1][POSITION] += 1
    
    print("Case #{}: {}".format(test, " ".join(map(str, solution))))
