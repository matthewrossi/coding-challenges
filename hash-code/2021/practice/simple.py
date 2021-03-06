import sys

def team_score(team):
    _, current_pizzas = team
    ingredients = set()
    for current_pizza in current_pizzas:
        _, current_ingredients = pizzas[current_pizza]
        ingredients.update(current_ingredients)
    return len(ingredients)**2

def scorer(teams):
    score = 0
    for team in teams:
        score += team_score(team)
    return score

nof_pizzas, *nof_teams = map(int, input().split())
pizzas = []
for i in range(nof_pizzas):
    nof_ingredients, *ingredients = input().split()
    nof_ingredients = int(nof_ingredients)
    pizzas.append((nof_ingredients, set(ingredients)))

order = [i for i in range(nof_pizzas)]
order.sort(key=lambda idx: pizzas[idx][0], reverse=True)

idx = 0
teams = []
for kind in range(2, -1, -1):
    left = nof_teams[kind]
    members = kind + 2
    while(left > 0 and nof_pizzas - idx >= members):
        team = (members, [order[idx + offset] for offset in range(members)])
        teams.append(team)
        idx += members
        left -= 1

score = scorer(teams)
print(f"score = {score}", file=sys.stderr)

print(len(teams))
for team in teams:
    members, current_pizzas = team
    print(members, *current_pizzas)
