import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nof_junctions, nof_streets, total_time, nof_cars, starting_junction = map(int, input().split())
for junction in range(nof_junctions):
    input()
speeds = []
for street in range(nof_streets):
    start, end, direction, time, length = map(int, input().split())
    speeds.append(length / time)

df = pd.DataFrame(speeds, columns=['speed']) 

bars = 30
min, max = min(speeds), max(speeds)
ranges = np.linspace(start=min, stop=max, num=bars)
middle = [(a + b) / 2 for a, b in zip(ranges[:-1], ranges[1:])]
frequencies = df["speed"].groupby(pd.cut(df["speed"].values, ranges)).count()
fig = plt.bar(middle, frequencies.values, width=0.02*(max-min))
plt.xlabel("Speed")
plt.ylabel("Number of packages")
plt.show()
