from collections import deque, namedtuple

inf = float("inf")
Edge = namedtuple('Edge', 'start, ')

nof_junctions, nof_streets, total_time, nof_cars, starting_junction = map(int, input().split())
# ignore lat and long information
for junction in range(nof_junctions):
    input()
topology = [[] for junction in range(nof_junctions)]
for street in range(nof_streets):
    start, end, direction, time, length = map(int, input().split())
    topology[start].append((end, time, length))
    if direction == 2:
        topology[end].append((start, time, length))

vertices = set(range(0, nof_junctions))
distances = [inf] * nof_junctions
distances[starting_junction] = 0
previous_vertices = [None] * nof_junctions

while vertices:
    current_vertex = min(vertices, key=lambda vertex: distances[vertex])
    if distances[current_vertex] == inf:
        break
    
    for neighbour, cost, _ in topology[current_vertex]:
        alternative_route = distances[current_vertex] + cost
        if alternative_route < distances[neighbour]:
            distances[neighbour] = alternative_route
            previous_vertices[neighbour] = current_vertex
    vertices.remove(current_vertex)

reachable = []
for vertex in range(nof_junctions):
    if distances[vertex] < total_time:
        reachable.append(vertex)
print(f"nof_junctions = {nof_junctions} nof_reachable = {len(reachable)}")  # all reachable within total_time
