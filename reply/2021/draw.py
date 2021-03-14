#!/usr/bin/env python3
import sys
import matplotlib as mpl
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}-{string}"

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


# PARSE INPUT
width, height = map(int, input().split())
nof_buildings, nof_antennas, reward = map(int, input().split())

buildings = [None] * nof_buildings
for i in range(nof_buildings):
    buildings[i] = Building(*map(int, input().split()))

antennas = [None] * nof_antennas
for i in range(nof_antennas):
    antennas[i] = Antenna(*map(int, input().split()))

# PARSE SUBMISSION
with open(sys.argv[2], 'r') as sub:
    nof_placed = int(sub.readline())
    for _ in range(nof_placed):
        id, antennas[id].x, antennas[id].y = map(int, sub.readline().split())

# VISUALIZATION
# buildings
buildings = pd.DataFrame([vars(b) for b in buildings])
plt.scatter(buildings.x, buildings.y, s=1, c=buildings.connection, cmap="YlOrRd")

# antennas
antennas = pd.DataFrame([vars(a) for a in antennas])
plt.scatter(antennas.x, antennas.y, s=1, c=antennas.speed, cmap="Greens")

# antennas range
for index, antenna in antennas.iterrows():
    x = antenna.x + np.array([0, -1, 0, 1]) * antenna.range
    y = antenna.y + np.array([-1, 0, 1, 0]) * antenna.range
    plt.gca().add_patch(patches.Polygon(xy=list(zip(x,y)), alpha=0.2, edgecolor="blue", fill=True))
    # rect = plt.Rectangle((antenna.x, antenna.y - antenna.range), 2**0.5 * antenna.range, 2**0.5 * antenna.range, 45, alpha=0.2)
    # plt.gca().add_patch(rect)
plt.show()
