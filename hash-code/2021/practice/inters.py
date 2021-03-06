import sys

from collections import namedtuple


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

# def argmin(pizzas):
#     minimum = float("+inf")
#     idx = -1
#     for candidate in (pizza for pizza in range(nof_pizzas) if available[pizza]):
#         total = set.intersection(*[inters[candidate][pizza] for pizza in pizzas])
#         if minimum > len(total):
#             minimum = len(total)
#             idx = candidate
#     return idx

def argmin(ingredients):
    minimum = float("+inf")
    idx = -1
    for candidate in (pizza for pizza in range(nof_pizzas) if available[pizza]):
        total = len(ingredients & pizzas[candidate].ingredients)
        if minimum > total:
            minimum = total
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
# PROBLEM: requires too much memory
# inters = [[{}] * nof_pizzas for _ in range(nof_pizzas)]
# for i in range(nof_pizzas):
#     # reuse intersections
#     for j in range(i):
#         inters[i][j] = inters[j][i]
#     # compute intersections
#     for j in range(i, nof_pizzas):
#         inters[i][j] = pizzas[i].ingredients & pizzas[j].ingredients

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
            pizza = argmin(merge)
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
    if len(sys.argv) == 1:
        print(f"Pizza n°{pizza} with {len(pizzas[pizza].ingredients)} was not delivered", file=sys.stderr)
    else:
        print(f"{sys.argv[1]}: Pizza n°{pizza} with {len(pizzas[pizza].ingredients)} was not delivered", file=sys.stderr)
    del teams[-1]

# score
score = scorer(teams)
if len(sys.argv) == 1:
    print(f"score = {score}", file=sys.stderr)
else:
    print(f"{sys.argv[1]}: score = {score}", file=sys.stderr)


# produce submission
print(len(teams))
for team in teams:
    members, current_pizzas = team
    print(members, *current_pizzas)
