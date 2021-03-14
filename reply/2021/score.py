#!/usr/bin/env python3
import sys
from collections import namedtuple


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

Building = namedtuple("Building", ["x", "y", "latency", "connection"])

def dist(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

def pair_score(building, antenna):
    distance = dist(building.x, building.y, antenna.x, antenna.y)
    score = building.connection * antenna.speed - building.latency * distance
    return score


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

# PARSE SUBMISSION
with open(sys.argv[2], 'r') as sub:
    nof_placed = int(sub.readline())
    for _ in range(nof_placed):
        id, antennas[id].x, antennas[id].y = map(int, sub.readline().split())

# SCORE
building_scores = [float("-inf")] * nof_buildings
for antenna in antennas:
    # skip not placed antennas
    if antenna.x is None:
        continue

    x, y, r = antenna.x, antenna.y, antenna.range
    # retrieve building in range
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
                building_scores[id] = max(building_scores[id], pair_score(buildings[id], antenna))

score = 0
bonus = True
for building_score in building_scores:
    if building_score != float("-inf"):
        score += building_score
    else:
        bonus = False

peprint(score + (reward if bonus else 0))
