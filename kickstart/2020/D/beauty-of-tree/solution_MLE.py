# amadea (bilva) go from a node to the root painting every A-th (B-th) node
# starting from the curr one
# beauty = number of colored nodes
# expected beauty

from collections import defaultdict

t = int(input())
for test in range(1, t + 1):
    n, a, b = map(int, input().split()) 
    parent = list(map(int, input().split()))  # no root

    # build relative depth to each node
    rel_depth = [[0] * n for i in range(n)]
    for i in range(n):
        stack = [(i, -1)]
        while stack:
            curr, curr_parent = stack.pop()
            # update relative depth
            if curr_parent != -1:#i:
                rel_depth[i][curr] = rel_depth[i][curr_parent] + 1
            # insert childs
            for j in range(i + 1, n):
                if curr == parent[j - 1] - 1:
                    stack.append((j, curr))
    
    # build at_depth for each node
    at_depth = [defaultdict(int) for i in range(n)]
    for i in range(n):
        for d in rel_depth[i]:
            at_depth[i][d] += 1

    result = 0

    # independent coloring
    for d, count in at_depth[0].items():
        only_A = (d // a + 1) * (count / n)
        only_B = (d // b + 1) * (count / n)
        result += only_A + only_B

    # subtract overlap probability 
    for i in range(n):
        # compute possible overlap on the i-th node
        nodes_at_mod_A = 1
        for d, count in at_depth[i].items():
            if d and not d % a:
                nodes_at_mod_A += count
        nodes_at_mod_B = 1
        for d, count in at_depth[i].items():
            if d and not d % b:
                nodes_at_mod_B += count
        result -= nodes_at_mod_A * nodes_at_mod_B / n**2

    print("Case #{}: {}".format(test, result))
