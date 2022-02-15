# Create a pizza with ingredients that clients only like

LIKE = 0
DISLIKE = 1
KINDS = [LIKE, DISLIKE]

# Parse input
nof_clients = int(input())
prefs = [[] for _ in range(nof_clients)]
for i in range(nof_clients):
    for kind in KINDS:
        _, *ingredients = input().split()
        prefs[i].append(ingredients)

ingredients = [set() for _ in [LIKE, DISLIKE]]
for kind in KINDS:
    curr_ingredients = ingredients[kind]
    for pref in prefs:
        for ingredient in pref[kind]:
            curr_ingredients.add(ingredient)
pizza = ingredients[LIKE] - ingredients[DISLIKE]

print(len(pizza), " ".join(pizza))
