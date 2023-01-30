#!/usr/bin/env python3

DIRECTIONS = {
    (0, 1): "E",    # right
    (1, 0): "S",    # down
    (0, -1): "W",   # left
    (-1, 0): "N",   # up
}


def merge():
    merged = {(0,0)}
    stack = []
    for di, dj in DIRECTIONS:
        if 0 <= di < r and 0 <= dj < c and cells[di][dj] == "*":
            stack.append((0, 0, (di, dj)))

    while stack:
        i, j, direction = stack.pop()

        if (i + direction[0], j + direction[1]) in merged:
            continue

        # Merge according to the direction
        if direction[0] == 0:
            if direction[1] == -1:  # left
                next[2*i][2*j - 1] = (2*i, 2*j)
                next[2*i + 1][2*j] = (2*i + 1, 2*j - 1)
            else:   # right
                next[2*i][2*j + 1] = (2*i, 2*(j + 1))
                next[2*i + 1][2*(j + 1)] = (2*i + 1, 2*j + 1)
        elif direction[0] == -1:    # up
            next[2*i][2*j] = (2*i - 1, 2*j)
            next[2*i - 1][2*j + 1] = (2*i, 2*j + 1)
        else: # down
            next[2*i + 1][2*j + 1] = (2*(i + 1), 2*j + 1)
            next[2*(i + 1)][2*j] = (2*i + 1, 2*j)
        merged.add((i + direction[0], j + direction[1]))

        # Move to the newly merged node
        i += direction[0]
        j += direction[1]

        # Add its adjacent viable nodes
        for di, dj in DIRECTIONS:
            if 0 <= i + di < r and 0 <= j + dj < c and \
                    cells[i + di][j + dj] == "*" and \
                    (i + di, j + dj) not in merged:
                stack.append((i, j, (di, dj)))

    return len(merged)


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    r, c = map(int, input().split())
    cells = [input() for _ in range(r)]

    next = [[-1] * (2*c) for _ in range(2*r)]
    free_cells = 0
    for i in range(r):
        for j in range(c):
            if cells[i][j] == "*":
                next[2*i][2*j] = (2*i, 2*j + 1)
                next[2*i][2*j + 1] = (2*i + 1, 2*j + 1)
                next[2*i + 1][2*j + 1] = (2*i + 1, 2*j)
                next[2*i + 1][2*j] = (2*i, 2*j)
                free_cells += 1

    connected_cells = merge()

    if connected_cells < free_cells:
        print("Case #{}: IMPOSSIBLE".format(test))
        continue

    # Translate the path in directions
    directions = [DIRECTIONS[next[0][0]]]
    i, j = next[0][0]
    while i or j:
        next_i, next_j = next[i][j]
        directions.append(DIRECTIONS[(next_i - i, next_j - j)])
        i, j = next_i, next_j

    print("Case #{}: {}".format(test, "".join(directions)))
