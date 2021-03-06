import random
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

teams = []
with open(sys.argv[1], 'r') as prev:
    line = prev.readline()
    for team in prev:
        members, *current_pizzas = map(int, team.split())
        teams.append((members, current_pizzas))

# random change pizzas among teams
for _ in range(100000):
    i = random.randint(0, len(teams) - 1)
    j = random.randint(0, len(teams) - 1)

    before = team_score(teams[i]) + team_score(teams[j])

    members_i, pizzas_i = teams[i]
    members_j, pizzas_j = teams[j]
    pi = random.randint(0, members_i - 1)
    pj = random.randint(0, members_j - 1)

    pizzas_i[pi], pizzas_j[pj] = pizzas_j[pj], pizzas_i[pi]
    
    after = team_score(teams[i]) + team_score(teams[j])

    if after < before:
        pizzas_i[pi], pizzas_j[pj] = pizzas_j[pj], pizzas_i[pi]

score = scorer(teams)
print(f"score = {score}", file=sys.stderr)

print(len(teams))
for team in teams:
    members, current_pizzas = team
    print(members, *current_pizzas)
