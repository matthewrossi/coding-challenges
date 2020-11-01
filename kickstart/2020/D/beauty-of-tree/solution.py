# amadea (bilva) go from a node to the root painting every A-th (B-th) node
# starting from the curr one
# beauty = number of colored nodes
# expected beauty

from collections import defaultdict


class Node:

    def __init__(self, id, parent=None):
        self.id = id
        self.parent = parent
        self.childs = []

        if parent:
            parent.childs.append(self)
    
    def __str__(self):
        return str(self.id)


def update(node):
    curr_id = node.id
    depth = len(path_taken)
    visit_a[curr_id] += 1
    if a <= depth:
        visit_a[path_taken[depth - a].id] += visit_a[curr_id]
    visit_b[curr_id] += 1
    if b <= depth:
        visit_b[path_taken[depth - b].id] += visit_b[curr_id]


t = int(input())
for test in range(1, t + 1):
    n, a, b = map(int, input().split()) 
    parent = list(map(int, input().split()))  # no root

    # create tree
    index = {0: Node(0)}
    for i, p in enumerate(parent, start=1):
        index[i] = Node(i, index[p - 1])

    path_taken = []
    visit_a, visit_b = [0] * n, [0] * n

    stack = [index[0]]
    while stack:
        curr = stack.pop()
        # pop parents of the previous node
        while path_taken and curr.parent != path_taken[-1]:
            update(path_taken.pop())
        path_taken.append(curr)        
        if curr.childs:
            stack.extend(curr.childs)
        else:
            curr = path_taken.pop()
            # consider current leaf node
            update(curr)

    # pop parents of the previous node
    while path_taken:
        update(path_taken.pop())

    tot_union = sum(visit_a) + sum(visit_b)
    tot_intersection = sum(a * b for a, b in zip(visit_a, visit_b))

    print("Case #{}: {}".format(test, tot_union / n - tot_intersection / n**2))
