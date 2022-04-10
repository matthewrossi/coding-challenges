# WRONG ANSWER

import random

nof_test = int(input())
for test in range(1, nof_test + 1):
    nof_rooms, k = map(int, input().split())
    
    passages = [0] * k
    weigths = [1] * k

    # Starting point
    room, nof_passages = map(int, input().split())
    passages[0] = nof_passages

    # Gather as much info as possible
    for i in range(k):
        if i % 2 == 0:
            # Walk to a next room
            print("W")
            room, nof_passages = map(int, input().split())
            passages[i] = nof_passages
            weigths[i] = passages[i - 1] / nof_passages
        else:
            # Teleport to a new room
            print("T {}".format(random.randint(1, nof_rooms)))
            room, nof_passages = map(int, input().split())
            passages[i] = nof_passages

    # Produce reasonable extimation
    # NOTE: Compute a weighted average which serves as an unbiased estimate
    fanout = 0
    for weight, nof_passages in zip(weigths, passages):
        fanout += weight * nof_passages
    fanout /= k
    extimation = int(fanout * nof_rooms) // 2

    print("E {}".format(extimation))
