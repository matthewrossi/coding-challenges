import sys

from collections import namedtuple


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}: {string}"

def peprint(string):
    eprint(prefix(string))


Pizza = namedtuple("Pizza", ["nof_ingredients", "ingredients"])
Team = namedtuple("Team", ["size", "pizzas"])


def scorer(teams):
    score = 0
    for team in teams:
        ingredients = set()
        for pizza in team.pizzas:
            ingredients.update(pizzas[pizza].ingredients)
        score += len(ingredients)**2
    return score

def argmax(ingredients):
    idx = maximum = -1
    for candidate in (pizza for pizza in range(nof_pizzas) if available[pizza]):
        #inter = ingredients & pizzas[candidate].ingredients
        total = len(ingredients ^ pizzas[candidate].ingredients)**2 / (len(ingredients) + len(pizzas[candidate].ingredients))
        if maximum < total:
            maximum = total
            idx = candidate
    return idx

# parse input
nof_pizzas, *nof_teams = map(int, input().split())
pizzas = []
for i in range(nof_pizzas):
    nof_ingredients, *ingredients = input().split()
    nof_ingredients = int(nof_ingredients)
    pizzas.append(Pizza(nof_ingredients, set(ingredients)))

available = [True] * nof_pizzas

order = [i for i in range(nof_pizzas)]
order.sort(key=lambda idx: pizzas[idx][0], reverse=True)

idx = 0
teams = []
for kind in range(2, -1, -1):
    left = nof_teams[kind]
    members = kind + 2
    while(left > 0 and nof_pizzas - idx >= members):
        pizza = order[idx]
        team_pizzas = [pizza]
        available[pizza] = False
        merge = set()
        for offset in range(members - 1):
            merge.update(pizzas[pizza].ingredients)
            pizza = argmax(merge)
            team_pizzas.append(pizza)
            available[pizza] = False
        teams.append(Team(members, team_pizzas))
        left -= 1
        # skip pizzas already delivered
        while idx < nof_pizzas and not available[order[idx]]:
            idx += 1

# remove last team when no pizza was available
if -1 in teams[-1].pizzas:
    team_pizzas = teams[-1].pizzas
    pizza = team_pizzas[0]
    peprint(f"Pizza n°{pizza} with {len(pizzas[pizza].ingredients)} ingredients was not delivered")
    del teams[-1]

# score
score = scorer(teams)
peprint(f"score = {score}")

# produce submission
print(len(teams))
for team in teams:
    members, current_pizzas = team
    print(members, *current_pizzas)
