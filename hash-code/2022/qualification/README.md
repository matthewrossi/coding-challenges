# Qualification round

## Greedy solutions

### [Basic - schedule projects whenever possible](run.py)

Sort projects by a given heuristic, pick projects we can satisfy by following
this order.
We can satisfy a given project everytime there are enough contributors with
the necessary skills.

### [Wait - consider waiting before scheduling](wait2schedule.py)

Similar, to the basic solution, but consider keeping some contributors
waiting to then schedule better projects.

## Scripts

### [Run](run.sh)

Run the given program in parallel over every input data set.

### [Data set analysis](stats.py)

Compute and visualize interesting information about the input data sets. Like:

- number of contributors
- number of unique skills
- contributors distribution by #skills
- contributors distribution by skill
- number of projects
- projects distribution by score
- projects distribution by soft deadline
- projects distribution by #roles
- projects distribution by role

You can run it in parallel on all input data sets by using
[stats.sh](stats.sh).
