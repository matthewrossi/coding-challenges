#!/usr/bin/env python3

# Naive solution: for each point of the room compute the sum of manhattan
# distances to furnitures

# Ideas to improve complexity of the solution:
# - start by finding best x coordinate and then best y coordinate
# - the best coordinate always fall into a furniture border


def min_distance(start, end):
    # Sort furniture extremes
    start.sort()
    end.sort()

    # Start off at the lowest coordinate
    distance = sum(start) - nof_furnitures * start[0]
    min_distance = distance
    min_distance_pos = start[0]
    prev = start[0]

    # TODO: remove inside variable as it is not needed to solve the problem
    # Update the distance as we move to higher coordinate
    start_idx = inside = 1
    end_idx = before = 0
    after = nof_furnitures - 1
    while start_idx < nof_furnitures or end_idx < nof_furnitures:
        if start_idx < nof_furnitures and (end_idx == nof_furnitures
                                           or start[start_idx] < end[end_idx]):
            # A furniture starts at the current position
            steps = start[start_idx] - prev
            distance += (before - after) * steps
            if distance < min_distance:
                min_distance = distance
                min_distance_pos = start[start_idx]
            inside += 1
            after -= 1
            prev = start[start_idx]
            start_idx += 1
        else:
            # A furniture ends at the current position
            steps = end[end_idx] - prev
            distance += (before - after) * steps
            if distance < min_distance:
                min_distance = distance
                min_distance_pos = end[end_idx]
            inside -= 1
            before += 1
            prev = end[end_idx]
            end_idx += 1

    return min_distance_pos


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_furnitures = int(input())
    from_xs, to_xs = [None] * nof_furnitures, [None] * nof_furnitures
    from_ys, to_ys = [None] * nof_furnitures, [None] * nof_furnitures
    for i in range(nof_furnitures):
        from_xs[i], from_ys[i], to_xs[i], to_ys[i] = map(int, input().split())
    x = min_distance(from_xs, to_xs)
    y = min_distance(from_ys, to_ys)
    print("Case #{}: {} {}".format(test, x, y))
