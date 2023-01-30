#!/usr/bin/env python3

DIRECTIONS = [
    [0, 1],     # right
    [1, 0],     # down    
]

# NOTE: The following implementation reaches stack limits
def hamiltonian_path(E, n, root):
    path.append(root)
    path_set.add(root)

    for i in E[root]:
        if i not in path_set:
            if hamiltonian_path(E, n, i):
                return True
    
    if len(path) == n and path[0] in E[path[-1]]:
        return True

    node = path.pop()
    path_set.remove(node)
    return False


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    r, c = map(int, input().split())
    cells = [input() for _ in range(r)]

    bigger_cells = [["#"] * (2*c) for _ in range(2*r)]
    free_cells = 0
    for i in range(r):
        for j in range(c):
            if cells[i][j] == "*":
                bigger_cells[2*i][2*j] = "*"
                bigger_cells[2*i][2*j + 1] = "*"
                bigger_cells[2*i + 1][2*j] = "*"
                bigger_cells[2*i + 1][2*j + 1] = "*"
                free_cells += 4

    graph = [set() for _ in range(4*r*c)]
    for i in range(2*r):
        for j in range(2*c):
            for (di, dj) in DIRECTIONS:
                if i + di < 2*r and j + dj < 2*c and \
                        bigger_cells[i][j] == bigger_cells[i + di][j + dj] == "*":
                    graph[2*c * i + j].add(2*c * (i + di) + (j + dj))
                    graph[2*c * (i + di) + (j + dj)].add(2*c * i + j)

    path = []
    path_set = set()
    is_possible = hamiltonian_path(graph, free_cells, 0)

    if not is_possible:
        print("Case #{}: IMPOSSIBLE".format(test))
        continue

    # Translate the path in directions
    directions = []
    for i in range(free_cells):
        if path[i] > path[(i + 1) % free_cells]:
            if path[i] - path[(i + 1) % free_cells] == 1:
                directions.append("W")
            else:
                directions.append("N")
        else:
            if path[(i + 1) % free_cells] - path[i] == 1:
                directions.append("E")
            else:
                directions.append("S")

    print("Case #{}: {}".format(test, "".join(directions)))
