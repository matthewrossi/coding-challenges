nof_junctions, nof_streets, total_time, nof_cars, starting_junction = map(int, input().split())
# ignore lat and long information
for junction in range(nof_junctions):
    input()
streets = []
for street in range(nof_streets):
    start, end, direction, time, length = map(int, input().split())
    streets.append((time, length))

streets.sort()  # sorts on the 0-th tuple element
print(streets)  # no relation among time and score
    