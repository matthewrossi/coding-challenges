#!/usr/bin/env python3
import sys
from collections import UserDict, defaultdict


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


def buildings_in_range(x, y, r):
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

# place antennas avoiding covering already covered areas
building_ids = sorted(range(nof_buildings), key=lambda id: buildings[id].connection, reverse=True)
antenna_ids = sorted(range(nof_antennas), key=lambda id: antennas[id].range)

a_idx = b_idx = 0
while a_idx < len(antenna_ids) and b_idx < nof_buildings:
    building = buildings[building_ids[b_idx]]
    antenna = antennas[antenna_ids[a_idx]]

    # skip building already covered by an antenna
    if building.covered:
        b_idx += 1
        continue

    # skip building if any of the buildings we cover are already covered
    in_range = buildings_in_range(building.x, building.y, antenna.range)
    covered = False
    for b_id in in_range:
        if buildings[b_id].covered:
            covered = True
            break
    if covered:
        b_idx += 1
        continue

    # place antenna on top of building
    antenna.x = building.x
    antenna.y = building.y

    # update buildings in range as covered
    for b_id in buildings_in_range(antenna.x, antenna.y, antenna.range):
        buildings[b_id].covered = True

    a_idx += 1
    b_idx += 1

used = a_idx
peprint(f"Using {used}/{nof_antennas} antennas")

print(used)
for i in range(nof_antennas):
    if antennas[i].x != None:
        print(i, antennas[i].x, antennas[i].y)
