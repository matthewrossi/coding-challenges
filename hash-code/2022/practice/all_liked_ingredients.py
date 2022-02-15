# Create a pizza with all liked ingredients

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

# Create a mega pizza with all liked ingredients
pizza = set()
for pref in prefs:
    pizza.update(pref[LIKE])
print(len(pizza), " ".join(pizza))
