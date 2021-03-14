#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
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

# ANALYSIS
print("N° buildings:", nof_buildings)
print("N° antennas:", nof_antennas)
print("Reward:", reward)

buildings = pd.DataFrame([vars(b) for b in buildings])
antennas = pd.DataFrame([vars(a) for a in antennas])

print("\n[*] BUILDINGS")

unique = buildings["latency"].unique()
unique.sort()
latency_mins = unique[0:6]

print("Minimum latency:", latency_mins)
print("Maximum latency:", buildings["latency"].max())

latency = buildings["latency"].value_counts()
plt.bar(latency.index, latency.values)
plt.show()

unique = buildings["connection"].unique()
unique.sort()
connection_mins = unique[0:6]

print("Minimum connection:", connection_mins)
print("Maximum connection:", buildings["connection"].max())

connection = buildings["connection"].value_counts()
plt.bar(connection.index, connection.values)
plt.show()

fig, axs = plt.subplots(1, 2)
# color grade by latency weight
axs[0].set_title("Latency weight")
im0 = axs[0].scatter(buildings.x, buildings.y, s=1, c=buildings.latency, cmap="YlOrRd")
# isolate centroids
centroids =  buildings[buildings.latency.isin(latency_mins)]
im0 = axs[0].scatter(centroids.x, centroids.y, s=3, c="black")
# color grade by connection weight
axs[1].set_title("Connection weight")
im1 = axs[1].scatter(buildings.x, buildings.y, s=1, c=buildings.connection, cmap="YlOrRd")
# isolate centroids
centroids =  buildings[buildings.connection.isin(connection_mins)]
im0 = axs[1].scatter(centroids.x, centroids.y, s=3, c="black")

print("Centroids number: ", len(centroids))

plt.show()

print("\n[*] ANTENNAS")

print("Minimum range:", antennas["range"].min())
print("Maximum range:", antennas["range"].max())

range = antennas["range"].value_counts()
plt.bar(range.index, range.values)
plt.show()

# speed = antennas["speed"].value_counts()
# TODO: group by ranges with pd.cut
# bins = [int(i) for i in np.linspace(1, 10000, num=100)]
# plt.bar(speed.index, speed.values)
# plt.show()

print("Minimum speed:", antennas["speed"].min())
print("Maximum speed:", antennas["speed"].max())

n, bins, _ = plt.hist(antennas["speed"], bins=antennas["speed"].nunique() // 10, rwidth=0.8)
plt.show()

# see the relation among range and speed
plt.scatter(antennas.range, antennas.speed, s=1)
plt.show()

# OVERALL:
# low range antennas have the whole spectrum of speeds
# higher range antennas have lower cap on speed

# A: just submit solution in pdf

# B: 
# - 50k buildings
#   - uniform distrib of weights
#   - 400x400 grid
#      - uniform distribution
#      - uniform distribution of latency and connection weight
# - 1k antennas
#   - range most in 0 to 5 then very few up to 100 (0 - 100)
#   - speed most in 500 to 1k, some up to 5k (500 - 4992)

# C:
# - #building = #antennas
# - 60k buildings
#   - connection weight = 0 and uniform distribution of latency weights
#   - 600x600 grid
#       - uniform distribution
#       - uniform distribution of latency and connection weight
# - 60k antennas
#   - 0 range
#   - uniform distrib of speeds between 1 and 1k (1 - 1000)
# - SOLUTION: antenna on each building

# D:
# - 40k buildings
#   - connection = latency (normal distribution except for 54: 123, 55: 1769)
#   - 1200x1200 grid
#       - distribution with square groups with different densities
#       - higher latency and connection weight on boundaries of square groups
# - 1k antennas
#   - most range between 0 and 10, some aroung 20, less around 50 and few at 100 (0 - 100)
#   - quasi-uniform distribution 1 to 5k (1 - 4994)

# E:
# - 200k building
#   - strange distribution
#   - 2000x2000 grid
#       - has some empty spaces but looks and some are with lower densities
#       - higher connection weight on top-right
# - 6k antennas
#   - most range between 0 and 5, few up to 18, even less later (0 - 119)
#   - higher the speed lower the frequency (1 - 7990)

# F:
# - 350k building
#   - strange distribution
#   - 6000x6000
#       - has some empty spaces and lower densities areas
#       - connection weight delineate different regions with clear cuts
# - 32k antennas
#   - most range between 0 and 5, few arounf 12 and 25, then less and less later (0 - 200)
#   - uniform distrib of speeds between 1 and 5k (1 - 5000)
