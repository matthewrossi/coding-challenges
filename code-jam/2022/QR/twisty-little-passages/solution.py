import random

nof_test = int(input())
for test in range(1, nof_test + 1):
    nof_rooms, k = map(int, input().split())
    
    passages = [0] * nof_rooms
    walks = [False] * nof_rooms

    # Starting point
    room, nof_passages = map(int, input().split())
    passages[room - 1] = nof_passages

    # Gather as much info as possible
    for i in range(k):
        if i % 2 == 0:
            # Walk to a next room
            print("W")
            room, nof_passages = map(int, input().split())
            passages[room - 1] = nof_passages
            walks[room - 1] = True
        else:
            # Teleport to a new room
            print("T {}".format(random.randint(1, nof_rooms)))
            room, nof_passages = map(int, input().split())
            passages[room - 1] = nof_passages

    # Produce reasonable extimation
    # NOTE: Do not consider walks during fanout extimation
    fanout = nof_teleports = nof_walks = 0
    for room in range(nof_rooms):
        if passages[room]:
            if not walks[room]:
                fanout += passages[room]
                nof_teleports += 1
            else:
                nof_walks += 1
    fanout /= nof_teleports
    nof_rooms_to_extimate = nof_rooms - (nof_teleports + nof_walks)
    extimation = int(sum(passages) + fanout * nof_rooms_to_extimate) // 2

    print("E {}".format(extimation))
