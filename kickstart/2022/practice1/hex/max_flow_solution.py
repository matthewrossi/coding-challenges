DIRS = [
    (0, -1),    # left
    (-1, 0),    # top-left
    (-1, 1),    # top-right
    (0, 1),     # right
    (1, 0),     # bottom-right
    (1, -1),    # bottom-left
]
SOURCE = -2
SINK = -1


def create_graph(board, player):
    n = len(board)

    pos_to_id = {}
    blues = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                pos_to_id[(i, j)] = blues
                blues += 1

    graph = [[0] * (blues + 2) for _ in range(blues + 2)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                current_node = pos_to_id[(i, j)]
                for di, dj in DIRS:
                    idx = pos_to_id.get((i + di, j + dj))
                    if idx is not None:
                        graph[current_node][idx] = 1

    if player == 'B':
        for i in range(n):
            idx = pos_to_id.get((i, 0))
            if idx is not None:
                graph[SOURCE][idx] = 1
            idx = pos_to_id.get((i, n - 1))
            if idx is not None:
                graph[idx][SINK] = 1
    elif player == 'R':
        for i in range(n):
            idx = pos_to_id.get((0, i))
            if idx is not None:
                graph[SOURCE][idx] = 1
            idx = pos_to_id.get((n - 1, i))
            if idx is not None:
                graph[idx][SINK] = 1
    return blues, graph


def search_path(graph, source, sink, parent):
    nof_nodes = len(graph)
    visited = [False] * nof_nodes
    queue = [source]
    visited[source] = True
    while queue:
        node = queue.pop(0)
        for neighbor, capacity in enumerate(graph[node]):
            if not visited[neighbor] and capacity > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = node
    return True if visited[sink] else False


def get_winning_paths(graph, source, sink):
    nof_nodes = len(graph)
    parent = [-1] * nof_nodes
    max_flow = 0
    while search_path(graph, source, sink, parent):
        # Find maximum flow through the path
        path_flow = float("inf")
        s = sink
        while(s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        # Increase overall flow
        max_flow += path_flow
        # Updating the residual values of edges
        v = sink
        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


def solve(board):
    blues, blue_graph = create_graph(board, 'B')
    reds, red_graph = create_graph(board, 'R')
    if blues - reds < -1 or blues - reds > 1:
        return "Impossible"

    blue_wins = get_winning_paths(blue_graph, SOURCE, SINK)
    if blue_wins == 1 and reds > blues or blue_wins > 1:
        return "Impossible"
    red_wins = get_winning_paths(red_graph, SOURCE, SINK)
    if red_wins == 1 and blues > reds or red_wins > 1:
        return "Impossible"
    
    # NOTE: There is no way both players have a winning path
    if not blue_wins and not red_wins:
        return "Nobody wins"
    return "Blue wins" if blue_wins else "Red wins"


if __name__ == "__main__":
    nof_tests = int(input())
    for test in range(1, nof_tests + 1):
        n = int(input())
        board = [input() for _ in range(n)]
        res = solve(board)
        print("Case #{}: {}".format(test, res))
