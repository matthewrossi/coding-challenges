# Start off with a mega pizza with all ingredients (which satisfies people 
# without dislikes), then remove ingredients widely disliked to improve the
# overall score

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


def get_new_clients(ingredient):
    """Get clients who dislike current pizza due to given ingredient.
    
    All clients that have all the ingredients they like in the pizza, but have
    the given ingredient which is the only one they dislike in the current
    pizza.

    Args:
        ingredient (string): name of the ingredient we plan on removing.

    Returns:
        list: list of clients we get by removing the ingredient
    """
    new_client_candidates = who_dislikes_ingredient[ingredient]
    new_clients = [client
                   for client in new_client_candidates
                   if pizza.issuperset(prefs[client][LIKE]) \
                       and pizza.intersection(prefs[client][DISLIKE]) == {ingredient}]
    return new_clients


def get_newly_lost_clients(ingredient):
    """Get clients who would buy the current pizza due to given ingredient.

    Args:
        ingredient (string): name of the ingredient we plan on removing.

    Returns:
        list: list of clients we lose by removing the ingredient
    """
    lost_client_candidates = who_likes_ingredient[ingredient]
    lost_client = [client for client in lost_client_candidates if sold[client]]
    return lost_client


# Parse input
nof_clients = int(input())
prefs = [[] for _ in range(nof_clients)]
for i in range(nof_clients):
    for kind in KINDS:
        _, *ingredients = input().split()
        prefs[i].append(ingredients)

# Precompute efficient datastructures to see the effect of an ingredient change
who_likes_ingredient = defaultdict(set)
who_dislikes_ingredient = defaultdict(set)
for i, pref in enumerate(prefs):
    for ingredient in pref[LIKE]:
        who_likes_ingredient[ingredient].add(i)
    for ingredient in pref[DISLIKE]:
        who_dislikes_ingredient[ingredient].add(i)

# Precompute set of liked and disliked ingredients
ingredients = [set() for _ in [LIKE, DISLIKE]]
for kind in KINDS:
    curr_ingredients = ingredients[kind]
    for pref in prefs:
        curr_ingredients.update(pref[kind])

# Start off with a mega pizza with all liked ingredients
pizza = ingredients[LIKE]

# ...which satisfies all people without dislikes or dislike only bad
# ingredients
bad_ingredients = ingredients[DISLIKE] - ingredients[LIKE]
sold = [bad_ingredients.issuperset(prefs[i][DISLIKE])
        for i in range(nof_clients)]

# Remove ingredients untill we cannot improve the score anymore
nof_removed_ingredients = 0
while True:
    # Find "best" ingredient to remove
    max_score_increment = 0
    ingredient_to_remove = None
    for ingredient in pizza:
        nof_new_clients = len(get_new_clients(ingredient))
        nof_lost_clients = len(get_newly_lost_clients(ingredient))
        score_increment = nof_new_clients - nof_lost_clients
        if score_increment > max_score_increment:
            max_score_increment = score_increment
            ingredient_to_remove = ingredient

    # Does its removal improve our score?
    if not max_score_increment: break

    new_clients = get_new_clients(ingredient_to_remove)
    lost_clients = list(who_likes_ingredient[ingredient_to_remove])

    nof_removed_ingredients += 1

    # Update the pizza removing the selected ingredient
    pizza.remove(ingredient_to_remove)
    # Update sold accoding to clients change
    for client in new_clients:
        sold[client] = True
    for client in lost_clients:
        sold[client] = False

peprint(f"{nof_removed_ingredients=}")

# Score
peprint(f"score = {sum(sold)}")

# Produce submission
print(len(pizza), " ".join(pizza))
