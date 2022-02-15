import random
import sys

from collections import defaultdict


LIKE = 0
DISLIKE = 1
KINDS = [LIKE, DISLIKE]


def current_clients(pizza):
    return {client
            for client, pref in enumerate(prefs)
            if pizza.issuperset(pref[LIKE]) and \
                not pizza.intersection(pref[DISLIKE])}


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

# Find ingredients that clients only like
ingredients = [set() for _ in [LIKE, DISLIKE]]
for kind in KINDS:
    curr_ingredients = ingredients[kind]
    for pref in prefs:
        for ingredient in pref[kind]:
            curr_ingredients.add(ingredient)
free_ingredients = ingredients[LIKE] - ingredients[DISLIKE]

# Parse and evaluate previous result
pizza = []
with open(sys.argv[1], 'r') as prev:
    line = prev.readline()
    _, *pizza = line.split()
pizza = set(pizza)
clients = current_clients(pizza)
score = len(clients)

for i in range(1000):
    # Keep half of the current clients
    to_keep = set(random.sample(clients, len(clients) // 2))
    
    # Init new pizza with ingredients of the clients to keep and free
    # ingredients
    new_pizza = set(free_ingredients)
    for client in to_keep:
        new_pizza.update(prefs[client][LIKE])

    # Find list of remaining eligible clients
    nodes = {i for i in range(nof_clients)}
    for node in to_keep:
        nodes.remove(node)
        nodes.difference_update(graph[node])

    # Build a dependency graph of the remaining eligible clients
    new_graph = [set() for _ in range(nof_clients)]
    for i in nodes:
        for like in prefs[i][LIKE]:
            new_graph[i].update(who_dislikes_ingredient[like])
            new_graph[i].intersection_update(nodes)
    for i in nodes:
        for dislike in prefs[i][DISLIKE]:
            new_graph[i].update(who_likes_ingredient[dislike])
            new_graph[i].intersection_update(nodes)

    # Find the best solution given the fixed half
    to_add = set()
    while nodes:
        # Pick node with lowest degree
        min_degree = float("+inf")
        best = None
        for node in nodes:
            if len(new_graph[node]) < min_degree:
                min_degree = len(new_graph[node])
                best = node
        
        neighbors = list(new_graph[best])

        # Update set of clients satisfied by the current pizza
        to_add.add(best)
        # Update pizza with the client's liked ingredients
        new_pizza.update(prefs[best][LIKE])

        # Drop selected node and its neighbors
        nodes.remove(best)
        nodes.difference_update(neighbors)

        # Drop selected node and its neighbors edges
        for neighbor in neighbors:
            for node in new_graph[neighbor]:
                new_graph[node].remove(neighbor)
            new_graph[neighbor] = set()
        assert new_graph[best] == set()

    new_clients = to_keep | to_add
    new_score = len(new_clients)

    # Keep change if it improves the score
    if new_score >= score:
        pizza = new_pizza
        clients = new_clients
        score = new_score

# Score
print(f"{score=}", file=sys.stderr)

# Produce submission
print(len(pizza), " ".join(pizza))
