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


# PARSE INPUT
width, height = map(int, input().split())
nof_buildings, nof_antennas, reward = map(int, input().split())


buildings = [None] * nof_buildings
for i in range(nof_buildings):
    buildings[i] = Building(*map(int, input().split()))

antennas = [None] * nof_antennas
for i in range(nof_antennas):
    antennas[i] = Antenna(*map(int, input().split()))

# SOLVE
# order building by connection weight
building_ids = sorted(range(nof_buildings), key=lambda id: buildings[id].connection, reverse=True)

# order antennas by decreasing connection speed (TOTAL: 15631812973)
antenna_ids = sorted(range(nof_antennas), key=lambda id: antennas[id].speed, reverse=True)
# do not order (TOTAL: 16697680030)
antenna_ids = range(nof_antennas)
# order antennas by increasing connection range (TOTAL: 17748373756)
antenna_ids = sorted(range(nof_antennas), key=lambda id: antennas[id].range)

# place antennas on top of buildings
current = 0
for id in antenna_ids:
    antennas[id].x = buildings[building_ids[current]].x
    antennas[id].y = buildings[building_ids[current]].y
    current += 1    # increase this to avoid picking consecutive buildings

# PRODUCE SUBMISSION
print(nof_antennas)
for i in range(nof_antennas):
    print(i, antennas[i].x, antennas[i].y)
