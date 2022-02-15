#!/usr/bin/env python

import matplotlib.pyplot as plt

from collections import defaultdict


LIKE = 0
DISLIKE = 1
KINDS = [LIKE, DISLIKE]
STRINGS = ["likes", "dislikes"]


# Parse input
nof_clients = int(input())
prefs = [[] for _ in range(nof_clients)]
for i in range(nof_clients):
    for kind in KINDS:
        _, *ingredients = input().split()
        prefs[i].append(ingredients)

print(f"N° clients: {nof_clients}")

# clients = defaultdict(int)
# for pref in prefs: 
#     clients[f"{sorted(pref[LIKE])}{sorted(pref[DISLIKE])}"] += 1
# print(f"N° unique clients: {len(clients)}")
# non_unique_clients = {key:value for key, value in clients.items() if value > 1}
# print(f"Clients with higher frequency: {non_unique_clients}")

# for kind in KINDS:
#     clients = defaultdict(int)
#     for pref in prefs: 
#         clients[f"{sorted(pref[kind])}"] += 1
#     print(f"N° unique clients ({STRINGS[kind]}): {len(clients)}")
#     non_unique_clients = {key:value for key, value in clients.items() if value > 1}
#     print(f"Clients with higher frequency ({STRINGS[kind]}): {non_unique_clients}")

# Client distributions by #prefereces
for kind in KINDS:
    clients_by_pref = defaultdict(int)
    for pref in prefs:
        clients_by_pref[len(pref[kind])] += 1

    min_pref, max_pref = min(clients_by_pref), max(clients_by_pref)
    print(f"\nMinimum number of {STRINGS[kind]}: {min_pref}")
    print(f"Maximum number of {STRINGS[kind]}: {max_pref}")

    #print(f"Client distribution by #{STRINGS[kind]}: {clients_by_pref}")
    plt.bar(clients_by_pref.keys(), clients_by_pref.values())
    # plt.show()
    # plt.savefig(prefix(f"clients_by_{STRINGS[kind]}.png"))

# Ingredients
ingredients = set()
for pref in prefs:
    for kind in KINDS:
        ingredients.update(pref[kind])
print(f"\n\nN° unique ingredients: {len(ingredients)}")

# Prefereces distribution by ingredients
pref_by_ingredients = [defaultdict(int) for _ in [LIKE, DISLIKE]]
for kind in KINDS:
    curr_pref_by_ingredients = pref_by_ingredients[kind]
    for pref in prefs:
            for ingredient in pref[kind]:
                curr_pref_by_ingredients[ingredient] += 1

    print(f"\nN° unique ingredients ({STRINGS[kind]}): {len(curr_pref_by_ingredients)}")
    print(f"N° ingredients only in {STRINGS[1 - kind]}: {len(ingredients) - len(curr_pref_by_ingredients)}")
    
    if curr_pref_by_ingredients:
        rare = min(curr_pref_by_ingredients, key=curr_pref_by_ingredients.get)
        print(f"Most rare ingredient ({STRINGS[kind]}): {rare} with {curr_pref_by_ingredients[rare]} occurancies")
        common = max(curr_pref_by_ingredients, key=curr_pref_by_ingredients.get)
        print(f"Most common ingredient ({STRINGS[kind]}): {common} with {curr_pref_by_ingredients[common]} occurancies")

    #print(f"Preferences distribution by #{STRINGS[kind]}: {curr_pref_by_ingredients}")
    # plt.bar(curr_pref_by_ingredients.keys(), curr_pref_by_ingredients.values())
    # plt.show()
    # plt.savefig(prefix(f"{STRINGS[kind]}_by_ingredients.png"))

# Ingredients distribution by #prefereces
for kind in KINDS:
    ingredients_by_pref = defaultdict(int)
    curr_pref_by_ingredients = pref_by_ingredients[kind]
    for ingredient, pref in curr_pref_by_ingredients.items():
        ingredients_by_pref[pref] += 1
    #print(f"Ingredients distribution by #{STRINGS[kind]}: {curr_pref_by_ingredients}")
    # plt.bar(ingredients_by_pref.keys(), ingredients_by_pref.values())
    # plt.show()
    # plt.savefig(prefix(f"ingredients_by_{STRINGS[kind]}.png"))
