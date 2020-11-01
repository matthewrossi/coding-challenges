# 1 to N rooms in a row
# N-1 locked doors connect the adjacent rooms
# each door has a unique difficulty level

# start room, goes to lower difficulty, if only one locked, opens it
# once a door is unlocked it remains so

# queries: K-th room she visits starting from S-th

import numpy as np

from collections import defaultdict


def prev_higher(array):
    prev = [-1] * len(array)
    stack = []
    for i, item in enumerate(array):
        # remove items lower than current item
        while stack and stack[-1][1] < item:
            stack.pop()
        if stack:
            # save index of closest previous item higher than current item
            prev[i] = stack[-1][0]
        stack.append((i, item))
    return prev


def next_higher(array):
    nxt = [-1] * len(array)
    stack = []
    for i in range(len(array) - 1, -1, -1):
        item = array[i]
        # remove items lower than current item
        while stack and stack[-1][1] < item:
            stack.pop()
        if stack:
            # save index of closest previous item higher than current item
            nxt[i] = stack[-1][0]
        stack.append((i, item))
    return nxt

def subtree_sizes(node):
    for child in childs[node]:
        sizes[node] += subtree_sizes(child)
    return sizes[node]

t = int(input())
for test in range(1, t + 1):
    n, q = map(int, input().split())
    doors = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    left = prev_higher(doors)
    right = next_higher(doors)

    # create adjacency lists
    parent = [-1] * (n - 1)
    childs = defaultdict(list)
    for i in range(n - 1):
        if right[i] == -1 or (left[i] != -1 and doors[left[i]] < doors[right[i]]):
            parent[i] = left[i]
            childs[parent[i]].append(i)
        else:
            parent[i] = right[i]
            childs[parent[i]].append(i)

    # compute subtree sizes
    sizes = [1] * (n - 1)
    subtree_sizes(*childs[-1])

    # TODO: preprocess tree with binary lifting

    answer = []
    for query in queries:
        start, step = query
        if step == 1:
            # don't move
            answer.append(str(start))
        else:
            # open step - 1 doors
            curr_left = start - 2
            curr_right = start - 1
            if curr_right == n - 1 or (curr_left != -1 and doors[curr_left] < doors[curr_right]):
                first_door = curr_left
            else:
                first_door = curr_right

            step = step - 1
            if sizes[first_door] >= step:
                if first_door == curr_left:
                    answer.append(start - step)
                else:
                    answer.append(start + step)
            else:
                current = first_door
                while sizes[current] < step:
                    current = parent[current]
                if first_door < current:
                    left_child = min(childs[current])
                    answer.append(current + 1 + step - sizes[left_child])
                else:
                    right_child = max(childs[current])
                    answer.append(current + 2 - (step - sizes[right_child]))
            
    print("Case #{}: {}".format(test, " ".join(map(str, answer))))
