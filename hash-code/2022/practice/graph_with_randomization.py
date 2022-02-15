import random
import sys

from collections import defaultdict


LIKE = 0
DISLIKE = 1
KINDS = [LIKE, DISLIKE]


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}: {string}"


def peprint(string):
    eprint(prefix(string))


def scorer(pizza):
    score = 0
    for pref in prefs:
        if pizza.issuperset(pref[LIKE]) and \
                not pizza.intersection(pref[DISLIKE]):
            score += 1
    return score


# Parse input
nof_clients = int(input())
prefs = [[] for _ in range(nof_clients)]
for i in range(nof_clients):
    for kind in KINDS:
        _, *ingredients = input().split()
        prefs[i].append(ingredients)

# Precompute efficient datastructures to see the effect of an ingredient on
# other clients
who_likes_ingredient = defaultdict(set)
who_dislikes_ingredient = defaultdict(set)
for i, pref in enumerate(prefs):
    for ingredient in pref[LIKE]:
        who_likes_ingredient[ingredient].add(i)
    for ingredient in pref[DISLIKE]:
        who_dislikes_ingredient[ingredient].add(i)

# Represent the clients as a dependency graph
# Two clients have an edge connecting them if the choosing of a client
# precludes the choice of another client
graph = [set() for _ in range(nof_clients)]
for i in range(nof_clients):
    for like in prefs[i][LIKE]:
        graph[i].update(who_dislikes_ingredient[like])
for i in range(nof_clients):
    for dislike in prefs[i][DISLIKE]:
        graph[i].update(who_likes_ingredient[dislike])

# Initialize pizza with ingredients that clients only like 
ingredients = [set() for _ in [LIKE, DISLIKE]]
for kind in KINDS:
    curr_ingredients = ingredients[kind]
    for pref in prefs:
        for ingredient in pref[kind]:
            curr_ingredients.add(ingredient)
pizza = ingredients[LIKE] - ingredients[DISLIKE]

nodes = {i for i in range(nof_clients)}
while nodes:
    # Pick a random node among the ones with lowest degree
    degree = {node:len(graph[node]) for node in nodes}
    min_node = min(degree, key=lambda node: degree[node])
    candidates = [node for node in nodes if degree[node] == degree[min_node]]
    best = random.choice(candidates)
    
    neighbors = list(graph[best])

    # Update pizza with the client's liked ingredients
    pizza.update(prefs[best][LIKE])

    # Drop selected node and its neighbors
    nodes.remove(best)
    nodes.difference_update(neighbors)

    # Drop selected node and its neighbors edges
    for neighbor in neighbors:
        for node in graph[neighbor]:
            graph[node].remove(neighbor)
        graph[neighbor] = set()
    assert graph[best] == set()

# Produce submission
print(len(pizza), " ".join(pizza))

score = scorer(pizza)
peprint(f"{score=}")
