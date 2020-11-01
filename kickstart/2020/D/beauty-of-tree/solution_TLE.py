# amadea (bilva) go from a node to the root painting every A-th (B-th) node
# starting from the curr one
# beauty = number of colored nodes
# expected beauty

from collections import defaultdict

t = int(input())
for test in range(1, t + 1):
    n, a, b = map(int, input().split()) 
    parent = list(map(int, input().split()))  # no root

    tot_union = tot_intersection = 0
    for i in range(n):
        # relative depth to i-th node
        rel_depth = [0] * n
        stack = [(i, -1)]
        while stack:
            curr, curr_parent = stack.pop()
            # update relative depth
            if curr_parent != -1:
                rel_depth[curr] = rel_depth[curr_parent] + 1
            # insert childs
            for j in range(i + 1, n):
                if curr == parent[j - 1] - 1:
                    stack.append((j, curr))

        # at_depth on relative depth
        at_depth = defaultdict(int)
        for d in rel_depth:
            at_depth[d] += 1

        nodes_at_mod_A = 1
        for d, count in at_depth.items():
            if d and not d % a:
                nodes_at_mod_A += count
        nodes_at_mod_B = 1
        for d, count in at_depth.items():
            if d and not d % b:
                nodes_at_mod_B += count
        tot_union += nodes_at_mod_A + nodes_at_mod_B
        tot_intersection += nodes_at_mod_A * nodes_at_mod_B

    print("Case #{}: {}".format(test, tot_union / n - tot_intersection / n**2))
