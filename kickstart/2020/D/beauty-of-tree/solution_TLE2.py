# amadea (bilva) go from a node to the root painting every A-th (B-th) node
# starting from the curr one
# beauty = number of colored nodes
# expected beauty

from collections import defaultdict


class Node:

    def __init__(self, id, parent=None):
        self.id = id
        self.depth = 0
        self.childs = []

        if parent:
            self.depth = parent.depth + 1
            parent.childs.append(self)


t = int(input())
for test in range(1, t + 1):
    n, a, b = map(int, input().split()) 
    parent = list(map(int, input().split()))  # no root

    # create tree
    index = {0: Node(0)}
    for i, p in enumerate(parent, start=1):
        index[i] = Node(i, index[p - 1])

    tot_union = tot_intersection = 0
    for i in range(n):
        nodes_at_mod_A = nodes_at_mod_B = 1

        ith_depth = index[i].depth
        stack = [index[i]]
        while stack:
            curr = stack.pop()

            rel_depth = curr.depth - ith_depth
            if rel_depth and not rel_depth % a:
                nodes_at_mod_A += 1
            if rel_depth and not rel_depth % b:
                nodes_at_mod_B += 1
            stack.extend(curr.childs)

        tot_union += nodes_at_mod_A + nodes_at_mod_B
        tot_intersection += nodes_at_mod_A * nodes_at_mod_B

    print("Case #{}: {}".format(test, tot_union / n - tot_intersection / n**2))
