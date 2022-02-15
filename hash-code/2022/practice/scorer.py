import sys

LIKE = 0
DISLIKE = 1
KINDS = [LIKE, DISLIKE]


def prefix(string):
    return string if len(sys.argv) == 2 else f"{sys.argv[2]}: {string}"


def pprint(string):
    print(prefix(string))


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

# Parse result
pizza = []
with open(sys.argv[1], 'r') as prev:
    line = prev.readline()
    _, *pizza = line.split()
pizza = set(pizza)

score = scorer(pizza)
pprint(f"{score=}")
