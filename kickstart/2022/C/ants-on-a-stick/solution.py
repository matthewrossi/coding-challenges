#!/usr/bin/env python3

POSITION = TIME = 0
DIRECTION = 1
INDEX = 2

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n, l = map(int, input().split())

    ants = []
    for i in range(n):
        p, d = map(int, input().split())
        ants.append([p, d, i + 1])

    falling_events = []
    for i in range(n):
        falling_time = ants[i][POSITION] if ants[i][DIRECTION] == 0 else l - ants[i][POSITION]
        falling_events.append((falling_time, ants[i][DIRECTION]))

    ants.sort()
    falling_events.sort()

    solution = []
    start = 0
    end = n - 1
    for i in range(n):
        if i + 1 < n and falling_events[i][TIME] == falling_events[i + 1][TIME]:
            if falling_events[i][DIRECTION] == 0:
                idx1 = ants[start][INDEX]
                idx2 = ants[end][INDEX]
            else:
                idx1 = ants[end][INDEX]
                idx2 = ants[start][INDEX]

            if idx1 > idx2:
                falling_events[i], falling_events[i + 1] = falling_events[i + 1], falling_events[i]

        if falling_events[i][DIRECTION] == 0:
            solution.append(ants[start][INDEX])
            start += 1
        else:
            solution.append(ants[end][INDEX])
            end -= 1
    
    print("Case #{}: {}".format(test, " ".join(map(str, solution))))
