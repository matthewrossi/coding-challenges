# remove part of the network that are not reachable in time
# create a semplified version of the input file
# (if not streets/nodes are pruned this step is useless)

# compute the highest rewarding path walkable in time
# update weight 0-ing out the reward for streets we already went through 
# cycle

# use the computation done at the previos step in the cycle to perform a faster evaluation of the new highest rewarding path
# dijastra keeping track of the previous visited node should accomplish this (only the most rewarding paths )

# cost(time) should be diretly related to reward(length), but the speed is not necessarely the same for all streets
# do all dataset work on != speeds?
# to takle this we should consider as best the street with higher speed (greedy, knapsack problem get most rewarding path out of the time available)

# a decision tree while exhaustive, explodes very quickly

nof_junctions, nof_streets, time, nof_cars, starting_junction = map(int, input().split())
# ignore lat and long information
for junction in range(nof_junctions):
    input()
topology = [[] for junction in range(nof_junctions)]
for street in range(nof_streets):
    start, end, direction, time, length = map(int, input().split())
    topology[start].append((end, direction, time, length))

# ...

print(nof_cars)
for car in range(nof_cars):
    print(car + 1)
    for junction in routes[car]:
        print(junction)