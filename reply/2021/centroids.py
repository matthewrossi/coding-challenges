#!/usr/bin/env python3
import sys
from collections import defaultdict


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}: {string}"

def peprint(string):
    eprint(prefix(string))


class Antenna:
    def __init__(self, range, speed):
        self.range = range
        self.speed = speed
        self.x = None
        self.y = None

class Building:
    def __init__(self, x, y, latency, connection):
        self.x = x
        self.y = y
        self.latency = latency
        self.connection = connection
        self.covered = False


def buildings_in_range(antenna):
    x, y, r = antenna.x, antenna.y, antenna.range
    # retrieve building in range
    in_range = []
    for i in range(2*r + 2):
        x_offset = -r + i
        # outside left border
        if x + x_offset < 0:
            continue
        # outside right border
        if x + x_offset >= width:
            break

        y_offsets = range(-i, i + 1) if i <= r else range(-(2 * r - i), (2 * r - i) + 1)
        for y_offset in y_offsets:           
            # outside down border
            if y + y_offset < 0:
                continue
            # outside up border
            if y + y_offset >= height:
                break

            id = by_coords[x + x_offset][y + y_offset]
            if id is not None:
                in_range.append(id)
    return in_range

def dist(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


# PARSE INPUT
width, height = map(int, input().split())
nof_buildings, nof_antennas, reward = map(int, input().split())


buildings = [None] * nof_buildings
by_coords = [[None] * height for _ in range(width)]
for i in range(nof_buildings):
    building = Building(*map(int, input().split()))
    buildings[i] = building
    by_coords[building.x][building.y] = i

antennas = [None] * nof_antennas
for i in range(nof_antennas):
    antennas[i] = Antenna(*map(int, input().split()))

# SOLVE

# high range antennas
high = [id for id in range(nof_antennas) if antennas[id].range > 10]

# isolate squares and their dimension
unique = list({b.latency for b in buildings})
unique.sort()
mins = unique[0:6]
centroids = [i for i, b in enumerate(buildings) if b.latency in mins]

# clean centroid
spots = []
for id in centroids:
    centroid = buildings[id]
    # skip this centroid as it is already in there
    for spot in spots:
        if dist(centroid.x, centroid.y, buildings[spot].x, buildings[spot].y) < 20:
            break
    else:
        spots.append(id)

# compute square size
sizes = []
for spot in spots:
    x, y = buildings[spot].x, buildings[spot].y
    
    # compute the hight of the square
    count = 0
    for y_offset in range(0, 60):
        # outside up border
        if y + y_offset >= height:
            break
        no_building = True
        for x_offset in range(-10, 10):
            # outside left border
            if x + x_offset < 0:
                continue
            # outside right border
            if x + x_offset >= width:
                break
            id = by_coords[x + x_offset][y + y_offset]
            if id is not None:
                no_building = False
                count = 0

        if no_building:
            count += 1
        if count == 5:
            break
    h = (y_offset - 5) * 2

    # compute the width of the square
    count = 0
    for x_offset in range(0, 60):
        # outside up border
        if x + x_offset >= width:
            break
        no_building = True
        for y_offset in range(-15, 15):
            # outside left border
            if y + y_offset < 0:
                continue
            # outside right border
            if y + y_offset >= height:
                break
            id = by_coords[x + x_offset][y + y_offset]
            if id is not None:
                no_building = False
                count = 0

        if no_building:
            count += 1
        if count == 5:
            break
    w = (x_offset - 5) * 2
    sizes.append(max(h, w))

# place antenna bigger on bigger spots
high = sorted(high, key=lambda id: antennas[id].range, reverse=True)
spots_ids = sorted(range(len(spots)), key=lambda id: sizes[id], reverse=True)

current = 0
for spot_id, size in zip(spots_ids, sizes):
    building = buildings[spots[spot_id]]
    antenna = antennas[high[current]]
    antenna.x = building.x
    antenna.y = building.y
    # update buildings in range as covered
    for b_id in buildings_in_range(antenna):
        buildings[b_id].covered = True
    current += 1

used = current

# place leftovers
building_ids = sorted(range(nof_buildings), key=lambda id: buildings[id].connection, reverse=True)
antenna_ids = high[current:]

a_idx = b_idx = 0
while a_idx < len(antenna_ids) and b_idx < nof_buildings:
    building = buildings[building_ids[b_idx]]
    antenna = antennas[antenna_ids[a_idx]]

    # skip building already covered by an antenna
    if building.covered:
        b_idx += 1
        continue

    # place antenna on top of building
    antenna.x = building.x
    antenna.y = building.y

    # update buildings in range as covered
    for b_id in buildings_in_range(antenna):
        buildings[b_id].covered = True

    a_idx += 1
    b_idx += 1

used += a_idx

# low range antennas
# place antenna fast low range antennas on high connection weight buildings
building_ids = sorted(range(nof_buildings), key=lambda id: buildings[id].connection, reverse=True)
low = [id for id in range(nof_antennas) if antennas[id].range <= 10]
antenna_ids = sorted(low, key=lambda id: antennas[id].speed, reverse=False)

# place low range antennas on top of the buildings not covered
a_idx = b_idx = 0
while a_idx < len(antenna_ids) and b_idx < nof_buildings:
    building = buildings[building_ids[b_idx]]
    antenna = antennas[antenna_ids[a_idx]]

    # skip building already covered by an antenna
    if building.covered:
        b_idx += 1
        continue

    # place antenna on top of building
    antenna.x = building.x
    antenna.y = building.y

    # update buildings in range as covered
    for b_id in buildings_in_range(antenna):
        buildings[b_id].covered = True

    a_idx += 1
    b_idx += 1

# PRODUCE SUBMISSION
used += a_idx
peprint(f"Using {used}/{nof_antennas} antennas")

print(used)
for i in range(nof_antennas):
    if antennas[i].x != None:
        print(i, antennas[i].x, antennas[i].y)
