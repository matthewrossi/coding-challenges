# Practice round

## Greedy solutions

### Simple

Sort buidings on decreasing connection weight and put on them antennas starting
from the ones with less range.
Skipping some building in the process improves performance on big data sets.

### Skip buildings already covered by an antenna

Sort buidings on decreasing connection weight and put on them antennas starting
from the ones with less range.
While at it, it keeps track of the covered buildings and avoid placing an
antenna on top of an already covered building.
Skipping some building in the process improves performance on big data sets.

### Centroids

Data set D exibits an interesting pattern, with buildings grouped up into
squares of different sizes and square centers with minimum values of their
weights. This solution tries to exploit this pattern by:

1. locating the center of the squares (centroids)
2. identifying the size of the squares
3. assigning longer range antennas to the centroids depending on the size
   of the square
4. placing shorter range antennas as in the previous solution.

### Avoid overlapping of the antenna ranges

Sort buidings on decreasing connection weight and put on them antennas starting
from the ones with less range.
While at it, it keeps track of the covered buildings and avoid placing an
antenna on top of a building where its range overlaps with a previously placed
antenna.
Skipping some building in the process improves performance on big data sets.

## Data sets analysis

Compute and visualize interesting information about the input data sets. Like:

- number of buildings and antennas, and reward amount
- minimum and maximum values of buildings latency and connection weights
- frequency distribution of buildings latency and connection weights
- drawings of the buildings distribution with color grade based on latency and
  connection weights
- highlight buildings that act like centroids in data set D
- minimum and maximum values of antennas range and speed
- frequency distribution of antennas range and speed
- draw the relation among antennas range and speed

## Visualization

Visualize how a submission works on its respective data set.
Draw buildings distribution with color grade based on connection weights and on
top of it display antennas placement and the area they cover with their range.

## Scoring

Compute the score of a data set, given its data set and a submission.
It does so in an efficient way, by caching buildings by their position in the
grid, computing the overall score in a linear time with respect to the
number of buildings covered by the antennas.

## Scripts

### [script.sh](script.sh)

Run the given program in parallel over every input data set.

### [score.sh](score.sh)

Run the [score.py](score.py) program in parallel over every input data set,
it logs scores and at the end computes the total score.
