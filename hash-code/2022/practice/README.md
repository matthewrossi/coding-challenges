# Practice round

## Greedy solutions

### [Pizza with free ingredients](no_disliked_ingredients.py)

Create a pizza with all the ingredients none dislikes.

The idea is to avoid losing any people due to their dislike of an ingredient,
however this means we lose many due to some missing ingredients they like.

### [Megapizza with all ingredients people like](all_liked-ingredients.py)

Create a pizza with all the ingredients people likes.

The idea is dual of the previous one, we want to avoid losing any people due
to missing ingredients they like, but this means losing some due to the
ingredients they dislike.

Among the two basic solutions, this proves to be a more successfull starting
point with the given datasets.

### [Remove some megapizza ingredients](reduce_megapizza.py)

Start off with a megapizza with all liked ingredients, then remove ingredients
widely disliked to improve the overall number of clients.

### [Pick clients insted of ingredients](graph.py)

Represent the clients as a dependency graph.
Two clients have an edge connecting them if the choosing of a client precludes
the choice of another client, due to their ingredients incompatibility.
Thanks to this representation, we can build the pizza from the groud up by
picking the liked ingredients of people how have the lowest number of conflicts.

## Randomization

### [Add some randomization to the ingredients removal](reduce_megapizza-with_randomization.py)

Randomize the [Remove some megapizza ingredients](#remove-some-megapizza-ingredientsreducemegapizzapy)
by picking a random ingredient to remove among the ones promising the highest
score increment.

### [Add some randomization to the client selection](graph_with_randomization.py)

Randomize the [Pick clients insted of ingredients](#pick-clients-insted-of-ingredientsgraphpy)
by picking a random client to among the ones with lowest number of
incompatibilities.

### [Improve existing client selection](improve_graph.py)

Improve on previous solutions by keeping half of the selected clients, and
trying to improve on it by using the usual client selection.

### [The more randomization the better](improve_graph_with_randomization.py)

Merge of the above two solutions.

## Scripts

### [Run](run.sh)

Run the given program in parallel over every input data set.

### [Score](score.sh)

Compute the score of the results in parallel over every input data set.

### [Data set analysis](stats.py)

Compute and visualize interesting information about the input data sets. Like:

- number of clients
- clients distribution by #likes and #dislikes
- number of unique ingredients
- number of unique ingredients in likes and dislikes
- #likes and #dislikes by ingredients
- ingredients distribution by #likes and #dislikes
