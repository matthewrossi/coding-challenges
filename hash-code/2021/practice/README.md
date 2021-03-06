# Practice round

## Greedy solutions

### Simple

Sort pizzas on decreasing number of ingredients and assign them to the teams
starting from the ones with more members.

### Minimize intersections

Sort pizzas on decreasing number of ingredients and assign them to the teams
starting from the ones with more members. Choose the next team pizza by
minimizing the ingredients intersection.

### Maximize symmetric difference

Sort pizzas on decreasing number of ingredients and assign them to the teams
starting from the ones with more members. Choose the next team pizza by
maximizing the symmetric difference among ingredients.

NOTE: The symmetric difference of two sets A and B is the set of elements that
are in either A or B, but not in their intersection.

### Maximize score by union

Sort pizzas on decreasing number of ingredients and assign them to the teams
starting from the ones with more members. Choose the next team pizzas by
maximizing the score per ingredient in the union of ingredients.

### Maximize score by sum

Sort pizzas on decreasing number of ingredients and assign them to the teams
starting from the ones with more members. Choose the next team pizzas by
maximizing the score per ingredient.

## Randomization

Swap random pizzas among random pairs of teams when it improves the score.

## Data sets analysis

Compute and visualize interesting information about the input data sets. Like:

- number of pizzas available and the actual teams demand
- pizzas distribution by number of ingredients
- total number of ingredients and number of unique ingredients
- number of pizzas containing each ingredient
- ingredients distribution by number of pizzas containing them

## Scripts

### [script.sh](script.sh)

Run the given program in parallel over every input data set.

### [randomize.sh](randomize.sh)

Run multiple repetitions of [randomize.py](randomize.py) over the given input
data set improving on the previous step output.

## Score

![score](https://user-images.githubusercontent.com/15113769/110214042-06930700-7ea3-11eb-9824-19fb087a4506.png)
