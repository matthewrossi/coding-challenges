import sys
import matplotlib.pyplot as plt

from collections import namedtuple


def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}-{string}"


Pizza = namedtuple("Pizza", ["nof_ingredients", "ingredients"])
Team = namedtuple("Team", ["size", "pizzas"])


# parse input
nof_pizzas, *nof_teams = map(int, input().split())
pizzas = []
for i in range(nof_pizzas):
    nof_ingredients, *ingredients = input().split()
    nof_ingredients = int(nof_ingredients)
    pizzas.append(Pizza(nof_ingredients, set(ingredients)))

print(f"N° pizzas: {nof_pizzas}")

demand = 0
for i in range(3):
    print(f"{nof_teams[i]} teams of {i+2} people")
    demand += (i+2) * nof_teams[i]

print(f"\nTotal demand: {demand}")
if demand > nof_pizzas:
    print(f"We are short on pizzas!!!")

pizza_distribution = {}
for pizza in pizzas:
    pizza_distribution[pizza.nof_ingredients] = pizza_distribution.get(pizza.nof_ingredients, 0) + 1

min_pizza, max_pizza = min(pizzas), max(pizzas)
print(f"\nSmallest pizza has {len(min_pizza.ingredients)} ingredients")
print(f"Biggest pizza has {len(max_pizza.ingredients)} ingredients")

print(f"Pizza distribution on #ingredients: {pizza_distribution}")
plt.bar(pizza_distribution.keys(), pizza_distribution.values())
plt.show()
# plt.savefig(prefix('pizza_by_ingredients.png'))

nof_ingredients = 0
for pizza in pizzas:
    nof_ingredients += pizza.nof_ingredients
print(f"\nTotal number of ingredients: {nof_ingredients}")

ingredients = {}
for pizza in pizzas:
    for ingredient in pizza.ingredients:
        ingredients[ingredient] = ingredients.get(ingredient, 0) + 1
print(f"N° unique ingredients: {len(ingredients)}")

rare = min(ingredients, key=ingredients.get)
print(f"\nMost rare ingredient: {rare} with {ingredients[rare]} occurancies")
common = max(ingredients, key=ingredients.get)
print(f"Most common ingredient: {common} with {ingredients[common]} occurancies")

print(f"Ingredients frequency: {ingredients}")
plt.bar(ingredients.keys(), ingredients.values())
plt.show()
# plt.savefig(prefix('ingredients_freq.png'))

ingredients_by_freq = {}
for ingredient, freq in ingredients.items():
    ingredients_by_freq[freq] = ingredients_by_freq.get(freq, 0) + 1
plt.bar(ingredients_by_freq.keys(), ingredients_by_freq.values())
plt.show()
# plt.savefig(prefix('ingredients_by_freq.png'))
